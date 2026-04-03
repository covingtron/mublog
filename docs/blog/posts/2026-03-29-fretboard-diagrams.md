---
date: 2026-03-29
slug: fretboard-diagrams
---

# Fretboard Diagrams

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Music&display=swap');

.noto-music {
  font-family: 'Noto Music', sans-serif;
}

.fretboard-grid {
  display: inline-grid;
  grid-template-columns: repeat(7, 1.5rem);
  grid-template-rows: repeat(6, 1.5rem);
  margin: 1rem 0;
  font: 0.95rem/1 monospace;
  background-image:
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor);
  background-position:
    2.25rem 3rem,
    2.25rem 4.5rem,
    2.25rem 6rem,
    2.25rem 7.5rem,
    2.25rem calc(9rem - 1px),
    2.25rem 3rem,
    3.75rem 3rem,
    5.25rem 3rem,
    6.75rem 3rem,
    8.25rem 3rem,
    9.75rem 3rem;
  background-repeat: no-repeat;
  background-size:
    7.5rem 3px,
    7.5rem 1px,
    7.5rem 1px,
    7.5rem 1px,
    7.5rem 1px,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem;
}

.fretboard-grid > span { display: grid; place-items: center; }

.fretboard-pos {
  display: inline-grid;
  grid-template-columns: repeat(7, 1.5rem);
  grid-template-rows: repeat(6, 1.5rem);
  margin: 1rem 0;
  font: 0.95rem/1 monospace;
  background-image:
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor);
  background-position:
    2.25rem 3rem,
    2.25rem 4.5rem,
    2.25rem 6rem,
    2.25rem 7.5rem,
    2.25rem calc(9rem - 1px),
    2.25rem 3rem,
    3.75rem 3rem,
    5.25rem 3rem,
    6.75rem 3rem,
    8.25rem 3rem,
    9.75rem 3rem;
  background-repeat: no-repeat;
  background-size:
    7.5rem 3px,
    7.5rem 1px,
    7.5rem 1px,
    7.5rem 1px,
    7.5rem 1px,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem;
}

.fretboard-pos > span { display: grid; place-items: center; }
.fretboard-pos > [data-pos^='L'] { grid-column: 1; }
.fretboard-pos > [data-pos^='E'] { grid-column: 2; }
.fretboard-pos > [data-pos^='A'] { grid-column: 3; }
.fretboard-pos > [data-pos^='D'] { grid-column: 4; }
.fretboard-pos > [data-pos^='G'] { grid-column: 5; }
.fretboard-pos > [data-pos^='B'] { grid-column: 6; }
.fretboard-pos > [data-pos^='e'] { grid-column: 7; }
.fretboard-pos > [data-pos$='H'] { grid-row: 1; }
.fretboard-pos > [data-pos$='0'] { grid-row: 2; }
.fretboard-pos > [data-pos$='1'] { grid-row: 3; }
.fretboard-pos > [data-pos$='2'] { grid-row: 4; }
.fretboard-pos > [data-pos$='3'] { grid-row: 5; }
.fretboard-pos > [data-pos$='4'] { grid-row: 6; }

</style>

