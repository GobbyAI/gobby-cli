# gobby-cli Release Guide

This guide covers the multi-crate Rust release flow for maintainers.

## Current Release Set

| Crate | Binary | Version | Tag | Publishes? |
|---|---|---:|---|---|
| `gobby-core` | n/a | `0.5.0` | `gobby-core-v0.5.0` | crates.io only |
| `gobby-code` | `gcode` | `1.2.0` | `gcode-v1.2.0` | crates.io + GitHub binaries |
| `gobby-hooks` | `ghook` | `0.6.0` | `ghook-v0.6.0` | crates.io + GitHub binaries |
| `gobby-squeeze` | `gsqz` | `0.4.7` | `gsqz-v0.4.7` | crates.io + GitHub binaries |
| `gobby-local` | `gloc` | `0.1.5` | `gloc-v0.1.5` | crates.io + GitHub binaries |
| `gobby-wiki` | `gwiki` | `0.5.0` | `gwiki-v0.5.0` | crates.io + GitHub binaries |

## Version Rules

- Bump `gobby-code` to `1.2.0` (post-1.0 minor; verify there are no breaking
  CLI or envelope changes).
- Bump `gobby-core` to `0.5.0` (a breaking pre-1.0 minor bump: removed public
  APIs, `ureq` and the embeddings client re-gated under the `ai` feature).
- Bump `gobby-wiki` to `0.5.0` and `gobby-hooks` to `0.6.0` (pre-1.0 minors
  with new features).
- Bump patch versions for `gobby-squeeze` and `gobby-local`.
- `gobby-core 0.4.0 → 0.5.0` is breaking under Cargo's pre-1.0 semver, so every
  consumer crate's `gobby-core` path dependency must move its explicit `version`
  to `0.5.0` in the same release (gcode, gwiki — both dep and dev-dep — gsqz,
  gloc, and ghook). crates.io also rejects a path dependency with no version, so
  the `version` field must never be dropped.

## Tag Order

Publish the upstream library before the binaries that depend on it. Every binary
crate resolves `gobby-core 0.5.0` from crates.io at publish time, so
`gobby-core` must be indexed first. `gwiki` additionally re-verifies that the
published `gobby-core` exposes the `ai` feature.

```bash
git tag gobby-core-v0.5.0
git push origin gobby-core-v0.5.0

# Wait for crates.io to index gobby-core 0.5.0.

git tag gcode-v1.2.0
git tag ghook-v0.6.0
git tag gsqz-v0.4.7
git tag gloc-v0.1.5
git tag gwiki-v0.5.0

# Push the tags ONE AT A TIME. GitHub Actions does not create push events for
# any tag when more than three tags arrive in a single push, so a batched
# `git push origin <tag> <tag> <tag> <tag> ...` silently triggers NO release
# workflows. Push each tag in its own invocation:
for tag in gcode-v1.2.0 ghook-v0.6.0 gsqz-v0.4.7 gloc-v0.1.5 gwiki-v0.5.0; do
  git push origin "refs/tags/$tag"
done
```

If a batch push already created the tags on the remote without triggering
workflows, delete them first (`git push origin --delete <tag> ...`) and re-push
individually as above — re-pushing an existing remote tag ref is a no-op and
fires no event.

Since #609 `gsqz` depends on `gobby-core` (no default features), so it follows
the same tag ordering as the other binaries. The release workflows verify binary
crate tag/version alignment where the installer expects GitHub assets.
`gobby-core` has no binary artifact matrix.

The `gwiki` crates.io publish uses Trusted Publishing in the GitHub environment
`crates-io`. The workflow obtains an OIDC token during the publish job, so no
crates.io API token secret is needed for that release.

## Local Install Check

Build release binaries locally before tagging and copy the released binaries
into the Gobby bin directory:

```bash
cargo build --release -p gobby-code -p gobby-hooks -p gobby-squeeze -p gobby-local -p gobby-wiki
mkdir -p ~/.gobby/bin
cp target/release/gcode target/release/ghook target/release/gsqz target/release/gloc target/release/gwiki ~/.gobby/bin/
~/.gobby/bin/gcode --version
~/.gobby/bin/ghook --version
~/.gobby/bin/gsqz --version
~/.gobby/bin/gloc --version
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
cargo clippy -p gobby-squeeze -- -D warnings
cargo clippy -p gobby-squeeze --no-default-features -- -D warnings
cargo clippy -p gobby-local -- -D warnings
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
cargo nextest run -p gobby-squeeze
cargo test --doc -p gobby-squeeze
cargo nextest run -p gobby-local
cargo test --doc -p gobby-local
cargo nextest run -p gobby-wiki
cargo test --doc -p gobby-wiki
cargo build --workspace --no-default-features
cargo build --release -p gobby-code -p gobby-hooks -p gobby-squeeze -p gobby-local -p gobby-wiki
```

The repository CI still owns cross-target release packaging. Local validation
only proves manifests, lockfile resolution, and native release binaries.

_Last verified: 2026-06-11_
