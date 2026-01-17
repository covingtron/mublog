# mublog

Simple Publish on your Own Site, Syndicate Elsewhere (POSSE) favoring Python tools



### 3. Prepare, install, and run pcam

```bash
bash .biobuddies/includes.bash upc
npm install
# npm install pins versions for npm clean-install, called as part of ups, to use
bash .biobuddies/includes.bash ups
bash .biobuddies/includes.bash pcam
ln --force --symbolic .biobuddies/justfile justfile
```

### 4. Create mkdoc-material Project

Add `mkdocs-material` to your Python dev dependencies (see `pyproject.toml` above) and add `wrangler` to `package.json` devDependencies for any Cloudflare worker needs.

Bootstrap the mkdocs site and install the Material theme:

```bash
# create the initial site structure
mkdocs new .
```

You can also create a minimal `mkdocs.yml` immediately (examples below) — during development serve with:
```bash
mkdocs serve
```
### 5. Create site and basic configuration (cov.ing/tron)

Initialize the mkdocs site and use the following basic configuration tailored for a small blog hosted at `https://cov.ing/tron`.

Create the site:
```bash
mkdocs new .
```

Example `mkdocs.yml` (place in repo root):
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



