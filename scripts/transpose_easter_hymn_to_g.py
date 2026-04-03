"""Transpose the downloaded Easter Hymn ABC from D to G."""

import re
from pathlib import Path

src = Path('tmp-easter-hymn.abc')
dst = Path('tmp-easter-hymn-in-g.abc')

text = src.read_text()
text = text.replace('K:D', 'K:G')

chords = {'"D"': '"G"', '"G"': '"C"', '"A"': '"D"', '"E7"': '"A7"'}
for old, new in chords.items():
    text = text.replace(old, new)

notes = {
    'D': 'G',
    'E': 'A',
    'F': 'B',
    'G': 'c',
    'A': 'd',
    'B': 'e',
    'c': 'f',
    'd': 'g',
    'e': 'a',
    'f': 'b',
}


def transpose_note(match: re.Match[str]) -> str:
    note = match.group('note')
    return f'{notes[note]}{match.group("length")}'


lines = []
for raw_line in text.splitlines():
    line = raw_line
    if raw_line.startswith(('"', '|', '[')) or re.match(r'^[A-Ga-fzZ]', raw_line):
        parts = raw_line.split('"')
        for index, part in enumerate(parts):
            if index % 2 == 0:
                parts[index] = re.sub(
                    r'(?P<note>[A-Ga-f])(?P<length>\d*/?\d*)', transpose_note, part
                )
        line = '"'.join(parts)
    lines.append(line)

text = '\n'.join(lines) + '\n'
dst.write_text(text)
