---
title: crates/gwiki/src/ingest/mediawiki.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/mediawiki.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/mediawiki.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/mediawiki.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/mediawiki.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `MediaWikiPageSnapshot` | class | The 'MediaWikiPageSnapshot' struct represents a point-in-time capture of a MediaWiki page, containing metadata such as its title, source URL, revision identifier, optional revision timestamp, retrieval timestamp, optional category, and the raw wikitext content. [crates/gwiki/src/ingest/mediawiki.rs:12-20] |
| `ingest_page` | function | The 'ingest_page' function registers a MediaWiki page snapshot as a source draft manifest, renders its wikitext content into Markdown, and then writes and indexes the formatted document within the specified vault and wiki index store. [crates/gwiki/src/ingest/mediawiki.rs:23-41] |
| `render_mediawiki_markdown` | function | The 'render_mediawiki_markdown' function generates a markdown-formatted string by prepending a serialized metadata block and a level-one heading of the page title to the raw wikitext from a 'MediaWikiPageSnapshot'. [crates/gwiki/src/ingest/mediawiki.rs:44-77] |

_Verified by 1 in-file unit test._

