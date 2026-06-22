---
title: crates/gwiki/src/ingest/pdf/ingest.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/ingest.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/ingest.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/pdf/ingest.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/pdf/ingest.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ingest_pages` | function | The 'ingest_pages' function ingests PDF pages into a wiki index store by delegating to 'ingest_pages_with_vision' with an empty vector and an unavailable vision endpoint configuration. [crates/gwiki/src/ingest/pdf/ingest.rs:23-37] |
| `ingest_pdf_file` | function | The 'ingest_pdf_file' function ingests a PDF file snapshot into a vault scope using a vision endpoint and specified options, and subsequently updates the wiki index store with the newly ingested content. [crates/gwiki/src/ingest/pdf/ingest.rs:41-52] |
| `ingest_pdf_file_without_index` | function | This function extracts text-layer pages and renders page images from a PDF file snapshot, tracking any extraction or rendering degradation failures, and forwards them alongside the provided vision endpoint to 'ingest_pages_with_vision_inner' for final processing. [crates/gwiki/src/ingest/pdf/ingest.rs:55-108] |
| `ingest_pages_with_vision` | function | This function ingests rendered PDF pages using a vision endpoint by delegating to an unindexed ingestion helper and subsequently updates the wiki index store with the newly ingested content. [crates/gwiki/src/ingest/pdf/ingest.rs:111-128] |
| `ingest_pages_with_vision_without_index` | function | This function delegates the ingestion of rendered PDF pages using a vision endpoint to an inner function, passing an empty index vector and returning a Result containing the IngestResult or a WikiError. [crates/gwiki/src/ingest/pdf/ingest.rs:131-146] |
| `ingest_pages_with_vision_inner` | function | This function registers a PDF snapshot in the vault manifest, saves the original asset, merges extracted text with vision-rendered pages to generate a structured markdown representation, and handles document degradation and rollback logic. [crates/gwiki/src/ingest/pdf/ingest.rs:149-220] |
| `rollback_registered_pdf_source` | function | This function reverts a PDF ingestion failure by deleting the optionally specified PDF asset, restoring the source manifest to its previous state, and returning the original 'WikiError' augmented with diagnostics from any subsequent cleanup or manifest-write failures. [crates/gwiki/src/ingest/pdf/ingest.rs:223-247] |
| `cleanup_pdf_file` | function | The 'cleanup_pdf_file' function deletes the file located at the combined path of 'vault_root' and 'relative_path', ignoring 'NotFound' errors and appending any other encountered I/O errors to the provided 'cleanup_errors' vector. [crates/gwiki/src/ingest/pdf/ingest.rs:250-257] |
| `pdf_cleanup_detail` | function | The 'pdf_cleanup_detail' function returns a formatted string containing a semicolon-delimited list of cleanup errors prefixed with a label if the input slice is non-empty, and an empty string otherwise. [crates/gwiki/src/ingest/pdf/ingest.rs:260-266] |

