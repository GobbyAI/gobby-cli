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
  - 134-193
  - 195-217
  - 219-245
  - 247-250
  - 252-262
  - 264-270
  - 272-290
  - 292-294
  - 296-330
  - 337-344
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile/index.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Purpose

This file updates the generated wiki index and manages the bookkeeping around compiled content. `update_wiki_index` acquires an index lock, loads or initializes `_index.md`, and ensures the compiled article is linked under a “Compiled pages” section by using the link/heading helpers. The rest of the module supports provenance and synchronization: it writes provenance sections for source chunks, maps chunks and articles to stable section IDs, marks sources as compiled, and uses file and index locks to prevent concurrent edits while compiling.
[crates/gwiki/src/compile/index.rs:16-63]
[crates/gwiki/src/compile/index.rs:65-94]
[crates/gwiki/src/compile/index.rs:96-98]
[crates/gwiki/src/compile/index.rs:100-102]
[crates/gwiki/src/compile/index.rs:104-106]

## API Symbols

- `update_wiki_index` (function) component `update_wiki_index [function]` (`3f09bb62-7ee3-5979-bcf6-49346dd087f6`) lines 16-63 [crates/gwiki/src/compile/index.rs:16-63]
  - Signature: `pub(crate) fn update_wiki_index(`
  - Purpose: Indexed function `update_wiki_index` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:16-63]
- `insert_compiled_page_link` (function) component `insert_compiled_page_link [function]` (`db1bb4e7-8492-594b-be39-e60973e9976f`) lines 65-94 [crates/gwiki/src/compile/index.rs:65-94]
  - Signature: `pub(super) fn insert_compiled_page_link(index: &mut String, link: &str) -> Result<(), WikiError> {`
  - Purpose: Indexed function `insert_compiled_page_link` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:65-94]
- `has_compiled_pages_heading` (function) component `has_compiled_pages_heading [function]` (`6e117f33-212e-5617-8922-1f912616373a`) lines 96-98 [crates/gwiki/src/compile/index.rs:96-98]
  - Signature: `fn has_compiled_pages_heading(index: &str) -> bool {`
  - Purpose: Indexed function `has_compiled_pages_heading` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:96-98]
- `has_compiled_page_link` (function) component `has_compiled_page_link [function]` (`8a8fad35-0605-5d7e-8337-77d99e362f64`) lines 100-102 [crates/gwiki/src/compile/index.rs:100-102]
  - Signature: `fn has_compiled_page_link(index: &str, link: &str) -> bool {`
  - Purpose: Indexed function `has_compiled_page_link` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:100-102]
- `has_exact_line` (function) component `has_exact_line [function]` (`43fef494-7f9b-5c21-9f91-260631da5688`) lines 104-106 [crates/gwiki/src/compile/index.rs:104-106]
  - Signature: `fn has_exact_line(markdown: &str, expected: &str) -> bool {`
  - Purpose: Indexed function `has_exact_line` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:104-106]
- `exact_line_end` (function) component `exact_line_end [function]` (`54ec3ba7-27d4-5900-bbae-9b4a1e506977`) lines 108-117 [crates/gwiki/src/compile/index.rs:108-117]
  - Signature: `fn exact_line_end(markdown: &str, expected: &str) -> Option<usize> {`
  - Purpose: Indexed function `exact_line_end` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:108-117]
- `next_section_heading_offset` (function) component `next_section_heading_offset [function]` (`8b3a3172-d870-51cb-b0a1-e7eda831e87b`) lines 119-128 [crates/gwiki/src/compile/index.rs:119-128]
  - Signature: `fn next_section_heading_offset(markdown: &str, start: usize) -> Option<usize> {`
  - Purpose: Indexed function `next_section_heading_offset` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:119-128]
- `line_body` (function) component `line_body [function]` (`0faa4d12-cb37-582c-bb6a-dbe2dcaf0dba`) lines 130-132 [crates/gwiki/src/compile/index.rs:130-132]
  - Signature: `fn line_body(line: &str) -> &str {`
  - Purpose: Indexed function `line_body` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:130-132]
