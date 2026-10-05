#!/usr/bin/env python3
"""Gera as imagens otimizadas da landing page a partir dos arquivos originais.

Uso (na raiz do projeto):
    python3 tools/optimize-images.py

Requer Pillow (pip install pillow) e a pasta materiais-de-origem/. Os
originais nunca são alterados. Para trocar uma foto, substitua o arquivo de
origem ou edite a lista PHOTOS e rode o script novamente.

A imagem de compartilhamento (1200x630) é montada pelo Chromium, com as
fontes do site, por outro script:
    node tools/render-compartilhamento.js
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "materiais-de-origem"
SRC = SOURCES / "fotos"
LOGO_SRC = SOURCES / "logo" / "Logo.png"
OUT = ROOT / "assets" / "img"

CREAM = (251, 244, 230)  # #fbf4e6, fundo da página

# Nada é ampliado: a maior versão gerada é a do original.
WIDTHS = (480, 640, 800, 1200)

# nome de saída -> (arquivo em materiais-de-origem/fotos, área usada ou None)
# A área é (esquerda, topo, direita, base) em pixels do original. As capturas
# do Instagram levam 3 px de borda fora.
PHOTOS = {
    # a casa
    "salao": ("imagem-01.png", None),
    "mezanino": ("imagem-02.png", None),
    "fachada-toldo": ("imagem-03.png", None),
    "fachada-esquina": ("imagem-04.png", None),
    # um dia no Mandacaru (as quatro fotos trazem a etiqueta de horário
    # publicada pela própria casa: 08h, 12h, 15h, 19h)
    "manha-torrada": ("Screenshot 2026-10-05 151425.png", (3, 3, 708, 892)),
    "almoco-prato": ("Screenshot 2026-10-05 151434.png", (3, 3, 708, 890)),
    "tarde-cafe": ("Screenshot 2026-10-05 151444.png", (3, 3, 709, 889)),
    "noite-pizza": ("Screenshot 2026-10-05 151453.png", (3, 3, 710, 892)),
    # da cozinha e do balcão
    "latte-croissant": ("Screenshot 2026-10-05 151320.png", (3, 3, 739, 886)),
    "frappe": ("Screenshot 2026-10-05 151339.png", (3, 3, 711, 890)),
    "sanduiche": ("Screenshot 2026-10-05 151357.png", (3, 3, 711, 887)),
    "sanduiche-cafe": ("Screenshot 2026-10-05 151503.png", (3, 3, 666, 891)),
    "barista": ("Screenshot 2026-10-05 151518.png", (3, 3, 665, 889)),
    "torrada-beterraba": ("Screenshot 2026-10-05 151535.png", (3, 3, 710, 888)),
    "bolo-chocolate": ("Screenshot 2026-10-05 151549.png", (3, 3, 714, 883)),
    "cafe-coado": ("Screenshot 2026-10-05 151104.png", (3, 3, 442, 591)),
    "tabua-vinho": ("Screenshot 2026-10-05 151251.png", (3, 3, 470, 590)),
}


def resize_to_width(im: Image.Image, width: int) -> Image.Image:
    if im.width <= width:
        return im.copy()
    height = round(im.height * width / im.width)
    return im.resize((width, height), Image.LANCZOS)


def save_set(im: Image.Image, name: str) -> None:
    for width in WIDTHS:
        if width < im.width:
            resize_to_width(im, width).save(OUT / f"{name}-{width}.webp", "WEBP", quality=78, method=6)
    im.save(OUT / f"{name}-{im.width}.webp", "WEBP", quality=78, method=6)
    # fallback JPEG para navegadores sem WebP
    im.save(OUT / f"{name}-{im.width}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
    print(f"{name}: {im.width}x{im.height}")


def build_photos() -> None:
    for name, (source, area) in PHOTOS.items():
        im = Image.open(SRC / source).convert("RGB")
        save_set(im.crop(area) if area else im, name)


def build_logo() -> None:
    """Logo em PNG transparente (2170x725, laranja e azul). Só recorta a
    margem vazia e gera os tamanhos usados."""
    logo = Image.open(LOGO_SRC).convert("RGBA")
    box = logo.getchannel("A").getbbox()
    m = 10
    logo = logo.crop((max(0, box[0] - m), max(0, box[1] - m), min(logo.width, box[2] + m), min(logo.height, box[3] + m)))
    for width in (720, 480, 320):
        out = resize_to_width(logo, width)
        out.save(OUT / f"logo-mandacaru-{width}.png", optimize=True)
        out.save(OUT / f"logo-mandacaru-{width}.webp", "WEBP", quality=90, method=6)
    print(f"logo-mandacaru: {logo.width}x{logo.height} (salvo em 720, 480 e 320)")

    # Ícones: só o "m" inicial do logo, sobre o creme (o nome inteiro não
    # cabe em 32 px). Área do "m" medida no logo recortado.
    m_box = (0, 0, round(logo.width * 0.172), logo.height)
    letter = logo.crop(m_box)
    lb = letter.getchannel("A").getbbox()
    letter = letter.crop(lb)
    for name, size in (("favicon-32", 32), ("apple-touch-icon", 180), ("icon-192", 192)):
        tile = Image.new("RGBA", (512, 512), CREAM + (255,))
        fitted = letter.resize((400, round(letter.height * 400 / letter.width)), Image.LANCZOS)
        tile.alpha_composite(fitted, ((512 - fitted.width) // 2, (512 - fitted.height) // 2))
        tile.convert("RGB").resize((size, size), Image.LANCZOS).save(OUT / f"{name}.png", optimize=True)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_photos()
    build_logo()
    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"{len(list(OUT.iterdir()))} arquivos, {total / 1024:.0f} KB no total")
