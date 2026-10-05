#!/usr/bin/env node
/* Monta a imagem de compartilhamento (1200x630) com o Chromium, usando as
   fontes do site e as imagens geradas por tools/optimize-images.py (os
   ícones também saem de lá, a partir do "m" do logo).

   Uso (na raiz do projeto), com o Playwright instalado:
     node tools/render-compartilhamento.js

   Variáveis opcionais: PLAYWRIGHT_MODULE (caminho do módulo playwright) e
   CHROMIUM_PATH (executável do Chromium). */
const path = require('path');
const fs = require('fs');
const os = require('os');

const playwrightModule = process.env.PLAYWRIGHT_MODULE || 'playwright';
const { chromium } = require(playwrightModule);

const root = path.resolve(__dirname, '..');
const out = path.join(root, 'assets/img');

const fontFace = (family, file) => `@font-face { font-family: "${family}"; src: url("file://${path.join(root, 'assets/fonts', file)}") format("woff2"); font-weight: 300 800; }`;
const fonts = [fontFace('Young Serif', 'young-serif-normal-latin.woff2'), fontFace('Plus Jakarta Sans', 'plus-jakarta-sans-normal-latin.woff2')].join('\n');

const CREAM = '#fbf4e6', ORANGE = '#b04010', ORANGE7 = '#8a3009', INK = '#2b1b15', GREEN = '#2e5440', SOFT = '#6a584f';

const html = `<div style="width:1200px;height:630px;display:grid;grid-template-columns:600px 600px;background:${CREAM};color:${INK};font-family:'Plus Jakarta Sans',sans-serif;overflow:hidden">
  <div style="display:flex;flex-direction:column;justify-content:center;padding:0 64px">
    <img src="file://${path.join(out, 'logo-mandacaru-480.png')}" style="width:220px;height:auto" alt="">
    <div style="margin-top:40px;display:flex;align-items:center;gap:10px;font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:${GREEN}">Café em Maringá, PR <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:${ORANGE}"></span> Todos os dias</div>
    <div style="margin-top:16px;font-family:'Young Serif',serif;font-size:56px;line-height:1.05;letter-spacing:-.01em">Um café com<br><span style="color:${ORANGE}">jardim dentro.</span></div>
    <div style="margin-top:22px;font-size:19px;line-height:1.45;color:${SOFT}">Café da manhã, almoço e, à noite,<br>a pizza da Jacaré Vermelho.<br>Av. Mandacaru, 695. Nota 4,7 no Google.</div>
  </div>
  <div style="position:relative">
    <img src="file://${path.join(out, 'salao-1461.jpg')}" style="position:absolute;inset:0;width:600px;height:630px;object-fit:cover;object-position:55% 50%" alt="">
    <div style="position:absolute;left:-90px;bottom:60px;width:200px;height:200px;border:8px solid ${CREAM};border-radius:50%;overflow:hidden;background:${CREAM}"><img src="file://${path.join(out, 'latte-croissant-736.jpg')}" style="width:100%;height:100%;object-fit:cover;object-position:50% 40%" alt=""></div>
  </div>
</div>`;

(async () => {
  const browser = await chromium.launch(
    process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}
  );
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  // a página é aberta por file:// para o Chromium aceitar as fontes e as fotos locais
  const tmp = path.join(os.tmpdir(), 'mandacaru-render.html');
  fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${fonts} body{margin:0;background:transparent}</style></head><body>${html}</body></html>`);
  await page.goto('file://' + tmp, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(out, 'compartilhamento.jpg'), type: 'jpeg', quality: 86 });
  fs.unlinkSync(tmp);
  await browser.close();
  console.log('assets/img/compartilhamento.jpg');
})();
