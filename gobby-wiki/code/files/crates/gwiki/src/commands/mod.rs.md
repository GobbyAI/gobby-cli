---
title: crates/gwiki/src/commands/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/mod.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

`crates/gwiki/src/commands/mod.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run` | function | The 'run' function pattern matches on a 'Command' enum to delegate to the appropriate subcommand execution handler, returning a 'Result' containing either a 'CommandOutcome' or 'WikiError'. [crates/gwiki/src/commands/mod.rs:32-108] |
| `scoped_outcome` | function | Constructs and returns a 'CommandOutcome' with exit code 0, embedding the provided payload and text into a 'CommandResult' and generating a status message indicating the command resolved the specified scope. [crates/gwiki/src/commands/mod.rs:110-121] |
| `run_analysis_command` | function | Executes a scoped analysis closure, serializes its generic result to JSON, and returns a CommandOutcome containing both the serialized payload and rendered string representation. [crates/gwiki/src/commands/mod.rs:123-147] |

