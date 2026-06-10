---
title: crates/gwiki/src/ingest/document/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/mod.rs
  ranges:
  - 21-27
  - 30-36
  - 38-46
  - 39-45
  - 49-53
  - 56-62
  - 64-66
  - 68-71
  - '73'
  - 75-84
  - 86-98
  - 100-111
  - 113-188
  - 190-198
  - 200-211
  - 201-210
  - 213-215
  - 217-219
  - 221-226
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/document/mod.rs

Module: [[code/modules/crates/gwiki/src/ingest/document|crates/gwiki/src/ingest/document]]

## Purpose

`crates/gwiki/src/ingest/document/mod.rs` exposes 19 indexed API symbols.
[crates/gwiki/src/ingest/document/mod.rs:21-27]
[crates/gwiki/src/ingest/document/mod.rs:30-36]
[crates/gwiki/src/ingest/document/mod.rs:38-46]
[crates/gwiki/src/ingest/document/mod.rs:39-45]
[crates/gwiki/src/ingest/document/mod.rs:49-53]
[crates/gwiki/src/ingest/document/mod.rs:56-62]
[crates/gwiki/src/ingest/document/mod.rs:64-66]
[crates/gwiki/src/ingest/document/mod.rs:68-71]
[crates/gwiki/src/ingest/document/mod.rs:73]
[crates/gwiki/src/ingest/document/mod.rs:75-84]
[crates/gwiki/src/ingest/document/mod.rs:86-98]
[crates/gwiki/src/ingest/document/mod.rs:100-111]
[crates/gwiki/src/ingest/document/mod.rs:113-188]
[crates/gwiki/src/ingest/document/mod.rs:190-198]
[crates/gwiki/src/ingest/document/mod.rs:200-211]
[crates/gwiki/src/ingest/document/mod.rs:201-210]
[crates/gwiki/src/ingest/document/mod.rs:213-215]
[crates/gwiki/src/ingest/document/mod.rs:217-219]
[crates/gwiki/src/ingest/document/mod.rs:221-226]

## API Symbols

- `DocumentSnapshot` (class) component `DocumentSnapshot [class]` (`a2170ab3-1a1e-5c51-832b-406793e1bce7`) lines 21-27 [crates/gwiki/src/ingest/document/mod.rs:21-27]
  - Signature: `pub struct DocumentSnapshot {`
  - Purpose: DocumentSnapshot is a struct that encapsulates a document's binary payload alongside metadata fields for location, filename, acquisition timestamp, and source classification. [crates/gwiki/src/ingest/document/mod.rs:21-27]
- `DocumentIngestResult` (class) component `DocumentIngestResult [class]` (`c2f16281-469b-5302-a747-bc93bf64448f`) lines 30-36 [crates/gwiki/src/ingest/document/mod.rs:30-36]
  - Signature: `pub struct DocumentIngestResult {`
  - Purpose: `DocumentIngestResult` encapsulates the output of document ingestion, containing a `SourceRecord` and file paths to raw, asset, and derived document variants along with optional degradation metadata. [crates/gwiki/src/ingest/document/mod.rs:30-36]
- `IngestResult` (class) component `IngestResult [class]` (`8e08dbc3-2620-5c3e-bd4d-0ffd0efcb683`) lines 38-46 [crates/gwiki/src/ingest/document/mod.rs:38-46]
  - Signature: `impl From<DocumentIngestResult> for IngestResult {`
  - Purpose: This `From` trait implementation converts a `DocumentIngestResult` into an `IngestResult` by transferring the `record` and `raw_path` fields and wrapping `asset_path` in `Some()`. [crates/gwiki/src/ingest/document/mod.rs:38-46]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`236a0122-e48b-568e-a972-a8f6e74f01d5`) lines 39-45 [crates/gwiki/src/ingest/document/mod.rs:39-45]
  - Signature: `fn from(result: DocumentIngestResult) -> Self {`
  - Purpose: Implements the `From` trait to convert a `DocumentIngestResult` into `Self` by extracting its `record` and `raw_path` fields directly and wrapping the `asset_path` field in `Option::Some`. [crates/gwiki/src/ingest/document/mod.rs:39-45]
