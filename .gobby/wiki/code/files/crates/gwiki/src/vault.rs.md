---
title: crates/gwiki/src/vault.rs
type: code_file
provenance:
- file: crates/gwiki/src/vault.rs
  ranges:
  - 18-21
  - 24-27
  - 53-58
  - 60-97
  - 99-135
  - 138-141
  - 143-149
  - 151-178
  - 180-216
  - 218-228
  - 230-249
  - 256-273
  - 276-301
  - 304-322
  - 325-344
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/vault.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/vault.rs` exposes 15 indexed API symbols.
[crates/gwiki/src/vault.rs:18-21]
[crates/gwiki/src/vault.rs:24-27]
[crates/gwiki/src/vault.rs:53-58]
[crates/gwiki/src/vault.rs:60-97]
[crates/gwiki/src/vault.rs:99-135]
[crates/gwiki/src/vault.rs:138-141]
[crates/gwiki/src/vault.rs:143-149]
[crates/gwiki/src/vault.rs:151-178]
[crates/gwiki/src/vault.rs:180-216]
[crates/gwiki/src/vault.rs:218-228]
[crates/gwiki/src/vault.rs:230-249]
[crates/gwiki/src/vault.rs:256-273]
[crates/gwiki/src/vault.rs:276-301]
[crates/gwiki/src/vault.rs:304-322]
[crates/gwiki/src/vault.rs:325-344]

## API Symbols

- `VaultPaths` (class) component `VaultPaths [class]` (`7460e2bb-8bbb-5913-ab06-9f2763e02f84`) lines 18-21 [crates/gwiki/src/vault.rs:18-21]
  - Signature: `pub struct VaultPaths {`
  - Purpose: Indexed class `VaultPaths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:18-21]
- `CreatedVaultPaths` (class) component `CreatedVaultPaths [class]` (`8b183387-1520-5b82-9c97-1bba6e0bb1f2`) lines 24-27 [crates/gwiki/src/vault.rs:24-27]
  - Signature: `pub struct CreatedVaultPaths {`
  - Purpose: Indexed class `CreatedVaultPaths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:24-27]
- `required_paths` (function) component `required_paths [function]` (`fee1312c-26f3-574f-a325-353bc30db9bf`) lines 53-58 [crates/gwiki/src/vault.rs:53-58]
  - Signature: `pub fn required_paths() -> VaultPaths {`
  - Purpose: Indexed function `required_paths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:53-58]
- `initialize` (function) component `initialize [function]` (`ac98dc01-3c70-56f5-8184-26e0738e9277`) lines 60-97 [crates/gwiki/src/vault.rs:60-97]
  - Signature: `pub fn initialize(scope: &ResolvedScope) -> Result<CreatedVaultPaths, WikiError> {`
  - Purpose: Indexed function `initialize` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:60-97]
- `cleanup_created` (function) component `cleanup_created [function]` (`a96c60de-d2ca-524a-94d8-1534c1d6c2f7`) lines 99-135 [crates/gwiki/src/vault.rs:99-135]
  - Signature: `pub fn cleanup_created(root: &Path, created: &CreatedVaultPaths) -> Result<(), WikiError> {`
  - Purpose: Indexed function `cleanup_created` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:99-135]
- `ScopeFile` (class) component `ScopeFile [class]` (`e5739909-382c-56af-b259-8f08aa56298b`) lines 138-141 [crates/gwiki/src/vault.rs:138-141]
  - Signature: `struct ScopeFile<'a> {`
  - Purpose: Indexed class `ScopeFile` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:138-141]
- `create_dir` (function) component `create_dir [function]` (`a5bd0051-fe3c-5297-b389-10a64038b431`) lines 143-149 [crates/gwiki/src/vault.rs:143-149]
  - Signature: `fn create_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `create_dir` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:143-149]
- `ensure_file` (function) component `ensure_file [function]` (`dbbcea7a-4cbc-5846-83d1-ccd453cf3347`) lines 151-178 [crates/gwiki/src/vault.rs:151-178]
  - Signature: `fn ensure_file(path: &Path, contents: &str) -> Result<bool, WikiError> {`
  - Purpose: Indexed function `ensure_file` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:151-178]
- `write_scope_file_atomically` (function) component `write_scope_file_atomically [function]` (`cd8fd6fb-a21e-568d-b2c3-c4ae2c221201`) lines 180-216 [crates/gwiki/src/vault.rs:180-216]
  - Signature: `fn write_scope_file_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Indexed function `write_scope_file_atomically` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:180-216]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`89b75acb-405d-5271-addc-3babaa7ca2a8`) lines 218-228 [crates/gwiki/src/vault.rs:218-228]
  - Signature: `fn temp_sibling_path(path: &Path) -> std::path::PathBuf {`
  - Purpose: Indexed function `temp_sibling_path` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:218-228]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`1dd99763-7700-5b19-9269-f07307844b6a`) lines 230-249 [crates/gwiki/src/vault.rs:230-249]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `sync_parent_dir` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:230-249]
- `vault_shape_lists_required_paths` (function) component `vault_shape_lists_required_paths [function]` (`b2a7d71f-58e6-5f0f-8579-d29751ff4eea`) lines 256-273 [crates/gwiki/src/vault.rs:256-273]
  - Signature: `fn vault_shape_lists_required_paths() {`
  - Purpose: Indexed function `vault_shape_lists_required_paths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:256-273]
- `default_files_drive_required_paths_and_contents` (function) component `default_files_drive_required_paths_and_contents [function]` (`4c2608fb-9dbf-55c0-8627-e67c18885215`) lines 276-301 [crates/gwiki/src/vault.rs:276-301]
  - Signature: `fn default_files_drive_required_paths_and_contents() {`
  - Purpose: Indexed function `default_files_drive_required_paths_and_contents` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:276-301]
- `initialize_overwrites_scope_file` (function) component `initialize_overwrites_scope_file [function]` (`465bb95e-dd29-592c-979d-7cc98336beea`) lines 304-322 [crates/gwiki/src/vault.rs:304-322]
  - Signature: `fn initialize_overwrites_scope_file() {`
  - Purpose: Indexed function `initialize_overwrites_scope_file` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:304-322]
- `cleanup_created_removes_only_created_vault_paths` (function) component `cleanup_created_removes_only_created_vault_paths [function]` (`86e6d33f-0054-5698-b93d-c502f1954b1d`) lines 325-344 [crates/gwiki/src/vault.rs:325-344]
  - Signature: `fn cleanup_created_removes_only_created_vault_paths() {`
  - Purpose: Indexed function `cleanup_created_removes_only_created_vault_paths` in `crates/gwiki/src/vault.rs`. [crates/gwiki/src/vault.rs:325-344]

