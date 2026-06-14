---
title: crates/gwiki/src/log.rs
type: code_file
provenance:
- file: crates/gwiki/src/log.rs
  ranges:
  - 9-15
  - 19-22
  - 25-49
  - 52-90
  - 93-108
  - 111-117
  - 121-128
  - 131-150
  - 153-155
  - 158-164
  - 167-174
  - 183-211
  - 214-233
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/log.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the log-writing model for `gwiki`: `LogEntry` captures a timestamped scoped action with a summary and artifact paths, and `LogWriteReport` returns the scope log path plus an optional mirrored global log path. `append_logs` writes each entry to the scope `log.md` first, then mirrors it to the global log only if configured and not the same file, so the scope log remains the source of truth. The lower-level helpers handle creating parent directories, opening/appending the file, writing the log header and rendered entry text, comparing paths and file identities, and resolving fallback paths; the tests verify that scope and global logs are both written when distinct and only written once when they refer to the same underlying file.
[crates/gwiki/src/log.rs:9-15]
[crates/gwiki/src/log.rs:19-22]
[crates/gwiki/src/log.rs:25-49]
[crates/gwiki/src/log.rs:52-90]
[crates/gwiki/src/log.rs:93-108]

## API Symbols

- `LogEntry` (class) component `LogEntry [class]` (`47249c61-90eb-5016-a137-1f84e94def71`) lines 9-15 [crates/gwiki/src/log.rs:9-15]
  - Signature: `pub struct LogEntry {`
  - Purpose: Indexed class `LogEntry` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:9-15]
- `LogWriteReport` (class) component `LogWriteReport [class]` (`155406c5-4669-5972-ae59-43f52b041264`) lines 19-22 [crates/gwiki/src/log.rs:19-22]
  - Signature: `pub struct LogWriteReport {`
  - Purpose: Indexed class `LogWriteReport` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:19-22]
- `append_logs` (function) component `append_logs [function]` (`e25c78fd-9fad-5d50-ac2e-0f30fc7cf0d4`) lines 25-49 [crates/gwiki/src/log.rs:25-49]
  - Signature: `pub fn append_logs(`
  - Purpose: Indexed function `append_logs` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:25-49]
- `append_log` (function) component `append_log [function]` (`5a81c5f5-59c0-5a9a-b384-dffa85b8a546`) lines 52-90 [crates/gwiki/src/log.rs:52-90]
  - Signature: `fn append_log(path: &Path, entry: &LogEntry) -> Result<(), WikiError> {`
  - Purpose: Indexed function `append_log` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:52-90]
- `render_entry` (function) component `render_entry [function]` (`c901ce57-f6ac-5378-9cff-d0c90c33fe47`) lines 93-108 [crates/gwiki/src/log.rs:93-108]
  - Signature: `fn render_entry(entry: &LogEntry) -> String {`
  - Purpose: Indexed function `render_entry` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:93-108]
- `same_log_path` (function) component `same_log_path [function]` (`2061b5d6-09ae-519b-81a7-dfb43d19c803`) lines 111-117 [crates/gwiki/src/log.rs:111-117]
  - Signature: `fn same_log_path(left: &Path, right: &Path) -> bool {`
  - Purpose: Indexed function `same_log_path` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:111-117]
- `same_file_identity` (function) component `same_file_identity [function]` (`daf9baeb-a7d2-5d26-bd81-7e9e6e73a25d`) lines 121-128 [crates/gwiki/src/log.rs:121-128]
  - Signature: `fn same_file_identity(left: &Path, right: &Path) -> bool {`
  - Purpose: Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:121-128]
- `same_file_identity` (function) component `same_file_identity [function]` (`3369600f-19cf-5eb7-bfaa-0f3febdffc27`) lines 131-150 [crates/gwiki/src/log.rs:131-150]
  - Signature: `fn same_file_identity(left: &Path, right: &Path) -> bool {`
  - Purpose: Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:131-150]
- `identity` (function) component `identity [function]` (`1b3d975f-81ca-57fe-9355-230c91ee4f52`) lines 134-144 [crates/gwiki/src/log.rs:134-144]
  - Signature: `fn identity(path: &Path) -> Option<(u32, u32, u32)> {`
  - Purpose: Indexed function `identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:134-144]
- `same_file_identity` (function) component `same_file_identity [function]` (`13c7499a-efc1-596f-a7e0-631a33814bbc`) lines 153-155 [crates/gwiki/src/log.rs:153-155]
  - Signature: `fn same_file_identity(_left: &Path, _right: &Path) -> bool {`
  - Purpose: Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:153-155]
- `resolved_log_path` (function) component `resolved_log_path [function]` (`feecdee7-b91b-5ad5-8e7d-3c44fde84722`) lines 158-164 [crates/gwiki/src/log.rs:158-164]
  - Signature: `fn resolved_log_path(path: &Path) -> PathBuf {`
  - Purpose: Indexed function `resolved_log_path` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:158-164]
- `resolve_log_path_fallback` (function) component `resolve_log_path_fallback [function]` (`15a03020-97f3-53aa-a339-085717550af0`) lines 167-174 [crates/gwiki/src/log.rs:167-174]
  - Signature: `fn resolve_log_path_fallback(path: &Path) -> PathBuf {`
  - Purpose: Indexed function `resolve_log_path_fallback` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:167-174]
- `writes_scope_and_global_logs` (function) component `writes_scope_and_global_logs [function]` (`29419c8a-9ca7-5c5e-9f37-f78a78ae1be9`) lines 183-211 [crates/gwiki/src/log.rs:183-211]
  - Signature: `fn writes_scope_and_global_logs() {`
  - Purpose: Indexed function `writes_scope_and_global_logs` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:183-211]
- `does_not_append_twice_when_scope_and_global_logs_match` (function) component `does_not_append_twice_when_scope_and_global_logs_match [function]` (`bdf78f1d-bfe3-5b48-84db-656d1f7eb4d9`) lines 214-233 [crates/gwiki/src/log.rs:214-233]
  - Signature: `fn does_not_append_twice_when_scope_and_global_logs_match() {`
  - Purpose: Indexed function `does_not_append_twice_when_scope_and_global_logs_match` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:214-233]

