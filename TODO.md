# mublog

Simple Publish on your Own Site, Syndicate Elsewhere (POSSE) favoring Python tools



### 3. Autoformat with pcam

Run `pcam` to autoformat the codebase and run the configured pre-commit hooks:

```bash
source .biobuddies/includes.bash && source .venv/bin/activate && pcam
```

After running `pcam` (which runs the pre-commit hooks), install Python and Node dev dependencies with the included helper wrapper:

```bash
bash .biobuddies/includes.bash ups
```

This `ups` wrapper runs `uv pip install` and an npm clean-install to ensure your environment matches `pyproject.toml` and `package-lock.json`/`package.json`.



Run `npm install` before the first `bash .biobuddies/includes.bash ups` run.

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



