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

# crates/gwiki/src/falkor_graph/sync.rs

Module: [[code/modules/crates/gwiki/src/falkor_graph|crates/gwiki/src/falkor_graph]]

## Purpose

This file synchronizes a gwiki search scope from Postgres into FalkorDB. It loads graph facts for a `SearchScope`, opens a `GraphClient` from Falkor config, clears any existing `WikiDoc`, `WikiSource`, and `WikiTarget` nodes for that scope, then replays the generated Cypher write statements into the graph. The helper functions encapsulate scoped deletion, statement execution, and conversion of sync/connect failures into `WikiError::Config`.
[crates/gwiki/src/falkor_graph/sync.rs:13-29]
[crates/gwiki/src/falkor_graph/sync.rs:31-44]
[crates/gwiki/src/falkor_graph/sync.rs:46-49]
[crates/gwiki/src/falkor_graph/sync.rs:51-55]

## API Symbols

- `sync_scope_from_postgres` (function) component `sync_scope_from_postgres [function]` (`770ff3b5-3bd6-545f-805c-ed9f07a88298`) lines 13-29 [crates/gwiki/src/falkor_graph/sync.rs:13-29]
  - Signature: `pub(crate) fn sync_scope_from_postgres(`
  - Purpose: Loads wiki graph facts for the given 'SearchScope' from Postgres, connects to FalkorDB using the provided config, clears the corresponding scope in the graph, and replays all generated write statements into the graph, returning any connection or sync errors as 'WikiError'. [crates/gwiki/src/falkor_graph/sync.rs:13-29]
- `clear_scope` (function) component `clear_scope [function]` (`988a1ff8-f62d-573d-ac49-fa72e1241701`) lines 31-44 [crates/gwiki/src/falkor_graph/sync.rs:31-44]
  - Signature: `fn clear_scope(client: &mut GraphClient, scope: &SearchScope) -> anyhow::Result<()> {`
  - Purpose: Deletes all 'WikiDoc', 'WikiSource', and 'WikiTarget' nodes matching the given scope by 'scope_kind' and 'scope_id' in the graph, but returns an error if the scope is global and therefore cannot be cleared as a scoped projection. [crates/gwiki/src/falkor_graph/sync.rs:31-44]
- `execute_statement` (function) component `execute_statement [function]` (`e353979f-80a6-56cd-993f-957f8701d872`) lines 46-49 [crates/gwiki/src/falkor_graph/sync.rs:46-49]
  - Signature: `fn execute_statement(client: &mut GraphClient, statement: GraphStatement) -> anyhow::Result<()> {`
  - Purpose: Executes the statement’s Cypher query against the provided 'GraphClient' with no parameters and returns 'Ok(())' if the query succeeds. [crates/gwiki/src/falkor_graph/sync.rs:46-49]
- `graph_sync_error` (function) component `graph_sync_error [function]` (`16c528c1-6f71-5f96-8d12-86160d9397e8`) lines 51-55 [crates/gwiki/src/falkor_graph/sync.rs:51-55]
  - Signature: `fn graph_sync_error(error: anyhow::Error) -> WikiError {`
  - Purpose: Converts an 'anyhow::Error' into a 'WikiError::Config' with a detail message stating that syncing the gwiki graph to FalkorDB failed, including the original error text. [crates/gwiki/src/falkor_graph/sync.rs:51-55]

