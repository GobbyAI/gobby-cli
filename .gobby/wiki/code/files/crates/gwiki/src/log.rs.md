---
title: crates/gwiki/src/log.rs
type: code_file
provenance:
- file: crates/gwiki/src/log.rs
  ranges:
  - 8-14
  - 17-20
  - 22-46
  - 48-86
  - 88-103
  - 105-111
  - 114-121
  - 124-143
  - 127-137
  - 146-148
  - 150-156
  - 158-165
  - 174-202
  - 205-224
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/log.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/log.rs` exposes 14 indexed API symbols.
[crates/gwiki/src/log.rs:8-14]
[crates/gwiki/src/log.rs:17-20]
[crates/gwiki/src/log.rs:22-46]
[crates/gwiki/src/log.rs:48-86]
[crates/gwiki/src/log.rs:88-103]
[crates/gwiki/src/log.rs:105-111]
[crates/gwiki/src/log.rs:114-121]
[crates/gwiki/src/log.rs:124-143]
[crates/gwiki/src/log.rs:127-137]
[crates/gwiki/src/log.rs:146-148]
[crates/gwiki/src/log.rs:150-156]
[crates/gwiki/src/log.rs:158-165]
[crates/gwiki/src/log.rs:174-202]
[crates/gwiki/src/log.rs:205-224]

## API Symbols

- `LogEntry` (class) component `LogEntry [class]` (`601ce88c-b5d7-5e2a-8f25-b6a9df8617e3`) lines 8-14 [crates/gwiki/src/log.rs:8-14]
  - Signature: `pub struct LogEntry {`
  - Purpose: Indexed class `LogEntry` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:8-14]
- `LogWriteReport` (class) component `LogWriteReport [class]` (`df69753e-61eb-5ecd-a85d-f9299d7ddde0`) lines 17-20 [crates/gwiki/src/log.rs:17-20]
  - Signature: `pub struct LogWriteReport {`
  - Purpose: Indexed class `LogWriteReport` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:17-20]
- `append_logs` (function) component `append_logs [function]` (`258c40ab-f206-5c27-aa38-7839bb6eb074`) lines 22-46 [crates/gwiki/src/log.rs:22-46]
  - Signature: `pub fn append_logs(`
  - Purpose: Indexed function `append_logs` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:22-46]
- `append_log` (function) component `append_log [function]` (`f10a88f5-fdf3-50ad-ad3c-7142458f7918`) lines 48-86 [crates/gwiki/src/log.rs:48-86]
  - Signature: `fn append_log(path: &Path, entry: &LogEntry) -> Result<(), WikiError> {`
  - Purpose: Indexed function `append_log` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:48-86]
- `render_entry` (function) component `render_entry [function]` (`1f968dda-340a-55c2-ab9e-f23dfed349b8`) lines 88-103 [crates/gwiki/src/log.rs:88-103]
  - Signature: `fn render_entry(entry: &LogEntry) -> String {`
  - Purpose: Indexed function `render_entry` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:88-103]
- `same_log_path` (function) component `same_log_path [function]` (`7a2058eb-b621-5369-9318-d4a5793e2924`) lines 105-111 [crates/gwiki/src/log.rs:105-111]
  - Signature: `fn same_log_path(left: &Path, right: &Path) -> bool {`
  - Purpose: Indexed function `same_log_path` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:105-111]
- `same_file_identity` (function) component `same_file_identity [function]` (`a099b2b1-7449-57cc-80a6-b0537dfbd694`) lines 114-121 [crates/gwiki/src/log.rs:114-121]
  - Signature: `fn same_file_identity(left: &Path, right: &Path) -> bool {`
  - Purpose: Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:114-121]
- `same_file_identity` (function) component `same_file_identity [function]` (`2de90eaf-bed3-5d8c-a746-9014b5f79f38`) lines 124-143 [crates/gwiki/src/log.rs:124-143]
  - Signature: `fn same_file_identity(left: &Path, right: &Path) -> bool {`
  - Purpose: Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:124-143]
- `identity` (function) component `identity [function]` (`2dcc20f2-8437-543b-81b6-ad6c3793acb1`) lines 127-137 [crates/gwiki/src/log.rs:127-137]
  - Signature: `fn identity(path: &Path) -> Option<(u32, u32, u32)> {`
  - Purpose: Indexed function `identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:127-137]
- `same_file_identity` (function) component `same_file_identity [function]` (`97e8e1a0-7bdb-53f2-897f-b98596fd9e83`) lines 146-148 [crates/gwiki/src/log.rs:146-148]
  - Signature: `fn same_file_identity(_left: &Path, _right: &Path) -> bool {`
  - Purpose: Indexed function `same_file_identity` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:146-148]
- `resolved_log_path` (function) component `resolved_log_path [function]` (`499f4ef5-31f6-5430-a313-b431bff31108`) lines 150-156 [crates/gwiki/src/log.rs:150-156]
  - Signature: `fn resolved_log_path(path: &Path) -> PathBuf {`
  - Purpose: Indexed function `resolved_log_path` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:150-156]
- `resolve_log_path_fallback` (function) component `resolve_log_path_fallback [function]` (`d649a64c-6a28-5cae-b07c-dd7d03cb9515`) lines 158-165 [crates/gwiki/src/log.rs:158-165]
  - Signature: `fn resolve_log_path_fallback(path: &Path) -> PathBuf {`
  - Purpose: Indexed function `resolve_log_path_fallback` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:158-165]
- `writes_scope_and_global_logs` (function) component `writes_scope_and_global_logs [function]` (`efc25269-c347-5051-bd16-b0673f28fdb6`) lines 174-202 [crates/gwiki/src/log.rs:174-202]
  - Signature: `fn writes_scope_and_global_logs() {`
  - Purpose: Indexed function `writes_scope_and_global_logs` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:174-202]
- `does_not_append_twice_when_scope_and_global_logs_match` (function) component `does_not_append_twice_when_scope_and_global_logs_match [function]` (`fce7be73-db98-5365-91f8-799e2357202b`) lines 205-224 [crates/gwiki/src/log.rs:205-224]
  - Signature: `fn does_not_append_twice_when_scope_and_global_logs_match() {`
  - Purpose: Indexed function `does_not_append_twice_when_scope_and_global_logs_match` in `crates/gwiki/src/log.rs`. [crates/gwiki/src/log.rs:205-224]

