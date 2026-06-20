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

`crates/gcode` is the GCode CLI crate and its surrounding contract/assets bundle. It defines a “Fast code index CLI for Gobby” contract at version 2, including invocation schema, global flags, scope resolution, command metadata, JSON output keys, and error-code metadata (crates/gcode/contract/gcode.contract.json:1-94). The main application layer owns CLI orchestration, configuration/context resolution, PostgreSQL index access, graph/vector projection lifecycle, search/grep, setup, freshness, visibility, and shared output/model contracts (crates/gcode/src/commands/grep.rs:1-100, crates/gcode/src/commands/search.rs:1-100).

The key runtime flow is command dispatch into thin handlers: handlers resolve a `Context`, connect to backing services, apply scope and visibility rules, then render through `output::Format`. `grep` runs that pattern over indexed chunks, while `search` combines exact, BM25, vector, and graph-style results before output (crates/gcode/src/commands/grep.rs:1-100, crates/gcode/src/commands/search.rs:1-100). The `assets/import_roots` data supports dependency/import resolution by mapping package or require identifiers to top-level API roots used by downstream indexing code.

At build time, the crate exposes a small Cargo build script that declares sensitivity to `GCODE_POSTGRES_TEST_DATABASE_URL`, registers `gcode_postgres_tests` as an allowed cfg, and enables that cfg only when the env var is present (crates/gcode/build.rs:1-9). This makes PostgreSQL-backed test code opt-in through environment configuration rather than always compiling it.

| Surface | Role | Evidence |
| --- | --- | --- |
| `contract` | Static CLI contract: version, flags, commands, output keys, errors | crates/gcode/contract/gcode.contract.json:1-94 |
| `src` | Main CLI implementation and service orchestration | crates/gcode/src/commands/grep.rs:1-100; crates/gcode/src/commands/search.rs:1-100 |
| `assets/import_roots` | Registry data for dependency/import root resolution | child module summary |
| `build.rs::main` | Cargo cfg setup for PostgreSQL test gating | crates/gcode/build.rs:1-9 |

| Environment Variable | Effect | Evidence |
| --- | --- | --- |
| `GCODE_POSTGRES_TEST_DATABASE_URL` | Triggers Cargo rerun and enables `cfg(gcode_postgres_tests)` when set | crates/gcode/build.rs:2-7 |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/assets\|crates/gcode/assets]] | `crates/gcode/assets` is a data-only asset area for GCode’s dependency/import resolution. Its child module, `assets/import_roots`, provides registry JSON files that map package or require identifiers to top-level API roots used by downstream indexing code. |
| [[code/modules/crates/gcode/contract\|crates/gcode/contract]] | `crates/gcode/contract` is the static contract surface for the `gcode` CLI, identified as contract version 2 and summarized as a “Fast code index CLI for Gobby” (crates/gcode/contract/gcode.contract.json:1-4). It centralizes the tool’s invocation schema: global flags, scope resolution, commands, JSON output keys, and error-code metadata (crates/gcode/contract/gcode.contract.json:5-94). |
| [[code/modules/crates/gcode/src\|crates/gcode/src]] | `crates/gcode/src` is the main gcode application crate: it owns the CLI surface, configuration/context resolution, PostgreSQL code-index access, graph/vector projection lifecycle, search/grep commands, setup, freshness, visibility, and shared output/model contracts. The command layer is thin orchestration: handlers resolve `Context`, connect to backing services, apply scope and visibility rules, then render through `output::Format`; `grep` follows this pattern over indexed chunks, while `search` merges exact, BM25, vector, and graph-style results (`crates/gcode/src/commands/grep.rs:1-100`,… |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/build.rs\|crates/gcode/build.rs]] | `crates/gcode/build.rs` exposes 1 indexed API symbol. |

