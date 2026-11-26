// Mapa do percurso: três direções, módulo atual destacado. Uso: node mapa_img.js <modulo> <saida.png>
const sharp = require('sharp');
const cur = parseInt(process.argv[2], 10);
const out = process.argv[3];
const NOT = '#082A45', EST = '#245E78', OURO = '#C99A64', BEGE = '#F4EFEA', CARD = '#FBF8F4', LINHA = '#E2D8CC', MUTED = '#5A6B74';
const dirs = [
  { nome: 'Traduzir', mods: [1, 2], sub: 'fundamentos e prática' },
  { nome: 'Ganhar eixo e presença', mods: [3, 4, 5, 6], sub: 'corpo, emoções, escolha e cultivo' },
  { nome: 'Ocupar o próprio espaço', mods: [7, 8], sub: 'relação, expressão e continuidade' },
];
const W = 1600, H = 570;
const x0 = 150, bw = 420, gap = 70, by = 150, bh = 170;
let s = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
<rect width="${W}" height="${H}" fill="${BEGE}"/>
<text x="60" y="78" font-family="EB Garamond, Georgia, serif" font-size="46" fill="${NOT}">Mapa do percurso</text>
<text x="${W - 60}" y="78" text-anchor="end" font-family="Inter, Arial, sans-serif" font-size="22" fill="${MUTED}">Você está no Módulo ${cur}</text>
<line x1="60" y1="100" x2="130" y2="100" stroke="${OURO}" stroke-width="3"/>`;
// M0
s += `<circle cx="80" cy="${by + bh / 2}" r="34" fill="${CARD}" stroke="${LINHA}" stroke-width="2"/>
<text x="80" y="${by + bh / 2 + 8}" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="22" fill="${MUTED}">M0</text>
<text x="80" y="${by + bh / 2 + 62}" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="17" fill="${MUTED}">entrada</text>`;
dirs.forEach((d, i) => {
  const x = x0 + i * (bw + gap);
  const ativo = d.mods.includes(cur);
  const fill = ativo ? EST : CARD, tc = ativo ? '#FFFFFF' : NOT, sc = ativo ? BEGE : MUTED;
  s += `<rect x="${x}" y="${by}" width="${bw}" height="${bh}" rx="22" fill="${fill}" stroke="${ativo ? EST : LINHA}" stroke-width="2"/>
<text x="${x + 30}" y="${by + 46}" font-family="Inter, Arial, sans-serif" font-size="16" font-weight="700" letter-spacing="2" fill="${ativo ? OURO : OURO}">${['1', '2', '3'][i]} · DIREÇÃO</text>
<text x="${x + 30}" y="${by + 96}" font-family="EB Garamond, Georgia, serif" font-size="${d.nome.length > 20 ? 34 : 40}" fill="${tc}">${d.nome}</text>
<text x="${x + 30}" y="${by + 136}" font-family="Inter, Arial, sans-serif" font-size="19" fill="${sc}">${d.sub}</text>`;
  // chips de módulos
  const cw = 74, cg = 14, tot = d.mods.length * cw + (d.mods.length - 1) * cg;
  d.mods.forEach((m, j) => {
    const cx = x + (bw - tot) / 2 + j * (cw + cg);
    const on = m === cur;
    s += `<rect x="${cx}" y="${by + bh + 26}" width="${cw}" height="46" rx="23" fill="${on ? OURO : CARD}" stroke="${on ? OURO : LINHA}" stroke-width="2"/>
<text x="${cx + cw / 2}" y="${by + bh + 57}" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="21" font-weight="${on ? 700 : 400}" fill="${on ? NOT : MUTED}">M${m}</text>`;
  });
  if (i < 2) {
    const ax = x + bw + 14, ay = by + bh / 2;
    s += `<path d="M ${ax} ${ay} L ${ax + gap - 28} ${ay}" stroke="${OURO}" stroke-width="4"/>
<path d="M ${ax + gap - 34} ${ay - 12} L ${ax + gap - 20} ${ay} L ${ax + gap - 34} ${ay + 12}" fill="none" stroke="${OURO}" stroke-width="4" stroke-linejoin="round"/>`;
  }
});
// seta de retorno discreta
const rx1 = x0 + 2 * (bw + gap) + bw / 2, rx2 = x0 + bw / 2, ry = by + bh + 110;
s += `<path d="M ${rx1} ${ry - 18} Q ${rx1} ${ry + 40} ${(rx1 + rx2) / 2} ${ry + 40} Q ${rx2} ${ry + 40} ${rx2} ${ry - 18}" fill="none" stroke="${MUTED}" stroke-width="2" stroke-dasharray="7 7"/>
<path d="M ${rx2 - 10} ${ry - 4} L ${rx2} ${ry - 20} L ${rx2 + 10} ${ry - 4}" fill="none" stroke="${MUTED}" stroke-width="2"/>
<text x="${(rx1 + rx2) / 2}" y="${ry + 76}" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-style="italic" font-size="26" fill="${MUTED}">uma direção alimenta a outra</text>
</svg>`;
sharp(Buffer.from(s)).png().toFile(out).then(() => console.log(out));
