---
date: 2026-04-13
slug: unicode-staff-grid
---

# Unicode Staff Grid

The [fretboard post](/ton/blog/2026/03/29/fretboard-diagrams/) ended with “these approaches
also apply to musical staves.” This version does just that, but keeps one constraint: start with
the Unicode staff glyph, measure the source units once, and derive the placement grid from those
measurements instead of nudging pixels by hand.

The relevant character is <span class="noto-music">&#x1D11A;</span>,
`'\U0001d11a'`, musical symbol five-line staff.

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Music&family=Source+Serif+4:wght@400;600&display=swap');

.noto-music {
  font-family: 'Noto Music', sans-serif;
}

.staff-demo {
  --glyph-scale: 6.25rem;
  --staff-stretch: 2;
  --staff-left: calc(var(--glyph-scale) * 50 / 1000);
  --staff-width: calc(var(--glyph-scale) * var(--staff-stretch));
  --staff-top-line: calc(var(--glyph-scale) * 12 / 1000);
  --staff-step: calc(var(--glyph-scale) * 122 / 1000);
  --quarter-font-size: calc(var(--staff-step) * 1000 / 250);
  --half-font-size: calc(var(--staff-step) * 1000 / 270);
  --quarter-up-center: calc(var(--quarter-font-size) * 873 / 1000);
  --quarter-down-center: calc(var(--quarter-font-size) * 125 / 1000);
  --half-down-center: calc(var(--half-font-size) * 135 / 1000);
  --note-gap: calc(var(--glyph-scale) * 44 / 1000);
  --prefix-width: calc(var(--glyph-scale) * 0.42);
  --staff-origin-y: calc(var(--staff-step) * 0.52);
  --notes-left: calc(var(--staff-left) + var(--prefix-width));
  --slot-step: calc((var(--staff-width) - var(--notes-left) - var(--half-font-size)) / 15);
  display: block;
  height: calc(var(--staff-step) * 10.9 + 3rem);
  margin: 1rem 0;
  padding: calc(var(--staff-step) * 0.5) 0 0;
  position: relative;
  width: calc(var(--staff-width) + var(--staff-left));
}

.staff-demo::before {
  color: currentColor;
  content: '\1D11A';
  font: var(--glyph-scale)/1 'Noto Music', sans-serif;
  left: 0;
  opacity: 0.28;
  pointer-events: none;
  position: absolute;
  top: var(--staff-origin-y);
  transform: scaleX(var(--staff-stretch));
  transform-origin: left top;
  white-space: pre;
}

.staff-items {
  color: #0f4c81;
  display: block;
  left: 0;
  position: absolute;
  top: 0;
  width: 100%;
}

.staff-items > span {
  color: #0f4c81;
  display: block;
  position: relative;
}

.staff-labels {
  color: #0f4c81;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  left: var(--staff-left);
  position: absolute;
  top: calc(var(--staff-step) * 10.9);
  width: var(--staff-width);
}

.staff-labels > span {
  justify-self: center;
  white-space: pre;
}

.staff-items > [data-pos^='a'],
.staff-items > [data-pos^='c'],
.staff-items > [data-pos^='d'],
.staff-items > [data-pos^='e'],
.staff-items > [data-pos^='g'],
.staff-items > [data-pos^='G'] {
  position: absolute;
}

.staff-items > [data-pos^='a'],
.staff-items > [data-pos^='c'] {
  font: 700 calc(var(--staff-step) * 1.4)/0.82 'Source Serif 4', serif;
  left: calc(var(--notes-left) - var(--slot-step) * 0.75);
}

.staff-items > [data-pos^='G'],
.staff-items > [data-pos^='g'],
.staff-items > [data-pos^='d'],
.staff-items > [data-pos^='e'] {
  font: var(--quarter-font-size)/1 'Noto Music', sans-serif;
}

.staff-items > [data-pos^='a'] {
  top: calc(var(--staff-origin-y) + var(--staff-top-line) + var(--staff-step) * 5 - 0.55em);
}

.staff-items > [data-pos^='G'] {
  left: calc(var(--staff-left) * 0.55);
  top: calc(var(--staff-origin-y) + var(--staff-top-line) + var(--staff-step) * 6 - var(--quarter-up-center));
}

.staff-items > [data-pos^='c'] {
  top: calc(var(--staff-origin-y) + var(--staff-top-line) + var(--staff-step) * 3 - 0.55em);
}

.staff-items > [data-pos^='g'] {
  top: calc(var(--staff-origin-y) + var(--staff-top-line) + var(--staff-step) * 6 - var(--quarter-up-center));
}

.staff-items > [data-pos^='d'] {
  top: calc(var(--staff-origin-y) + var(--staff-top-line) + var(--staff-step) * 2 - var(--quarter-down-center));
  transform: rotate(180deg);
}

.staff-items > [data-pos^='e'] {
  top: calc(var(--staff-origin-y) + var(--staff-top-line) + var(--staff-step) * 1 - var(--quarter-down-center));
  transform: rotate(180deg);
}

.staff-items > [data-pos$='04'] {
  left: var(--notes-left);
}

