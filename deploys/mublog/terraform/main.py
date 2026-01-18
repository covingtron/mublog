"""Helicopyter mublog deploy module."""

from os import environ
from pathlib import Path

from cdktf_cdktf_provider_cloudflare.dns_record import DnsRecord
from cdktf_cdktf_provider_cloudflare.workers_route import WorkersRoute
from cdktf_cdktf_provider_cloudflare.workers_script import WorkersScript
from helicopyter import HeliStack


def synth(stack: HeliStack) -> None:
    stack.provide('cloudflare')

    envi = '${terraform.workspace}'
    script_name = f'mublog-{envi}'

    stack.push(
        WorkersScript,
        'this',
        account_id=environ['CLOUDFLARE_ACCOUNT_ID'],
        compatibility_date='2025-01-17',
        content=(Path(__file__).parent / 'worker.js').read_text(),
        main_module='worker.js',
        script_name=script_name,
    ).add_override(
        'assets',
        {
            'config': {
                'not_found_handling': 'single-page-application',
                'run_worker_first': ['/api/*'],
            },
            'directory': '../../../site',
        },
    )

    stack.push(
        DnsRecord,
        'this',
        content='100::',  # RFC 6666 discard placeholder
        name=envi,
        proxied=True,
        ttl=1,
        type='AAAA',
        zone_id=environ['CLOUDFLARE_ZONE_ID'],
    )

    stack.push(
        WorkersRoute,
        'api',
        pattern=f'{envi}.cov.ing/api/*',
        script=script_name,
        zone_id=environ['CLOUDFLARE_ZONE_ID'],
    )

    stack.push(
        WorkersRoute,
        'blog',
        pattern=f'{envi}.cov.ing/blog/*',
        script=script_name,
        zone_id=environ['CLOUDFLARE_ZONE_ID'],
    )
