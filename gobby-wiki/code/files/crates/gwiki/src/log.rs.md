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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/log.rs:9-15](crates/gwiki/src/log.rs#L9-L15), [crates/gwiki/src/log.rs:19-22](crates/gwiki/src/log.rs#L19-L22), [crates/gwiki/src/log.rs:25-49](crates/gwiki/src/log.rs#L25-L49), [crates/gwiki/src/log.rs:52-90](crates/gwiki/src/log.rs#L52-L90), [crates/gwiki/src/log.rs:93-108](crates/gwiki/src/log.rs#L93-L108), [crates/gwiki/src/log.rs:111-117](crates/gwiki/src/log.rs#L111-L117), [crates/gwiki/src/log.rs:121-128](crates/gwiki/src/log.rs#L121-L128), [crates/gwiki/src/log.rs:131-150](crates/gwiki/src/log.rs#L131-L150), [crates/gwiki/src/log.rs:153-155](crates/gwiki/src/log.rs#L153-L155), [crates/gwiki/src/log.rs:158-164](crates/gwiki/src/log.rs#L158-L164), [crates/gwiki/src/log.rs:167-174](crates/gwiki/src/log.rs#L167-L174), [crates/gwiki/src/log.rs:183-211](crates/gwiki/src/log.rs#L183-L211), [crates/gwiki/src/log.rs:214-233](crates/gwiki/src/log.rs#L214-L233)

</details>

# crates/gwiki/src/log.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the log record and write-report types for gwiki and implements appending those records to markdown log files. `append_logs` writes a `LogEntry` to the current scope’s `log.md`, then mirrors it to an optional global hub log only after the scope write succeeds; it returns the resulting scope and global paths in `LogWriteReport`. The lower-level `append_log` helper creates parent directories, opens or creates the target file, writes a `# Log` header for new files, and appends the rendered entry. The remaining helpers handle formatting and path/file-identity comparisons so the code can detect when scope and global logs are the same file and avoid double-appending; the tests cover that shared-path behavior.
[crates/gwiki/src/log.rs:9-15]
[crates/gwiki/src/log.rs:19-22]
[crates/gwiki/src/log.rs:25-49]
[crates/gwiki/src/log.rs:52-90]
[crates/gwiki/src/log.rs:93-108]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `LogEntry` | class | `pub struct LogEntry {` | `LogEntry [class]` | `47249c61-90eb-5016-a137-1f84e94def71` | 9-15 [crates/gwiki/src/log.rs:9-15] | Indexed class `LogEntry` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:9-15] |
| `LogWriteReport` | class | `pub struct LogWriteReport {` | `LogWriteReport [class]` | `155406c5-4669-5972-ae59-43f52b041264` | 19-22 [crates/gwiki/src/log.rs:19-22] | Indexed class `LogWriteReport` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:19-22] |
| `append_logs` | function | `pub fn append_logs(` | `append_logs [function]` | `e25c78fd-9fad-5d50-ac2e-0f30fc7cf0d4` | 25-49 [crates/gwiki/src/log.rs:25-49] | Indexed function `append_logs` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:25-49] |
| `append_log` | function | `fn append_log(path: &Path, entry: &LogEntry) -> Result<(), WikiError> {` | `append_log [function]` | `5a81c5f5-59c0-5a9a-b384-dffa85b8a546` | 52-90 [crates/gwiki/src/log.rs:52-90] | Indexed function `append_log` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:52-90] |
| `render_entry` | function | `fn render_entry(entry: &LogEntry) -> String {` | `render_entry [function]` | `c901ce57-f6ac-5378-9cff-d0c90c33fe47` | 93-108 [crates/gwiki/src/log.rs:93-108] | Indexed function `render_entry` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:93-108] |
| `same_log_path` | function | `fn same_log_path(left: &Path, right: &Path) -> bool {` | `same_log_path [function]` | `2061b5d6-09ae-519b-81a7-dfb43d19c803` | 111-117 [crates/gwiki/src/log.rs:111-117] | Indexed function `same_log_path` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:111-117] |
| `same_file_identity` | function | `fn same_file_identity(left: &Path, right: &Path) -> bool {` | `same_file_identity [function]` | `daf9baeb-a7d2-5d26-bd81-7e9e6e73a25d` | 121-128 [crates/gwiki/src/log.rs:121-128] | Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:121-128] |
| `same_file_identity` | function | `fn same_file_identity(left: &Path, right: &Path) -> bool {` | `same_file_identity [function]` | `3369600f-19cf-5eb7-bfaa-0f3febdffc27` | 131-150 [crates/gwiki/src/log.rs:131-150] | Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:131-150] |
| `identity` | function | `fn identity(path: &Path) -> Option<(u32, u32, u32)> {` | `identity [function]` | `1b3d975f-81ca-57fe-9355-230c91ee4f52` | 134-144 [crates/gwiki/src/log.rs:134-144] | Indexed function `identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:134-144] |
| `same_file_identity` | function | `fn same_file_identity(_left: &Path, _right: &Path) -> bool {` | `same_file_identity [function]` | `13c7499a-efc1-596f-a7e0-631a33814bbc` | 153-155 [crates/gwiki/src/log.rs:153-155] | Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:153-155] |
| `resolved_log_path` | function | `fn resolved_log_path(path: &Path) -> PathBuf {` | `resolved_log_path [function]` | `feecdee7-b91b-5ad5-8e7d-3c44fde84722` | 158-164 [crates/gwiki/src/log.rs:158-164] | Indexed function `resolved_log_path` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:158-164] |
| `resolve_log_path_fallback` | function | `fn resolve_log_path_fallback(path: &Path) -> PathBuf {` | `resolve_log_path_fallback [function]` | `15a03020-97f3-53aa-a339-085717550af0` | 167-174 [crates/gwiki/src/log.rs:167-174] | Indexed function `resolve_log_path_fallback` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:167-174] |
| `writes_scope_and_global_logs` | function | `fn writes_scope_and_global_logs() {` | `writes_scope_and_global_logs [function]` | `29419c8a-9ca7-5c5e-9f37-f78a78ae1be9` | 183-211 [crates/gwiki/src/log.rs:183-211] | Indexed function `writes_scope_and_global_logs` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:183-211] |
| `does_not_append_twice_when_scope_and_global_logs_match` | function | `fn does_not_append_twice_when_scope_and_global_logs_match() {` | `does_not_append_twice_when_scope_and_global_logs_match [function]` | `bdf78f1d-bfe3-5b48-84db-656d1f7eb4d9` | 214-233 [crates/gwiki/src/log.rs:214-233] | Indexed function `does_not_append_twice_when_scope_and_global_logs_match` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:214-233] |
