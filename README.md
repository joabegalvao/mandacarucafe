# Mandacaru Café

Landing page de uma página para o Mandacaru Café, em Maringá PR: café da manhã, almoço e, à noite, a pizzaria Jacaré Vermelho. Site estático (HTML, CSS e JavaScript puros), sem build, sem dependências em tempo de execução. Abra `index.html` ou sirva a pasta com qualquer servidor estático (`python3 -m http.server 4197`).

## Dados do cliente

| Campo | Valor |
| --- | --- |
| Nome | Mandacaru Café |
| Segmento | Café: café da manhã, almoço e pizza no jantar |
| Público | Homens e mulheres |
| WhatsApp | (44) 3346-8445, `https://wa.me/554433468445` |
| Instagram | [@mandacarucafe.oficial](https://www.instagram.com/mandacarucafe.oficial/) |
| Endereço | Av. Mandacaru, 695, Vila Santa Izabel, Maringá PR, CEP 87080-000 |
| Horários | Café todos os dias das 8h30 às 19h; almoço das 11h às 15h; Jacaré Vermelho (pizza) todos os dias das 19h à 0h |
| Nota no Google | 4,7 em 488 avaliações (igual ao briefing, conferida em 05/10/2026) |
| E-mail, cardápio, preços, reservas | Não informados |

O briefing trouxe o bairro como "Vl"; o Google completa **Vila Santa Izabel** e o CEP.

### Conferido no Google (05/10/2026)

Busca "Mandacaru Café, Av. Mandacaru, 695, Maringá PR" no Maps: ficha **Mandacaru Café**, Av. Mandacaru, 695, Vila Santa Izabel, Maringá, 87080-000, **4,7 em 488 avaliações**. Bate com o briefing. A busca "Jacaré Vermelho pizzaria Maringá" mostra várias unidades da pizzaria na cidade, entre elas "Jacaré Vermelho Mandacaru", o que confirma a pizza no mesmo endereço à noite.

### Avaliações (texto original, sem edição)

- **Aléxia Palú:** "O ambiente é muito lindo!! Atendimento e comidas também foram ótimas."
- **Cláudia Tupan:** "Amei o Mandacaru Café! O ambiente é super aconchegante, dá vontade de ficar horas. O atendimento é maravilhoso, todo mundo muito atencioso."
- **Isabelle Bulla:** "Avaliando após minha segunda visita! Ambiente lindo, atendimento atencioso, comidas muito saborosas!!! As opções do cardápio são maravilhosas e a vitrine de doces é de encher os olhos e a barriga!!!!"

Trechos das avaliações aparecem também na seção "A casa" (Cláudia) e no texto de "Cozinha e balcão" (Isabelle). Não vieram fotos de perfil; aparece só o nome.

## Síntese estratégica

| Definição | Decisão |
| --- | --- |
| Proposta de valor | Um café com jardim dentro, aberto o dia inteiro: café da manhã, almoço, tarde de café e pizza à noite, todos os dias |
| Principal objeção | "É só um café ou dá para almoçar e jantar? Que horas abre e fecha?" |
| Conversão prioritária | WhatsApp, com três mensagens (saber mais, cardápio, pizza da noite) |
| Direção visual | As cores da própria casa: amarelo das paredes, vinho do teto, verde das plantas e do mármore, laranja e azul do logo; janelas redondas como motivo |

## Direção visual

Pedido: "o melhor feito até agora, bem temático, aconchegante, com áreas verdes e cores bonitas".

- **Cores**, todas medidas no logo e nas fotos: laranja `#b04010` e azul `#004090` do logo; amarelo mostarda `#e9b84c` das paredes (fundo da seção "Um dia no Mandacaru"); vinho `#5b1f2b` do teto (seção da pizza à noite, fecho e rodapé); verde `#3d6b4e` das plantas e do mármore (rótulos, folha, ícones de contato); caramelo `#a8552a` do couro (contornos); creme `#fbf4e6` como papel. O laranja escurecido `#8a3009` garante contraste AA sobre o amarelo.
- **Fontes**: **Young Serif** nos títulos (serifa macia, de café de bairro) e **Plus Jakarta Sans** no texto e rótulos (geométrica arredondada, como o letreiro do logo). Arquivos locais em `assets/fonts`, subconjunto latino.
- **Motivo**: as janelas redondas do café. A "escotilha" com o cafezinho sobreposta à foto do salão no hero, as horas em pílulas, o relógio em disco na seção da noite, a nota 4,7 em um disco amarelo. Cantos arredondados nas fotos, botões em pílula.
- **Hero**: dois painéis. Texto no creme à esquerda; o salão (foto 1461 px) ocupando a metade direita até a borda da tela, com a janela redonda do café sobreposta. No celular a foto vem primeiro.
- **Um dia no Mandacaru**: quatro momentos (8h30, 11h, 15h, 19h) ligados por uma linha pontilhada; as quatro fotos são da própria casa e trazem a etiqueta de horário que ela mesma publicou (08h, 12h, 15h, 19h), o que reforça a narrativa. No celular a fileira desliza na horizontal.
- Sem degradê, sombra ou efeito de vidro. Ícones em SVG inline; a folha foi desenhada para o projeto.

## Estrutura

Cabeçalho → Hero → Um dia no Mandacaru → A casa (texto, citação, 3 fotos) → Cozinha e balcão (8 fotos em mosaico) → Pizza à noite (relógio 19h à 0h, Jacaré Vermelho) → Avaliações (4,7 em disco, 3 depoimentos) → Horários e endereço (tabela, contatos, mapa) → Fecho → Rodapé. Botão flutuante de WhatsApp.

## Imagens

Todas vêm de `materiais-de-origem/` e são geradas por `tools/optimize-images.py` (Pillow), em 480, 640, 800, 1200 px e no tamanho original; nenhuma é ampliada.

| Arquivo em `assets/img` | Origem | Uso |
| --- | --- | --- |
| `salao-*` | `imagem-01.png` (1461x1076) | Hero e compartilhamento |
| `mezanino-*` | `imagem-02.png` (1091x1442) | A casa |
| `fachada-toldo-*`, `fachada-esquina-*` | `imagem-03.png`, `imagem-04.png` | A casa |
| `manha-torrada-*`, `almoco-prato-*`, `tarde-cafe-*`, `noite-pizza-*` | capturas 151425, 151434, 151444, 151453 (711x895) | Um dia no Mandacaru (com as etiquetas 08h, 12h, 15h, 19h da casa) |
| `latte-croissant-*` | captura 151320 (742x889) | Janela redonda do hero e compartilhamento |
| `frappe-*`, `sanduiche-*`, `bolo-chocolate-*`, `tabua-vinho-*`, `torrada-beterraba-*`, `cafe-coado-*`, `sanduiche-cafe-*`, `barista-*` | demais capturas (445 a 717 px) | Cozinha e balcão |
| `logo-mandacaru-{320,480,720}` | `logo/Logo.png` (2170x725, transparente) | Cabeçalho, rodapé (sobre chapa creme), compartilhamento |
| `favicon-32`, `apple-touch-icon`, `icon-192` | o "m" do logo sobre creme | Ícones |
| `compartilhamento.jpg` | montagem 1200x630 | Open Graph / WhatsApp (`node tools/render-compartilhamento.js`) |

As capturas do Instagram têm 3 px de borda, cortados. As quatro fotos do dia trazem a etiqueta de hora sobreposta, publicada pela própria casa; foram mantidas porque coincidem com os horários do briefing.

## Links e mensagens

| Onde | Destino |
| --- | --- |
| WhatsApp (cabeçalho, hero, contatos, fecho, rodapé, botão flutuante) | "Olá! Vi o site do Mandacaru Café e quero saber mais." |
| Pedir o cardápio | "Olá! Vi o site do Mandacaru Café e quero ver o cardápio." |
| Perguntar sobre a pizza | "Olá! Vi o site do Mandacaru Café e quero saber sobre a pizza da noite." |
| Instagram | https://www.instagram.com/mandacarucafe.oficial/ |
| Endereço, Abrir no Google Maps, Como chegar | `https://www.google.com/maps/search/?api=1&query=Mandacaru+Café, Av. Mandacaru, 695, Maringá PR` |

## Decisões

- Os textos descrevem o que as fotos mostram (pão na chapa, prato do almoço, café coado, doces de vitrine, pizza) sem inventar cardápio nem preços; o cardápio completo é pedido pelo WhatsApp.
- "Jacaré Vermelho" aparece como a pizzaria que ocupa a casa à noite, conforme o briefing e a ficha do Google; não há afirmação sobre sabores ou delivery.
- Reservas não foram confirmadas; o texto fala em "mesas em grupo ou dúvidas, chame no WhatsApp".
- O logo (laranja e azul) fica sobre creme no cabeçalho e sobre uma chapa creme no rodapé vinho.
- Sem JS tudo aparece; o menu fica aberto e o botão de menu some.

## Testes (05/10/2026, Chromium via Playwright)

41 verificações aprovadas: sem rolagem horizontal de 320 a 1920 px; título do hero em 2 linhas no desktop e 2 a 3 no celular; contraste AA em todos os textos (incluindo laranja escuro sobre amarelo e mostarda sobre vinho); menu no celular (abre, Esc fecha, foco volta, toques ≥ 48 px); teclado e link de pular; sem JS; movimento reduzido; carga inicial no celular de 379 KB (as 877 KB de fotos abaixo da dobra são `loading="lazy"` e entram só ao rolar); nenhuma imagem exibida acima do tamanho original em 390 e 1920 px; dados estruturados `CafeOrCoffeeShop` com horários e `aggregateRating`.

Nota sobre a medição: o Chromium sem rede real baixa todas as imagens lazy de uma vez, por isso o teste separa o que é inicial do que é lazy.

## Pendências

- Cardápio, preços e se há reservas: a casa pode informar para a página mostrar.
- Fotos de perfil das avaliações, se autorizadas.
- Publicar e apontar o domínio; trocar `og:image` por URL absoluta quando houver domínio.

## Estrutura de arquivos

```
index.html
assets/css/styles.css
assets/js/main.js
assets/fonts/      Young Serif e Plus Jakarta Sans (woff2, subconjunto latino)
assets/img/        imagens otimizadas (geradas)
tools/optimize-images.py
tools/render-compartilhamento.js
materiais-de-origem/   originais do cliente (fora do git)
```

## Repositório

- GitHub: `git@github.com:joabegalvao/mandacarucafe.git` (branch `main`)
- Portfólio: publicado também em `gostoudosite.com.br/mandacarucafe/` (o Dockerfile do gostoudosite clona este repositório na pasta `mandacarucafe`)
- Os originais do cliente ficam só na pasta local `materiais-de-origem/`, fora do git
