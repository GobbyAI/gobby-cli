---
title: crates/gwiki/src/ingest/url.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/url.rs
  ranges:
  - 25-31
  - 34-38
  - 41-45
  - 48-51
  - 53-65
  - 68-77
  - 79-113
  - 115-148
  - 150-163
  - 165-170
  - 172-211
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/url.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

This file defines the URL-ingest data model and orchestration for turning fetched web content into wiki content. `UrlSnapshot` captures a fetch result, while `AcceptedUrlIngest`, `UrlIngestFailure`, and `UrlBatchIngest` record per-URL outcomes and provide batch status/exit-code reporting. The ingest path splits HTML and non-HTML snapshots: HTML snapshots are parsed for a title, rendered to canonical markdown, and written into the vault, while non-HTML snapshots are stored as assets with a markdown wrapper. Batch ingestion fetches each URL, collects successes and failures, and triggers reindexing when anything was accepted.
[crates/gwiki/src/ingest/url.rs:25-31]
[crates/gwiki/src/ingest/url.rs:34-38]
[crates/gwiki/src/ingest/url.rs:41-45]
[crates/gwiki/src/ingest/url.rs:48-51]
[crates/gwiki/src/ingest/url.rs:53-65]

## API Symbols

- `UrlSnapshot` (class) component `UrlSnapshot [class]` (`c14b8f0a-a77a-503a-9bb9-4353724c9db4`) lines 25-31 [crates/gwiki/src/ingest/url.rs:25-31]
  - Signature: `pub struct UrlSnapshot {`
  - Purpose: 'UrlSnapshot' is a data container capturing an HTTP fetch result, including the originally requested URL, the resolved final URL, fetch timestamp, raw response body bytes, and an optional content type. [crates/gwiki/src/ingest/url.rs:25-31]
- `AcceptedUrlIngest` (class) component `AcceptedUrlIngest [class]` (`10b5ab90-399b-564d-a071-16987e705a84`) lines 34-38 [crates/gwiki/src/ingest/url.rs:34-38]
  - Signature: `pub struct AcceptedUrlIngest {`
  - Purpose: 'AcceptedUrlIngest' is a data container for an ingest operation that records the originally requested URL, the resolved final URL, and the associated 'IngestResult'. [crates/gwiki/src/ingest/url.rs:34-38]
- `UrlIngestFailure` (class) component `UrlIngestFailure [class]` (`e1a888d5-5ecc-50f0-8c6b-a2edc46ac72f`) lines 41-45 [crates/gwiki/src/ingest/url.rs:41-45]
  - Signature: `pub struct UrlIngestFailure {`
  - Purpose: 'UrlIngestFailure' is a Rust struct that records a failed URL ingestion attempt with the affected 'url', an error 'code', and a human-readable 'message'. [crates/gwiki/src/ingest/url.rs:41-45]
- `UrlBatchIngest` (class) component `UrlBatchIngest [class]` (`c301d5b8-188c-50a5-acbc-40f22d82cba4`) lines 48-51 [crates/gwiki/src/ingest/url.rs:48-51]
  - Signature: `pub struct UrlBatchIngest {`
  - Purpose: 'UrlBatchIngest' is a batch result struct containing two public vectors: 'accepted', which stores successfully accepted URL ingests, and 'failed', which stores corresponding ingestion failures. [crates/gwiki/src/ingest/url.rs:48-51]
- `UrlBatchIngest` (class) component `UrlBatchIngest [class]` (`17c6626f-8890-5afa-b08e-d691de95afe8`) lines 53-65 [crates/gwiki/src/ingest/url.rs:53-65]
  - Signature: `impl UrlBatchIngest {`
  - Purpose: UrlBatchIngest derives a batch-ingest result from its 'accepted' and 'failed' sets, returning '"ingested"', '"partial"', or '"failed"' via 'status()' and a Unix-style 'exit_code()' of '0' when any items were accepted or '1' when none were. [crates/gwiki/src/ingest/url.rs:53-65]
- `UrlBatchIngest.status` (method) component `UrlBatchIngest.status [method]` (`0cc24868-fd0f-555a-b5cf-895a77c56d02`) lines 54-60 [crates/gwiki/src/ingest/url.rs:54-60]
  - Signature: `pub fn status(&self) -> &'static str {`
  - Purpose: Returns a static status string based on collection emptiness: '"ingested"' when 'accepted' is non-empty and 'failed' is empty, '"partial"' when both are non-empty, and '"failed"' when 'accepted' is empty. [crates/gwiki/src/ingest/url.rs:54-60]
