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

This file maintains compile-time wiki bookkeeping. It updates `_index.md` under an exclusive `.gwiki/index.lock`, creating the “Compiled pages” section if needed and inserting a synthesized page link only once, with small helpers for line/heading detection and Markdown insertion. It also records provenance under a separate `.gwiki/provenance.lock`: it loads or initializes the provenance graph, derives article sections from the article outline or rendered headings, maps source chunks to sections by ordinal, and marks matching source manifest entries as compiled.
[crates/gwiki/src/compile/index.rs:16-63]
[crates/gwiki/src/compile/index.rs:65-94]
[crates/gwiki/src/compile/index.rs:96-98]
[crates/gwiki/src/compile/index.rs:100-102]
[crates/gwiki/src/compile/index.rs:104-106]

## API Symbols

- `update_wiki_index` (function) component `update_wiki_index [function]` (`3f09bb62-7ee3-5979-bcf6-49346dd087f6`) lines 16-63 [crates/gwiki/src/compile/index.rs:16-63]
  - Signature: `pub(crate) fn update_wiki_index(`
  - Purpose: Atomically acquires a wiki index lock under '.gwiki/index.lock', loads or initializes '_index.md', inserts the synthesized article’s wiki link if it is not already present, and writes the updated index back to disk with I/O errors wrapped as 'WikiError::Io'. [crates/gwiki/src/compile/index.rs:16-63]
- `insert_compiled_page_link` (function) component `insert_compiled_page_link [function]` (`db1bb4e7-8492-594b-be39-e60973e9976f`) lines 65-94 [crates/gwiki/src/compile/index.rs:65-94]
  - Signature: `pub(super) fn insert_compiled_page_link(index: &mut String, link: &str) -> Result<(), WikiError> {`
  - Purpose: Ensures the '## Compiled pages' heading exists in the markdown 'index' and inserts a '- {link}' entry into that section, preserving blank-line separation from surrounding content, or returns a 'WikiError::Config' if the heading cannot be located. [crates/gwiki/src/compile/index.rs:65-94]
- `has_compiled_pages_heading` (function) component `has_compiled_pages_heading [function]` (`6e117f33-212e-5617-8922-1f912616373a`) lines 96-98 [crates/gwiki/src/compile/index.rs:96-98]
  - Signature: `fn has_compiled_pages_heading(index: &str) -> bool {`
  - Purpose: Returns 'true' if 'index' contains a line exactly equal to '## Compiled pages', otherwise 'false'. [crates/gwiki/src/compile/index.rs:96-98]
- `has_compiled_page_link` (function) component `has_compiled_page_link [function]` (`8a8fad35-0605-5d7e-8337-77d99e362f64`) lines 100-102 [crates/gwiki/src/compile/index.rs:100-102]
  - Signature: `fn has_compiled_page_link(index: &str, link: &str) -> bool {`
  - Purpose: Returns 'true' if 'index' contains an exact line matching '- {link}', otherwise 'false'. [crates/gwiki/src/compile/index.rs:100-102]
- `has_exact_line` (function) component `has_exact_line [function]` (`43fef494-7f9b-5c21-9f91-260631da5688`) lines 104-106 [crates/gwiki/src/compile/index.rs:104-106]
  - Signature: `fn has_exact_line(markdown: &str, expected: &str) -> bool {`
  - Purpose: Returns 'true' if any line in the 'markdown' string exactly equals 'expected', and 'false' otherwise. [crates/gwiki/src/compile/index.rs:104-106]
- `exact_line_end` (function) component `exact_line_end [function]` (`54ec3ba7-27d4-5900-bbae-9b4a1e506977`) lines 108-117 [crates/gwiki/src/compile/index.rs:108-117]
  - Signature: `fn exact_line_end(markdown: &str, expected: &str) -> Option<usize> {`
  - Purpose: Returns the byte index immediately after the first line in 'markdown' whose content, excluding its trailing newline via 'line_body', exactly matches 'expected', or 'None' if no such line exists. [crates/gwiki/src/compile/index.rs:108-117]
- `next_section_heading_offset` (function) component `next_section_heading_offset [function]` (`8b3a3172-d870-51cb-b0a1-e7eda831e87b`) lines 119-128 [crates/gwiki/src/compile/index.rs:119-128]
  - Signature: `fn next_section_heading_offset(markdown: &str, start: usize) -> Option<usize> {`
  - Purpose: Returns the byte offset of the first line at or after 'start' whose content, after stripping line ending, begins with '## ', or 'None' if no such section heading exists. [crates/gwiki/src/compile/index.rs:119-128]
- `line_body` (function) component `line_body [function]` (`0faa4d12-cb37-582c-bb6a-dbe2dcaf0dba`) lines 130-132 [crates/gwiki/src/compile/index.rs:130-132]
  - Signature: `fn line_body(line: &str) -> &str {`
  - Purpose: Returns the input string with any trailing '\n' and then trailing '\r' characters removed, yielding a slice of the original line body without line terminators. [crates/gwiki/src/compile/index.rs:130-132]
- `write_provenance` (function) component `write_provenance [function]` (`f36d0d54-3863-5836-b84a-0edaf33e8c9c`) lines 134-193 [crates/gwiki/src/compile/index.rs:134-193]
  - Signature: `pub(crate) fn write_provenance(`
  - Purpose: Acquires a provenance lock, loads or initializes the vault’s provenance graph, derives article sections and source manifest records, and records links from each source chunk to its corresponding article section using chunk byte offsets and source IDs. [crates/gwiki/src/compile/index.rs:134-193]
