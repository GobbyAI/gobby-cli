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

`gobby-wiki` / `gwiki` remains unreleased. Keep its package version at `0.1.0`
until the wiki CLI is ready for a public tag.

## Version Rules

- Keep `gobby-code` at `0.9.9` for this release.
- Bump `gobby-core` to `0.3.0`.
- Bump patch versions for `gobby-hooks`, `gobby-squeeze`, and `gobby-local`.
- Update all path dependencies on `gobby-core` to `0.3.0`, including the
  unreleased `gobby-wiki` crate, so the workspace resolves against the local
  core crate.
- Do not tag or publish `gobby-wiki`.

## Tag Order

Publish upstream library dependencies before binaries that depend on them:

```bash
git tag gobby-core-v0.3.0
git push origin gobby-core-v0.3.0

# Wait for crates.io to index gobby-core 0.3.0.

git tag gcode-v0.9.9
git tag ghook-v0.4.5
git tag gsqz-v0.4.5
git tag gloc-v0.1.3
git push origin gcode-v0.9.9 ghook-v0.4.5 gsqz-v0.4.5 gloc-v0.1.3
```

The release workflows verify binary crate tag/version alignment where the
installer expects GitHub assets. `gobby-core` has no binary artifact matrix.

## Local Install Check

Build release binaries locally before tagging and copy only the released
binaries into the Gobby bin directory:

```bash
cargo build --release -p gobby-code -p gobby-hooks -p gobby-squeeze -p gobby-local
mkdir -p ~/.gobby/bin
cp target/release/gcode target/release/ghook target/release/gsqz target/release/gloc ~/.gobby/bin/
~/.gobby/bin/gcode --version
~/.gobby/bin/ghook --version
~/.gobby/bin/gsqz --version
~/.gobby/bin/gloc --version
```

Do not copy `gwiki` for this release.

## Validation

Before tagging, run the focused release checks:

```bash
cargo clippy -p gobby-core --all-targets -- -D warnings
cargo clippy -p gobby-code -- -D warnings
cargo clippy -p gobby-code --no-default-features -- -D warnings
cargo clippy -p gobby-hooks --all-targets -- -D warnings
cargo clippy -p gobby-squeeze -- -D warnings
cargo clippy -p gobby-squeeze --no-default-features -- -D warnings
cargo clippy -p gobby-local -- -D warnings
cargo test -p gobby-core
cargo test -p gobby-code
cargo test -p gobby-code --no-default-features
cargo test -p gobby-hooks
cargo test -p gobby-squeeze
cargo test -p gobby-squeeze --no-default-features
cargo test -p gobby-local
cargo build --release -p gobby-code -p gobby-hooks -p gobby-squeeze -p gobby-local
```

The repository CI still owns cross-target release packaging. Local validation
only proves manifests, lockfile resolution, and native release binaries.

_Last verified: 2026-05-31_
