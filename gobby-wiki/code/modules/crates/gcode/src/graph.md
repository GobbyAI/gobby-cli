---
title: crates/gcode/src/graph
type: code_module
provenance:
- file: crates/gcode/src/graph/code_graph.rs
- file: crates/gcode/src/graph/code_graph/connection.rs
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/read.rs
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
- file: crates/gcode/src/graph/code_graph/read/support.rs
- file: crates/gcode/src/graph/code_graph/tests.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
- file: crates/gcode/src/graph/code_graph/write/support.rs
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
- file: crates/gcode/src/graph/mod.rs
- file: crates/gcode/src/graph/report.rs
- file: crates/gcode/src/graph/report/generation.rs
- file: crates/gcode/src/graph/report/loading.rs
- file: crates/gcode/src/graph/report/queries.rs
- file: crates/gcode/src/graph/report/render.rs
- file: crates/gcode/src/graph/report/rows.rs
- file: crates/gcode/src/graph/report/summary.rs
- file: crates/gcode/src/graph/report/tests.rs
- file: crates/gcode/src/graph/report/time.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/graph/typed_query.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

## crates/gcode/src/graph

The `graph` module is the central engine for building, querying, and reporting on a code-knowledge graph that maps symbols, files, calls, and imports across a project. It is divided into three public sub-modules declared in `mod.rs` (lines 1–4): `code_graph`, `report`, and `typed_query`. Together they form a layered stack — `typed_query` provides safe Cypher serialization, `code_graph` owns all graph persistence and traversal logic against a running graph daemon, and `report` aggregates the stored graph into human-readable analytics.

`code_graph` is itself composed of private sub-modules (`connection`, `lifecycle`, `payload`, `read`, `write`) that are unified by a flat re-export surface in `code_graph.rs` (lines 8–49). The lifecycle layer (`GraphLifecycleAction`, `GraphLifecycleRequest`, `GraphLifecycleTimeouts`, `run_lifecycle_action`) drives daemon start/stop/status over HTTP, resolving the daemon URL via `require_daemon_url` and routing through `build_lifecycle_url`. The read layer exposes high-level graph traversal functions (`project_overview_graph`, `file_graph`, `symbol_neighbors`, `blast_radius`, `shortest_symbol_path`, batch caller/callee lookups) that execute against the daemon and deserialize rows into `GraphNode`, `GraphLink`, and `GraphPayload` structures. The write layer (`CodeGraph`, `sync_file_graph`, `delete_file_graph`, `clear_project`, `cleanup_orphans`) handles upsert and teardown of nodes and edges, including sentinel-skipping logic for unparsed imports and project-scoped orphan cleanup confirmed by tests `cleanup_orphans_is_project_scoped` and `clear_project_is_project_scoped`.

`typed_query` (lines 1–100 of `typed_query.rs`) is a standalone, dependency-light module that wraps a Cypher string with a `HashMap<String, String>` of pre-rendered parameters. All values flow through `render_cypher_value`, which handles the full `TypedValue` variant set (`Null`, `String`, `Integer`, `Float`, `Bool`, `List`, `Map`) and rejects non-finite floats via `TypedQueryError::NonFiniteFloat`. Identifiers (parameter names and map keys) are validated by `validate_identifier`, producing `TypedQueryError::InvalidIdentifier` on failure. This ensures that no raw user input reaches the Cypher engine without escaping, enforced by tests such as `string_literals_escape_both_quote_delimiters` and `unsafe_values_return_typed_errors`.

`report` (re-exports in `report.rs` lines 12–16) generates `ProjectGraphReport` values from live graph queries or offline snapshots through `generate_report`, `generate_report_with_options`, `generate_report_from_snapshot`, and `empty_report`. The report pipeline loads hotspots, incoming-call hotspots, target frequencies, and bridge-edge hypotheses (`BridgeEdgeHypothesis`), then renders Markdown output via `render_markdown` with CommonMark-compliant backtick escaping. A degradation contract (`ReportDegradation`) allows the report to degrade gracefully when the graph service is unavailable, confirmed by `report_degradation_contract`.

