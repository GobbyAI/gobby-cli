---
title: crates/gcode/src/commands/init.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/init.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/init.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/init.rs` exposes 1 indexed API symbol.

## How it fits

`crates/gcode/src/commands/init.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run` | function | Resolves the project identity, optionally creates 'gcode.json', installs supported AI CLI skills unless the project is Gobby-managed, and then resolves the database URL to begin auto-indexing the project. [crates/gcode/src/commands/init.rs:11-148] |

