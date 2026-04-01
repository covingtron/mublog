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
</style>

Unicode includes an empty four-string fretboard, [<span class="noto-music">&#x1D11D;</span>](https://codepoints.net/U+1D11D), for
ukulele, and an empty six-string fretboard, [<span class="noto-music">&#x1D11C;</span>](https://codepoints.net/U+1D11C), for guitar.
How are people supposed to compose the fretboard background and marks like ●, ◯, and ✕?

One approach that I'm experimenting with is using multiple lines: one column per string, one row
per fret, top markers for muted and open strings, and filled dots placed inside the grid where
fingers land.

Open C major: `x32010`

<div style="font-family: monospace; line-height: 1.275; white-space: pre">
  E   A   D   G   B   e
  ✕           ◯       ◯
  ┌───┬───┬───┬───┬───┐
0 │   │   │   │   │   │
  ├───┼───┼───┼───┼───┤
1 │   │   │   │   ●   │
  ├───┼───┼───┼───┼───┤
2 │   │   ●   │   │   │
  ├───┼───┼───┼───┼───┤
3 │   ●   │   │   │   │
  └───┴───┴───┴───┴───┘
</div>

This needed an inline `div` with `white-space: pre` and a tuned `line-height` to reduce the
vertical gaps, though there are probably better ways to do it.

```html
<div style="font-family: monospace; line-height: 1.275; white-space: pre">
  E   A   D   G   B   e
  ✕           ◯       ◯
  ┌───┬───┬───┬───┬───┐
0 │   │   │   │   │   │
  ├───┼───┼───┼───┼───┤
1 │   │   │   │   ●   │
  ├───┼───┼───┼───┼───┤
2 │   │   ●   │   │   │
  ├───┼───┼───┼───┼───┤
3 │   ●   │   │   │   │
  └───┴───┴───┴───┴───┘
</div>
```

This approach can probably also be applied to musical staves.
