---
title: crates/gwiki/src/models.rs
type: code_file
provenance:
- file: crates/gwiki/src/models.rs
  ranges:
  - 12-15
  - 17-52
  - 18-23
  - 25-30
  - 32-37
  - 39-44
  - 46-51
  - 55-61
  - 63-73
  - 64-72
  - 76-80
  - 83-97
  - 99-150
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

# crates/gwiki/src/models.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/models.rs` exposes 24 indexed API symbols.
[crates/gwiki/src/models.rs:12-15]
[crates/gwiki/src/models.rs:17-52]
[crates/gwiki/src/models.rs:18-23]
[crates/gwiki/src/models.rs:25-30]
[crates/gwiki/src/models.rs:32-37]

## API Symbols

- `WikiScope` (type) component `WikiScope [type]` (`4792be91-7004-5369-ad18-d82f1b468ab7`) lines 12-15 [crates/gwiki/src/models.rs:12-15]
  - Signature: `pub enum WikiScope {`
  - Purpose: Indexed type `WikiScope` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:12-15]
- `WikiScope` (class) component `WikiScope [class]` (`40397d7b-7740-58e8-9f10-5a55753a588f`) lines 17-52 [crates/gwiki/src/models.rs:17-52]
  - Signature: `impl WikiScope {`
  - Purpose: Indexed class `WikiScope` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:17-52]
- `WikiScope.kind` (method) component `WikiScope.kind [method]` (`81172c49-3041-5063-9d2e-328d3fd6bebb`) lines 18-23 [crates/gwiki/src/models.rs:18-23]
  - Signature: `pub fn kind(&self) -> &'static str {`
  - Purpose: Indexed method `WikiScope.kind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:18-23]
- `WikiScope.identity` (method) component `WikiScope.identity [method]` (`33bfa353-2946-5117-97a2-c0714d5e2f74`) lines 25-30 [crates/gwiki/src/models.rs:25-30]
  - Signature: `pub fn identity(&self) -> &str {`
  - Purpose: Indexed method `WikiScope.identity` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:25-30]
- `WikiScope.project_id` (method) component `WikiScope.project_id [method]` (`8ebad210-3fc5-515c-8a98-775dbe53d65e`) lines 32-37 [crates/gwiki/src/models.rs:32-37]
  - Signature: `pub fn project_id(&self) -> Option<&str> {`
  - Purpose: Indexed method `WikiScope.project_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:32-37]
- `WikiScope.topic_name` (method) component `WikiScope.topic_name [method]` (`e762ad7e-c14e-5d6e-a3bb-327df48c58b6`) lines 39-44 [crates/gwiki/src/models.rs:39-44]
  - Signature: `pub fn topic_name(&self) -> Option<&str> {`
  - Purpose: Indexed method `WikiScope.topic_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:39-44]
- `WikiScope.vector_collection_name` (method) component `WikiScope.vector_collection_name [method]` (`b04d8576-0ee4-51e9-a00d-fb22d8bb7965`) lines 46-51 [crates/gwiki/src/models.rs:46-51]
  - Signature: `pub fn vector_collection_name(&self) -> Result<String, WikiError> {`
  - Purpose: Indexed method `WikiScope.vector_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:46-51]
- `WikiSourceKind` (type) component `WikiSourceKind [type]` (`28a9fd5f-53cc-5bb9-9f33-ac9a855acd18`) lines 55-61 [crates/gwiki/src/models.rs:55-61]
  - Signature: `pub enum WikiSourceKind {`
  - Purpose: Indexed type `WikiSourceKind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:55-61]
- `WikiSourceKind` (class) component `WikiSourceKind [class]` (`4af3c38a-49bc-53aa-8158-a6eb223ecc3b`) lines 63-73 [crates/gwiki/src/models.rs:63-73]
  - Signature: `impl WikiSourceKind {`
  - Purpose: Indexed class `WikiSourceKind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:63-73]
- `WikiSourceKind.as_str` (method) component `WikiSourceKind.as_str [method]` (`696a59a7-4c67-58df-a9d7-5c68f2408540`) lines 64-72 [crates/gwiki/src/models.rs:64-72]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Indexed method `WikiSourceKind.as_str` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:64-72]
- `WikiProvenance` (class) component `WikiProvenance [class]` (`c0bf1e97-3a61-5560-ac10-c381d8c42182`) lines 76-80 [crates/gwiki/src/models.rs:76-80]
  - Signature: `pub struct WikiProvenance {`
  - Purpose: Indexed class `WikiProvenance` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:76-80]
- `WikiDocumentRow` (class) component `WikiDocumentRow [class]` (`8e4ef925-26d2-593f-935b-43c59da0c57e`) lines 83-97 [crates/gwiki/src/models.rs:83-97]
  - Signature: `pub struct WikiDocumentRow {`
  - Purpose: Indexed class `WikiDocumentRow` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:83-97]
