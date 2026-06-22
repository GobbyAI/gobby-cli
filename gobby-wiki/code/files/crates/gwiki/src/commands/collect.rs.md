---
title: crates/gwiki/src/commands/collect.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/collect.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/collect.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/collect.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/collect.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the command scope from 'selection', idempotently initializes the vault, creates an in-memory wiki store, collects inbox and index data for 'scope.root()' using the current timestamp, and returns the rendered 'CommandOutcome'. [crates/gwiki/src/commands/collect.rs:10-20] |
| `render` | function | Builds a 'collect' command outcome by counting accepted and skipped items from 'report', packaging the scope, root path, counts, and full report into a JSON payload plus a formatted status message, and returning 'scoped_outcome("collect", ...)'. [crates/gwiki/src/commands/collect.rs:22-43] |