- `write_provenance` (function) component `write_provenance [function]` (`f36d0d54-3863-5836-b84a-0edaf33e8c9c`) lines 134-193 [crates/gwiki/src/compile/index.rs:134-193]
  - Signature: `pub(crate) fn write_provenance(`
  - Purpose: Indexed function `write_provenance` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:134-193]
- `lock_provenance` (function) component `lock_provenance [function]` (`db7865d3-9fb4-5d98-8450-105ede1284a4`) lines 195-217 [crates/gwiki/src/compile/index.rs:195-217]
  - Signature: `fn lock_provenance(vault_root: &Path) -> Result<fs::File, WikiError> {`
  - Purpose: Indexed function `lock_provenance` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:195-217]
- `provenance_sections` (function) component `provenance_sections [function]` (`0cdc1b36-9f9a-5703-98f9-b28d100c8b57`) lines 219-245 [crates/gwiki/src/compile/index.rs:219-245]
  - Signature: `fn provenance_sections(`
  - Purpose: Indexed function `provenance_sections` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:219-245]
- `section_for_chunk` (function) component `section_for_chunk [function]` (`5893b7f8-395a-5bdd-85c0-76d995757665`) lines 247-250 [crates/gwiki/src/compile/index.rs:247-250]
  - Signature: `fn section_for_chunk(sections: &[WikiSectionRef], chunk_ordinal: usize) -> &WikiSectionRef {`
  - Purpose: Indexed function `section_for_chunk` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:247-250]
- `rendered_article_sections` (function) component `rendered_article_sections [function]` (`9576f3de-ea14-55c3-afef-7ea57de8fcef`) lines 252-262 [crates/gwiki/src/compile/index.rs:252-262]
  - Signature: `fn rendered_article_sections(markdown: &str) -> Vec<String> {`
  - Purpose: Indexed function `rendered_article_sections` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:252-262]
- `section_id_for_article` (function) component `section_id_for_article [function]` (`48930bf4-aeb8-5490-8246-5dc6e2d52f2f`) lines 264-270 [crates/gwiki/src/compile/index.rs:264-270]
  - Signature: `fn section_id_for_article(article: &SynthesizedPage, heading: &str) -> String {`
  - Purpose: Indexed function `section_id_for_article` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:264-270]
- `mark_sources_compiled` (function) component `mark_sources_compiled [function]` (`5985bdf2-d328-5271-a1d8-08bcd257a73d`) lines 272-290 [crates/gwiki/src/compile/index.rs:272-290]
  - Signature: `pub(crate) fn mark_sources_compiled(`
  - Purpose: Indexed function `mark_sources_compiled` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:272-290]
- `lock_wiki_index` (function) component `lock_wiki_index [function]` (`3e28f071-5dc8-5415-9b48-aaa3380f0f1a`) lines 292-294 [crates/gwiki/src/compile/index.rs:292-294]
  - Signature: `fn lock_wiki_index(lock: &fs::File, lock_path: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `lock_wiki_index` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:292-294]
- `lock_file` (function) component `lock_file [function]` (`5d6965b3-4153-5c8a-b169-a6dc4aa91374`) lines 296-330 [crates/gwiki/src/compile/index.rs:296-330]
  - Signature: `fn lock_file(lock: &fs::File, lock_path: &Path, action: &'static str) -> Result<(), WikiError> {`
  - Purpose: Indexed function `lock_file` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:296-330]
- `insert_compiled_page_link_creates_missing_section` (function) component `insert_compiled_page_link_creates_missing_section [function]` (`c8247e83-3fee-5dcb-8ade-4ad5fafd9c11`) lines 337-344 [crates/gwiki/src/compile/index.rs:337-344]
  - Signature: `fn insert_compiled_page_link_creates_missing_section() {`
  - Purpose: Indexed function `insert_compiled_page_link_creates_missing_section` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:337-344]

