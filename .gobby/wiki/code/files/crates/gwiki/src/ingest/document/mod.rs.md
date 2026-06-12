---
title: crates/gwiki/src/ingest/document/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/mod.rs
  ranges:
  - 21-27
  - 30-36
  - 38-46
  - 49-53
  - 56-62
  - 64-66
  - 68-72
  - '74'
  - 77-86
  - 88-100
  - 103-114
  - 116-191
  - 193-201
  - 203-214
  - 216-218
  - 220-222
  - 224-229
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

## API Symbols

- `DocumentSnapshot` (class) component `DocumentSnapshot [class]` (`a2170ab3-1a1e-5c51-832b-406793e1bce7`) lines 21-27 [crates/gwiki/src/ingest/document/mod.rs:21-27]
  - Signature: `pub struct DocumentSnapshot {`
  - Purpose: Indexed class `DocumentSnapshot` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:21-27]
- `DocumentIngestResult` (class) component `DocumentIngestResult [class]` (`c2f16281-469b-5302-a747-bc93bf64448f`) lines 30-36 [crates/gwiki/src/ingest/document/mod.rs:30-36]
  - Signature: `pub struct DocumentIngestResult {`
  - Purpose: Indexed class `DocumentIngestResult` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:30-36]
- `IngestResult` (class) component `IngestResult [class]` (`8e08dbc3-2620-5c3e-bd4d-0ffd0efcb683`) lines 38-46 [crates/gwiki/src/ingest/document/mod.rs:38-46]
  - Signature: `impl From<DocumentIngestResult> for IngestResult {`
  - Purpose: Indexed class `IngestResult` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:38-46]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`236a0122-e48b-568e-a972-a8f6e74f01d5`) lines 39-45 [crates/gwiki/src/ingest/document/mod.rs:39-45]
  - Signature: `fn from(result: DocumentIngestResult) -> Self {`
  - Purpose: Indexed method `IngestResult.from` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:39-45]
- `DocumentRequest` (class) component `DocumentRequest [class]` (`57b7429b-82c7-5e61-b514-0414c1939186`) lines 49-53 [crates/gwiki/src/ingest/document/mod.rs:49-53]
  - Signature: `pub struct DocumentRequest<'a> {`
  - Purpose: Indexed class `DocumentRequest` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:49-53]
- `DocumentExtraction` (class) component `DocumentExtraction [class]` (`155919ce-7fcf-5e47-a07c-36a4c3c0cd67`) lines 56-62 [crates/gwiki/src/ingest/document/mod.rs:56-62]
  - Signature: `pub struct DocumentExtraction {`
  - Purpose: Indexed class `DocumentExtraction` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:56-62]
- `DocumentExtractor` (type) component `DocumentExtractor [type]` (`0504ad43-232f-5372-83f6-19f11aa1fd79`) lines 64-66 [crates/gwiki/src/ingest/document/mod.rs:64-66]
  - Signature: `pub trait DocumentExtractor {`
  - Purpose: Indexed type `DocumentExtractor` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:64-66]
- `DocumentEndpoint` (type) component `DocumentEndpoint [type]` (`b711a19f-ca46-5c02-92fd-d658bdc13ee9`) lines 68-72 [crates/gwiki/src/ingest/document/mod.rs:68-72]
  - Signature: `pub enum DocumentEndpoint<'a> {`
  - Purpose: Indexed type `DocumentEndpoint` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:68-72]
- `LocalDocumentExtractor` (class) component `LocalDocumentExtractor [class]` (`00487aef-a03c-5717-9a3b-876c3f91922b`) lines 74-74 [crates/gwiki/src/ingest/document/mod.rs:74]
  - Signature: `struct LocalDocumentExtractor;`
  - Purpose: Indexed class `LocalDocumentExtractor` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:74]
