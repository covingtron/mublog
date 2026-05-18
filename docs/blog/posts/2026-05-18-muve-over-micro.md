---
date: 2026-05-18
slug: muve-over-micro
---

# Muve Over, Micro

I ran into a bug caused by accidental mixing of mu `μ` `\u03bc` and micro `µ` `\u00b5`
in Python and PostgreSQL. Different developers working at different times had copied and
pasted different encodings that looked identical. Duplication appeared in a units table
created by data migrations copying string literals from Python code into database rows.
At first I thought the database schema just needed a unique constraint on the abbreviation
to surface and prevent the problem, but that did not work. The strings were different
bytes.

I did not begin this journey with a favorite character encoding, just with the
determination that there could only be one.

## Normalize When You Can

My TL;DR is that character codes are messy; where possible,
[NFKC normalize like Python](https://stackoverflow.com/a/50128375/3787516) to tidy them
up.

Since [PEP-3131](https://peps.python.org/pep-3131/) was implemented, Python allows both
mu `μ` `\u03bc` and micro `µ` `\u00b5` as identifiers, but the underlying NFKC
normalization means only the former will work reliably.

```shell
python -c 'print("""class C:
    \xb5=1
print(hex(ord(dir(C)[-1])))""")' | tee /dev/fd/2 | python -
```

```python
class C:
    µ = 1
print(hex(ord(dir(C)[-1])))
```

```shell
0x3bc
```

See [this Stack Overflow question](https://stackoverflow.com/q/34097193/3787516) for a
`getattr` failure that autofixing micro to mu can prevent.

For the people that want to limit their `.py` files to unambiguous characters only,
Python already leans toward replacing micro `µ` `\u00b5` with mu `μ` `\u03bc`.

## Why Not Use Mu for Micro?

In the [Ruff discussion that prompted this post](https://github.com/astral-sh/ruff/issues/14433#issuecomment-2712443359),
the motivating example was the Greek letter mu.

If a name is code, [PLC2401](https://docs.astral.sh/ruff/rules/non-ascii-name/) seems
closer to the right rule than a generic confusables check, because it flags all non-ASCII
characters. There may be room to use the confusables list there too.

If a name is a unit abbreviation like microseconds, why not abbreviate with mu `μ`
`\u03bc`?

The Pandas project
[already abbreviates microfarads that way](https://github.com/pandas-dev/pandas/blob/513e78760a8faee6723908ca23ea83dcabc5dd77/pandas/tests/computation/test_eval.py#L192).
I am pretty sure IPython is the source of the microseconds timing strings in pandas
comments, and [the IPython maintainer was willing to switch](https://github.com/ipython/ipython/pull/14426/files)
from micro `µ` `\u00b5` to mu `μ` `\u03bc`. My
[pandas enhancement](https://github.com/pandas-dev/pandas/issues/58472) to accept mu in
addition to micro in their miniature units library remains attention-starved, but a
narrower tooling fix would likely race through review.

## Keyboards

IBM's [AZERTY](https://en.wikipedia.org/wiki/AZERTY) keyboard for France and Belgium
seems like the origin of the micro `µ` `\u00b5` character and a reason for its early
separate encoding from the Greek alphabet. [QWERTZ](https://en.wikipedia.org/wiki/QWERTZ)
also includes a micro key. The
[Greek keyboard layout](https://en.wikiversity.org/wiki/Enabling_Greek_Characters_on_Your_Keyboard)
generates mu `μ` `\u03bc`. Keycode conversion in either direction is possible but not
widespread.

## Standards Bodies Do Not Agree

I am not sure science and measurement groups are aligned on the topic, or have put much
thought into character encodings at all.

As of March 2025, I saw micro `µ` `\u00b5` on
[BIPM's SI prefixes page](https://www.bipm.org/en/measurement-units/si-prefixes)
but mu `μ` `\u03bc` on
[NIST's metric SI prefixes page](https://www.nist.gov/pml/owm/metric-si-prefixes).
Within the SI brochure PDF I found both encodings:

```shell
pdfgrep -o '[μµ]' ~/Downloads/SI-Brochure-9-EN.pdf | python -c 'import fileinput; from collections import Counter
for key, value in Counter([mu.strip() for mu in fileinput.input()]).items():
    print(f"{hex(ord(key))}: {value}")'
0x3bc: 12
0xb5: 16
```

If anyone finds a useful explanation from groups like these, or anyone really, of the
benefits of multiple different encodings, or the relative merits of one encoding over
another, I would be interested in reading it.

Unicode documents also vary.

[Technical Report 25](http://www.unicode.org/reports/tr25), last updated in 2017, says
micro sign exists largely for legacy compatibility and prefers mu in Unicode contexts.

[Unicode 16 Core Spec](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-7/#G12477),
last updated in 2025, says the ohm sign should give way to omega, but for micro sign and
mu, either is common as a micro sign while only mu should be used for Greek text.

I still do not understand why these authors talk about the non-existence of canonical
equivalence rather than the existence of compatibility equivalence.

## Compatibility Equivalence

Mu `μ` `\u03bc` is the compatibility equivalent of micro `µ` `\u00b5` under NFKD and
NFKC:

<https://github.com/unicode-org/icu/blob/30e23b0d286f87fefb161dc56e90afac5df0dc43/icu4c/source/data/unidata/norm2/nfkc_scf.txt#L63>

```text
00B5>03BC
```

<https://www.unicode.org/charts/PDF/U0080.pdf>

> 00B5 μ MICRO SIGN
> ≈ 03BC μ greek small letter mu

While micro and mu may have distinct visual appearances or behaviors, they are frequently
indistinct in practice:
[Google Fonts comparison of mu and micro](https://fonts.google.com/?preview.text=mu%20%CE%BC%20micro%20%C2%B5&preview.size=20&preview.layout=grid&categoryFilters=Feeling:%2FExpressive%2FBusiness).

## Conclusion

Character codes are messy. Normalize where possible. Prefer one encoding. Let tools
autofix when they can.

Or dare I say: muve over, micro.
