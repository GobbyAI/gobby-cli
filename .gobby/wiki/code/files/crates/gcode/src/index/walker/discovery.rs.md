---
title: crates/gcode/src/index/walker/discovery.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/discovery.rs
  ranges:
  - 12-17
  - 19-64
  - 66-84
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/discovery.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

This file discovers indexable files under a root path and splits them into two buckets: AST candidates and content-only candidates. `discover_files` is a convenience wrapper that uses default discovery options, while `discover_files_with_options` configures a hidden-file walker with the project size limit and optional gitignore handling, then supplements the walk with hidden-path allowlist entries; both sources feed `push_classified_file`, which deduplicates by canonical path and uses `classify_file` plus exclude patterns to decide whether each path belongs in `candidates`, `content_only`, or neither.
[crates/gcode/src/index/walker/discovery.rs:12-17]
[crates/gcode/src/index/walker/discovery.rs:19-64]
[crates/gcode/src/index/walker/discovery.rs:66-84]

## API Symbols

- `discover_files` (function) component `discover_files [function]` (`f931f3c8-31a0-557a-838b-3e606577def8`) lines 12-17 [crates/gcode/src/index/walker/discovery.rs:12-17]
  - Signature: `pub fn discover_files<S: AsRef<str>>(`
  - Purpose: Calls 'discover_files_with_options' with 'DiscoveryOptions::default()' to discover files under 'root' while applying 'exclude_patterns', returning a tuple of two 'Vec<PathBuf>' collections. [crates/gcode/src/index/walker/discovery.rs:12-17]
- `discover_files_with_options` (function) component `discover_files_with_options [function]` (`9d8a43e3-8601-5f60-884a-8e9bfbfcfd25`) lines 19-64 [crates/gcode/src/index/walker/discovery.rs:19-64]
  - Signature: `pub fn discover_files_with_options<S: AsRef<str>>(`
  - Purpose: Traverses 'root' with a hidden-file walker constrained by 'MAX_FILE_SIZE' and optional gitignore respect, then augments the result with paths from 'HiddenPathAllowlist', classifying each discovered file via 'push_classified_file' into deduplicated 'candidates' and 'content_only' lists returned as a tuple. [crates/gcode/src/index/walker/discovery.rs:19-64]
- `push_classified_file` (function) component `push_classified_file [function]` (`8d6d0547-e604-5076-858b-fc6889b96385`) lines 66-84 [crates/gcode/src/index/walker/discovery.rs:66-84]
  - Signature: `fn push_classified_file(`
  - Purpose: Deduplicates a path by canonicalized identity, classifies the file relative to 'root' with 'exclude_patterns', and appends the original path to either 'candidates' for 'Ast' files or 'content_only' for 'ContentOnly' files. [crates/gcode/src/index/walker/discovery.rs:66-84]

