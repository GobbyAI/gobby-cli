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

This file defines the log data model and write path for gwiki. `LogEntry` captures a timestamped scope action with summary text and artifact paths, while `append_logs` writes that entry to the scope’s `log.md` and, if configured, mirrors it to a global hub log unless both paths resolve to the same file. The lower-level `append_log` helper creates parent directories, opens the log in append mode, inserts the `# Log` header for new files, and appends the rendered Markdown entry. `render_entry` turns an entry into the final Markdown format, and the path/identity helpers prevent duplicate writes by comparing canonical paths or filesystem identities across platforms. The tests verify both the dual-write behavior and the single-write case when scope and global logs alias the same file.
[crates/gwiki/src/log.rs:9-15]
[crates/gwiki/src/log.rs:19-22]
[crates/gwiki/src/log.rs:25-49]
[crates/gwiki/src/log.rs:52-90]
[crates/gwiki/src/log.rs:93-108]

## API Symbols

- `LogEntry` (class) component `LogEntry [class]` (`47249c61-90eb-5016-a137-1f84e94def71`) lines 9-15 [crates/gwiki/src/log.rs:9-15]
  - Signature: `pub struct LogEntry {`
  - Purpose: 'LogEntry' is a record type representing a logged event with a timestamp, a 'ScopeIdentity' scope, an action name, a textual summary, and a list of artifact file paths. [crates/gwiki/src/log.rs:9-15]
- `LogWriteReport` (class) component `LogWriteReport [class]` (`155406c5-4669-5972-ae59-43f52b041264`) lines 19-22 [crates/gwiki/src/log.rs:19-22]
  - Signature: `pub struct LogWriteReport {`
  - Purpose: 'LogWriteReport' records the file path of a scope-specific log and, optionally, the file path of a global log associated with the same write operation. [crates/gwiki/src/log.rs:19-22]
- `append_logs` (function) component `append_logs [function]` (`e25c78fd-9fad-5d50-ac2e-0f30fc7cf0d4`) lines 25-49 [crates/gwiki/src/log.rs:25-49]
  - Signature: `pub fn append_logs(`
  - Purpose: Appends a 'LogEntry' to 'scope_root/log.md', then conditionally mirrors the same entry to 'global_hub_root/log.md' only if it is a different path, returning both write targets in a 'LogWriteReport'. [crates/gwiki/src/log.rs:25-49]
- `append_log` (function) component `append_log [function]` (`5a81c5f5-59c0-5a9a-b384-dffa85b8a546`) lines 52-90 [crates/gwiki/src/log.rs:52-90]
  - Signature: `fn append_log(path: &Path, entry: &LogEntry) -> Result<(), WikiError> {`
  - Purpose: Creates the log file’s parent directory if needed, opens the file in append mode, writes a '# Log' header when the file is empty, and appends the rendered 'LogEntry', mapping any I/O failure to 'WikiError::Io'. [crates/gwiki/src/log.rs:52-90]
- `render_entry` (function) component `render_entry [function]` (`c901ce57-f6ac-5378-9cff-d0c90c33fe47`) lines 93-108 [crates/gwiki/src/log.rs:93-108]
  - Signature: `fn render_entry(entry: &LogEntry) -> String {`
  - Purpose: Formats a 'LogEntry' into a Markdown string with a heading containing timestamp and action, a scope line, the summary text, and an optional bullet list of artifact display paths, then appends a trailing blank line. [crates/gwiki/src/log.rs:93-108]
- `same_log_path` (function) component `same_log_path [function]` (`2061b5d6-09ae-519b-81a7-dfb43d19c803`) lines 111-117 [crates/gwiki/src/log.rs:111-117]
  - Signature: `fn same_log_path(left: &Path, right: &Path) -> bool {`
  - Purpose: Returns 'true' when two log paths resolve to the same canonical log location or refer to the same underlying file identity, preventing duplicate entries for aliases. [crates/gwiki/src/log.rs:111-117]
