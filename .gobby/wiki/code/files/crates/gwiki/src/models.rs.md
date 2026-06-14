---
title: crates/gwiki/src/models.rs
type: code_file
provenance:
- file: crates/gwiki/src/models.rs
  ranges:
  - 12-15
  - 17-52
  - 55-61
  - 63-73
  - 76-80
  - 83-97
  - 99-150
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

This file defines the core wiki data models and naming helpers used by `gwiki`: `WikiScope` represents either a project or topic namespace and provides variant introspection plus derived vector collection names, `WikiSourceKind` normalizes source categories to stable strings, `WikiProvenance` records where a document came from, and `WikiDocumentRow` stores the denormalized database row for a wiki document. The supporting functions validate scope identifiers and map scopes to namespaced storage keys, while the tests verify that those derived names stay properly scoped and that document rows keep their cached scope fields internally consistent.
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
  - Purpose: 'WikiScope' is an enum-like type that represents either a project-scoped or topic-scoped wiki namespace and exposes helpers to report its kind, return its identity string, optionally extract the project ID or topic name, and derive the corresponding vector collection name with error handling. [crates/gwiki/src/models.rs:17-52]
- `WikiScope.kind` (method) component `WikiScope.kind [method]` (`81172c49-3041-5063-9d2e-328d3fd6bebb`) lines 18-23 [crates/gwiki/src/models.rs:18-23]
  - Signature: `pub fn kind(&self) -> &'static str {`
  - Purpose: Returns a static string slice identifying the enum variant, '"project"' for 'Self::Project' and '"topic"' for 'Self::Topic'. [crates/gwiki/src/models.rs:18-23]
- `WikiScope.identity` (method) component `WikiScope.identity [method]` (`33bfa353-2946-5117-97a2-c0714d5e2f74`) lines 25-30 [crates/gwiki/src/models.rs:25-30]
  - Signature: `pub fn identity(&self) -> &str {`
  - Purpose: Returns a '&str' view of the variant’s identifier, using 'project_id' for 'Project' and 'name' for 'Topic'. [crates/gwiki/src/models.rs:25-30]
- `WikiScope.project_id` (method) component `WikiScope.project_id [method]` (`8ebad210-3fc5-515c-8a98-775dbe53d65e`) lines 32-37 [crates/gwiki/src/models.rs:32-37]
  - Signature: `pub fn project_id(&self) -> Option<&str> {`
  - Purpose: Returns the inner 'project_id' string slice when 'self' is 'Self::Project', and 'None' when 'self' is 'Self::Topic'. [crates/gwiki/src/models.rs:32-37]
- `WikiScope.topic_name` (method) component `WikiScope.topic_name [method]` (`e762ad7e-c14e-5d6e-a3bb-327df48c58b6`) lines 39-44 [crates/gwiki/src/models.rs:39-44]
  - Signature: `pub fn topic_name(&self) -> Option<&str> {`
  - Purpose: Returns 'None' for 'Self::Project' and 'Some(&str)' containing the topic name for 'Self::Topic'. [crates/gwiki/src/models.rs:39-44]
- `WikiScope.vector_collection_name` (method) component `WikiScope.vector_collection_name [method]` (`b04d8576-0ee4-51e9-a00d-fb22d8bb7965`) lines 46-51 [crates/gwiki/src/models.rs:46-51]
  - Signature: `pub fn vector_collection_name(&self) -> Result<String, WikiError> {`
  - Purpose: Returns the vector collection name for the enum variant by delegating to 'project_collection_name(project_id)' for 'Project' and 'topic_collection_name(name)' for 'Topic', propagating any 'WikiError' from those helpers. [crates/gwiki/src/models.rs:46-51]
- `WikiSourceKind` (type) component `WikiSourceKind [type]` (`28a9fd5f-53cc-5bb9-9f33-ac9a855acd18`) lines 55-61 [crates/gwiki/src/models.rs:55-61]
  - Signature: `pub enum WikiSourceKind {`
  - Purpose: Indexed type `WikiSourceKind` in `crates/gwiki/src/models.rs`. [crates/gwiki/src/models.rs:55-61]
- `WikiSourceKind` (class) component `WikiSourceKind [class]` (`4af3c38a-49bc-53aa-8158-a6eb223ecc3b`) lines 63-73 [crates/gwiki/src/models.rs:63-73]
  - Signature: `impl WikiSourceKind {`
  - Purpose: 'WikiSourceKind' is an enum helper that maps each variant ('Raw', 'SourceNote', 'Concept', 'Topic', 'Inbox') to its corresponding stable string identifier via 'as_str()'. [crates/gwiki/src/models.rs:63-73]
