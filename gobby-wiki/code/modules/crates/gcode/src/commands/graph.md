---
title: crates/gcode/src/commands/graph
type: code_module
provenance:
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/payload.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/graph/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph

Parent: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

The `crates/gcode/src/commands/graph` module implements graph-oriented command handlers for both lifecycle operations and read/query output. Its read path imports configuration, database access, graph read APIs, full-text symbol resolution, token-budget helpers, shared models, and output formatting, then degrades gracefully when FalkorDB is absent or unreachable by emitting hints and empty paged JSON/text responses where appropriate (`reads.rs:1-100`). Lifecycle handling owns graph sync contract errors, including structured JSON payloads and a dedicated exit code for sync-file contract failures (`lifecycle.rs:1-100`).

Payload commands provide user-facing graph exports and reports: project reports are generated through `crate::graph::report::generate_report_with_options`, while overview, file, and neighbor graph payloads call into `crate::graph::code_graph` and then render either JSON or compact text (`payload.rs:1-97`). Tests exercise the command surface through `super::{imports, report}`, validate degraded reads without FalkorDB, verify Markdown report text, and cover text formatting helpers for grouped results and symbol paths (`tests.rs:1-100`).

The wider collaboration pattern is command-layer orchestration over shared services: this module receives a `Context`, calls graph backends in `crate::graph::code_graph`, consults `crate::db` and `crate::search::fts` for read flows, uses projection sync/report types for lifecycle work, and emits through `crate::output` in `Format::Json` or `Format::Text` (`reads.rs:1-100`, `lifecycle.rs:1-100`, `payload.rs:1-97`). Its test module imports public command functions and helper formatters from the sibling graph files, showing that formatting behavior and failure contracts are part of the expected command semantics (`tests.rs:1-100`).

| Public symbol / fact | Purpose | Source |
| --- | --- | --- |
| `GRAPH_SYNC_CONTRACT_EXIT_CODE` | Exit code `2` for graph sync-file contract errors | `lifecycle.rs:1-100` |
| `GraphSyncContractError` | Structured sync contract failure with JSON payload, `exit_code`, `print`, and `payload` accessors | `lifecycle.rs:1-100` |
| `format_report_text` | Returns report Markdown for text output | `payload.rs:1-97` |
| `report(ctx, top_n, format)` | Generates a project graph report and prints JSON or Markdown text | `payload.rs:1-97` |
| `overview(ctx, limit, format)` | Prints a project overview graph payload | `payload.rs:1-97` |
| `file(ctx, file_path, format)` | Prints a file-specific graph payload | `payload.rs:1-97` |
| `GRAPH_BACKEND_HINT` | Hint used when FalkorDB graph backend/projection is unavailable | `reads.rs:1-100` |
[crates/gcode/src/commands/graph/lifecycle.rs:12-14]
[crates/gcode/src/commands/graph/payload.rs:6-37]
[crates/gcode/src/commands/graph/reads.rs:19-25]
[crates/gcode/src/commands/graph/tests.rs:22-36]
[crates/gcode/src/commands/graph/lifecycle.rs:17-28]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/graph/lifecycle.rs\|crates/gcode/src/commands/graph/lifecycle.rs]] | `crates/gcode/src/commands/graph/lifecycle.rs` exposes 25 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] | `crates/gcode/src/commands/graph/payload.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] | `crates/gcode/src/commands/graph/reads.rs` exposes 42 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/tests.rs\|crates/gcode/src/commands/graph/tests.rs]] | `crates/gcode/src/commands/graph/tests.rs` exposes 24 indexed API symbols. |

