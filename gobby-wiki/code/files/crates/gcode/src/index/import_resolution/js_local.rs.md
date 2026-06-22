---
title: crates/gcode/src/index/import_resolution/js_local.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/js_local.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/js_local.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/js_local.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/js_local.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `js_candidate_files` | function | Generates a deduplicated list of candidate JavaScript/TypeScript import target paths by expanding each non-empty key from 'js_import_target_keys(rel_path, self_package, specifier)' into '{key}.{ext}' and '{key}/index.{ext}' for the extensions 'js', 'jsx', 'cjs', 'mjs', 'ts', and 'tsx'. [crates/gcode/src/index/import_resolution/js_local.rs:7-24] |
| `js_import_target_keys` | function | Returns a deduplicated set of possible module-key strings for a JavaScript import specifier by trimming it and resolving relative paths, absolute paths, '@/' or '~/' aliases, and same-package imports (including the package root and 'package_name/...' subpaths), otherwise returning an empty vector. [crates/gcode/src/index/import_resolution/js_local.rs:26-69] |
| `module_key_variants` | function | Normalizes a module key, returns an empty vector if it becomes empty, otherwise returns the normalized key and, when it ends with '/index' and the prefix is non-empty, also returns the prefix without that suffix. [crates/gcode/src/index/import_resolution/js_local.rs:71-84] |
| `normalize_module_path` | function | Builds a normalized module path by discarding '.' segments, resolving '..' by popping the previous path component, ignoring root/prefix components, joining the remaining components with '/', and stripping any JavaScript extension from the result. [crates/gcode/src/index/import_resolution/js_local.rs:86-99] |
| `normalize_module_key` | function | Returns a normalized module path string by converting backslashes to slashes, stripping leading/trailing slashes, removing empty and '.' segments, resolving '..' by popping the previous segment, and joining the remaining components with '/'. [crates/gcode/src/index/import_resolution/js_local.rs:101-115] |
| `strip_js_extension` | function | Returns the input module path/name with a trailing '.js', '.jsx', '.cjs', '.mjs', '.ts', or '.tsx' extension removed if present, otherwise returns the original string unchanged. [crates/gcode/src/index/import_resolution/js_local.rs:117-124] |
| `dedupe` | function | Returns a new 'Vec<String>' containing the input strings in their original order, with only the first occurrence of each distinct value preserved. [crates/gcode/src/index/import_resolution/js_local.rs:126-134] |
| `contains` | function | Returns 'true' if any string in 'files' is exactly equal to 'expected', otherwise 'false'. [crates/gcode/src/index/import_resolution/js_local.rs:140-142] |

_Verified by 5 in-file unit tests._

