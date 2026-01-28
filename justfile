set allow-duplicate-recipes

import '.biobuddies/justfile'

# Build mkdocs site
build:
    .venv/bin/mkdocs build

# Preview mkdocs site
preview:
    .venv/bin/mkdocs serve

# Helichopyter Synth (uses local helichopyter instead of helicopyter)
[private]
hs cona='all':
    .venv/bin/python -m helichopyter deploys/{{ cona }}/terraform.py

# Helicopyter synth and Terraform Apply (helichopyter override)
hta cona envi *args:
    #!/usr/bin/env bash
    if [[ "{{ envi }}" == "default" ]]; then
        echo 'The default workspace behaves inconsistently.'
        echo 'If you only have one environment, please name it `prod`.'
        exit 1
    fi
    {{ JUST }} hs {{ cona }} \
        && TF_VAR_giha=`{{ JUST }} giha` TF_VAR_tabr=`{{ JUST }} tabr` TF_WORKSPACE={{ envi }} \
            ${INSH_TF:-terraform} -chdir=deploys/{{ cona }}/terraform apply {{ args }}

# Helicopyter synth and Terraform Plan (helichopyter override)
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
