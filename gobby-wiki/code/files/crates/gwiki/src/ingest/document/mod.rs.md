---
title: crates/gwiki/src/ingest/document/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/mod.rs
  ranges:
  - 21-27
  - 30-36
  - 39-45
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
  - 204-213
  - 216-218
  - 220-222
  - 224-229
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/document/mod.rs:21-27](crates/gwiki/src/ingest/document/mod.rs#L21-L27), [crates/gwiki/src/ingest/document/mod.rs:30-36](crates/gwiki/src/ingest/document/mod.rs#L30-L36), [crates/gwiki/src/ingest/document/mod.rs:39-45](crates/gwiki/src/ingest/document/mod.rs#L39-L45), [crates/gwiki/src/ingest/document/mod.rs:49-53](crates/gwiki/src/ingest/document/mod.rs#L49-L53), [crates/gwiki/src/ingest/document/mod.rs:56-62](crates/gwiki/src/ingest/document/mod.rs#L56-L62), [crates/gwiki/src/ingest/document/mod.rs:64-66](crates/gwiki/src/ingest/document/mod.rs#L64-L66), [crates/gwiki/src/ingest/document/mod.rs:68-72](crates/gwiki/src/ingest/document/mod.rs#L68-L72), [crates/gwiki/src/ingest/document/mod.rs:74](crates/gwiki/src/ingest/document/mod.rs#L74), [crates/gwiki/src/ingest/document/mod.rs:77-86](crates/gwiki/src/ingest/document/mod.rs#L77-L86), [crates/gwiki/src/ingest/document/mod.rs:88-100](crates/gwiki/src/ingest/document/mod.rs#L88-L100), [crates/gwiki/src/ingest/document/mod.rs:103-114](crates/gwiki/src/ingest/document/mod.rs#L103-L114), [crates/gwiki/src/ingest/document/mod.rs:116-191](crates/gwiki/src/ingest/document/mod.rs#L116-L191), [crates/gwiki/src/ingest/document/mod.rs:193-201](crates/gwiki/src/ingest/document/mod.rs#L193-L201), [crates/gwiki/src/ingest/document/mod.rs:204-213](crates/gwiki/src/ingest/document/mod.rs#L204-L213), [crates/gwiki/src/ingest/document/mod.rs:216-218](crates/gwiki/src/ingest/document/mod.rs#L216-L218), [crates/gwiki/src/ingest/document/mod.rs:220-222](crates/gwiki/src/ingest/document/mod.rs#L220-L222), [crates/gwiki/src/ingest/document/mod.rs:224-229](crates/gwiki/src/ingest/document/mod.rs#L224-L229)

</details>

# crates/gwiki/src/ingest/document/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This module implements document ingestion for gwiki, wiring together snapshot capture, format-specific extraction, asset/raw output, and optional post-ingest indexing. It defines the data passed through the pipeline (`DocumentSnapshot`, `DocumentRequest`, `DocumentExtraction`, `DocumentIngestResult`), the `DocumentExtractor`/`DocumentEndpoint` abstraction used to route extraction work, and a local extractor implementation. The public ingest functions handle the full flow with or without index updates, including endpoint-driven ingestion, cleanup on failure, extension and XML-entity handling, and error construction, while the `html`, `office`, and `render` submodules provide the actual format-specific extraction logic.
[crates/gwiki/src/ingest/document/mod.rs:21-27]
[crates/gwiki/src/ingest/document/mod.rs:30-36]
[crates/gwiki/src/ingest/document/mod.rs:39-45]
[crates/gwiki/src/ingest/document/mod.rs:49-53]
[crates/gwiki/src/ingest/document/mod.rs:56-62]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DocumentSnapshot` | class | `pub struct DocumentSnapshot {` | `DocumentSnapshot [class]` | `a2170ab3-1a1e-5c51-832b-406793e1bce7` | 21-27 [crates/gwiki/src/ingest/document/mod.rs:21-27] | Indexed class `DocumentSnapshot` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:21-27] |
| `DocumentIngestResult` | class | `pub struct DocumentIngestResult {` | `DocumentIngestResult [class]` | `c2f16281-469b-5302-a747-bc93bf64448f` | 30-36 [crates/gwiki/src/ingest/document/mod.rs:30-36] | Indexed class `DocumentIngestResult` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:30-36] |
| `IngestResult::from` | method | `fn from(result: DocumentIngestResult) -> Self {` | `IngestResult::from [method]` | `236a0122-e48b-568e-a972-a8f6e74f01d5` | 39-45 [crates/gwiki/src/ingest/document/mod.rs:39-45] | Indexed method `IngestResult::from` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:39-45] |
| `DocumentRequest` | class | `pub struct DocumentRequest<'a> {` | `DocumentRequest [class]` | `57b7429b-82c7-5e61-b514-0414c1939186` | 49-53 [crates/gwiki/src/ingest/document/mod.rs:49-53] | Indexed class `DocumentRequest` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:49-53] |
| `DocumentExtraction` | class | `pub struct DocumentExtraction {` | `DocumentExtraction [class]` | `155919ce-7fcf-5e47-a07c-36a4c3c0cd67` | 56-62 [crates/gwiki/src/ingest/document/mod.rs:56-62] | Indexed class `DocumentExtraction` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:56-62] |
| `DocumentExtractor` | type | `pub trait DocumentExtractor {` | `DocumentExtractor [type]` | `0504ad43-232f-5372-83f6-19f11aa1fd79` | 64-66 [crates/gwiki/src/ingest/document/mod.rs:64-66] | Indexed type `DocumentExtractor` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:64-66] |
| `DocumentEndpoint` | type | `pub enum DocumentEndpoint<'a> {` | `DocumentEndpoint [type]` | `b711a19f-ca46-5c02-92fd-d658bdc13ee9` | 68-72 [crates/gwiki/src/ingest/document/mod.rs:68-72] | Indexed type `DocumentEndpoint` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:68-72] |
| `LocalDocumentExtractor` | class | `struct LocalDocumentExtractor;` | `LocalDocumentExtractor [class]` | `00487aef-a03c-5717-9a3b-876c3f91922b` | 74-74 [crates/gwiki/src/ingest/document/mod.rs:74] | Indexed class `LocalDocumentExtractor` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:74] |
| `ingest_document` | function | `pub fn ingest_document(` | `ingest_document [function]` | `8395cafa-adba-570b-9a18-f0732ee176b7` | 77-86 [crates/gwiki/src/ingest/document/mod.rs:77-86] | Indexed function `ingest_document` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:77-86] |
| `ingest_document_without_index` | function | `pub(crate) fn ingest_document_without_index(` | `ingest_document_without_index [function]` | `31a4c0ea-3eb5-5480-b27e-96b19f488838` | 88-100 [crates/gwiki/src/ingest/document/mod.rs:88-100] | Indexed function `ingest_document_without_index` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:88-100] |
| `ingest_document_with_endpoint` | function | `pub fn ingest_document_with_endpoint(` | `ingest_document_with_endpoint [function]` | `433322d9-00c7-5134-9d5b-514d879a9fc9` | 103-114 [crates/gwiki/src/ingest/document/mod.rs:103-114] | Indexed function `ingest_document_with_endpoint` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:103-114] |
| `ingest_document_with_endpoint_without_index` | function | `pub(crate) fn ingest_document_with_endpoint_without_index(` | `ingest_document_with_endpoint_without_index [function]` | `a2b12b47-340d-51ff-9881-88a88e72371d` | 116-191 [crates/gwiki/src/ingest/document/mod.rs:116-191] | Indexed function `ingest_document_with_endpoint_without_index` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:116-191] |
| `remove_document_asset_after_failure` | function | `fn remove_document_asset_after_failure(vault_root: &Path, asset_path: &Path, context: &str) {` | `remove_document_asset_after_failure [function]` | `a5d4a792-398c-5fe8-aae5-b5d9f9286b18` | 193-201 [crates/gwiki/src/ingest/document/mod.rs:193-201] | Indexed function `remove_document_asset_after_failure` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:193-201] |
| `LocalDocumentExtractor::extract` | method | `fn extract(&self, request: &DocumentRequest<'_>) -> Result<DocumentExtraction, WikiError> {` | `LocalDocumentExtractor::extract [method]` | `3de3b955-3f02-5281-9dff-82378cff55f0` | 204-213 [crates/gwiki/src/ingest/document/mod.rs:204-213] | Indexed method `LocalDocumentExtractor::extract` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:204-213] |
| `extension` | function | `fn extension(file_name: &str) -> Option<String> {` | `extension [function]` | `cd44aaaa-0a4f-5c89-82a7-ad7d80c518b4` | 216-218 [crates/gwiki/src/ingest/document/mod.rs:216-218] | Indexed function `extension` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:216-218] |
| `decode_xml_entities` | function | `fn decode_xml_entities(text: &str) -> String {` | `decode_xml_entities [function]` | `beb66529-f429-5375-a6e6-f8e21382dd5f` | 220-222 [crates/gwiki/src/ingest/document/mod.rs:220-222] | Indexed function `decode_xml_entities` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:220-222] |
| `document_error` | function | `fn document_error(message: impl Into<String>) -> WikiError {` | `document_error [function]` | `a037af27-493a-5edd-9284-72919842ba8b` | 224-229 [crates/gwiki/src/ingest/document/mod.rs:224-229] | Indexed function `document_error` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:224-229] |
