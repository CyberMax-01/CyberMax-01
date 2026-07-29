import json
import os

with open('projects.json') as f:
    projects = json.load(f)['projects']

BORDER = 18
BG = "#0F172A"
TITLE_BG = "#1E293B"
ACCENT = "#10B981"
TEXT = "#E2E8F0"
MUTED = "#94A3B8"

lines = []
lines.append('<svg xmlns="http://www.w3.org/2000/svg" width="760" height="420" font-family="ui-monospace,Menlo,Consolas,monospace" role="img" aria-label="Project showcase">')
lines.append('<defs>')
lines.append('<linearGradient id="grad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0F172A"/><stop offset="1" stop-color="#1E293B"/></linearGradient>')
lines.append('<filter id="glow"><feGaussianBlur stdDeviation="3"/></filter>')
lines.append('</defs>')
lines.append(f'<rect x="2" y="2" width="756" height="416" rx="14" fill="{BG}"/>')
lines.append(f'<rect x="2" y="2" width="756" height="42" rx="14" fill="{TITLE_BG}"/>')
lines.append(f'<circle cx="22" cy="20" r="4" fill="#EF4444"/><circle cx="34" cy="20" r="4" fill="#FBBF24"/><circle cx="46" cy="20" r="4" fill="#22C55E"/>')
lines.append(f'<text x="380" y="27" text-anchor="middle" font-size="14" fill="{TEXT}">Projects</text>')

for idx, p in enumerate(projects):
    x0 = BORDER
    y0 = 54 + idx * 42
    x1 = 760 - BORDER
    y1 = y0 + 36
    lines.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="8" fill="{TITLE_BG}" stroke="{ACCENT}" stroke-width="1.2" opacity="0.95"/>')
    lines.append(f'<text x="{x0+12}" y="{y0+18}" font-size="13" fill="{ACCENT}">{p["name"]}</text>')
    lines.append(f'<text x="{x0+12}" y="{y0+34}" font-size="11" fill="{MUTED}">{p["description"]}</text>')
    lines.append(f'<text x="{x1-10}" y="{y0+26}" text-anchor="end" font-size="11" fill="{MUTED}">★ {p["stars"]} · ⑂ {p["forks"]} · {p["language"]}</text>')

lines.append('</svg>')

with open('projects/projects.svg','w') as f:
    f.write('\n'.join(lines))
print('Generated projects/projects.svg')
