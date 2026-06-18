---
title: crates/gwiki/src/graph/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/graph/mod.rs` exposes 59 indexed API symbols.

## How it fits

`crates/gwiki/src/graph/mod.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiGraphDocument` | class | Indexed class `WikiGraphDocument` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:22-26] |
| `WikiGraphSource` | class | Indexed class `WikiGraphSource` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:29-33] |
| `WikiGraphLinkTarget` | type | Indexed type `WikiGraphLinkTarget` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:36-39] |
| `WikiGraphLink` | class | Indexed class `WikiGraphLink` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:42-47] |
| `WikiGraphCodeEdge` | class | Indexed class `WikiGraphCodeEdge` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:50-59] |
| `WikiGraphFacts` | class | Indexed class `WikiGraphFacts` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:62-67] |
| `GraphExportOptions` | class | Indexed class `GraphExportOptions` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:70-72] |
| `GraphExportOptions::available` | method | Indexed method `GraphExportOptions::available` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:75-77] |
| `GraphExportOptions::degraded` | method | Indexed method `GraphExportOptions::degraded` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:79-81] |
| `GraphExport` | class | Indexed class `GraphExport` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:85-92] |
| `GraphExportNode` | class | Indexed class `GraphExportNode` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:95-103] |
| `GraphExportEdges` | class | Indexed class `GraphExportEdges` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:106-113] |
| `GraphExportEdge` | class | Indexed class `GraphExportEdge` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:116-122] |
| `GraphStatement` | class | Indexed class `GraphStatement` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:125-127] |
| `WikiBacklink` | class | Indexed class `WikiBacklink` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:130-135] |
| `LinkSuggestion` | class | Indexed class `LinkSuggestion` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:138-143] |
| `RelatedPathOptions` | class | Indexed class `RelatedPathOptions` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:146-148] |
| `RelatedPathOptions::default` | method | Indexed method `RelatedPathOptions::default` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:151-155] |
| `graph_write_statements` | function | Indexed function `graph_write_statements` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:158-239] |
| `MemoryWikiGraph` | class | Indexed class `MemoryWikiGraph` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:242-244] |
| `MemoryWikiGraph::replace_facts` | method | Indexed method `MemoryWikiGraph::replace_facts` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:247-249] |
| `MemoryWikiGraph::graph_facts_for_tests` | method | Indexed method `MemoryWikiGraph::graph_facts_for_tests` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:252-254] |
| `MemoryWikiGraph::backlinks` | method | Indexed method `MemoryWikiGraph::backlinks` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:256-290] |
| `MemoryWikiGraph::link_suggestions` | method | Indexed method `MemoryWikiGraph::link_suggestions` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:292-334] |
| `MemoryWikiGraph::Accumulator` | class | Indexed class `MemoryWikiGraph::Accumulator` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:298-301] |
| `MemoryWikiGraph::related_paths` | method | Indexed method `MemoryWikiGraph::related_paths` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:336-343] |
| `MemoryWikiGraph::related_paths_with_options` | method | Indexed method `MemoryWikiGraph::related_paths_with_options` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:345-405] |
| `MemoryWikiGraph::document_keys` | method | Indexed method `MemoryWikiGraph::document_keys` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:407-413] |
| `label` | function | Indexed function `label` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:416-418] |
| `rel` | function | Indexed function `rel` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:420-422] |
| `property` | function | Indexed function `property` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:424-426] |
| `string` | function | Indexed function `string` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:428-430] |
| `scope_properties` | function | Indexed function `scope_properties` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:432-440] |
| `scoped_path_properties` | function | Indexed function `scoped_path_properties` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:442-449] |
| `graph_path` | function | Indexed function `graph_path` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:451-453] |
| `document_node` | function | Indexed function `document_node` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:455-464] |
| `source_node` | function | Indexed function `source_node` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:466-475] |
| `citation_node` | function | Indexed function `citation_node` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:477-486] |
| `unresolved_target_node` | function | Indexed function `unresolved_target_node` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:488-497] |
| `document_id` | function | Indexed function `document_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:499-501] |
| `source_node_id` | function | Indexed function `source_node_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:503-505] |
| `citation_node_id` | function | Indexed function `citation_node_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:507-513] |
| `unresolved_target_id` | function | Indexed function `unresolved_target_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:515-517] |
| `code_endpoint_id` | function | Indexed function `code_endpoint_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:519-521] |
| `scoped_id` | function | Indexed function `scoped_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:523-532] |
| `readable_id_prefix` | function | Indexed function `readable_id_prefix` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:534-554] |
| `document_kind` | function | Indexed function `document_kind` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:556-565] |
| `is_code_path` | function | Indexed function `is_code_path` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:567-593] |
| `mermaid_node_id` | function | Indexed function `mermaid_node_id` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:595-599] |
| `mermaid_label` | function | Indexed function `mermaid_label` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:601-606] |
| `graph_labels_are_wiki_owned` | function | Indexed function `graph_labels_are_wiki_owned` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:613-679] |
| `graph_write_skips_relationships_to_missing_documents` | function | Indexed function `graph_write_skips_relationships_to_missing_documents` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:682-715] |
| `scoped_graph_ids_hash_structured_values` | function | Indexed function `scoped_graph_ids_hash_structured_values` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:718-725] |
| `backlinks_are_scope_filtered` | function | Indexed function `backlinks_are_scope_filtered` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:728-771] |
| `link_suggest_is_read_only` | function | Indexed function `link_suggest_is_read_only` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:774-817] |
| `related_paths_support_weight_options_and_skip_non_finite_scores` | function | Indexed function `related_paths_support_weight_options_and_skip_non_finite_scores` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:820-862] |
| `doc` | function | Indexed function `doc` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:864-870] |
| `resolved_link` | function | Indexed function `resolved_link` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:872-884] |
| `unresolved_link` | function | Indexed function `unresolved_link` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:886-893] |

