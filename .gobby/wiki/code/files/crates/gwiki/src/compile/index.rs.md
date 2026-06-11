---
title: crates/gwiki/src/compile/index.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/index.rs
  ranges:
  - 16-63
  - 65-94
  - 96-98
  - 100-102
  - 104-106
  - 108-117
  - 119-128
  - 130-132
  - 134-197
  - 199-221
  - 223-230
  - 232-250
  - 252-254
  - 256-290
  - 297-304
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile/index.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Purpose

`crates/gwiki/src/compile/index.rs` exposes 15 indexed API symbols.
[crates/gwiki/src/compile/index.rs:16-63]
[crates/gwiki/src/compile/index.rs:65-94]
[crates/gwiki/src/compile/index.rs:96-98]
[crates/gwiki/src/compile/index.rs:100-102]
[crates/gwiki/src/compile/index.rs:104-106]

## API Symbols

- `update_wiki_index` (function) component `update_wiki_index [function]` (`3f09bb62-7ee3-5979-bcf6-49346dd087f6`) lines 16-63 [crates/gwiki/src/compile/index.rs:16-63]
  - Signature: `pub(crate) fn update_wiki_index(`
  - Purpose: Atomically updates the wiki index file by adding a wiki link for the provided article if not already present, using file-based locking for synchronization. [crates/gwiki/src/compile/index.rs:16-63]
- `insert_compiled_page_link` (function) component `insert_compiled_page_link [function]` (`db1bb4e7-8492-594b-be39-e60973e9976f`) lines 65-94 [crates/gwiki/src/compile/index.rs:65-94]
  - Signature: `pub(super) fn insert_compiled_page_link(index: &mut String, link: &str) -> Result<(), WikiError> {`
  - Purpose: Appends a markdown-formatted link entry to a wiki index's `## Compiled pages` section, automatically creating the section with proper formatting if absent. [crates/gwiki/src/compile/index.rs:65-94]
- `has_compiled_pages_heading` (function) component `has_compiled_pages_heading [function]` (`6e117f33-212e-5617-8922-1f912616373a`) lines 96-98 [crates/gwiki/src/compile/index.rs:96-98]
  - Signature: `fn has_compiled_pages_heading(index: &str) -> bool {`
  - Purpose: Returns `true` if the input string contains an exact line matching the markdown heading `## Compiled pages`, otherwise `false`. [crates/gwiki/src/compile/index.rs:96-98]
- `has_compiled_page_link` (function) component `has_compiled_page_link [function]` (`8a8fad35-0605-5d7e-8337-77d99e362f64`) lines 100-102 [crates/gwiki/src/compile/index.rs:100-102]
  - Signature: `fn has_compiled_page_link(index: &str, link: &str) -> bool {`
  - Purpose: This function returns true if the index string contains an exact line matching the provided link formatted as a markdown list item (`- {link}`). [crates/gwiki/src/compile/index.rs:100-102]
- `has_exact_line` (function) component `has_exact_line [function]` (`43fef494-7f9b-5c21-9f91-260631da5688`) lines 104-106 [crates/gwiki/src/compile/index.rs:104-106]
  - Signature: `fn has_exact_line(markdown: &str, expected: &str) -> bool {`
  - Purpose: The function returns `true` if any line in the markdown string exactly matches the expected string, otherwise `false`. [crates/gwiki/src/compile/index.rs:104-106]
- `exact_line_end` (function) component `exact_line_end [function]` (`54ec3ba7-27d4-5900-bbae-9b4a1e506977`) lines 108-117 [crates/gwiki/src/compile/index.rs:108-117]
  - Signature: `fn exact_line_end(markdown: &str, expected: &str) -> Option<usize> {`
  - Purpose: Returns the byte offset immediately after the first line in markdown whose body equals expected, or None if no match is found. [crates/gwiki/src/compile/index.rs:108-117]
- `next_section_heading_offset` (function) component `next_section_heading_offset [function]` (`8b3a3172-d870-51cb-b0a1-e7eda831e87b`) lines 119-128 [crates/gwiki/src/compile/index.rs:119-128]
  - Signature: `fn next_section_heading_offset(markdown: &str, start: usize) -> Option<usize> {`
  - Purpose: Returns the byte offset of the first markdown level 2 heading (`## `) at or after the given start position, or `None` if none exists. [crates/gwiki/src/compile/index.rs:119-128]
