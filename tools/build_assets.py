"""Build the profile's self-contained vector artwork from local source files."""
from functools import lru_cache
from html import escape
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets'
INK, PANEL, WHITE = '#0D1117', '#141C26', '#F1F5F9'
SOFT, MINT, CORAL, EDGE = '#B2C1D1', '#8FE3CF', '#FFAD94', '#344357'


@lru_cache(maxsize=6)
def face(weight):
    f = instantiateVariableFont(TTFont(OUT / 'fonts/Archivo.ttf'), {'wght': weight, 'wdth': 100})
    return f, f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm


def text(value, x, y, size=20, fill=WHITE, weight=450, anchor='start'):
    """Outline text so the artwork needs neither remote nor installed fonts."""
    font, glyphs, cmap, upem = face(weight)
    advance = sum(font['hmtx'][cmap[ord(c)]][0] for c in value)
    if anchor == 'middle':
        x -= advance * size / upem / 2
    elif anchor == 'end':
        x -= advance * size / upem
    paths, cursor = [], 0
    for c in value:
        name = cmap[ord(c)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        if pen.getCommands():
            paths.append(f'<path transform="translate({cursor} 0)" d="{pen.getCommands()}"/>')
        cursor += font['hmtx'][name][0]
    return f'<g fill="{fill}" transform="translate({x:.2f} {y}) scale({size/upem:.6f} {-size/upem:.6f})">' + ''.join(paths) + '</g>'


def line(path, color=EDGE, width=2, extra=''):
    return f'<path d="{path}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def rect(x, y, w, h, fill=PANEL, radius=16, stroke=None):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}"' + (f' stroke="{stroke}"' if stroke else '') + '/>'


def circle(x, y, r, fill=INK, stroke=None, width=2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"' + (f' stroke="{stroke}" stroke-width="{width}"' if stroke else '') + '/>'


def arrow(x, y, color=MINT):
    return line(f'M{x-9} {y+9}l18 -18m-17 0h17v17', color, 2.3)


def icon(kind, x, y, color=MINT, size=24):
    paths = {
        'agent': 'M8 3v3M16 3v3M5 7h14v13H5zM9 11h.01M15 11h.01M9 16h6M2 11h3M19 11h3',
        'app': 'M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2ZM10 5h4M11 19h2',
        'backend': 'M3 4h18v6H3zM3 14h18v6H3zM7 7h.01M7 17h.01M12 7h5M12 17h5',
        'check': 'M5 12l4 4L19 6',
        'mail': 'M3 5h18v14H3zM3 6l9 7 9-7',
        'link': 'M9 15l6-6M7 14l-2 2a3 3 0 0 0 4 4l4-4M11 8l4-4a3 3 0 0 1 4 4l-2 2',
        'github': 'M9 20c-4 1-4-2-6-2M15 22v-4c0-1-.3-2-1-2 4-.5 7-2 7-7 0-1.5-.5-3-1.5-4 0-1 .1-2-.5-3-2 0-3 1-4 1-2-.5-4-.5-6 0C8 2 7 1 5 1c-.6 1-.5 2-.5 3C3.5 5 3 6.5 3 8c0 5 3 6.5 7 7-.7.5-1 1.5-1 3v4',
        'heart': 'M20 5c-3-3-6 0-8 2-2-2-5-5-8-2-4 4 1 9 8 15 7-6 12-11 8-15Z',
        'chat': 'M4 3h16v13H9l-5 5zM8 8h8M8 12h5',
        'quote': 'M4 5h16v14H4zM8 9h3v4H8zM14 9h3v4h-3z',
        'human': 'M15 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM5 20v-2a7 7 0 0 1 14 0v2',
        'watch': 'M8 2h8v4H8zM8 18h8v4H8zM5 6h14v12H5zM9 12h1l1-3 2 6 1-3h2',
        'code': 'M8 6l-6 6 6 6M16 6l6 6-6 6M14 3l-4 18',
    }
    return f'<g transform="translate({x} {y}) scale({size/24})">{line(paths[kind],color,1.7)}</g>'


def svg(w, h, title, desc, content, styles=''):
    letters = {}

    def reuse(match):
        transform, path = match.groups()
        key = letters.setdefault(path, f'letter-{len(letters)}')
        return f'<use href="#{key}" transform="{transform}"/>'

    content = re.sub(r'<path transform="([^"]+)" d="([^"]+)"/>', reuse, content)
    definitions = ''.join(f'<path id="{key}" d="{path}"/>' for path, key in letters.items())
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><defs>{definitions}</defs><style>{styles}</style>{content}</svg>'


def signal_loop(x, y, scale=1):
    """Exact Bezier geometry: three system nodes joined by a continuous route."""
    route = 'M48 87C90 2 250 2 292 87C334 172 186 219 125 155C64 91 232 38 264 124C296 210 92 247 48 163C4 79 131 14 211 59'
    s = '<defs><linearGradient id="route" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#8FE3CF"/><stop offset=".52" stop-color="#79BAE4"/><stop offset="1" stop-color="#FFAD94"/></linearGradient></defs>'
    s += f'<g transform="translate({x} {y}) scale({scale})">'
    s += line(route, '#243344', 25)
    s += line(route, 'url(#route)', 3)
    s += line(route, WHITE, 3, 'pathLength="1000" class="pulse"')
    for px, py, name, kind in [(48, 87, 'AGENT', 'agent'), (284, 77, 'APP', 'app'), (176, 195, 'BACKEND', 'backend')]:
        s += circle(px, py, 27, PANEL, EDGE)
        s += icon(kind, px-12, py-12, MINT if kind != 'backend' else CORAL)
        s += text(name, px, py+48, 15, SOFT, 600, 'middle')
    return s + '</g>'


def header(mobile=False):
    w, h = (480, 282) if mobile else (960, 300)
    s = rect(0, 0, w, h, '#111A25', 16)
    s += line(f'M1 {h-1}H{w-1}', '#344E59', 1)
    if mobile:
        s += text("Hey, I'm Aryan.", 28, 56, 39, WHITE, 650)
        s += text('AI engineer at Omi', 30, 92, 21, MINT, 600)
        route = 'M70 160C100 115 210 115 240 160S380 205 410 160'
        s += line(route, '#344E59', 3)
        s += line(route, MINT, 3, 'pathLength="1000" class="pulse"')
        for px, kind, label in [(70, 'agent', 'Agent'), (240, 'app', 'App'), (410, 'backend', 'Backend')]:
            s += circle(px, 160, 26, PANEL, EDGE, 1)
            s += icon(kind, px-12, 148, MINT if kind != 'backend' else CORAL)
            s += text(label, px, 213, 18, SOFT, 450, 'middle')
        s += text('Build it. Break it. Make it dependable.', 30, 262, 17, CORAL, 450)
    else:
        s += text("Hey, I'm Aryan.", 36, 86, 48, WHITE, 650)
        s += text('AI engineer at Omi', 38, 125, 23, MINT, 600)
        s += text('I build agents, apps and the systems', 38, 172, 20, SOFT)
        s += text('that make them dependable.', 38, 202, 20, SOFT)
        s += text('Build it. Break it. Make it dependable.', 38, 261, 16, CORAL)
        s += signal_loop(576, 17, 1.02)
    motion = '.pulse{stroke-dasharray:8 992;stroke-dashoffset:1000;animation:travel 4.8s cubic-bezier(.16,1,.3,1) 1;opacity:0}@keyframes travel{0%{stroke-dashoffset:1000;opacity:0}12%{opacity:1}85%{opacity:1}100%{stroke-dashoffset:0;opacity:0}}@media(prefers-reduced-motion:reduce){.pulse{animation:none}}'
    return svg(w, h, "Hey, I'm Aryan — AI engineer at Omi", 'A signal travels through connected agent, app and backend nodes. Build it. Break it. Make it dependable.', s, motion)


def showcase(kind, mobile=False):
    if kind == 'mira':
        return mira_showcase(mobile)
    w, h = (480, 345) if mobile else (960, 248)
    accent = MINT if kind == 'omi' else CORAL
    name = 'Omi' if kind == 'omi' else 'Mira'
    summary = 'AI across native apps, wearables and the backend.' if kind == 'omi' else "Omi's AI support assistant."
    s = rect(0, 0, w, h, PANEL)
    s += text(name, 28 if mobile else 34, 57 if mobile else 64, 38 if mobile else 42, WHITE, 650)
    s += arrow(w-36, 37, accent)
    if kind == 'omi':
        lines = ['Native apps. Wearables. Backend reliability.'] if mobile else ['AI across native apps, wearables', 'and the backend.']
        for i, t in enumerate(lines):
            s += text(t, 30 if mobile else 36, (94 if mobile else 104)+i*28, 18 if mobile else 20, SOFT)
        s += text('Swift  /  Flutter  /  Python', 30 if mobile else 36, 131 if mobile else 200, 16, accent, 600)
        ox, oy, gap = (64, 204, 150) if mobile else (575, 72, 138)
        for i, (label, symbol) in enumerate([('Record', 'watch'), ('Persist', 'app'), ('Recover', 'check')]):
            px = ox+i*gap
            if i < 2:
                s += line(f'M{px+35} {oy+24}H{px+gap-35}', EDGE)
                s += circle(px+gap-43, oy+24, 3, accent)
            s += circle(px, oy+24, 33, INK)
            s += icon(symbol, px-14, oy+10, accent, 28)
            s += text(label, px, oy+85, 17, SOFT, 450, 'middle')
        s += text('Watch recording recovery', 30 if mobile else 550, 319 if mobile else 222, 15, accent, 450)
    else:
        lines = ["Omi's AI support assistant."] if mobile else ["Omi's AI support assistant.", 'Evidence, answers and human handoffs.']
        for i, t in enumerate(lines):
            s += text(t, 30 if mobile else 36, (94 if mobile else 104)+i*28, 18 if mobile else 20, SOFT)
        s += text('Retrieval  /  Agent workflows', 30 if mobile else 36, 131 if mobile else 200, 16, accent, 600)
        ox, oy, gap = (64, 204, 150) if mobile else (575, 72, 138)
        for i, (label, symbol) in enumerate([('Question', 'chat'), ('Sources', 'quote'), ('Handoff', 'human')]):
            px = ox+i*gap
            if i < 2:
                s += line(f'M{px+35} {oy+24}H{px+gap-35}', EDGE)
                s += circle(px+gap-43, oy+24, 3, accent)
            s += circle(px, oy+24, 33, INK)
            s += icon(symbol, px-14, oy+10, accent, 28)
            s += text(label, px, oy+85, 17, SOFT, 450, 'middle')
        s += text('Help that knows when to hand off.', 30 if mobile else 550, 319 if mobile else 222, 15, accent)
    return svg(w, h, f'{name} — {summary}', 'An explanatory workflow diagram; links below the artwork lead to public source and contributions.', s)


def mira_showcase(mobile=False):
    w, h = (480, 325) if mobile else (960, 248)
    s = rect(0, 0, w, h, '#231F27')
    s += arrow(w-36, 37, CORAL)
    if mobile:
        s += text('Mira', 30, 58, 38, WHITE, 650)
        s += text("Omi's AI support assistant.", 30, 95, 19, SOFT)
        s += line('M30 130H450', '#59404E', 1)
        ox, oy = 30, 162
    else:
        s += text('Mira', 540, 67, 42, WHITE, 650)
        s += text("Omi's AI support assistant.", 542, 109, 20, SOFT)
        s += text('Retrieval. Agent workflows.', 542, 150, 18, CORAL)
        s += text('A clear path to a human.', 542, 181, 18, CORAL)
        ox, oy = 38, 49
    for i, (label, kind) in enumerate([('Find the right source.', 'quote'), ('Make the answer useful.', 'chat'), ('Know when to hand off.', 'human')]):
        yy = oy+i*54
        s += icon(kind, ox, yy-20, CORAL, 25)
        s += text(label, ox+45, yy, 21 if mobile else 24, WHITE, 450)
    return svg(w, h, "Mira — Omi's AI support assistant", 'Find the right source. Make the answer useful. Know when to hand off. Retrieval and agent workflows.', s)


def project(kind, mobile=False):
    data = {
        'astar': ('Astar', 'A screen-aware voice assistant for macOS.', 'Screen. Speech. Tools.', MINT),
        'lab': ('Agent Reliability Lab', 'Did the agent actually complete the action?', 'Synthetic traces. Real checks.', CORAL),
        'thapar': ('ThaparGo', 'A campus, connected: navigation to societies.', 'React. Supabase. Internet Computer.', '#A9BFFF'),
    }
    title, desc, detail, accent = data[kind]
    w, h = (480, 232) if mobile else (960, 166)
    s = rect(0, 0, w, h, '#141C26')
    s += text(title, 28, 49, 27 if mobile else 28, WHITE, 600)
    s += arrow(w-32, 32, accent)
    s += text(desc, 30, 86, 18 if mobile else 19, SOFT)
    if not mobile:
        s += text(detail, 30, 135, 14, accent)
    if kind == 'astar':
        centers, y = ([70, 240, 410], 146) if mobile else ([662, 773, 884], 66)
        for i, label in enumerate(['Screen', 'Voice', 'Tools']):
            x = centers[i]
            if i == 0:
                s += rect(x-17, y-13, 34, 24, INK, 3, accent)
                s += line(f'M{x-8} {y+17}h16M{x} {y+11}v6', accent, 1.5)
            elif i == 1:
                for dx, height in [(-14, 8), (-7, 22), (0, 32), (7, 20), (14, 8)]:
                    s += line(f'M{x+dx} {y-height/2}v{height}', accent, 2.3)
            else:
                s += icon('code', x-17, y-17, accent, 34)
            s += text(label, x, y+53, 18 if mobile else 16, SOFT, 450, 'middle')
        plus = (centers[0]+centers[1])/2
        s += line(f'M{plus-5} {y}h10M{plus} {y-5}v10', SOFT, 1.5)
        ax = (centers[1]+centers[2])/2
        s += line(f'M{ax-10} {y}h20m-6-6 6 6-6 6', accent, 1.5)
    elif kind == 'lab':
        x, y = (30, 131) if mobile else (636, 53)
        s += text('CLAIM', x, y, 13, CORAL, 600)
        s += text('Action complete', x+105, y, 18, WHITE)
        s += line(f'M{x} {y+15}H{w-32}', EDGE, 1)
        s += text('EVIDENCE', x, y+46, 13, MINT, 600)
        s += text('Outcome checked', x+105, y+46, 18, WHITE)
        s += icon('check', w-55, y+28, MINT, 23)
        s += text('Synthetic trace', x, y+79, 13, SOFT)
    else:
        centers, y = ([70, 240, 410], 145) if mobile else ([655, 767, 879], 66)
        s += line(f'M{centers[0]} {y}Q{centers[1]} {y-52} {centers[2]} {y}M{centers[0]} {y}L{centers[1]} {y+18}L{centers[2]} {y}', '#536481', 2)
        for i, label in enumerate(['Classes', 'Rooms', 'Societies']):
            x, yy = centers[i], y+(18 if i==1 else 0)
            s += circle(x, yy, 7, INK, accent, 2)
            s += text(label, x, yy+40, 18 if mobile else 16, SOFT, 450, 'middle')
    return svg(w, h, title, f'{desc} {detail}', s)


def tech(mobile=False):
    names = [('python', 'Python', '#FFD980'), ('swift', 'Swift', CORAL), ('dart', 'Dart', '#70CFFF'), ('typescript', 'TypeScript', '#88BBFF'), ('react', 'React', '#8CDEF4'), ('fastapi', 'FastAPI', MINT), ('flutter', 'Flutter', '#91CFFF'), ('postgresql', 'Postgres', '#B2C8E6')]
    w, h = (480, 230) if mobile else (960, 112)
    s = rect(0, 0, w, h, INK)
    for i, (slug, label, color) in enumerate(names):
        col, row = (i % 4, i // 4) if mobile else (i, 0)
        x, y = col*120+60, row*112+27
        source = ET.parse(OUT / 'icons' / f'{slug}.svg').getroot()
        paths = ''.join(f'<path d="{e.attrib["d"]}"/>' for e in source.iter() if e.tag.endswith('path'))
        s += f'<g fill="{color}" transform="translate({x-20} {y}) scale(1.666667)">{paths}</g>'
        s += text(label, x, y+70, 18 if mobile else 15, SOFT, 450, 'middle')
    return svg(w, h, 'Tools I work with', 'Python, Swift, Dart, TypeScript, React, FastAPI, Flutter and PostgreSQL.', s)


def activity(mobile=False):
    data = json.loads((OUT / 'public-work.json').read_text())
    w, h = (480, 230) if mobile else (960, 150)
    s = rect(0, 0, w, h, PANEL)
    for x, value, label in [(30 if mobile else 34, str(data['omi_merged_prs']), 'merged PRs in Omi'), (262 if mobile else 352, str(data['public_merged_prs']), 'merged public PRs')]:
        s += text(value, x, 67 if mobile else 66, 42, MINT if x < 100 else CORAL, 650)
        s += text(label, x, 97 if mobile else 101, 17, SOFT)
    if mobile:
        s += line('M30 127H450', EDGE, 1)
        s += text('Changes you can open. Tests you can inspect.', 30, 163, 17, WHITE)
        s += text('Public GitHub snapshot · 31 October 2026', 30, 198, 14, SOFT)
    else:
        s += line('M650 30V120', EDGE, 1)
        s += text('Built in the open.', 684, 61, 21, WHITE, 600)
        s += text('Public GitHub snapshot', 684, 92, 15, SOFT)
        s += text('31 October 2026', 684, 117, 15, SOFT)
    return svg(w, h, 'Public engineering contributions', f"{data['omi_merged_prs']} merged authored Omi PRs; {data['public_merged_prs']} merged authored public PRs overall. Snapshot checked 31 October 2026; counts are not release or customer outcomes.", s)


def button(label, kind, fill, fg=WHITE, width=196):
    s = rect(0, 0, width, 46, fill, 12)
    s += icon(kind, 16, 13, fg, 20)
    s += text(label, 47, 29, 16, fg, 600)
    return svg(width, 46, label, label, s)


def main():
    for mobile in (False, True):
        suffix = '-mobile' if mobile else ''
        for name, build in [('header', header), ('tech', tech), ('activity', activity)]:
            (OUT / f'{name}{suffix}.svg').write_text(build(mobile))
        for kind in ('omi', 'mira'):
            (OUT / f'work-{kind}{suffix}.svg').write_text(showcase(kind, mobile))
        for kind in ('astar', 'lab', 'thapar'):
            (OUT / f'project-{kind}{suffix}.svg').write_text(project(kind, mobile))
    controls = [
        ('contact-email', 'Say hello', 'mail', '#243C3C', MINT, 154),
        ('contact-linkedin', 'LinkedIn', 'human', '#243444', '#D7E7F7', 154),
        ('contact-portfolio', 'Portfolio', 'link', '#3F302E', '#FFD0C0', 154),
        ('support-wise', 'Support via Wise', 'heart', '#9FE870', '#163300', 218),
        ('support-github', 'GitHub Sponsors', 'github', '#392C39', '#F6CAE8', 218),
    ]
    for name, label, kind, bg, fg, width in controls:
        (OUT / f'{name}.svg').write_text(button(label, kind, bg, fg, width))
    for name in ['masthead.svg', 'masthead-dark.svg', 'masthead-mobile.svg', 'masthead-mobile-dark.svg']:
        (OUT / name).unlink(missing_ok=True)
    print('Built 16 artwork variants and 5 linked controls.')


if __name__ == '__main__':
    main()
