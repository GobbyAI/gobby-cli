---
title: crates/gcode/src/cli
type: code_module
provenance:
- file: crates/gcode/src/cli/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `crates/gcode/src/cli` test surface enforces that every leaf Clap command exposed by `Cli::command()` is documented in the generated Gobby contract. It imports the parent CLI definitions with `super::*`, uses Clap’s `CommandFactory`, and compares discovered command paths against `gobby_code::contract::contract().commands` .

The key flow starts by building the Clap command tree, collecting only leaf subcommands, and diffing those leaves against contract command names. Missing entries fail the test with a comma-separated list, making this module a guardrail between CLI implementation and external command metadata .

Collaboration-wise, this module is called by the Rust test runner, calls into the parent CLI via `Cli::command()`, calls out to `gobby_code::contract::contract()`, and uses Clap’s `get_subcommands()` API to recursively traverse nested commands  . The test suite is further split into focused sibling test modules for `codewiki`, `grep`, `projection`, `search`, and `top_level` coverage .

| Symbol | Kind | Responsibility |
| --- | --- | --- |
| `clap_command_leaves_are_documented_in_contract` | test function | Verifies every Clap leaf command has a contract entry  |
| `clap_command_leaves` | helper function | Initializes collection of leaf command paths  |
| `collect_clap_command_leaves` | helper function | Recursively walks subcommands and records leaf paths  |
[crates/gcode/src/cli/tests.rs:12-30]
[crates/gcode/src/cli/tests.rs:32-36]
[crates/gcode/src/cli/tests.rs:38-55]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/cli/tests.rs\|crates/gcode/src/cli/tests.rs]] | `crates/gcode/src/cli/tests.rs` exposes 3 indexed API symbols. |

