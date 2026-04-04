---
date: 2026-04-03
slug: christ-the-lord-is-risen-today
---

# Christ the Lord Is Risen Today

The [last post](/ton/blog/2026/03/29/fretboard-diagrams/) walked through ASCII art, CSS grids, sparse position markup, and the Unicode
fretboard glyph. For a full seasonal song, this version uses the glyph-and-position approach with
build-time templating, so concise source expands into a somewhat verbose HTML page.

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Music&family=Source+Serif+4:wght@400;600&display=swap');

.hymn-sheet {
  font-family: 'Source Serif 4', serif;
  font-size: 1.08rem;
  line-height: 1.7;
}

.verse { margin: 1.5rem 0; }

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

In G:

Try one of these 4/4 strumming patterns:

- `↓  ↓↑  ↑↓↑`
- `↓  ↓  ↓↑  ↓↑`

<div class="hymn-sheet">
  <div class="verse" aria-label="Verse 1">
    {{ lead_line(Christ_the_Lord_is='G', risen_to_day_2d='C', ay_2c_a_2d='G', al_2d='C', le_2d='C', lu_2d='G', u_2d='D7', ia_21='G') }}
    {{ lead_line(Sons_of_men_and='C', angels='Am', say_2d='G', ay='D7', _2c_a_2d='G', al_2d='C', le_2d='C', lu_2d='G', u_2d='D7', ia_21='G') }}
    {{ lead_line(Raise_your_joys_and='D7', try_2d='G', umphs_2c='D7', high_2c='G', a_2d='D7', al_2d='C', le_2d='C', lu_2d='D7', u_2d='C', ia_21='G') }}
    {{ lead_line(Sing_2c_ye_heavens_2c_and='G', earth_re_2d_ply_2d='C', y_2c_a_2d='G', al_2d='C', le_2d='C', lu_2d='G', u_2d='D7', ia_21='G') }}
  </div>

  <div class="verse" aria-label="Verse 2">
    {{ lead_line(Lives_again_our='G', glorious_Ki_2d='C', ing_2c_a_2d='G', al_2d='C', le_2d='C', lu_2d='G', u_2d='D7', ia_21='G') }}
    {{ lead_line(Where_2c_O_death_2c_is='C', now_thy='Am', sti_2d='G', ing_3f='D7', A_2d='G', al_2d='C', le_2d='C', lu_2d='G', u_2d='D7', ia_21='G') }}
    {{ lead_line(Once_He_died_our='D7', souls='G', to='D7', save_2c='G', a_2d='D7', al_2d='C', le_2d='C', lu_2d='D7', u_2d='C', ia_21='G') }}
    {{ lead_line(Where_thy_victory_2c='G', O='C', grave_3f_a_2d='G', al_2d='C', le_2d='C', lu_2d='G', u_2d='D7', ia_21='G') }}
  </div>

  <div class="verse" aria-label="Verse 3">
    {{ lead_line(Love_27_s_redeeming='G', work_is='C', done_2c_a_2d='G', al_2d='C', le_2d='C', lu_2d='G', u_2d='D7', ia_21='G') }}
    {{ lead_line(Fought_the_fight_2c_the='C', battle='Am', won_2d='G', on_2c_a_2d='D7', al_2d='G', le_2d='G', lu_2d='C', u_2d='G', ia_21='D7', _='G') }}
    {{ lead_line(Death_in_vain_for='D7', bids='G', Him='D7', rise_2c='G', a_2d='D7', al_2d='C', le_2d='C', lu_2d='D7', u_2d='C', ia_21='G') }}
    {{ lead_line(Christ_hath_opened='G', para='C', dise_2c_a_2d='G', al_2d='C', le_2d='C', lu_2d='G', u_2d='D7', ia_21='G') }}
  </div>
</div>

