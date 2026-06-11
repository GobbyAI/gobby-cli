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

# crates/gcode/src/project.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/project.rs` exposes 16 indexed API symbols.
[crates/gcode/src/project.rs:15-18]
[crates/gcode/src/project.rs:21-30]
[crates/gcode/src/project.rs:35-44]
[crates/gcode/src/project.rs:47-70]
[crates/gcode/src/project.rs:78-115]

## API Symbols

- `IsolationMarker` (class) component `IsolationMarker [class]` (`b754b762-52ed-587c-b4d0-f2dd4f2a5440`) lines 15-18 [crates/gcode/src/project.rs:15-18]
  - Signature: `pub struct IsolationMarker {`
  - Purpose: `IsolationMarker` is a struct that stores optional parent project identifiers (path and ID) to track project isolation boundaries. [crates/gcode/src/project.rs:15-18]
- `read_gcode_json` (function) component `read_gcode_json [function]` (`4f681307-deba-54d9-adc6-a69fc9dd2c6c`) lines 21-30 [crates/gcode/src/project.rs:21-30]
  - Signature: `pub fn read_gcode_json(project_root: &Path) -> anyhow::Result<String> {`
  - Purpose: Reads the "id" field from a JSON file at `.gobby/gcode.json` relative to the project root and returns it as a String, or an error if the file is inaccessible or the field is missing. [crates/gcode/src/project.rs:21-30]
- `code_index_id_for_root` (function) component `code_index_id_for_root [function]` (`fb2c6384-be67-5ea1-a338-6e9e3ab1075c`) lines 35-44 [crates/gcode/src/project.rs:35-44]
  - Signature: `pub fn code_index_id_for_root(root: &Path) -> String {`
  - Purpose: Generates a deterministic UUID v5 from the canonical form of a given file path using a predefined namespace, returning it as a string. [crates/gcode/src/project.rs:35-44]
- `read_isolation_marker` (function) component `read_isolation_marker [function]` (`0dbfa9ad-18c8-5246-9665-aa3819682cf7`) lines 47-70 [crates/gcode/src/project.rs:47-70]
  - Signature: `pub fn read_isolation_marker(project_root: &Path) -> Option<IsolationMarker> {`
  - Purpose: Reads a project's `.gobby/project.json` configuration file and returns an optional `IsolationMarker` containing parent project path and ID if either field is non-empty. [crates/gcode/src/project.rs:47-70]
- `ensure_gcode_json` (function) component `ensure_gcode_json [function]` (`d7f9547a-f9cf-560c-b138-e885f7216d75`) lines 78-115 [crates/gcode/src/project.rs:78-115]
  - Signature: `pub fn ensure_gcode_json(project_root: &Path) -> anyhow::Result<(String, bool)> {`
  - Purpose: Ensures `.gobby/gcode.json` exists with project metadata (ID, name, creation timestamp), returning the project ID and a boolean flag indicating whether the file was newly initialized. [crates/gcode/src/project.rs:78-115]
- `has_identity_file` (function) component `has_identity_file [function]` (`afe90a1f-613f-5ab6-a790-d26deb7d60dc`) lines 118-121 [crates/gcode/src/project.rs:118-121]
  - Signature: `pub fn has_identity_file(project_root: &Path) -> bool {`
  - Purpose: Returns a boolean indicating whether the `.gobby` directory contains at least one identity file (`project.json` or `gcode.json`). [crates/gcode/src/project.rs:118-121]
- `now_iso8601` (function) component `now_iso8601 [function]` (`c99a8253-098a-59db-b318-bcb07e72742a`) lines 126-128 [crates/gcode/src/project.rs:126-128]
  - Signature: `fn now_iso8601() -> String {`
  - Purpose: Returns the current UTC timestamp as an RFC3339-formatted string with microsecond precision and explicit timezone offset. [crates/gcode/src/project.rs:126-128]
- `absolute_fallback` (function) component `absolute_fallback [function]` (`896dd4bd-21e8-529a-914a-26efe0b1f294`) lines 130-138 [crates/gcode/src/project.rs:130-138]
  - Signature: `fn absolute_fallback(path: &Path) -> PathBuf {`
  - Purpose: Converts relative paths to absolute by joining with the current working directory (or temp directory as a fallback), while returning absolute paths unchanged. [crates/gcode/src/project.rs:130-138]
