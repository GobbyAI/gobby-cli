---
title: crates/gcode/src/index/security.rs
type: code_file
provenance:
- file: crates/gcode/src/index/security.rs
  ranges:
  - 26-31
  - 34-39
  - 42-54
  - 63-89
  - 91-93
  - 96-120
  - 123-127
  - 129-148
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/security.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Provides security filters for the code indexer. The file verifies that paths stay within the indexing root, rejects unsafe symlinks, treats unreadable or NUL-containing files as binary, and decides whether to skip a path based on glob patterns with special handling for root-level generated directories. It also flags secret-looking filenames and extensions, and includes a small recursive glob matcher that powers the exclusion checks.
[crates/gcode/src/index/security.rs:26-31]
[crates/gcode/src/index/security.rs:34-39]
[crates/gcode/src/index/security.rs:42-54]
[crates/gcode/src/index/security.rs:63-89]
[crates/gcode/src/index/security.rs:91-93]

## API Symbols

- `validate_path` (function) component `validate_path [function]` (`de4b2dfa-54db-529b-9386-c2bbf1ee2b5c`) lines 26-31 [crates/gcode/src/index/security.rs:26-31]
  - Signature: `pub fn validate_path(path: &Path, root: &Path) -> bool {`
  - Purpose: Returns 'true' only if both 'path' and 'root' can be canonicalized successfully and the canonicalized 'path' is located within or equal to the canonicalized 'root' directory; otherwise returns 'false'. [crates/gcode/src/index/security.rs:26-31]
- `is_symlink_safe` (function) component `is_symlink_safe [function]` (`38718a5d-64c1-5d96-84d7-62c546031882`) lines 34-39 [crates/gcode/src/index/security.rs:34-39]
  - Signature: `pub fn is_symlink_safe(path: &Path, root: &Path) -> bool {`
  - Purpose: Returns 'true' for any non-symlink path, and for symlinks delegates to 'validate_path(path, root)' to determine whether the symlink is safe relative to 'root'. [crates/gcode/src/index/security.rs:34-39]
- `is_binary` (function) component `is_binary [function]` (`6393eb82-9b21-5c1c-aad9-a650215e5c71`) lines 42-54 [crates/gcode/src/index/security.rs:42-54]
  - Signature: `pub fn is_binary(path: &Path) -> bool {`
  - Purpose: Returns 'true' if the file at 'path' cannot be opened or read, or if the first up to 8192 bytes contain a NUL byte, otherwise 'false'. [crates/gcode/src/index/security.rs:42-54]
- `should_exclude_path` (function) component `should_exclude_path [function]` (`af921ac4-e098-5d62-a38c-15823e0b99f2`) lines 63-89 [crates/gcode/src/index/security.rs:63-89]
  - Signature: `pub fn should_exclude_path(root: &Path, path: &Path, patterns: &[impl AsRef<str>]) -> bool {`
  - Purpose: Returns 'true' if any glob pattern matches a path component of 'path' relative to 'root' (or the first component for root-generated directories), and 'false' otherwise. [crates/gcode/src/index/security.rs:63-89]
- `is_root_generated_dir` (function) component `is_root_generated_dir [function]` (`06c7e85f-3065-540e-9d0e-b7fafdbe1d08`) lines 91-93 [crates/gcode/src/index/security.rs:91-93]
  - Signature: `fn is_root_generated_dir(pattern: &str) -> bool {`
  - Purpose: Returns 'true' if 'pattern' exactly matches one of the entries in 'ROOT_GENERATED_DIRS', otherwise 'false'. [crates/gcode/src/index/security.rs:91-93]
- `has_secret_extension` (function) component `has_secret_extension [function]` (`8eb85387-7bfe-51cc-aa21-2b86e14569b5`) lines 96-120 [crates/gcode/src/index/security.rs:96-120]
  - Signature: `pub fn has_secret_extension(path: &Path) -> bool {`
  - Purpose: Returns 'true' when the path’s filename or extension matches any configured secret indicator by checking for a secret extension, a secret filename prefix, or a secret substring, all case-insensitively. [crates/gcode/src/index/security.rs:96-120]
- `glob_match` (function) component `glob_match [function]` (`31c0a5dd-c5c8-5aaa-bb51-0d7a03b246fd`) lines 123-127 [crates/gcode/src/index/security.rs:123-127]
  - Signature: `pub fn glob_match(pattern: &str, text: &str) -> bool {`
  - Purpose: Converts 'pattern' and 'text' into 'Vec<char>' values and returns the result of 'glob_inner(&pc, &tc)', i.e. whether the text matches the glob pattern. [crates/gcode/src/index/security.rs:123-127]
- `glob_inner` (function) component `glob_inner [function]` (`b011b000-658b-5ed7-bb2d-c7183aca80cd`) lines 129-148 [crates/gcode/src/index/security.rs:129-148]
  - Signature: `fn glob_inner(pattern: &[char], text: &[char]) -> bool {`
  - Purpose: 'glob_inner' recursively matches a glob pattern against text, where '*' matches any sequence of characters (including empty), '?' matches exactly one character, and all other characters must match literally. [crates/gcode/src/index/security.rs:129-148]

