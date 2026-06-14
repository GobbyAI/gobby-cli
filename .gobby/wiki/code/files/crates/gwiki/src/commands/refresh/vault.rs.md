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

This file provides helper routines for refreshing raw vault source assets: it resolves raw source paths, finds existing `raw/assets` files whose stem matches a given id, safely deletes superseded relative files, and validates that refresh paths stay under the scope root. The functions work together so a refresh can locate matching assets, remove outdated files without treating missing files as errors, and reject unsafe or out-of-vault relative paths before any deletion happens.
[crates/gwiki/src/commands/refresh/vault.rs:7-9]
[crates/gwiki/src/commands/refresh/vault.rs:16-49]
[crates/gwiki/src/commands/refresh/vault.rs:51-66]
[crates/gwiki/src/commands/refresh/vault.rs:68-101]
[crates/gwiki/src/commands/refresh/vault.rs:103-112]

## API Symbols

- `raw_source_path` (function) component `raw_source_path [function]` (`7ddeb860-4996-5c9e-a5de-5ea32fbaa3fe`) lines 7-9 [crates/gwiki/src/commands/refresh/vault.rs:7-9]
  - Signature: `pub(crate) fn raw_source_path(id: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `raw_source_path` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:7-9]
- `source_asset_paths_for_id` (function) component `source_asset_paths_for_id [function]` (`ae8e3acc-72e8-542f-a848-14c1b2142b96`) lines 16-49 [crates/gwiki/src/commands/refresh/vault.rs:16-49]
  - Signature: `pub(crate) fn source_asset_paths_for_id(`
  - Purpose: Indexed function `source_asset_paths_for_id` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:16-49]
- `remove_relative_file` (function) component `remove_relative_file [function]` (`9e8329db-1be0-5251-bd70-004062b7efbb`) lines 51-66 [crates/gwiki/src/commands/refresh/vault.rs:51-66]
  - Signature: `pub(crate) fn remove_relative_file(`
  - Purpose: Indexed function `remove_relative_file` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:51-66]
- `safe_refresh_relative_path` (function) component `safe_refresh_relative_path [function]` (`b8008095-9a22-5c29-9787-a87dec3b4a7d`) lines 68-101 [crates/gwiki/src/commands/refresh/vault.rs:68-101]
  - Signature: `fn safe_refresh_relative_path(relative_path: &Path) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `safe_refresh_relative_path` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:68-101]
- `ensure_scope_root` (function) component `ensure_scope_root [function]` (`28780a83-c6fe-5064-9065-eae3d4de0538`) lines 103-112 [crates/gwiki/src/commands/refresh/vault.rs:103-112]
  - Signature: `pub(crate) fn ensure_scope_root(root: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `ensure_scope_root` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:103-112]