.staff-items > [data-pos$='08'] {
  left: calc(var(--notes-left) + var(--slot-step) * 4);
}

.staff-items > [data-pos$='12'] {
  left: calc(var(--notes-left) + var(--slot-step) * 8);
}

.staff-items > [data-pos$='16'] {
  left: calc(var(--notes-left) + var(--slot-step) * 12);
}
</style>

The source file in [notofonts/music](https://github.com/notofonts/music) is
[`sources/NotoMusic.glyphs`](https://github.com/notofonts/music/blob/main/sources/NotoMusic.glyphs).

<details markdown="1">
<summary>Python to download the font source, measure, and print the table:</summary>

```python
uv run --no-project --with fonttools python - <<'PY'
import re
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlretrieve

from fontTools.ttLib import TTFont


@dataclass(frozen=True)
class Bounds:
    left: int
    bottom: int
    right: int
    top: int

    @property
    def width(self) -> int:
        return self.right - self.left

    @property
    def height(self) -> int:
        return self.top - self.bottom

    @property
    def center_x(self) -> float:
        return (self.left + self.right) / 2

    @property
    def center_y(self) -> float:
        return (self.bottom + self.top) / 2


def bound_points(points: list[tuple[int, int]]) -> Bounds:
    horizontal, vertical = zip(*points)
    return Bounds(min(horizontal), min(vertical), max(horizontal), max(vertical))


def source_points(block: str) -> list[tuple[int, int]]:
    return [(int(x), int(y)) for x, y in re.findall(r'\(([-\d]+),([-\d]+),[a-z]+\)', block)]


def glyph_block(text: str, glyph_name: str) -> str:
    start = text.rfind('{', 0, text.index(f'glyphname = {glyph_name};'))
    depth = 0
    for index in range(start, len(text)):
        character = text[index]
        if character == '{':
            depth += 1
        elif character == '}':
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    raise ValueError(f'Unclosed glyph block for {glyph_name}')


def measure_source(text: str, glyph_name: str, staff: bool = False) -> dict[str, object]:
    block = glyph_block(text, glyph_name)
    details = ''
    if staff:
        lines = sorted(
            (
                bound_points(source_points(nodes))
                for nodes in re.findall(r'nodes = \((.*?)\);', block, re.S)
            ),
            key=lambda bounds: bounds.bottom,
        )
        gap = lines[1].bottom - lines[0].top
        center_step = lines[1].center_y - lines[0].center_y
        details = (
            f'{len(lines)} lines; thickness {lines[0].height}; gap {gap}; '
            f'center step {center_step:.0f}; note step {center_step / 2:.0f}'
        )
    return {
        'advance_width': int(re.search(r'width = (\d+);', block).group(1)),
        'bounds': bound_points(source_points(block)),
        'details': details,
    }


def measure_note(font: TTFont, glyph_name: str, notehead_top: int) -> dict[str, object]:
    glyph = font['glyf'][glyph_name]
    bounds = Bounds(glyph.xMin, glyph.yMin, glyph.xMax, glyph.yMax)
    coordinates, _, flags = glyph.getCoordinates(font['glyf'])
    notehead = bound_points([(x, y) for x, y in coordinates if y <= notehead_top])
    stem_left = min(x for x, y in coordinates if y > notehead_top)
    stem_right = max(x for x, y in coordinates if y > notehead_top)
    stem_bottom = min(
        y
        for (x, y), flag in zip(coordinates, flags)
        if flag & 1 and x in (stem_left, stem_right) and y < bounds.top
    )
    stem = bound_points([
        (x, y) for x, y in coordinates if x >= stem_left and y >= notehead.center_y
    ])
    return {
        'advance_width': font['hmtx'][glyph_name][0],
        'bounds': bounds,
        'details': (
            f'notehead ({notehead.left}, {notehead.bottom})-'
            f'({notehead.right}, {notehead.top}) '
            f'center ({notehead.center_x:.1f}, {notehead.center_y:.1f}); '
            f'stem ({stem.left}, {stem_bottom})-({stem.right}, {stem.top}); '
            f'top offsets up/down {bounds.top - notehead.center_y:.1f}/'
            f'{notehead.center_y - bounds.bottom:.1f}'
        ),
    }


def measure_table(source: Path, font_path: Path) -> list[dict[str, object]]:
    text = source.read_text()
    notehead = '\U0001d158'
    with TTFont(font_path) as font:
        glyph_names = font.getBestCmap()
        notehead_top = font['glyf'][glyph_names[ord(notehead)]].yMax
        rows = []
        for label, character, kind in (
            ('4-string fretboard', '\U0001d11d', 'source'),
            ('5-string fretboard', '\U0001d11e', 'source'),
            ('5-line staff', '\U0001d11a', 'staff'),
            ('Stemless notehead', notehead, 'source'),
            ('Quarter note', '\U0001d15f', 'note'),
            ('Half note', '\U0001d15e', 'note'),
        ):
            glyph_name = glyph_names[ord(character)]
            measurement = (
                measure_note(font, glyph_name, notehead_top)
                if kind == 'note'
                else measure_source(text, glyph_name, staff=kind == 'staff')
            )
            rows.append({'label': label, 'codepoint': ascii(character), **measurement})
    return rows


def markdown_table(rows: list[dict[str, object]]) -> str:
    return '\n'.join([
        '| Glyph | Codepoint | Advance | Bounds `(l,b)-(r,t)` | Size | Center | Details |',
        '| --- | --- | ---: | --- | --- | --- | --- |',
        *(
            (
                '| {label} | `{codepoint}` | {advance_width} | '
                '({bounds.left}, {bounds.bottom})-({bounds.right}, {bounds.top}) | '
                '{bounds.width}x{bounds.height} | '
                '({bounds.center_x:.1f}, {bounds.center_y:.1f}) | {details} |'
            ).format(**row)
            for row in rows
        ),
    ])


with TemporaryDirectory() as directory:
    source = Path(directory) / 'NotoMusic.glyphs'
    font = Path(directory) / 'NotoMusic.ttf'
    urlretrieve(
        'https://raw.githubusercontent.com/notofonts/music/main/sources/NotoMusic.glyphs', source
    )
    urlretrieve(
        'https://raw.githubusercontent.com/notofonts/noto-fonts/main/'
        'hinted/ttf/NotoMusic/NotoMusic-Regular.ttf',
        font,
    )
    print(markdown_table(measure_table(source, font)))
PY
```

</details>

The full table is longer, but for this post the staff, quarter-note, and half-note rows are the
ones that matter:

| Glyph | Codepoint | Advance | Bounds `(l,b)-(r,t)` | Size | Center | Details |
| --- | --- | ---: | --- | --- | --- | --- |
| 5-line staff | `'\U0001d11a'` | 1100 | (50, 0)-(1050, 1000) | 1000x1000 | (550.0, 500.0) | 5 lines; thickness 24; gap 220; center step 244; note step 122 |
| Quarter note | `'\U0001d15f'` | 400 | (51, 11)-(350, 1009) | 299x998 | (200.5, 510.0) | measured from built TTF glyph bounds |
| Half note | `'\U0001d15e'` | 397 | (50, -1)-(347, 1009) | 297x1010 | (198.5, 504.0) | measured from built TTF glyph bounds |

The useful CSS variables fall straight out of those measurements:

```css
.staff-demo {
  --glyph-scale: 20rem;
  --staff-left: calc(var(--glyph-scale) * 50 / 1000);
  --staff-width: calc(var(--glyph-scale) * 2);
  --staff-top-line: calc(var(--glyph-scale) * 12 / 1000);
  --staff-step: calc(var(--glyph-scale) * 122 / 1000);
}
```

`50 / 1000` is the left inset, `12 / 1000` is the top-line center, and `122 / 1000` is half of
the `244` unit line-center spacing, so it lands on both lines and spaces.

For the marks themselves, quarter notes and half notes are easier to read than bare noteheads. The
overlay uses `Noto Music` glyphs for both from the same musical-symbol family:
<span class="noto-music">𝅘𝅥</span>, `'\U0001d15f'`, musical symbol quarter note, and
<span class="noto-music">𝅗𝅥</span>, `'\U0001d15e'`, musical symbol half note.

With that grid, a sparse `data-pos` overlay can treat one scaled staff glyph as one 16-slot
measure block and place the treble clef, the stacked `4/4`, and then the note characters. Every
 character uses exactly one row letter plus a two-digit base-10 column: the clef centers on `G`,
 column `02` is left empty because the treble clef is wide, the time-signature digits sit on `a`
 and `c`, and the notes use their pitch rows. The last two digits give the column from `01`
 through `16`. Uppercase and lowercase distinguish lower and
higher pitches. The first measure of “Twinkle, Twinkle, Little Star” is `G G d d`; the next
measure starts a new staff block when the 16 slots run out.

<div class="staff-demo" aria-label="Twinkle, Twinkle, Little Star first phrase on a measured Unicode staff">
  <div class="staff-items" aria-hidden="true">
    <span data-pos="G01">𝄞</span>
    <span data-pos="a03">4</span>
    <span data-pos="c03">4</span>
    <span data-pos="g04">𝅘𝅥</span>
    <span data-pos="g08">𝅘𝅥</span>
    <span data-pos="d12">𝅘𝅥</span>
    <span data-pos="d16">𝅘𝅥</span>
  </div>
  <div class="staff-labels" aria-hidden="true">
    <span>G</span>
    <span>G</span>
    <span>d</span>
    <span>d</span>
  </div>
</div>

```html
<div class="staff-demo">
  <div class="staff-items">
    <span data-pos="G01">&#x1d11e;</span>
    <span data-pos="a03">4</span>
    <span data-pos="c03">4</span>
    <span data-pos="g04">&#x1d15f;</span>
    <span data-pos="g08">&#x1d15f;</span>
    <span data-pos="d12">&#x1d15f;</span>
    <span data-pos="d16">&#x1d15f;</span>
  </div>
</div>
```

This is the part I wanted from the start: one Unicode background glyph, one measured grid, and
then ordinary markup on top. The fretboard glyph and the staff glyph both work better once the
source units become the API.
