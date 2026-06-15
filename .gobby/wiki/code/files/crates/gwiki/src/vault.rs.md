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

# crates/gwiki/src/vault.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines and maintains the shared gwiki/codewiki vault shape. It declares the required directory manifest and default index files, exposes `required_paths()` for callers that need the expected layout, and implements `initialize()` to create missing directories and files under a resolved scope root while tracking which ones were newly created. It also writes `.gwiki/scope.json` atomically from the scope identity and root, provides `cleanup_created()` to remove only the paths that were created during setup, and includes small helpers for directory creation, conditional file creation, atomic temp-file replacement, and parent-directory syncing.
[crates/gwiki/src/vault.rs:19-22]
[crates/gwiki/src/vault.rs:25-28]
[crates/gwiki/src/vault.rs:55-60]
[crates/gwiki/src/vault.rs:62-99]
[crates/gwiki/src/vault.rs:101-137]

## API Symbols

- `VaultPaths` (class) component `VaultPaths [class]` (`0433aeb7-39e7-56c5-8fe7-6dbdd014402a`) lines 19-22 [crates/gwiki/src/vault.rs:19-22]
  - Signature: `pub struct VaultPaths {`
  - Purpose: `VaultPaths` is a path manifest struct that stores a static slice of vault directory names and a vector of static file names. [crates/gwiki/src/vault.rs:19-22]
- `CreatedVaultPaths` (class) component `CreatedVaultPaths [class]` (`9003c07a-c018-5b3e-b2bd-13a9e1d98877`) lines 25-28 [crates/gwiki/src/vault.rs:25-28]
  - Signature: `pub struct CreatedVaultPaths {`
  - Purpose: `CreatedVaultPaths` is a simple record type that tracks the string paths of directories and files created during a vault creation operation in separate `Vec<String>` fields. [crates/gwiki/src/vault.rs:25-28]
- `required_paths` (function) component `required_paths [function]` (`46cbefbd-c277-5d47-84ff-c1fb4884188f`) lines 55-60 [crates/gwiki/src/vault.rs:55-60]
  - Signature: `pub fn required_paths() -> VaultPaths {`
  - Purpose: Constructs and returns a `VaultPaths` with `directories` set to `DIRECTORIES` and `files` populated by collecting the path entries from `DEFAULT_FILES`. [crates/gwiki/src/vault.rs:55-60]
- `initialize` (function) component `initialize [function]` (`9deaf6bb-98b8-5a3f-a804-aa2d569b81a8`) lines 62-99 [crates/gwiki/src/vault.rs:62-99]
  - Signature: `pub fn initialize(scope: &ResolvedScope) -> Result<CreatedVaultPaths, WikiError> {`
  - Purpose: `initialize` ensures the vault root contains the required directory structure and default files, writes `.gwiki/scope.json` atomically from the scope identity and root path, and returns the set of directories and files that were newly created. [crates/gwiki/src/vault.rs:62-99]
- `cleanup_created` (function) component `cleanup_created [function]` (`05bd5ec2-4638-5321-b9b6-3b1a7ff4aee8`) lines 101-137 [crates/gwiki/src/vault.rs:101-137]
  - Signature: `pub fn cleanup_created(root: &Path, created: &CreatedVaultPaths) -> Result<(), WikiError> {`
  - Purpose: Deletes each path recorded in `created.files` and then removes `created.directories` in reverse order, ignoring `NotFound` for files and `NotFound` or `DirectoryNotEmpty` for directories, while returning a `WikiError::Io` for any other filesystem error. [crates/gwiki/src/vault.rs:101-137]
- `ScopeFile` (class) component `ScopeFile [class]` (`42c150a9-b9df-5d3b-863e-db0bf4c84b8b`) lines 140-143 [crates/gwiki/src/vault.rs:140-143]
  - Signature: `struct ScopeFile<'a> {`
  - Purpose: `ScopeFile<'a>` is a lifetime-parameterized Rust struct that holds borrowed string slices for a scope’s `identity` and `root` fields. [crates/gwiki/src/vault.rs:140-143]
