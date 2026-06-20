---
title: crates/gcode/src/index/import_resolution/context/apple.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/apple.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context/apple.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/context/apple.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context/apple.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ObjcIndex` | class | 'ObjcIndex' is a module-private index that maps strings to lists of imported files, file types, and file functions via three 'HashMap<String, Vec<String>>' fields. [crates/gcode/src/index/import_resolution/context/apple.rs:8-12] |
| `build_objc_indexes` | function | Scans 'candidate_files' for Objective-C header/implementation files ('.h', '.m', '.mm'), extracts declared type and function names from each file, deduplicates them, and builds an 'ObjcIndex' keyed by the file’s relative path and filename variants. [crates/gcode/src/index/import_resolution/context/apple.rs:14-110] |
| `objc_declared_type_name` | function | Returns the declared Objective-C type name from an '@interface', '@implementation', or '@protocol' line by extracting the first token after the directive, validating it with 'is_objc_identifier', and returning it as 'Some(String)' or 'None' if no valid name is present. [crates/gcode/src/index/import_resolution/context/apple.rs:112-123] |
| `objc_declared_function_name` | function | Returns the trailing Objective-C-like identifier before the first '(' on a non-comment, non-preprocessor, non-assignment, non-'typedef' line, rejecting reserved keywords and invalid identifiers, and otherwise returns it as 'Some(String)'. [crates/gcode/src/index/import_resolution/context/apple.rs:125-149] |
| `objc_relative_import_file` | function | Returns 'Some(normalized_path)' for a relative Objective-C import resolved against 'rel_path'’s parent, but returns 'None' if 'import_path' is absolute, contains '$', ''', or '$(', or includes platform root/prefix path components. [crates/gcode/src/index/import_resolution/context/apple.rs:151-169] |
| `normalize_objc_project_path` | function | Returns a normalized relative project path string by collapsing '.' and '..' components, rejecting rooted or prefixed paths and any '..' that escapes above the start, and converting backslashes to forward slashes, or 'None' if the result is invalid or empty. [crates/gcode/src/index/import_resolution/context/apple.rs:171-187] |
| `is_objc_identifier` | function | Returns 'true' iff 'name' is non-empty and consists of an ASCII letter or underscore followed by only ASCII alphanumeric characters or underscores. [crates/gcode/src/index/import_resolution/context/apple.rs:189-196] |
| `swift_modules_for_rel` | function | Returns the set of Swift module names inferred from a relative path by collecting the directory name immediately following any 'Sources' or 'Tests' component, plus the path’s parent directory if it is a non-empty name other than 'Sources' or 'Tests'. [crates/gcode/src/index/import_resolution/context/apple.rs:203-225] |
| `build_swift_module_files` | function | Filters the input paths to '.swift' files, computes their Swift module names from each path relative to 'root_path', groups normalized relative file paths by module in parallel, then sorts and deduplicates each module’s file list before returning the 'HashMap<String, Vec<String>>'. [crates/gcode/src/index/import_resolution/context/apple.rs:232-274] |