For hymn background, [this United Methodist Church history note](https://www.umcdiscipleship.org/articles/history-of-hymns-christ-the-lord-is-risen-today)
is a good companion to the lead sheet.

The first line in the source looks like this:

{% raw %}

```jinja
{{
    lead_line(
        Christ_the_Lord_is='G',
        risen_to_day_2d='C',
        ay_2c_a_2d='G',
        al_2d='C',
        le_2d='C',
        lu_2d='G',
        u_2d='D7',
        ia_21='G',
    )
}}
```

{% endraw %}

That expands at build time into HTML like this:

```html
<p class="lead-line">
    <span class="cell">
        <span class="chord-box" aria-label="G chord diagram" data-chord="G">
            <span data-pos="E3">●</span>
            <span data-pos="A2">●</span>
            <span data-pos="D0">◯</span>
            <span data-pos="G0">◯</span>
            <span data-pos="B0">◯</span>
            <span data-pos="e3">●</span>
        </span>
        <span class="lyric">Christ the Lord is</span>
    </span>
    <span class="cell">
        <span class="chord-box" aria-label="C chord diagram" data-chord="C">
            <span data-pos="E0">✕</span>
            <span data-pos="A3">●</span>
            <span data-pos="D2">●</span>
            <span data-pos="G0">◯</span>
            <span data-pos="B1">●</span>
            <span data-pos="e0">◯</span>
        </span>
        <span class="lyric">risen to day-</span>
    </span>
    <span class="cell">
        <span class="chord-box" aria-label="G chord diagram" data-chord="G">
            <span data-pos="E3">●</span>
            <span data-pos="A2">●</span>
            <span data-pos="D0">◯</span>
            <span data-pos="G0">◯</span>
            <span data-pos="B0">◯</span>
            <span data-pos="e3">●</span>
        </span>
        <span class="lyric">ay, a-</span>
    </span>
    <span class="cell">
        <span class="chord-box" aria-label="C chord diagram" data-chord="C">
            <span data-pos="E0">✕</span>
            <span data-pos="A3">●</span>
            <span data-pos="D2">●</span>
            <span data-pos="G0">◯</span>
            <span data-pos="B1">●</span>
            <span data-pos="e0">◯</span>
        </span>
        <span class="lyric">al-</span>
    </span>
    <span class="cell">
        <span class="chord-box" aria-label="C chord diagram" data-chord="C">
            <span data-pos="E0">✕</span>
            <span data-pos="A3">●</span>
            <span data-pos="D2">●</span>
            <span data-pos="G0">◯</span>
            <span data-pos="B1">●</span>
            <span data-pos="e0">◯</span>
        </span>
        <span class="lyric">le-</span>
    </span>
    <span class="cell">
        <span class="chord-box" aria-label="G chord diagram" data-chord="G">
            <span data-pos="E3">●</span>
            <span data-pos="A2">●</span>
            <span data-pos="D0">◯</span>
            <span data-pos="G0">◯</span>
            <span data-pos="B0">◯</span>
            <span data-pos="e3">●</span>
        </span>
        <span class="lyric">lu-</span>
    </span>
    <span class="cell">
        <span class="chord-box" aria-label="D7 chord diagram" data-chord="D7">
            <span data-pos="E0">✕</span>
            <span data-pos="A0">✕</span>
            <span data-pos="D0">◯</span>
            <span data-pos="G2">●</span>
            <span data-pos="B1">●</span>
            <span data-pos="e2">●</span>
        </span>
        <span class="lyric">u-</span>
    </span>
    <span class="cell">
        <span class="chord-box" aria-label="G chord diagram" data-chord="G">
            <span data-pos="E3">●</span>
            <span data-pos="A2">●</span>
            <span data-pos="D0">◯</span>
            <span data-pos="G0">◯</span>
            <span data-pos="B0">◯</span>
            <span data-pos="e3">●</span>
        </span>
        <span class="lyric">ia!</span>
    </span>
</p>
```

Happy Easter!
