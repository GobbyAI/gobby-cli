---
title: crates/gwiki/src/models.rs
type: code_file
provenance:
- file: crates/gwiki/src/models.rs
  ranges:
  - 12-15
  - 18-23
  - 25-30
  - 32-37
  - 39-44
  - 46-51
  - 55-61
  - 64-72
  - 76-80
  - 83-97
  - 100-125
  - 127-149
  - 152-154
  - 156-158
  - 160-166
  - 168-174
  - 176-191
  - 198-236
  - 239-260
  - 263-284
  - 287-291
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/models.rs:12-15](crates/gwiki/src/models.rs#L12-L15), [crates/gwiki/src/models.rs:18-23](crates/gwiki/src/models.rs#L18-L23), [crates/gwiki/src/models.rs:25-30](crates/gwiki/src/models.rs#L25-L30), [crates/gwiki/src/models.rs:32-37](crates/gwiki/src/models.rs#L32-L37), [crates/gwiki/src/models.rs:39-44](crates/gwiki/src/models.rs#L39-L44), [crates/gwiki/src/models.rs:46-51](crates/gwiki/src/models.rs#L46-L51), [crates/gwiki/src/models.rs:55-61](crates/gwiki/src/models.rs#L55-L61), [crates/gwiki/src/models.rs:64-72](crates/gwiki/src/models.rs#L64-L72), [crates/gwiki/src/models.rs:76-80](crates/gwiki/src/models.rs#L76-L80), [crates/gwiki/src/models.rs:83-97](crates/gwiki/src/models.rs#L83-L97), [crates/gwiki/src/models.rs:100-125](crates/gwiki/src/models.rs#L100-L125), [crates/gwiki/src/models.rs:127-149](crates/gwiki/src/models.rs#L127-L149), [crates/gwiki/src/models.rs:152-154](crates/gwiki/src/models.rs#L152-L154), [crates/gwiki/src/models.rs:156-158](crates/gwiki/src/models.rs#L156-L158), [crates/gwiki/src/models.rs:160-166](crates/gwiki/src/models.rs#L160-L166), [crates/gwiki/src/models.rs:168-174](crates/gwiki/src/models.rs#L168-L174), [crates/gwiki/src/models.rs:176-191](crates/gwiki/src/models.rs#L176-L191), [crates/gwiki/src/models.rs:198-236](crates/gwiki/src/models.rs#L198-L236), [crates/gwiki/src/models.rs:239-260](crates/gwiki/src/models.rs#L239-L260), [crates/gwiki/src/models.rs:263-284](crates/gwiki/src/models.rs#L263-L284), [crates/gwiki/src/models.rs:287-291](crates/gwiki/src/models.rs#L287-L291)

</details>

# crates/gwiki/src/models.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the core wiki data models and their naming/validation helpers. `WikiScope` represents either a project or topic scope and exposes accessors plus a method to derive the backing vector collection name; `WikiSourceKind` normalizes source categories to stable string labels; `WikiProvenance` stores source path, capture origin, and content hash metadata; and `WikiDocumentRow` packages a wiki document with denormalized scope columns for PostgreSQL filtering and a constructor/consistency check to keep the stored scope fields aligned. The free functions support scope and identifier validation, generate namespaced storage/collection names, and the tests verify those derived names are scoped correctly and reject invalid path-like or control-only IDs.
[crates/gwiki/src/models.rs:12-15]
[crates/gwiki/src/models.rs:18-23]
[crates/gwiki/src/models.rs:25-30]
[crates/gwiki/src/models.rs:32-37]
[crates/gwiki/src/models.rs:39-44]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WikiScope` | type | `pub enum WikiScope {` | `WikiScope [type]` | `4792be91-7004-5369-ad18-d82f1b468ab7` | 12-15 [crates/gwiki/src/models.rs:12-15] | Indexed type `WikiScope` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:12-15] |
| `WikiScope::kind` | method | `pub fn kind(&self) -> &'static str {` | `WikiScope::kind [method]` | `81172c49-3041-5063-9d2e-328d3fd6bebb` | 18-23 [crates/gwiki/src/models.rs:18-23] | Indexed method `WikiScope::kind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:18-23] |
| `WikiScope::identity` | method | `pub fn identity(&self) -> &str {` | `WikiScope::identity [method]` | `33bfa353-2946-5117-97a2-c0714d5e2f74` | 25-30 [crates/gwiki/src/models.rs:25-30] | Indexed method `WikiScope::identity` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:25-30] |
| `WikiScope::project_id` | method | `pub fn project_id(&self) -> Option<&str> {` | `WikiScope::project_id [method]` | `8ebad210-3fc5-515c-8a98-775dbe53d65e` | 32-37 [crates/gwiki/src/models.rs:32-37] | Indexed method `WikiScope::project_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:32-37] |
| `WikiScope::topic_name` | method | `pub fn topic_name(&self) -> Option<&str> {` | `WikiScope::topic_name [method]` | `e762ad7e-c14e-5d6e-a3bb-327df48c58b6` | 39-44 [crates/gwiki/src/models.rs:39-44] | Indexed method `WikiScope::topic_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:39-44] |
| `WikiScope::vector_collection_name` | method | `pub fn vector_collection_name(&self) -> Result<String, WikiError> {` | `WikiScope::vector_collection_name [method]` | `b04d8576-0ee4-51e9-a00d-fb22d8bb7965` | 46-51 [crates/gwiki/src/models.rs:46-51] | Indexed method `WikiScope::vector_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:46-51] |
| `WikiSourceKind` | type | `pub enum WikiSourceKind {` | `WikiSourceKind [type]` | `28a9fd5f-53cc-5bb9-9f33-ac9a855acd18` | 55-61 [crates/gwiki/src/models.rs:55-61] | Indexed type `WikiSourceKind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:55-61] |
| `WikiSourceKind::as_str` | method | `pub fn as_str(self) -> &'static str {` | `WikiSourceKind::as_str [method]` | `696a59a7-4c67-58df-a9d7-5c68f2408540` | 64-72 [crates/gwiki/src/models.rs:64-72] | Indexed method `WikiSourceKind::as_str` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:64-72] |
| `WikiProvenance` | class | `pub struct WikiProvenance {` | `WikiProvenance [class]` | `c0bf1e97-3a61-5560-ac10-c381d8c42182` | 76-80 [crates/gwiki/src/models.rs:76-80] | Indexed class `WikiProvenance` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:76-80] |
| `WikiDocumentRow` | class | `pub struct WikiDocumentRow {` | `WikiDocumentRow [class]` | `8e4ef925-26d2-593f-935b-43c59da0c57e` | 83-97 [crates/gwiki/src/models.rs:83-97] | Indexed class `WikiDocumentRow` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:83-97] |
| `WikiDocumentRow::new` | method | `pub fn new(` | `WikiDocumentRow::new [method]` | `6bc9d9b6-cb79-5c7d-b37c-7947b0d35ff2` | 100-125 [crates/gwiki/src/models.rs:100-125] | Indexed method `WikiDocumentRow::new` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:100-125] |
| `WikiDocumentRow::validate_scope_consistency` | method | `pub fn validate_scope_consistency(&self) -> Result<(), WikiError> {` | `WikiDocumentRow::validate_scope_consistency [method]` | `1de96c6a-ea0e-51a7-8202-7da5224cfa3f` | 127-149 [crates/gwiki/src/models.rs:127-149] | Indexed method `WikiDocumentRow::validate_scope_consistency` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:127-149] |
| `validate_project_id` | function | `pub fn validate_project_id(project_id: &str) -> Result<String, WikiError> {` | `validate_project_id [function]` | `0f5971e4-9439-58a0-9740-d7d3bb60c5e9` | 152-154 [crates/gwiki/src/models.rs:152-154] | Indexed function `validate_project_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:152-154] |
| `validate_topic_name` | function | `pub fn validate_topic_name(topic_name: &str) -> Result<String, WikiError> {` | `validate_topic_name [function]` | `6154e5d0-4352-50b8-bcd9-397ec838e66b` | 156-158 [crates/gwiki/src/models.rs:156-158] | Indexed function `validate_topic_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:156-158] |
| `project_collection_name` | function | `pub fn project_collection_name(project_id: &str) -> Result<String, WikiError> {` | `project_collection_name [function]` | `2223a5b6-20e7-58ab-be07-803da478da38` | 160-166 [crates/gwiki/src/models.rs:160-166] | Indexed function `project_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:160-166] |
| `topic_collection_name` | function | `pub fn topic_collection_name(topic_name: &str) -> Result<String, WikiError> {` | `topic_collection_name [function]` | `309b9ac5-9996-5e41-a732-3cfcbabc192e` | 168-174 [crates/gwiki/src/models.rs:168-174] | Indexed function `topic_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:168-174] |
| `validate_scope_id` | function | `fn validate_scope_id(kind: &'static str, value: &str) -> Result<String, WikiError> {` | `validate_scope_id [function]` | `bf19e351-2f53-5714-9a63-40edfa51dfa3` | 176-191 [crates/gwiki/src/models.rs:176-191] | Indexed function `validate_scope_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:176-191] |
| `derived_storage_names_are_namespaced` | function | `fn derived_storage_names_are_namespaced() {` | `derived_storage_names_are_namespaced [function]` | `658e3138-12ac-51f5-8c43-2941369c8c9c` | 198-236 [crates/gwiki/src/models.rs:198-236] | Indexed function `derived_storage_names_are_namespaced` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:198-236] |
| `document_row_constructor_keeps_denormalized_scope_consistent` | function | `fn document_row_constructor_keeps_denormalized_scope_consistent() {` | `document_row_constructor_keeps_denormalized_scope_consistent [function]` | `a017cb7c-a021-5c72-b316-b5d25758f612` | 239-260 [crates/gwiki/src/models.rs:239-260] | Indexed function `document_row_constructor_keeps_denormalized_scope_consistent` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:239-260] |
| `scope_storage_names_reject_path_like_or_nested_ids` | function | `fn scope_storage_names_reject_path_like_or_nested_ids() {` | `scope_storage_names_reject_path_like_or_nested_ids [function]` | `5a429679-d7b5-5b00-8aaa-3111923ebc2d` | 263-284 [crates/gwiki/src/models.rs:263-284] | Indexed function `scope_storage_names_reject_path_like_or_nested_ids` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:263-284] |
| `scope_storage_names_reject_ascii_controls_only` | function | `fn scope_storage_names_reject_ascii_controls_only() {` | `scope_storage_names_reject_ascii_controls_only [function]` | `7ea1e11e-278b-5422-ba93-23448980a6ce` | 287-291 [crates/gwiki/src/models.rs:287-291] | Indexed function `scope_storage_names_reject_ascii_controls_only` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:287-291] |
