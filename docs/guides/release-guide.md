# gobby-cli Release Guide

This guide covers the multi-crate Rust release flow for maintainers.

## Current Release Set

| Crate | Binary | Version | Tag | Publishes? |
|---|---|---:|---|---|
| `gobby-core` | n/a | `0.3.0` | `gobby-core-v0.3.0` | crates.io only |
| `gobby-code` | `gcode` | `0.9.9` | `gcode-v0.9.9` | crates.io + GitHub binaries |
| `gobby-hooks` | `ghook` | `0.4.5` | `ghook-v0.4.5` | crates.io + GitHub binaries |
| `gobby-squeeze` | `gsqz` | `0.4.5` | `gsqz-v0.4.5` | crates.io + GitHub binaries |
| `gobby-local` | `gloc` | `0.1.3` | `gloc-v0.1.3` | crates.io + GitHub binaries |
| `gobby-wiki` | `gwiki` | `0.2.0` | `gwiki-v0.2.0` | crates.io + GitHub binaries |

`gobby-wiki` ships its first public release as `0.2.0` in this set.

## Version Rules

- Keep `gobby-code` at `0.9.9` for this release.
- Bump `gobby-core` to `0.3.0`.
- Bump patch versions for `gobby-hooks`, `gobby-squeeze`, and `gobby-local`.
- Release `gobby-wiki` for the first time as `0.2.0`.
- Every binary crate's `gobby-core` path dependency must also carry an explicit
  `version = "0.3.0"`. crates.io rejects a path dependency with no version, so a
  bare path dep blocks `cargo publish`. `gobby-local` previously omitted the
  version and could not publish; it now pins `0.3.0` like the others.

## Tag Order

Publish the upstream library before the binaries that depend on it. Every binary
crate resolves `gobby-core 0.3.0` from crates.io at publish time, so
`gobby-core` must be indexed first. `gwiki` additionally re-verifies that the
published `gobby-core` exposes the `ai` feature.

```bash
git tag gobby-core-v0.3.0
git push origin gobby-core-v0.3.0

# Wait for crates.io to index gobby-core 0.3.0.

git tag gcode-v0.9.9
git tag ghook-v0.4.5
git tag gsqz-v0.4.5
git tag gloc-v0.1.3
git tag gwiki-v0.2.0

# Push the tags ONE AT A TIME. GitHub Actions does not create push events for
# any tag when more than three tags arrive in a single push, so a batched
# `git push origin <tag> <tag> <tag> <tag> ...` silently triggers NO release
# workflows. Push each tag in its own invocation:
for tag in gcode-v0.9.9 ghook-v0.4.5 gsqz-v0.4.5 gloc-v0.1.3 gwiki-v0.2.0; do
  git push origin "refs/tags/$tag"
done
```

If a batch push already created the tags on the remote without triggering
workflows, delete them first (`git push origin --delete <tag> ...`) and re-push
individually as above — re-pushing an existing remote tag ref is a no-op and
fires no event.

`gsqz` has no `gobby-core` dependency and may be tagged at any time. The release
workflows verify binary crate tag/version alignment where the installer expects
GitHub assets. `gobby-core` has no binary artifact matrix.

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

_Last verified: 2026-06-03_
