---
title: crates/gwiki/src/indexer.rs
type: code_file
provenance:
- file: crates/gwiki/src/indexer.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/indexer.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/indexer.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gwiki/src/indexer.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexOptions` | class | 'IndexOptions' is a struct containing a single boolean field, 'respect_gitignore', which controls whether indexing honors '.gitignore' rules. [crates/gwiki/src/indexer.rs:16-18] |
| `IndexOptions::default` | method | Returns a 'Self' instance with 'respect_gitignore' initialized to 'true'. [crates/gwiki/src/indexer.rs:21-25] |
| `IndexError` | type | Indexed type `IndexError` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:29-35] |
| `IndexError::fmt` | method | Implements 'Display' by matching each error variant and formatting a specific human-readable diagnostic message, including embedded paths and byte-limit values where applicable. [crates/gwiki/src/indexer.rs:38-57] |
| `IndexError::source` | method | Returns the underlying 'std::error::Error' for 'Io' and 'Store' variants by borrowing their inner error, and returns 'None' for all other variants. [crates/gwiki/src/indexer.rs:61-67] |
| `IndexError::from` | method | Converts a 'StoreError' into 'Self' by wrapping it in the 'Self::Store' enum variant. [crates/gwiki/src/indexer.rs:71-73] |
| `IndexError::from` | method | Converts a 'std::io::Error' into 'Self' by wrapping it in the 'Self::Io' variant. [crates/gwiki/src/indexer.rs:77-79] |
| `index_vault` | function | 'index_vault' indexes a vault rooted at the given path into the provided 'WikiIndexStore' by delegating to 'index_vault_with_options' with 'IndexOptions::default()', returning an 'IndexError' on failure. [crates/gwiki/src/indexer.rs:82-87] |
| `index_vault_with_options` | function | Indexes a vault root by diffing previously stored and newly discovered content hashes, then applying per-file add/change/delete/unchanged/skipped ingestion updates to the 'WikiIndexStore' and derived rows according to 'IndexOptions'. [crates/gwiki/src/indexer.rs:89-148] |
| `discover_indexable_hashes` | function | Delegates to 'discover_indexable_hashes_with_limit', passing 'vault_root', the configured memory index limit in bytes, and 'options', and returns the resulting 'Result<BTreeMap<PathBuf, String>, IndexError>'. [crates/gwiki/src/indexer.rs:150-155] |
| `discover_indexable_hashes_with_limit` | function | Walks files under 'vault_root' with optional gitignore respect, filters to regular indexable vault paths, accumulates their sizes against an optional 'memory_limit', and returns a 'BTreeMap' of relative paths to content hashes or a corresponding 'IndexError' on walk, path, hash, or limit failures. [crates/gwiki/src/indexer.rs:157-197] |
| `index_file` | function | Indexes a wiki file by looking up its current content hash, reading and parsing the file into document/chunks/links/source, then upserting all derived records and recording the file hash and ingestion event in the index store. [crates/gwiki/src/indexer.rs:199-236] |
| `is_indexable_vault_path` | function | Returns 'true' only for 'raw/INDEX.md' or for '.md' files whose normalized path components start with 'code' or 'knowledge', and 'false' otherwise. [crates/gwiki/src/indexer.rs:238-249] |
| `document_kind` | function | Returns a 'WikiDocumentKind' based on the path prefix, treating 'raw/INDEX.md' as 'SourceCatalog', any 'code/...' path as 'CodeDoc', 'knowledge/sources/...' as 'SourceNote', 'knowledge/concepts/...' as 'Concept', 'knowledge/topics/...' as 'Topic', and other 'knowledge/...' paths as 'Concept', otherwise 'None'. [crates/gwiki/src/indexer.rs:251-264] |
| `normal_components` | function | Returns a 'Vec<&str>' containing only the UTF-8 'Component::Normal' segments of 'path', discarding all non-normal path components. [crates/gwiki/src/indexer.rs:266-273] |
| `ParsedWikiDocument` | class | 'ParsedWikiDocument' is a parsed representation of a wiki document that bundles the original 'WikiDocument' with its extracted 'WikiChunk's, 'WikiLink's, and originating 'WikiSource'. [crates/gwiki/src/indexer.rs:275-280] |
| `parse_wiki_document` | function | 'parse_wiki_document' constructs a 'ParsedWikiDocument' from a wiki file path, document kind, content hash, and Markdown body by deriving the title from the first heading, chunking the body into indexed 'WikiChunk's with extracted text slices and headings, collecting links, and populating the nested 'WikiDocument' and 'WikiSource' metadata. [crates/gwiki/src/indexer.rs:282-324] |
| `chunks_for_markdown` | function | 'chunks_for_markdown' splits a markdown body into 'Chunk' records at each detected heading span, using each heading’s byte range start up to the next heading or EOF, and falling back to a single whole-file chunk with an optional fallback heading when no headings are found. [crates/gwiki/src/indexer.rs:326-355] |
| `heading_spans` | function | Scans the input text line by line, and returns a vector of '(byte_offset, heading_text)' for each line that 'parse_heading' recognizes as a heading. [crates/gwiki/src/indexer.rs:357-369] |
| `first_heading` | function | Returns the first line in 'body' that 'parse_heading' recognizes as a heading, or 'None' if no heading is found. [crates/gwiki/src/indexer.rs:371-373] |
| `parse_heading` | function | Parses an ATX markdown heading from 'line', returns the heading text as 'Some(String)' when present and non-empty, and otherwise returns 'None'. [crates/gwiki/src/indexer.rs:375-379] |
| `extract_links` | function | 'extract_links' parses wiki links from 'body' with no excluded prefixes, attaches 'path' to each extracted link as its source, preserves target/alias and byte offsets, sorts the resulting 'Vec<WikiLink>' by 'byte_start', and returns it. [crates/gwiki/src/indexer.rs:381-394] |
| `write_file` | function | Joins 'relative' to 'root', creates any missing parent directories for the resulting path, and writes 'contents' to that file, panicking on any filesystem error. [crates/gwiki/src/indexer.rs:407-413] |
| `seed_derived_rows` | function | Seeds a 'MemoryWikiStore' entry for the given relative path with stale placeholder data by inserting a 'WikiDocument', empty chunks, one dummy link, a 'WikiSource', and a file hash all keyed to that path. [crates/gwiki/src/indexer.rs:415-448] |
| `index_writer_upserts_documents_chunks_links_sources_and_ingestions` | function | Creates a temporary wiki vault containing a topic Markdown document, indexes it into a 'MemoryWikiStore', and verifies that the writer upserts the document as a 'Topic' with non-empty chunks, two extracted links, a matching source record, and an 'Added' ingestion event. [crates/gwiki/src/indexer.rs:451-468] |
| `index_vault_respects_gitignore_by_default_and_option` | function | Verifies that 'index_vault' ignores files matched by '.gitignore' by default, but 'index_vault_with_options' indexes them when 'respect_gitignore' is set to 'false'. [crates/gwiki/src/indexer.rs:471-509] |
| `deleted_file_removes_derived_rows_only` | function | Verifies that 'index_vault' removes all derived store rows and records a deleted path for a stale document, while leaving unrelated raw files on disk unchanged. [crates/gwiki/src/indexer.rs:512-534] |
| `raw_sources_are_immutable` | function | Verifies that indexing a vault leaves raw source files unchanged on disk and stores only 'raw/INDEX.md' in the document map, not 'raw/article.txt'. [crates/gwiki/src/indexer.rs:537-561] |
| `unchanged_files_are_skipped` | function | Verifies that re-indexing a vault without modifying a file leaves all store upsert/replacement counters unchanged and records the ingestion event as 'WikiIngestionEvent::Unchanged' for that file. [crates/gwiki/src/indexer.rs:564-594] |
| `indexes_codedocs_with_provenance` | function | Creates a temporary codedoc Markdown file with YAML provenance and an internal link, indexes the vault into a 'MemoryWikiStore', and verifies the document is classified as 'CodeDoc' with provenance preserved, link metadata extracted, and an 'Added' ingestion event recorded. [crates/gwiki/src/indexer.rs:597-617] |
| `unified_vault_indexes_code_root_wikilinks` | function | Verifies that 'index_vault' classifies both unified-vault markdown pages as 'WikiDocumentKind::CodeDoc' and extracts their bidirectional wikilinks, preserving the alias on the module-to-file link and the source provenance metadata. [crates/gwiki/src/indexer.rs:620-650] |
| `codedoc_tree_indexes_idempotently` | function | Verifies that 'index_vault' indexes only Markdown code docs, ignores non-Markdown files, and is idempotent across re-indexing by reporting changed versus unchanged ingestions and updating document, chunk, link, and source counts accordingly. [crates/gwiki/src/indexer.rs:653-686] |
| `memory_index_limit_rejects_large_vaults` | function | Creates a temporary vault containing a single indexed file, invokes discovery with a memory index limit of 4, and asserts that the operation fails with 'IndexError::MemoryIndexTooLarge'. [crates/gwiki/src/indexer.rs:689-702] |

