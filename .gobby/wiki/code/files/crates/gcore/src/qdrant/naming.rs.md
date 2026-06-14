---
title: crates/gcore/src/qdrant/naming.rs
type: code_file
provenance:
- file: crates/gcore/src/qdrant/naming.rs
  ranges:
  - 3-10
  - 13-22
  - 25-43
  - 45-70
  - 77-90
  - 93-110
  - 113-124
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/qdrant/naming.rs

Module: [[code/modules/crates/gcore/src/qdrant|crates/gcore/src/qdrant]]

## Purpose

Defines Qdrant collection naming rules. `CollectionScope` models three naming modes: project-scoped, topic-scoped, or custom. `collection_name` builds the final collection name from a namespace and scope, while `validate_collection_name_component` enforces that each component is non-empty, trimmed, non-reserved, and free of path-like or control/whitespace characters. `CollectionNameError` captures the specific validation failures. The tests verify that scoped names are generated for all scope variants and that invalid custom or scoped components are rejected.
[crates/gcore/src/qdrant/naming.rs:3-10]
[crates/gcore/src/qdrant/naming.rs:13-22]
[crates/gcore/src/qdrant/naming.rs:25-43]
[crates/gcore/src/qdrant/naming.rs:45-70]
[crates/gcore/src/qdrant/naming.rs:77-90]

## API Symbols

- `CollectionScope` (type) component `CollectionScope [type]` (`abbe32ae-0e46-50b7-b285-ac9fa5e9e8e6`) lines 3-10 [crates/gcore/src/qdrant/naming.rs:3-10]
  - Signature: `pub enum CollectionScope<'a> {`
  - Purpose: Indexed type `CollectionScope` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:3-10]
- `CollectionNameError` (type) component `CollectionNameError [type]` (`92855afa-85af-5755-85c0-f142ec859337`) lines 13-22 [crates/gcore/src/qdrant/naming.rs:13-22]
  - Signature: `pub enum CollectionNameError {`
  - Purpose: Indexed type `CollectionNameError` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:13-22]
- `collection_name` (function) component `collection_name [function]` (`704b9e85-52a6-5bb2-ac95-ce0749de0ef1`) lines 25-43 [crates/gcore/src/qdrant/naming.rs:25-43]
  - Signature: `pub fn collection_name(`
  - Purpose: Indexed function `collection_name` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:25-43]
- `validate_collection_name_component` (function) component `validate_collection_name_component [function]` (`147cebfa-0217-5938-87b2-c119945fc554`) lines 45-70 [crates/gcore/src/qdrant/naming.rs:45-70]
  - Signature: `fn validate_collection_name_component(name: &str) -> Result<(), CollectionNameError> {`
  - Purpose: Indexed function `validate_collection_name_component` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:45-70]
- `collection_name_covers_all_scopes` (function) component `collection_name_covers_all_scopes [function]` (`02838fe0-8c43-5772-b63c-885d64cd7fa2`) lines 77-90 [crates/gcore/src/qdrant/naming.rs:77-90]
  - Signature: `fn collection_name_covers_all_scopes() {`
  - Purpose: Indexed function `collection_name_covers_all_scopes` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:77-90]
- `custom_collection_name_rejects_path_like_and_blank_names` (function) component `custom_collection_name_rejects_path_like_and_blank_names [function]` (`76dec9cd-2130-5608-8118-f71981da2842`) lines 93-110 [crates/gcore/src/qdrant/naming.rs:93-110]
  - Signature: `fn custom_collection_name_rejects_path_like_and_blank_names() {`
  - Purpose: Indexed function `custom_collection_name_rejects_path_like_and_blank_names` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:93-110]
- `scoped_collection_names_reject_invalid_components` (function) component `scoped_collection_names_reject_invalid_components [function]` (`4ce082ce-edc0-5bef-af16-a94cfb768f53`) lines 113-124 [crates/gcore/src/qdrant/naming.rs:113-124]
  - Signature: `fn scoped_collection_names_reject_invalid_components() {`
  - Purpose: Indexed function `scoped_collection_names_reject_invalid_components` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:113-124]

