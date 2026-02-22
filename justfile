set allow-duplicate-recipes

import '.biobuddies/justfile'

# Build mkdocs site
build:
    .venv/bin/mkdocs build

# Preview mkdocs site
preview:
    .venv/bin/mkdocs serve

# Pre-Commit Run (defaults to modified files) with local Python and Node tools on PATH
pcr *args:
    #!/usr/bin/env bash
    set -euxo pipefail
    checkout="$HOME/code/$({{ JUST }} cona)"
    [[ -d "$checkout" ]] || {
        echo "ERROR: expected checkout at $checkout"
        exit 1
    }
    export PATH="$checkout/.venv/bin:$checkout/node_modules/.bin:$PATH"
    pre-commit run {{ args }}

# run Pre-Commit on All files
pca *args:
    @# Seemingly contradicting the help text, experimentation shows hook positional arguments must
    @# come before flags
    {{ JUST }} pcr {{ args }} --all-files

# run Pre-Commit on All files including Manual stage hooks
pcam *args:
    {{ JUST }} pca {{ args }} --hook-stage manual

# run Pre-Commit on modified files including Manual stage hooks
pcm *args:
    {{ JUST }} pcr {{ args }} --hook-stage manual

# Install pre-commit hooks using the project toolchain path
pc-install:
    #!/usr/bin/env bash
    set -euxo pipefail
    checkout="$HOME/code/$({{ JUST }} cona)"
    [[ -d "$checkout" ]] || {
        echo "ERROR: expected checkout at $checkout"
        exit 1
    }
    export PATH="$checkout/.venv/bin:$checkout/node_modules/.bin:$PATH"
    pre-commit install --install-hooks
    hook=.git/hooks/pre-commit
    [[ -f "$hook" ]] || {
        echo "ERROR: expected generated hook at $hook"
        exit 1
    }
    anchor='# end templated'
    grep -Fq "$anchor" "$hook" || {
        echo "ERROR: expected anchor not found in $hook: $anchor"
        exit 1
    }
    marker='Added by just pc-install: ensure local toolchain for system hooks'
    if ! grep -Fq "$marker" "$hook"; then
        tmp=$(mktemp)
        awk -v anchor="$anchor" -v marker="$marker" -v checkout="$checkout" '
            { print }
            $0 == anchor && !done {
                print ""
                print "# " marker
                print "export PATH=\"" checkout "/.venv/bin:" checkout "/node_modules/.bin:$PATH\""
                done = 1
            }
        ' "$hook" > "$tmp"
        mv "$tmp" "$hook"
        chmod +x "$hook"
    fi

# Helichopyter Synth (uses local helichopyter instead of helicopyter)
hs cona='all':
    .venv/bin/python -m helichopyter {{ if cona == 'all' { 'all' } else { 'deploys/' + cona + '/terraform.py' } }}

# Helicopyter synth and Terraform Apply
hta cona envi *args:
    #!/usr/bin/env bash
    set -euxo pipefail
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
    set -euxo pipefail
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
    set -euxo pipefail
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
    rm -f site/ton/flan
    mkdir -p site/ton/flan
    printf 'CONA=mublog\nENVI=%s\nGIHA=%s\nTABR=%s\n' \
        "${TF_WORKSPACE}" "${TF_VAR_GIHA}" "${TF_VAR_TABR}" > site/ton/flan/index.html
    {{ JUST }} hs mublog \
        && env -u TF_WORKSPACE ${INSH_TF:-terraform} -chdir=deploys/mublog/terraform init -upgrade \
        && { ${INSH_TF:-terraform} -chdir=deploys/mublog/terraform workspace new "${TF_WORKSPACE}" || true; } \
        && TF_VAR_GIHA="${TF_VAR_GIHA}" TF_VAR_TABR="${TF_VAR_TABR}" TF_WORKSPACE="${TF_WORKSPACE}" \
            ${INSH_TF:-terraform} -chdir=deploys/mublog/terraform apply -auto-approve