### Public API — `typed_query`

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TypedQuery` | struct | Cypher string + rendered params map |
| `TypedQuery::new` | method | Create query with no params |
| `TypedQuery::with_params` | method | Create query with typed params, validates all |
| `TypedQuery::insert_param` | method | Add/overwrite one validated param |
| `TypedValue` | enum | Rust-side Cypher value (`Null`/`String`/`Integer`/`Float`/`Bool`/`List`/`Map`) |
| `IdentifierKind` | enum | `ParameterName` or `MapKey` — context for validation errors |
| `TypedQueryError` | enum | `InvalidIdentifier` or `NonFiniteFloat` |
| `cypher_string_literal` | fn | Escape and single-quote a bare string |
| `render_cypher_value` | fn | Recursively render a `TypedValue` to a Cypher literal |
| `validate_identifier` | fn | Reject identifiers that would break Cypher syntax |
| `clamp_limit` / `clamp_offset` | fn | Pagination guard utilities |
| `id_list_literal` | fn | Render a list of IDs as a Cypher literal |

### Public API — `code_graph` (graph lifecycle)

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphLifecycleAction` | type | Variant set of daemon lifecycle operations |
| `GraphLifecycleAction::cli_command` | method | Maps action to CLI command string |
| `GraphLifecycleAction::endpoint_path` | method | HTTP path for the action |
| `GraphLifecycleAction::success_prefix` | method | Expected response prefix for success detection |
| `GraphLifecycleRequest` | struct | Carries request context for a lifecycle call |
| `GraphLifecycleRequest::from_context` | method | Construct from ambient context |
| `GraphLifecycleTimeouts` | struct | Per-action timeout config, reads from env |
| `GraphLifecycleTimeouts::from_env` | method | Populate from environment variables |
| `GraphLifecycleTimeouts::for_action` | method | Look up timeout for a specific action |
| `run_lifecycle_action` | fn | Execute a lifecycle action with retries |
| `require_daemon_url` | fn | Resolve and validate daemon base URL |
| `GraphReadError` | type | Error surface for read failures |
| `GraphReadRequest` | struct | Typed read request descriptor |

### Public API — `code_graph` (read traversals)

| Function | Purpose |
| --- | --- |
| `project_overview_graph` | Full-project node/link overview |
| `file_graph` | Nodes and calls scoped to one file |
| `symbol_neighbors` | Immediate neighbors of a symbol node |
| `blast_radius` / `blast_radius_graph` | Upstream/downstream impact set for a target |
| `shortest_symbol_path` | BFS path between two symbols |
| `count_callers` / `count_usages` | Aggregate edge counts |
| `find_callers` / `find_usages` | Paginated caller/usage lists |
| `find_callers_batch` / `find_callees_batch` | Batch traversals across symbol sets |
| `find_caller_ids` / `find_usage_ids` | ID-only variants for lightweight lookups |
| `get_imports` | File-level import edges |
| `resolve_external_call_target` | Resolve ambiguous external call targets |

### Public API — `report`

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `generate_report` | fn | Live report from graph daemon |
| `generate_report_with_options` | fn | Report with `ProjectGraphReportOptions` overrides |
| `empty_report` | fn | Zero-data report for degraded state |
| `ProjectGraphReport` | struct | Top-level report value |
| `ProjectGraphReportOptions` | struct | Limit, hotspot count, etc. (defaults via `default()`) |
| `GraphReportSummary` | struct | Node/edge count summary |
| `GraphReportHotspots` | struct | Ranked hotspot list |
| `GraphHotspot` | struct | Single hotspot entry with degree stats |
| `BridgeEdgeHypothesis` | struct | Inferred cross-boundary edge hypothesis |
| `BridgeReportSummary` | struct | Aggregated bridge-edge findings |
| `TargetFrequency` | struct | Call-target occurrence frequency |
| `ReportDegradation` | struct | Signals partial/unavailable data |
| `ConfidenceRange` | struct | Score band for edge confidence |
| `NamedCount` | struct | `(name, count)` pair used in summaries |
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
[crates/gcode/src/graph/code_graph/connection.rs:7-12]
[crates/gcode/src/graph/code_graph/lifecycle.rs:18-21]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/graph/code_graph\|crates/gcode/src/graph/code_graph]] | ## crates/gcode/src/graph/code\_graph |
| [[code/modules/crates/gcode/src/graph/report\|crates/gcode/src/graph/report]] | ## crates/gcode/src/graph/report |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/graph/code_graph.rs\|crates/gcode/src/graph/code_graph.rs]] | `crates/gcode/src/graph/code_graph.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/graph/mod.rs\|crates/gcode/src/graph/mod.rs]] | `crates/gcode/src/graph/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report.rs\|crates/gcode/src/graph/report.rs]] | `crates/gcode/src/graph/report.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/graph/typed_query.rs\|crates/gcode/src/graph/typed_query.rs]] | `crates/gcode/src/graph/typed_query.rs` exposes 25 indexed API symbols. |

