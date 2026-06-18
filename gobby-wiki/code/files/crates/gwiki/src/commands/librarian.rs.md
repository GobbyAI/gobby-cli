---
title: crates/gwiki/src/commands/librarian.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/librarian.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/librarian.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/librarian.rs` exposes 1 indexed API symbol.

## How it fits

`crates/gwiki/src/commands/librarian.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Dispatches the 'librarian' analysis command for the selected scope using default 'librarian::Options', then renders the result as text via 'librarian::render_text' and returns the resulting 'CommandOutcome' or 'WikiError'. [crates/gwiki/src/commands/librarian.rs:3-11] |

