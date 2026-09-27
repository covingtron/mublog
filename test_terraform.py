"""Exercise deployment synthesis through the same entry point used by mise."""

from os import environ
from pathlib import Path
from shutil import copy
from subprocess import check_call
from sys import executable


def test_terraform_synthesis(tmp_path: Path):
    directory = Path('deploys/mublog/terraform')
    target = tmp_path / directory
    target.mkdir(parents=True)
    for name in ('main.py', 'worker.js'):
        copy(directory / name, target / name)
    check_call(
        [executable, '-m', 'helicopyter', 'mublog', '--format_with=cat'],
        cwd=tmp_path,
        env={**environ, 'CLOUDFLARE_ACCOUNT_ID': 'test-account', 'CLOUDFLARE_ZONE_ID': 'test-zone'},
    )
    generated = (target / 'main.tf').read_text()
    assert '\n  backend "s3" {' in generated
    assert '\nprovider "cloudflare" {}' in generated
    assert 'name = terraform.workspace == "main" ? "@" : terraform.workspace' in generated
    assert 'subdomain = terraform.workspace == "main" ? "" : "${terraform.workspace}."' in generated
    assert 'count = terraform.workspace == "main" ? 1 : 0' in generated
    assert generated.count('script = cloudflare_workers_script.this.script_name') == 3
    assert 'pattern = "${local.subdomain}cov.ing/*"' in generated
    assert 'skip_credentials_validation = true' in generated
