---
title: crates/ghook/src/main.rs
type: code_file
provenance:
- file: crates/ghook/src/main.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/main.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/main.rs` exposes 2 indexed API symbols.

## How it fits

`crates/ghook/src/main.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `main` | function | Parses CLI arguments and dispatches to '--version' stamp writing, '--diagnose', or '--gobby-owned' handling, otherwise emits an error and exits with code 2. [crates/ghook/src/main.rs:40-63] |
| `run_diagnose` | function | Validates that '--cli' and '--type' are present, runs 'diagnose::diagnose' with those values, prints the result as pretty JSON to stdout on success, and returns exit code '2' with an error message if arguments are missing or serialization fails. [crates/ghook/src/main.rs:65-81] |

