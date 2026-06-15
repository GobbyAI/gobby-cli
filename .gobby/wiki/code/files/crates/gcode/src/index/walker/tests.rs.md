---
title: crates/gcode/src/index/walker/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/tests.rs
  ranges:
  - 11-17
  - 19-31
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/tests.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

Test support module for `index::walker` that pulls in the classification, discovery, generated, and hidden test cases and provides two helpers: `write_file` creates a file under a root path after making parent directories, and `rels` converts a list of paths under that root into sorted relative path strings for easy comparison in assertions.
[crates/gcode/src/index/walker/tests.rs:11-17]
[crates/gcode/src/index/walker/tests.rs:19-31]

## API Symbols

- `write_file` (function) component `write_file [function]` (`8cdbdb21-4dad-50df-8229-7384dd4ce8c3`) lines 11-17 [crates/gcode/src/index/walker/tests.rs:11-17]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &[u8]) {`
  - Purpose: Joins 'rel' to 'root', creates any missing parent directories for the resulting path, and then writes 'contents' to that file, panicking on any I/O failure. [crates/gcode/src/index/walker/tests.rs:11-17]
- `rels` (function) component `rels [function]` (`61fa14cb-3e0b-569c-9365-bc120f11dc91`) lines 19-31 [crates/gcode/src/index/walker/tests.rs:19-31]
  - Signature: `fn rels(root: &Path, paths: Vec<PathBuf>) -> Vec<String> {`
  - Purpose: Returns the lexicographically sorted list of UTF-8-lossy relative path strings obtained by stripping 'root' from each input path, panicking if any path is not under 'root'. [crates/gcode/src/index/walker/tests.rs:19-31]

