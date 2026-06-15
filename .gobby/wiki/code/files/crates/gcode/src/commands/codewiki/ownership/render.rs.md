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

# crates/gcode/src/commands/codewiki/ownership/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Purpose

Builds the Codewiki code-ownership render output. It first derives a list of degraded provenance flags from overall ownership status and whether any files have declared or derived ownership, then serializes YAML frontmatter for the page with generated metadata, optional degraded/partial markers, and a stable schema. The remaining helpers format the ownership body: they write module and file sections, compute primary ownership and aggregate contributor totals with deterministic identities, and emit the per-owner and per-contributor lines that make up the final report.
[crates/gcode/src/commands/codewiki/ownership/render.rs:10-34]
[crates/gcode/src/commands/codewiki/ownership/render.rs:36-68]
[crates/gcode/src/commands/codewiki/ownership/render.rs:38-52]
[crates/gcode/src/commands/codewiki/ownership/render.rs:70-72]
[crates/gcode/src/commands/codewiki/ownership/render.rs:74-100]

## API Symbols

- `degraded_sources` (function) component `degraded_sources [function]` (`50920e55-cf5e-5112-ad77-822ba34fe62b`) lines 10-34 [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34]
  - Signature: `pub(super) fn degraded_sources(`
  - Purpose: Indexed function `degraded_sources` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34]
- `ownership_frontmatter` (function) component `ownership_frontmatter [function]` (`48ca619a-d7bc-59fa-a10e-f8acf9c10363`) lines 36-68 [crates/gcode/src/commands/codewiki/ownership/render.rs:36-68]
  - Signature: `pub(super) fn ownership_frontmatter(partial: bool, degraded_sources: &[String]) -> String {`
  - Purpose: Indexed function `ownership_frontmatter` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:36-68]
- `Frontmatter` (class) component `Frontmatter [class]` (`f034c4da-42e6-59a4-b0a0-f0ec45bf3452`) lines 38-52 [crates/gcode/src/commands/codewiki/ownership/render.rs:38-52]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: Indexed class `Frontmatter` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:38-52]
- `is_false` (function) component `is_false [function]` (`05ae00f9-a722-5ad4-a323-d3dd0b0a664b`) lines 70-72 [crates/gcode/src/commands/codewiki/ownership/render.rs:70-72]
  - Signature: `fn is_false(value: &bool) -> bool {`
  - Purpose: Indexed function `is_false` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:70-72]
- `write_modules` (function) component `write_modules [function]` (`f8d33520-f172-5739-88bc-31fb182f8888`) lines 74-100 [crates/gcode/src/commands/codewiki/ownership/render.rs:74-100]
  - Signature: `pub(super) fn write_modules(`
  - Purpose: Indexed function `write_modules` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:74-100]
- `write_files` (function) component `write_files [function]` (`1076ddc3-1d5d-5db2-83b1-774040ebbf48`) lines 102-114 [crates/gcode/src/commands/codewiki/ownership/render.rs:102-114]
  - Signature: `pub(super) fn write_files(doc: &mut String, by_file: &BTreeMap<String, FileOwnership>) {`
  - Purpose: Indexed function `write_files` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:102-114]
- `aggregate_primary` (function) component `aggregate_primary [function]` (`5af25571-0a4f-5774-bcd8-c1706f2dbaff`) lines 116-126 [crates/gcode/src/commands/codewiki/ownership/render.rs:116-126]
  - Signature: `fn aggregate_primary(files: &[(&String, &FileOwnership)]) -> Vec<String> {`
  - Purpose: Indexed function `aggregate_primary` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:116-126]
- `aggregate_contributors` (function) component `aggregate_contributors [function]` (`4157ac5f-7eba-5c56-8f43-64db9958c306`) lines 128-172 [crates/gcode/src/commands/codewiki/ownership/render.rs:128-172]
  - Signature: `fn aggregate_contributors(files: &[(&String, &FileOwnership)]) -> Vec<OwnershipContributor> {`
  - Purpose: Aggregates all derived contributors across the input files by contributor ID, merges their line counts while deterministically preserving a stable name/email identity, then returns the top five 'OwnershipContributor' records sorted by descending lines, ascending name, and ascending contributor ID. [crates/gcode/src/commands/codewiki/ownership/render.rs:128-172]
- `write_owner_line` (function) component `write_owner_line [function]` (`77306155-d2df-548d-a1df-889d0b0e27c0`) lines 174-180 [crates/gcode/src/commands/codewiki/ownership/render.rs:174-180]
  - Signature: `fn write_owner_line(doc: &mut String, label: &str, owners: &[String]) {`
  - Purpose: Indexed function `write_owner_line` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:174-180]
- `write_contributor_line` (function) component `write_contributor_line [function]` (`e2c7f95a-4bce-5b63-8701-8a5dc000af1a`) lines 182-204 [crates/gcode/src/commands/codewiki/ownership/render.rs:182-204]
  - Signature: `fn write_contributor_line(doc: &mut String, contributors: &[OwnershipContributor]) {`
  - Purpose: Indexed function `write_contributor_line` in `crates/gcode/src/commands/codewiki/ownership/render.rs`. [crates/gcode/src/commands/codewiki/ownership/render.rs:182-204]