- `WikiSourceKind.as_str` (method) component `WikiSourceKind.as_str [method]` (`696a59a7-4c67-58df-a9d7-5c68f2408540`) lines 64-72 [crates/gwiki/src/models.rs:64-72]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Returns the static string literal corresponding to 'self', mapping each variant to its lowercase identifier ('Raw' → '"raw"', 'SourceNote' → '"source_note"', 'Concept' → '"concept"', 'Topic' → '"topic"', 'Inbox' → '"inbox"'). [crates/gwiki/src/models.rs:64-72]
- `WikiProvenance` (class) component `WikiProvenance [class]` (`c0bf1e97-3a61-5560-ac10-c381d8c42182`) lines 76-80 [crates/gwiki/src/models.rs:76-80]
  - Signature: `pub struct WikiProvenance {`
  - Purpose: 'WikiProvenance' is a data-only provenance record that identifies the source wiki path, optionally records the origin it was captured from, and stores a content hash for integrity or change tracking. [crates/gwiki/src/models.rs:76-80]
- `WikiDocumentRow` (class) component `WikiDocumentRow [class]` (`8e4ef925-26d2-593f-935b-43c59da0c57e`) lines 83-97 [crates/gwiki/src/models.rs:83-97]
  - Signature: `pub struct WikiDocumentRow {`
  - Purpose: 'WikiDocumentRow' is a PostgreSQL-facing row model for a wiki document that stores canonical scope identifiers plus denormalized scope fields, document path, source kind, content hash, and JSON frontmatter/provenance metadata. [crates/gwiki/src/models.rs:83-97]
- `WikiDocumentRow` (class) component `WikiDocumentRow [class]` (`6ed795c1-e7b2-5739-82d9-e9bf5a8696da`) lines 99-150 [crates/gwiki/src/models.rs:99-150]
  - Signature: `impl WikiDocumentRow {`
  - Purpose: 'WikiDocumentRow' is a denormalized persistence model for a wiki document that stores scope metadata, path, source kind, content hash, frontmatter, and provenance, and can validate that the cached 'project_id'/'topic_name' fields are consistent with the encoded 'scope_kind' and 'scope_id'. [crates/gwiki/src/models.rs:99-150]
- `WikiDocumentRow.new` (method) component `WikiDocumentRow.new [method]` (`6bc9d9b6-cb79-5c7d-b37c-7947b0d35ff2`) lines 100-125 [crates/gwiki/src/models.rs:100-125]
  - Signature: `pub fn new(`
  - Purpose: Constructs a 'Self' by converting the provided 'id', 'path', and 'content_hash' into owned 'String's, deriving 'scope_kind', 'scope_id', 'project_id', and 'topic_name' from the supplied 'WikiScope', and storing the 'source_kind', 'frontmatter', and 'provenance' values unchanged. [crates/gwiki/src/models.rs:100-125]
- `WikiDocumentRow.validate_scope_consistency` (method) component `WikiDocumentRow.validate_scope_consistency [method]` (`1de96c6a-ea0e-51a7-8202-7da5224cfa3f`) lines 127-149 [crates/gwiki/src/models.rs:127-149]
  - Signature: `pub fn validate_scope_consistency(&self) -> Result<(), WikiError> {`
  - Purpose: Validates that the denormalized scope fields are internally consistent by accepting only 'project' rows where 'project_id == scope_id' and 'topic_name' is 'None', or 'topic' rows where 'topic_name == scope_id' and 'project_id' is 'None', otherwise returning 'WikiError::InvalidInput' for 'scope'. [crates/gwiki/src/models.rs:127-149]
- `validate_project_id` (function) component `validate_project_id [function]` (`0f5971e4-9439-58a0-9740-d7d3bb60c5e9`) lines 152-154 [crates/gwiki/src/models.rs:152-154]
  - Signature: `pub fn validate_project_id(project_id: &str) -> Result<String, WikiError> {`
  - Purpose: Returns the result of 'validate_scope_id("project id", project_id)', validating the supplied project ID and propagating any 'WikiError' while yielding a normalized 'String' on success. [crates/gwiki/src/models.rs:152-154]
