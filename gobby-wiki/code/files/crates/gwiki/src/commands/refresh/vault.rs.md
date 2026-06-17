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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/refresh/vault.rs:7-9](crates/gwiki/src/commands/refresh/vault.rs#L7-L9), [crates/gwiki/src/commands/refresh/vault.rs:16-49](crates/gwiki/src/commands/refresh/vault.rs#L16-L49), [crates/gwiki/src/commands/refresh/vault.rs:51-66](crates/gwiki/src/commands/refresh/vault.rs#L51-L66), [crates/gwiki/src/commands/refresh/vault.rs:68-101](crates/gwiki/src/commands/refresh/vault.rs#L68-L101), [crates/gwiki/src/commands/refresh/vault.rs:103-112](crates/gwiki/src/commands/refresh/vault.rs#L103-L112)

</details>

# crates/gwiki/src/commands/refresh/vault.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

This file provides refresh-time vault path helpers for locating, matching, and removing raw source files safely. `raw_source_path` delegates raw source path resolution to the shared `paths` module, `source_asset_paths_for_id` scans `raw/assets` for vault-relative asset files whose stem matches a trimmed id, `remove_relative_file` validates a relative path before deleting the corresponding file and treats missing files as a non-error, `safe_refresh_relative_path` enforces that refresh paths stay within the allowed vault-relative scope, and `ensure_scope_root` supports that scope check. Together, these helpers let the refresh command find superseded assets and clean them up without escaping the vault root.
[crates/gwiki/src/commands/refresh/vault.rs:7-9]
[crates/gwiki/src/commands/refresh/vault.rs:16-49]
[crates/gwiki/src/commands/refresh/vault.rs:51-66]
[crates/gwiki/src/commands/refresh/vault.rs:68-101]
[crates/gwiki/src/commands/refresh/vault.rs:103-112]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `raw_source_path` | function | `pub(crate) fn raw_source_path(id: &str) -> Result<PathBuf, WikiError> {` | `raw_source_path [function]` | `7ddeb860-4996-5c9e-a5de-5ea32fbaa3fe` | 7-9 [crates/gwiki/src/commands/refresh/vault.rs:7-9] | Indexed function `raw_source_path` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:7-9] |
| `source_asset_paths_for_id` | function | `pub(crate) fn source_asset_paths_for_id(` | `source_asset_paths_for_id [function]` | `ae8e3acc-72e8-542f-a848-14c1b2142b96` | 16-49 [crates/gwiki/src/commands/refresh/vault.rs:16-49] | Indexed function `source_asset_paths_for_id` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:16-49] |
| `remove_relative_file` | function | `pub(crate) fn remove_relative_file(` | `remove_relative_file [function]` | `9e8329db-1be0-5251-bd70-004062b7efbb` | 51-66 [crates/gwiki/src/commands/refresh/vault.rs:51-66] | Indexed function `remove_relative_file` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:51-66] |
| `safe_refresh_relative_path` | function | `fn safe_refresh_relative_path(relative_path: &Path) -> Result<PathBuf, WikiError> {` | `safe_refresh_relative_path [function]` | `b8008095-9a22-5c29-9787-a87dec3b4a7d` | 68-101 [crates/gwiki/src/commands/refresh/vault.rs:68-101] | Indexed function `safe_refresh_relative_path` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:68-101] |
| `ensure_scope_root` | function | `pub(crate) fn ensure_scope_root(root: &Path) -> Result<(), WikiError> {` | `ensure_scope_root [function]` | `28780a83-c6fe-5064-9065-eae3d4de0538` | 103-112 [crates/gwiki/src/commands/refresh/vault.rs:103-112] | Indexed function `ensure_scope_root` in `crates/gwiki/src/commands/refresh/vault.rs`. [crates/gwiki/src/commands/refresh/vault.rs:103-112] |