- `ingest_document` (function) component `ingest_document [function]` (`8395cafa-adba-570b-9a18-f0732ee176b7`) lines 77-86 [crates/gwiki/src/ingest/document/mod.rs:77-86]
  - Signature: `pub fn ingest_document(`
  - Purpose: Indexed function `ingest_document` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:77-86]
- `ingest_document_without_index` (function) component `ingest_document_without_index [function]` (`31a4c0ea-3eb5-5480-b27e-96b19f488838`) lines 88-100 [crates/gwiki/src/ingest/document/mod.rs:88-100]
  - Signature: `pub(crate) fn ingest_document_without_index(`
  - Purpose: Indexed function `ingest_document_without_index` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:88-100]
- `ingest_document_with_endpoint` (function) component `ingest_document_with_endpoint [function]` (`433322d9-00c7-5134-9d5b-514d879a9fc9`) lines 103-114 [crates/gwiki/src/ingest/document/mod.rs:103-114]
  - Signature: `pub fn ingest_document_with_endpoint(`
  - Purpose: Indexed function `ingest_document_with_endpoint` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:103-114]
- `ingest_document_with_endpoint_without_index` (function) component `ingest_document_with_endpoint_without_index [function]` (`a2b12b47-340d-51ff-9881-88a88e72371d`) lines 116-191 [crates/gwiki/src/ingest/document/mod.rs:116-191]
  - Signature: `pub(crate) fn ingest_document_with_endpoint_without_index(`
  - Purpose: Indexed function `ingest_document_with_endpoint_without_index` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:116-191]
- `remove_document_asset_after_failure` (function) component `remove_document_asset_after_failure [function]` (`a5d4a792-398c-5fe8-aae5-b5d9f9286b18`) lines 193-201 [crates/gwiki/src/ingest/document/mod.rs:193-201]
  - Signature: `fn remove_document_asset_after_failure(vault_root: &Path, asset_path: &Path, context: &str) {`
  - Purpose: Indexed function `remove_document_asset_after_failure` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:193-201]
- `LocalDocumentExtractor` (class) component `LocalDocumentExtractor [class]` (`85439eaa-41ac-59b8-b33e-3f011823eead`) lines 203-214 [crates/gwiki/src/ingest/document/mod.rs:203-214]
  - Signature: `impl DocumentExtractor for LocalDocumentExtractor {`
  - Purpose: Indexed class `LocalDocumentExtractor` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:203-214]
- `LocalDocumentExtractor.extract` (method) component `LocalDocumentExtractor.extract [method]` (`3de3b955-3f02-5281-9dff-82378cff55f0`) lines 204-213 [crates/gwiki/src/ingest/document/mod.rs:204-213]
  - Signature: `fn extract(&self, request: &DocumentRequest<'_>) -> Result<DocumentExtraction, WikiError> {`
  - Purpose: Indexed method `LocalDocumentExtractor.extract` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:204-213]
- `extension` (function) component `extension [function]` (`cd44aaaa-0a4f-5c89-82a7-ad7d80c518b4`) lines 216-218 [crates/gwiki/src/ingest/document/mod.rs:216-218]
  - Signature: `fn extension(file_name: &str) -> Option<String> {`
  - Purpose: Indexed function `extension` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:216-218]
- `decode_xml_entities` (function) component `decode_xml_entities [function]` (`beb66529-f429-5375-a6e6-f8e21382dd5f`) lines 220-222 [crates/gwiki/src/ingest/document/mod.rs:220-222]
  - Signature: `fn decode_xml_entities(text: &str) -> String {`
  - Purpose: Indexed function `decode_xml_entities` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:220-222]
- `document_error` (function) component `document_error [function]` (`a037af27-493a-5edd-9284-72919842ba8b`) lines 224-229 [crates/gwiki/src/ingest/document/mod.rs:224-229]
  - Signature: `fn document_error(message: impl Into<String>) -> WikiError {`
  - Purpose: Indexed function `document_error` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:224-229]

