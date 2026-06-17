---
title: scripts/verify.sh
type: code_file
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

# scripts/verify.sh

Module: [[code/modules/scripts|scripts]]

## Purpose

`scripts/verify.sh` is a small Bash wrapper for running repository verification checks. It defines `usage` to print the supported check names and `run_check` to dispatch each requested name to the matching Cargo command: workspace build, nextest unit tests, doctests, formatting, or Clippy linting. The script defaults to running all checks when invoked with no arguments, and it exits early with help text or an error if the user asks for help or passes an unknown check.
[scripts/verify.sh:4-10]
[scripts/verify.sh:12-39]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `usage` | function | `usage() {` | `usage [function]` | `a2012a5e-328e-53ba-9859-6ec386be77cc` | 4-10 [scripts/verify.sh:4-10] | Indexed function `usage` in `scripts/verify.sh`. [scripts/verify.sh:4-10] |
| `run_check` | function | `run_check() {` | `run_check [function]` | `37c18a2a-c9eb-575b-9103-7673b10f6ef1` | 12-39 [scripts/verify.sh:12-39] | Indexed function `run_check` in `scripts/verify.sh`. [scripts/verify.sh:12-39] |