- `line_body` (function) component `line_body [function]` (`0faa4d12-cb37-582c-bb6a-dbe2dcaf0dba`) lines 130-132 [crates/gwiki/src/compile/index.rs:130-132]
  - Signature: `fn line_body(line: &str) -> &str {`
  - Purpose: Removes trailing newline (`\n`) and carriage return (`\r`) characters from a string slice. [crates/gwiki/src/compile/index.rs:130-132]
- `write_provenance` (function) component `write_provenance [function]` (`f36d0d54-3863-5836-b84a-0edaf33e8c9c`) lines 134-197 [crates/gwiki/src/compile/index.rs:134-197]
  - Signature: `pub(crate) fn write_provenance(`
  - Purpose: This function records provenance metadata by loading or initializing a ProvenanceGraph and adding ProvenanceLinks that map source document chunks to sections of a synthesized wiki article. [crates/gwiki/src/compile/index.rs:134-197]
- `lock_provenance` (function) component `lock_provenance [function]` (`80e78fc1-fb42-57ad-a1d4-18719d825b54`) lines 199-221 [crates/gwiki/src/compile/index.rs:199-221]
  - Signature: `fn lock_provenance(vault_root: &Path) -> Result<fs::File, WikiError> {`
  - Purpose: Creates and acquires a file lock on the provenance lock file at `vault_root/.gwiki/provenance.lock`, returning the locked file handle. [crates/gwiki/src/compile/index.rs:199-221]
- `first_rendered_article_section` (function) component `first_rendered_article_section [function]` (`31f9fae1-6ee0-5d4b-b604-491003baed5c`) lines 223-230 [crates/gwiki/src/compile/index.rs:223-230]
  - Signature: `fn first_rendered_article_section(markdown: &str) -> Option<String> {`
  - Purpose: Extracts and returns the trimmed text content of the first Markdown level-2 heading (##) as an `Option<String>`, or `None` if no such heading exists. [crates/gwiki/src/compile/index.rs:223-230]
- `mark_sources_compiled` (function) component `mark_sources_compiled [function]` (`bfe33f1b-15af-5af6-ae2e-11e405e0daaa`) lines 232-250 [crates/gwiki/src/compile/index.rs:232-250]
  - Signature: `pub(crate) fn mark_sources_compiled(`
  - Purpose: Updates the source manifest to mark all entries matching the provided source paths with `CompileStatus::Compiled` if not already compiled. [crates/gwiki/src/compile/index.rs:232-250]
- `lock_wiki_index` (function) component `lock_wiki_index [function]` (`8826b932-6250-5299-a37c-e218d8fdb489`) lines 252-254 [crates/gwiki/src/compile/index.rs:252-254]
  - Signature: `fn lock_wiki_index(lock: &fs::File, lock_path: &Path) -> Result<(), WikiError> {`
  - Purpose: Acquires an exclusive lock on the wiki index by delegating to the `lock_file` function with the provided file handle and lock path. [crates/gwiki/src/compile/index.rs:252-254]
- `lock_file` (function) component `lock_file [function]` (`69699489-4263-5e02-9dbc-56f81d56c6fc`) lines 256-290 [crates/gwiki/src/compile/index.rs:256-290]
  - Signature: `fn lock_file(lock: &fs::File, lock_path: &Path, action: &'static str) -> Result<(), WikiError> {`
  - Purpose: Acquires an exclusive file lock with a configurable timeout, retrying at 25ms intervals until either successful or the timeout elapses. [crates/gwiki/src/compile/index.rs:256-290]
- `insert_compiled_page_link_creates_missing_section` (function) component `insert_compiled_page_link_creates_missing_section [function]` (`f8472fe5-12c1-50ed-ab41-189036a30911`) lines 297-304 [crates/gwiki/src/compile/index.rs:297-304]
  - Signature: `fn insert_compiled_page_link_creates_missing_section() {`
  - Purpose: Tests that `insert_compiled_page_link` dynamically creates a missing "Compiled pages" section in the wiki index while preserving existing sections. [crates/gwiki/src/compile/index.rs:297-304]

