---
title: crates/gcode/src/index/walker/classification.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/classification.rs
  ranges:
  - 15-52
  - 56-66
  - 69-78
  - 81-93
  - 95-111
  - 113-117
  - 119-144
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/classification.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

This file classifies candidate paths for indexing, separating safe files into AST-backed content or content-only text, while rejecting unsafe, generated, or hidden cases. `classify_file` is the main decision point: it first filters out non-indexable files, then treats hidden metadata, unknown languages, and oversized data-language files as `ContentOnly`, and other detected languages as `Ast`. The other helpers adapt that core logic for explicit requests, boolean indexability checks, content-language naming, visibility checks, path equivalence, and safety validation so discovery and indexing use the same rules.
[crates/gcode/src/index/walker/classification.rs:15-52]
[crates/gcode/src/index/walker/classification.rs:56-66]
[crates/gcode/src/index/walker/classification.rs:69-78]
[crates/gcode/src/index/walker/classification.rs:81-93]
[crates/gcode/src/index/walker/classification.rs:95-111]

## API Symbols

- `classify_file` (function) component `classify_file [function]` (`2b6a5919-acd7-599b-8e25-a5668bbd68c2`) lines 15-52 [crates/gcode/src/index/walker/classification.rs:15-52]
  - Signature: `pub fn classify_file(`
  - Purpose: 'classify_file' returns 'None' for unsafe, generated, or bundle files, otherwise classifies a file as 'ContentOnly' for hidden metadata, unknown languages, or oversized data-language files, and as 'Ast' for other detected languages. [crates/gcode/src/index/walker/classification.rs:15-52]
- `classify_explicit_file_with_options` (function) component `classify_explicit_file_with_options [function]` (`9e3f2864-703d-518a-944a-7d2a35ff744b`) lines 56-66 [crates/gcode/src/index/walker/classification.rs:56-66]
  - Signature: `pub fn classify_explicit_file_with_options(`
  - Purpose: Returns 'None' when the explicit 'path' is hidden by gitignore-aware visibility rules, otherwise delegates to 'classify_file(root, path, exclude_patterns)' and returns its 'Option<FileClassification>' result. [crates/gcode/src/index/walker/classification.rs:56-66]
- `is_content_indexable` (function) component `is_content_indexable [function]` (`01e57cf4-5711-55ab-8ff5-c0e7e800f88a`) lines 69-78 [crates/gcode/src/index/walker/classification.rs:69-78]
  - Signature: `pub fn is_content_indexable(`
  - Purpose: Returns 'true' only when 'classify_file(root, path, exclude_patterns)' yields 'Some(FileClassification::ContentOnly)', otherwise 'false'. [crates/gcode/src/index/walker/classification.rs:69-78]
- `content_language` (function) component `content_language [function]` (`44ba0277-d89a-549c-9061-755cf7af4b2a`) lines 81-93 [crates/gcode/src/index/walker/classification.rs:81-93]
  - Signature: `pub fn content_language(path: &Path) -> String {`
  - Purpose: Returns the lowercase file extension of 'path' as the content language, defaulting to '"text"' when absent, while normalizing 'md'/'markdown' to '"markdown"' and 'yml'/'yaml' to '"yaml"'. [crates/gcode/src/index/walker/classification.rs:81-93]
- `explicit_path_visible` (function) component `explicit_path_visible [function]` (`b80b2c1b-627d-5c31-813a-c3b758cf87e9`) lines 95-111 [crates/gcode/src/index/walker/classification.rs:95-111]
  - Signature: `fn explicit_path_visible(root: &Path, path: &Path, options: DiscoveryOptions) -> bool {`
  - Purpose: Returns 'false' for hidden paths not matched by the root allowlist, otherwise checks whether the exact existing 'path' is discoverable as a file by a one-level walker rooted at its parent with gitignore and max-file-size constraints applied. [crates/gcode/src/index/walker/classification.rs:95-111]
- `same_existing_path` (function) component `same_existing_path [function]` (`ce414d42-18fb-53a0-9266-ab69b2ae3312`) lines 113-117 [crates/gcode/src/index/walker/classification.rs:113-117]
  - Signature: `fn same_existing_path(left: &Path, right: &Path) -> bool {`
  - Purpose: Returns 'true' when 'left' and 'right' resolve to the same canonicalized filesystem path, falling back to their original path values if canonicalization fails, and then comparing the resulting 'PathBuf's for equality. [crates/gcode/src/index/walker/classification.rs:113-117]
- `is_safe_text_file` (function) component `is_safe_text_file [function]` (`1d62664b-98f9-531f-a9aa-a81238650db4`) lines 119-144 [crates/gcode/src/index/walker/classification.rs:119-144]
  - Signature: `fn is_safe_text_file(root: &Path, path: &Path, exclude_patterns: &[impl AsRef<str>]) -> bool {`
  - Purpose: Returns 'true' only for an existing regular file under 'root' that passes path and symlink validation, is not excluded or secret-suffixed, has readable metadata with size in '(0, MAX_FILE_SIZE]', and is not detected as binary. [crates/gcode/src/index/walker/classification.rs:119-144]

