---
title: crates/gcode/src/index/walker/generated.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/generated.rs
  ranges:
  - 18-38
  - 40-45
  - 47-57
  - 59-65
  - 67-92
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/generated.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

Helpers for classifying JavaScript-family files as generated bundles during indexing. `is_generated_js_bundle` gates on JS-like extensions, then tries to read the file prefix and metadata; it returns true if the prefix contains common generated-code markers, or for sufficiently large files if the content looks minified. The supporting helpers handle reading a bounded file prefix, checking the extension, scanning the initial bytes for marker phrases, and applying simple minification heuristics based on file size, line length, and line count.
[crates/gcode/src/index/walker/generated.rs:18-38]
[crates/gcode/src/index/walker/generated.rs:40-45]
[crates/gcode/src/index/walker/generated.rs:47-57]
[crates/gcode/src/index/walker/generated.rs:59-65]
[crates/gcode/src/index/walker/generated.rs:67-92]

## API Symbols

- `is_generated_js_bundle` (function) component `is_generated_js_bundle [function]` (`2b409858-23d3-52c7-8431-b919fcffbd48`) lines 18-38 [crates/gcode/src/index/walker/generated.rs:18-38]
  - Signature: `pub(super) fn is_generated_js_bundle(path: &Path) -> bool {`
  - Purpose: Returns 'true' for JS-family files that either contain a generated-JS marker in the file prefix or, if the file is at least 'MINIFIED_JS_MIN_BYTES' long, satisfy 'looks_minified_js_bundle', and returns 'false' on non-JS files or any metadata/prefix read failure. [crates/gcode/src/index/walker/generated.rs:18-38]
- `read_file_prefix` (function) component `read_file_prefix [function]` (`475c641a-7973-57e4-a3fd-9d7a4fa992a6`) lines 40-45 [crates/gcode/src/index/walker/generated.rs:40-45]
  - Signature: `fn read_file_prefix(path: &Path, max_bytes: u64) -> std::io::Result<Vec<u8>> {`
  - Purpose: Opens the file at 'path', reads up to 'max_bytes' from the start into a preallocated 'Vec<u8>', and returns the collected bytes or any I/O error. [crates/gcode/src/index/walker/generated.rs:40-45]
- `is_js_family_file` (function) component `is_js_family_file [function]` (`bedcdc41-d3fd-5edb-9713-09805de2a617`) lines 47-57 [crates/gcode/src/index/walker/generated.rs:47-57]
  - Signature: `fn is_js_family_file(path: &Path) -> bool {`
  - Purpose: Returns 'true' if the given path has an extension that, case-insensitively, is 'js', 'jsx', 'cjs', or 'mjs', and 'false' otherwise, including when the path has no valid UTF-8 extension. [crates/gcode/src/index/walker/generated.rs:47-57]
- `contains_generated_js_marker` (function) component `contains_generated_js_marker [function]` (`04e89974-6865-5e44-9f84-2470487b0f55`) lines 59-65 [crates/gcode/src/index/walker/generated.rs:59-65]
  - Signature: `fn contains_generated_js_marker(bytes: &[u8]) -> bool {`
  - Purpose: Scans up to 'GENERATED_JS_MARKER_SCAN_BYTES' from the start of 'bytes', lossily decodes them to lowercase ASCII text, and returns 'true' if any string in 'GENERATED_JS_MARKERS' appears as a substring. [crates/gcode/src/index/walker/generated.rs:59-65]
- `looks_minified_js_bundle` (function) component `looks_minified_js_bundle [function]` (`83a73907-da7d-5569-90f3-d0d8a76c71ca`) lines 67-92 [crates/gcode/src/index/walker/generated.rs:67-92]
  - Signature: `fn looks_minified_js_bundle(bytes: &[u8]) -> bool {`
  - Purpose: Returns 'true' when the input is at least 'MINIFIED_JS_MIN_BYTES' and, after splitting on '\n', either contains a line of at least 'MINIFIED_JS_LONG_LINE_BYTES' or has at most 'MINIFIED_JS_MAX_LINES' nonempty lines with an average line length of at least 'MINIFIED_JS_AVG_LINE_BYTES'. [crates/gcode/src/index/walker/generated.rs:67-92]

