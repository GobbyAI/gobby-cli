---
title: crates/gwiki/src/falkor_graph/sync.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/sync.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph/sync.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/falkor_graph/sync.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/falkor_graph/sync.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `sync_scope_from_postgres` | function | Synchronizes wiki graph facts from PostgreSQL to FalkorDB for a specified scope by loading facts, clearing the existing scope data, and executing generated graph write statements. [crates/gwiki/src/falkor_graph/sync.rs:13-29] |
| `clear_scope` | function | Deletes all WikiDoc, WikiSource, and WikiTarget nodes from the graph database whose scope_kind and scope_id match the provided SearchScope parameters. [crates/gwiki/src/falkor_graph/sync.rs:31-44] |
| `execute_statement` | function | Executes a Cypher query extracted from a 'GraphStatement' against a mutable 'GraphClient', returning an 'anyhow::Result<()>'. [crates/gwiki/src/falkor_graph/sync.rs:46-49] |
| `graph_sync_error` | function | This function transforms an 'anyhow::Error' into a 'WikiError::Config' variant with a formatted detail message indicating a gwiki graph synchronization failure to FalkorDB. [crates/gwiki/src/falkor_graph/sync.rs:51-55] |

