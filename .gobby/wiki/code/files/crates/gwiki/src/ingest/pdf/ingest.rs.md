---
title: crates/gwiki/src/ingest/pdf/ingest.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/ingest.rs
  ranges:
  - 22-36
  - 39-50
  - 53-106
  - 108-125
  - 127-142
  - 144-215
  - 217-241
  - 243-250
  - 252-258
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/ingest.rs

Module: [[code/modules/crates/gwiki/src/ingest/pdf|crates/gwiki/src/ingest/pdf]]

## Purpose

`crates/gwiki/src/ingest/pdf/ingest.rs` exposes 9 indexed API symbols.
[crates/gwiki/src/ingest/pdf/ingest.rs:22-36]
[crates/gwiki/src/ingest/pdf/ingest.rs:39-50]
[crates/gwiki/src/ingest/pdf/ingest.rs:53-106]
[crates/gwiki/src/ingest/pdf/ingest.rs:108-125]
[crates/gwiki/src/ingest/pdf/ingest.rs:127-142]

## API Symbols

- `ingest_pages` (function) component `ingest_pages [function]` (`6bb75d7e-5346-5605-a548-efd3bec8d0bd`) lines 22-36 [crates/gwiki/src/ingest/pdf/ingest.rs:22-36]
  - Signature: `pub fn ingest_pages(`
  - Purpose: Ingests a PDF snapshot into a wiki index store with vision endpoint capabilities disabled. [crates/gwiki/src/ingest/pdf/ingest.rs:22-36]
- `ingest_pdf_file` (function) component `ingest_pdf_file [function]` (`0dbff40e-79dc-55af-9a8e-081c6e0b6a90`) lines 39-50 [crates/gwiki/src/ingest/pdf/ingest.rs:39-50]
  - Signature: `pub fn ingest_pdf_file(`
  - Purpose: Ingests a PDF file snapshot into a wiki vault using a vision endpoint, then reindexes the wiki index store. [crates/gwiki/src/ingest/pdf/ingest.rs:39-50]
- `ingest_pdf_file_without_index` (function) component `ingest_pdf_file_without_index [function]` (`c31a124b-c8b0-5a38-975e-858dfc948d68`) lines 53-106 [crates/gwiki/src/ingest/pdf/ingest.rs:53-106]
  - Signature: `pub(crate) fn ingest_pdf_file_without_index(`
  - Purpose: Extracts text-layer pages and optionally renders pages from a PDF snapshot, accumulates processing degradation metadata, then delegates to the vision-enabled inner ingestion handler. [crates/gwiki/src/ingest/pdf/ingest.rs:53-106]
- `ingest_pages_with_vision` (function) component `ingest_pages_with_vision [function]` (`e8e8727c-9ab9-5144-8b44-d4059af7d331`) lines 108-125 [crates/gwiki/src/ingest/pdf/ingest.rs:108-125]
  - Signature: `pub fn ingest_pages_with_vision(`
  - Purpose: # Summary

Ingests rendered PDF pages using a vision endpoint and reindexes the wiki store afterward. [crates/gwiki/src/ingest/pdf/ingest.rs:108-125]
- `ingest_pages_with_vision_without_index` (function) component `ingest_pages_with_vision_without_index [function]` (`48de14c2-fe03-5a2e-a1dd-a09d67251539`) lines 127-142 [crates/gwiki/src/ingest/pdf/ingest.rs:127-142]
  - Signature: `pub(crate) fn ingest_pages_with_vision_without_index(`
  - Purpose: Ingests rendered PDF pages using vision processing without an index by delegating to the inner implementation with an empty index vector. [crates/gwiki/src/ingest/pdf/ingest.rs:127-142]
- `ingest_pages_with_vision_inner` (function) component `ingest_pages_with_vision_inner [function]` (`1a1ab6c5-a69f-55be-86a4-40c2dc9b90e4`) lines 144-215 [crates/gwiki/src/ingest/pdf/ingest.rs:144-215]
  - Signature: `fn ingest_pages_with_vision_inner(`
  - Purpose: Ingests a PDF source into a vault by registering it in a manifest, merging extracted text with vision-API-rendered pages, and converting the result to markdown output. [crates/gwiki/src/ingest/pdf/ingest.rs:144-215]
- `rollback_registered_pdf_source` (function) component `rollback_registered_pdf_source [function]` (`aa49042f-d020-5f88-8653-d05920be2e66`) lines 217-241 [crates/gwiki/src/ingest/pdf/ingest.rs:217-241]
  - Signature: `fn rollback_registered_pdf_source<T>(`
  - Purpose: Rolls back a failed PDF source registration by restoring the previous manifest state and cleaning up associated assets, returning the original error with any rollback failures appended. [crates/gwiki/src/ingest/pdf/ingest.rs:217-241]
- `cleanup_pdf_file` (function) component `cleanup_pdf_file [function]` (`00f73c8d-095a-5e9f-9c63-6f2c28aad24b`) lines 243-250 [crates/gwiki/src/ingest/pdf/ingest.rs:243-250]
  - Signature: `fn cleanup_pdf_file(vault_root: &Path, relative_path: &Path, cleanup_errors: &mut Vec<String>) {`
  - Purpose: Attempts to delete a file at the joined vault path, silently ignoring NotFound errors while appending any other deletion failures to the provided error vector. [crates/gwiki/src/ingest/pdf/ingest.rs:243-250]
- `pdf_cleanup_detail` (function) component `pdf_cleanup_detail [function]` (`ca8ef461-604f-5305-a423-ef35e605d583`) lines 252-258 [crates/gwiki/src/ingest/pdf/ingest.rs:252-258]
  - Signature: `fn pdf_cleanup_detail(cleanup_errors: &[String]) -> String {`
  - Purpose: Returns a formatted string containing semicolon-separated cleanup errors prefixed with `"; cleanup failures: "`, or an empty string if the input slice is empty. [crates/gwiki/src/ingest/pdf/ingest.rs:252-258]

