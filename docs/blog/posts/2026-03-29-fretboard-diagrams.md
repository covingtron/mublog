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
  grid-template-rows: repeat(5, 1.5rem);
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
    linear-gradient(currentColor, currentColor);
  background-position:
    2.25rem 3rem,
    2.25rem 4.5rem,
    2.25rem 6rem,
    2.25rem 7.5rem,
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
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem;
}

.fretboard-grid > span {
  display: grid;
  place-items: center;
}

.fretboard-pos {
  display: inline-grid;
  grid-template-columns: repeat(7, 1.5rem);
  grid-template-rows: repeat(5, 1.5rem);
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
    linear-gradient(currentColor, currentColor);
  background-position:
    2.25rem 3rem,
    2.25rem 4.5rem,
    2.25rem 6rem,
    2.25rem 7.5rem,
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
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem;
}

.fretboard-pos > span {
  display: grid;
  place-items: center;
}

.fretboard-pos > [data-pos^='L'] {
  grid-column: 1;
}

.fretboard-pos > [data-pos^='E'] {
  grid-column: 2;
}

.fretboard-pos > [data-pos^='A'] {
  grid-column: 3;
}

.fretboard-pos > [data-pos^='D'] {
  grid-column: 4;
}

.fretboard-pos > [data-pos^='G'] {
  grid-column: 5;
}

.fretboard-pos > [data-pos^='B'] {
  grid-column: 6;
}

.fretboard-pos > [data-pos^='e'] {
  grid-column: 7;
}

.fretboard-pos > [data-pos$='H'] {
  grid-row: 1;
}

.fretboard-pos > [data-pos$='0'] {
  grid-row: 2;
}

.fretboard-pos > [data-pos$='1'] {
  grid-row: 3;
}

.fretboard-pos > [data-pos$='2'] {
  grid-row: 4;
}

.fretboard-pos > [data-pos$='3'] {
  grid-row: 5;
}

</style>

Unicode includes an empty four-string fretboard, [<span class="noto-music">&#x1D11D;</span>](https://codepoints.net/U+1D11D), for
ukulele or bass, and an empty six-string fretboard, [<span class="noto-music">&#x1D11C;</span>](https://codepoints.net/U+1D11C), for guitar.
How are people supposed to compose the fretboard background and marks like ●, ◯, and ✕?

One approach that I'm experimenting with is using multiple lines: one column per string, one row
per fret, top markers for muted and open strings, and filled dots placed inside the grid where
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
  └───┴───┴───┴───┴───┘
</pre>

This needed a `pre` tag with a tuned `line-height` to reduce the
vertical gaps, though there are probably better ways to do it.

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
  └───┴───┴───┴───┴───┘
</pre>
```

A CSS grid diagram, or CSS-only chord box, looks like this:

<div class="fretboard-grid" aria-label="Open C major chord diagram">
  <span></span><span>E</span><span>A</span><span>D</span><span>G</span><span>B</span><span>e</span>
  <span></span><span>✕</span><span></span><span></span><span>◯</span><span></span><span>◯</span>
  <span>1</span><span></span><span></span><span></span><span></span><span>●</span><span></span>
  <span>2</span><span></span><span></span><span>●</span><span></span><span></span><span></span>
  <span>3</span><span></span><span>●</span><span></span><span></span><span></span><span></span>
</div>

```html
<style>
.fretboard-grid {
  display: inline-grid;
  grid-template-columns: repeat(7, 1.5rem);
  grid-template-rows: repeat(5, 1.5rem);
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
    linear-gradient(currentColor, currentColor);
  background-position:
    2.25rem 3rem,
    2.25rem 4.5rem,
    2.25rem 6rem,
    2.25rem 7.5rem,
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
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem;
}

.fretboard-grid > span {
  display: grid;
  place-items: center;
}

</style>

<div class="fretboard-grid" aria-label="Open C major chord diagram">
  <span></span><span>E</span><span>A</span><span>D</span><span>G</span><span>B</span><span>e</span>
  <span></span><span>✕</span><span></span><span></span><span>◯</span><span></span><span>◯</span>
  <span>1</span><span></span><span></span><span></span><span></span><span>●</span><span></span>
  <span>2</span><span></span><span></span><span>●</span><span></span><span></span><span></span>
  <span>3</span><span></span><span>●</span><span></span><span></span><span></span><span></span>
</div>
```

A sparse `data-pos` version can skip the empty cells. The CSS `^=` attribute selector matches the
starting string letter, and `$=` matches the ending row number, so `A3` decodes to the A string
and third fret. The string letters are supplemented with `L` and `R` for the left and right
margins, and the row numbers are supplemented with `H` for the header row and `0` for the nut
marker row, which holds muted-string marks `✕` and open-string marks `◯`.

<div class="fretboard-pos" aria-label="Open C major chord diagram">
  <span data-pos="L1">1</span>
  <span data-pos="L2">2</span>
  <span data-pos="L3">3</span>
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
  grid-template-rows: repeat(5, 1.5rem);
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
    linear-gradient(currentColor, currentColor);
  background-position:
    2.25rem 3rem,
    2.25rem 4.5rem,
    2.25rem 6rem,
    2.25rem 7.5rem,
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
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem,
    1px 4.5rem;
}

.fretboard-pos > span {
  display: grid;
  place-items: center;
}

.fretboard-pos > [data-pos^='L'] {
  grid-column: 1;
}

.fretboard-pos > [data-pos^='E'] {
  grid-column: 2;
}

.fretboard-pos > [data-pos^='A'] {
  grid-column: 3;
}

.fretboard-pos > [data-pos^='D'] {
  grid-column: 4;
}

.fretboard-pos > [data-pos^='G'] {
  grid-column: 5;
}

.fretboard-pos > [data-pos^='B'] {
  grid-column: 6;
}

.fretboard-pos > [data-pos^='e'] {
  grid-column: 7;
}

.fretboard-pos > [data-pos$='H'] {
  grid-row: 1;
}

.fretboard-pos > [data-pos$='0'] {
  grid-row: 2;
}

.fretboard-pos > [data-pos$='1'] {
  grid-row: 3;
}

.fretboard-pos > [data-pos$='2'] {
  grid-row: 4;
}

.fretboard-pos > [data-pos$='3'] {
  grid-row: 5;
}
</style>

<div class="fretboard-pos" aria-label="Open C major chord diagram">
  <span data-pos="L1">1</span>
  <span data-pos="L2">2</span>
  <span data-pos="L3">3</span>
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

These approaches can probably also be applied to musical staves.
