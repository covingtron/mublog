---
date: 2026-04-28
slug: gh-https-auth
---

# Authenticate git with gh over HTTPS

`gh auth login` does more than GitHub API access; it also configures git's credential helper.
From then on, HTTPS remotes authenticate as whichever account is active in `gh`.

```bash
# New repo: clone over HTTPS, not SSH
gh repo clone biobuddies/helicopyter
# remote is https://github.com/biobuddies/helicopyter.git

# Existing repo: switch to HTTPS
git remote set-url origin https://github.com/biobuddies/helicopyter.git
```

Behind the scenes, `gh` registers itself as the credential helper:

```
# git config --list | grep credential.https.github
credential.https://github.com.helper=
credential.https://github.com.helper=!/path/to/gh auth git-credential
```

When git needs credentials, it calls `gh auth git-credential`, which reads the stored token.

Token storage depends on the platform:

- **macOS**: `osxkeychain`, the Keychain Access app
- **Linux**: `~/.config/gh/hosts.yml` (encrypted with a key from `pass`, `gpg`, or plain file)

`gh auth status` confirms which account is active:

```
# gh auth status
github.com
  ✓ Logged in to github.com account covingtron (keyring)
  - Active account: true
  - Git operations protocol: https
```

No SSH keys needed, no `~/.ssh/config`. Every push authenticates as the
active `gh` account.

In GitHub Actions, `GITHUB_TOKEN` is available automatically via OIDC. When `$GITHUB_TOKEN`
is set, `gh auth git-credential` uses it instead of a stored token; no `gh auth login`
needed in CI. This is the same token that actions/checkout uses for HTTPS clones.

Pip and uv support `git+https://` dependencies. There are two ways to authenticate them:

```
# Token in URL; pip/uv parse it directly, no git credential helper needed
hadolint-py @ git+https://${GITHUB_TOKEN}@github.com/AleksaC/hadolint-py.git

# Clean URL; git resolves creds via gh auth git-credential
hadolint-py @ git+https://github.com/AleksaC/hadolint-py.git
```

Token-in-URL works everywhere but risks leaking into lock files; older versions of uv and
pip-compile could bake the token into `requirements.txt`. With `gh auth git-credential`,
the URL stays concise and the credential helper handles auth transparently; git, pip,
and uv all use it. This requires `gh` installed in CI.
