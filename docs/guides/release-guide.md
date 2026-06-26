# gobby-cli Release Guide

This guide covers the multi-crate Rust release flow for maintainers.

## Current Release Set

| Crate | Binary | Version | Tag | Publishes? |
|---|---|---:|---|---|
| `gobby-core` | n/a | `0.6.1` | `gobby-core-v0.6.1` | crates.io only |
| `gobby-code` | `gcode` | `1.3.3` | `gcode-v1.3.3` | crates.io + GitHub binaries |
| `gobby-hooks` | `ghook` | `0.6.2` | `ghook-v0.6.2` | crates.io + GitHub binaries |
| `gobby-wiki` | `gwiki` | `0.6.5` | `gwiki-v0.6.5` | crates.io + GitHub binaries |

## Version Rules

- Bump only crates whose shipped behavior, public API, or release artifacts
  changed.
- `gobby-core` is pre-1.0. A minor bump is breaking under Cargo semver, so every
  active consumer crate's `gobby-core` path dependency must move its explicit
  `version` in the same release (`gcode`, `gwiki` dependency and dev-dependency,
  and `ghook`). crates.io rejects path dependencies without a `version` field,
  so never drop it.
- Keep tag prefixes aligned with the package release contract: `gcode-v*`,
  `ghook-v*`, `gwiki-v*`, and `gobby-core-v*`.

## Tag Order

When `gobby-core` changes, publish the upstream library before binaries that
depend on it. Every binary crate resolves `gobby-core` from crates.io at publish
time, so the new core version must be indexed first. `gwiki` additionally
re-verifies that the published `gobby-core` exposes the `ai` feature.

```bash
git tag gobby-core-v0.6.1
git push origin gobby-core-v0.6.1

# Wait for crates.io to index gobby-core 0.6.1.

git tag gcode-v1.3.3
git tag ghook-v0.6.2
git tag gwiki-v0.6.5

# Push the tags ONE AT A TIME. GitHub Actions does not create push events for
# any tag when more than three tags arrive in a single push, so a batched
# `git push origin <tag> <tag> <tag> <tag> ...` silently triggers NO release
# workflows. Push each tag in its own invocation:
for tag in gcode-v1.3.3 ghook-v0.6.2 gwiki-v0.6.5; do
  git push origin "refs/tags/$tag"
done
```

If a batch push already created the tags on the remote without triggering
workflows, delete them first (`git push origin --delete <tag> ...`) and re-push
individually as above — re-pushing an existing remote tag ref is a no-op and
fires no event.

The release workflows verify binary crate tag/version alignment where the
installer expects GitHub assets. `gobby-core` has no binary artifact matrix.

The `gwiki` crates.io publish uses Trusted Publishing in the GitHub environment
`crates-io`. The workflow obtains an OIDC token during the publish job, so no
crates.io API token secret is needed for that release.

## Local Install Check

Build release binaries locally before tagging and copy the released binaries
into the Gobby bin directory:

```bash
cargo build --release -p gobby-code -p gobby-hooks -p gobby-wiki
mkdir -p ~/.gobby/bin
cp target/release/gcode target/release/ghook target/release/gwiki ~/.gobby/bin/
~/.gobby/bin/gcode --version
~/.gobby/bin/ghook --version
~/.gobby/bin/gwiki --version
```

Refresh each `~/.gobby/bin/.<name>-version` sidecar to the released version, and
run `ghook --version` so it rewrites `~/.gobby/bin/.ghook-runtime.json`.

## Validation

Before tagging, run the focused release checks:

```bash
cargo fmt --all --check
cargo clippy --workspace --all-targets -- -D warnings
cargo clippy -p gobby-core --all-targets -- -D warnings
cargo clippy -p gobby-core --all-targets --no-default-features -- -D warnings
cargo clippy -p gobby-code -- -D warnings
cargo clippy -p gobby-code --no-default-features -- -D warnings
cargo clippy -p gobby-hooks --all-targets -- -D warnings
cargo clippy -p gobby-hooks --all-targets --no-default-features -- -D warnings
cargo clippy -p gobby-wiki --all-targets -- -D warnings
cargo clippy -p gobby-wiki --all-targets --no-default-features -- -D warnings
cargo nextest run --workspace --no-default-features
cargo test --doc --workspace --no-default-features
cargo nextest run -p gobby-core
cargo test --doc -p gobby-core
cargo nextest run -p gobby-code
cargo test --doc -p gobby-code
cargo nextest run -p gobby-hooks
cargo test --doc -p gobby-hooks
cargo nextest run -p gobby-wiki
cargo test --doc -p gobby-wiki
cargo build --workspace --no-default-features
cargo build --release -p gobby-code -p gobby-hooks -p gobby-wiki
```

The repository CI still owns cross-target release packaging. Local validation
only proves manifests, lockfile resolution, and native release binaries.

_Last verified: 2026-06-26_
