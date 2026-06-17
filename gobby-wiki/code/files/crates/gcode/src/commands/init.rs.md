---
title: crates/gcode/src/commands/init.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/init.rs
  ranges:
  - 11-148
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/init.rs:11-148](crates/gcode/src/commands/init.rs#L11-L148)

</details>

# crates/gcode/src/commands/init.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Defines the `run` command for project initialization. It resolves or generates the project identity, optionally writes `gcode.json`, classifies the project state, installs supported AI CLI skills unless the project is managed by Gobby, and then prepares the database-backed indexing context so the project can be auto-indexed during setup. [crates/gcode/src/commands/init.rs:11-148]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `run` | function | `pub fn run(project_root: &Path, format: Format, quiet: bool) -> anyhow::Result<()> {` | `run [function]` | `fe31a853-1683-5729-9359-f9f539491450` | 11-148 [crates/gcode/src/commands/init.rs:11-148] | Indexed function `run` in `crates/gcode/src/commands/init.rs`. [crates/gcode/src/commands/init.rs:11-148] |
