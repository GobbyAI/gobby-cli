---
title: crates/gwiki/src/ingest/url.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/url.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/url.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/url.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/url.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `UrlSnapshot` | class | The 'UrlSnapshot' struct represents the captured state of a URL fetch operation, storing the requested and final URLs, retrieval timestamp, raw response body bytes, and an optional content type. [crates/gwiki/src/ingest/url.rs:25-31] |
| `AcceptedUrlIngest` | class | The 'AcceptedUrlIngest' struct represents the state and outcome of a URL ingestion process, storing the originally requested URL, the final resolved URL, and the resulting ingestion status. [crates/gwiki/src/ingest/url.rs:34-38] |
| `UrlIngestFailure` | class | The 'UrlIngestFailure' struct represents a failure encountered during URL ingestion, encapsulating the target URL, an error code, and a descriptive error message. [crates/gwiki/src/ingest/url.rs:41-45] |
| `UrlBatchIngest` | class | The 'UrlBatchIngest' struct represents the outcome of a batch URL ingestion process, categorizing results into vectors of successfully accepted URL ingestions and failed URL ingestions. [crates/gwiki/src/ingest/url.rs:48-51] |
| `UrlBatchIngest::status` | method | The 'status' method returns a static string slice indicating the ingestion state as "ingested" if only accepted items exist, "partial" if both accepted and failed items are present, and "failed" if there are no accepted items. [crates/gwiki/src/ingest/url.rs:54-60] |
| `UrlBatchIngest::exit_code` | method | This method returns '1' if the 'accepted' collection is empty, and '0' otherwise, by converting the boolean result of 'is_empty()' to a 'u8'. [crates/gwiki/src/ingest/url.rs:62-64] |
| `ingest_snapshot` | function | The 'ingest_snapshot' function ingests a 'UrlSnapshot' into the specified 'vault_root' directory and subsequently indexes the updated vault using the provided 'WikiIndexStore', returning an 'IngestResult' on success. [crates/gwiki/src/ingest/url.rs:68-77] |
| `ingest_snapshot_without_index` | function | The 'ingest_snapshot_without_index' function processes a 'UrlSnapshot' by either delegating non-HTML content to a dedicated handler or, for HTML content, parsing the document, registering a 'SourceManifest' record, rendering its parsed structure into Markdown, and writing the raw Markdown file to the vault. [crates/gwiki/src/ingest/url.rs:79-113] |
| `ingest_non_html_snapshot_without_index` | function | This function ingests a non-HTML 'UrlSnapshot' into a vault by registering a 'SourceManifest' record, writing the raw snapshot body as a local asset, generating and writing a corresponding metadata-rich Markdown file, and returning the resulting manifest record and output paths. [crates/gwiki/src/ingest/url.rs:115-148] |
| `ingest_urls` | function | The 'ingest_urls' function ingests a slice of URLs into a wiki index store under a specified vault root and timestamp by delegating to 'ingest_urls_with_fetcher' using the default 'fetch::fetch_url_snapshot' fetcher. [crates/gwiki/src/ingest/url.rs:150-163] |
| `fetch_url_snapshot` | function | The 'fetch_url_snapshot' function delegates the retrieval of a URL snapshot at a given timestamp to 'fetch::fetch_url_snapshot', returning a 'Result' of 'UrlSnapshot' or 'UrlIngestFailure'. [crates/gwiki/src/ingest/url.rs:165-170] |
| `ingest_urls_with_fetcher` | function | This function ingests a batch of URLs by fetching their snapshots via a provided closure, writing them to a vault, updating the wiki search index if any ingestion succeeds, and returning a detailed report of successful and failed ingests. [crates/gwiki/src/ingest/url.rs:172-211] |

