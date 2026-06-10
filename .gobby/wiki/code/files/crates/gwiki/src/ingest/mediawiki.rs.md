---
title: crates/gwiki/src/ingest/mediawiki.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/mediawiki.rs
  ranges:
  - 11-19
  - 21-39
  - 41-74
  - 83-120
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/mediawiki.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

`crates/gwiki/src/ingest/mediawiki.rs` exposes 4 indexed API symbols.
[crates/gwiki/src/ingest/mediawiki.rs:11-19]
[crates/gwiki/src/ingest/mediawiki.rs:21-39]
[crates/gwiki/src/ingest/mediawiki.rs:41-74]
[crates/gwiki/src/ingest/mediawiki.rs:83-120]

## API Symbols

- `MediaWikiPageSnapshot` (class) component `MediaWikiPageSnapshot [class]` (`03a1634e-133f-5c13-b1c0-c120d86cb998`) lines 11-19 [crates/gwiki/src/ingest/mediawiki.rs:11-19]
  - Signature: `pub struct MediaWikiPageSnapshot {`
  - Purpose: A struct representing an immutable snapshot of a MediaWiki page revision, capturing its title, source URL, revision metadata, raw wikitext content, and optional category. [crates/gwiki/src/ingest/mediawiki.rs:11-19]
- `ingest_page` (function) component `ingest_page [function]` (`77b967ac-499a-5b8e-b001-df7152e82bbc`) lines 21-39 [crates/gwiki/src/ingest/mediawiki.rs:21-39]
  - Signature: `pub fn ingest_page(`
  - Purpose: Ingests a MediaWiki page snapshot by registering its wikitext as a source manifest, rendering it to markdown, and persisting the indexed content to a vault store. [crates/gwiki/src/ingest/mediawiki.rs:21-39]
- `render_mediawiki_markdown` (function) component `render_mediawiki_markdown [function]` (`02f7bfe4-c68b-5768-9baa-90161c0d76c6`) lines 41-74 [crates/gwiki/src/ingest/mediawiki.rs:41-74]
  - Signature: `fn render_mediawiki_markdown(`
  - Purpose: # Summary

This function transforms a MediaWiki page snapshot into a markdown document by constructing a YAML-formatted metadata header (containing source URL, revision ID, fetch timestamp, and source hash), followed by a markdown heading and the original wikitext content. [crates/gwiki/src/ingest/mediawiki.rs:41-74]
- `mediawiki_records_revision_metadata` (function) component `mediawiki_records_revision_metadata [function]` (`7a8dff0f-5ddd-5523-bfb3-3daa3975b059`) lines 83-120 [crates/gwiki/src/ingest/mediawiki.rs:83-120]
  - Signature: `fn mediawiki_records_revision_metadata() {`
  - Purpose: Tests that `ingest_page` correctly converts a MediaWiki page snapshot into a markdown file with YAML frontmatter metadata (including revision ID, timestamp, source URL, and category) and generates the corresponding source manifest entry. [crates/gwiki/src/ingest/mediawiki.rs:83-120]

