---
title: crates/gcode/src/search/graph_boost.rs
type: code_file
provenance:
- file: crates/gcode/src/search/graph_boost.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/graph_boost.rs

Module: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Overview

`crates/gcode/src/search/graph_boost.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/search/graph_boost.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `graph_boost` | function | Returns an ordered, de-duplicated 'Vec<String>' of up to 10 caller and usage symbol IDs for the best exact-visible symbol match to 'query', or an empty vector if graph support, database connection, or symbol resolution is unavailable. [crates/gcode/src/search/graph_boost.rs:21-47] |
| `graph_expand` | function | Returns an empty list unless 'seed_ids' is nonempty, FalkorDB is configured, and a PostgreSQL connection is available; otherwise it filters the seed symbols to those visible to the caller, groups them by project, and expands the graph by collecting up to 30 callee IDs and 30 caller IDs per project via 'graph_expand_grouped'. [crates/gcode/src/search/graph_boost.rs:55-86] |
| `graph_expand_grouped` | function | Builds a deduplicated 'Vec<String>' by iterating each project’s ID group, deriving a project-specific visibility context, invoking 'graph_neighbors' to get callees and callers, and appending only non-empty IDs not previously seen. [crates/gcode/src/search/graph_boost.rs:88-106] |
| `make_ctx_no_falkordb` | function | Constructs a 'Context' test configuration with dummy PostgreSQL and project paths, 'project_id' set to '"test"', 'quiet' enabled, FalkorDB/Qdrant/embedding/daemon unset, and default code-vector and indexing settings with 'ProjectIndexScope::Single'. [crates/gcode/src/search/graph_boost.rs:113-127] |
| `make_ctx_with_overlay` | function | Constructs and returns a 'Context' for an overlay project, hardcoding local PostgreSQL/FalkorDB settings, disabling Qdrant and daemon access, using default vector/indexing configs, and setting 'index_scope' to an overlay mapping from project 'overlay' at '/overlay' onto parent project 'parent' at '/parent'. [crates/gcode/src/search/graph_boost.rs:129-153] |

_Verified by 4 in-file unit tests._

