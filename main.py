"""MkDocs macros for the hymn lead sheet."""

from functools import reduce
from re import sub

from markupsafe import Markup
from mkdocs_macros.plugin import MacrosPlugin

chords = {
    'Am': {'E0': '✕', 'A0': '◯', 'D2': '●', 'G2': '●', 'B1': '●', 'e0': '◯'},
    'C': {'E0': '✕', 'A3': '●', 'D2': '●', 'G0': '◯', 'B1': '●', 'e0': '◯'},
    'D': {'E0': '✕', 'A0': '✕', 'D0': '◯', 'G2': '●', 'B3': '●', 'e2': '●'},
    'D7': {'E0': '✕', 'A0': '✕', 'D0': '◯', 'G2': '●', 'B1': '●', 'e2': '●'},
    'G': {'E3': '●', 'A2': '●', 'D0': '◯', 'G0': '◯', 'B0': '◯', 'e3': '●'},
}
symbols = {'21': '!', '22': '"', '27': "'", '2c': ',', '2d': '-', '2e': '.', '3b': ';', '3f': '?'}


def define_env(env: MacrosPlugin) -> None:
    @env.macro
    def lead_line(**cells: str) -> Markup:  # pyright: ignore[reportUnusedFunction]
        return Markup(  # noqa: S704
            f'<p class="lead-line">{
                "".join(
                    (
                        '<span class="cell">'
                        f'<span class="chord-box" aria-label="{chord} chord diagram" '
                        f'data-chord="{chord}">'
                        + "".join(
                            f'<span data-pos="{position}">{mark}</span>'
                            for position, mark in chords[chord].items()
                        )
                        + "</span>"
                        + '<span class="lyric">'
                        + "".join(
                            sub(
                                r"\s*'\s*",
                                "'",
                                sub(
                                    r"\s*-\s*",
                                    "-",
                                    sub(
                                        r"\s+([,!?])",
                                        r"\1",
                                        " ".join(
                                            reduce(
                                                lambda text, symbol: text.replace(*symbol),
                                                symbols.items(),
                                                token,
                                            )
                                            for token in lyric.split("_")
                                        ),
                                    ),
                                ),
                            )
                        )
                        + "</span>"
                        + "</span>"
                    )
                    for lyric, chord in cells.items()
                )
            }</p>'
        )