- `UrlBatchIngest.exit_code` (method) component `UrlBatchIngest.exit_code [method]` (`2e635155-f4db-5502-9348-7e6cdca94939`) lines 62-64 [crates/gwiki/src/ingest/url.rs:62-64]
  - Signature: `pub fn exit_code(&self) -> u8 {`
  - Purpose: Returns '1' if 'self.accepted' is empty and '0' otherwise, by converting the emptiness check to 'u8'. [crates/gwiki/src/ingest/url.rs:62-64]
- `ingest_snapshot` (function) component `ingest_snapshot [function]` (`c056c1c8-97f3-5779-9a83-3d2e3dda80a0`) lines 68-77 [crates/gwiki/src/ingest/url.rs:68-77]
  - Signature: `pub fn ingest_snapshot(`
  - Purpose: Ingests a URL snapshot into the vault by delegating to 'ingest_snapshot_without_index', then reindexes the vault via 'index_after_ingest', returning the original 'IngestResult' or propagating any 'WikiError'. [crates/gwiki/src/ingest/url.rs:68-77]
- `ingest_snapshot_without_index` (function) component `ingest_snapshot_without_index [function]` (`a4f1949d-4667-5f9f-9af6-cf853e1476ca`) lines 79-113 [crates/gwiki/src/ingest/url.rs:79-113]
  - Signature: `pub(crate) fn ingest_snapshot_without_index(`
  - Purpose: Ingests a URL snapshot into the vault without indexing by routing non-HTML snapshots to a separate handler, otherwise parsing the HTML to extract a title, register a 'SourceDraft', render canonical markdown from the document and content hash, write the raw markdown, and return the resulting record and raw path. [crates/gwiki/src/ingest/url.rs:79-113]
- `ingest_non_html_snapshot_without_index` (function) component `ingest_non_html_snapshot_without_index [function]` (`c4a98887-d879-58d7-81a6-9d70911c19b3`) lines 115-148 [crates/gwiki/src/ingest/url.rs:115-148]
  - Signature: `fn ingest_non_html_snapshot_without_index(`
  - Purpose: Ingests a non-HTML 'UrlSnapshot' by hashing its body, deriving a source kind and title, registering a 'SourceDraft' in the vault manifest, writing the body as an asset plus a rendered raw Markdown wrapper, and returning the resulting record with paths to the raw markdown and asset. [crates/gwiki/src/ingest/url.rs:115-148]
- `ingest_urls` (function) component `ingest_urls [function]` (`62953a1c-8373-5ac7-a984-4be6c048f349`) lines 150-163 [crates/gwiki/src/ingest/url.rs:150-163]
  - Signature: `pub(crate) fn ingest_urls(`
  - Purpose: Delegates URL batch ingestion to 'ingest_urls_with_fetcher' using the default 'fetch::fetch_url_snapshot' fetcher, passing through 'vault_root', 'store', 'urls', and 'fetched_at', and returns the resulting 'UrlBatchIngest' or 'WikiError'. [crates/gwiki/src/ingest/url.rs:150-163]
- `fetch_url_snapshot` (function) component `fetch_url_snapshot [function]` (`4c565554-84f8-5b2e-90f6-3ee1cce5914f`) lines 165-170 [crates/gwiki/src/ingest/url.rs:165-170]
  - Signature: `pub(crate) fn fetch_url_snapshot(`
  - Purpose: Delegates to 'fetch::fetch_url_snapshot' to retrieve and return a 'UrlSnapshot' for the given 'url' and 'fetched_at' timestamp, propagating any 'UrlIngestFailure'. [crates/gwiki/src/ingest/url.rs:165-170]
- `ingest_urls_with_fetcher` (function) component `ingest_urls_with_fetcher [function]` (`ab220337-f2ba-54b8-9c30-7018ddfa681b`) lines 172-211 [crates/gwiki/src/ingest/url.rs:172-211]
  - Signature: `pub(crate) fn ingest_urls_with_fetcher(`
  - Purpose: Validates that at least one URL was provided, then for each URL fetches a snapshot at 'fetched_at', ingests successful snapshots into the vault, records per-URL successes and failures, and triggers a post-ingest index rebuild if any snapshot was accepted before returning the aggregated 'UrlBatchIngest'. [crates/gwiki/src/ingest/url.rs:172-211]

