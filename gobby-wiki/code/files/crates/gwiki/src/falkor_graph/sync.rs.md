---
title: crates/gwiki/src/falkor_graph/sync.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/sync.rs
  ranges:
  - 13-29
  - 31-44
  - 46-49
  - 51-55
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/falkor_graph/sync.rs:13-29](crates/gwiki/src/falkor_graph/sync.rs#L13-L29), [crates/gwiki/src/falkor_graph/sync.rs:31-44](crates/gwiki/src/falkor_graph/sync.rs#L31-L44), [crates/gwiki/src/falkor_graph/sync.rs:46-49](crates/gwiki/src/falkor_graph/sync.rs#L46-L49), [crates/gwiki/src/falkor_graph/sync.rs:51-55](crates/gwiki/src/falkor_graph/sync.rs#L51-L55)

</details>

# crates/gwiki/src/falkor_graph/sync.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file syncs a wiki graph projection from Postgres into FalkorDB. `sync_scope_from_postgres` loads graph facts for a `SearchScope`, opens a FalkorDB `GraphClient` from config, clears any existing nodes for that scope, then writes the new graph statements one by one. `clear_scope` deletes existing `WikiDoc`, `WikiSource`, and `WikiTarget` nodes for a scoped projection, but refuses to clear the global scope because it cannot be represented as a scoped delete. `execute_statement` is a small helper that runs each generated Cypher statement. `graph_sync_error` maps FalkorDB failures into `WikiError::Config` with a sync-specific message.
[crates/gwiki/src/falkor_graph/sync.rs:13-29]
[crates/gwiki/src/falkor_graph/sync.rs:31-44]
[crates/gwiki/src/falkor_graph/sync.rs:46-49]
[crates/gwiki/src/falkor_graph/sync.rs:51-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `sync_scope_from_postgres` | function | `pub(crate) fn sync_scope_from_postgres(` | `sync_scope_from_postgres [function]` | `770ff3b5-3bd6-545f-805c-ed9f07a88298` | 13-29 [crates/gwiki/src/falkor_graph/sync.rs:13-29] | Indexed function `sync_scope_from_postgres` in `crates/gwiki/src/falkor_graph/sync.rs`. [crates/gwiki/src/falkor_graph/sync.rs:13-29] |
| `clear_scope` | function | `fn clear_scope(client: &mut GraphClient, scope: &SearchScope) -> anyhow::Result<()> {` | `clear_scope [function]` | `988a1ff8-f62d-573d-ac49-fa72e1241701` | 31-44 [crates/gwiki/src/falkor_graph/sync.rs:31-44] | Indexed function `clear_scope` in `crates/gwiki/src/falkor_graph/sync.rs`. [crates/gwiki/src/falkor_graph/sync.rs:31-44] |
| `execute_statement` | function | `fn execute_statement(client: &mut GraphClient, statement: GraphStatement) -> anyhow::Result<()> {` | `execute_statement [function]` | `e353979f-80a6-56cd-993f-957f8701d872` | 46-49 [crates/gwiki/src/falkor_graph/sync.rs:46-49] | Indexed function `execute_statement` in `crates/gwiki/src/falkor_graph/sync.rs`. [crates/gwiki/src/falkor_graph/sync.rs:46-49] |
| `graph_sync_error` | function | `fn graph_sync_error(error: anyhow::Error) -> WikiError {` | `graph_sync_error [function]` | `16c528c1-6f71-5f96-8d12-86160d9397e8` | 51-55 [crates/gwiki/src/falkor_graph/sync.rs:51-55] | Indexed function `graph_sync_error` in `crates/gwiki/src/falkor_graph/sync.rs`. [crates/gwiki/src/falkor_graph/sync.rs:51-55] |
