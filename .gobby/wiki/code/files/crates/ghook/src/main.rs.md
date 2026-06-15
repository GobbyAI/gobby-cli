---
title: crates/ghook/src/main.rs
type: code_file
provenance:
- file: crates/ghook/src/main.rs
  ranges:
  - 40-63
  - 65-81
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/main.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

This file is the `ghook` CLI entrypoint and mode dispatcher. `main` parses command-line arguments, then routes to version handling, diagnostics, or gobby-owned hook execution; if no valid mode is selected, it prints a usage error and exits with code 2. `run_diagnose` implements the diagnostic path by requiring both `--cli` and `--type`, calling `diagnose::diagnose`, and printing the result as pretty JSON on stdout, or reporting an error and returning exit code 2 if validation or serialization fails.
[crates/ghook/src/main.rs:40-63]
[crates/ghook/src/main.rs:65-81]

## API Symbols

- `main` (function) component `main [function]` (`dee4d56b-3252-5af3-b9d2-b1548601bf33`) lines 40-63 [crates/ghook/src/main.rs:40-63]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Parses CLI arguments and dispatches to version output, diagnostics, or gobby-owned execution, otherwise prints an error and exits with code 2. [crates/ghook/src/main.rs:40-63]
- `run_diagnose` (function) component `run_diagnose [function]` (`80fd2295-eda8-5a6e-88af-12217cc3aa17`) lines 65-81 [crates/ghook/src/main.rs:65-81]
  - Signature: `fn run_diagnose(args: &Args) -> ExitCode {`
  - Purpose: Validates that '--cli' and '--type' are both present, runs 'diagnose::diagnose(cli, hook_type)', prints the result as pretty JSON to stdout on success, and otherwise emits an error to stderr and returns exit code '2'. [crates/ghook/src/main.rs:65-81]

