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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/qdrant/naming.rs:3-10](crates/gcore/src/qdrant/naming.rs#L3-L10), [crates/gcore/src/qdrant/naming.rs:13-22](crates/gcore/src/qdrant/naming.rs#L13-L22), [crates/gcore/src/qdrant/naming.rs:25-43](crates/gcore/src/qdrant/naming.rs#L25-L43), [crates/gcore/src/qdrant/naming.rs:45-70](crates/gcore/src/qdrant/naming.rs#L45-L70), [crates/gcore/src/qdrant/naming.rs:77-90](crates/gcore/src/qdrant/naming.rs#L77-L90), [crates/gcore/src/qdrant/naming.rs:93-110](crates/gcore/src/qdrant/naming.rs#L93-L110), [crates/gcore/src/qdrant/naming.rs:113-124](crates/gcore/src/qdrant/naming.rs#L113-L124)

</details>

# crates/gcore/src/qdrant/naming.rs

Module: [[code/modules/crates/gcore/src/qdrant|crates/gcore/src/qdrant]]

## Purpose

Defines Qdrant collection naming rules. `CollectionScope` lets callers choose a project-scoped, topic-scoped, or custom collection name, `CollectionNameError` describes invalid-name cases, and `collection_name` builds the final name by validating each component before formatting scoped names or returning a custom name verbatim. The private validator rejects empty, whitespace-surrounded, reserved (`.`/`..`), and path-like or control-character-containing components, and the tests verify all scopes and invalid-name rejections.
[crates/gcore/src/qdrant/naming.rs:3-10]
[crates/gcore/src/qdrant/naming.rs:13-22]
[crates/gcore/src/qdrant/naming.rs:25-43]
[crates/gcore/src/qdrant/naming.rs:45-70]
[crates/gcore/src/qdrant/naming.rs:77-90]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CollectionScope` | type | `pub enum CollectionScope<'a> {` | `CollectionScope [type]` | `abbe32ae-0e46-50b7-b285-ac9fa5e9e8e6` | 3-10 [crates/gcore/src/qdrant/naming.rs:3-10] | Indexed type `CollectionScope` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:3-10] |
| `CollectionNameError` | type | `pub enum CollectionNameError {` | `CollectionNameError [type]` | `92855afa-85af-5755-85c0-f142ec859337` | 13-22 [crates/gcore/src/qdrant/naming.rs:13-22] | Indexed type `CollectionNameError` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:13-22] |
| `collection_name` | function | `pub fn collection_name(` | `collection_name [function]` | `704b9e85-52a6-5bb2-ac95-ce0749de0ef1` | 25-43 [crates/gcore/src/qdrant/naming.rs:25-43] | Indexed function `collection_name` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:25-43] |
| `validate_collection_name_component` | function | `fn validate_collection_name_component(name: &str) -> Result<(), CollectionNameError> {` | `validate_collection_name_component [function]` | `147cebfa-0217-5938-87b2-c119945fc554` | 45-70 [crates/gcore/src/qdrant/naming.rs:45-70] | Indexed function `validate_collection_name_component` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:45-70] |
| `collection_name_covers_all_scopes` | function | `fn collection_name_covers_all_scopes() {` | `collection_name_covers_all_scopes [function]` | `02838fe0-8c43-5772-b63c-885d64cd7fa2` | 77-90 [crates/gcore/src/qdrant/naming.rs:77-90] | Indexed function `collection_name_covers_all_scopes` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:77-90] |
| `custom_collection_name_rejects_path_like_and_blank_names` | function | `fn custom_collection_name_rejects_path_like_and_blank_names() {` | `custom_collection_name_rejects_path_like_and_blank_names [function]` | `76dec9cd-2130-5608-8118-f71981da2842` | 93-110 [crates/gcore/src/qdrant/naming.rs:93-110] | Indexed function `custom_collection_name_rejects_path_like_and_blank_names` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:93-110] |
| `scoped_collection_names_reject_invalid_components` | function | `fn scoped_collection_names_reject_invalid_components() {` | `scoped_collection_names_reject_invalid_components [function]` | `4ce082ce-edc0-5bef-af16-a94cfb768f53` | 113-124 [crates/gcore/src/qdrant/naming.rs:113-124] | Indexed function `scoped_collection_names_reject_invalid_components` in `crates/gcore/src/qdrant/naming.rs`. [crates/gcore/src/qdrant/naming.rs:113-124] |
