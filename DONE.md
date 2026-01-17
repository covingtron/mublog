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