- `validate_topic_name` (function) component `validate_topic_name [function]` (`6154e5d0-4352-50b8-bcd9-397ec838e66b`) lines 156-158 [crates/gwiki/src/models.rs:156-158]
  - Signature: `pub fn validate_topic_name(topic_name: &str) -> Result<String, WikiError> {`
  - Purpose: Validates a wiki topic name by delegating to 'validate_scope_id("topic name", topic_name)' and returning the resulting 'String' or a 'WikiError'. [crates/gwiki/src/models.rs:156-158]
- `project_collection_name` (function) component `project_collection_name [function]` (`2223a5b6-20e7-58ab-be07-803da478da38`) lines 160-166 [crates/gwiki/src/models.rs:160-166]
  - Signature: `pub fn project_collection_name(project_id: &str) -> Result<String, WikiError> {`
  - Purpose: Validates the given project ID and returns the infallible wiki collection name for that project by formatting '"gwiki"' with 'CollectionScope::Project(&project_id)'. [crates/gwiki/src/models.rs:160-166]
- `topic_collection_name` (function) component `topic_collection_name [function]` (`309b9ac5-9996-5e41-a732-3cfcbabc192e`) lines 168-174 [crates/gwiki/src/models.rs:168-174]
  - Signature: `pub fn topic_collection_name(topic_name: &str) -> Result<String, WikiError> {`
  - Purpose: Validates the topic name, then returns the 'gwiki' topic-scoped collection name as a 'String', panicking only if the infallible scope-to-name conversion unexpectedly fails. [crates/gwiki/src/models.rs:168-174]
- `validate_scope_id` (function) component `validate_scope_id [function]` (`bf19e351-2f53-5714-9a63-40edfa51dfa3`) lines 176-191 [crates/gwiki/src/models.rs:176-191]
  - Signature: `fn validate_scope_id(kind: &'static str, value: &str) -> Result<String, WikiError> {`
  - Purpose: Trims the input and returns an owned 'String' if the scope ID is non-empty and does not equal '.' or '..', contain ':', '/', '\', or any ASCII control character, otherwise returns 'WikiError::InvalidScope' with a formatted detail message. [crates/gwiki/src/models.rs:176-191]
- `derived_storage_names_are_namespaced` (function) component `derived_storage_names_are_namespaced [function]` (`658e3138-12ac-51f5-8c43-2941369c8c9c`) lines 198-236 [crates/gwiki/src/models.rs:198-236]
  - Signature: `fn derived_storage_names_are_namespaced() {`
  - Purpose: Verifies that wiki storage-derived names are correctly namespaced by scope, with fixed label constants and 'project'/'topic' collection names and 'WikiScope'-derived vector collection names matching the expected 'gwiki_project_*' and 'gwiki_topic_*' formats. [crates/gwiki/src/models.rs:198-236]
- `document_row_constructor_keeps_denormalized_scope_consistent` (function) component `document_row_constructor_keeps_denormalized_scope_consistent [function]` (`a017cb7c-a021-5c72-b316-b5d25758f612`) lines 239-260 [crates/gwiki/src/models.rs:239-260]
  - Signature: `fn document_row_constructor_keeps_denormalized_scope_consistent() {`
  - Purpose: Verifies that 'WikiDocumentRow::new' populates denormalized scope fields consistently for a project-scoped row and that 'validate_scope_consistency()' accepts the valid row but rejects a row with an inconsistent 'topic_name'. [crates/gwiki/src/models.rs:239-260]
- `scope_storage_names_reject_path_like_or_nested_ids` (function) component `scope_storage_names_reject_path_like_or_nested_ids [function]` (`5a429679-d7b5-5b00-8aaa-3111923ebc2d`) lines 263-284 [crates/gwiki/src/models.rs:263-284]
  - Signature: `fn scope_storage_names_reject_path_like_or_nested_ids() {`
  - Purpose: It verifies that both 'project_collection_name' and 'topic_collection_name' reject invalid storage names that are empty, whitespace-only, dot segments, or contain path-like, nested, or disallowed separator/control characters such as '/', '\', ':', newline, or NUL. [crates/gwiki/src/models.rs:263-284]
- `scope_storage_names_reject_ascii_controls_only` (function) component `scope_storage_names_reject_ascii_controls_only [function]` (`7ea1e11e-278b-5422-ba93-23448980a6ce`) lines 287-291 [crates/gwiki/src/models.rs:287-291]
  - Signature: `fn scope_storage_names_reject_ascii_controls_only() {`
  - Purpose: Verifies that project and topic collection-name validators reject embedded ASCII control characters ('U+001F' and 'U+007F') while allowing a non-ASCII control-like character ('U+0085'). [crates/gwiki/src/models.rs:287-291]

