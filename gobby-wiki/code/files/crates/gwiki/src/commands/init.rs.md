---
title: crates/gwiki/src/commands/init.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/init.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/init.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/init.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/init.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the target scope, initializes the vault, seeds Obsidian metadata and project '.gitignore' as needed, rolls back created files if registry registration fails, and otherwise returns a rendered 'CommandOutcome' for the resolved scope identity. [crates/gwiki/src/commands/init.rs:9-26] |
| `render` | function | Builds a JSON payload and human-readable message for an '"init"' command indicating the scope, root path, and created directories/files, then returns the result via 'scoped_outcome("init", ...)'. [crates/gwiki/src/commands/init.rs:28-46] |

