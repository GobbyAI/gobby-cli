---
title: crates/gcode/src/index/walker/generated.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/generated.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/generated.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Overview

`crates/gcode/src/index/walker/generated.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/index/walker/generated.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `is_generated_js_bundle` | function | Returns 'true' for a JavaScript-family path only if the file can be stat’ed and read, then either its prefix contains a generated-JS marker or, when large enough, its prefix heuristically looks like a minified JS bundle; otherwise it returns 'false'. [crates/gcode/src/index/walker/generated.rs:18-38] |
| `read_file_prefix` | function | Opens the file at 'path', reads up to 'max_bytes' from the beginning into a newly allocated 'Vec<u8>', and returns the buffered prefix or any I/O error encountered. [crates/gcode/src/index/walker/generated.rs:40-45] |
| `is_js_family_file` | function | Returns 'true' iff the given path has an extension that case-insensitively matches one of 'js', 'jsx', 'cjs', or 'mjs'; otherwise it returns 'false'. [crates/gcode/src/index/walker/generated.rs:47-57] |
| `contains_generated_js_marker` | function | Scans up to 'GENERATED_JS_MARKER_SCAN_BYTES' from the start of 'bytes', lowercases the UTF-8-lossy text, and returns 'true' if any marker in 'GENERATED_JS_MARKERS' appears as a substring. [crates/gcode/src/index/walker/generated.rs:59-65] |
| `looks_minified_js_bundle` | function | Returns 'true' when the byte slice is at least 'MINIFIED_JS_MIN_BYTES' long and either contains a line at least 'MINIFIED_JS_LONG_LINE_BYTES' bytes long or has at most 'MINIFIED_JS_MAX_LINES' non-empty lines with an average non-empty line length of at least 'MINIFIED_JS_AVG_LINE_BYTES'; otherwise returns 'false'. [crates/gcode/src/index/walker/generated.rs:67-92] |

