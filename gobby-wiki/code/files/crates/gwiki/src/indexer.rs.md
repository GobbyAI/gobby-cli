---
title: crates/gwiki/src/indexer.rs
type: code_file
provenance:
- file: crates/gwiki/src/indexer.rs
  ranges:
  - 16-18
  - 21-25
  - 29-35
  - 38-57
  - 61-67
  - 71-73
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/indexer.rs:16-18](crates/gwiki/src/indexer.rs#L16-L18), [crates/gwiki/src/indexer.rs:21-25](crates/gwiki/src/indexer.rs#L21-L25), [crates/gwiki/src/indexer.rs:29-35](crates/gwiki/src/indexer.rs#L29-L35), [crates/gwiki/src/indexer.rs:38-57](crates/gwiki/src/indexer.rs#L38-L57), [crates/gwiki/src/indexer.rs:61-67](crates/gwiki/src/indexer.rs#L61-L67), [crates/gwiki/src/indexer.rs:71-73](crates/gwiki/src/indexer.rs#L71-L73), [crates/gwiki/src/indexer.rs:77-79](crates/gwiki/src/indexer.rs#L77-L79), [crates/gwiki/src/indexer.rs:82-87](crates/gwiki/src/indexer.rs#L82-L87), [crates/gwiki/src/indexer.rs:89-148](crates/gwiki/src/indexer.rs#L89-L148), [crates/gwiki/src/indexer.rs:150-155](crates/gwiki/src/indexer.rs#L150-L155), [crates/gwiki/src/indexer.rs:157-197](crates/gwiki/src/indexer.rs#L157-L197), [crates/gwiki/src/indexer.rs:199-236](crates/gwiki/src/indexer.rs#L199-L236), [crates/gwiki/src/indexer.rs:238-249](crates/gwiki/src/indexer.rs#L238-L249), [crates/gwiki/src/indexer.rs:251-264](crates/gwiki/src/indexer.rs#L251-L264), [crates/gwiki/src/indexer.rs:266-273](crates/gwiki/src/indexer.rs#L266-L273), [crates/gwiki/src/indexer.rs:275-280](crates/gwiki/src/indexer.rs#L275-L280), [crates/gwiki/src/indexer.rs:282-324](crates/gwiki/src/indexer.rs#L282-L324), [crates/gwiki/src/indexer.rs:326-355](crates/gwiki/src/indexer.rs#L326-L355), [crates/gwiki/src/indexer.rs:357-369](crates/gwiki/src/indexer.rs#L357-L369), [crates/gwiki/src/indexer.rs:371-373](crates/gwiki/src/indexer.rs#L371-L373), [crates/gwiki/src/indexer.rs:375-379](crates/gwiki/src/indexer.rs#L375-L379), [crates/gwiki/src/indexer.rs:381-394](crates/gwiki/src/indexer.rs#L381-L394), [crates/gwiki/src/indexer.rs:407-413](crates/gwiki/src/indexer.rs#L407-L413), [crates/gwiki/src/indexer.rs:415-448](crates/gwiki/src/indexer.rs#L415-L448), [crates/gwiki/src/indexer.rs:451-468](crates/gwiki/src/indexer.rs#L451-L468), [crates/gwiki/src/indexer.rs:471-509](crates/gwiki/src/indexer.rs#L471-L509), [crates/gwiki/src/indexer.rs:512-534](crates/gwiki/src/indexer.rs#L512-L534), [crates/gwiki/src/indexer.rs:537-561](crates/gwiki/src/indexer.rs#L537-L561), [crates/gwiki/src/indexer.rs:564-594](crates/gwiki/src/indexer.rs#L564-L594), [crates/gwiki/src/indexer.rs:597-617](crates/gwiki/src/indexer.rs#L597-L617), [crates/gwiki/src/indexer.rs:620-650](crates/gwiki/src/indexer.rs#L620-L650), [crates/gwiki/src/indexer.rs:653-686](crates/gwiki/src/indexer.rs#L653-L686), [crates/gwiki/src/indexer.rs:689-702](crates/gwiki/src/indexer.rs#L689-L702)

</details>

# crates/gwiki/src/indexer.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements wiki-vault indexing into a `WikiIndexStore`: `IndexOptions` controls traversal behavior, `IndexError` wraps I/O, walk, store, path, and memory-limit failures, and `index_vault`/`index_vault_with_options` drive the full scan. The helpers break that work into finding indexable files, validating vault paths, parsing wiki documents and markdown headings/links into chunks and derived rows, and writing documents, chunks, links, sources, and ingestions back to the store. The test functions exercise the main guarantees: gitignore handling, deleted-file cleanup, immutable raw sources, skipping unchanged files, codedoc provenance, unified code-root indexing, idempotency, and memory-limit rejection.
[crates/gwiki/src/indexer.rs:16-18]
[crates/gwiki/src/indexer.rs:21-25]
[crates/gwiki/src/indexer.rs:29-35]
[crates/gwiki/src/indexer.rs:38-57]
[crates/gwiki/src/indexer.rs:61-67]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IndexOptions` | class | `pub struct IndexOptions {` | `IndexOptions [class]` | `4c0b2412-48bc-5519-b681-b25e7c1381f4` | 16-18 [crates/gwiki/src/indexer.rs:16-18] | Indexed class `IndexOptions` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:16-18] |
| `IndexOptions::default` | method | `fn default() -> Self {` | `IndexOptions::default [method]` | `d05bc2bb-85a0-51dc-87d9-eeeacd4a0868` | 21-25 [crates/gwiki/src/indexer.rs:21-25] | Indexed method `IndexOptions::default` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:21-25] |
| `IndexError` | type | `pub enum IndexError {` | `IndexError [type]` | `901f70e5-76ce-54e3-8d7c-b2cfff5671e5` | 29-35 [crates/gwiki/src/indexer.rs:29-35] | Indexed type `IndexError` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:29-35] |
| `IndexError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `IndexError::fmt [method]` | `2cccdbc9-38c3-5be8-b21c-7066af4ac7b4` | 38-57 [crates/gwiki/src/indexer.rs:38-57] | Indexed method `IndexError::fmt` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:38-57] |
| `IndexError::source` | method | `fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {` | `IndexError::source [method]` | `a5b3cc15-25f4-5c9c-8f7c-919a12e981f6` | 61-67 [crates/gwiki/src/indexer.rs:61-67] | Indexed method `IndexError::source` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:61-67] |
| `IndexError::from` | method | `fn from(error: StoreError) -> Self {` | `IndexError::from [method]` | `fe5e70bc-0102-59ac-b2d2-f7e411b44584` | 71-73 [crates/gwiki/src/indexer.rs:71-73] | Indexed method `IndexError::from` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:71-73] |
| `IndexError::from` | method | `fn from(error: std::io::Error) -> Self {` | `IndexError::from [method]` | `8daaa8db-7d4b-5157-a3d4-abc0676e44ed` | 77-79 [crates/gwiki/src/indexer.rs:77-79] | Indexed method `IndexError::from` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:77-79] |
| `index_vault` | function | `pub fn index_vault(` | `index_vault [function]` | `084350ac-2f89-55f2-9c57-b19dda5ff561` | 82-87 [crates/gwiki/src/indexer.rs:82-87] | Indexed function `index_vault` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:82-87] |
| `index_vault_with_options` | function | `pub fn index_vault_with_options(` | `index_vault_with_options [function]` | `11e149bf-fa0b-56b6-8c0d-4f729cf32adb` | 89-148 [crates/gwiki/src/indexer.rs:89-148] | Indexed function `index_vault_with_options` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:89-148] |
| `discover_indexable_hashes` | function | `fn discover_indexable_hashes(` | `discover_indexable_hashes [function]` | `70f7cc06-4f06-5527-9155-02dadbab84b6` | 150-155 [crates/gwiki/src/indexer.rs:150-155] | Indexed function `discover_indexable_hashes` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:150-155] |
| `discover_indexable_hashes_with_limit` | function | `fn discover_indexable_hashes_with_limit(` | `discover_indexable_hashes_with_limit [function]` | `e9f3a60e-0d75-51af-843c-d15a25690d51` | 157-197 [crates/gwiki/src/indexer.rs:157-197] | Indexed function `discover_indexable_hashes_with_limit` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:157-197] |
| `index_file` | function | `fn index_file(` | `index_file [function]` | `8a82206b-9853-5e69-9af3-8eeab7750a99` | 199-236 [crates/gwiki/src/indexer.rs:199-236] | Indexed function `index_file` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:199-236] |
| `is_indexable_vault_path` | function | `fn is_indexable_vault_path(path: &Path) -> bool {` | `is_indexable_vault_path [function]` | `454f0e1b-bcd3-5357-9bf8-00d249913589` | 238-249 [crates/gwiki/src/indexer.rs:238-249] | Indexed function `is_indexable_vault_path` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:238-249] |
| `document_kind` | function | `fn document_kind(path: &Path) -> Option<WikiDocumentKind> {` | `document_kind [function]` | `c2ee0a22-adad-5769-9858-850c69430ffb` | 251-264 [crates/gwiki/src/indexer.rs:251-264] | Indexed function `document_kind` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:251-264] |
| `normal_components` | function | `fn normal_components(path: &Path) -> Vec<&str> {` | `normal_components [function]` | `2e59d38a-c236-5562-88e0-26becf1424b4` | 266-273 [crates/gwiki/src/indexer.rs:266-273] | Indexed function `normal_components` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:266-273] |
| `ParsedWikiDocument` | class | `struct ParsedWikiDocument {` | `ParsedWikiDocument [class]` | `16e3cf6a-812e-562b-b582-3c8ef91e9602` | 275-280 [crates/gwiki/src/indexer.rs:275-280] | Indexed class `ParsedWikiDocument` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:275-280] |
| `parse_wiki_document` | function | `fn parse_wiki_document(` | `parse_wiki_document [function]` | `91882ecb-e322-5ec5-ad83-bb17da31747e` | 282-324 [crates/gwiki/src/indexer.rs:282-324] | Indexed function `parse_wiki_document` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:282-324] |
| `chunks_for_markdown` | function | `fn chunks_for_markdown(path: &Path, fallback_heading: Option<String>, body: &str) -> Vec<Chunk> {` | `chunks_for_markdown [function]` | `d6e3ff08-8184-5139-90a6-614c5f7ccdc2` | 326-355 [crates/gwiki/src/indexer.rs:326-355] | Indexed function `chunks_for_markdown` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:326-355] |
| `heading_spans` | function | `fn heading_spans(body: &str) -> Vec<(usize, String)> {` | `heading_spans [function]` | `68efa745-44b7-561e-8f88-15c7ad0928d6` | 357-369 [crates/gwiki/src/indexer.rs:357-369] | Indexed function `heading_spans` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:357-369] |
| `first_heading` | function | `fn first_heading(body: &str) -> Option<String> {` | `first_heading [function]` | `0b45a32f-714e-548a-8fa8-d0e0bca02990` | 371-373 [crates/gwiki/src/indexer.rs:371-373] | Indexed function `first_heading` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:371-373] |
| `parse_heading` | function | `fn parse_heading(line: &str) -> Option<String> {` | `parse_heading [function]` | `a284a042-b745-53fb-b624-89a1b032b168` | 375-379 [crates/gwiki/src/indexer.rs:375-379] | Indexed function `parse_heading` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:375-379] |
| `extract_links` | function | `fn extract_links(path: &Path, body: &str) -> Vec<WikiLink> {` | `extract_links [function]` | `cde72f8a-83cd-59f5-b5ab-2f1f82be9ab3` | 381-394 [crates/gwiki/src/indexer.rs:381-394] | Indexed function `extract_links` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:381-394] |
| `write_file` | function | `fn write_file(root: &Path, relative: &str, contents: &str) {` | `write_file [function]` | `bcd36297-c732-56f1-901f-8002f067116a` | 407-413 [crates/gwiki/src/indexer.rs:407-413] | Indexed function `write_file` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:407-413] |
| `seed_derived_rows` | function | `fn seed_derived_rows(store: &mut MemoryWikiStore, relative: &str) {` | `seed_derived_rows [function]` | `386a32bf-877a-5bac-b8be-37ef0b124c52` | 415-448 [crates/gwiki/src/indexer.rs:415-448] | Indexed function `seed_derived_rows` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:415-448] |
| `index_writer_upserts_documents_chunks_links_sources_and_ingestions` | function | `fn index_writer_upserts_documents_chunks_links_sources_and_ingestions() {` | `index_writer_upserts_documents_chunks_links_sources_and_ingestions [function]` | `d0ec2c8b-fd87-5c6d-b990-d6931dfc8438` | 451-468 [crates/gwiki/src/indexer.rs:451-468] | Indexed function `index_writer_upserts_documents_chunks_links_sources_and_ingestions` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:451-468] |
| `index_vault_respects_gitignore_by_default_and_option` | function | `fn index_vault_respects_gitignore_by_default_and_option() {` | `index_vault_respects_gitignore_by_default_and_option [function]` | `60118c6e-5c3f-58a0-bcdb-97b9fc079fc3` | 471-509 [crates/gwiki/src/indexer.rs:471-509] | Indexed function `index_vault_respects_gitignore_by_default_and_option` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:471-509] |
| `deleted_file_removes_derived_rows_only` | function | `fn deleted_file_removes_derived_rows_only() {` | `deleted_file_removes_derived_rows_only [function]` | `e37773f9-f5aa-55db-af22-5e873ac4a395` | 512-534 [crates/gwiki/src/indexer.rs:512-534] | Indexed function `deleted_file_removes_derived_rows_only` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:512-534] |
| `raw_sources_are_immutable` | function | `fn raw_sources_are_immutable() {` | `raw_sources_are_immutable [function]` | `1c8a74f1-9357-5269-a187-1d3c983a7fb4` | 537-561 [crates/gwiki/src/indexer.rs:537-561] | Indexed function `raw_sources_are_immutable` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:537-561] |
| `unchanged_files_are_skipped` | function | `fn unchanged_files_are_skipped() {` | `unchanged_files_are_skipped [function]` | `fc514bab-383f-5ed7-9cfa-dc7cebcfb999` | 564-594 [crates/gwiki/src/indexer.rs:564-594] | Indexed function `unchanged_files_are_skipped` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:564-594] |
| `indexes_codedocs_with_provenance` | function | `fn indexes_codedocs_with_provenance() {` | `indexes_codedocs_with_provenance [function]` | `7ee93e40-52bc-5348-a205-8344758e6d03` | 597-617 [crates/gwiki/src/indexer.rs:597-617] | Indexed function `indexes_codedocs_with_provenance` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:597-617] |
| `unified_vault_indexes_code_root_wikilinks` | function | `fn unified_vault_indexes_code_root_wikilinks() {` | `unified_vault_indexes_code_root_wikilinks [function]` | `511d17b9-6550-5f9f-948a-8ee679db7405` | 620-650 [crates/gwiki/src/indexer.rs:620-650] | Indexed function `unified_vault_indexes_code_root_wikilinks` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:620-650] |
| `codedoc_tree_indexes_idempotently` | function | `fn codedoc_tree_indexes_idempotently() {` | `codedoc_tree_indexes_idempotently [function]` | `ea2a0fcb-438e-5356-83ac-0ebb8a45fb30` | 653-686 [crates/gwiki/src/indexer.rs:653-686] | Indexed function `codedoc_tree_indexes_idempotently` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:653-686] |
| `memory_index_limit_rejects_large_vaults` | function | `fn memory_index_limit_rejects_large_vaults() {` | `memory_index_limit_rejects_large_vaults [function]` | `e5285059-1154-5c63-b7b8-1e7c53352c9c` | 689-702 [crates/gwiki/src/indexer.rs:689-702] | Indexed function `memory_index_limit_rejects_large_vaults` in `crates/gwiki/src/indexer.rs`. [crates/gwiki/src/indexer.rs:689-702] |
