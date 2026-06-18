---
title: crates/gwiki/src/compile/index.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/index.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile/index.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/compile/index.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gwiki/src/compile/index.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `update_wiki_index` | function | Ensures the wiki index file exists, acquires an index lock, reads or initializes '_index.md', inserts the synthesized article’s link if missing, and writes the updated index back to disk. [crates/gwiki/src/compile/index.rs:16-63] |
| `insert_compiled_page_link` | function | Ensures the '## Compiled pages' section exists in the wiki index and inserts a '- {link}' entry at the end of that section, preserving blank-line separation and returning a 'WikiError::Config' if the heading cannot be located. [crates/gwiki/src/compile/index.rs:65-94] |
| `has_compiled_pages_heading` | function | Returns 'true' if 'index' contains a line that exactly matches '## Compiled pages', otherwise 'false'. [crates/gwiki/src/compile/index.rs:96-98] |
| `has_compiled_page_link` | function | Returns 'true' if 'index' contains an exact line matching '- {link}', otherwise 'false'. [crates/gwiki/src/compile/index.rs:100-102] |
| `has_exact_line` | function | Returns 'true' if any line in 'markdown' is exactly equal to 'expected', otherwise 'false'. [crates/gwiki/src/compile/index.rs:104-106] |
| `exact_line_end` | function | Returns the byte offset immediately after the first line in 'markdown' whose body matches 'expected' exactly, or 'None' if no such line exists. [crates/gwiki/src/compile/index.rs:108-117] |
| `next_section_heading_offset` | function | Returns the byte offset of the first line at or after 'start' whose trimmed line body begins with '## ', or 'None' if no such level-2 heading appears in the remaining markdown. [crates/gwiki/src/compile/index.rs:119-128] |
| `line_body` | function | Returns the input string with any trailing '\n' and then trailing '\r' characters removed from the end, yielding a '&str' slice of the line body. [crates/gwiki/src/compile/index.rs:130-132] |
| `write_provenance` | function | Acquires the provenance lock, loads or initializes the vault’s provenance graph, resolves source IDs and chunk byte ranges, and records provenance links from each accepted source chunk to the corresponding synthesized article section in 'meta/provenance.json'. [crates/gwiki/src/compile/index.rs:134-193] |
| `lock_provenance` | function | Creates the provenance lock file under 'vault_root/STATE_ROOT/provenance.lock', ensures its parent directory exists, opens it for read/write without truncation, acquires an exclusive file lock via 'lock_file', and returns the locked 'fs::File' or a mapped 'WikiError' on I/O failure. [crates/gwiki/src/compile/index.rs:195-219] |
| `provenance_sections` | function | Builds a list of 'WikiSectionRef' values for a page by normalizing non-empty outline headings, falling back to headings parsed from the article markdown or to a default '"Overview"' section, and assigning each section a computed 'section_id' plus the cloned 'page_path'. [crates/gwiki/src/compile/index.rs:221-247] |
| `section_for_chunk` | function | Returns the 'WikiSectionRef' at 'chunk_ordinal', clamping the index to the last available section with 'min' and 'saturating_sub(1)' so it never indexes past the end of 'sections'. [crates/gwiki/src/compile/index.rs:249-252] |
| `rendered_article_sections` | function | Extracts all non-empty level-2 Markdown headings ('## ' prefixes) from the input text, trims surrounding whitespace, and returns them as a 'Vec<String>'. [crates/gwiki/src/compile/index.rs:254-264] |
| `section_id_for_article` | function | Returns a slugified section ID based on 'article.title' when 'heading' is '"Overview"', otherwise returns the slugified 'heading' string. [crates/gwiki/src/compile/index.rs:266-272] |
| `mark_sources_compiled` | function | Marks any manifest entries whose recorded source path matches one of the given 'source_paths' as 'CompileStatus::Compiled', and persists the manifest update only if at least one entry changed. [crates/gwiki/src/compile/index.rs:274-292] |
| `lock_wiki_index` | function | Delegates to 'lock_file' to acquire a file lock for the wiki index at 'lock_path', returning 'Ok(())' or a 'WikiError'. [crates/gwiki/src/compile/index.rs:294-296] |
| `lock_file` | function | 'lock_file' repeatedly attempts to acquire an exclusive 'fs4' lock on 'lock' until success or 'index_lock_timeout()' elapses, returning 'Ok(())' on success and otherwise mapping timeout or lock-acquisition errors into 'WikiError::Io' annotated with 'action' and 'lock_path'. [crates/gwiki/src/compile/index.rs:298-332] |
| `insert_compiled_page_link_creates_missing_section` | function | Verifies that 'insert_compiled_page_link' adds a missing '## Compiled pages' section containing the new compiled page link without disturbing existing sections. [crates/gwiki/src/compile/index.rs:339-346] |

