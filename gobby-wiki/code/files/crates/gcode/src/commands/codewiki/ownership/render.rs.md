---
title: crates/gcode/src/commands/codewiki/ownership/render.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/render.rs
  ranges:
  - 10-34
  - 36-68
  - 70-72
  - 74-100
  - 102-114
  - 116-126
  - 128-172
  - 174-180
  - 182-204
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34](crates/gcode/src/commands/codewiki/ownership/render.rs#L10-L34), [crates/gcode/src/commands/codewiki/ownership/render.rs:36-68](crates/gcode/src/commands/codewiki/ownership/render.rs#L36-L68), [crates/gcode/src/commands/codewiki/ownership/render.rs:70-72](crates/gcode/src/commands/codewiki/ownership/render.rs#L70-L72), [crates/gcode/src/commands/codewiki/ownership/render.rs:74-100](crates/gcode/src/commands/codewiki/ownership/render.rs#L74-L100), [crates/gcode/src/commands/codewiki/ownership/render.rs:102-114](crates/gcode/src/commands/codewiki/ownership/render.rs#L102-L114), [crates/gcode/src/commands/codewiki/ownership/render.rs:116-126](crates/gcode/src/commands/codewiki/ownership/render.rs#L116-L126), [crates/gcode/src/commands/codewiki/ownership/render.rs:128-172](crates/gcode/src/commands/codewiki/ownership/render.rs#L128-L172), [crates/gcode/src/commands/codewiki/ownership/render.rs:174-180](crates/gcode/src/commands/codewiki/ownership/render.rs#L174-L180), [crates/gcode/src/commands/codewiki/ownership/render.rs:182-204](crates/gcode/src/commands/codewiki/ownership/render.rs#L182-L204)

</details>

# crates/gcode/src/commands/codewiki/ownership/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Purpose

Builds the codewiki ownership page output: it derives degraded provenance flags from `OwnershipStatus` and per-file ownership data, serializes YAML frontmatter for a “Code Ownership” document, and then formats ownership content by writing module and file sections. The helper functions split the work into small steps: `degraded_sources` records missing or partial input signals, `ownership_frontmatter` emits the generated page metadata, `is_false` supports YAML serialization, and the `write_*`/`aggregate_*` helpers organize owners and contributors into deterministic lines for modules and files.
[crates/gcode/src/commands/codewiki/ownership/render.rs:10-34]
[crates/gcode/src/commands/codewiki/ownership/render.rs:36-68]
[crates/gcode/src/commands/codewiki/ownership/render.rs:38-52]
[crates/gcode/src/commands/codewiki/ownership/render.rs:70-72]
[crates/gcode/src/commands/codewiki/ownership/render.rs:74-100]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `degraded_sources` | function | `pub(super) fn degraded_sources(` | `degraded_sources [function]` | `50920e55-cf5e-5112-ad77-822ba34fe62b` | 10-34 [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34] | Indexed function `degraded_sources` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34] |
| `ownership_frontmatter` | function | `pub(super) fn ownership_frontmatter(partial: bool, degraded_sources: &[String]) -> String {` | `ownership_frontmatter [function]` | `48ca619a-d7bc-59fa-a10e-f8acf9c10363` | 36-68 [crates/gcode/src/commands/codewiki/ownership/render.rs:36-68] | Indexed function `ownership_frontmatter` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:36-68] |
| `Frontmatter` | class | `struct Frontmatter<'a> {` | `Frontmatter [class]` | `f034c4da-42e6-59a4-b0a0-f0ec45bf3452` | 38-52 [crates/gcode/src/commands/codewiki/ownership/render.rs:38-52] | Indexed class `Frontmatter` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:38-52] |
| `is_false` | function | `fn is_false(value: &bool) -> bool {` | `is_false [function]` | `05ae00f9-a722-5ad4-a323-d3dd0b0a664b` | 70-72 [crates/gcode/src/commands/codewiki/ownership/render.rs:70-72] | Indexed function `is_false` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:70-72] |
| `write_modules` | function | `pub(super) fn write_modules(` | `write_modules [function]` | `f8d33520-f172-5739-88bc-31fb182f8888` | 74-100 [crates/gcode/src/commands/codewiki/ownership/render.rs:74-100] | Indexed function `write_modules` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:74-100] |
| `write_files` | function | `pub(super) fn write_files(doc: &mut String, by_file: &BTreeMap<String, FileOwnership>) {` | `write_files [function]` | `1076ddc3-1d5d-5db2-83b1-774040ebbf48` | 102-114 [crates/gcode/src/commands/codewiki/ownership/render.rs:102-114] | Indexed function `write_files` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:102-114] |
| `aggregate_primary` | function | `fn aggregate_primary(files: &[(&String, &FileOwnership)]) -> Vec<String> {` | `aggregate_primary [function]` | `5af25571-0a4f-5774-bcd8-c1706f2dbaff` | 116-126 [crates/gcode/src/commands/codewiki/ownership/render.rs:116-126] | Indexed function `aggregate_primary` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:116-126] |
| `aggregate_contributors` | function | `fn aggregate_contributors(files: &[(&String, &FileOwnership)]) -> Vec<OwnershipContributor> {` | `aggregate_contributors [function]` | `4157ac5f-7eba-5c56-8f43-64db9958c306` | 128-172 [crates/gcode/src/commands/codewiki/ownership/render.rs:128-172] | Indexed function `aggregate_contributors` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:128-172] |
| `write_owner_line` | function | `fn write_owner_line(doc: &mut String, label: &str, owners: &[String]) {` | `write_owner_line [function]` | `77306155-d2df-548d-a1df-889d0b0e27c0` | 174-180 [crates/gcode/src/commands/codewiki/ownership/render.rs:174-180] | Indexed function `write_owner_line` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:174-180] |
| `write_contributor_line` | function | `fn write_contributor_line(doc: &mut String, contributors: &[OwnershipContributor]) {` | `write_contributor_line [function]` | `e2c7f95a-4bce-5b63-8701-8a5dc000af1a` | 182-204 [crates/gcode/src/commands/codewiki/ownership/render.rs:182-204] | Indexed function `write_contributor_line` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:182-204] |
