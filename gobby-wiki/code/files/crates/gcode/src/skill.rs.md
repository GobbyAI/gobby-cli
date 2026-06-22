---
title: crates/gcode/src/skill.rs
type: code_file
provenance:
- file: crates/gcode/src/skill.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/skill.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/skill.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/skill.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SkillTarget` | class | 'SkillTarget' is a struct that identifies an install target by a static display name and an internal 'InstallKind' value. [crates/gcode/src/skill.rs:20-23] |
| `InstallKind` | type | Indexed type `InstallKind` in `crates/gcode/src/skill.rs`. [crates/gcode/src/skill.rs:26-29] |
| `supported_targets` | function | Returns the static slice 'SKILL_TARGETS' as the set of supported 'SkillTarget' values. [crates/gcode/src/skill.rs:61-63] |
| `install_skill` | function | Dispatches to either 'install_claude_plugin(project_root)' or 'install_skill_dir(project_root, cli_dir)' based on 'target.kind', returning the resulting 'std::io::Result<String>'. [crates/gcode/src/skill.rs:67-72] |
| `install_claude_plugin` | function | Creates '.claude-plugin/plugin.json' and 'skills/gcode/SKILL.md' under 'project_root' with predefined contents, then returns '"skills/gcode/SKILL.md"' on success. [crates/gcode/src/skill.rs:75-85] |
| `install_skill_dir` | function | Creates '<project_root>/<cli_dir>/skills/gcode', writes 'SKILL.md' there with 'SKILL_CONTENT', and returns the relative path '"{cli_dir}/skills/gcode/SKILL.md"' on success. [crates/gcode/src/skill.rs:88-94] |
| `target_path` | function | Returns the 'SKILL.md' path for the 'gcode' skill under either the project root or a CLI-specific directory, depending on whether 'target.kind' is 'ClaudePlugin' or 'SkillDir { cli_dir }'. [crates/gcode/src/skill.rs:100-107] |
| `expected_reported_path` | function | Returns the expected 'SKILL.md' report path for a target, using the fixed 'skills/gcode/SKILL.md' location for 'ClaudePlugin' installs and '${cli_dir}/skills/gcode/SKILL.md' for 'SkillDir' installs. [crates/gcode/src/skill.rs:109-114] |

_Verified by 5 in-file unit tests._

