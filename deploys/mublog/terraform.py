"""Terraform configuration for mublog."""

from os import environ
from pathlib import Path

from helichopyter import backend, provider, required_providers, resource

required_providers(cloudflare={'source': 'cloudflare/cloudflare', 'version': '5.14.0'})
backend(
    's3',
    bucket='terraform',
    key='mublog.tfstate',
    region='auto',
    workspace_key_prefix='mublog',
    skip_credentials_validation='true',
    skip_metadata_api_check='true',
    skip_region_validation='true',
    skip_requesting_account_id='true',
    skip_s3_checksum='true',
    use_path_style='true',
)

provider('cloudflare')

resource('cloudflare_workers_script', 'this')(
    account_id=environ['CLOUDFLARE_ACCOUNT_ID'],
    compatibility_date='2025-01-17',
    content=(Path(__file__).parent / 'terraform' / 'worker.js').read_text(),
    main_module='worker.js',
    script_name='mublog-${terraform.workspace}',
    assets={
        'config': {'not_found_handling': 'single-page-application', 'run_worker_first': ['/api/*']},
        'directory': '../../../site',
    },
)

resource('cloudflare_dns_record', 'this')(
    count='${terraform.workspace == "main" ? 1 : 0}',
    content='100::',
    name='${terraform.workspace == "main" ? "@" : terraform.workspace}',
    proxied=True,
    ttl=1,
    type='AAAA',
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
)

resource('cloudflare_workers_route', 'api')(
    pattern='${terraform.workspace == "main" ? "" : "${terraform.workspace}."}cov.ing/api/*',
    script='mublog-${terraform.workspace}',
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
)

resource('cloudflare_workers_route', 'ton')(
    pattern='${terraform.workspace == "main" ? "" : "${terraform.workspace}."}cov.ing/ton/*',
    script='mublog-${terraform.workspace}',
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
)

resource('cloudflare_workers_route', 'root')(
    pattern='${terraform.workspace == "main" ? "" : "${terraform.workspace}."}cov.ing/',
    script='mublog-${terraform.workspace}',
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
)

resource('cloudflare_ruleset', 'append_slash')(
    count='${terraform.workspace == "main" ? 1 : 0}',
    kind='zone',
    name='append-slash',
    phase='http_request_dynamic_redirect',
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
    rules=[
        {
            'action': 'redirect',
            'action_parameters': {
                'from_value': {
                    'preserve_query_string': True,
                    'status_code': 301,
                    'target_url': {'expression': 'concat(http.request.uri.path, "/")'},
                }
            },
            'description': 'Append slash',
            'expression': (
                'not ends_with(http.request.uri.path, "/")'
                'and not http.request.uri.path contains "."'
                'and not starts_with(http.request.uri.path, "/assets/")'
            ),
        },
        {
            'action': 'redirect',
            'action_parameters': {
                'from_value': {
                    'preserve_query_string': True,
                    'status_code': 301,
                    'target_url': {'value': '/ton/'},
                }
            },
            'description': 'Redirect root to ton',
            'expression': 'http.request.uri.path eq "/"',
        },
    ],
)
