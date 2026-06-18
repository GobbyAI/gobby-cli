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

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/mod.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/mod.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run` | function | Dispatches the given 'Command' enum variant to its corresponding module-level 'execute' function and returns that operation’s 'Result<CommandOutcome, WikiError>'. [crates/gwiki/src/commands/mod.rs:32-106] |
| `scoped_outcome` | function | Constructs a successful 'CommandOutcome' with exit code '0', a single status message of the form '"{command} resolved scope {scope}"', and a 'CommandResult' containing the supplied JSON 'payload' and 'text'. [crates/gwiki/src/commands/mod.rs:108-119] |
| `run_analysis_command` | function | Resolves the selected scope, executes the provided analysis closure on that scope’s root path and identity, serializes the returned report to JSON, and packages both the serialized payload and rendered summary into a scoped 'CommandOutcome'. [crates/gwiki/src/commands/mod.rs:121-145] |

