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

# crates/gwiki/src/ingest/mediawiki.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

This file defines the MediaWiki ingestion path for gwiki: it packages a fetched page into a `MediaWikiPageSnapshot`, registers the raw wikitext as a source manifest entry, renders a Markdown document with metadata, and writes it into the vault/index via `write_raw_then_index`. `render_mediawiki_markdown` builds the frontmatter from page and revision fields, normalizing values to single lines and including optional revision timestamp and category, while `mediawiki_records_revision_metadata` captures the revision details that should be preserved in the indexed record.
[crates/gwiki/src/ingest/mediawiki.rs:12-20]
[crates/gwiki/src/ingest/mediawiki.rs:23-41]
[crates/gwiki/src/ingest/mediawiki.rs:44-77]
[crates/gwiki/src/ingest/mediawiki.rs:86-123]

## API Symbols

- `MediaWikiPageSnapshot` (class) component `MediaWikiPageSnapshot [class]` (`470371ee-0191-55ba-9bd4-50518c31030d`) lines 12-20 [crates/gwiki/src/ingest/mediawiki.rs:12-20]
  - Signature: `pub struct MediaWikiPageSnapshot {`
  - Purpose: Indexed class `MediaWikiPageSnapshot` in `crates/gwiki/src/ingest/mediawiki.rs`. [crates/gwiki/src/ingest/mediawiki.rs:12-20]
- `ingest_page` (function) component `ingest_page [function]` (`85bc50e7-a305-5dc5-835f-d8714205e70b`) lines 23-41 [crates/gwiki/src/ingest/mediawiki.rs:23-41]
  - Signature: `pub fn ingest_page(`
  - Purpose: Indexed function `ingest_page` in `crates/gwiki/src/ingest/mediawiki.rs`. [crates/gwiki/src/ingest/mediawiki.rs:23-41]
- `render_mediawiki_markdown` (function) component `render_mediawiki_markdown [function]` (`8bacfa5e-3925-593c-9c3b-da9a9ebb8967`) lines 44-77 [crates/gwiki/src/ingest/mediawiki.rs:44-77]
  - Signature: `fn render_mediawiki_markdown(`
  - Purpose: Indexed function `render_mediawiki_markdown` in `crates/gwiki/src/ingest/mediawiki.rs`. [crates/gwiki/src/ingest/mediawiki.rs:44-77]
- `mediawiki_records_revision_metadata` (function) component `mediawiki_records_revision_metadata [function]` (`91cffa1e-7fbc-5079-b2de-98e00d68b797`) lines 86-123 [crates/gwiki/src/ingest/mediawiki.rs:86-123]
  - Signature: `fn mediawiki_records_revision_metadata() {`
  - Purpose: Indexed function `mediawiki_records_revision_metadata` in `crates/gwiki/src/ingest/mediawiki.rs`. [crates/gwiki/src/ingest/mediawiki.rs:86-123]

