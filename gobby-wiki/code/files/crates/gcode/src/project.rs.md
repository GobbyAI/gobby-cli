---
title: crates/gcode/src/project.rs
type: code_file
provenance:
- file: crates/gcode/src/project.rs
  ranges:
  - 15-18
  - 21-30
  - 35-44
  - 47-70
  - 78-115
  - 118-121
  - 126-128
  - 130-138
  - 145-152
  - 155-161
  - 164-183
  - 186-201
  - 204-226
  - 229-245
  - 248-254
  - 257-265
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/project.rs:15-18](crates/gcode/src/project.rs#L15-L18), [crates/gcode/src/project.rs:21-30](crates/gcode/src/project.rs#L21-L30), [crates/gcode/src/project.rs:35-44](crates/gcode/src/project.rs#L35-L44), [crates/gcode/src/project.rs:47-70](crates/gcode/src/project.rs#L47-L70), [crates/gcode/src/project.rs:78-115](crates/gcode/src/project.rs#L78-L115), [crates/gcode/src/project.rs:118-121](crates/gcode/src/project.rs#L118-L121), [crates/gcode/src/project.rs:126-128](crates/gcode/src/project.rs#L126-L128), [crates/gcode/src/project.rs:130-138](crates/gcode/src/project.rs#L130-L138), [crates/gcode/src/project.rs:145-152](crates/gcode/src/project.rs#L145-L152), [crates/gcode/src/project.rs:155-161](crates/gcode/src/project.rs#L155-L161), [crates/gcode/src/project.rs:164-183](crates/gcode/src/project.rs#L164-L183), [crates/gcode/src/project.rs:186-201](crates/gcode/src/project.rs#L186-L201), [crates/gcode/src/project.rs:204-226](crates/gcode/src/project.rs#L204-L226), [crates/gcode/src/project.rs:229-245](crates/gcode/src/project.rs#L229-L245), [crates/gcode/src/project.rs:248-254](crates/gcode/src/project.rs#L248-L254), [crates/gcode/src/project.rs:257-265](crates/gcode/src/project.rs#L257-L265)

</details>

# crates/gcode/src/project.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Provides project identity resolution for gcode standalone mode. It reads a gcode-owned ID from `.gobby/gcode.json`, checks `.gobby/project.json` for an isolation marker that records parent project metadata, and falls back to generating a deterministic code-index UUID from the project root path when no stored ID is available. The helper functions also detect whether an identity file exists, format timestamps, and normalize fallback paths. The test cases cover deterministic ID generation, differing roots producing different IDs, isolation-marker parsing, creation and reuse behavior for `gcode.json`, timestamp formatting, and identity-file detection.
[crates/gcode/src/project.rs:15-18]
[crates/gcode/src/project.rs:21-30]
[crates/gcode/src/project.rs:35-44]
[crates/gcode/src/project.rs:47-70]
[crates/gcode/src/project.rs:78-115]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IsolationMarker` | class | `pub struct IsolationMarker {` | `IsolationMarker [class]` | `b754b762-52ed-587c-b4d0-f2dd4f2a5440` | 15-18 [crates/gcode/src/project.rs:15-18] | Indexed class `IsolationMarker` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:15-18] |
| `read_gcode_json` | function | `pub fn read_gcode_json(project_root: &Path) -> anyhow::Result<String> {` | `read_gcode_json [function]` | `4f681307-deba-54d9-adc6-a69fc9dd2c6c` | 21-30 [crates/gcode/src/project.rs:21-30] | Indexed function `read_gcode_json` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:21-30] |
| `code_index_id_for_root` | function | `pub fn code_index_id_for_root(root: &Path) -> String {` | `code_index_id_for_root [function]` | `fb2c6384-be67-5ea1-a338-6e9e3ab1075c` | 35-44 [crates/gcode/src/project.rs:35-44] | Indexed function `code_index_id_for_root` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:35-44] |
| `read_isolation_marker` | function | `pub fn read_isolation_marker(project_root: &Path) -> Option<IsolationMarker> {` | `read_isolation_marker [function]` | `0dbfa9ad-18c8-5246-9665-aa3819682cf7` | 47-70 [crates/gcode/src/project.rs:47-70] | Indexed function `read_isolation_marker` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:47-70] |
| `ensure_gcode_json` | function | `pub fn ensure_gcode_json(project_root: &Path) -> anyhow::Result<(String, bool)> {` | `ensure_gcode_json [function]` | `d7f9547a-f9cf-560c-b138-e885f7216d75` | 78-115 [crates/gcode/src/project.rs:78-115] | Indexed function `ensure_gcode_json` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:78-115] |
| `has_identity_file` | function | `pub fn has_identity_file(project_root: &Path) -> bool {` | `has_identity_file [function]` | `afe90a1f-613f-5ab6-a790-d26deb7d60dc` | 118-121 [crates/gcode/src/project.rs:118-121] | Indexed function `has_identity_file` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:118-121] |
| `now_iso8601` | function | `fn now_iso8601() -> String {` | `now_iso8601 [function]` | `c99a8253-098a-59db-b318-bcb07e72742a` | 126-128 [crates/gcode/src/project.rs:126-128] | Indexed function `now_iso8601` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:126-128] |
| `absolute_fallback` | function | `fn absolute_fallback(path: &Path) -> PathBuf {` | `absolute_fallback [function]` | `896dd4bd-21e8-529a-914a-26efe0b1f294` | 130-138 [crates/gcode/src/project.rs:130-138] | Indexed function `absolute_fallback` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:130-138] |
| `test_code_index_id_for_root_deterministic` | function | `fn test_code_index_id_for_root_deterministic() {` | `test_code_index_id_for_root_deterministic [function]` | `28aaf799-7974-505a-9374-0f2746c10b4b` | 145-152 [crates/gcode/src/project.rs:145-152] | Indexed function `test_code_index_id_for_root_deterministic` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:145-152] |
| `test_code_index_id_for_root_different_paths` | function | `fn test_code_index_id_for_root_different_paths() {` | `test_code_index_id_for_root_different_paths [function]` | `19f46b95-cbd2-56c2-81ed-405f4c6c937e` | 155-161 [crates/gcode/src/project.rs:155-161] | Indexed function `test_code_index_id_for_root_different_paths` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:155-161] |
| `test_read_isolation_marker_detects_parent_fields` | function | `fn test_read_isolation_marker_detects_parent_fields() {` | `test_read_isolation_marker_detects_parent_fields [function]` | `fb435773-d249-5341-b942-f7366eaa854e` | 164-183 [crates/gcode/src/project.rs:164-183] | Indexed function `test_read_isolation_marker_detects_parent_fields` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:164-183] |
| `test_ensure_gcode_json_creates_new` | function | `fn test_ensure_gcode_json_creates_new() {` | `test_ensure_gcode_json_creates_new [function]` | `baa997d0-b8ca-53fd-8922-7973d0038af7` | 186-201 [crates/gcode/src/project.rs:186-201] | Indexed function `test_ensure_gcode_json_creates_new` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:186-201] |
| `test_ensure_gcode_json_skips_when_project_json_exists` | function | `fn test_ensure_gcode_json_skips_when_project_json_exists() {` | `test_ensure_gcode_json_skips_when_project_json_exists [function]` | `18eb1b3b-6103-5b73-8075-cf6108ff4856` | 204-226 [crates/gcode/src/project.rs:204-226] | Indexed function `test_ensure_gcode_json_skips_when_project_json_exists` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:204-226] |
| `test_ensure_gcode_json_reads_existing` | function | `fn test_ensure_gcode_json_reads_existing() {` | `test_ensure_gcode_json_reads_existing [function]` | `e2d0d9b9-d9c8-5c67-8cb1-8d6f4cc1bcd9` | 229-245 [crates/gcode/src/project.rs:229-245] | Indexed function `test_ensure_gcode_json_reads_existing` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:229-245] |
| `test_now_iso8601_format` | function | `fn test_now_iso8601_format() {` | `test_now_iso8601_format [function]` | `53a928ec-218f-53d1-ae0f-58db8aa5ecb4` | 248-254 [crates/gcode/src/project.rs:248-254] | Indexed function `test_now_iso8601_format` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:248-254] |
| `test_has_identity_file` | function | `fn test_has_identity_file() {` | `test_has_identity_file [function]` | `191e009d-b5ac-58f2-b6d1-b3b66cab5b90` | 257-265 [crates/gcode/src/project.rs:257-265] | Indexed function `test_has_identity_file` in `crates/gcode/src/project.rs`. [crates/gcode/src/project.rs:257-265] |