- `WikiDocumentRow` (class) component `WikiDocumentRow [class]` (`6ed795c1-e7b2-5739-82d9-e9bf5a8696da`) lines 99-150 [crates/gwiki/src/models.rs:99-150]
  - Signature: `impl WikiDocumentRow {`
  - Purpose: Indexed class `WikiDocumentRow` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:99-150]
- `WikiDocumentRow.new` (method) component `WikiDocumentRow.new [method]` (`6bc9d9b6-cb79-5c7d-b37c-7947b0d35ff2`) lines 100-125 [crates/gwiki/src/models.rs:100-125]
  - Signature: `pub fn new(`
  - Purpose: Indexed method `WikiDocumentRow.new` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:100-125]
- `WikiDocumentRow.validate_scope_consistency` (method) component `WikiDocumentRow.validate_scope_consistency [method]` (`1de96c6a-ea0e-51a7-8202-7da5224cfa3f`) lines 127-149 [crates/gwiki/src/models.rs:127-149]
  - Signature: `pub fn validate_scope_consistency(&self) -> Result<(), WikiError> {`
  - Purpose: Indexed method `WikiDocumentRow.validate_scope_consistency` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:127-149]
- `validate_project_id` (function) component `validate_project_id [function]` (`0f5971e4-9439-58a0-9740-d7d3bb60c5e9`) lines 152-154 [crates/gwiki/src/models.rs:152-154]
  - Signature: `pub fn validate_project_id(project_id: &str) -> Result<String, WikiError> {`
  - Purpose: Indexed function `validate_project_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:152-154]
- `validate_topic_name` (function) component `validate_topic_name [function]` (`6154e5d0-4352-50b8-bcd9-397ec838e66b`) lines 156-158 [crates/gwiki/src/models.rs:156-158]
  - Signature: `pub fn validate_topic_name(topic_name: &str) -> Result<String, WikiError> {`
  - Purpose: Indexed function `validate_topic_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:156-158]
- `project_collection_name` (function) component `project_collection_name [function]` (`2223a5b6-20e7-58ab-be07-803da478da38`) lines 160-166 [crates/gwiki/src/models.rs:160-166]
  - Signature: `pub fn project_collection_name(project_id: &str) -> Result<String, WikiError> {`
  - Purpose: Indexed function `project_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:160-166]
- `topic_collection_name` (function) component `topic_collection_name [function]` (`309b9ac5-9996-5e41-a732-3cfcbabc192e`) lines 168-174 [crates/gwiki/src/models.rs:168-174]
  - Signature: `pub fn topic_collection_name(topic_name: &str) -> Result<String, WikiError> {`
  - Purpose: Indexed function `topic_collection_name` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:168-174]
- `validate_scope_id` (function) component `validate_scope_id [function]` (`bf19e351-2f53-5714-9a63-40edfa51dfa3`) lines 176-191 [crates/gwiki/src/models.rs:176-191]
  - Signature: `fn validate_scope_id(kind: &'static str, value: &str) -> Result<String, WikiError> {`
  - Purpose: Indexed function `validate_scope_id` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:176-191]
- `derived_storage_names_are_namespaced` (function) component `derived_storage_names_are_namespaced [function]` (`658e3138-12ac-51f5-8c43-2941369c8c9c`) lines 198-236 [crates/gwiki/src/models.rs:198-236]
  - Signature: `fn derived_storage_names_are_namespaced() {`
  - Purpose: Indexed function `derived_storage_names_are_namespaced` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:198-236]
- `document_row_constructor_keeps_denormalized_scope_consistent` (function) component `document_row_constructor_keeps_denormalized_scope_consistent [function]` (`a017cb7c-a021-5c72-b316-b5d25758f612`) lines 239-260 [crates/gwiki/src/models.rs:239-260]
  - Signature: `fn document_row_constructor_keeps_denormalized_scope_consistent() {`
  - Purpose: Indexed function `document_row_constructor_keeps_denormalized_scope_consistent` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:239-260]
- `scope_storage_names_reject_path_like_or_nested_ids` (function) component `scope_storage_names_reject_path_like_or_nested_ids [function]` (`5a429679-d7b5-5b00-8aaa-3111923ebc2d`) lines 263-284 [crates/gwiki/src/models.rs:263-284]
  - Signature: `fn scope_storage_names_reject_path_like_or_nested_ids() {`
  - Purpose: Indexed function `scope_storage_names_reject_path_like_or_nested_ids` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:263-284]
- `scope_storage_names_reject_ascii_controls_only` (function) component `scope_storage_names_reject_ascii_controls_only [function]` (`7ea1e11e-278b-5422-ba93-23448980a6ce`) lines 287-291 [crates/gwiki/src/models.rs:287-291]
  - Signature: `fn scope_storage_names_reject_ascii_controls_only() {`
  - Purpose: Indexed function `scope_storage_names_reject_ascii_controls_only` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:287-291]

