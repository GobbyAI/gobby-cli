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

`crates/gcode/src/index/import_resolution/js_local.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

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
| `relative_specifier_resolves_to_sibling_file_and_index` | function | Verifies that resolving the relative specifier './c' from 'src/a/b.ts' yields sibling candidate files 'src/a/c.ts', 'src/a/c.js', and 'src/a/c/index.tsx'. [crates/gcode/src/index/import_resolution/js_local.rs:145-150] |
| `parent_specifier_walks_up_one_directory` | function | Verifies that 'js_candidate_files("src/a/b.ts", None, "../shared")' resolves a parent-directory import to 'src/shared.ts'. [crates/gcode/src/index/import_resolution/js_local.rs:153-156] |
| `at_alias_maps_to_src_root` | function | Verifies that 'js_candidate_files("src/app.js", None, "@/utils")' resolves the '@/' alias to the source root by including 'src/utils.js' in the returned candidate file list. [crates/gcode/src/index/import_resolution/js_local.rs:159-162] |
| `self_package_specifier_resolves_with_and_without_src` | function | Verifies that resolving the self package specifier '"app/utils"' from 'src/app.js' yields candidate files in both 'src/utils.js' and 'utils.js'. [crates/gcode/src/index/import_resolution/js_local.rs:165-169] |
| `bare_external_specifier_yields_no_candidates` | function | Verifies that 'js_candidate_files("src/app.js", Some("app"), "lodash")' returns an empty set for a bare external module specifier. [crates/gcode/src/index/import_resolution/js_local.rs:172-174] |

