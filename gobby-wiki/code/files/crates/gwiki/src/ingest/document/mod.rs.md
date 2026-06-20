---
title: crates/gwiki/src/ingest/document/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/document/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/document/mod.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/document/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DocumentSnapshot` | class | The 'DocumentSnapshot' struct represents a captured snapshot of a retrieved document, storing its location, file name, fetch timestamp, raw byte payload, and source kind. [crates/gwiki/src/ingest/document/mod.rs:21-27] |
| `DocumentIngestResult` | class | The 'DocumentIngestResult' structure represents the outcome of a document ingestion process, encapsulating its source record, file paths for the raw, asset, and derived artifacts, and an optional document degradation assessment. [crates/gwiki/src/ingest/document/mod.rs:30-36] |
| `IngestResult::from` | method | This 'from' implementation converts a 'DocumentIngestResult' into an instance of 'Self' by directly mapping the 'record' and 'raw_path' fields and wrapping the 'asset_path' field in 'Some'. [crates/gwiki/src/ingest/document/mod.rs:39-45] |
| `DocumentRequest` | class | The 'DocumentRequest' struct is a lifetime-bound container that holds borrowed references to a document's file name, its source kind, and its raw byte contents. [crates/gwiki/src/ingest/document/mod.rs:49-53] |
| `DocumentExtraction` | class | 'DocumentExtraction' is a Rust struct that encapsulates the results of a document extraction process, containing an optional title, the extracted markdown text, unit metrics consisting of a static label and count, and optional details regarding document degradation. [crates/gwiki/src/ingest/document/mod.rs:56-62] |
| `DocumentExtractor` | type | Indexed type `DocumentExtractor` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:64-66] |
| `DocumentEndpoint` | type | Indexed type `DocumentEndpoint` in `crates/gwiki/src/ingest/document/mod.rs`. [crates/gwiki/src/ingest/document/mod.rs:68-72] |
| `LocalDocumentExtractor` | class | The 'LocalDocumentExtractor' struct is designed to parse and extract structured content or metadata from locally stored document files. [crates/gwiki/src/ingest/document/mod.rs:74] |
| `ingest_document` | function | The 'ingest_document' function ingests a document snapshot under a specific scope into the vault root, indexes the vault root using the provided index store, and returns a 'DocumentIngestResult' or a 'WikiError'. [crates/gwiki/src/ingest/document/mod.rs:77-86] |
| `ingest_document_without_index` | function | This function ingests a document without updating the index by delegating the process to 'ingest_document_with_endpoint_without_index' with a static local extractor endpoint. [crates/gwiki/src/ingest/document/mod.rs:88-100] |
| `ingest_document_with_endpoint` | function | The 'ingest_document_with_endpoint' function ingests a document snapshot using a specified endpoint under a vault root and scope identity, updates the provided wiki index store with the changes, and returns the ingestion result. [crates/gwiki/src/ingest/document/mod.rs:103-114] |
| `ingest_document_with_endpoint_without_index` | function | This function ingests a document snapshot by extracting its content via a document endpoint, registering the document draft in a source manifest, writing the raw asset, and generating and writing its rendered raw markdown file to the vault without performing indexing. [crates/gwiki/src/ingest/document/mod.rs:116-191] |
| `remove_document_asset_after_failure` | function | The 'remove_document_asset_after_failure' function attempts to delete a document asset at the path formed by joining 'vault_root' and 'asset_path' and logs a warning with the specified 'context' if the file removal operation fails. [crates/gwiki/src/ingest/document/mod.rs:193-201] |
| `LocalDocumentExtractor::extract` | method | The 'extract' method pattern-matches on the 'DocumentRequest''s kind to delegate extraction to either 'extract_html_document' or 'extract_office_document' based on whether it is HTML or an Office document, returning a 'DocumentExtraction' or a 'WikiError' for unsupported formats. [crates/gwiki/src/ingest/document/mod.rs:204-213] |
| `extension` | function | The 'extension' function retrieves the lowercase file extension of a given file name by delegating to the 'lowercase_extension' function and returning the result as an 'Option<String>'. [crates/gwiki/src/ingest/document/mod.rs:216-218] |
| `decode_xml_entities` | function | The 'decode_xml_entities' function decodes HTML and XML entities within a given string slice using the 'html_escape' library and returns the decoded text as an owned 'String'. [crates/gwiki/src/ingest/document/mod.rs:220-222] |
| `document_error` | function | The 'document_error' function constructs and returns a 'WikiError::InvalidInput' error variant, setting the 'field' to '"document"' and converting the provided 'message' argument into a 'String'. [crates/gwiki/src/ingest/document/mod.rs:224-229] |

