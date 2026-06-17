---
title: crates/gcode/src/commands/codewiki/ownership/codeowners.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/codeowners.rs
  ranges:
  - 5-7
  - 10-13
  - 15-25
  - 27-45
  - 47-66
  - 68-103
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7](crates/gcode/src/commands/codewiki/ownership/codeowners.rs#L5-L7), [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13](crates/gcode/src/commands/codewiki/ownership/codeowners.rs#L10-L13), [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:15-25](crates/gcode/src/commands/codewiki/ownership/codeowners.rs#L15-L25), [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:27-45](crates/gcode/src/commands/codewiki/ownership/codeowners.rs#L27-L45), [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:47-66](crates/gcode/src/commands/codewiki/ownership/codeowners.rs#L47-L66), [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:68-103](crates/gcode/src/commands/codewiki/ownership/codeowners.rs#L68-L103)

</details>

# crates/gcode/src/commands/codewiki/ownership/codeowners.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Purpose

This file loads a repository’s CODEOWNERS data from `CODEOWNERS`, `.github/CODEOWNERS`, or `docs/CODEOWNERS`, parses it into an internal list of pattern-to-owner entries, and then resolves ownership for a set of files. `declared_owners_for_files` applies the parsed rules with last-match-wins behavior, while `codeowners_pattern_matches` handles path normalization plus simple prefix and glob-style matching.
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:15-25]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:27-45]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:47-66]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Codeowners` | class | `pub(super) struct Codeowners {` | `Codeowners [class]` | `b7214f2b-5200-5b3b-8a05-ce29fa302ae5` | 5-7 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7] | Indexed class `Codeowners` in `crates/gcode/src/commands/codewiki/ownership/codeowners.rs`. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7] |
| `CodeownersEntry` | class | `struct CodeownersEntry {` | `CodeownersEntry [class]` | `0b77a9c2-942f-57a0-8b0a-c397639e536d` | 10-13 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13] | Indexed class `CodeownersEntry` in `crates/gcode/src/commands/codewiki/ownership/codeowners.rs`. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13] |
| `read_codeowners` | function | `pub(super) fn read_codeowners(project_root: &Path) -> anyhow::Result<Option<Codeowners>> {` | `read_codeowners [function]` | `0eb87879-c0f9-507c-8a1b-b76628a55cd2` | 15-25 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:15-25] | Indexed function `read_codeowners` in `crates/gcode/src/commands/codewiki/ownership/codeowners.rs`. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:15-25] |
| `parse_codeowners` | function | `fn parse_codeowners(raw: &str) -> Codeowners {` | `parse_codeowners [function]` | `384dc2ca-c42f-5ae2-b6a6-4ffc836578a9` | 27-45 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:27-45] | Indexed function `parse_codeowners` in `crates/gcode/src/commands/codewiki/ownership/codeowners.rs`. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:27-45] |
| `declared_owners_for_files` | function | `pub(super) fn declared_owners_for_files(` | `declared_owners_for_files [function]` | `a804138c-ec87-50d6-8d3a-8f8f8c23b1c5` | 47-66 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:47-66] | Indexed function `declared_owners_for_files` in `crates/gcode/src/commands/codewiki/ownership/codeowners.rs`. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:47-66] |
| `codeowners_pattern_matches` | function | `fn codeowners_pattern_matches(pattern: &str, file: &str) -> bool {` | `codeowners_pattern_matches [function]` | `06e9f2ac-39d4-5519-b820-9c91e7df61ba` | 68-103 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:68-103] | Indexed function `codeowners_pattern_matches` in `crates/gcode/src/commands/codewiki/ownership/codeowners.rs`. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:68-103] |
