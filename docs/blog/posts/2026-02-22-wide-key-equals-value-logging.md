---
date: 2026-02-22
slug: wini-wide-key-equals-value-logging
---

# Wide Key `=` Equals Value Logging

## Key `=` Equals Value

Wide `key=value` logging keeps information explicit, compact, and searchable.
It uses named fields for most values; free-form text can still go on the right-hand side of
`msg=`. It also avoids the complexity and visual noise of JavaScript Object Notation (JSON).
[Labeled Tab Separated Values (LTSV)](http://ltsv.org) keeps the same
wide, one-line shape while using `:` colon and `\t` tab separators instead of `=` equals and ` ` space. [Brandur wrote
about logfmt](https://brandur.org/logfmt) in 2013: stable keys, small values, one request or task
per line. Another description I've
thought is appropriate for this format is "Wide INI (WINI)". In `grep`, `journalctl`, or Papertrail, searching for `st=5`
catches status codes 500..599 inclusive--with no parser in the loop. The Python structlog library exposes
[KV renderer](https://www.structlog.org/en/stable/api.html#structlog.processors.KeyValueRenderer)
and [logfmt](https://www.structlog.org/en/stable/api.html#structlog.processors.LogfmtRenderer)
for this style directly, and so does
[python-logfmter](https://github.com/josheppinette/python-logfmter).

| Format | Published | Structured | Key/Value | Element | Visually Noisy |
| ------ | --------- | ---------- | --------- | ------- | -------------- |
| Prose |  | No ❌ | None ❌ | `\n` newline ❌ | No ✅ |
| [INInitialization (INI)](https://en.wikipedia.org/wiki/INI_file) | 1980s | Yes ✅ | `=` equals ✅ | `\n` newline ❌ | No ✅ |
| [Common Log Format (CLF)](https://en.wikipedia.org/wiki/Common_Log_Format) | 1995 | No ❌ | None ❌ | ` ` space ✅ | 🤷 |
| [YAML Ain't Markup Language (YAML)](https://en.wikipedia.org/wiki/YAML) | 2001 | Yes ✅ | `:` colon ✅ | `\n` newline plus indentation ❌ | No ✅ |
| [JavaScript Object Notation (JSON)](https://en.wikipedia.org/wiki/JSON) | 2001 | Yes ✅ | `:` colon ✅ | `,` comma ✅ | Yes ❌ |
| [Labeled Tab-Separated Values (LTSV)](https://en.wikipedia.org/wiki/Labeled_Tab-separated_Values) | 2012 | Yes ✅ | `:` colon ✅ | `\t` tab ✅ | No ✅ |
| [Tom's Obvious Markup Language (TOML)](https://en.wikipedia.org/wiki/TOML) | 2013 | Yes ✅ | `=` equals ✅ | `\n` newline ❌ | No ✅ |
| [logfmt](https://brandur.org/logfmt) | 2013 | Yes ✅ | `=` equals ✅ | ` ` space ✅ | No ✅ |

Emit keys consistently to implement structured `key=value` logging. Most
operational values are simple scalars. Serialize iterables and mappings compactly to remain simple:
`list=1,2,3 dict=1..2:buckle-my-shoe,3..4:knock-at-the-door`. This follows the LTSV guidance of avoiding quotes and escapes to keep tooling requirements minimal.
As an escape hatch, complex data can be stuffed into the value as Python literals or JSON.
Reducing unnecessary punctuation also reduces LLM token usage.

## Wide Events / Canonical Log Lines

Fewer lines are better, with one line per request (or task) as the ideal.
[Canonical log lines](https://brandur.org/canonical-log-lines) makes that operational case well:
coherent context, easier streaming, and cleaner copy-paste to record incident details.
Multiple lines per request (or task) make key consistency harder to maintain.
[LoggingSucks](https://loggingsucks.com/) reaches the same practical conclusion from another
angle: wide single-line records make debugging and operations efficient, although Boris Tane's
unexplained choice of JSON over `key=value` adds punctuation and tool requirements
where clarity should win.

## Keys/Labels

An aspiration here is to combine Gunicorn and Django output into one consistent wide
`key=value` log line.
In the meantime, here is an [example of configuring gunicorn](https://github.com/biobuddies/allowedflare/blob/5b51b883a50f8ed2e200cc0776ad860c787f0291/gunicorn.conf.py#L5)
with abbreviated keys:

```py
access_log_format = '%(r)s st=%(s)s lb=%(h)s ip=%({x-forwarded-for}i)s rt=%(L)ss us=%(u)s rf=%(f)s'
```

Of course, abbreviating has downsides, so use whole words when they are a better choice or when
you are unsure.

| Abbr | LTSV Recommend | Description | Apache | nginx | gunicorn |
| ---- | -------------- | ----------- | ------ | ----- | -------- |
|      | `time` | Time the request was received | `%t` | `$time_local` | `%(t)s` |
| `lb` or `ip`* | `host` | Nearest client IP | `%h` | `$remote_addr` | `%(h)s` |
| `ff` or `ip`* | `forwardedfor` | Forwarded client IP | `%{X-Forwarded-For}i` | `$http_x_forwarded_for` | `%({x-forwarded-for}i)s` |
| `us` | `user` | Remote user | `%u` | `$remote_user` | `%(u)s` |
| `em` | | User email | | | |
|      | `req` | First line of request (method, uri, rows) | `%r` | `$request` | `%(r)s` |
|      | `method` | Request method | `%m` | `$request_method` | `%(m)s` |
|      | `uri` | Request URI | `%U%q` | `$request_uri` | `%(U)s%(q)s` |
|      | `protocol` | Requested Protocol (usually "HTTP/1.0" or "HTTP/1.1") | `%H` | `$server_protocol` | `%(H)s` |
| `st` | `status` | Status code | `%>s` | `$status` | `%(s)s` |
|      | `size` | Size of response in bytes, excluding HTTP headers; suffix with `b` for explicit units | `%Bb` (or `%bb` for compatibility with combined format) | `${body_bytes_sent}b` | `%(B)sb` |
|      | `reqsize` | Bytes received, including request and headers; suffix with `b` for explicit units | `%Ib` (`mod_log_io` required) | `${request_length}b` | `%({content-length}i)sb` |
| `rf` | `referer` | Referer header | `%{Referer}i` | `$http_referer` | `%(f)s` |
| `ua` | `ua` | User-Agent header | `%{User-agent}i` | `$http_user_agent` | `%(a)s` |
| `hs` | `vhost` | Host header | `%{Host}i` | `$host` | `%({host}i)s` |
|      | `reqtime_microsec` | The time taken to serve the request, in microseconds; suffix with `us` for explicit units | `%Dus` | | `%(D)sus` |
| `rt` | `reqtime` | The time taken to serve the request, in seconds; suffix with `s` for explicit units | `%Ts` | `${request_time}s` | `%(L)ss` |
|      | `cache` | X-Cache header | `%{X-Cache}o` | `$upstream_http_x_cache` | `%({x-cache}o)s` |
|      | `runtime` | Execution time for processing some request, e.g. X-Runtime header for application server or processing time of SQL for DB server. | `%{X-Runtime}o` | `$upstream_http_x_runtime` | `%({x-runtime}o)s` |
|      | `apptime` | Response time from the upstream server | | `$upstream_response_time` | |

\* Replace `lb` or `ff` with `ip` based on presence or absence of load balancer.
