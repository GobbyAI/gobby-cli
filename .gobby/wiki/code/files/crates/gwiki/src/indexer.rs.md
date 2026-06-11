---
title: crates/gwiki/src/indexer.rs
type: code_file
provenance:
- file: crates/gwiki/src/indexer.rs
  ranges:
  - 16-18
  - 20-26
  - 21-25
  - 29-35
  - 37-58
  - 38-57
  - 60-68
  - 61-67
  - 70-74
  - 71-73
  - 76-80
  - 77-79
  - 82-87
  - 89-148
  - 150-155
  - 157-197
  - 199-236
  - 238-249
  - 251-264
  - 266-273
  - 275-280
  - 282-324
  - 326-355
  - 357-369
  - 371-373
  - 375-379
  - 381-394
  - 407-413
  - 415-448
  - 451-468
  - 471-509
  - 512-534
  - 537-561
  - 564-594
  - 597-617
  - 620-650
  - 653-686
  - 689-702
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/indexer.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/indexer.rs` exposes 38 indexed API symbols.
[crates/gwiki/src/indexer.rs:16-18]
[crates/gwiki/src/indexer.rs:20-26]
[crates/gwiki/src/indexer.rs:21-25]
[crates/gwiki/src/indexer.rs:29-35]
[crates/gwiki/src/indexer.rs:37-58]

## API Symbols

- `IndexOptions` (class) component `IndexOptions [class]` (`4c0b2412-48bc-5519-b681-b25e7c1381f4`) lines 16-18 [crates/gwiki/src/indexer.rs:16-18]
  - Signature: `pub struct IndexOptions {`
  - Purpose: IndexOptions is a configuration struct with a single boolean field that controls whether `.gitignore` files are respected during indexing operations. [crates/gwiki/src/indexer.rs:16-18]
- `IndexOptions` (class) component `IndexOptions [class]` (`9144ed2e-6b1d-5b1c-a241-8d245fe5a930`) lines 20-26 [crates/gwiki/src/indexer.rs:20-26]
  - Signature: `impl Default for IndexOptions {`
  - Purpose: The `Default` trait implementation for `IndexOptions` initializes instances with `.gitignore` file respect enabled (`respect_gitignore: true`). [crates/gwiki/src/indexer.rs:20-26]
- `IndexOptions.default` (method) component `IndexOptions.default [method]` (`d05bc2bb-85a0-51dc-87d9-eeeacd4a0868`) lines 21-25 [crates/gwiki/src/indexer.rs:21-25]
  - Signature: `fn default() -> Self {`
  - Purpose: This method implements the `Default` trait to construct a new instance of Self with the `respect_gitignore` field set to `true`. [crates/gwiki/src/indexer.rs:21-25]
- `IndexError` (type) component `IndexError [type]` (`901f70e5-76ce-54e3-8d7c-b2cfff5671e5`) lines 29-35 [crates/gwiki/src/indexer.rs:29-35]
  - Signature: `pub enum IndexError {`
  - Purpose: Indexed type `IndexError` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:29-35]
- `IndexError` (class) component `IndexError [class]` (`469c5c07-735b-5a31-80e9-ba04a474d049`) lines 37-58 [crates/gwiki/src/indexer.rs:37-58]
  - Signature: `impl fmt::Display for IndexError {`
  - Purpose: A Rust `Display` trait implementation for `IndexError` that formats five enumeration variants representing distinct wiki indexing failures: I/O errors, directory traversal errors, store errors, vault boundary violations, and memory limit exceeded conditions. [crates/gwiki/src/indexer.rs:37-58]
- `IndexError.fmt` (method) component `IndexError.fmt [method]` (`2cccdbc9-38c3-5be8-b21c-7066af4ac7b4`) lines 38-57 [crates/gwiki/src/indexer.rs:38-57]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Implements the `Display` trait for a wiki index error enum, formatting each variant (I/O, walk, store, path validation, or memory limit failures) as a contextual error message. [crates/gwiki/src/indexer.rs:38-57]
- `IndexError` (class) component `IndexError [class]` (`d4e2fb6c-6897-5fd2-ac71-2ac09b3938fb`) lines 60-68 [crates/gwiki/src/indexer.rs:60-68]
  - Signature: `impl std::error::Error for IndexError {`
  - Purpose: This `std::error::Error` trait implementation for `IndexError` enables error source chaining by exposing underlying `Io` and `Store` error sources through the `source()` method, while treating other variants as terminal errors. [crates/gwiki/src/indexer.rs:60-68]
- `IndexError.source` (method) component `IndexError.source [method]` (`a5b3cc15-25f4-5c9c-8f7c-919a12e981f6`) lines 61-67 [crates/gwiki/src/indexer.rs:61-67]
  - Signature: `fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {`
  - Purpose: Returns an optional reference to the underlying error source, extracting it from `Io` and `Store` variants while returning `None` for all other enum variants. [crates/gwiki/src/indexer.rs:61-67]
- `IndexError` (class) component `IndexError [class]` (`c100b2cb-8ca3-596d-8579-677720c5e3af`) lines 70-74 [crates/gwiki/src/indexer.rs:70-74]
  - Signature: `impl From<StoreError> for IndexError {`
  - Purpose: Implements the `From<StoreError>` trait for `IndexError`, enabling automatic conversion that wraps `StoreError` values in the `IndexError::Store` variant. [crates/gwiki/src/indexer.rs:70-74]
- `IndexError.from` (method) component `IndexError.from [method]` (`fe5e70bc-0102-59ac-b2d2-f7e411b44584`) lines 71-73 [crates/gwiki/src/indexer.rs:71-73]
  - Signature: `fn from(error: StoreError) -> Self {`
  - Purpose: This `From` trait implementation converts a `StoreError` into `Self` by wrapping it in the `Store` enum variant. [crates/gwiki/src/indexer.rs:71-73]
- `IndexError` (class) component `IndexError [class]` (`60917d58-fc32-5054-acb2-c66c21b1eaed`) lines 76-80 [crates/gwiki/src/indexer.rs:76-80]
  - Signature: `impl From<std::io::Error> for IndexError {`
  - Purpose: Implements the `From` trait to provide automatic conversion from `std::io::Error` into `IndexError::Io`. [crates/gwiki/src/indexer.rs:76-80]
- `IndexError.from` (method) component `IndexError.from [method]` (`8daaa8db-7d4b-5157-a3d4-abc0676e44ed`) lines 77-79 [crates/gwiki/src/indexer.rs:77-79]
  - Signature: `fn from(error: std::io::Error) -> Self {`
  - Purpose: Implements the `From<std::io::Error>` trait to convert `std::io::Error` into the calling type's `Io` enum variant. [crates/gwiki/src/indexer.rs:77-79]
- `index_vault` (function) component `index_vault [function]` (`084350ac-2f89-55f2-9c57-b19dda5ff561`) lines 82-87 [crates/gwiki/src/indexer.rs:82-87]
  - Signature: `pub fn index_vault(`
  - Purpose: Indexes a vault directory into a wiki index store using default indexing options. [crates/gwiki/src/indexer.rs:82-87]
- `index_vault_with_options` (function) component `index_vault_with_options [function]` (`11e149bf-fa0b-56b6-8c0d-4f729cf32adb`) lines 89-148 [crates/gwiki/src/indexer.rs:89-148]
  - Signature: `pub fn index_vault_with_options(`
  - Purpose: Incrementally indexes a wiki vault by comparing previous and current file content hashes, generating change events (added, changed, deleted, unchanged, skipped), and persisting ingestion records to a WikiIndexStore for each file state. [crates/gwiki/src/indexer.rs:89-148]
- `discover_indexable_hashes` (function) component `discover_indexable_hashes [function]` (`70f7cc06-4f06-5527-9155-02dadbab84b6`) lines 150-155 [crates/gwiki/src/indexer.rs:150-155]
  - Signature: `fn discover_indexable_hashes(`
  - Purpose: Discovers and returns a sorted map of paths to their corresponding indexable hash strings within a vault, bounded by the configured memory index limit. [crates/gwiki/src/indexer.rs:150-155]
- `discover_indexable_hashes_with_limit` (function) component `discover_indexable_hashes_with_limit [function]` (`e9f3a60e-0d75-51af-843c-d15a25690d51`) lines 157-197 [crates/gwiki/src/indexer.rs:157-197]
  - Signature: `fn discover_indexable_hashes_with_limit(`
  - Purpose: Builds a BTreeMap mapping relative file paths to content hashes for all indexable vault files, constrained by an optional memory limit that returns an error if exceeded. [crates/gwiki/src/indexer.rs:157-197]
- `index_file` (function) component `index_file [function]` (`8a82206b-9853-5e69-9af3-8eeab7750a99`) lines 199-236 [crates/gwiki/src/indexer.rs:199-236]
  - Signature: `fn index_file(`
  - Purpose: Reads a wiki document from disk, parses it by document kind, and upserts the resulting document, chunks, links, and source to an index store while recording the content hash and ingestion event. [crates/gwiki/src/indexer.rs:199-236]
- `is_indexable_vault_path` (function) component `is_indexable_vault_path [function]` (`454f0e1b-bcd3-5357-9bf8-00d249913589`) lines 238-249 [crates/gwiki/src/indexer.rs:238-249]
  - Signature: `fn is_indexable_vault_path(path: &Path) -> bool {`
  - Purpose: Returns `true` if the path is `raw/INDEX.md` or a markdown file with root directory `code` or `knowledge`. [crates/gwiki/src/indexer.rs:238-249]
- `document_kind` (function) component `document_kind [function]` (`c2ee0a22-adad-5769-9858-850c69430ffb`) lines 251-264 [crates/gwiki/src/indexer.rs:251-264]
  - Signature: `fn document_kind(path: &Path) -> Option<WikiDocumentKind> {`
  - Purpose: Determines the `WikiDocumentKind` classification of a file path by pattern matching its normalized path components, with special handling for raw/INDEX.md returning `SourceCatalog`. [crates/gwiki/src/indexer.rs:251-264]
- `normal_components` (function) component `normal_components [function]` (`2e59d38a-c236-5562-88e0-26becf1424b4`) lines 266-273 [crates/gwiki/src/indexer.rs:266-273]
  - Signature: `fn normal_components(path: &Path) -> Vec<&str> {`
  - Purpose: Extracts all normal path components from the given Path and returns them as a vector of string slices, filtering out root, parent, and prefix components. [crates/gwiki/src/indexer.rs:266-273]
- `ParsedWikiDocument` (class) component `ParsedWikiDocument [class]` (`16e3cf6a-812e-562b-b582-3c8ef91e9602`) lines 275-280 [crates/gwiki/src/indexer.rs:275-280]
  - Signature: `struct ParsedWikiDocument {`
  - Purpose: ParsedWikiDocument is a container struct that aggregates a parsed wiki document with its decomposed content chunks, extracted hyperlinks, and source metadata. [crates/gwiki/src/indexer.rs:275-280]
- `parse_wiki_document` (function) component `parse_wiki_document [function]` (`91882ecb-e322-5ec5-ad83-bb17da31747e`) lines 282-324 [crates/gwiki/src/indexer.rs:282-324]
  - Signature: `fn parse_wiki_document(`
  - Purpose: Parses a markdown wiki document into a structured result containing the original document metadata, indexed content chunks with byte-range offsets and associated headings, and extracted hyperlinks. [crates/gwiki/src/indexer.rs:282-324]
- `chunks_for_markdown` (function) component `chunks_for_markdown [function]` (`d6e3ff08-8184-5139-90a6-614c5f7ccdc2`) lines 326-355 [crates/gwiki/src/indexer.rs:326-355]
  - Signature: `fn chunks_for_markdown(path: &Path, fallback_heading: Option<String>, body: &str) -> Vec<Chunk> {`
  - Purpose: This function partitions a markdown document into Chunks by heading boundaries, creating one Chunk per heading section spanning to the next heading, or a single Chunk with fallback heading if no headings exist. [crates/gwiki/src/indexer.rs:326-355]
- `heading_spans` (function) component `heading_spans [function]` (`68efa745-44b7-561e-8f88-15c7ad0928d6`) lines 357-369 [crates/gwiki/src/indexer.rs:357-369]
  - Signature: `fn heading_spans(body: &str) -> Vec<(usize, String)> {`
  - Purpose: Parses a string line-by-line to identify headings and returns a vector of (byte_offset, heading_text) tuples for each heading found. [crates/gwiki/src/indexer.rs:357-369]
- `first_heading` (function) component `first_heading [function]` (`0b45a32f-714e-548a-8fa8-d0e0bca02990`) lines 371-373 [crates/gwiki/src/indexer.rs:371-373]
  - Signature: `fn first_heading(body: &str) -> Option<String> {`
  - Purpose: Extracts and returns the first heading from a string by finding the first line that successfully parses as a heading, or None if no heading is found. [crates/gwiki/src/indexer.rs:371-373]
- `parse_heading` (function) component `parse_heading [function]` (`a284a042-b745-53fb-b624-89a1b032b168`) lines 375-379 [crates/gwiki/src/indexer.rs:375-379]
  - Signature: `fn parse_heading(line: &str) -> Option<String> {`
  - Purpose: Parses an ATX-format markdown heading from a string and returns the heading text if valid and non-empty, otherwise `None`. [crates/gwiki/src/indexer.rs:375-379]
- `extract_links` (function) component `extract_links [function]` (`cde72f8a-83cd-59f5-b5ab-2f1f82be9ab3`) lines 381-394 [crates/gwiki/src/indexer.rs:381-394]
  - Signature: `fn extract_links(path: &Path, body: &str) -> Vec<WikiLink> {`
  - Purpose: This function extracts wiki links from a document body, enriches them with the source file path and byte offsets, and returns a sorted vector of `WikiLink` structs ordered by byte position. [crates/gwiki/src/indexer.rs:381-394]
- `write_file` (function) component `write_file [function]` (`bcd36297-c732-56f1-901f-8002f067116a`) lines 407-413 [crates/gwiki/src/indexer.rs:407-413]
  - Signature: `fn write_file(root: &Path, relative: &str, contents: &str) {`
  - Purpose: Writes file contents to a path formed by joining a root directory with a relative path, creating all parent directories as needed. [crates/gwiki/src/indexer.rs:407-413]
- `seed_derived_rows` (function) component `seed_derived_rows [function]` (`386a32bf-877a-5bac-b8be-37ef0b124c52`) lines 415-448 [crates/gwiki/src/indexer.rs:415-448]
  - Signature: `fn seed_derived_rows(store: &mut MemoryWikiStore, relative: &str) {`
  - Purpose: Inserts a WikiDocument with stale metadata and its associated derived data structures (empty chunks, WikiLink, WikiSource, and file hash) into a MemoryWikiStore for a given path. [crates/gwiki/src/indexer.rs:415-448]
- `index_writer_upserts_documents_chunks_links_sources_and_ingestions` (function) component `index_writer_upserts_documents_chunks_links_sources_and_ingestions [function]` (`d0ec2c8b-fd87-5c6d-b990-d6931dfc8438`) lines 451-468 [crates/gwiki/src/indexer.rs:451-468]
  - Signature: `fn index_writer_upserts_documents_chunks_links_sources_and_ingestions() {`
  - Purpose: This test function verifies that `index_vault()` correctly indexes a wiki markdown file and populates a MemoryWikiStore with its documents, chunks, extracted links, sources, and ingestion events. [crates/gwiki/src/indexer.rs:451-468]
- `index_vault_respects_gitignore_by_default_and_option` (function) component `index_vault_respects_gitignore_by_default_and_option [function]` (`60118c6e-5c3f-58a0-bcdb-97b9fc079fc3`) lines 471-509 [crates/gwiki/src/indexer.rs:471-509]
  - Signature: `fn index_vault_respects_gitignore_by_default_and_option() {`
  - Purpose: This test validates that `index_vault` respects `.gitignore` patterns by default while `index_vault_with_options` allows disabling this behavior through the `respect_gitignore` flag in `IndexOptions`. [crates/gwiki/src/indexer.rs:471-509]
- `deleted_file_removes_derived_rows_only` (function) component `deleted_file_removes_derived_rows_only [function]` (`e37773f9-f5aa-55db-af22-5e873ac4a395`) lines 512-534 [crates/gwiki/src/indexer.rs:512-534]
  - Signature: `fn deleted_file_removes_derived_rows_only() {`
  - Purpose: Verifies that vault indexing removes deleted derived documents from all associated indices (documents, chunks, links, sources, file_hashes) while preserving raw source files. [crates/gwiki/src/indexer.rs:512-534]
- `raw_sources_are_immutable` (function) component `raw_sources_are_immutable [function]` (`1c8a74f1-9357-5269-a187-1d3c983a7fb4`) lines 537-561 [crates/gwiki/src/indexer.rs:537-561]
  - Signature: `fn raw_sources_are_immutable() {`
  - Purpose: This test verifies that raw source files remain immutable and unindexed as individual documents after vault indexing, being referenced only through their INDEX.md manifest file. [crates/gwiki/src/indexer.rs:537-561]
- `unchanged_files_are_skipped` (function) component `unchanged_files_are_skipped [function]` (`fc514bab-383f-5ed7-9cfa-dc7cebcfb999`) lines 564-594 [crates/gwiki/src/indexer.rs:564-594]
  - Signature: `fn unchanged_files_are_skipped() {`
  - Purpose: # Summary

This test verifies that re-indexing a vault with unchanged files produces no mutations to documents, chunks, links, or sources and logs a `WikiIngestionEvent::Unchanged` event. [crates/gwiki/src/indexer.rs:564-594]
- `indexes_codedocs_with_provenance` (function) component `indexes_codedocs_with_provenance [function]` (`7ee93e40-52bc-5348-a205-8344758e6d03`) lines 597-617 [crates/gwiki/src/indexer.rs:597-617]
  - Signature: `fn indexes_codedocs_with_provenance() {`
  - Purpose: Tests that the vault indexer correctly processes markdown CodeDocs with source provenance metadata, preserving the metadata and extracting inter-document links. [crates/gwiki/src/indexer.rs:597-617]
- `unified_vault_indexes_code_root_wikilinks` (function) component `unified_vault_indexes_code_root_wikilinks [function]` (`511d17b9-6550-5f9f-948a-8ee679db7405`) lines 620-650 [crates/gwiki/src/indexer.rs:620-650]
  - Signature: `fn unified_vault_indexes_code_root_wikilinks() {`
  - Purpose: # Summary

This test validates that `index_vault` correctly indexes bidirectional wikilinks between code module and file documentation, preserving document classification as CodeDoc and source metadata. [crates/gwiki/src/indexer.rs:620-650]
- `codedoc_tree_indexes_idempotently` (function) component `codedoc_tree_indexes_idempotently [function]` (`ea2a0fcb-438e-5356-83ac-0ebb8a45fb30`) lines 653-686 [crates/gwiki/src/indexer.rs:653-686]
  - Signature: `fn codedoc_tree_indexes_idempotently() {`
  - Purpose: Tests idempotent vault indexing that correctly filters markdown files, detects document changes via ingestion events, and performs necessary chunk/link/source replacements on re-indexing. [crates/gwiki/src/indexer.rs:653-686]
- `memory_index_limit_rejects_large_vaults` (function) component `memory_index_limit_rejects_large_vaults [function]` (`e5285059-1154-5c63-b7b8-1e7c53352c9c`) lines 689-702 [crates/gwiki/src/indexer.rs:689-702]
  - Signature: `fn memory_index_limit_rejects_large_vaults() {`
  - Purpose: This test verifies that `discover_indexable_hashes_with_limit` rejects vaults exceeding a configured byte limit by returning an `IndexError::MemoryIndexTooLarge` error. [crates/gwiki/src/indexer.rs:689-702]

