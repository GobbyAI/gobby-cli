---
title: crates/gwiki/src/vault.rs
type: code_file
provenance:
- file: crates/gwiki/src/vault.rs
  ranges:
  - 19-22
  - 25-28
  - 55-60
  - 62-99
  - 101-137
  - 140-143
  - 145-151
  - 153-180
  - 182-218
  - 220-230
  - 232-251
  - 258-275
  - 278-303
  - 306-324
  - 327-346
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/vault.rs:19-22](crates/gwiki/src/vault.rs#L19-L22), [crates/gwiki/src/vault.rs:25-28](crates/gwiki/src/vault.rs#L25-L28), [crates/gwiki/src/vault.rs:55-60](crates/gwiki/src/vault.rs#L55-L60), [crates/gwiki/src/vault.rs:62-99](crates/gwiki/src/vault.rs#L62-L99), [crates/gwiki/src/vault.rs:101-137](crates/gwiki/src/vault.rs#L101-L137), [crates/gwiki/src/vault.rs:140-143](crates/gwiki/src/vault.rs#L140-L143), [crates/gwiki/src/vault.rs:145-151](crates/gwiki/src/vault.rs#L145-L151), [crates/gwiki/src/vault.rs:153-180](crates/gwiki/src/vault.rs#L153-L180), [crates/gwiki/src/vault.rs:182-218](crates/gwiki/src/vault.rs#L182-L218), [crates/gwiki/src/vault.rs:220-230](crates/gwiki/src/vault.rs#L220-L230), [crates/gwiki/src/vault.rs:232-251](crates/gwiki/src/vault.rs#L232-L251), [crates/gwiki/src/vault.rs:258-275](crates/gwiki/src/vault.rs#L258-L275), [crates/gwiki/src/vault.rs:278-303](crates/gwiki/src/vault.rs#L278-L303), [crates/gwiki/src/vault.rs:306-324](crates/gwiki/src/vault.rs#L306-L324), [crates/gwiki/src/vault.rs:327-346](crates/gwiki/src/vault.rs#L327-L346)

</details>

# crates/gwiki/src/vault.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the shared Obsidian vault layout for `gwiki` and provides setup/teardown utilities for it. `VaultPaths` and `CreatedVaultPaths` describe the required directories/files and what was actually created, `required_paths` exposes the static layout, `initialize` creates the directory tree and default files plus the `.gwiki/scope.json` scope record, and `cleanup_created` removes only the paths reported as newly created; the helper functions handle directory creation, file creation, atomic scope-file writes, temp sibling naming, and parent-directory syncing, with the remaining functions covering path computation and behavior checks around the vault shape and default contents.
[crates/gwiki/src/vault.rs:19-22]
[crates/gwiki/src/vault.rs:25-28]
[crates/gwiki/src/vault.rs:55-60]
[crates/gwiki/src/vault.rs:62-99]
[crates/gwiki/src/vault.rs:101-137]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `VaultPaths` | class | `pub struct VaultPaths {` | `VaultPaths [class]` | `0433aeb7-39e7-56c5-8fe7-6dbdd014402a` | 19-22 [crates/gwiki/src/vault.rs:19-22] | Indexed class `VaultPaths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:19-22] |
| `CreatedVaultPaths` | class | `pub struct CreatedVaultPaths {` | `CreatedVaultPaths [class]` | `9003c07a-c018-5b3e-b2bd-13a9e1d98877` | 25-28 [crates/gwiki/src/vault.rs:25-28] | Indexed class `CreatedVaultPaths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:25-28] |
| `required_paths` | function | `pub fn required_paths() -> VaultPaths {` | `required_paths [function]` | `46cbefbd-c277-5d47-84ff-c1fb4884188f` | 55-60 [crates/gwiki/src/vault.rs:55-60] | Indexed function `required_paths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:55-60] |
| `initialize` | function | `pub fn initialize(scope: &ResolvedScope) -> Result<CreatedVaultPaths, WikiError> {` | `initialize [function]` | `9deaf6bb-98b8-5a3f-a804-aa2d569b81a8` | 62-99 [crates/gwiki/src/vault.rs:62-99] | Indexed function `initialize` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:62-99] |
| `cleanup_created` | function | `pub fn cleanup_created(root: &Path, created: &CreatedVaultPaths) -> Result<(), WikiError> {` | `cleanup_created [function]` | `05bd5ec2-4638-5321-b9b6-3b1a7ff4aee8` | 101-137 [crates/gwiki/src/vault.rs:101-137] | Indexed function `cleanup_created` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:101-137] |
| `ScopeFile` | class | `struct ScopeFile<'a> {` | `ScopeFile [class]` | `42c150a9-b9df-5d3b-863e-db0bf4c84b8b` | 140-143 [crates/gwiki/src/vault.rs:140-143] | Indexed class `ScopeFile` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:140-143] |
| `create_dir` | function | `fn create_dir(path: &Path) -> Result<(), WikiError> {` | `create_dir [function]` | `f32e550a-c2b7-50fb-9e3c-ba86d901a5a4` | 145-151 [crates/gwiki/src/vault.rs:145-151] | Indexed function `create_dir` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:145-151] |
| `ensure_file` | function | `fn ensure_file(path: &Path, contents: &str) -> Result<bool, WikiError> {` | `ensure_file [function]` | `2bd832f1-7d3b-5934-8be7-5052c11aeaba` | 153-180 [crates/gwiki/src/vault.rs:153-180] | Indexed function `ensure_file` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:153-180] |
| `write_scope_file_atomically` | function | `fn write_scope_file_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {` | `write_scope_file_atomically [function]` | `371c0e25-ab4a-55df-aadf-d6d90c3200e9` | 182-218 [crates/gwiki/src/vault.rs:182-218] | Indexed function `write_scope_file_atomically` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:182-218] |
| `temp_sibling_path` | function | `fn temp_sibling_path(path: &Path) -> std::path::PathBuf {` | `temp_sibling_path [function]` | `4225e946-4a3b-5823-a2e7-dfb08342091c` | 220-230 [crates/gwiki/src/vault.rs:220-230] | Indexed function `temp_sibling_path` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:220-230] |
| `sync_parent_dir` | function | `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {` | `sync_parent_dir [function]` | `85cc7a94-2779-527f-b183-d346b699098d` | 232-251 [crates/gwiki/src/vault.rs:232-251] | Indexed function `sync_parent_dir` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:232-251] |
| `vault_shape_lists_required_paths` | function | `fn vault_shape_lists_required_paths() {` | `vault_shape_lists_required_paths [function]` | `845dfe34-4c30-5889-87ea-8be3bdba301e` | 258-275 [crates/gwiki/src/vault.rs:258-275] | Indexed function `vault_shape_lists_required_paths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:258-275] |
| `default_files_drive_required_paths_and_contents` | function | `fn default_files_drive_required_paths_and_contents() {` | `default_files_drive_required_paths_and_contents [function]` | `d8d3f30b-c0cd-55ad-a923-f0a8b4e54954` | 278-303 [crates/gwiki/src/vault.rs:278-303] | Indexed function `default_files_drive_required_paths_and_contents` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:278-303] |
| `initialize_overwrites_scope_file` | function | `fn initialize_overwrites_scope_file() {` | `initialize_overwrites_scope_file [function]` | `722b3e70-0ef4-5c9e-9a25-4cda6ba8f668` | 306-324 [crates/gwiki/src/vault.rs:306-324] | Indexed function `initialize_overwrites_scope_file` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:306-324] |
| `cleanup_created_removes_only_created_vault_paths` | function | `fn cleanup_created_removes_only_created_vault_paths() {` | `cleanup_created_removes_only_created_vault_paths [function]` | `30472266-4128-599e-ad8f-06d79314f59b` | 327-346 [crates/gwiki/src/vault.rs:327-346] | Indexed function `cleanup_created_removes_only_created_vault_paths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:327-346] |
