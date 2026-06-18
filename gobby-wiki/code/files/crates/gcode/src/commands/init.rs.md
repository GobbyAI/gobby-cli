---
title: crates/gcode/src/commands/init.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/init.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/init.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview
The `crates/gcode/src/commands/init.rs` file manages the initialization process for a codebase. Its primary role is to establish a verified project identity and prepare the repository environment for search and query capabilities.

For self-managed environments, the process integrates with `crate::skill` to install CLI extension targets in `crates/gcode/src/commands/init.rs:31-52`. This allows AI assistant capabilities to be deployed directly into the workspace.

Finally, the command connects with `crate::db` to retrieve the active database URL in `crates/gcode/src/commands/init.rs:57`. It packages these references into an indexing context defined in `crates/gcode/src/commands/init.rs:58-67`, feeding configuration state directly into the auto-indexing pipeline. [crates/gcode/src/commands/init.rs:11-148]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run` | function | Resolves the project identity, optionally creates 'gcode.json', installs supported AI CLI skills unless the project is Gobby-managed, and then resolves the database URL to begin auto-indexing the project. [crates/gcode/src/commands/init.rs:11-148] |

