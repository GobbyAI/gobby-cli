---
title: crates/gwiki/src/ingest/url
type: code_module
provenance:
- file: crates/gwiki/src/ingest/url/fetch.rs
- file: crates/gwiki/src/ingest/url/render.rs
- file: crates/gwiki/src/ingest/url/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/url

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

## Module: `crates/gwiki/src/ingest/url`

This module is responsible for the full lifecycle of ingesting a remote URL into the gwiki knowledge store. It is organized into three concerns: HTTP retrieval (`fetch.rs`), Markdown rendering (`render.rs`), and integration tests (`tests.rs`). The public entry point visible from the parent `ingest` module is `ingest_snapshot`, which accepts a `UrlSnapshot` value and coordinates writing raw Markdown files and updating the `SourceManifest`. Internally, `fetch_url_snapshot` drives the network layer, while `render_url_markdown` and `render_non_html_url_markdown` handle serialization of the captured snapshot into a structured Markdown document with YAML-like front-matter fields.

The fetch layer (`fetch.rs:14-18`) wraps `ureq` behind a `BlockingUrlFetcher` that enforces a hard 30-second timeout, caps non-2xx error response bodies at 8 KB, and manually follows up to 10 redirects so that each hop can be validated before following. Before issuing any request, `validate_fetch_url` and `validate_resolved_fetch_url` (called at `fetch.rs:41-42`) reject disallowed IP ranges (checked via `is_disallowed_fetch_ip`) to prevent SSRF. Transport errors and HTTP error statuses are mapped into `UrlIngestFailure` variants at `fetch.rs:50-67`.

The render layer (`render.rs:11-36`) converts the fetched `UrlSnapshot` into a Markdown string by prepending structured metadata fields and then appending either an HTML-to-markdownish-text conversion (via `html_to_markdownish_text` and `scraper`) or a stub note for non-HTML assets. The distinction is made by `snapshot_is_html` (`render.rs:63`), which inspects the `content_type` field against `text/html` and `application/xhtml+xml`. Non-HTML responses are written with an additional `source_asset` field and a `media_degradation` tag (`render.rs:43-59`). Helpers `extract_title` and `html_to_markdownish_text` are tested directly in `tests.rs:8-9` alongside fetch utilities such as `read_limited_body`, `resolve_redirect_url`, and `content_length_exceeds_limit`.

This module calls into `crate::ingest` for shared utilities (`markdown_metadata`, `markdown_title`, `single_line`, `text_from_utf8_lossy`, `path_to_string`) and into `crate::sources::{SourceKind, SourceManifest}` for manifest I/O. It writes to `crate::store` types (`WikiDocument`, `WikiChunk`, `WikiLink`, `WikiIngestion`, `WikiSource`, `WikiIndexStore`) as confirmed by the test imports at `tests.rs:14-17`. The `gobby_core::indexing::content_hash` function (`tests.rs:5`) is used to produce the `source_hash` field embedded in every output document.

### Fetch constants

| Constant | Value | Purpose |
|---|---|---|
| `URL_FETCH_TIMEOUT` | 30 s | Absolute HTTP request deadline (`fetch.rs:10`) |
| `HTTP_STATUS_BODY_LIMIT_BYTES` | 8 192 B | Body read cap for error status responses (`fetch.rs:11`) |
| `MAX_REDIRECTS` | 10 | Maximum redirect hops before failure (`fetch.rs:12`) |
| `USER_AGENT` | `gwiki/0.1` | `User-Agent` header sent on every request (`fetch.rs:13`) |

### Markdown front-matter fields

| Field | HTML render | Non-HTML render | Notes |
|---|---|---|---|
| `source_kind` | `"url"` | dynamic `SourceKind` | `render.rs:19`, `render.rs:44` |
| `source_url` | `snapshot.final_url` | `snapshot.final_url` | Resolved after redirects |
| `requested_url` | `snapshot.requested_url` | `snapshot.requested_url` | Original caller URL |
| `canonical_url` | caller-supplied | caller-supplied | Fragment stripped |
| `fetched_at` | `snapshot.fetched_at` | `snapshot.fetched_at` | ISO 8601 timestamp |
| `source_hash` | `content_hash(&body)` | `content_hash(&body)` | From `gobby_core` |
| `content_type` | optional | optional | Omitted when absent |
| `source_asset` | — | asset file path | Non-HTML only (`render.rs:51`) |
| `media_degradation` | — | `"url_non_html_asset"` | Non-HTML only (`render.rs:52`) |

### Key public symbols

| Symbol | File | Role |
|---|---|---|
| `fetch_url_snapshot(url, fetched_at)` | `fetch.rs:14` | Top-level HTTP fetch → `UrlSnapshot` |
| `ingest_snapshot(path, store, snapshot)` | (parent `mod.rs`) | Orchestrates fetch → render → store write |
| `render_url_markdown(…)` | `render.rs:11` | HTML snapshot → Markdown string |
| `render_non_html_url_markdown(…)` | `render.rs:37` | Non-HTML snapshot → stub Markdown |
| `snapshot_is_html(snapshot)` | `render.rs:63` | Content-type branch selector |
| `html_to_markdownish_text(doc)` | `render.rs` | `scraper::Html` → plain Markdown body |
| `extract_title(doc)` | `render.rs` | Pulls `<title>` or first heading |
[crates/gwiki/src/ingest/url/fetch.rs:15-20]
[crates/gwiki/src/ingest/url/render.rs:12-37]
[crates/gwiki/src/ingest/url/tests.rs:21-60]
[crates/gwiki/src/ingest/url/fetch.rs:23-25]
[crates/gwiki/src/ingest/url/fetch.rs:28-35]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/url/fetch.rs\|crates/gwiki/src/ingest/url/fetch.rs]] | `crates/gwiki/src/ingest/url/fetch.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/url/render.rs\|crates/gwiki/src/ingest/url/render.rs]] | `crates/gwiki/src/ingest/url/render.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/url/tests.rs\|crates/gwiki/src/ingest/url/tests.rs]] | `crates/gwiki/src/ingest/url/tests.rs` exposes 18 indexed API symbols. |

