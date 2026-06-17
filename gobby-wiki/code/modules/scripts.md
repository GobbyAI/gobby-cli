---
title: scripts
type: code_module
provenance:
- file: scripts/verify.sh
  ranges:
  - 4-10
  - 12-39
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [scripts/verify.sh:4-10](scripts/verify.sh#L4-L10), [scripts/verify.sh:12-39](scripts/verify.sh#L12-L39)

</details>

# scripts

Parent: [[code/repo|Repository Overview]]

## Overview

The scripts module serves as a repository utility layer containing verification helper scripts to streamline continuous integration and local development. Its primary component, scripts/verify.sh, acts as a central wrapper for executing workspace-wide quality checks . The script's main flow sequentially processes user-provided check names, falling back to a default suite of all five checks if invoked with no arguments . It dispatches each check to its corresponding Cargo command, handling workspace compilation, unit tests via Nextest, documentation tests, formatting validation, and Clippy lints [scripts/verify.sh:12-39].

The module collaborates directly with Cargo and system-level build tools, standardizing how developer verification is run across different environments. Error handling is built into the dispatch flow, where encountering an unsupported check or a help request prints the usage text and exits the process immediately [scripts/verify.sh:4-10, scripts/verify.sh:29-37].

### CLI Commands and Arguments

| Argument / Flag | Description | Underlying Action |
| --- | --- | --- |
| build | Compiles the Cargo workspace without default features | cargo build --workspace --no-default-features [scripts/verify.sh:14-16] |
| unit_tests | Runs unit tests across the workspace via Nextest without default features | cargo nextest run --workspace --no-default-features [scripts/verify.sh:17-19] |
| doc_tests | Executes workspace documentation tests without default features | cargo test --doc --workspace --no-default-features [scripts/verify.sh:20-22] |
| format | Verifies that all workspace code complies with formatting rules | cargo fmt --all --check [scripts/verify.sh:23-25] |
| lint | Performs static analysis via Clippy, denying compiler warnings | cargo clippy --workspace --no-default-features -- -D warnings [scripts/verify.sh:26-28] |
| -h, --help, help | Displays the usage message and exits successfully | Calls usage [scripts/verify.sh:29-32] |

### Script Functions

| Component | Stable Component ID | Description |
| --- | --- | --- |
| usage | a2012a5e-328e-53ba-9859-6ec386be77cc | Prints script usage and supported check names to standard error [scripts/verify.sh:4-10]. |
| run_check | 37c18a2a-c9eb-575b-9103-7673b10f6ef1 | Dispatches input parameters to the corresponding Rust/Cargo toolchains or error-handling flows [scripts/verify.sh:12-39]. |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/scripts/verify.sh\|scripts/verify.sh]] | `scripts/verify.sh` is a small Bash wrapper for running repository verification checks. It defines `usage` to print the supported check names and `run_check` to dispatch each requested name to the matching Cargo command: workspace build, nextest unit tests, doctests, formatting, or Clippy linting. The script defaults to running all checks when invoked with no arguments, and it exits early with help text or an error if the user asks for help or passes an unknown check. [scripts/verify.sh:4-10] [scripts/verify.sh:12-39] |

## Components

| Component ID |
| --- |
| `a2012a5e-328e-53ba-9859-6ec386be77cc` |
| `37c18a2a-c9eb-575b-9103-7673b10f6ef1` |
