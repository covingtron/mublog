"""Repository layout checks tied to the local mise migration."""

from pathlib import Path
from subprocess import run

repo = Path(__file__).resolve().parent


def git_check_ignore(path: str):
    return run(
        ['git', 'check-ignore', '-v', path],
        capture_output=True,
        check=False,
        cwd=repo,
        text=True,
    )


def test_site_gitignore_ignores_build_output_and_tracks_static_files():
    gitignore_sed = (repo / '.gitignore.sed').read_text()

    assert '/site/*' in gitignore_sed
    assert '!/site/favicon.svg' in gitignore_sed
    assert '!/site/robots.txt' in gitignore_sed

    ignored = git_check_ignore('site/ton/index.html')

    assert ignored.returncode == 0
    assert '.gitignore' in ignored.stdout

    for path in ('site/favicon.svg', 'site/robots.txt'):
        tracked = git_check_ignore(path)
        assert tracked.returncode == 1


def test_repository_no_longer_depends_on_biobuddies():
    assert not (repo / '.biobuddies').exists()
    for path in (
        '.config/autoformat-excludes',
        '.config/mise.toml',
        '.config/ruff.toml',
        '.config/typos.toml',
        'pyproject.toml',
    ):
        assert '.biobuddies' not in (repo / path).read_text()