- `test_code_index_id_for_root_deterministic` (function) component `test_code_index_id_for_root_deterministic [function]` (`28aaf799-7974-505a-9374-0f2746c10b4b`) lines 145-152 [crates/gcode/src/project.rs:145-152]
  - Signature: `fn test_code_index_id_for_root_deterministic() {`
  - Purpose: Verifies that `code_index_id_for_root` deterministically generates valid UUID identifiers for the same directory path. [crates/gcode/src/project.rs:145-152]
- `test_code_index_id_for_root_different_paths` (function) component `test_code_index_id_for_root_different_paths [function]` (`19f46b95-cbd2-56c2-81ed-405f4c6c937e`) lines 155-161 [crates/gcode/src/project.rs:155-161]
  - Signature: `fn test_code_index_id_for_root_different_paths() {`
  - Purpose: Verifies that `code_index_id_for_root` generates distinct identifiers for different directory paths. [crates/gcode/src/project.rs:155-161]
- `test_read_isolation_marker_detects_parent_fields` (function) component `test_read_isolation_marker_detects_parent_fields [function]` (`fb435773-d249-5341-b942-f7366eaa854e`) lines 164-183 [crates/gcode/src/project.rs:164-183]
  - Signature: `fn test_read_isolation_marker_detects_parent_fields() {`
  - Purpose: Tests that `read_isolation_marker()` successfully deserializes `parent_project_path` and `parent_project_id` fields from a `.gobby/project.json` configuration file. [crates/gcode/src/project.rs:164-183]
- `test_ensure_gcode_json_creates_new` (function) component `test_ensure_gcode_json_creates_new [function]` (`baa997d0-b8ca-53fd-8922-7973d0038af7`) lines 186-201 [crates/gcode/src/project.rs:186-201]
  - Signature: `fn test_ensure_gcode_json_creates_new() {`
  - Purpose: This test verifies that `ensure_gcode_json` creates a new `.gobby/gcode.json` file containing a valid UUID that matches the deterministic ID generated by `code_index_id_for_root`. [crates/gcode/src/project.rs:186-201]
- `test_ensure_gcode_json_skips_when_project_json_exists` (function) component `test_ensure_gcode_json_skips_when_project_json_exists [function]` (`18eb1b3b-6103-5b73-8075-cf6108ff4856`) lines 204-226 [crates/gcode/src/project.rs:204-226]
  - Signature: `fn test_ensure_gcode_json_skips_when_project_json_exists() {`
  - Purpose: Verifies that `ensure_gcode_json()` skips `gcode.json` creation and returns the existing project ID when `project.json` is already present in the `.gobby` directory. [crates/gcode/src/project.rs:204-226]
- `test_ensure_gcode_json_reads_existing` (function) component `test_ensure_gcode_json_reads_existing [function]` (`e2d0d9b9-d9c8-5c67-8cb1-8d6f4cc1bcd9`) lines 229-245 [crates/gcode/src/project.rs:229-245]
  - Signature: `fn test_ensure_gcode_json_reads_existing() {`
  - Purpose: Tests idempotent behavior of `ensure_gcode_json` by verifying it reads existing gcode.json files without overwriting them and returns consistent IDs across multiple invocations. [crates/gcode/src/project.rs:229-245]
- `test_now_iso8601_format` (function) component `test_now_iso8601_format [function]` (`53a928ec-218f-53d1-ae0f-58db8aa5ecb4`) lines 248-254 [crates/gcode/src/project.rs:248-254]
  - Signature: `fn test_now_iso8601_format() {`
  - Purpose: Asserts that `now_iso8601()` returns an ISO 8601-formatted UTC timestamp string with minimum length of 27 characters, containing a 'T' separator, and ending with 'Z'. [crates/gcode/src/project.rs:248-254]
- `test_has_identity_file` (function) component `test_has_identity_file [function]` (`191e009d-b5ac-58f2-b6d1-b3b66cab5b90`) lines 257-265 [crates/gcode/src/project.rs:257-265]
  - Signature: `fn test_has_identity_file() {`
  - Purpose: Unit test that verifies `has_identity_file()` correctly returns false for directories lacking a `.gobby/gcode.json` file and true when the file is present. [crates/gcode/src/project.rs:257-265]

