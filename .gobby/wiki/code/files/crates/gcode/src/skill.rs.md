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

# crates/gcode/src/skill.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/skill.rs` exposes 13 indexed API symbols.
[crates/gcode/src/skill.rs:20-23]
[crates/gcode/src/skill.rs:26-29]
[crates/gcode/src/skill.rs:61-63]
[crates/gcode/src/skill.rs:67-72]
[crates/gcode/src/skill.rs:75-85]

## API Symbols

- `SkillTarget` (class) component `SkillTarget [class]` (`5a41c0d8-d3ac-577b-8a2f-141c12fdb8c5`) lines 20-23 [crates/gcode/src/skill.rs:20-23]
  - Signature: `pub struct SkillTarget {`
  - Purpose: `SkillTarget` is a struct that encapsulates a skill identifier with a public static display name and a private `InstallKind` field for type-safe skill categorization. [crates/gcode/src/skill.rs:20-23]
- `InstallKind` (type) component `InstallKind [type]` (`1ddf8fc8-5593-56e8-889f-8eb842a4fdb4`) lines 26-29 [crates/gcode/src/skill.rs:26-29]
  - Signature: `enum InstallKind {`
  - Purpose: Indexed type `InstallKind` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:26-29]
- `supported_targets` (function) component `supported_targets [function]` (`e754ea69-291a-54da-bf88-8dcfd72a920e`) lines 61-63 [crates/gcode/src/skill.rs:61-63]
  - Signature: `pub fn supported_targets() -> &'static [SkillTarget] {`
  - Purpose: Returns a static reference to a slice of `SkillTarget` values representing the available skill targets. [crates/gcode/src/skill.rs:61-63]
- `install_skill` (function) component `install_skill [function]` (`f4026363-dfb6-5286-acc2-5a86c632d07f`) lines 67-72 [crates/gcode/src/skill.rs:67-72]
  - Signature: `pub fn install_skill(project_root: &Path, target: &SkillTarget) -> std::io::Result<String> {`
  - Purpose: Routes skill installation requests to the appropriate handler (`install_claude_plugin` or `install_skill_dir`) based on the `SkillTarget.kind` variant, returning a String result or I/O error. [crates/gcode/src/skill.rs:67-72]
- `install_claude_plugin` (function) component `install_claude_plugin [function]` (`e57757de-fa8f-547a-8aa9-7d140d1970c5`) lines 75-85 [crates/gcode/src/skill.rs:75-85]
  - Signature: `fn install_claude_plugin(project_root: &Path) -> std::io::Result<String> {`
  - Purpose: Creates and populates `.claude-plugin` and `skills/gcode` directories with configuration and skill definition files, returning the path to the created SKILL.md file. [crates/gcode/src/skill.rs:75-85]
- `install_skill_dir` (function) component `install_skill_dir [function]` (`39d2c4fc-8622-55d4-bea7-0206eb612361`) lines 88-94 [crates/gcode/src/skill.rs:88-94]
  - Signature: `fn install_skill_dir(project_root: &Path, cli_dir: &str) -> std::io::Result<String> {`
  - Purpose: Creates a nested directory structure for a gcode skill at `project_root/cli_dir/skills/gcode/`, writes a skill manifest file (SKILL.md) to it, and returns the relative file path. [crates/gcode/src/skill.rs:88-94]
- `target_path` (function) component `target_path [function]` (`f5127b17-bbd0-5674-880c-a48b16e55c6b`) lines 100-107 [crates/gcode/src/skill.rs:100-107]
  - Signature: `fn target_path(project_root: &Path, target: &SkillTarget) -> std::path::PathBuf {`
  - Purpose: Resolves the filesystem path to a skill manifest file (SKILL.md) based on the target installation kind, either at the project root for ClaudePlugin or nested under a specified CLI directory for SkillDir. [crates/gcode/src/skill.rs:100-107]
- `expected_reported_path` (function) component `expected_reported_path [function]` (`49d13cc4-d67f-54a4-9b43-0fc64a6ddd77`) lines 109-114 [crates/gcode/src/skill.rs:109-114]
  - Signature: `fn expected_reported_path(target: &SkillTarget) -> String {`
  - Purpose: This function constructs the expected filesystem path to a gcode skill's SKILL.md documentation file, returning either a fixed path for Claude plugin installations or a user-specified CLI directory path for skill directory installations. [crates/gcode/src/skill.rs:109-114]
- `plugin_json_is_valid` (function) component `plugin_json_is_valid [function]` (`03634f4d-8a9a-546f-ac12-55889da932ba`) lines 117-128 [crates/gcode/src/skill.rs:117-128]
  - Signature: `fn plugin_json_is_valid() {`
  - Purpose: This function validates that the plugin manifest JSON contains the expected metadata: a "name" field set to "gcode", a "version" field set to "0.1.0", and a non-empty "description" field. [crates/gcode/src/skill.rs:117-128]
- `supported_targets_are_stable` (function) component `supported_targets_are_stable [function]` (`d765a135-4f04-5ba7-ac6b-d2d077a8f544`) lines 131-148 [crates/gcode/src/skill.rs:131-148]
  - Signature: `fn supported_targets_are_stable() {`
  - Purpose: This function asserts that the display names of supported compilation targets remain stable and match a hardcoded list of six expected target identifiers. [crates/gcode/src/skill.rs:131-148]
- `installs_skill_to_all_supported_target_paths` (function) component `installs_skill_to_all_supported_target_paths [function]` (`76a52bfa-6711-5213-872c-422f93d36c99`) lines 151-164 [crates/gcode/src/skill.rs:151-164]
  - Signature: `fn installs_skill_to_all_supported_target_paths() {`
  - Purpose: This test function verifies that `install_skill()` correctly installs skill content to all supported targets and returns the expected installation paths for each. [crates/gcode/src/skill.rs:151-164]
- `claude_plugin_manifest_is_written` (function) component `claude_plugin_manifest_is_written [function]` (`223d866d-626c-567b-b1d6-88465ce3d9d4`) lines 167-188 [crates/gcode/src/skill.rs:167-188]
  - Signature: `fn claude_plugin_manifest_is_written() {`
  - Purpose: Verifies that installing a skill for the Claude Code target writes a plugin.json manifest with the correct gcode skill name, description, version, and installation path. [crates/gcode/src/skill.rs:167-188]
- `installing_skills_does_not_delete_existing_cli_files` (function) component `installing_skills_does_not_delete_existing_cli_files [function]` (`763371cd-4805-55d6-a148-30cea10b3791`) lines 191-220 [crates/gcode/src/skill.rs:191-220]
  - Signature: `fn installing_skills_does_not_delete_existing_cli_files() {`
  - Purpose: This test asserts that installing skills for all supported targets does not delete or overwrite existing CLI configuration and user files in the installation directory. [crates/gcode/src/skill.rs:191-220]

