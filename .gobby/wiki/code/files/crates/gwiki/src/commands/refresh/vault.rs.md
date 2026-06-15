---
title: crates/gwiki/src/commands/refresh/vault.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/vault.rs
  ranges:
  - 7-9
  - 16-49
  - 51-66
  - 68-101
  - 103-112
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/vault.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

This file provides vault-scoped path and cleanup helpers for the refresh command. It delegates raw source path lookup to `paths::raw_source_path`, scans `raw/assets` for asset files whose stem matches a trimmed ID, safely normalizes vault-relative paths before deleting superseded files, and verifies that a scope root directory exists before refresh work proceeds.
[crates/gwiki/src/commands/refresh/vault.rs:7-9]
[crates/gwiki/src/commands/refresh/vault.rs:16-49]
[crates/gwiki/src/commands/refresh/vault.rs:51-66]
[crates/gwiki/src/commands/refresh/vault.rs:68-101]
[crates/gwiki/src/commands/refresh/vault.rs:103-112]

## API Symbols

- `raw_source_path` (function) component `raw_source_path [function]` (`7ddeb860-4996-5c9e-a5de-5ea32fbaa3fe`) lines 7-9 [crates/gwiki/src/commands/refresh/vault.rs:7-9]
  - Signature: `pub(crate) fn raw_source_path(id: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Returns the raw source file path for the given 'id' by delegating to 'paths::raw_source_path(id)', propagating the resulting 'PathBuf' or 'WikiError'. [crates/gwiki/src/commands/refresh/vault.rs:7-9]
- `source_asset_paths_for_id` (function) component `source_asset_paths_for_id [function]` (`ae8e3acc-72e8-542f-a848-14c1b2142b96`) lines 16-49 [crates/gwiki/src/commands/refresh/vault.rs:16-49]
  - Signature: `pub(crate) fn source_asset_paths_for_id(`
  - Purpose: Returns every 'raw/assets/*' file under 'vault_root' whose filename stem exactly matches the trimmed 'id' and has a non-empty extension, or an empty list if the asset directory does not exist. [crates/gwiki/src/commands/refresh/vault.rs:16-49]
- `remove_relative_file` (function) component `remove_relative_file [function]` (`9e8329db-1be0-5251-bd70-004062b7efbb`) lines 51-66 [crates/gwiki/src/commands/refresh/vault.rs:51-66]
  - Signature: `pub(crate) fn remove_relative_file(`
  - Purpose: Normalizes the given relative path with 'safe_refresh_relative_path', joins it to 'vault_root', deletes the resulting file, returns 'Ok(true)' if removal succeeds, 'Ok(false)' if the file does not exist, and wraps any other I/O failure in 'WikiError::Io'. [crates/gwiki/src/commands/refresh/vault.rs:51-66]
- `safe_refresh_relative_path` (function) component `safe_refresh_relative_path [function]` (`b8008095-9a22-5c29-9787-a87dec3b4a7d`) lines 68-101 [crates/gwiki/src/commands/refresh/vault.rs:68-101]
  - Signature: `fn safe_refresh_relative_path(relative_path: &Path) -> Result<PathBuf, WikiError> {`
  - Purpose: Validates that 'relative_path' is non-empty, vault-relative, and contains at least one normal path component by rejecting root, prefix, parent-directory, and empty-only inputs, then returns a normalized 'PathBuf' with '.' components removed. [crates/gwiki/src/commands/refresh/vault.rs:68-101]
- `ensure_scope_root` (function) component `ensure_scope_root [function]` (`28780a83-c6fe-5064-9065-eae3d4de0538`) lines 103-112 [crates/gwiki/src/commands/refresh/vault.rs:103-112]
  - Signature: `pub(crate) fn ensure_scope_root(root: &Path) -> Result<(), WikiError> {`
  - Purpose: Returns 'Ok(())' when 'root' exists as a directory, otherwise returns 'WikiError::NotFound' identifying the missing wiki scope by the path string. [crates/gwiki/src/commands/refresh/vault.rs:103-112]

