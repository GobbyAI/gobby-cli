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

This file defines the `MediaWikiPageSnapshot` input model and the ingest path for turning a fetched MediaWiki page into stored wiki content and index metadata. `ingest_page` normalizes the title and source URL, registers the snapshot as a `MediaWiki` source draft with revision/fetch data, renders a Markdown wrapper around the raw wikitext via `render_mediawiki_markdown`, and writes the raw content plus index entry; the test confirms the written metadata preserves the expected normalized fields, revision details, category, and citation/source kind.
[crates/gwiki/src/ingest/mediawiki.rs:12-20]
[crates/gwiki/src/ingest/mediawiki.rs:23-41]
[crates/gwiki/src/ingest/mediawiki.rs:44-77]
[crates/gwiki/src/ingest/mediawiki.rs:86-123]

## API Symbols

- `MediaWikiPageSnapshot` (class) component `MediaWikiPageSnapshot [class]` (`470371ee-0191-55ba-9bd4-50518c31030d`) lines 12-20 [crates/gwiki/src/ingest/mediawiki.rs:12-20]
  - Signature: `pub struct MediaWikiPageSnapshot {`
  - Purpose: 'MediaWikiPageSnapshot' is a data container capturing a fetched MediaWiki page’s identity, provenance, and content, including its title, source URL, revision metadata, fetch timestamp, raw wikitext, and optional category. [crates/gwiki/src/ingest/mediawiki.rs:12-20]
- `ingest_page` (function) component `ingest_page [function]` (`85bc50e7-a305-5dc5-835f-d8714205e70b`) lines 23-41 [crates/gwiki/src/ingest/mediawiki.rs:23-41]
  - Signature: `pub fn ingest_page(`
  - Purpose: 'ingest_page' normalizes a MediaWiki snapshot’s title and source URL, registers the page as a 'SourceManifest' draft with its wikitext and fetch metadata, renders Markdown from the snapshot and content hash, and writes the raw content plus index entry via 'write_raw_then_index'. [crates/gwiki/src/ingest/mediawiki.rs:23-41]
- `render_mediawiki_markdown` (function) component `render_mediawiki_markdown [function]` (`8bacfa5e-3925-593c-9c3b-da9a9ebb8967`) lines 44-77 [crates/gwiki/src/ingest/mediawiki.rs:44-77]
  - Signature: `fn render_mediawiki_markdown(`
  - Purpose: Builds a Markdown document with MediaWiki metadata front matter, a level-1 title heading, and the page’s raw wikitext body, appending a trailing newline if needed. [crates/gwiki/src/ingest/mediawiki.rs:44-77]
- `mediawiki_records_revision_metadata` (function) component `mediawiki_records_revision_metadata [function]` (`91cffa1e-7fbc-5079-b2de-98e00d68b797`) lines 86-123 [crates/gwiki/src/ingest/mediawiki.rs:86-123]
  - Signature: `fn mediawiki_records_revision_metadata() {`
  - Purpose: Verifies that 'ingest_page' normalizes MediaWiki snapshot metadata into the written raw markdown and source manifest, including newline-stripped title/source URL, revision fields, category metadata, and 'MediaWiki' source kind/citation. [crates/gwiki/src/ingest/mediawiki.rs:86-123]

