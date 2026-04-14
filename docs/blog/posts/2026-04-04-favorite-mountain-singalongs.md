---
date: 2026-04-04
slug: favorite-mountain-singalongs
---

# Favorite Mountain Singalongs

Two mountain songs work well with the same three open chords. This version keeps both in G, so a
group can stay on `G`, `C`, and `D7` all the way through.

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Music&family=Source+Serif+4:wght@400;600&display=swap');

.song-sheet {
  font-family: 'Source Serif 4', serif;
  font-size: 1.08rem;
  line-height: 1.7;
}

.song {
  margin: 2rem 0;
}

.verse {
  margin: 1.25rem 0;
}

.chord-box {
  --glyph-scale: 3.4rem;
  --column-origin: calc(var(--glyph-scale) * 137 / 2000);
  --gap: calc(var(--glyph-scale) * 172 / 1000);
  --row-origin: calc(0.16rem + var(--glyph-scale) * 503 / 2000);
  display: inline-block;
  position: relative;
  margin: 0 0 0.1rem;
  width: 3.2rem;
  height: 4.25rem;
  font: 0.72rem/1 monospace;
}

.chord-box::before {
  content: '\1D11C';
  color: currentColor;
  font: var(--glyph-scale)/1 'Noto Music', sans-serif;
  left: 0;
  opacity: 0.4;
  pointer-events: none;
  position: absolute;
  top: 0.1rem;
  z-index: 0;
}

.chord-box > span {
  position: absolute;
  transform: translate(-50%, -50%);
  z-index: 1;
}

.chord-box::after {
  content: attr(data-chord);
  left: 50%;
  position: absolute;
  top: 3.75rem;
  transform: translate(-50%, 0);
  z-index: 1;
}

.chord-box > [data-pos^='E'] { left: var(--column-origin); }
.chord-box > [data-pos^='A'] { left: calc(var(--column-origin) + var(--gap)); }
.chord-box > [data-pos^='D'] { left: calc(var(--column-origin) + var(--gap) * 2); }
.chord-box > [data-pos^='G'] { left: calc(var(--column-origin) + var(--gap) * 3); }
.chord-box > [data-pos^='B'] { left: calc(var(--column-origin) + var(--gap) * 4); }
.chord-box > [data-pos^='e'] { left: calc(var(--column-origin) + var(--gap) * 5); }
.chord-box > [data-pos$='0'] { top: 0.46rem; }
.chord-box > [data-pos$='1'] { top: var(--row-origin); }
.chord-box > [data-pos$='2'] { top: calc(var(--row-origin) + var(--gap)); }
.chord-box > [data-pos$='3'] { top: calc(var(--row-origin) + var(--gap) * 2); }
.chord-box > [data-pos$='4'] { top: calc(var(--row-origin) + var(--gap) * 3); }

.lead-line {
  display: inline-grid;
  grid-auto-columns: max-content;
  grid-auto-flow: column;
  align-items: end;
  column-gap: 0.15rem;
  margin: 0.8rem 0;
}

.cell {
  border: 1px solid #1e5aa8;
  border-radius: 0.25rem;
  display: grid;
  grid-template-rows: auto auto;
  justify-items: start;
  padding: 0.15rem;
}

.lyric {
  min-height: 1.6em;
  padding: 0 0.2rem;
  white-space: pre;
}
</style>

Try `↓  ↓↑  ↑↓↑` all the way through, or just keep a steady down-strum if the room is loud.

<div class="song-sheet">
  <section class="song" aria-labelledby="bear">
    <h2 id="bear">The Bear Went Over the Mountain</h2>

    <div class="verse" aria-label="Verse 1">
      {{ lead_line(The_bear_went_o='G', ver_the='G', moun_2d='C', tain='G') }}
      {{ lead_line(The_bear_went_o='G', ver_the='G', moun_2d='C', tain='G') }}
      {{ lead_line(The_bear_went_o='G', ver_the='G', moun_2d='C', tain='G') }}
      {{ lead_line(To_see='G', what_he='D7', could='G', see='G') }}
    </div>

    <div class="verse" aria-label="Verse 2">
      {{ lead_line(And_all='G', that_he='D7', could='G', see='G') }}
      {{ lead_line(And_all='G', that_he='D7', could='G', see='G') }}
      {{ lead_line(And_all='G', that_he='D7', could='G', see='G') }}
      {{ lead_line(Was_the='G', other_side='G', of_the='D7', moun_2d_tain='G') }}
    </div>
  </section>

  <section class="song" aria-labelledby="coming-round">
    <h2 id="coming-round">She'll Be Coming 'Round the Mountain</h2>

    <div class="verse" aria-label="Chorus">
      {{ lead_line(She_27_ll_be_com='G', ing_27_round_the='G', moun_2d='C', tain='G', when_she='D7', comes='G') }}
      {{ lead_line(She_27_ll_be_com='G', ing_27_round_the='G', moun_2d='C', tain='G', when_she='D7', comes='G') }}
      {{ lead_line(She_27_ll_be_com='G', ing_27_round_the='G', moun_2d='C', tain='G') }}
      {{ lead_line(She_27_ll_be_com='G', ing_27_round_the='G', moun_2d='C', tain='G') }}
      {{ lead_line(She_27_ll_be_com='G', ing_27_round_the='G', moun_2d='C', tain='G', when_she='D7', comes='G') }}
    </div>
  </section>
</div>

If you want a little more motion, hold `D7` on the last cell, then turn back to `G` as the next
line starts.
