---
title: crates/gwiki/src/synthesis/paths.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/paths.rs
  ranges:
  - 10-38
  - 40-63
  - 65-80
  - 82-87
  - 89-95
  - 97-120
  - 122-136
  - 138-143
  - 145-167
  - 169-179
  - 181-186
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/synthesis/paths.rs:10-38](crates/gwiki/src/synthesis/paths.rs#L10-L38), [crates/gwiki/src/synthesis/paths.rs:40-63](crates/gwiki/src/synthesis/paths.rs#L40-L63), [crates/gwiki/src/synthesis/paths.rs:65-80](crates/gwiki/src/synthesis/paths.rs#L65-L80), [crates/gwiki/src/synthesis/paths.rs:82-87](crates/gwiki/src/synthesis/paths.rs#L82-L87), [crates/gwiki/src/synthesis/paths.rs:89-95](crates/gwiki/src/synthesis/paths.rs#L89-L95), [crates/gwiki/src/synthesis/paths.rs:97-120](crates/gwiki/src/synthesis/paths.rs#L97-L120), [crates/gwiki/src/synthesis/paths.rs:122-136](crates/gwiki/src/synthesis/paths.rs#L122-L136), [crates/gwiki/src/synthesis/paths.rs:138-143](crates/gwiki/src/synthesis/paths.rs#L138-L143), [crates/gwiki/src/synthesis/paths.rs:145-167](crates/gwiki/src/synthesis/paths.rs#L145-L167), [crates/gwiki/src/synthesis/paths.rs:169-179](crates/gwiki/src/synthesis/paths.rs#L169-L179), [crates/gwiki/src/synthesis/paths.rs:181-186](crates/gwiki/src/synthesis/paths.rs#L181-L186)

</details>

# crates/gwiki/src/synthesis/paths.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file provides path and link utilities for wiki synthesis. It canonicalizes synthesized paths against the vault root, rejects any result that escapes the vault, and checks that existing parent directories stay inside the vault as well. It also builds Obsidian-style wiki links, converts titles into lowercase ASCII slugs, finds a unique slug when collisions occur, trims markdown extensions, and computes per-source article file paths and corresponding links for synthesized pages.
[crates/gwiki/src/synthesis/paths.rs:10-38]
[crates/gwiki/src/synthesis/paths.rs:40-63]
[crates/gwiki/src/synthesis/paths.rs:65-80]
[crates/gwiki/src/synthesis/paths.rs:82-87]
[crates/gwiki/src/synthesis/paths.rs:89-95]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ensure_synthesized_path_inside_vault` | function | `pub fn ensure_synthesized_path_inside_vault(` | `ensure_synthesized_path_inside_vault [function]` | `96caeb49-0570-51eb-99f7-44deed808120` | 10-38 [crates/gwiki/src/synthesis/paths.rs:10-38] | Resolves the vault root and a synthesized candidate path, canonicalizes the candidate’s existing prefix, and returns an error unless the resulting path is strictly inside the vault root with no '..', root, or platform prefix components. [crates/gwiki/src/synthesis/paths.rs:10-38] |
| `canonicalize_existing_prefix` | function | `fn canonicalize_existing_prefix(path: &Path, action: &'static str) -> Result<PathBuf, WikiError> {` | `canonicalize_existing_prefix [function]` | `2cb7da8b-561e-5a0d-b989-e5ee9a9d0dbb` | 40-63 [crates/gwiki/src/synthesis/paths.rs:40-63] | Walks up 'path' to the nearest existing ancestor, canonicalizes that ancestor, then appends the missing suffix components back in original order, returning the reconstructed 'PathBuf' or an 'Io'-wrapped 'WikiError' tagged with 'action' and the canonicalized prefix path. [crates/gwiki/src/synthesis/paths.rs:40-63] |
| `ensure_existing_parent_inside_vault` | function | `pub(super) fn ensure_existing_parent_inside_vault(` | `ensure_existing_parent_inside_vault [function]` | `0f8bb06f-4162-5a3c-ab30-73196b5771a8` | 65-80 [crates/gwiki/src/synthesis/paths.rs:65-80] | Canonicalizes the vault root and the existing parent directory, then returns 'Ok(())' only if the parent path is within the canonical vault root, otherwise returns a 'WikiError' for an out-of-vault synthesized path. [crates/gwiki/src/synthesis/paths.rs:65-80] |
| `synthesized_path_outside_vault` | function | `fn synthesized_path_outside_vault(field: &'static str) -> WikiError {` | `synthesized_path_outside_vault [function]` | `16a3f599-5006-5d2c-a302-a60cfb3d38c8` | 82-87 [crates/gwiki/src/synthesis/paths.rs:82-87] | Constructs a 'WikiError::InvalidInput' for the given field with the message that a synthesized wiki page path must remain inside the vault. [crates/gwiki/src/synthesis/paths.rs:82-87] |
| `wiki_link` | function | `pub fn wiki_link(vault_root: &Path, path: &Path, title: &str) -> String {` | `wiki_link [function]` | `c1b49f48-d413-5523-a62b-1e98dc06e3da` | 89-95 [crates/gwiki/src/synthesis/paths.rs:89-95] | Constructs an Obsidian-style wiki link string '`[[relative/path\|title]]`' by computing 'path' relative to 'vault_root' and stripping any Markdown extension before inserting the provided 'title'. [crates/gwiki/src/synthesis/paths.rs:89-95] |
| `slugify` | function | `pub fn slugify(title: &str) -> String {` | `slugify [function]` | `7af270fd-4f51-5d18-a756-620f8b404c20` | 97-120 [crates/gwiki/src/synthesis/paths.rs:97-120] | Converts 'title' to a lowercase ASCII slug by retaining alphanumeric characters, collapsing any run of non-alphanumeric characters into single '-' separators between tokens, trimming trailing dashes, and returning '"wiki-page"' if the result is empty. [crates/gwiki/src/synthesis/paths.rs:97-120] |
| `slugify_unique` | function | `pub fn slugify_unique(title: &str, mut exists: impl FnMut(&str) -> bool) -> String {` | `slugify_unique [function]` | `1afe4b8d-6db3-5b65-8595-9123d02e330d` | 122-136 [crates/gwiki/src/synthesis/paths.rs:122-136] | Generates a slug from 'title', returns it if 'exists' says it is unused, otherwise appends '-2' through '-MAX_SLUG_TRIES' until finding an unused slug, and falls back to 'base-<uuid>' if all candidates are taken. [crates/gwiki/src/synthesis/paths.rs:122-136] |
| `relative_path` | function | `pub fn relative_path(root: &Path, path: &Path) -> String {` | `relative_path [function]` | `4ed48e8f-e1aa-57c2-afa7-fcb5cf31233a` | 138-143 [crates/gwiki/src/synthesis/paths.rs:138-143] | Returns 'path' with 'root' stripped as a prefix when possible, otherwise the original path, then converts it to a lossy string and normalizes path separators to '/'. [crates/gwiki/src/synthesis/paths.rs:138-143] |
| `source_page_paths` | function | `pub(super) fn source_page_paths(` | `source_page_paths [function]` | `770c444d-c8c2-5bac-b97f-b6c6cccfcf34` | 145-167 [crates/gwiki/src/synthesis/paths.rs:145-167] | Computes unique markdown file paths under the vault’s source-article directory for each 'SynthesisSource' by slugifying titles, reserving the current article’s existing slug if applicable, and avoiding collisions with already reserved names or existing '.md' files. [crates/gwiki/src/synthesis/paths.rs:145-167] |
| `source_links` | function | `pub(super) fn source_links(` | `source_links [function]` | `8acef57f-b4b9-5b51-bfef-b766b70fe43d` | 169-179 [crates/gwiki/src/synthesis/paths.rs:169-179] | Builds and returns a 'Vec<String>' of wiki links by zipping each 'SynthesisSource' with its corresponding 'PathBuf' and passing the vault root, path, and source title to 'wiki_link'. [crates/gwiki/src/synthesis/paths.rs:169-179] |
| `trim_markdown_extension` | function | `fn trim_markdown_extension(path: &str) -> String {` | `trim_markdown_extension [function]` | `7835d455-c923-5368-8b76-da211b993b61` | 181-186 [crates/gwiki/src/synthesis/paths.rs:181-186] | Returns a 'String' containing 'path' with a trailing '.md' or '.markdown' suffix removed, or the original path unchanged if neither suffix is present. [crates/gwiki/src/synthesis/paths.rs:181-186] |
