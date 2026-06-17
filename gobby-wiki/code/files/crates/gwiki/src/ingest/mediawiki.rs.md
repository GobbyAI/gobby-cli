---
title: crates/gwiki/src/ingest/mediawiki.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/mediawiki.rs
  ranges:
  - 12-20
  - 23-41
  - 44-77
  - 86-123
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/mediawiki.rs:12-20](crates/gwiki/src/ingest/mediawiki.rs#L12-L20), [crates/gwiki/src/ingest/mediawiki.rs:23-41](crates/gwiki/src/ingest/mediawiki.rs#L23-L41), [crates/gwiki/src/ingest/mediawiki.rs:44-77](crates/gwiki/src/ingest/mediawiki.rs#L44-L77), [crates/gwiki/src/ingest/mediawiki.rs:86-123](crates/gwiki/src/ingest/mediawiki.rs#L86-L123)

</details>

# crates/gwiki/src/ingest/mediawiki.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file ingests a MediaWiki page snapshot into the wiki index. `MediaWikiPageSnapshot` carries the fetched page data and revision details, `ingest_page` turns that snapshot into a `SourceDraft`, registers it in the `SourceManifest`, renders Markdown, and writes/indexes the result, `render_mediawiki_markdown` builds the Markdown with normalized metadata and page content, and `mediawiki_records_revision_metadata` is a helper for extracting or recording revision-related metadata used by the ingest flow.
[crates/gwiki/src/ingest/mediawiki.rs:12-20]
[crates/gwiki/src/ingest/mediawiki.rs:23-41]
[crates/gwiki/src/ingest/mediawiki.rs:44-77]
[crates/gwiki/src/ingest/mediawiki.rs:86-123]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `MediaWikiPageSnapshot` | class | `pub struct MediaWikiPageSnapshot {` | `MediaWikiPageSnapshot [class]` | `470371ee-0191-55ba-9bd4-50518c31030d` | 12-20 [crates/gwiki/src/ingest/mediawiki.rs:12-20] | Indexed class `MediaWikiPageSnapshot` in `crates/gwiki/src/ingest/mediawiki.rs`. [crates/gwiki/src/ingest/mediawiki.rs:12-20] |
| `ingest_page` | function | `pub fn ingest_page(` | `ingest_page [function]` | `85bc50e7-a305-5dc5-835f-d8714205e70b` | 23-41 [crates/gwiki/src/ingest/mediawiki.rs:23-41] | Indexed function `ingest_page` in `crates/gwiki/src/ingest/mediawiki.rs`. [crates/gwiki/src/ingest/mediawiki.rs:23-41] |
| `render_mediawiki_markdown` | function | `fn render_mediawiki_markdown(` | `render_mediawiki_markdown [function]` | `8bacfa5e-3925-593c-9c3b-da9a9ebb8967` | 44-77 [crates/gwiki/src/ingest/mediawiki.rs:44-77] | Indexed function `render_mediawiki_markdown` in `crates/gwiki/src/ingest/mediawiki.rs`. [crates/gwiki/src/ingest/mediawiki.rs:44-77] |
| `mediawiki_records_revision_metadata` | function | `fn mediawiki_records_revision_metadata() {` | `mediawiki_records_revision_metadata [function]` | `91cffa1e-7fbc-5079-b2de-98e00d68b797` | 86-123 [crates/gwiki/src/ingest/mediawiki.rs:86-123] | Indexed function `mediawiki_records_revision_metadata` in `crates/gwiki/src/ingest/mediawiki.rs`. [crates/gwiki/src/ingest/mediawiki.rs:86-123] |
