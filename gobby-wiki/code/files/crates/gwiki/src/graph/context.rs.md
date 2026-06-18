---
title: crates/gwiki/src/graph/context.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/context.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/graph/context.rs` exposes 35 indexed API symbols.

## How it fits

`crates/gwiki/src/graph/context.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphContextOptions` | class | Indexed class `GraphContextOptions` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:8-11] |
| `GraphContextOptions::available` | method | Indexed method `GraphContextOptions::available` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:14-16] |
| `GraphContextOptions::degraded` | method | Indexed method `GraphContextOptions::degraded` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:18-23] |
| `GraphContextOptions::with_truncated_components` | method | Indexed method `GraphContextOptions::with_truncated_components` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:25-28] |
| `GraphContextPack` | class | Indexed class `GraphContextPack` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:32-39] |
| `GraphContextScope` | class | Indexed class `GraphContextScope` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:42-45] |
| `GraphContextDegradation` | class | Indexed class `GraphContextDegradation` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:48-53] |
| `GraphContextWarning` | class | Indexed class `GraphContextWarning` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:56-61] |
| `GraphContextNeighborhood` | class | Indexed class `GraphContextNeighborhood` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:64-73] |
| `GraphContextNeighbor` | class | Indexed class `GraphContextNeighbor` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:76-80] |
| `GraphContextDocLink` | class | Indexed class `GraphContextDocLink` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:83-88] |
| `GraphContextCodeEdge` | class | Indexed class `GraphContextCodeEdge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:91-99] |
| `GraphContextRecommendation` | class | Indexed class `GraphContextRecommendation` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:102-105] |
| `build_context_pack` | function | Indexed function `build_context_pack` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:107-153] |
| `context_scope` | function | Indexed function `context_scope` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:155-172] |
| `citations_by_document` | function | Indexed function `citations_by_document` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:174-183] |
| `degradation_warnings` | function | Indexed function `degradation_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:185-201] |
| `capped_graph_warning` | function | Indexed function `capped_graph_warning` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:203-212] |
| `stale_link_warnings` | function | Indexed function `stale_link_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:214-227] |
| `audit_warnings` | function | Indexed function `audit_warnings` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:229-242] |
| `neighbors_for_path` | function | Indexed function `neighbors_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:244-272] |
| `doc_links_for_path` | function | Indexed function `doc_links_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:274-311] |
| `code_calls_for_path` | function | Indexed function `code_calls_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:313-320] |
| `code_imports_for_path` | function | Indexed function `code_imports_for_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:322-329] |
| `graph_context_code_edge` | function | Indexed function `graph_context_code_edge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:331-340] |
| `recommendations` | function | Indexed function `recommendations` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:342-390] |
| `display_path` | function | Indexed function `display_path` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:392-394] |
| `graph_context_json_includes_neighborhoods_and_empty_code_edges` | function | Indexed function `graph_context_json_includes_neighborhoods_and_empty_code_edges` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:407-502] |
| `graph_context_json_reports_truncated_shared_code_as_capped_data` | function | Indexed function `graph_context_json_reports_truncated_shared_code_as_capped_data` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:505-557] |
| `ask_unified_graph_context_merges_wiki_and_code_edges` | function | Indexed function `ask_unified_graph_context_merges_wiki_and_code_edges` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:560-654] |
| `doc` | function | Indexed function `doc` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:656-662] |
| `source` | function | Indexed function `source` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:664-670] |
| `resolved_link` | function | Indexed function `resolved_link` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:672-684] |
| `unresolved_link` | function | Indexed function `unresolved_link` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:686-693] |
| `code_edge` | function | Indexed function `code_edge` in `crates/gwiki/src/graph/context.rs`. [crates/gwiki/src/graph/context.rs:695-714] |

