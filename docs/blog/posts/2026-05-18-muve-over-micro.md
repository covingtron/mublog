---
date: 2026-05-18
slug: muve-over-micro
---

Thanks @dylwil3 for looking into this. Tagging @Skylion007, @MichaReiser, and @AlexWaygood to continue the conversation started on https://github.com/astral-sh/ruff/pull/14403.

### A general thought
I wonder if line-and-character-specific ignores, similar to `type: ignore[operator]`, could help with adoption of `RUF001`, `RUF002`, and `RUF003`:

```
sigma = 'σ'  # noqa: RUF001[σ]
```

### Specific responses to the previous thread
> The main example encountered in an ecosystem check is the Greek letter μ

I'm confused by the bokeh hit listed in https://github.com/astral-sh/ruff/pull/14403#issuecomment-2481411110

I thought I already fixed it in https://github.com/bokeh/bokeh/pull/13668/files

> [mu] may be used as a variable name (in which case one wants the Greek letter U+03BC)

Agreed. I recently experimented with an example and learned that [PLC2401](https://docs.astral.sh/ruff/rules/non-ascii-name/) seems to be the rule for code, and it seems to flag all non-ASCII characters. Perhaps there is an opportunity use the "confusables" list for that rule.

> or as part of an SI unit like µs (in which case one wants the "micro" symbol U+00B5).

Why not abbreviate microseconds with mu μ `\u03bc`?

The Pandas project [already abbreviates microfarads like that](https://github.com/pandas-dev/pandas/blob/513e78760a8faee6723908ca23ea83dcabc5dd77/pandas/tests/computation/test_eval.py#L192). I'm pretty sure ipython is the source of the microseconds code timing strings in the comments of pandas, and [the ipython maintainer was willing to switch](https://github.com/ipython/ipython/pull/14426/files) from micro µ `\u00b5` to mu μ `\u03bc`. My [pandas enhancement](https://github.com/pandas-dev/pandas/issues/58472) accepting mu in addition to micro in their from-scratch miniature units library remains unfortunately attention starved. A more narrowly scoped tooling fixes change would likely race through review.

But now for the feature presentation...

### Mutwo Strikes Back.

My TL;DR is that character codes are messy; where possible, [NFKC normalize like Python](https://stackoverflow.com/a/50128375/3787516) to tidy them up.

The error that motivated me to work on this was the accidental mixup of mu μ `\u03bc` and micro µ `\u00b5` characters in a Python Django codebase and PostgreSQL database. Duplication accidentally arose in a units table created by data migrations copying string literals from Python code into database rows. At first I thought the database schema just needed a unique constraint on the abbreviation to surface and prevent the problem, but that didn't work. Different developers working at different times had copied and pasted different encodings that looked identical. I would like to help develop autoformatting that prevents this class of error. I did not begin this journey with a favorite character encoding, just with the determination that there could only be one. (Latin lowercase u remains a possible source of mixup, but at least it has many different pixels.)

Digging deeper, I've learned several things.

#### Keyboards
IBM's [azerty](https://en.wikipedia.org/wiki/AZERTY) keyboard for France and Belgium seems like the origin of the micro µ `\u00b5` character and reason for its early encoding separate from the other Greek characters. [qwertz](https://en.wikipedia.org/wiki/QWERTZ) also includes a micro key. The [Greek keyboard layout](https://en.wikiversity.org/wiki/Enabling_Greek_Characters_on_Your_Keyboard) generates mu μ `\u03bc`. Keycode conversion in either direction is possible but not widespread.

#### Confusion
I'm not sure if science/measurement groups are aligned on the topic or have put much thought into character encodings. As of March 2025, I see micro µ `\u00b5` on https://www.bipm.org/en/measurement-units/si-prefixes but mu μ `\u03bc` on https://www.nist.gov/pml/owm/metric-si-prefixes. Within the SI brochure PDF I see both encodings:
```
pdfgrep -o '[μµ]' ~/Downloads/SI-Brochure-9-EN.pdf | python -c 'import fileinput; from collections import Counter
for key, value in Counter([mu.strip() for mu in fileinput.input()]).items():
    print(f"{hex(ord(key))}: {value}")'
0x3bc: 12
0xb5: 16
```
If anyone finds a useful explanation from groups like these, or anyone really, of the benefits of multiple different encodings, or the relative merits of one encoding over another, I'd be interested in reading them.

Unicode Consortium ($5 000 to contribute, $50 000 to cast a full vote) documents vary:

[Technical Report 25](http://www.unicode.org/reports/tr25) last updated 2017:

> 2.5 Duplicated Characters
>
> Some Greek letters are encoded elsewhere as technical symbols. These include U+00B5 µ
> MICRO SIGN, U+2126 Ω OHM SIGN, and several characters among the APL functional symbols in
> the Miscellaneous Technical block. U+03A9 Ω GREEK LETTER CAPITAL OMEGA is the canonical
> equivalent of U+2126 Ω and its use is preferred. Micro sign is included in several parts of
> ISO/IEC 8859, and therefore supported in many legacy environments where U+03BC μ
> GREEK LETTER SMALL MU is not available. Implementations therefore need to be able to recog-
> nize the micro sign, even though U+03BC μ is the preferred character in a Unicode context.

[Unicode 16 Core Spec](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-7/#G12477) last updated 2025:

> Greek Letters as Symbols. The use of Greek letters for mathematical variables and operators is well established. Characters from the Greek block may be used for these symbols.
>
> For compatibility purposes, a few Greek letters are separately encoded as symbols in other character blocks. Examples include U+00B5
> µ MICRO SIGN in the Latin-1 Supplement character block and U+2126 Ω OHM SIGN in the Letterlike Symbols character block. The ohm sign is canonically equivalent to the capital omega, and normalization would remove any distinction. Its use is therefore discouraged in favor of capital omega. The same equivalence does not exist between micro sign and mu, and use of either character as a micro sign is common. For Greek text, only the mu should be used.

[Edit: I don't understand why these authors write about non-existence of _canonical_ equivalence rather than the existence of _compatibility_ equivalence.]

On Wikipedia ($0 to contribute), the [Mu page](https://en.wikipedia.org/wiki/Mu_(letter)#Unicode) and [micro- page](https://en.wikipedia.org/wiki/Micro-#Symbol_encoding_in_character_sets) [edit: previously seemed to disagree but have since been updated by me and maybe others].

#### Kompatability
> [K]ompatibility equivalence is a weaker type of equivalence [than canonical equivalence] between characters or sequences of characters which represent the same abstract character (or sequence of abstract characters), but which may have distinct visual appearances or behaviors. The visual appearances of the compatibility equivalent forms typically constitute a subset of the expected range of visual appearances of the character (or sequence of characters) they are equivalent to. However, these variant forms may represent a visual distinction that is significant in some textual contexts, but not in others. As a result, greater care is required to determine when use of a compatibility equivalent is appropriate. If the visual distinction is stylistic, then markup or styling could be used to represent the formatting information. However, some characters with compatibility decompositions are used in mathematical notation to represent a distinction of a semantic nature; replacing the use of distinct character codes by formatting in such contexts may cause problems.

Mu μ `\u03bc` is the Kompatability equivalent (NFKD and NFKC) of micro µ `\u00b5`:

https://github.com/unicode-org/icu/blob/30e23b0d286f87fefb161dc56e90afac5df0dc43/icu4c/source/data/unidata/norm2/nfkc_scf.txt#L63
```
00B5>03BC
```

https://www.unicode.org/charts/PDF/U0080.pdf
> 00B5 μ MICRO SIGN
> ≈ 03BC μ greek small letter mu

While micro and mu "may have distinct visual appearances or behaviors", they are frequently indistinct: [Google fonts comparison of mu and micro](https://fonts.google.com/?preview.text=mu%20%CE%BC%20micro%20%C2%B5&preview.size=20&preview.layout=grid&categoryFilters=Feeling:%2FExpressive%2FBusiness).

#### Code
Since [PEP-3131](https://peps.python.org/pep-3131/) was implemented, Python allows both mu μ `\u03bc` and micro µ `\u00b5` as identifiers, but the underlying NFKC normalization means only the former will work reliably.
```shell
python -c 'print("""class C:
    \xb5=1
print(hex(ord(dir(C)[-1])))""")' | tee /dev/fd/2 | python -
```
```python
class C:
    µ=1
print(hex(ord(dir(C)[-1])))
```
```shell
0x3bc
```

See https://stackoverflow.com/q/34097193/3787516 for a getattr failure that autofixing micro to mu can prevent.

#### Conclusion
For the people that want to limit their .py files to unambiguous characters only, PEP-3131 replaces micro µ `\u00b5`  with mu μ `\u03bc`. Or dare I say: muve over, micro.
