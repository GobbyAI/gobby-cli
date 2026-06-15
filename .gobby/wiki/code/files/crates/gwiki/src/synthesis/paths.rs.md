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

# crates/gwiki/src/synthesis/paths.rs

Module: [[code/modules/crates/gwiki/src/synthesis|crates/gwiki/src/synthesis]]

## Purpose

This file centralizes path handling for wiki synthesis: it validates that generated paths and their parent directories stay inside the vault, canonicalizing the longest existing prefix to make checks work even when the target path does not yet exist. It also provides the supporting utilities used during synthesis, including slug generation and uniqueness, relative-path formatting, markdown-extension trimming, Obsidian-style wiki link construction, and assigning unique source-page paths and links for synthesized sources.
[crates/gwiki/src/synthesis/paths.rs:10-38]
[crates/gwiki/src/synthesis/paths.rs:40-63]
[crates/gwiki/src/synthesis/paths.rs:65-80]
[crates/gwiki/src/synthesis/paths.rs:82-87]
[crates/gwiki/src/synthesis/paths.rs:89-95]

## API Symbols

- `ensure_synthesized_path_inside_vault` (function) component `ensure_synthesized_path_inside_vault [function]` (`96caeb49-0570-51eb-99f7-44deed808120`) lines 10-38 [crates/gwiki/src/synthesis/paths.rs:10-38]
  - Signature: `pub fn ensure_synthesized_path_inside_vault(`
  - Purpose: Resolves 'vault_root' and the synthesized 'path', then rejects it unless its canonicalized form is strictly within the vault root and contains no '..', root, or platform prefix components. [crates/gwiki/src/synthesis/paths.rs:10-38]
- `canonicalize_existing_prefix` (function) component `canonicalize_existing_prefix [function]` (`2cb7da8b-561e-5a0d-b989-e5ee9a9d0dbb`) lines 40-63 [crates/gwiki/src/synthesis/paths.rs:40-63]
  - Signature: `fn canonicalize_existing_prefix(path: &Path, action: &'static str) -> Result<PathBuf, WikiError> {`
  - Purpose: Resolves the longest existing ancestor of 'path' with 'canonicalize()', then appends any missing trailing path components in order to return a 'PathBuf' for the intended path or map the canonicalization I/O failure into 'WikiError::Io' with the supplied 'action'. [crates/gwiki/src/synthesis/paths.rs:40-63]
- `ensure_existing_parent_inside_vault` (function) component `ensure_existing_parent_inside_vault [function]` (`0f8bb06f-4162-5a3c-ab30-73196b5771a8`) lines 65-80 [crates/gwiki/src/synthesis/paths.rs:65-80]
  - Signature: `pub(super) fn ensure_existing_parent_inside_vault(`
  - Purpose: Resolves 'vault_root' and the existing 'parent' directory to canonical paths, returns 'Ok(())' only if the parent lies within the vault root, and otherwise returns a 'WikiError' indicating the synthesized path is outside the vault. [crates/gwiki/src/synthesis/paths.rs:65-80]
- `synthesized_path_outside_vault` (function) component `synthesized_path_outside_vault [function]` (`16a3f599-5006-5d2c-a302-a60cfb3d38c8`) lines 82-87 [crates/gwiki/src/synthesis/paths.rs:82-87]
  - Signature: `fn synthesized_path_outside_vault(field: &'static str) -> WikiError {`
  - Purpose: Constructs a 'WikiError::InvalidInput' for the given field with the message that a synthesized wiki page path must remain inside the vault. [crates/gwiki/src/synthesis/paths.rs:82-87]
- `wiki_link` (function) component `wiki_link [function]` (`c1b49f48-d413-5523-a62b-1e98dc06e3da`) lines 89-95 [crates/gwiki/src/synthesis/paths.rs:89-95]
  - Signature: `pub fn wiki_link(vault_root: &Path, path: &Path, title: &str) -> String {`
  - Purpose: Builds an Obsidian-style wiki link string of the form '`[[relative_path_without_markdown_extension|title]]`' by computing 'path' relative to 'vault_root' and trimming its markdown extension. [crates/gwiki/src/synthesis/paths.rs:89-95]
- `slugify` (function) component `slugify [function]` (`7af270fd-4f51-5d18-a756-620f8b404c20`) lines 97-120 [crates/gwiki/src/synthesis/paths.rs:97-120]
  - Signature: `pub fn slugify(title: &str) -> String {`
  - Purpose: Converts 'title' to a lowercase ASCII slug by preserving alphanumerics, collapsing non-alphanumeric runs into single hyphens between segments, trimming trailing hyphens, and returning '"wiki-page"' if nothing remains. [crates/gwiki/src/synthesis/paths.rs:97-120]
- `slugify_unique` (function) component `slugify_unique [function]` (`1afe4b8d-6db3-5b65-8595-9123d02e330d`) lines 122-136 [crates/gwiki/src/synthesis/paths.rs:122-136]
  - Signature: `pub fn slugify_unique(title: &str, mut exists: impl FnMut(&str) -> bool) -> String {`
  - Purpose: Returns a slugified version of 'title' that is guaranteed unique by first trying the base slug, then 'base-2' through 'base-MAX_SLUG_TRIES', and finally appending a new UUID suffix if all candidates already exist. [crates/gwiki/src/synthesis/paths.rs:122-136]
- `relative_path` (function) component `relative_path [function]` (`4ed48e8f-e1aa-57c2-afa7-fcb5cf31233a`) lines 138-143 [crates/gwiki/src/synthesis/paths.rs:138-143]
  - Signature: `pub fn relative_path(root: &Path, path: &Path) -> String {`
  - Purpose: Returns 'path' relative to 'root' when 'root' is a prefix, otherwise returns the original path, converting it to a UTF-8 lossily rendered string and normalizing backslashes to forward slashes. [crates/gwiki/src/synthesis/paths.rs:138-143]
- `source_page_paths` (function) component `source_page_paths [function]` (`770c444d-c8c2-5bac-b97f-b6c6cccfcf34`) lines 145-167 [crates/gwiki/src/synthesis/paths.rs:145-167]
  - Signature: `pub(super) fn source_page_paths(`
  - Purpose: Generates unique source-page file paths under the vault’s source directory by slugifying each source title, reserving the current article’s stem when applicable, and avoiding collisions with previously reserved slugs or existing '.md' files. [crates/gwiki/src/synthesis/paths.rs:145-167]
- `source_links` (function) component `source_links [function]` (`8acef57f-b4b9-5b51-bfef-b766b70fe43d`) lines 169-179 [crates/gwiki/src/synthesis/paths.rs:169-179]
  - Signature: `pub(super) fn source_links(`
  - Purpose: Builds and returns a 'Vec<String>' of wiki links by zipping each 'SynthesisSource' with its corresponding 'PathBuf' and passing the vault root, path, and source title to 'wiki_link'. [crates/gwiki/src/synthesis/paths.rs:169-179]
- `trim_markdown_extension` (function) component `trim_markdown_extension [function]` (`7835d455-c923-5368-8b76-da211b993b61`) lines 181-186 [crates/gwiki/src/synthesis/paths.rs:181-186]
  - Signature: `fn trim_markdown_extension(path: &str) -> String {`
  - Purpose: Returns 'path' without a trailing '.md' or '.markdown' extension, or the original string unchanged if neither suffix is present. [crates/gwiki/src/synthesis/paths.rs:181-186]

