---
title: crates/gcore/src/project.rs
type: code_file
provenance:
- file: crates/gcore/src/project.rs
  ranges:
  - 13-25
  - 29-52
  - 54-63
  - 71-90
  - 93-114
  - 117-127
  - 130-146
  - 149-165
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/project.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/project.rs` exposes 8 indexed API symbols.
[crates/gcore/src/project.rs:13-25]
[crates/gcore/src/project.rs:29-52]
[crates/gcore/src/project.rs:54-63]
[crates/gcore/src/project.rs:71-90]
[crates/gcore/src/project.rs:93-114]
[crates/gcore/src/project.rs:117-127]
[crates/gcore/src/project.rs:130-146]
[crates/gcore/src/project.rs:149-165]

## API Symbols

- `find_project_root` (function) component `find_project_root [function]` (`434b0dcb-d52b-5d31-9c45-50ec3059336b`) lines 13-25 [crates/gcore/src/project.rs:13-25]
  - Signature: `pub fn find_project_root(start: &Path) -> Option<PathBuf> {`
  - Purpose: Traverses upward through parent directories to locate and return the first directory containing a `.gobby/project.json` or `.gobby/gcode.json` marker file. [crates/gcore/src/project.rs:13-25]
- `read_project_id` (function) component `read_project_id [function]` (`c1361067-d863-5291-a062-664afcabdac4`) lines 29-52 [crates/gcore/src/project.rs:29-52]
  - Signature: `pub fn read_project_id(project_root: &Path) -> anyhow::Result<String> {`
  - Purpose: Reads a project ID from `.gobby/project.json` with fallback to `.gobby/gcode.json`, returning the ID string or an error if both sources fail. [crates/gcore/src/project.rs:29-52]
- `read_project_id_from` (function) component `read_project_id_from [function]` (`c7298233-2fb2-51cb-95a4-4f05aaddba3e`) lines 54-63 [crates/gcore/src/project.rs:54-63]
  - Signature: `fn read_project_id_from(path: &Path) -> anyhow::Result<String> {`
  - Purpose: Extracts the string value of the `id` field from a JSON file at a specified path, with contextual error handling for file I/O, JSON parsing, and missing or non-string id fields. [crates/gcore/src/project.rs:54-63]
- `read_project_id_is_non_destructive` (function) component `read_project_id_is_non_destructive [function]` (`19d8a466-e866-5b7c-b628-f101f9a8eaa8`) lines 71-90 [crates/gcore/src/project.rs:71-90]
  - Signature: `fn read_project_id_is_non_destructive() {`
  - Purpose: This test verifies that `read_project_id()` successfully extracts the project ID from a project.json file without mutating the file's contents. [crates/gcore/src/project.rs:71-90]
- `read_project_id_falls_back_to_gcode_json_root_marker` (function) component `read_project_id_falls_back_to_gcode_json_root_marker [function]` (`509ac56e-98d1-5e7f-bae2-9d0e71a04d56`) lines 93-114 [crates/gcore/src/project.rs:93-114]
  - Signature: `fn read_project_id_falls_back_to_gcode_json_root_marker() {`
  - Purpose: This test verifies that `read_project_id()` correctly retrieves the project identifier from the `gcode.json` file located in the `.gobby` directory marker, which serves as the project root. [crates/gcore/src/project.rs:93-114]
- `missing_project_id_error_mentions_id_key` (function) component `missing_project_id_error_mentions_id_key [function]` (`133c38ef-4d4e-5f0d-917f-4a42ba9f9ba4`) lines 117-127 [crates/gcore/src/project.rs:117-127]
  - Signature: `fn missing_project_id_error_mentions_id_key() {`
  - Purpose: Tests that `read_project_id()` returns an error message explicitly mentioning the missing `'id' field` when reading a project configuration file lacking the id key. [crates/gcore/src/project.rs:117-127]
- `read_project_id_falls_back_to_gcode_json_when_project_json_is_bad` (function) component `read_project_id_falls_back_to_gcode_json_when_project_json_is_bad [function]` (`5f12b4d8-7b72-5605-a184-aa7cbfa9806c`) lines 130-146 [crates/gcore/src/project.rs:130-146]
  - Signature: `fn read_project_id_falls_back_to_gcode_json_when_project_json_is_bad() {`
  - Purpose: This test verifies that `read_project_id()` successfully falls back to reading the project ID from `gcode.json` when `project.json` lacks an id field. [crates/gcore/src/project.rs:130-146]
- `read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed` (function) component `read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed [function]` (`ab4a0d29-a7ae-51cc-89d3-a68d9f43c61a`) lines 149-165 [crates/gcore/src/project.rs:149-165]
  - Signature: `fn read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed() {`
  - Purpose: This test verifies that `read_project_id()` successfully returns the project ID from `gcode.json` when `project.json` contains invalid JSON. [crates/gcore/src/project.rs:149-165]