Unicode includes an empty four-string fretboard,
[<span class="noto-music">&#x1D11D;</span>](https://codepoints.net/U+1D11D), for ukulele or bass,
and an empty six-string fretboard,
[<span class="noto-music">&#x1D11C;</span>](https://codepoints.net/U+1D11C), for guitar.
How are people supposed to compose the fretboard background and marks like ●, ◯, and ✕?

Going all the way back to ASCII art and box drawings, one approach is multiple lines: one column
per string, one row per fret, top markers for muted and open strings, and filled dots where
fingers land.
The canonical left-to-right order for guitars is `L`, `E`, `A`, `D`, `G`, `B`, `e`, `R`.

Open C major: `x32010`

<pre style="font-family: monospace; line-height: 1.275">
  E   A   D   G   B   e
  ✕           ◯       ◯
  ┌───┬───┬───┬───┬───┐
1 │   │   │   │   ●   │
  ├───┼───┼───┼───┼───┤
2 │   │   ●   │   │   │
  ├───┼───┼───┼───┼───┤
3 │   ●   │   │   │   │
  ├───┼───┼───┼───┼───┤
4 │   │   │   │   │   │
  └───┴───┴───┴───┴───┘
</pre>

This needed a `pre` tag with a tuned `line-height` to reduce the vertical gaps.

```html
<pre style="font-family: monospace; line-height: 1.275">
  E   A   D   G   B   e
  ✕           ◯       ◯
  ┌───┬───┬───┬───┬───┐
1 │   │   │   │   ●   │
  ├───┼───┼───┼───┼───┤
2 │   │   ●   │   │   │
  ├───┼───┼───┼───┼───┤
3 │   ●   │   │   │   │
  ├───┼───┼───┼───┼───┤
4 │   │   │   │   │   │
  └───┴───┴───┴───┴───┘
</pre>
```

A CSS grid diagram looks like this:

<div class="fretboard-grid" aria-label="Open C major chord diagram">
  <span></span><span>E</span><span>A</span><span>D</span><span>G</span><span>B</span><span>e</span>
  <span></span><span>✕</span><span></span><span></span><span>◯</span><span></span><span>◯</span>
  <span>1</span><span></span><span></span><span></span><span></span><span>●</span><span></span>
  <span>2</span><span></span><span></span><span>●</span><span></span><span></span><span></span>
  <span>3</span><span></span><span>●</span><span></span><span></span><span></span><span></span>
  <span>4</span><span></span><span></span><span></span><span></span><span></span><span></span>
</div>

```html
<style>
.fretboard-grid {
  display: inline-grid;
  grid-template-columns: repeat(7, 1.5rem);
  grid-template-rows: repeat(6, 1.5rem);
  margin: 1rem 0;
  font: 0.95rem/1 monospace;
  background-image:
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor);
  background-position:
    2.25rem 3rem,
    2.25rem 4.5rem,
    2.25rem 6rem,
    2.25rem 7.5rem,
    2.25rem calc(9rem - 1px),
    2.25rem 3rem,
    3.75rem 3rem,
    5.25rem 3rem,
    6.75rem 3rem,
    8.25rem 3rem,
    9.75rem 3rem;
  background-repeat: no-repeat;
  background-size:
    7.5rem 3px,
    7.5rem 1px,
    7.5rem 1px,
    7.5rem 1px,
    7.5rem 1px,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem;
}

.fretboard-grid > span { display: grid; place-items: center; }
</style>

<div class="fretboard-grid" aria-label="Open C major chord diagram">
  <span></span><span>E</span><span>A</span><span>D</span><span>G</span><span>B</span><span>e</span>
  <span></span><span>✕</span><span></span><span></span><span>◯</span><span></span><span>◯</span>
  <span>1</span><span></span><span></span><span></span><span></span><span>●</span><span></span>
  <span>2</span><span></span><span></span><span>●</span><span></span><span></span><span></span>
  <span>3</span><span></span><span>●</span><span></span><span></span><span></span><span></span>
  <span>4</span><span></span><span></span><span></span><span></span><span></span><span></span>
</div>
```

A sparse `data-pos` version can skip the empty cells. The CSS `^=` selector matches the starting
string letter, and `$=` matches the ending row number, so `A3` decodes to the A string and third
fret. The string letters are supplemented with `L` and `R` for the margins, and the row numbers
with `H` for the header row and `0` for the nut marker row, which holds `✕` and `◯`.

<div class="fretboard-pos" aria-label="Open C major chord diagram">
  <span data-pos="L1">1</span>
  <span data-pos="L2">2</span>
  <span data-pos="L3">3</span>
  <span data-pos="L4">4</span>
  <span data-pos="EH">E</span>
  <span data-pos="E0">✕</span>
  <span data-pos="AH">A</span>
  <span data-pos="A3">●</span>
  <span data-pos="DH">D</span>
  <span data-pos="D2">●</span>
  <span data-pos="GH">G</span>
  <span data-pos="G0">◯</span>
  <span data-pos="BH">B</span>
  <span data-pos="B1">●</span>
  <span data-pos="eH">e</span>
  <span data-pos="e0">◯</span>
</div>

```html
<style>
.fretboard-pos {
  display: inline-grid;
  grid-template-columns: repeat(7, 1.5rem);
  grid-template-rows: repeat(6, 1.5rem);
  margin: 1rem 0;
  font: 0.95rem/1 monospace;
  background-image:
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor);
  background-position:
    2.25rem 3rem,
    2.25rem 4.5rem,
    2.25rem 6rem,
    2.25rem 7.5rem,
    2.25rem calc(9rem - 1px),
    2.25rem 3rem,
    3.75rem 3rem,
    5.25rem 3rem,
    6.75rem 3rem,
    8.25rem 3rem,
    9.75rem 3rem;
  background-repeat: no-repeat;
  background-size:
    7.5rem 3px,
    7.5rem 1px,
    7.5rem 1px,
    7.5rem 1px,
    7.5rem 1px,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem,
    1px 6rem;
}

.fretboard-pos > span { display: grid; place-items: center; }
.fretboard-pos > [data-pos^='L'] { grid-column: 1; }
.fretboard-pos > [data-pos^='E'] { grid-column: 2; }
.fretboard-pos > [data-pos^='A'] { grid-column: 3; }
.fretboard-pos > [data-pos^='D'] { grid-column: 4; }
.fretboard-pos > [data-pos^='G'] { grid-column: 5; }
.fretboard-pos > [data-pos^='B'] { grid-column: 6; }
.fretboard-pos > [data-pos^='e'] { grid-column: 7; }
.fretboard-pos > [data-pos$='H'] { grid-row: 1; }
.fretboard-pos > [data-pos$='0'] { grid-row: 2; }
.fretboard-pos > [data-pos$='1'] { grid-row: 3; }
.fretboard-pos > [data-pos$='2'] { grid-row: 4; }
.fretboard-pos > [data-pos$='3'] { grid-row: 5; }
.fretboard-pos > [data-pos$='4'] { grid-row: 6; }
</style>

<div class="fretboard-pos" aria-label="Open C major chord diagram">
  <span data-pos="L1">1</span>
  <span data-pos="L2">2</span>
  <span data-pos="L3">3</span>
  <span data-pos="L4">4</span>
  <span data-pos="EH">E</span>
  <span data-pos="E0">✕</span>
  <span data-pos="AH">A</span>
  <span data-pos="A3">●</span>
  <span data-pos="DH">D</span>
  <span data-pos="D2">●</span>
  <span data-pos="GH">G</span>
  <span data-pos="G0">◯</span>
  <span data-pos="BH">B</span>
  <span data-pos="B1">●</span>
  <span data-pos="eH">e</span>
  <span data-pos="e0">◯</span>
</div>
```

A Unicode-fretboard variation can keep the sparse `data-pos` markup and place marks from the
`Noto Music` source geometry. The six-string and four-string glyphs sit on the same integer grid:
a `37` unit stroke, a `135` unit gap, and `172` unit center spacing in a `1000` units-per-em font.

<style>
.fretboard-glyph {
  --glyph-scale: 7rem;
  --column-origin: calc(1.2rem + var(--glyph-scale) * 137 / 2000); /* left inset, source units */
  --gap: calc(var(--glyph-scale) * 172 / 1000); /* source units */
  --row-origin: calc(0.9rem + var(--glyph-scale) * 503 / 2000); /* top inset, source units */
  margin: 1rem 0;
  width: 8.7rem; /* fret-label column plus six-string glyph */
  height: 8.8rem; /* header, open row, four frets, bottom line */
  display: inline-block;
  position: relative;
}

.fretboard-glyph::before {
  content: '\1D11C'; /* MUSICAL SYMBOL SIX-STRING FRETBOARD */
  color: currentColor;
  font: var(--glyph-scale)/1 'Noto Music', sans-serif;
  left: 1.2rem; /* left inset */
  opacity: 0.32; /* fade glyph behind the marks */
  pointer-events: none;
  position: absolute;
  top: 0.9rem; /* top inset */
  z-index: 0;
}

.fretboard-glyph > span {
  font: 0.95rem/1 monospace; /* overlay text size and leading */
  position: absolute;
  transform: translate(-50%, -50%);
  z-index: 1;
}
.fretboard-glyph > [data-pos^='L'] { left: 0.3rem; transform: translateY(-50%); /* fret-label column */ }
.fretboard-glyph > [data-pos^='E'] { left: var(--column-origin); }
.fretboard-glyph > [data-pos^='A'] { left: calc(var(--column-origin) + var(--gap)); }
.fretboard-glyph > [data-pos^='D'] { left: calc(var(--column-origin) + var(--gap) * 2); }
.fretboard-glyph > [data-pos^='G'] { left: calc(var(--column-origin) + var(--gap) * 3); }
.fretboard-glyph > [data-pos^='B'] { left: calc(var(--column-origin) + var(--gap) * 4); }
.fretboard-glyph > [data-pos^='e'] { left: calc(var(--column-origin) + var(--gap) * 5); }
.fretboard-glyph > [data-pos$='H'] { top: 0.45rem; /* top inset - header adjustment */ }
.fretboard-glyph > [data-pos$='0'] { top: 1.2rem; /* top inset + nut adjustment */ }
.fretboard-glyph > [data-pos$='1'] { top: var(--row-origin); }
.fretboard-glyph > [data-pos$='2'] { top: calc(var(--row-origin) + var(--gap)); }
.fretboard-glyph > [data-pos$='3'] { top: calc(var(--row-origin) + var(--gap) * 2); }
.fretboard-glyph > [data-pos$='4'] { top: calc(var(--row-origin) + var(--gap) * 3); }
</style>

<div class="fretboard-glyph" aria-label="Open C major chord diagram">
  <span data-pos="L1">1</span>
  <span data-pos="L2">2</span>
  <span data-pos="L3">3</span>
  <span data-pos="L4">4</span>
  <span data-pos="EH">E</span>
  <span data-pos="E0">✕</span>
  <span data-pos="AH">A</span>
  <span data-pos="A3">●</span>
  <span data-pos="DH">D</span>
  <span data-pos="D2">●</span>
  <span data-pos="GH">G</span>
  <span data-pos="G0">◯</span>
  <span data-pos="BH">B</span>
  <span data-pos="B1">●</span>
  <span data-pos="eH">e</span>
  <span data-pos="e0">◯</span>
</div>

```html
<style>
.fretboard-glyph {
  --glyph-scale: 7rem;
  --column-origin: calc(1.2rem + var(--glyph-scale) * 137 / 2000); /* left inset, source units */
  --gap: calc(var(--glyph-scale) * 172 / 1000); /* source units */
  --row-origin: calc(0.9rem + var(--glyph-scale) * 503 / 2000); /* top inset, source units */
  margin: 1rem 0;
  width: 8.7rem; /* fret-label column plus six-string glyph */
  height: 8.8rem; /* header, open row, four frets, bottom line */
  display: inline-block;
  position: relative;
}

.fretboard-glyph::before {
  content: '\1D11C'; /* MUSICAL SYMBOL SIX-STRING FRETBOARD */
  color: currentColor;
  font: var(--glyph-scale)/1 'Noto Music', sans-serif;
  left: 1.2rem; /* left inset */
  opacity: 0.32; /* fade glyph behind the marks */
  pointer-events: none;
  position: absolute;
  top: 0.9rem; /* top inset */
  z-index: 0;
}

.fretboard-glyph > span {
  font: 0.95rem/1 monospace; /* overlay text size and leading */
  position: absolute;
  transform: translate(-50%, -50%);
  z-index: 1;
}
.fretboard-glyph > [data-pos^='L'] { left: 0.3rem; transform: translateY(-50%); /* fret-label column */ }
.fretboard-glyph > [data-pos^='E'] { left: var(--column-origin); }
.fretboard-glyph > [data-pos^='A'] { left: calc(var(--column-origin) + var(--gap)); }
.fretboard-glyph > [data-pos^='D'] { left: calc(var(--column-origin) + var(--gap) * 2); }
.fretboard-glyph > [data-pos^='G'] { left: calc(var(--column-origin) + var(--gap) * 3); }
.fretboard-glyph > [data-pos^='B'] { left: calc(var(--column-origin) + var(--gap) * 4); }
.fretboard-glyph > [data-pos^='e'] { left: calc(var(--column-origin) + var(--gap) * 5); }
.fretboard-glyph > [data-pos$='H'] { top: 0.45rem; /* top inset - header adjustment */ }
.fretboard-glyph > [data-pos$='0'] { top: 1.2rem; /* top inset + nut adjustment */ }
.fretboard-glyph > [data-pos$='1'] { top: var(--row-origin); }
.fretboard-glyph > [data-pos$='2'] { top: calc(var(--row-origin) + var(--gap)); }
.fretboard-glyph > [data-pos$='3'] { top: calc(var(--row-origin) + var(--gap) * 2); }
.fretboard-glyph > [data-pos$='4'] { top: calc(var(--row-origin) + var(--gap) * 3); }
</style>

<div class="fretboard-glyph" aria-label="Open C major chord diagram">
  <span data-pos="L1">1</span>
  <span data-pos="L2">2</span>
  <span data-pos="L3">3</span>
  <span data-pos="L4">4</span>
  <span data-pos="EH">E</span>
  <span data-pos="E0">✕</span>
  <span data-pos="AH">A</span>
  <span data-pos="A3">●</span>
  <span data-pos="DH">D</span>
  <span data-pos="D2">●</span>
  <span data-pos="GH">G</span>
  <span data-pos="G0">◯</span>
  <span data-pos="BH">B</span>
  <span data-pos="B1">●</span>
  <span data-pos="eH">e</span>
  <span data-pos="e0">◯</span>
</div>
```

These approaches also apply to musical staves.