- `lock_provenance` (function) component `lock_provenance [function]` (`db7865d3-9fb4-5d98-8450-105ede1284a4`) lines 195-217 [crates/gwiki/src/compile/index.rs:195-217]
  - Signature: `fn lock_provenance(vault_root: &Path) -> Result<fs::File, WikiError> {`
  - Purpose: Creates the '.gwiki/provenance.lock' file under 'vault_root', ensures its parent directory exists, acquires an exclusive file lock on it, and returns the locked 'fs::File' or maps I/O failures to 'WikiError'. [crates/gwiki/src/compile/index.rs:195-217]
- `provenance_sections` (function) component `provenance_sections [function]` (`0cdc1b36-9f9a-5703-98f9-b28d100c8b57`) lines 219-245 [crates/gwiki/src/compile/index.rs:219-245]
  - Signature: `fn provenance_sections(`
  - Purpose: 'provenance_sections' normalizes a provided outline into non-empty section headings, falls back to headings extracted from the article markdown or '"Overview"' if none exist, and returns a 'Vec<WikiSectionRef>' by pairing each heading with a section ID derived from the article and the cloned 'page_path'. [crates/gwiki/src/compile/index.rs:219-245]
- `section_for_chunk` (function) component `section_for_chunk [function]` (`5893b7f8-395a-5bdd-85c0-76d995757665`) lines 247-250 [crates/gwiki/src/compile/index.rs:247-250]
  - Signature: `fn section_for_chunk(sections: &[WikiSectionRef], chunk_ordinal: usize) -> &WikiSectionRef {`
  - Purpose: Returns a reference to the section at 'chunk_ordinal', clamping the index to the last available section when 'chunk_ordinal' exceeds 'sections.len() - 1'. [crates/gwiki/src/compile/index.rs:247-250]
- `rendered_article_sections` (function) component `rendered_article_sections [function]` (`9576f3de-ea14-55c3-afef-7ea57de8fcef`) lines 252-262 [crates/gwiki/src/compile/index.rs:252-262]
  - Signature: `fn rendered_article_sections(markdown: &str) -> Vec<String> {`
  - Purpose: Returns a 'Vec<String>' containing the non-empty trimmed text of every Markdown line that begins with the level-2 heading prefix '## '. [crates/gwiki/src/compile/index.rs:252-262]
- `section_id_for_article` (function) component `section_id_for_article [function]` (`48930bf4-aeb8-5490-8246-5dc6e2d52f2f`) lines 264-270 [crates/gwiki/src/compile/index.rs:264-270]
  - Signature: `fn section_id_for_article(article: &SynthesizedPage, heading: &str) -> String {`
  - Purpose: Returns a slugified section identifier using the article title for the '"Overview"' heading and the slugified heading text for all other headings. [crates/gwiki/src/compile/index.rs:264-270]
- `mark_sources_compiled` (function) component `mark_sources_compiled [function]` (`5985bdf2-d328-5271-a1d8-08bcd257a73d`) lines 272-290 [crates/gwiki/src/compile/index.rs:272-290]
  - Signature: `pub(crate) fn mark_sources_compiled(`
  - Purpose: Updates the source manifest under 'vault_root', marking any entries whose paths match one of 'source_paths' as 'CompileStatus::Compiled' if they are not already compiled, and persists the change only when at least one entry was modified. [crates/gwiki/src/compile/index.rs:272-290]
- `lock_wiki_index` (function) component `lock_wiki_index [function]` (`3e28f071-5dc8-5415-9b48-aaa3380f0f1a`) lines 292-294 [crates/gwiki/src/compile/index.rs:292-294]
  - Signature: `fn lock_wiki_index(lock: &fs::File, lock_path: &Path) -> Result<(), WikiError> {`
  - Purpose: Acquires an index lock by delegating to 'lock_file(lock, lock_path, "lock wiki index")' and returns its 'Result<(), WikiError>'. [crates/gwiki/src/compile/index.rs:292-294]
- `lock_file` (function) component `lock_file [function]` (`5d6965b3-4153-5c8a-b169-a6dc4aa91374`) lines 296-330 [crates/gwiki/src/compile/index.rs:296-330]
  - Signature: `fn lock_file(lock: &fs::File, lock_path: &Path, action: &'static str) -> Result<(), WikiError> {`
  - Purpose: 'lock_file' repeatedly attempts to acquire an exclusive 'fs4' lock on the given file, sleeping in short intervals until either the lock succeeds, a non-'WouldBlock' error occurs, or the configured timeout elapses and it returns a timed-out 'WikiError::Io' for the lock path. [crates/gwiki/src/compile/index.rs:296-330]
- `insert_compiled_page_link_creates_missing_section` (function) component `insert_compiled_page_link_creates_missing_section [function]` (`c8247e83-3fee-5dcb-8ade-4ad5fafd9c11`) lines 337-344 [crates/gwiki/src/compile/index.rs:337-344]
  - Signature: `fn insert_compiled_page_link_creates_missing_section() {`
  - Purpose: Verifies that 'insert_compiled_page_link' inserts '`[[Compiled/Page]]`' under a newly created '## Compiled pages' section in the index while leaving the existing '## Notes' section intact. [crates/gwiki/src/compile/index.rs:337-344]

