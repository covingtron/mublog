"""Regenerate Measles configuration and retain deployment comment permission."""

from pathlib import Path
from subprocess import check_call
from sys import argv
from tomllib import loads

configuration = loads(Path('.config/mise.toml').read_text())
check_call(  # noqa: S603 -- Execute the repository's trusted task definition.
    ['bash', '-c', configuration['tasks']['cookiecutter']['run'], 'cookiecutter', *argv[1:]]
)

# Upstream the comment permission if the downstream plan-comment trial proves useful.
workflow = Path('.github/workflows/act.yaml')
source = workflow.read_text()
permission = '            pull-requests: write\n'
anchor = '            contents: write\n'
if permission not in source:
    if source.count(anchor) != 1:
        raise ValueError('Expected one deployment contents permission')
    workflow.write_text(source.replace(anchor, anchor + permission))
