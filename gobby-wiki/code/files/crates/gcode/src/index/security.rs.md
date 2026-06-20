---
title: crates/gcode/src/index/security.rs
type: code_file
provenance:
- file: crates/gcode/src/index/security.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/security.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/security.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/index/security.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `validate_path` | function | Returns 'true' only when both 'path' and 'root' canonicalize successfully and the resolved 'path' lies within the resolved 'root' directory prefix, otherwise 'false'. [crates/gcode/src/index/security.rs:26-31] |
| `is_symlink_safe` | function | Returns 'true' for any non-symlink path, and for symlinks delegates to 'validate_path(path, root)' to determine whether the path is safe relative to 'root'. [crates/gcode/src/index/security.rs:34-39] |
| `is_binary` | function | Attempts to open the file at 'path', reads up to 8192 bytes, and returns 'true' if opening or reading fails or if the sampled bytes contain a NUL byte, otherwise 'false'. [crates/gcode/src/index/security.rs:42-54] |
| `should_exclude_path` | function | Returns 'true' if 'path' (relative to 'root' when possible) matches any glob pattern against either its first component for root-generated directory patterns or any path component for all other patterns, and 'false' otherwise. [crates/gcode/src/index/security.rs:63-89] |
| `is_root_generated_dir` | function | Returns 'true' if 'pattern' is an exact member of 'ROOT_GENERATED_DIRS', otherwise 'false'. [crates/gcode/src/index/security.rs:91-93] |
| `has_secret_extension` | function | Returns 'true' when the path’s lowercase filename or extension matches any configured secret extension, prefix, or substring pattern, and 'false' otherwise. [crates/gcode/src/index/security.rs:96-120] |
| `glob_match` | function | Converts 'pattern' and 'text' into 'Vec<char>' and returns the result of 'glob_inner(&pc, &tc)', performing glob-style matching over the two character sequences. [crates/gcode/src/index/security.rs:123-127] |
| `glob_inner` | function | Performs recursive glob matching of a character pattern against a character slice, where '*' matches any sequence including empty, '?' matches any single character, and all other characters must match literally. [crates/gcode/src/index/security.rs:129-148] |

