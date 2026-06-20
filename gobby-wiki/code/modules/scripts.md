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

The `scripts` module currently consists of `scripts/verify.sh`, a Bash verification entry point for the Rust workspace. It centralizes build, test, formatting, and lint checks behind named CLI checks, with `usage` documenting accepted arguments and default behavior (`scripts/verify.sh:4-9`).

The main flow is argument-driven: with no arguments, the script expands to the full check set, then iterates through each requested check and dispatches it through `run_check` (`scripts/verify.sh:34-48`). `run_check` delegates to Cargo, nextest, rustfmt, and clippy, and handles help or unknown check names with usage output and explicit exits (`scripts/verify.sh:11-32`).

| CLI check | Action | Citation |
| --- | --- | --- |
| `build` | `cargo build --workspace --no-default-features` | `scripts/verify.sh:13-15` |
| `unit_tests` | `cargo nextest run --workspace --no-default-features` | `scripts/verify.sh:16-18` |
| `doc_tests` | `cargo test --doc --workspace --no-default-features` | `scripts/verify.sh:19-21` |
| `format` | `cargo fmt --all --check` | `scripts/verify.sh:22-24` |
| `lint` | `cargo clippy --workspace --no-default-features -- -D warnings` | `scripts/verify.sh:25-27` |
| `-h`, `--help`, `help` | Print usage and exit successfully | `scripts/verify.sh:28-31` |

| Public symbol | Responsibility | Citation |
| --- | --- | --- |
| `usage` | Prints command syntax and default behavior | `scripts/verify.sh:4-9` |
| `run_check` | Dispatches named checks and handles errors | `scripts/verify.sh:11-32` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/scripts/verify.sh\|scripts/verify.sh]] | `scripts/verify.sh` exposes 2 indexed API symbols. |

