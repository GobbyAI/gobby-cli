---
title: crates/gcode/src/skill.rs
type: code_file
provenance:
- file: crates/gcode/src/skill.rs
  ranges:
  - 20-23
  - 26-29
  - 61-63
  - 67-72
  - 75-85
  - 88-94
  - 100-107
  - 109-114
  - 117-128
  - 131-148
  - 151-164
  - 167-188
  - 191-220
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/skill.rs:20-23](crates/gcode/src/skill.rs#L20-L23), [crates/gcode/src/skill.rs:26-29](crates/gcode/src/skill.rs#L26-L29), [crates/gcode/src/skill.rs:61-63](crates/gcode/src/skill.rs#L61-L63), [crates/gcode/src/skill.rs:67-72](crates/gcode/src/skill.rs#L67-L72), [crates/gcode/src/skill.rs:75-85](crates/gcode/src/skill.rs#L75-L85), [crates/gcode/src/skill.rs:88-94](crates/gcode/src/skill.rs#L88-L94), [crates/gcode/src/skill.rs:100-107](crates/gcode/src/skill.rs#L100-L107), [crates/gcode/src/skill.rs:109-114](crates/gcode/src/skill.rs#L109-L114), [crates/gcode/src/skill.rs:117-128](crates/gcode/src/skill.rs#L117-L128), [crates/gcode/src/skill.rs:131-148](crates/gcode/src/skill.rs#L131-L148), [crates/gcode/src/skill.rs:151-164](crates/gcode/src/skill.rs#L151-L164), [crates/gcode/src/skill.rs:167-188](crates/gcode/src/skill.rs#L167-L188), [crates/gcode/src/skill.rs:191-220](crates/gcode/src/skill.rs#L191-L220)

</details>

# crates/gcode/src/skill.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file packages the embedded `SKILL.md` for `gcode` and installs it into the project-specific location expected by each supported AI CLI. `SkillTarget` and `InstallKind` describe the available targets, `supported_targets` exposes the fixed target list, and `install_skill` dispatches to either `install_claude_plugin` or the generic `install_skill_dir`; the helper functions compute target paths, verify the Claude `plugin.json`, and the tests check the target list stays stable, installs land in all expected paths, the Claude manifest is written correctly, and existing CLI files are not removed.
[crates/gcode/src/skill.rs:20-23]
[crates/gcode/src/skill.rs:26-29]
[crates/gcode/src/skill.rs:61-63]
[crates/gcode/src/skill.rs:67-72]
[crates/gcode/src/skill.rs:75-85]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SkillTarget` | class | `pub struct SkillTarget {` | `SkillTarget [class]` | `5a41c0d8-d3ac-577b-8a2f-141c12fdb8c5` | 20-23 [crates/gcode/src/skill.rs:20-23] | Indexed class `SkillTarget` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:20-23] |
| `InstallKind` | type | `enum InstallKind {` | `InstallKind [type]` | `1ddf8fc8-5593-56e8-889f-8eb842a4fdb4` | 26-29 [crates/gcode/src/skill.rs:26-29] | Indexed type `InstallKind` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:26-29] |
| `supported_targets` | function | `pub fn supported_targets() -> &'static [SkillTarget] {` | `supported_targets [function]` | `e754ea69-291a-54da-bf88-8dcfd72a920e` | 61-63 [crates/gcode/src/skill.rs:61-63] | Indexed function `supported_targets` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:61-63] |
| `install_skill` | function | `pub fn install_skill(project_root: &Path, target: &SkillTarget) -> std::io::Result<String> {` | `install_skill [function]` | `f4026363-dfb6-5286-acc2-5a86c632d07f` | 67-72 [crates/gcode/src/skill.rs:67-72] | Indexed function `install_skill` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:67-72] |
| `install_claude_plugin` | function | `fn install_claude_plugin(project_root: &Path) -> std::io::Result<String> {` | `install_claude_plugin [function]` | `e57757de-fa8f-547a-8aa9-7d140d1970c5` | 75-85 [crates/gcode/src/skill.rs:75-85] | Indexed function `install_claude_plugin` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:75-85] |
| `install_skill_dir` | function | `fn install_skill_dir(project_root: &Path, cli_dir: &str) -> std::io::Result<String> {` | `install_skill_dir [function]` | `39d2c4fc-8622-55d4-bea7-0206eb612361` | 88-94 [crates/gcode/src/skill.rs:88-94] | Indexed function `install_skill_dir` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:88-94] |
| `target_path` | function | `fn target_path(project_root: &Path, target: &SkillTarget) -> std::path::PathBuf {` | `target_path [function]` | `f5127b17-bbd0-5674-880c-a48b16e55c6b` | 100-107 [crates/gcode/src/skill.rs:100-107] | Indexed function `target_path` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:100-107] |
| `expected_reported_path` | function | `fn expected_reported_path(target: &SkillTarget) -> String {` | `expected_reported_path [function]` | `49d13cc4-d67f-54a4-9b43-0fc64a6ddd77` | 109-114 [crates/gcode/src/skill.rs:109-114] | Indexed function `expected_reported_path` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:109-114] |
| `plugin_json_is_valid` | function | `fn plugin_json_is_valid() {` | `plugin_json_is_valid [function]` | `03634f4d-8a9a-546f-ac12-55889da932ba` | 117-128 [crates/gcode/src/skill.rs:117-128] | Indexed function `plugin_json_is_valid` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:117-128] |
| `supported_targets_are_stable` | function | `fn supported_targets_are_stable() {` | `supported_targets_are_stable [function]` | `d765a135-4f04-5ba7-ac6b-d2d077a8f544` | 131-148 [crates/gcode/src/skill.rs:131-148] | Indexed function `supported_targets_are_stable` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:131-148] |
| `installs_skill_to_all_supported_target_paths` | function | `fn installs_skill_to_all_supported_target_paths() {` | `installs_skill_to_all_supported_target_paths [function]` | `76a52bfa-6711-5213-872c-422f93d36c99` | 151-164 [crates/gcode/src/skill.rs:151-164] | Indexed function `installs_skill_to_all_supported_target_paths` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:151-164] |
| `claude_plugin_manifest_is_written` | function | `fn claude_plugin_manifest_is_written() {` | `claude_plugin_manifest_is_written [function]` | `223d866d-626c-567b-b1d6-88465ce3d9d4` | 167-188 [crates/gcode/src/skill.rs:167-188] | Indexed function `claude_plugin_manifest_is_written` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:167-188] |
| `installing_skills_does_not_delete_existing_cli_files` | function | `fn installing_skills_does_not_delete_existing_cli_files() {` | `installing_skills_does_not_delete_existing_cli_files [function]` | `763371cd-4805-55d6-a148-30cea10b3791` | 191-220 [crates/gcode/src/skill.rs:191-220] | Indexed function `installing_skills_does_not_delete_existing_cli_files` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:191-220] |