- `DocumentRequest` (class) component `DocumentRequest [class]` (`57b7429b-82c7-5e61-b514-0414c1939186`) lines 49-53 [crates/gwiki/src/ingest/document/mod.rs:49-53]
  - Signature: `pub struct DocumentRequest<'a> {`
  - Purpose: `DocumentRequest` is a struct holding borrowed references to a document's filename, source kind, and byte content, all constrained to the same lifetime `'a`. [crates/gwiki/src/ingest/document/mod.rs:49-53]
- `DocumentExtraction` (class) component `DocumentExtraction [class]` (`155919ce-7fcf-5e47-a07c-36a4c3c0cd67`) lines 56-62 [crates/gwiki/src/ingest/document/mod.rs:56-62]
  - Signature: `pub struct DocumentExtraction {`
  - Purpose: `DocumentExtraction` is a struct that encapsulates the results of document extraction, containing an optional title, markdown-formatted content, static unit metadata (label and count), and optional degradation information. [crates/gwiki/src/ingest/document/mod.rs:56-62]
- `DocumentExtractor` (type) component `DocumentExtractor [type]` (`0504ad43-232f-5372-83f6-19f11aa1fd79`) lines 64-66 [crates/gwiki/src/ingest/document/mod.rs:64-66]
  - Signature: `pub trait DocumentExtractor {`
  - Purpose: Indexed type `DocumentExtractor` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:64-66]
- `DocumentEndpoint` (type) component `DocumentEndpoint [type]` (`b711a19f-ca46-5c02-92fd-d658bdc13ee9`) lines 68-71 [crates/gwiki/src/ingest/document/mod.rs:68-71]
  - Signature: `pub enum DocumentEndpoint<'a> {`
  - Purpose: Indexed type `DocumentEndpoint` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:68-71]
- `LocalDocumentExtractor` (class) component `LocalDocumentExtractor [class]` (`c414698f-396e-56ce-8131-734d5073562f`) lines 73-73 [crates/gwiki/src/ingest/document/mod.rs:73]
  - Signature: `struct LocalDocumentExtractor;`
  - Purpose: `LocalDocumentExtractor` is a unit struct (zero-sized type) that likely serves as a namespace or type marker for local document extraction operations, though its implementation details are not visible in this signature alone. [crates/gwiki/src/ingest/document/mod.rs:73]
- `ingest_document` (function) component `ingest_document [function]` (`680ced59-a597-5600-a6f1-c76a535f8112`) lines 75-84 [crates/gwiki/src/ingest/document/mod.rs:75-84]
  - Signature: `pub fn ingest_document(`
  - Purpose: Ingests a document snapshot into a vault and updates the wiki index store to reflect the change. [crates/gwiki/src/ingest/document/mod.rs:75-84]
- `ingest_document_without_index` (function) component `ingest_document_without_index [function]` (`74d50e7a-417e-5351-a83e-672ad2956497`) lines 86-98 [crates/gwiki/src/ingest/document/mod.rs:86-98]
  - Signature: `pub(crate) fn ingest_document_without_index(`
  - Purpose: This function ingests a document snapshot into a vault without indexing by delegating to an internal function with a static local document extractor endpoint. [crates/gwiki/src/ingest/document/mod.rs:86-98]
- `ingest_document_with_endpoint` (function) component `ingest_document_with_endpoint [function]` (`3e2326a6-a30f-56cd-ac77-497defe48782`) lines 100-111 [crates/gwiki/src/ingest/document/mod.rs:100-111]
  - Signature: `pub fn ingest_document_with_endpoint(`
  - Purpose: Ingests a document snapshot into a vault through a specified endpoint and subsequently updates the wiki index store. [crates/gwiki/src/ingest/document/mod.rs:100-111]
- `ingest_document_with_endpoint_without_index` (function) component `ingest_document_with_endpoint_without_index [function]` (`1eb62e82-d791-5f21-a742-6aa5d6bce9cf`) lines 113-188 [crates/gwiki/src/ingest/document/mod.rs:113-188]
  - Signature: `pub(crate) fn ingest_document_with_endpoint_without_index(`
  - Purpose: Ingests a document by extracting content through a provided DocumentEndpoint (handling both available and unavailable cases), registering it in a vault manifest, and persisting the document assets and markdown without index maintenance. [crates/gwiki/src/ingest/document/mod.rs:113-188]
- `remove_document_asset_after_failure` (function) component `remove_document_asset_after_failure [function]` (`6f4cbd57-a915-5fed-a9fa-b99276f8d10b`) lines 190-198 [crates/gwiki/src/ingest/document/mod.rs:190-198]
  - Signature: `fn remove_document_asset_after_failure(vault_root: &Path, asset_path: &Path, context: &str) {`
  - Purpose: Removes a document asset file from the vault directory, logging a warning if the deletion fails. [crates/gwiki/src/ingest/document/mod.rs:190-198]
- `LocalDocumentExtractor` (class) component `LocalDocumentExtractor [class]` (`50c77fe6-826b-5bfd-a089-0395b771c899`) lines 200-211 [crates/gwiki/src/ingest/document/mod.rs:200-211]
  - Signature: `impl DocumentExtractor for LocalDocumentExtractor {`
  - Purpose: LocalDocumentExtractor implements the DocumentExtractor trait to dispatch document extraction requests to format-specific handlers (HTML or Office) based on the source document kind, returning an error for unsupported formats. [crates/gwiki/src/ingest/document/mod.rs:200-211]
- `LocalDocumentExtractor.extract` (method) component `LocalDocumentExtractor.extract [method]` (`28c79fc5-4d65-5581-aca8-e84794639b9b`) lines 201-210 [crates/gwiki/src/ingest/document/mod.rs:201-210]
  - Signature: `fn extract(&self, request: &DocumentRequest<'_>) -> Result<DocumentExtraction, WikiError> {`
  - Purpose: Dispatches document extraction to the appropriate handler (HTML or Office) based on the source kind, returning a DocumentExtraction or WikiError for unsupported document types. [crates/gwiki/src/ingest/document/mod.rs:201-210]
- `extension` (function) component `extension [function]` (`d57f24a6-a7d6-51ad-95c0-1e1573e96f73`) lines 213-215 [crates/gwiki/src/ingest/document/mod.rs:213-215]
  - Signature: `fn extension(file_name: &str) -> Option<String> {`
  - Purpose: This function extracts the file extension from a filename and returns it in lowercase form as `Option<String>`, delegating to `lowercase_extension()` for the actual implementation. [crates/gwiki/src/ingest/document/mod.rs:213-215]
- `decode_xml_entities` (function) component `decode_xml_entities [function]` (`f0f02b28-319c-5b90-8f45-f6305a2891e5`) lines 217-219 [crates/gwiki/src/ingest/document/mod.rs:217-219]
  - Signature: `fn decode_xml_entities(text: &str) -> String {`
  - Purpose: Decodes HTML/XML entity references in a string reference and returns an owned String. [crates/gwiki/src/ingest/document/mod.rs:217-219]
- `document_error` (function) component `document_error [function]` (`d6e87f6e-13e8-52a9-a6d9-ddca9e0f8772`) lines 221-226 [crates/gwiki/src/ingest/document/mod.rs:221-226]
  - Signature: `fn document_error(message: impl Into<String>) -> WikiError {`
  - Purpose: This function constructs and returns a `WikiError::InvalidInput` variant with the field identifier "document" and a provided message converted to a `String`. [crates/gwiki/src/ingest/document/mod.rs:221-226]

