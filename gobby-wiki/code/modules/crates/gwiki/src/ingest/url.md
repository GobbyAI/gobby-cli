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

The `crates/gwiki/src/ingest/url` module ingests URL-backed sources by fetching a snapshot, classifying/rendering it, and producing wiki-facing source material. Fetching is handled by a blocking `ureq` agent with a fixed timeout, disabled automatic redirects, manual redirect handling, URL/IP validation, user-agent setting, and structured `UrlIngestFailure` errors for HTTP status and transport failures (`crates/gwiki/src/ingest/url/fetch.rs:1-100`).

Rendering turns `UrlSnapshot` data into markdown with metadata fields such as `source_kind`, `source_url`, `requested_url`, `canonical_url`, `fetched_at`, `source_hash`, and optional `content_type`. HTML responses are converted into “markdownish” text, while non-HTML responses are preserved as source assets and marked with `media_degradation: url_non_html_asset` (`crates/gwiki/src/ingest/url/render.rs:1-100`).

The module collaborates with shared ingest helpers for metadata, titles, path formatting, line cleanup, and lossy UTF-8 conversion; with `crate::sources::SourceKind` / `SourceManifest` for source cataloging; and with store types such as `WikiDocument`, `WikiIngestion`, and `WikiSource` during ingestion tests (`crates/gwiki/src/ingest/url/render.rs:1-100`, `crates/gwiki/src/ingest/url/tests.rs:1-100`). The tests show the end-to-end flow: a `UrlSnapshot` is ingested, raw markdown is written, canonical URL and fetch metadata are recorded, a source manifest entry is created with `SourceKind::Url`, and the in-memory wiki store receives the resulting document (`crates/gwiki/src/ingest/url/tests.rs:1-100`).

| Symbol | Role |
| --- | --- |
| `fetch_url_snapshot` | Entry point for fetching a URL into a `UrlSnapshot` (`crates/gwiki/src/ingest/url/fetch.rs:1-100`) |
| `render_url_markdown` | Renders HTML URL snapshots into markdown plus metadata (`crates/gwiki/src/ingest/url/render.rs:1-100`) |
| `render_non_html_url_markdown` | Renders non-HTML snapshots as asset-backed markdown stubs (`crates/gwiki/src/ingest/url/render.rs:1-100`) |
| `snapshot_is_html` | Detects whether a snapshot should be treated as HTML (`crates/gwiki/src/ingest/url/render.rs:1-100`) |

| Constant | Value / Purpose |
| --- | --- |
| `URL_FETCH_TIMEOUT` | 30-second fetch timeout (`crates/gwiki/src/ingest/url/fetch.rs:1-100`) |
| `HTTP_STATUS_BODY_LIMIT_BYTES` | 8 KiB HTTP error body limit (`crates/gwiki/src/ingest/url/fetch.rs:1-100`) |
| `MAX_REDIRECTS` | 10 manual redirects (`crates/gwiki/src/ingest/url/fetch.rs:1-100`) |
| `USER_AGENT` | `gwiki/0.1` request user agent (`crates/gwiki/src/ingest/url/fetch.rs:1-100`) |
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

