---
title: crates/gwiki/src/models.rs
type: code_file
provenance:
- file: crates/gwiki/src/models.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/models.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/models.rs` exposes 21 indexed API symbols.

## How it fits

`crates/gwiki/src/models.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiScope` | type | Indexed type `WikiScope` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:12-15] |
| `WikiScope::kind` | method | Indexed method `WikiScope::kind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:18-23] |
| `WikiScope::identity` | method | Indexed method `WikiScope::identity` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:25-30] |
| `WikiScope::project_id` | method | Indexed method `WikiScope::project_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:32-37] |
| `WikiScope::topic_name` | method | Indexed method `WikiScope::topic_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:39-44] |
| `WikiScope::vector_collection_name` | method | Indexed method `WikiScope::vector_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:46-51] |
| `WikiSourceKind` | type | Indexed type `WikiSourceKind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:55-61] |
| `WikiSourceKind::as_str` | method | Indexed method `WikiSourceKind::as_str` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:64-72] |
| `WikiProvenance` | class | Indexed class `WikiProvenance` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:76-80] |
| `WikiDocumentRow` | class | Indexed class `WikiDocumentRow` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:83-97] |
| `WikiDocumentRow::new` | method | Indexed method `WikiDocumentRow::new` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:100-125] |
| `WikiDocumentRow::validate_scope_consistency` | method | Indexed method `WikiDocumentRow::validate_scope_consistency` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:127-149] |
| `validate_project_id` | function | Indexed function `validate_project_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:152-154] |
| `validate_topic_name` | function | Indexed function `validate_topic_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:156-158] |
| `project_collection_name` | function | Indexed function `project_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:160-166] |
| `topic_collection_name` | function | Indexed function `topic_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:168-174] |
| `validate_scope_id` | function | Indexed function `validate_scope_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:176-191] |
| `derived_storage_names_are_namespaced` | function | Indexed function `derived_storage_names_are_namespaced` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:198-236] |
| `document_row_constructor_keeps_denormalized_scope_consistent` | function | Indexed function `document_row_constructor_keeps_denormalized_scope_consistent` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:239-260] |
| `scope_storage_names_reject_path_like_or_nested_ids` | function | Indexed function `scope_storage_names_reject_path_like_or_nested_ids` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:263-284] |
| `scope_storage_names_reject_ascii_controls_only` | function | Indexed function `scope_storage_names_reject_ascii_controls_only` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:287-291] |