- `create_dir` (function) component `create_dir [function]` (`f32e550a-c2b7-50fb-9e3c-ba86d901a5a4`) lines 145-151 [crates/gwiki/src/vault.rs:145-151]
  - Signature: `fn create_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Creates the target directory and any missing parents with `std::fs::create_dir_all`, converting any I/O failure into `WikiError::Io` annotated with the `"create directory"` action and the affected path. [crates/gwiki/src/vault.rs:145-151]
- `ensure_file` (function) component `ensure_file [function]` (`2bd832f1-7d3b-5934-8be7-5052c11aeaba`) lines 153-180 [crates/gwiki/src/vault.rs:153-180]
  - Signature: `fn ensure_file(path: &Path, contents: &str) -> Result<bool, WikiError> {`
  - Purpose: Creates the parent directory if needed, then atomically attempts to create `path` only if it does not already exist, writes `contents` to the new file, deletes it and returns a write error on partial write failure, returns `Ok(true)` if created, `Ok(false)` if the file already existed, and otherwise wraps creation I/O failures in `WikiError::Io`. [crates/gwiki/src/vault.rs:153-180]
- `write_scope_file_atomically` (function) component `write_scope_file_atomically [function]` (`371c0e25-ab4a-55df-aadf-d6d90c3200e9`) lines 182-218 [crates/gwiki/src/vault.rs:182-218]
  - Signature: `fn write_scope_file_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Creates the parent directory if needed, writes `contents` to a temporary sibling file, fsyncs it, atomically renames it into `path`, and then syncs the parent directory, cleaning up the temp file and returning a `WikiError::Io` on any I/O failure. [crates/gwiki/src/vault.rs:182-218]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`4225e946-4a3b-5823-a2e7-dfb08342091c`) lines 220-230 [crates/gwiki/src/vault.rs:220-230]
  - Signature: `fn temp_sibling_path(path: &Path) -> std::path::PathBuf {`
  - Purpose: Returns a sibling temporary `PathBuf` by replacing the input path’s filename with a dot-prefixed `.{original_or_scope.json}.{process_id}.{unix_nanos}.tmp` name, using `"scope.json"` when the original filename is missing or invalid UTF-8. [crates/gwiki/src/vault.rs:220-230]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`85cc7a94-2779-527f-b183-d346b699098d`) lines 232-251 [crates/gwiki/src/vault.rs:232-251]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix, `sync_parent_dir` opens the parent directory of `path` and calls `sync_all()` to flush its metadata to disk, returning a `WikiError::Io` on failure, while on non-Unix platforms it is a no-op. [crates/gwiki/src/vault.rs:232-251]
- `vault_shape_lists_required_paths` (function) component `vault_shape_lists_required_paths [function]` (`845dfe34-4c30-5889-87ea-8be3bdba301e`) lines 258-275 [crates/gwiki/src/vault.rs:258-275]
  - Signature: `fn vault_shape_lists_required_paths() {`
  - Purpose: This test function calls `required_paths()` and asserts that the returned vault shape includes a fixed set of required directories (`raw/assets`, `code`, `knowledge`, `_meta`, `knowledge/sources`, `knowledge/concepts`, `knowledge/topics`, `outputs`, `meta/health`) and files (`raw/INDEX.md`, `knowledge/INDEX.md`, `code/INDEX.md`, `_index.md`, `log.md`). [crates/gwiki/src/vault.rs:258-275]
- `default_files_drive_required_paths_and_contents` (function) component `default_files_drive_required_paths_and_contents [function]` (`d8d3f30b-c0cd-55ad-a923-f0a8b4e54954`) lines 278-303 [crates/gwiki/src/vault.rs:278-303]
  - Signature: `fn default_files_drive_required_paths_and_contents() {`
  - Purpose: This test verifies that `initialize(&scope)` creates every file in `DEFAULT_FILES` under the topic root with exact expected contents, and that `required_paths().files` matches the default file path list. [crates/gwiki/src/vault.rs:278-303]
- `initialize_overwrites_scope_file` (function) component `initialize_overwrites_scope_file [function]` (`722b3e70-0ef4-5c9e-9a25-4cda6ba8f668`) lines 306-324 [crates/gwiki/src/vault.rs:306-324]
  - Signature: `fn initialize_overwrites_scope_file() {`
  - Purpose: It verifies that calling `initialize` twice for a topic scope rewrites `wiki/.gwiki/scope.json` with the current `topic:rust` content, replaces any stale file contents, and does not classify that scope file as newly created. [crates/gwiki/src/vault.rs:306-324]
- `cleanup_created_removes_only_created_vault_paths` (function) component `cleanup_created_removes_only_created_vault_paths [function]` (`30472266-4128-599e-ad8f-06d79314f59b`) lines 327-346 [crates/gwiki/src/vault.rs:327-346]
  - Signature: `fn cleanup_created_removes_only_created_vault_paths() {`
  - Purpose: It verifies that `cleanup_created(&root, &created)` deletes only the files and directories recorded in `created` under `root` while leaving the root directory itself intact. [crates/gwiki/src/vault.rs:327-346]

