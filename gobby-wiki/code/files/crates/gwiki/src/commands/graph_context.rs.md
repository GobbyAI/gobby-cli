---
title: crates/gwiki/src/commands/graph_context.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/graph_context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/graph_context.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/graph_context.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/graph_context.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the requested scope, opens a read-only PostgreSQL connection using the gwiki graph-context index config, loads wiki graph facts and optionally project-scoped shared code graph edges while recording degraded/truncated sources, and returns a 'CommandOutcome' or 'WikiError' on configuration or connection failure. [crates/gwiki/src/commands/graph_context.rs:13-83] |
| `optional_falkor_config` | function | Resolves and returns an optional 'FalkorConfig' by building a config source from the Gobby home and primary Postgres client, mapping any resolution failures into 'WikiError::Config'. [crates/gwiki/src/commands/graph_context.rs:85-98] |

