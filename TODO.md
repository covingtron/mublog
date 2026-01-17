# mublog

Simple Publish on your Own Site, Syndicate Elsewhere (POSSE) favoring Python tools

## Completed Setup Notes

### 1. Bootstrap with Helicopyter Cookiecutter

Create `.cookiecutter.yaml`:
```yaml
default_context:
    languages: Node,Python
```

Set up tool versions and run cookiecutter template:
```bash
asdf plugin add nodejs
asdf install nodejs latest
asdf set nodejs latest
asdf plugin add uv
asdf install uv latest
asdf set uv latest
uvx cookiecutter https://github.com/biobuddies/helicopyter/archive/refs/heads/main.zip --no-input --overwrite-if-exists
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
          - id: django-upgrade
          - id: djlint-django
          - id: djlint-jinja
          - id: end-of-file-fixer
          - id: hadolint

          - id: mailmap
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
    'django-upgrade',
    'djlint',
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
```

### 3. Create mkdoc-material Project

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

### 4. Autoformat with pcam

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



