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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/compile/index.rs:16-63](crates/gwiki/src/compile/index.rs#L16-L63), [crates/gwiki/src/compile/index.rs:65-94](crates/gwiki/src/compile/index.rs#L65-L94), [crates/gwiki/src/compile/index.rs:96-98](crates/gwiki/src/compile/index.rs#L96-L98), [crates/gwiki/src/compile/index.rs:100-102](crates/gwiki/src/compile/index.rs#L100-L102), [crates/gwiki/src/compile/index.rs:104-106](crates/gwiki/src/compile/index.rs#L104-L106), [crates/gwiki/src/compile/index.rs:108-117](crates/gwiki/src/compile/index.rs#L108-L117), [crates/gwiki/src/compile/index.rs:119-128](crates/gwiki/src/compile/index.rs#L119-L128), [crates/gwiki/src/compile/index.rs:130-132](crates/gwiki/src/compile/index.rs#L130-L132), [crates/gwiki/src/compile/index.rs:134-193](crates/gwiki/src/compile/index.rs#L134-L193), [crates/gwiki/src/compile/index.rs:195-217](crates/gwiki/src/compile/index.rs#L195-L217), [crates/gwiki/src/compile/index.rs:219-245](crates/gwiki/src/compile/index.rs#L219-L245), [crates/gwiki/src/compile/index.rs:247-250](crates/gwiki/src/compile/index.rs#L247-L250), [crates/gwiki/src/compile/index.rs:252-262](crates/gwiki/src/compile/index.rs#L252-L262), [crates/gwiki/src/compile/index.rs:264-270](crates/gwiki/src/compile/index.rs#L264-L270), [crates/gwiki/src/compile/index.rs:272-290](crates/gwiki/src/compile/index.rs#L272-L290), [crates/gwiki/src/compile/index.rs:292-294](crates/gwiki/src/compile/index.rs#L292-L294), [crates/gwiki/src/compile/index.rs:296-330](crates/gwiki/src/compile/index.rs#L296-L330), [crates/gwiki/src/compile/index.rs:337-344](crates/gwiki/src/compile/index.rs#L337-L344)

</details>

# crates/gwiki/src/compile/index.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file maintains the wiki’s compiled-page index and related provenance bookkeeping. `update_wiki_index` acquires an index lock, loads or initializes `_index.md`, and ensures the current synthesized page is listed under a “Compiled pages” section. The helper functions handle detecting and inserting headings and page links, finding line and section boundaries, writing provenance sections for source chunks and rendered articles, marking sources as compiled, and providing file-level locks to keep index and provenance updates consistent.
[crates/gwiki/src/compile/index.rs:16-63]
[crates/gwiki/src/compile/index.rs:65-94]
[crates/gwiki/src/compile/index.rs:96-98]
[crates/gwiki/src/compile/index.rs:100-102]
[crates/gwiki/src/compile/index.rs:104-106]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `update_wiki_index` | function | `pub(crate) fn update_wiki_index(` | `update_wiki_index [function]` | `3f09bb62-7ee3-5979-bcf6-49346dd087f6` | 16-63 [crates/gwiki/src/compile/index.rs:16-63] | Indexed function `update_wiki_index` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:16-63] |
| `insert_compiled_page_link` | function | `pub(super) fn insert_compiled_page_link(index: &mut String, link: &str) -> Result<(), WikiError> {` | `insert_compiled_page_link [function]` | `db1bb4e7-8492-594b-be39-e60973e9976f` | 65-94 [crates/gwiki/src/compile/index.rs:65-94] | Indexed function `insert_compiled_page_link` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:65-94] |
| `has_compiled_pages_heading` | function | `fn has_compiled_pages_heading(index: &str) -> bool {` | `has_compiled_pages_heading [function]` | `6e117f33-212e-5617-8922-1f912616373a` | 96-98 [crates/gwiki/src/compile/index.rs:96-98] | Indexed function `has_compiled_pages_heading` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:96-98] |
| `has_compiled_page_link` | function | `fn has_compiled_page_link(index: &str, link: &str) -> bool {` | `has_compiled_page_link [function]` | `8a8fad35-0605-5d7e-8337-77d99e362f64` | 100-102 [crates/gwiki/src/compile/index.rs:100-102] | Indexed function `has_compiled_page_link` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:100-102] |
| `has_exact_line` | function | `fn has_exact_line(markdown: &str, expected: &str) -> bool {` | `has_exact_line [function]` | `43fef494-7f9b-5c21-9f91-260631da5688` | 104-106 [crates/gwiki/src/compile/index.rs:104-106] | Indexed function `has_exact_line` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:104-106] |
| `exact_line_end` | function | `fn exact_line_end(markdown: &str, expected: &str) -> Option<usize> {` | `exact_line_end [function]` | `54ec3ba7-27d4-5900-bbae-9b4a1e506977` | 108-117 [crates/gwiki/src/compile/index.rs:108-117] | Indexed function `exact_line_end` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:108-117] |
| `next_section_heading_offset` | function | `fn next_section_heading_offset(markdown: &str, start: usize) -> Option<usize> {` | `next_section_heading_offset [function]` | `8b3a3172-d870-51cb-b0a1-e7eda831e87b` | 119-128 [crates/gwiki/src/compile/index.rs:119-128] | Indexed function `next_section_heading_offset` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:119-128] |
| `line_body` | function | `fn line_body(line: &str) -> &str {` | `line_body [function]` | `0faa4d12-cb37-582c-bb6a-dbe2dcaf0dba` | 130-132 [crates/gwiki/src/compile/index.rs:130-132] | Indexed function `line_body` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:130-132] |
| `write_provenance` | function | `pub(crate) fn write_provenance(` | `write_provenance [function]` | `f36d0d54-3863-5836-b84a-0edaf33e8c9c` | 134-193 [crates/gwiki/src/compile/index.rs:134-193] | Indexed function `write_provenance` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:134-193] |
| `lock_provenance` | function | `fn lock_provenance(vault_root: &Path) -> Result<fs::File, WikiError> {` | `lock_provenance [function]` | `db7865d3-9fb4-5d98-8450-105ede1284a4` | 195-217 [crates/gwiki/src/compile/index.rs:195-217] | Indexed function `lock_provenance` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:195-217] |
| `provenance_sections` | function | `fn provenance_sections(` | `provenance_sections [function]` | `0cdc1b36-9f9a-5703-98f9-b28d100c8b57` | 219-245 [crates/gwiki/src/compile/index.rs:219-245] | Indexed function `provenance_sections` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:219-245] |
| `section_for_chunk` | function | `fn section_for_chunk(sections: &[WikiSectionRef], chunk_ordinal: usize) -> &WikiSectionRef {` | `section_for_chunk [function]` | `5893b7f8-395a-5bdd-85c0-76d995757665` | 247-250 [crates/gwiki/src/compile/index.rs:247-250] | Indexed function `section_for_chunk` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:247-250] |
| `rendered_article_sections` | function | `fn rendered_article_sections(markdown: &str) -> Vec<String> {` | `rendered_article_sections [function]` | `9576f3de-ea14-55c3-afef-7ea57de8fcef` | 252-262 [crates/gwiki/src/compile/index.rs:252-262] | Indexed function `rendered_article_sections` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:252-262] |
| `section_id_for_article` | function | `fn section_id_for_article(article: &SynthesizedPage, heading: &str) -> String {` | `section_id_for_article [function]` | `48930bf4-aeb8-5490-8246-5dc6e2d52f2f` | 264-270 [crates/gwiki/src/compile/index.rs:264-270] | Indexed function `section_id_for_article` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:264-270] |
| `mark_sources_compiled` | function | `pub(crate) fn mark_sources_compiled(` | `mark_sources_compiled [function]` | `5985bdf2-d328-5271-a1d8-08bcd257a73d` | 272-290 [crates/gwiki/src/compile/index.rs:272-290] | Indexed function `mark_sources_compiled` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:272-290] |
| `lock_wiki_index` | function | `fn lock_wiki_index(lock: &fs::File, lock_path: &Path) -> Result<(), WikiError> {` | `lock_wiki_index [function]` | `3e28f071-5dc8-5415-9b48-aaa3380f0f1a` | 292-294 [crates/gwiki/src/compile/index.rs:292-294] | Indexed function `lock_wiki_index` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:292-294] |
| `lock_file` | function | `fn lock_file(lock: &fs::File, lock_path: &Path, action: &'static str) -> Result<(), WikiError> {` | `lock_file [function]` | `5d6965b3-4153-5c8a-b169-a6dc4aa91374` | 296-330 [crates/gwiki/src/compile/index.rs:296-330] | Indexed function `lock_file` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:296-330] |
| `insert_compiled_page_link_creates_missing_section` | function | `fn insert_compiled_page_link_creates_missing_section() {` | `insert_compiled_page_link_creates_missing_section [function]` | `c8247e83-3fee-5dcb-8ade-4ad5fafd9c11` | 337-344 [crates/gwiki/src/compile/index.rs:337-344] | Indexed function `insert_compiled_page_link_creates_missing_section` in `crates/gwiki/src/compile/index.rs`. [crates/gwiki/src/compile/index.rs:337-344] |
