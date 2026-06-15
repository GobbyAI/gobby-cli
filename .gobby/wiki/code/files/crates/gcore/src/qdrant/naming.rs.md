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

This file defines Qdrant collection naming helpers: `CollectionScope` models whether a collection name is per-project, per-topic, or custom, and `CollectionNameError` describes why a name is invalid. `collection_name` turns a namespace plus scope into the final collection name, prefixing project/topic scopes with `{namespace}_project_{id}` or `{namespace}_topic_{name}` and leaving custom names unchanged after validation. `validate_collection_name_component` enforces the naming rules by rejecting empty, whitespace-surrounded, reserved dot-segment, control/whitespace, and path-like or delimiter-containing strings. The tests cover the expected formatting for each scope and the invalid-name cases for both custom and scoped components.
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
  - Purpose: Builds a validated collection name string from a namespace and 'CollectionScope', formatting project and topic scopes as '{namespace}_project_{id}' or '{namespace}_topic_{name}', and returning custom scope names unchanged. [crates/gcore/src/qdrant/naming.rs:25-43]
- `validate_collection_name_component` (function) component `validate_collection_name_component [function]` (`147cebfa-0217-5938-87b2-c119945fc554`) lines 45-70 [crates/gcore/src/qdrant/naming.rs:45-70]
  - Signature: `fn validate_collection_name_component(name: &str) -> Result<(), CollectionNameError> {`
  - Purpose: Validates that a collection name component is non-empty, has no leading or trailing whitespace, is not '.' or '..', and contains no ASCII control/whitespace characters or path-separator/colon characters, returning a specific 'CollectionNameError' on violation. [crates/gcore/src/qdrant/naming.rs:45-70]
- `collection_name_covers_all_scopes` (function) component `collection_name_covers_all_scopes [function]` (`02838fe0-8c43-5772-b63c-885d64cd7fa2`) lines 77-90 [crates/gcore/src/qdrant/naming.rs:77-90]
  - Signature: `fn collection_name_covers_all_scopes() {`
  - Purpose: Verifies that 'collection_name' formats project and topic scopes by prefixing the base name with '_<scope>_<id>' and preserves custom scoped names verbatim. [crates/gcore/src/qdrant/naming.rs:77-90]
- `custom_collection_name_rejects_path_like_and_blank_names` (function) component `custom_collection_name_rejects_path_like_and_blank_names [function]` (`76dec9cd-2130-5608-8118-f71981da2842`) lines 93-110 [crates/gcore/src/qdrant/naming.rs:93-110]
  - Signature: `fn custom_collection_name_rejects_path_like_and_blank_names() {`
  - Purpose: Verifies that 'collection_name("gcode", CollectionScope::Custom(...))' returns an error for blank, whitespace-only, dot-segment, path-like, delimiter-containing, and newline-containing custom collection names. [crates/gcore/src/qdrant/naming.rs:93-110]
- `scoped_collection_names_reject_invalid_components` (function) component `scoped_collection_names_reject_invalid_components [function]` (`4ce082ce-edc0-5bef-af16-a94cfb768f53`) lines 113-124 [crates/gcore/src/qdrant/naming.rs:113-124]
  - Signature: `fn scoped_collection_names_reject_invalid_components() {`
  - Purpose: Verifies that 'collection_name("gwiki", ...)' returns an error for project and topic scopes when given invalid component strings: empty, slash-containing, colon-containing, or space-containing values. [crates/gcore/src/qdrant/naming.rs:113-124]

