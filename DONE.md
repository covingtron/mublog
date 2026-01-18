# mublog

## Completed Setup Notes

### 1. Bootstrap with Helicopyter Cookiecutter

Create `.cookiecutter.yaml`:
```yaml
default_context:
    languages: Node,Python
```

From the repository root run:
```bash
cd /path/to/prj/mublog
asdf plugin add nodejs
asdf install nodejs latest
asdf set nodejs latest
asdf plugin add uv
asdf install uv latest
asdf set uv latest
uvx cookiecutter https://github.com/biobuddies/helicopyter/archive/refs/heads/main.zip --no-input --overwrite-if-exists
```

```json
{
    "name": "mublog",
    "version": "0",
    "private": true,
    "devDependencies": {
        "basedpyright": "*",
        "prettier": "*",
        "prettier-plugin-toml": "*",
        "prettier-plugin-jinja-template": "*",
        "prettier-plugin-organize-attributes": "*",
        "wrangler": "*"
    }
}
```

### 2. Configure Pre-commit and Tool Dependencies

A) Populate `.pre-commit-config.yaml` with the best hooks from helicopyter (using basedpyright, not mypy for speed):

```yaml
repos:
    - repo: https://github.com/biobuddies/helicopyter
      rev: v2026.00.01
      hooks:
          - id: actionlint
          - id: basedpyright
          - id: cookiecutter
          - id: end-of-file-fixer
          - id: hadolint
          - id: mailmap
          - id: prettier-write
          - id: ruff-check-fix
          - id: ruff-format
          - id: shellcheck
          - id: trailing-whitespace-fixer
          - id: typos
          - id: validate-pyproject
          - id: uv-pip-check
          - id: uv-pip-compile
          - id: yamllint
```

B) Write barebones floating version `pyproject.toml` and `package.json` to install all tools that pre-commit will use. Note: helicopyter hooks use `system` so runs with and without pre-commit use the same version.

`package.json`:
```json
{
    "devDependencies": {
        "basedpyright": "*",
        "prettier": "*",
        "prettier-plugin-toml": "*",
        "wrangler": "*"
    }
}
```

`pyproject.toml` dev dependencies:
```toml
[project.optional-dependencies]
dev = [
    'actionlint-py',
    'cookiecutter',
    'hadolint-py @ git+https://github.com/AleksaC/hadolint-py.git',
    'pre-commit',
    'pre-commit-hooks',
    'ruff',
    'rust-just',
    'shellcheck-py',
    'typos',
    'validate-pyproject',
    'yamllint',
    'mkdocs-material',
]

[tool.ruff]
extend = '.biobuddies/ruff.toml'

### 3. Prepare, install, and run pcam

```bash
bash .biobuddies/includes.bash upc
npm install
# npm install pins versions for npm clean-install, called as part of ups, to use
bash .biobuddies/includes.bash ups
bash .biobuddies/includes.bash pcam
ln -s -f .biobuddies/justfile justfile
```

### 4. Create mkdoc-material Project

Add `mkdocs-material` to your Python dev dependencies (see `pyproject.toml` above) and add `wrangler` to `package.json` devDependencies for any Cloudflare worker needs.

Bootstrap the mkdocs site and install the Material theme:

```bash
# create the initial site structure
mkdocs new .
```

You can also create a minimal `mkdocs.yaml` immediately (examples below) — during development serve with:
```bash
mkdocs serve
```

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
```
