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

## crates/gcode/src/commands/graph

This module is the command-layer façade for all graph-related operations in the gcode CLI. It is divided into three functional sub-files — lifecycle management, graph payload queries, and graph read queries — plus a test suite that exercises each. The module sits between the CLI command dispatcher and the lower-level `crate::graph::code_graph` engine, translating raw graph backend results into formatted output (`Format::Json` or `Format::Text`) and applying user-facing hint text whenever the optional FalkorDB backend is absent or unreachable reads.rs:12–16, lifecycle.rs:1–8, payload.rs:1–5.

### Lifecycle (`lifecycle.rs`)

The lifecycle sub-module governs graph synchronisation actions. It exposes a `LifecycleBackend` trait whose `run` method accepts a `GraphLifecycleAction` and returns a `GraphLifecycleOutput` lifecycle.rs:76–80. Two structured contract-error constructors — `GraphSyncContractError::project_not_indexed` and `GraphSyncContractError::indexed_file_not_found` — emit typed JSON payloads and exit with the reserved code `GRAPH_SYNC_CONTRACT_EXIT_CODE = 2` lifecycle.rs:9, lifecycle.rs:16–50. Callers outside this module can interrogate `GraphSyncContractError::exit_code()`, serialize via `print()`, or inspect the raw `payload()` lifecycle.rs:44–52.

| Symbol | Kind | Notes |
|---|---|---|
| `GRAPH_SYNC_CONTRACT_EXIT_CODE` | `pub const u8 = 2` | Reserved exit code for contract errors lifecycle.rs:9 |
| `GraphSyncContractError` | `pub struct` | Wraps a `serde_json::Value` payload lifecycle.rs:11–14 |
| `GraphSyncContractError::project_not_indexed` | `pub(super) fn` | Emits `reason: "project_not_indexed"` lifecycle.rs:17–27 |
| `GraphSyncContractError::indexed_file_not_found` | `pub(super) fn` | Emits `reason: "indexed_file_not_found"` lifecycle.rs:29–39 |
| `LifecycleBackend` | `pub(super) trait` | Abstracts the sync backend lifecycle.rs:76 |
| `format_success_text` | `pub(super) fn` | Formats human-readable success line lifecycle.rs:68–74 |

### Payload queries (`payload.rs`)

The payload sub-module handles graph shape queries. `report` generates a `ProjectGraphReport` (Markdown rendered) and prints it; `overview` returns a project-wide `GraphPayload` up to a caller-supplied limit; `file` and `neighbors` scope the payload to a specific file path or symbol respectively payload.rs:48–79. Text formatting uses `format_graph_payload_text`, which renders node-and-link lists, while JSON output delegates directly to `output::print_json` payload.rs:6–42.

| Public function | Signature shape | Backend called |
|---|---|---|
| `report` | `(ctx, top_n, format)` | `graph::report::generate_report_with_options` payload.rs:49–55 |
| `overview` | `(ctx, limit, format)` | `code_graph::project_overview_graph` payload.rs:57–60 |
| `file` | `(ctx, file_path, format)` | `code_graph::file_graph` payload.rs:62–65 |
| `neighbors` | `(ctx, symbol_id, limit, format)` | `code_graph::*` payload.rs:67+ |

### Read queries (`reads.rs`)

The reads sub-module exposes paginated graph traversal commands — imports, callers, usages, and blast-radius — all returning `PagedResponse<GraphResult>` reads.rs:7. Symbol arguments are resolved through `crate::search::fts::ResolvedGraphSymbol` before being forwarded to the graph backend reads.rs:9. When result sets are large, token-budget hint strings guide callers to narrow queries via `--limit`, `--offset`, or more specific symbol identifiers reads.rs:14–16. Formatting helpers `format_grouped_graph_results`, `format_usage_result_line`, `format_caller_result_line`, `format_blast_radius_result_line`, and `format_symbol_path_text` are exercised directly by the test suite tests.rs:6–9.

| Hint constant | Value | Context |
|---|---|---|
| `GRAPH_BACKEND_HINT` | `"Graph commands require a configured FalkorDB graph backend…"` | Missing FalkorDB config reads.rs:12 |
| `USAGES_TOKEN_BUDGET_REFINE_HINT` | `` "`--limit`, `--offset`, or a more specific symbol query" `` | Large usages result reads.rs:14 |
| `BLAST_RADIUS_TOKEN_BUDGET_REFINE_HINT` | `` "`--depth`, a more specific symbol query, or a symbol UUID" `` | Large blast-radius result reads.rs:15 |

Degradation is a first-class concern. `graph_read_unavailable` detects `GraphReadError::NotConfigured` and `GraphReadError::Unreachable` reads.rs:51–58, and `empty_paged_response` returns a well-formed zero-result `PagedResponse` with an embedded hint rather than propagating the error reads.rs:61–76. The test `graph_reads_degrade_when_falkor_missing` confirms that calling `imports` against a context with `falkordb: None` exits without error tests.rs:43–48.

### Cross-module relationships

The module imports heavily from the graph engine layer (`crate::graph::code_graph`, `crate::graph::report`) and the shared infrastructure (`crate::config::Context`, `crate::db`, `crate::models`, `crate::output`, `crate::search::fts`, `crate::projection`, `crate::commands::token_budget`). It is called from above by the CLI command dispatcher, which routes subcommands to the public functions in `payload.rs` and `reads.rs` and lifecycle actions through the `LifecycleBackend` implementor registered at startup. No child modules exist beneath this level.
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

