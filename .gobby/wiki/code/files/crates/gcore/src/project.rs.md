---
title: crates/gcore/src/project.rs
type: code_file
provenance:
- file: crates/gcore/src/project.rs
  ranges:
  - 12-24
  - 28-51
  - 53-62
  - 70-89
  - 92-113
  - 116-126
  - 129-145
  - 148-164
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/project.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file provides non-mutating helpers for locating a Gobby project and reading its project ID. `find_project_root` walks upward from a starting path until it finds a `.gobby` directory containing either `project.json` or `gcode.json`, while `read_project_id` prefers `.gobby/project.json` and falls back to `.gobby/gcode.json` for standalone code-index roots. The private `read_project_id_from` handles the shared file read, JSON parse, and `"id"` extraction logic, and the tests verify that lookup is non-destructive, that fallback to `gcode.json` works when needed, and that error messages mention the missing `id` field clearly.
[crates/gcore/src/project.rs:12-24]
[crates/gcore/src/project.rs:28-51]
[crates/gcore/src/project.rs:53-62]
[crates/gcore/src/project.rs:70-89]
[crates/gcore/src/project.rs:92-113]

## API Symbols

- `find_project_root` (function) component `find_project_root [function]` (`773fd042-0667-51b8-acdf-645b26e780e1`) lines 12-24 [crates/gcore/src/project.rs:12-24]
  - Signature: `pub fn find_project_root(start: &Path) -> Option<PathBuf> {`
  - Purpose: Indexed function `find_project_root` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:12-24]
- `read_project_id` (function) component `read_project_id [function]` (`ca892579-e399-5e47-aef7-91b3d9aab129`) lines 28-51 [crates/gcore/src/project.rs:28-51]
  - Signature: `pub fn read_project_id(project_root: &Path) -> anyhow::Result<String> {`
  - Purpose: Indexed function `read_project_id` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:28-51]
- `read_project_id_from` (function) component `read_project_id_from [function]` (`f0c8cb4c-fdc0-5645-939f-bc32e6b32c19`) lines 53-62 [crates/gcore/src/project.rs:53-62]
  - Signature: `fn read_project_id_from(path: &Path) -> anyhow::Result<String> {`
  - Purpose: Indexed function `read_project_id_from` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:53-62]
- `read_project_id_is_non_destructive` (function) component `read_project_id_is_non_destructive [function]` (`299860f6-1f8f-50b3-bda9-35a3313f3900`) lines 70-89 [crates/gcore/src/project.rs:70-89]
  - Signature: `fn read_project_id_is_non_destructive() {`
  - Purpose: Indexed function `read_project_id_is_non_destructive` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:70-89]
- `read_project_id_falls_back_to_gcode_json_root_marker` (function) component `read_project_id_falls_back_to_gcode_json_root_marker [function]` (`c2929b1f-653d-5e4a-8126-5f28cc30ea15`) lines 92-113 [crates/gcore/src/project.rs:92-113]
  - Signature: `fn read_project_id_falls_back_to_gcode_json_root_marker() {`
  - Purpose: Indexed function `read_project_id_falls_back_to_gcode_json_root_marker` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:92-113]
- `missing_project_id_error_mentions_id_key` (function) component `missing_project_id_error_mentions_id_key [function]` (`d0809951-b630-5b2d-a3ee-782cea3cec3e`) lines 116-126 [crates/gcore/src/project.rs:116-126]
  - Signature: `fn missing_project_id_error_mentions_id_key() {`
  - Purpose: Indexed function `missing_project_id_error_mentions_id_key` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:116-126]
- `read_project_id_falls_back_to_gcode_json_when_project_json_is_bad` (function) component `read_project_id_falls_back_to_gcode_json_when_project_json_is_bad [function]` (`6512e3bc-709d-5ab1-8555-d9f748341576`) lines 129-145 [crates/gcore/src/project.rs:129-145]
  - Signature: `fn read_project_id_falls_back_to_gcode_json_when_project_json_is_bad() {`
  - Purpose: Indexed function `read_project_id_falls_back_to_gcode_json_when_project_json_is_bad` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:129-145]
- `read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed` (function) component `read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed [function]` (`c32b60f5-9fe4-562a-9c5b-295b5354f930`) lines 148-164 [crates/gcore/src/project.rs:148-164]
  - Signature: `fn read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed() {`
  - Purpose: Indexed function `read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:148-164]

