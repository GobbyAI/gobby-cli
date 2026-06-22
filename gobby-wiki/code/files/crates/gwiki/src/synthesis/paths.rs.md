---
title: crates/gwiki/src/synthesis/paths.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/paths.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis/paths.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/synthesis/paths.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gwiki/src/synthesis/paths.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ensure_synthesized_path_inside_vault` | function | Resolves the vault root and a synthesized candidate path, canonicalizes the candidate’s existing prefix, and returns an error unless the resulting path is strictly inside the vault root with no '..', root, or platform prefix components. [crates/gwiki/src/synthesis/paths.rs:10-38] |
| `canonicalize_existing_prefix` | function | Walks up 'path' to the nearest existing ancestor, canonicalizes that ancestor, then appends the missing suffix components back in original order, returning the reconstructed 'PathBuf' or an 'Io'-wrapped 'WikiError' tagged with 'action' and the canonicalized prefix path. [crates/gwiki/src/synthesis/paths.rs:40-63] |
| `ensure_existing_parent_inside_vault` | function | Canonicalizes the vault root and the existing parent directory, then returns 'Ok(())' only if the parent path is within the canonical vault root, otherwise returns a 'WikiError' for an out-of-vault synthesized path. [crates/gwiki/src/synthesis/paths.rs:65-80] |
| `synthesized_path_outside_vault` | function | Constructs a 'WikiError::InvalidInput' for the given field with the message that a synthesized wiki page path must remain inside the vault. [crates/gwiki/src/synthesis/paths.rs:82-87] |
| `wiki_link` | function | Constructs an Obsidian-style wiki link string '`[[relative/path\|title]]`' by computing 'path' relative to 'vault_root' and stripping any Markdown extension before inserting the provided 'title'. [crates/gwiki/src/synthesis/paths.rs:89-95] |
| `slugify` | function | Converts 'title' to a lowercase ASCII slug by retaining alphanumeric characters, collapsing any run of non-alphanumeric characters into single '-' separators between tokens, trimming trailing dashes, and returning '"wiki-page"' if the result is empty. [crates/gwiki/src/synthesis/paths.rs:97-120] |
| `slugify_unique` | function | Generates a slug from 'title', returns it if 'exists' says it is unused, otherwise appends '-2' through '-MAX_SLUG_TRIES' until finding an unused slug, and falls back to 'base-<uuid>' if all candidates are taken. [crates/gwiki/src/synthesis/paths.rs:122-136] |
| `relative_path` | function | Returns 'path' with 'root' stripped as a prefix when possible, otherwise the original path, then converts it to a lossy string and normalizes path separators to '/'. [crates/gwiki/src/synthesis/paths.rs:138-143] |
| `source_page_paths` | function | Computes unique markdown file paths under the vault’s source-article directory for each 'SynthesisSource' by slugifying titles, reserving the current article’s existing slug if applicable, and avoiding collisions with already reserved names or existing '.md' files. [crates/gwiki/src/synthesis/paths.rs:145-167] |
| `source_links` | function | Builds and returns a 'Vec<String>' of wiki links by zipping each 'SynthesisSource' with its corresponding 'PathBuf' and passing the vault root, path, and source title to 'wiki_link'. [crates/gwiki/src/synthesis/paths.rs:169-179] |
| `trim_markdown_extension` | function | Returns a 'String' containing 'path' with a trailing '.md' or '.markdown' suffix removed, or the original path unchanged if neither suffix is present. [crates/gwiki/src/synthesis/paths.rs:181-186] |

