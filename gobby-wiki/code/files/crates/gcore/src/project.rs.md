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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/project.rs:12-24](crates/gcore/src/project.rs#L12-L24), [crates/gcore/src/project.rs:28-51](crates/gcore/src/project.rs#L28-L51), [crates/gcore/src/project.rs:53-62](crates/gcore/src/project.rs#L53-L62), [crates/gcore/src/project.rs:70-89](crates/gcore/src/project.rs#L70-L89), [crates/gcore/src/project.rs:92-113](crates/gcore/src/project.rs#L92-L113), [crates/gcore/src/project.rs:116-126](crates/gcore/src/project.rs#L116-L126), [crates/gcore/src/project.rs:129-145](crates/gcore/src/project.rs#L129-L145), [crates/gcore/src/project.rs:148-164](crates/gcore/src/project.rs#L148-L164)

</details>

# crates/gcore/src/project.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Provides shared helpers for locating a Gobby project root and reading its project ID without modifying anything. `find_project_root` walks upward from a starting path until it finds a `.gobby` directory containing either `project.json` or `gcode.json`. `read_project_id` then reads the ID from `.gobby/project.json` when present, falls back to `.gobby/gcode.json` for standalone code-index roots, and preserves informative errors when the primary file is missing, unreadable, malformed, or lacks an `id` field. `read_project_id_from` does the actual file read and JSON extraction, while the remaining functions exercise the non-destructive fallback and error-message behavior.
[crates/gcore/src/project.rs:12-24]
[crates/gcore/src/project.rs:28-51]
[crates/gcore/src/project.rs:53-62]
[crates/gcore/src/project.rs:70-89]
[crates/gcore/src/project.rs:92-113]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `find_project_root` | function | `pub fn find_project_root(start: &Path) -> Option<PathBuf> {` | `find_project_root [function]` | `773fd042-0667-51b8-acdf-645b26e780e1` | 12-24 [crates/gcore/src/project.rs:12-24] | Indexed function `find_project_root` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:12-24] |
| `read_project_id` | function | `pub fn read_project_id(project_root: &Path) -> anyhow::Result<String> {` | `read_project_id [function]` | `ca892579-e399-5e47-aef7-91b3d9aab129` | 28-51 [crates/gcore/src/project.rs:28-51] | Indexed function `read_project_id` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:28-51] |
| `read_project_id_from` | function | `fn read_project_id_from(path: &Path) -> anyhow::Result<String> {` | `read_project_id_from [function]` | `f0c8cb4c-fdc0-5645-939f-bc32e6b32c19` | 53-62 [crates/gcore/src/project.rs:53-62] | Indexed function `read_project_id_from` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:53-62] |
| `read_project_id_is_non_destructive` | function | `fn read_project_id_is_non_destructive() {` | `read_project_id_is_non_destructive [function]` | `299860f6-1f8f-50b3-bda9-35a3313f3900` | 70-89 [crates/gcore/src/project.rs:70-89] | Indexed function `read_project_id_is_non_destructive` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:70-89] |
| `read_project_id_falls_back_to_gcode_json_root_marker` | function | `fn read_project_id_falls_back_to_gcode_json_root_marker() {` | `read_project_id_falls_back_to_gcode_json_root_marker [function]` | `c2929b1f-653d-5e4a-8126-5f28cc30ea15` | 92-113 [crates/gcore/src/project.rs:92-113] | Indexed function `read_project_id_falls_back_to_gcode_json_root_marker` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:92-113] |
| `missing_project_id_error_mentions_id_key` | function | `fn missing_project_id_error_mentions_id_key() {` | `missing_project_id_error_mentions_id_key [function]` | `d0809951-b630-5b2d-a3ee-782cea3cec3e` | 116-126 [crates/gcore/src/project.rs:116-126] | Indexed function `missing_project_id_error_mentions_id_key` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:116-126] |
| `read_project_id_falls_back_to_gcode_json_when_project_json_is_bad` | function | `fn read_project_id_falls_back_to_gcode_json_when_project_json_is_bad() {` | `read_project_id_falls_back_to_gcode_json_when_project_json_is_bad [function]` | `6512e3bc-709d-5ab1-8555-d9f748341576` | 129-145 [crates/gcore/src/project.rs:129-145] | Indexed function `read_project_id_falls_back_to_gcode_json_when_project_json_is_bad` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:129-145] |
| `read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed` | function | `fn read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed() {` | `read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed [function]` | `c32b60f5-9fe4-562a-9c5b-295b5354f930` | 148-164 [crates/gcore/src/project.rs:148-164] | Indexed function `read_project_id_falls_back_to_gcode_json_when_project_json_is_malformed` in `crates/gcore/src/project.rs`. [crates/gcore/src/project.rs:148-164] |
