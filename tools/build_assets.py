"""Build self-contained SVGs from bundled OFL-licensed Archivo. No remote font."""
from html import escape
from math import cos, sin, pi
from pathlib import Path
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
font = instantiateVariableFont(TTFont(ROOT / 'assets/fonts/Archivo.ttf'), {'wght': 850, 'wdth': 100})
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
upem = font['head'].unitsPerEm


def lettering(text, x, y, size, color, max_width=None):
    cursor, paths = 0, []
    for char in text:
        name = cmap[ord(char)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        if pen.getCommands():
            paths.append(f'<path transform="translate({cursor} 0)" d="{pen.getCommands()}"/>')
        cursor += font['hmtx'][name][0]
    scale = min(size / upem, max_width / cursor) if max_width else size / upem
    return f'<g fill="{color}" transform="translate({x} {y}) scale({scale:.6f} {-scale:.6f})">' + ''.join(paths) + '</g>'


def mark(cx, cy, radius, color):
    strokes = []
    for i in range(6):
        a = i * pi / 3
        x1, y1 = cx + cos(a) * radius * .24, cy + sin(a) * radius * .24
        x2, y2 = cx + cos(a) * radius, cy + sin(a) * radius
        strokes.append(f'<path d="M{x1:.2f},{y1:.2f} L{x2:.2f},{y2:.2f}"/>')
    return f'<g stroke="{color}" stroke-width="{radius*.20:.2f}" stroke-linecap="square">' + ''.join(strokes) + '</g>'


def masthead(mobile=False, dark=False):
    bg, white, mint = ('#1D2FD0' if dark else '#263FE8'), '#F7F9F2', '#D8F5B1'
    w, h = (480, 480) if mobile else (1200, 470)
    title = 'Aryan Gupta — AI engineer at Omi'
    desc = 'Custom Archivo lettering and an open six-stroke mark. AI products, native apps and reliable systems.'
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>', '<style>.signal{stroke-dasharray:0 28 250 28;animation:trace 5s cubic-bezier(.16,1,.3,1) 1} @keyframes trace{0%{stroke-dashoffset:278}100%{stroke-dashoffset:0}} @media(prefers-reduced-motion:reduce){.signal{animation:none}}</style>', f'<path fill="{bg}" d="M0 0H{w}V{h}H0z"/>']
    if mobile:
        parts += [lettering('ARYAN', 24, 136, 130, white, 430), lettering('GUPTA', 24, 256, 130, white, 430), mark(91, 349, 55, mint), lettering('AI ENGINEER', 190, 330, 24, mint, 260), lettering('AT OMI', 190, 365, 24, white, 260), lettering('AGENTS / APPS / SYSTEMS', 24, 441, 22, white, 430)]
    else:
        parts += [lettering('ARYAN', 38, 197, 238, white, 880), lettering('GUPTA', 342, 388, 238, white, 814), mark(1063, 122, 76, mint), mark(139, 304, 82, mint), lettering('AI ENGINEER AT OMI', 40, 443, 24, white, 520), lettering('AGENTS / APPS / SYSTEMS', 760, 443, 24, mint, 400)]
    parts += [f'<path class="signal" fill="none" stroke="{white}" stroke-width="2" d="' + ('M33 349H149' if mobile else 'M985 122H1141') + '"/>', '</svg>']
    return ''.join(parts)


for mobile in (False, True):
    for dark in (False, True):
        name = 'masthead' + ('-mobile' if mobile else '') + ('-dark' if dark else '') + '.svg'
        (ROOT / 'assets' / name).write_text(masthead(mobile, dark))
        print('built assets/' + name)


for name, label, bg, fg in [
    ('wise', 'Support via Wise', '#D8F5B1', '#14200D'),
    ('github', 'GitHub Sponsors', '#263FE8', '#F7F9F2'),
]:
    button = '<svg xmlns="http://www.w3.org/2000/svg" width="320" height="70" viewBox="0 0 320 70" role="img">'
    button += f'<title>{escape(label)}</title><path fill="{bg}" d="M0 0H320V70H0z"/>'
    button += lettering(label, 20, 44, 25, fg, 248)
    button += f'<path d="M278 24h18v18m0-18-20 20" fill="none" stroke="{fg}" stroke-width="2.5"/>'
    button += '</svg>'
    (ROOT / 'assets' / f'support-{name}.svg').write_text(button)
    print('built assets/support-' + name + '.svg')
