# mublog

Simple Publish on your Own Site, Syndicate Elsewhere (POSSE) favoring Python tools






### 5. Create site and basic configuration (cov.ing/tron)

Initialize the mkdocs site and use the following basic configuration tailored for a small blog hosted at `https://cov.ing/tron`.



Example `mkdocs.yaml` (place in repo root):
```yaml
site_name: mublog
site_url: https://cov.ing/tron
repo_url: https://github.com/covingtron/mublog
theme:
  name: material
  palette:
    primary: 'indigo'
    accent: 'teal'
  font:
    text: 'Roboto'
    code: 'JetBrains Mono'
nav:
  - Home: index.md
  - Blog:
    - 'All posts': blog/index.md
  - About: about.md
plugins:
  - search
markdown_extensions:
  - toc:
      permalink: true
```

Docs structure (create these files under `docs/`):
- `docs/index.md` — welcome / landing page.
- `docs/blog/index.md` — blog index listing posts (link to individual markdown posts in `docs/blog/`)
- `docs/about.md` — about page

Serving locally:
```bash
mkdocs serve
```
