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

`crates/gcode/src/index/security.rs` exposes 8 indexed API symbols.
[crates/gcode/src/index/security.rs:26-31]
[crates/gcode/src/index/security.rs:34-39]
[crates/gcode/src/index/security.rs:42-54]
[crates/gcode/src/index/security.rs:63-89]
[crates/gcode/src/index/security.rs:91-93]

## API Symbols

- `validate_path` (function) component `validate_path [function]` (`de4b2dfa-54db-529b-9386-c2bbf1ee2b5c`) lines 26-31 [crates/gcode/src/index/security.rs:26-31]
  - Signature: `pub fn validate_path(path: &Path, root: &Path) -> bool {`
  - Purpose: Indexed function `validate_path` in `crates/gcode/src/index/security.rs`. [crates/gcode/src/index/security.rs:26-31]
- `is_symlink_safe` (function) component `is_symlink_safe [function]` (`38718a5d-64c1-5d96-84d7-62c546031882`) lines 34-39 [crates/gcode/src/index/security.rs:34-39]
  - Signature: `pub fn is_symlink_safe(path: &Path, root: &Path) -> bool {`
  - Purpose: Indexed function `is_symlink_safe` in `crates/gcode/src/index/security.rs`. [crates/gcode/src/index/security.rs:34-39]
- `is_binary` (function) component `is_binary [function]` (`6393eb82-9b21-5c1c-aad9-a650215e5c71`) lines 42-54 [crates/gcode/src/index/security.rs:42-54]
  - Signature: `pub fn is_binary(path: &Path) -> bool {`
  - Purpose: Indexed function `is_binary` in `crates/gcode/src/index/security.rs`. [crates/gcode/src/index/security.rs:42-54]
- `should_exclude_path` (function) component `should_exclude_path [function]` (`af921ac4-e098-5d62-a38c-15823e0b99f2`) lines 63-89 [crates/gcode/src/index/security.rs:63-89]
  - Signature: `pub fn should_exclude_path(root: &Path, path: &Path, patterns: &[impl AsRef<str>]) -> bool {`
  - Purpose: Indexed function `should_exclude_path` in `crates/gcode/src/index/security.rs`. [crates/gcode/src/index/security.rs:63-89]
- `is_root_generated_dir` (function) component `is_root_generated_dir [function]` (`06c7e85f-3065-540e-9d0e-b7fafdbe1d08`) lines 91-93 [crates/gcode/src/index/security.rs:91-93]
  - Signature: `fn is_root_generated_dir(pattern: &str) -> bool {`
  - Purpose: Indexed function `is_root_generated_dir` in `crates/gcode/src/index/security.rs`. [crates/gcode/src/index/security.rs:91-93]
- `has_secret_extension` (function) component `has_secret_extension [function]` (`8eb85387-7bfe-51cc-aa21-2b86e14569b5`) lines 96-120 [crates/gcode/src/index/security.rs:96-120]
  - Signature: `pub fn has_secret_extension(path: &Path) -> bool {`
  - Purpose: Indexed function `has_secret_extension` in `crates/gcode/src/index/security.rs`. [crates/gcode/src/index/security.rs:96-120]
- `glob_match` (function) component `glob_match [function]` (`31c0a5dd-c5c8-5aaa-bb51-0d7a03b246fd`) lines 123-127 [crates/gcode/src/index/security.rs:123-127]
  - Signature: `pub fn glob_match(pattern: &str, text: &str) -> bool {`
  - Purpose: Indexed function `glob_match` in `crates/gcode/src/index/security.rs`. [crates/gcode/src/index/security.rs:123-127]
- `glob_inner` (function) component `glob_inner [function]` (`b011b000-658b-5ed7-bb2d-c7183aca80cd`) lines 129-148 [crates/gcode/src/index/security.rs:129-148]
  - Signature: `fn glob_inner(pattern: &[char], text: &[char]) -> bool {`
  - Purpose: Indexed function `glob_inner` in `crates/gcode/src/index/security.rs`. [crates/gcode/src/index/security.rs:129-148]

