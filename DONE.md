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