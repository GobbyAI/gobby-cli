---
title: scripts
type: code_module
provenance:
- file: scripts/verify.sh
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# scripts

Parent: [[code/repo|Repository Overview]]

## Overview

## Module: scripts

The `scripts` module is a single-file Bash utility that provides a unified developer verification harness for the workspace. Its sole member, `scripts/verify.sh`, enforces a strict execution environment (`set -euo pipefail`) and orchestrates all standard quality-gate checks — compilation, unit testing, documentation testing, formatting, and linting — through a consistent command-line interface.

The script exposes two internal functions. `usage` (scripts/verify.sh:4-9) prints a concise help message to stderr describing accepted arguments. `run_check` (scripts/verify.sh:11-38) dispatches on a single string argument, invoking the appropriate Cargo subcommand for each named check. When invoked with no arguments, the script defaults to running the full ordered sequence of all five checks (scripts/verify.sh:40-42), making it suitable as a pre-commit or CI entrypoint with zero configuration.

### Supported Checks

| Check name | Underlying command | Description |
|---|---|---|
| `build` | `cargo build --workspace --no-default-features` | Compile all workspace crates |
| `unit_tests` | `cargo nextest run --workspace --no-default-features` | Run unit tests via nextest |
| `doc_tests` | `cargo test --doc --workspace --no-default-features` | Run documentation tests |
| `format` | `cargo fmt --all --check` | Verify code formatting |
| `lint` | `cargo clippy --workspace --no-default-features -- -D warnings` | Lint and deny all warnings |

### CLI Flags

| Flag | Behaviour |
|---|---|
| _(no arguments)_ | Runs all five checks in order (scripts/verify.sh:40-42) |
| `build \| unit_tests \| doc_tests \| format \| lint` | Runs the specified check(s) only |
| `-h`, `--help`, `help` | Prints usage and exits 0 (scripts/verify.sh:29-32) |
| _unknown value_ | Prints usage, emits error, and exits 2 (scripts/verify.sh:33-37) |

All workspace commands are invoked with `--no-default-features`, ensuring checks are reproducible across environments regardless of locally activated feature flags. The script has no cross-file dependencies and does not import or call into any other module; it is intended to be called directly by developers or CI runners as an entrypoint into the broader Rust workspace build system.

## Files

| File | Summary |
| --- | --- |
| [[code/files/scripts/verify.sh\|scripts/verify.sh]] | `scripts/verify.sh` exposes 2 indexed API symbols. |

