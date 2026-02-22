---
date: 2026-02-22
---

# Wide Key=Value Logging

Wide `key=value` logging keeps information explicit, compact, and searchable without pretending
to be prose. It favors named fields over free-form text and avoids the complexity and visual
noise of JavaScript Object Notation (JSON). [Brandur wrote about logfmt](https://brandur.org/logfmt)
in 2013: stable keys, small values, one request or task per line. Another description I've
thought is appropriate for this format is "Wide INI (WINI)". In `grep`, `journalctl`, or Papertrail,
`st=5` catches status codes 500..599 inclusive--with no parser in the loop. Structlog exposes
[KV renderer](https://www.structlog.org/en/stable/api.html#structlog.processors.KeyValueRenderer)
and [logfmt](https://www.structlog.org/en/stable/api.html#structlog.processors.LogfmtRenderer)
for this style directly, and so does [go-kit/log](https://github.com/go-kit/log).

Fewer lines are better, and one line per request or task is the ideal.
[Canonical log lines](https://brandur.org/canonical-log-lines) makes that operational case well:
coherent context, easier streaming, and cleaner copy-paste to record incident details.
Multi-line logs make key consistency harder to maintain.
[LoggingSucks](https://loggingsucks.com/) reaches the same practical conclusion from another
angle: wide single-line records make debugging and operations efficient, although that author's
unexplained choice of JSON over `key=value` for everyday logs adds punctuation and tool requirements
where clarity should win.
LTSV ([ltsv.org](https://ltsv.org/)) shows the same one-line, labeled-fields shape, differing
mainly in separators: `:` instead of `=` and `\t` instead of ` `.
