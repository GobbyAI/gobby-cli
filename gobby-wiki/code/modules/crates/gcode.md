---
title: crates/gcode
type: code_module
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/status.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/config/context.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/config/tests.rs
- file: crates/gcode/src/contract.rs
- file: crates/gcode/src/db/queries.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/index/languages.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcode/src/projection/sync.rs
- file: crates/gcode/src/search/fts/tests.rs
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/visibility.rs
provenance_truncated: 189
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode

Parent: [[code/modules/crates|crates]]

## Overview

## crates/gcode

`crates/gcode` is the top-level application crate for the Gcode toolchain. It houses the CLI binary entry point (`main`), a machine-readable contract surface (`crates/gcode/contract`), bundled static assets (`crates/gcode/assets`), and all runtime source logic (`crates/gcode/src`). The crate brings together every major subsystem — code indexing, graph analysis, vector search, AI documentation generation, project context resolution, and service configuration — into a single deployable `gcode` binary.

The build script (`build.rs:1-9`) is the crate's only compile-time gate. It watches one environment variable and conditionally emits a Cargo `cfg` flag that enables PostgreSQL-backed integration tests across the crate's test suite. When the variable is absent the cfg is never set, so Postgres tests are silently excluded rather than failing.

| Item | Detail |
|---|---|
| Env var watched | `GCODE_POSTGRES_TEST_DATABASE_URL` (`build.rs:2`) |
| Emitted cfg flag | `gcode_postgres_tests` (`build.rs:3,6`) |
| Rebuild trigger | `cargo:rerun-if-env-changed` on the same variable (`build.rs:2`) |

The `src` child module contains the bulk of public API symbols: the `Cli` struct and its command dispatch (`run`, `run_with_exit_code`, `dispatch_early_command`), typed command variants (`Command`, `GraphCommand`, `VectorCommand`, `EmbeddingsCommand`), and cross-cutting helpers for argument parsing (`AiRouteArg`, `AiDepthArg`, `AiProseDepthArg`), flag construction (`ai_flag`, `grep_flags`, `graph_read_flags`), and JSON output key contracts. The `contract` child module publishes `Contract`, `ContractCommand`, `ContractFlag`, and `BinaryContract` — the machine-readable specification against which the CLI's clap command tree is validated at test time via `clap_command_leaves_are_documented_in_contract`.

Externally, `crates/gcode` is the terminal consumer of nearly every other crate in the workspace: it calls into graph database code (FalkorDB via `CodeGraph`, `GraphPayload`), vector store code (Qdrant via `CodeSymbolVectorLifecycle`), the PostgreSQL index layer (`CodeFactSink`, search queries, schema validation), AI generation and verification pipelines, the codewiki documentation engine, and the multi-language parser/indexer. Nothing in the workspace imports from `crates/gcode`; it is strictly a consumer that wires all subsystems together and surfaces them through the CLI contract.
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21]
[crates/gcode/src/index/parser/calls/resolution.rs:6-10]
[crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]
[crates/gcode/src/vector/code_symbols/search.rs:8-14]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/assets\|crates/gcode/assets]] | ## crates/gcode/assets |
| [[code/modules/crates/gcode/contract\|crates/gcode/contract]] | ## crates/gcode/contract |
| [[code/modules/crates/gcode/src\|crates/gcode/src]] | ## crates/gcode/src |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/build.rs\|crates/gcode/build.rs]] | `crates/gcode/build.rs` exposes 1 indexed API symbol. |

