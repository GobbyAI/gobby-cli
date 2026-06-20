---
title: crates/gwiki/src/support/graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/graph.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/graph.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gwiki/src/support/graph.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `memory_graph_from_store` | function | Constructs a 'graph::MemoryWikiGraph' from a 'store::MemoryWikiStore' by cloning all documents, resolved links, and sources into fact records for the given 'SearchScope', then replacing the graph’s facts with those records and an empty 'code_edges' list. [crates/gwiki/src/support/graph.rs:8-55] |
| `resolve_graph_target` | function | Trims and normalizes a raw link target, rejects external or empty targets, resolves it against the source path and wiki store by direct document path or slug lookup, and otherwise returns an unresolved graph link target. [crates/gwiki/src/support/graph.rs:57-90] |
| `resolve_relative_graph_path` | function | Returns 'raw_target' without a leading '/' when it is absolute or not path-like, otherwise resolves it against 'source_path'’s parent, normalizes the joined path, and converts it to a forward-slash string. [crates/gwiki/src/support/graph.rs:92-103] |
| `is_path_like_target` | function | Returns 'true' if 'target' looks path-like by containing a '/', starting with '.', or ending with '.md', and 'false' otherwise. [crates/gwiki/src/support/graph.rs:105-107] |
| `normalize_path` | function | Returns a new 'PathBuf' containing only the path’s normal components, skipping '.' and root/prefix components and resolving '..' by popping the last accumulated segment. [crates/gwiki/src/support/graph.rs:109-122] |
| `slug_target_map` | function | Builds a deterministic 'BTreeMap' from slugified document file stems and titles to the first 'PathBuf' encountered for each slug in 'store.documents', preserving earlier entries on collisions. [crates/gwiki/src/support/graph.rs:124-146] |
| `is_external_target` | function | Returns 'true' if 'target' is empty or looks like an external URL or link scheme, specifically if it contains '://', starts with '//', starts with '\\\\', or starts with 'mailto:'. [crates/gwiki/src/support/graph.rs:148-154] |

_Verified by 4 in-file unit tests._