- `same_file_identity` (function) component `same_file_identity [function]` (`daf9baeb-a7d2-5d26-bd81-7e9e6e73a25d`) lines 121-128 [crates/gwiki/src/log.rs:121-128]
  - Signature: `fn same_file_identity(left: &Path, right: &Path) -> bool {`
  - Purpose: Returns 'true' only when both paths resolve successfully to metadata on Unix and refer to the same filesystem inode, as determined by equal device and inode numbers; otherwise returns 'false'. [crates/gwiki/src/log.rs:121-128]
- `same_file_identity` (function) component `same_file_identity [function]` (`3369600f-19cf-5eb7-bfaa-0f3febdffc27`) lines 131-150 [crates/gwiki/src/log.rs:131-150]
  - Signature: `fn same_file_identity(left: &Path, right: &Path) -> bool {`
  - Purpose: Returns 'true' only when both paths’ Windows metadata yields a nonzero '(volume serial number, file index high, file index low)' tuple and those tuples are equal, otherwise 'false'. [crates/gwiki/src/log.rs:131-150]
- `identity` (function) component `identity [function]` (`1b3d975f-81ca-57fe-9355-230c91ee4f52`) lines 134-144 [crates/gwiki/src/log.rs:134-144]
  - Signature: `fn identity(path: &Path) -> Option<(u32, u32, u32)> {`
  - Purpose: Returns 'None' if 'std::fs::metadata(path)' fails or both file index parts are zero, otherwise returns 'Some((volume_serial_number, file_index_high, file_index_low))' for the path. [crates/gwiki/src/log.rs:134-144]
- `same_file_identity` (function) component `same_file_identity [function]` (`13c7499a-efc1-596f-a7e0-631a33814bbc`) lines 153-155 [crates/gwiki/src/log.rs:153-155]
  - Signature: `fn same_file_identity(_left: &Path, _right: &Path) -> bool {`
  - Purpose: Returns 'false' for every pair of paths, indicating no file identity is ever considered a match. [crates/gwiki/src/log.rs:153-155]
- `resolved_log_path` (function) component `resolved_log_path [function]` (`feecdee7-b91b-5ad5-8e7d-3c44fde84722`) lines 158-164 [crates/gwiki/src/log.rs:158-164]
  - Signature: `fn resolved_log_path(path: &Path) -> PathBuf {`
  - Purpose: Returns the canonicalized version of 'path' when 'canonicalize()' succeeds, otherwise falls back to 'resolve_log_path_fallback(path)' to produce a 'PathBuf'. [crates/gwiki/src/log.rs:158-164]
- `resolve_log_path_fallback` (function) component `resolve_log_path_fallback [function]` (`15a03020-97f3-53aa-a339-085717550af0`) lines 167-174 [crates/gwiki/src/log.rs:167-174]
  - Signature: `fn resolve_log_path_fallback(path: &Path) -> PathBuf {`
  - Purpose: Returns the canonicalized parent directory joined with the original filename when the parent can be resolved, otherwise returns the input path unchanged. [crates/gwiki/src/log.rs:167-174]
- `writes_scope_and_global_logs` (function) component `writes_scope_and_global_logs [function]` (`29419c8a-9ca7-5c5e-9f37-f78a78ae1be9`) lines 183-211 [crates/gwiki/src/log.rs:183-211]
  - Signature: `fn writes_scope_and_global_logs() {`
  - Purpose: Verifies that 'append_logs' writes the same formatted log entry to both the scope-specific 'log.md' and the optional global 'hub/log.md', and returns the expected output paths. [crates/gwiki/src/log.rs:183-211]
- `does_not_append_twice_when_scope_and_global_logs_match` (function) component `does_not_append_twice_when_scope_and_global_logs_match [function]` (`bdf78f1d-bfe3-5b48-84db-656d1f7eb4d9`) lines 214-233 [crates/gwiki/src/log.rs:214-233]
  - Signature: `fn does_not_append_twice_when_scope_and_global_logs_match() {`
  - Purpose: Verifies that 'append_logs' writes a single shared 'log.md' when the scope and global log paths resolve to the same file, and does not duplicate the log entry. [crates/gwiki/src/log.rs:214-233]

