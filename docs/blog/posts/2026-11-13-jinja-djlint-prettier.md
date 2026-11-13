---
date: 2026-11-13
slug: j2-html-djlint-prettier
---

# Format Jinja2 HTML templates with djLint and Prettier

I like to lint and autoformat. For HTML with Jinja2 templating,
[djlint](https://djlint.com/) and
[prettier](https://blog.vjeux.com/2025/javascript/birth-of-prettier.html) are great,
but they disagree on some details like long lines. Here's how I've been combining them:

```bash
djlint --reformat --profile=jinja index.j2.html || test $? -eq 1
prettier --write index.j2.html
djlint --lint --profile=jinja index.j2.html
```

[:simple-mastodon: Mastodon](https://mastodon.social/@covracer/117609449755896792)
