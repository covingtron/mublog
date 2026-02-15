set allow-duplicate-recipes

import '.biobuddies/justfile'

# Build mkdocs site
build:
    .venv/bin/mkdocs build

# Preview mkdocs site
preview:
    .venv/bin/mkdocs serve

# Helichopyter Synth (uses local helichopyter instead of helicopyter)
hs cona='all':
    .venv/bin/python -m helichopyter {{ if cona == 'all' { 'all' } else { 'deploys/' + cona + '/terraform.py' } }}

# Helicopyter synth and Terraform Apply
hta cona envi *args:
    #!/usr/bin/env bash
    if [[ "{{ envi }}" == "default" ]]; then
        echo 'The default workspace behaves inconsistently.'
        echo 'If you only have one environment, please name it `prod`.'
        exit 1
    fi
    {{ JUST }} hs {{ cona }} \
        && TF_VAR_GIHA=`{{ JUST }} giha` TF_VAR_TABR=`{{ JUST }} tabr` TF_WORKSPACE={{ envi }} \
            ${INSH_TF:-terraform} -chdir=deploys/{{ cona }}/terraform apply {{ args }}

# Helicopyter synth and Terraform Plan
htp cona envi *args:
    #!/usr/bin/env bash
    if [[ "{{ envi }}" == "default" ]]; then
        echo 'The default workspace behaves inconsistently.'
        echo 'If you only have one environment, please name it `prod`.'
        exit 1
    fi
    {{ JUST }} hs {{ cona }} \
        && TF_WORKSPACE={{ envi }} ${INSH_TF:-terraform} -chdir=deploys/{{ cona }}/terraform plan \
        {{ args }}

# Deploy mublog: synth, init -upgrade, and apply
deploy:
    #!/usr/bin/env bash
    : "${TF_WORKSPACE:=`{{ JUST }} tabr`}"
    : "${TF_VAR_GIHA:=`{{ JUST }} giha`}"
    : "${TF_VAR_TABR:=${TF_WORKSPACE}}"
    : "${TF_WORKSPACE:?TF_WORKSPACE must be set and non-empty}"
    : "${TF_VAR_GIHA:?TF_VAR_GIHA must be set and non-empty}"
    : "${TF_VAR_TABR:?TF_VAR_TABR must be set and non-empty}"
    if [[ "${TF_WORKSPACE}" == "default" ]]; then
        echo 'The default workspace behaves inconsistently.'
        echo 'If you only have one environment, please name it `prod`.'
        exit 1
    fi
    {{ JUST }} hs mublog \
        && TF_WORKSPACE="${TF_WORKSPACE}" ${INSH_TF:-terraform} -chdir=deploys/mublog/terraform init -upgrade \
        && TF_VAR_GIHA="${TF_VAR_GIHA}" TF_VAR_TABR="${TF_VAR_TABR}" TF_WORKSPACE="${TF_WORKSPACE}" \
            ${INSH_TF:-terraform} -chdir=deploys/mublog/terraform apply -auto-approve
