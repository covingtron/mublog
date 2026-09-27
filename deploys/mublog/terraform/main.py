"""Terraform configuration for mublog."""

from os import environ
from pathlib import Path

from helicopyter import Block, only_main, provider, resource, terraform, tlocals

terraform.required_providers(cloudflare={'source': 'cloudflare/cloudflare', 'version': '5.14.0'})
terraform.backend('s3')(
    bucket='terraform',
    key='mublog.tfstate',
    region='auto',
    workspace_key_prefix='mublog',
    skip_credentials_validation=True,
    skip_metadata_api_check=True,
    skip_region_validation=True,
    skip_requesting_account_id=True,
    skip_s3_checksum=True,
    use_path_style=True,
)

provider.cloudflare()

tlocals(subdomain=Block('terraform.workspace == "main" ? "" : "${terraform.workspace}."'))

resource.cloudflare_workers_script.this(
    account_id=environ['CLOUDFLARE_ACCOUNT_ID'],
    compatibility_date='2025-01-17',
    content=(Path(__file__).parent / 'worker.js').read_text(),
    main_module='worker.js',
    script_name='mublog-${terraform.workspace}',
    assets={
        'config': {'not_found_handling': 'single-page-application', 'run_worker_first': ['/api/*']},
        'directory': '../../../site',
    },
)

resource.cloudflare_dns_record.this(
    content='100::',
    name=Block('terraform.workspace == "main" ? "@" : terraform.workspace'),
    proxied=True,
    ttl=1,
    type='AAAA',
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
)

resource.cloudflare_workers_route.api(
    depends_on=[resource.cloudflare_workers_script.this],
    pattern='${local.subdomain}cov.ing/api/*',
    script=resource.cloudflare_workers_script.this.script_name,
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
)

resource.cloudflare_workers_route.ton(
    depends_on=[resource.cloudflare_workers_script.this],
    pattern='${local.subdomain}cov.ing/ton/*',
    script=resource.cloudflare_workers_script.this.script_name,
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
)

resource.cloudflare_workers_route.root(
    depends_on=[resource.cloudflare_workers_script.this],
    pattern='${local.subdomain}cov.ing/*',
    script=resource.cloudflare_workers_script.this.script_name,
    zone_id=environ['CLOUDFLARE_ZONE_ID'],
)

with only_main():
    resource.cloudflare_ruleset.append_slash(
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
