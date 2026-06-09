---
title: crates/gcode/src/commands/codewiki/ownership.rs
type: code_file
source:
- file: crates/gcode/src/commands/codewiki/ownership.rs
  ranges:
  - 13-16
  - 18-25
  - 19-24
  - 28-31
  - 34-37
  - 40-45
  - 48-50
  - 53-56
  - 59-63
  - 66-69
  - 71-116
  - 118-128
  - 130-148
  - 150-169
  - 171-206
  - 208-253
  - 255-257
  - 259-290
  - 292-313
  - 315-349
  - 317-332
  - 351-353
  - 355-381
  - 383-395
  - 397-407
  - 409-431
  - 433-439
  - 441-463
  - 474-501
  - 504-524
  - 527-548
  - 551-574
  - 577-596
  - 598-603
  - 605-624
  - 626-635
  - 637-653
  - 655-663
provenance:
- file: crates/gcode/src/commands/codewiki/ownership.rs
  ranges:
  - 13-16
  - 18-25
  - 19-24
  - 28-31
  - 34-37
  - 40-45
  - 48-50
  - 53-56
  - 59-63
  - 66-69
  - 71-116
  - 118-128
  - 130-148
  - 150-169
  - 171-206
  - 208-253
  - 255-257
  - 259-290
  - 292-313
  - 315-349
  - 317-332
  - 351-353
  - 355-381
  - 383-395
  - 397-407
  - 409-431
  - 433-439
  - 441-463
  - 474-501
  - 504-524
  - 527-548
  - 551-574
  - 577-596
  - 598-603
  - 605-624
  - 626-635
  - 637-653
  - 655-663
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/ownership.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/ownership.rs` exposes 38 indexed API symbols.
[crates/gcode/src/commands/codewiki/ownership.rs:13-16] [crates/gcode/src/commands/codewiki/ownership.rs:18-25] [crates/gcode/src/commands/codewiki/ownership.rs:19-24] [crates/gcode/src/commands/codewiki/ownership.rs:28-31]
[crates/gcode/src/commands/codewiki/ownership.rs:34-37] [crates/gcode/src/commands/codewiki/ownership.rs:40-45] [crates/gcode/src/commands/codewiki/ownership.rs:48-50] [crates/gcode/src/commands/codewiki/ownership.rs:53-56]
[crates/gcode/src/commands/codewiki/ownership.rs:59-63] [crates/gcode/src/commands/codewiki/ownership.rs:66-69] [crates/gcode/src/commands/codewiki/ownership.rs:71-116] [crates/gcode/src/commands/codewiki/ownership.rs:118-128]
[crates/gcode/src/commands/codewiki/ownership.rs:130-148] [crates/gcode/src/commands/codewiki/ownership.rs:150-169] [crates/gcode/src/commands/codewiki/ownership.rs:171-206] [crates/gcode/src/commands/codewiki/ownership.rs:208-253]
[crates/gcode/src/commands/codewiki/ownership.rs:255-257] [crates/gcode/src/commands/codewiki/ownership.rs:259-290] [crates/gcode/src/commands/codewiki/ownership.rs:292-313] [crates/gcode/src/commands/codewiki/ownership.rs:315-349]
[crates/gcode/src/commands/codewiki/ownership.rs:317-332] [crates/gcode/src/commands/codewiki/ownership.rs:351-353] [crates/gcode/src/commands/codewiki/ownership.rs:355-381] [crates/gcode/src/commands/codewiki/ownership.rs:383-395]
[crates/gcode/src/commands/codewiki/ownership.rs:397-407] [crates/gcode/src/commands/codewiki/ownership.rs:409-431] [crates/gcode/src/commands/codewiki/ownership.rs:433-439] [crates/gcode/src/commands/codewiki/ownership.rs:441-463]
[crates/gcode/src/commands/codewiki/ownership.rs:474-501] [crates/gcode/src/commands/codewiki/ownership.rs:504-524] [crates/gcode/src/commands/codewiki/ownership.rs:527-548] [crates/gcode/src/commands/codewiki/ownership.rs:551-574]
[crates/gcode/src/commands/codewiki/ownership.rs:577-596] [crates/gcode/src/commands/codewiki/ownership.rs:598-603] [crates/gcode/src/commands/codewiki/ownership.rs:605-624] [crates/gcode/src/commands/codewiki/ownership.rs:626-635]
[crates/gcode/src/commands/codewiki/ownership.rs:637-653] [crates/gcode/src/commands/codewiki/ownership.rs:655-663]

## API Symbols

- `OwnershipOptions` (class) component `OwnershipOptions [class]` (`1a412fa9-ffc9-5eab-9e91-b90e886ab286`) lines 13-16 [crates/gcode/src/commands/codewiki/ownership.rs:13-16]
  - Signature: `pub(crate) struct OwnershipOptions {`
  - Purpose: `OwnershipOptions` is a crate-private struct that encapsulates configuration parameters for blame operations, comprising a file capacity limit (`usize`) and an operation timeout (`Duration`). [crates/gcode/src/commands/codewiki/ownership.rs:13-16]
- `OwnershipOptions` (class) component `OwnershipOptions [class]` (`fd470077-3483-5806-88fd-eb87dd55dc0b`) lines 18-25 [crates/gcode/src/commands/codewiki/ownership.rs:18-25]
  - Signature: `impl Default for OwnershipOptions {`
  - Purpose: The `Default` trait implementation for `OwnershipOptions` initializes `blame_file_cap` to 200 and `blame_timeout` to a 20-second duration. [crates/gcode/src/commands/codewiki/ownership.rs:18-25]
- `OwnershipOptions.default` (method) component `OwnershipOptions.default [method]` (`e652c60e-08d1-511e-9ab7-ef87f35db83e`) lines 19-24 [crates/gcode/src/commands/codewiki/ownership.rs:19-24]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `OwnershipOptions.default` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:19-24]
- `OwnershipMeta` (class) component `OwnershipMeta [class]` (`0db7980a-63e6-57ab-90a5-8848a79307da`) lines 28-31 [crates/gcode/src/commands/codewiki/ownership.rs:28-31]
  - Signature: `pub(crate) struct OwnershipMeta {`
  - Purpose: Indexed class `OwnershipMeta` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:28-31]
- `CachedBlameSummary` (class) component `CachedBlameSummary [class]` (`544abd88-cfbe-53ee-8f94-79488de3d5c0`) lines 34-37 [crates/gcode/src/commands/codewiki/ownership.rs:34-37]
  - Signature: `pub(crate) struct CachedBlameSummary {`
  - Purpose: Indexed class `CachedBlameSummary` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:34-37]
- `OwnershipContributor` (class) component `OwnershipContributor [class]` (`4dfb9dd3-d878-5252-993a-f006dcf8a065`) lines 40-45 [crates/gcode/src/commands/codewiki/ownership.rs:40-45]
  - Signature: `pub(crate) struct OwnershipContributor {`
  - Purpose: Indexed class `OwnershipContributor` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:40-45]
- `Codeowners` (class) component `Codeowners [class]` (`2182266f-82fa-5c68-a9de-f21a035733ee`) lines 48-50 [crates/gcode/src/commands/codewiki/ownership.rs:48-50]
  - Signature: `struct Codeowners {`
  - Purpose: Indexed class `Codeowners` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:48-50]
- `CodeownersEntry` (class) component `CodeownersEntry [class]` (`322902f3-e510-5ab1-a083-ba0449074ba8`) lines 53-56 [crates/gcode/src/commands/codewiki/ownership.rs:53-56]
  - Signature: `struct CodeownersEntry {`
  - Purpose: Indexed class `CodeownersEntry` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:53-56]
- `OwnershipStatus` (class) component `OwnershipStatus [class]` (`b214e5ab-4f69-5aaf-b156-b02260be38b5`) lines 59-63 [crates/gcode/src/commands/codewiki/ownership.rs:59-63]
  - Signature: `struct OwnershipStatus {`
  - Purpose: Indexed class `OwnershipStatus` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:59-63]
- `FileOwnership` (class) component `FileOwnership [class]` (`4e1a85d1-35a2-51ef-8b39-17035639dbbe`) lines 66-69 [crates/gcode/src/commands/codewiki/ownership.rs:66-69]
  - Signature: `struct FileOwnership {`
  - Purpose: Indexed class `FileOwnership` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:66-69]
- `build_ownership_doc` (function) component `build_ownership_doc [function]` (`dac79f42-a25f-5a0a-be06-680dce7aeb45`) lines 71-116 [crates/gcode/src/commands/codewiki/ownership.rs:71-116]
  - Signature: `pub(crate) fn build_ownership_doc(`
  - Purpose: Indexed function `build_ownership_doc` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:71-116]
- `read_codeowners` (function) component `read_codeowners [function]` (`9dcf41a0-ef09-5f86-be61-df3ec6c3115b`) lines 118-128 [crates/gcode/src/commands/codewiki/ownership.rs:118-128]
  - Signature: `fn read_codeowners(project_root: &Path) -> anyhow::Result<Option<Codeowners>> {`
  - Purpose: Indexed function `read_codeowners` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:118-128]
- `parse_codeowners` (function) component `parse_codeowners [function]` (`8f44a134-477a-5025-b3b4-f0b53992a09d`) lines 130-148 [crates/gcode/src/commands/codewiki/ownership.rs:130-148]
  - Signature: `fn parse_codeowners(raw: &str) -> Codeowners {`
  - Purpose: Indexed function `parse_codeowners` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:130-148]
- `declared_owners_for_files` (function) component `declared_owners_for_files [function]` (`a80586f6-12c1-5d4d-a4fe-095348149298`) lines 150-169 [crates/gcode/src/commands/codewiki/ownership.rs:150-169]
  - Signature: `fn declared_owners_for_files(`
  - Purpose: Indexed function `declared_owners_for_files` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:150-169]
- `codeowners_pattern_matches` (function) component `codeowners_pattern_matches [function]` (`16380659-8199-5345-8239-8262b27258a0`) lines 171-206 [crates/gcode/src/commands/codewiki/ownership.rs:171-206]
  - Signature: `fn codeowners_pattern_matches(pattern: &str, file: &str) -> bool {`
  - Purpose: Determines if a file path matches a CODEOWNERS pattern by applying glob or literal matching, scoped to full path or basename depending on pattern syntax. [crates/gcode/src/commands/codewiki/ownership.rs:171-206]
- `derived_owners_for_files` (function) component `derived_owners_for_files [function]` (`440d8976-0ef5-5d57-ac85-b94354607fcb`) lines 208-253 [crates/gcode/src/commands/codewiki/ownership.rs:208-253]
  - Signature: `fn derived_owners_for_files(`
  - Purpose: # Summary

Returns a map of file paths to ownership contributors by computing git blame results with content-hash-based caching, subject to configurable file count and timeout limits. [crates/gcode/src/commands/codewiki/ownership.rs:208-253]
- `content_hash` (function) component `content_hash [function]` (`8273b13c-705c-586b-a7bd-4b08c1e00599`) lines 255-257 [crates/gcode/src/commands/codewiki/ownership.rs:255-257]
  - Signature: `fn content_hash(project_root: &Path, file: &str) -> Option<String> {`
  - Purpose: Returns the content hash of a file located at the path formed by joining the project root with a relative file path, or None if hashing fails. [crates/gcode/src/commands/codewiki/ownership.rs:255-257]
- `blame_file_contributors` (function) component `blame_file_contributors [function]` (`f3c5cfea-551f-5218-9a33-d4f69fca40be`) lines 259-290 [crates/gcode/src/commands/codewiki/ownership.rs:259-290]
  - Signature: `fn blame_file_contributors(`
  - Purpose: Executes git blame on a specified file, aggregates line counts by commit author, and returns the top 5 contributors ranked by lines of code modified. [crates/gcode/src/commands/codewiki/ownership.rs:259-290]
- `degraded_sources` (function) component `degraded_sources [function]` (`6f204b45-c613-5e32-9a7e-f8ffbff4306f`) lines 292-313 [crates/gcode/src/commands/codewiki/ownership.rs:292-313]
  - Signature: `fn degraded_sources(`
  - Purpose: # Summary

Returns a vector of strings identifying degraded or unavailable code ownership data sources by checking CODEOWNERS availability, git blame availability/completeness, and universal file ownership coverage. [crates/gcode/src/commands/codewiki/ownership.rs:292-313]
- `ownership_frontmatter` (function) component `ownership_frontmatter [function]` (`a62cf571-1081-5e28-9632-f9319c3e1393`) lines 315-349 [crates/gcode/src/commands/codewiki/ownership.rs:315-349]
  - Signature: `fn ownership_frontmatter(partial: bool, degraded_sources: &[String]) -> String {`
  - Purpose: Indexed function `ownership_frontmatter` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:315-349]
- `Frontmatter` (class) component `Frontmatter [class]` (`6c766f92-52b4-54cb-a18f-2b15e0485f9e`) lines 317-332 [crates/gcode/src/commands/codewiki/ownership.rs:317-332]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: Indexed class `Frontmatter` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:317-332]
- `is_false` (function) component `is_false [function]` (`2bf49954-92e7-562d-8e40-7e8fda6b28a5`) lines 351-353 [crates/gcode/src/commands/codewiki/ownership.rs:351-353]
  - Signature: `fn is_false(value: &bool) -> bool {`
  - Purpose: Indexed function `is_false` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:351-353]
- `write_modules` (function) component `write_modules [function]` (`c76ec4d2-e3a3-5af9-bb69-a4e7b0216ebd`) lines 355-381 [crates/gcode/src/commands/codewiki/ownership.rs:355-381]
  - Signature: `fn write_modules(`
  - Purpose: Indexed function `write_modules` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:355-381]
- `write_files` (function) component `write_files [function]` (`1de9889e-babb-56ba-a8b0-bf56b54a7b8e`) lines 383-395 [crates/gcode/src/commands/codewiki/ownership.rs:383-395]
  - Signature: `fn write_files(doc: &mut String, by_file: &BTreeMap<String, FileOwnership>) {`
  - Purpose: Indexed function `write_files` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:383-395]
- `aggregate_primary` (function) component `aggregate_primary [function]` (`b4ebf07f-4df2-5a4b-86d1-ee814f385c57`) lines 397-407 [crates/gcode/src/commands/codewiki/ownership.rs:397-407]
  - Signature: `fn aggregate_primary(files: &[(&String, &FileOwnership)]) -> Vec<String> {`
  - Purpose: Indexed function `aggregate_primary` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:397-407]
- `aggregate_contributors` (function) component `aggregate_contributors [function]` (`c7cc0b35-e4ab-5cc6-bd60-9acfe9200427`) lines 409-431 [crates/gcode/src/commands/codewiki/ownership.rs:409-431]
  - Signature: `fn aggregate_contributors(files: &[(&String, &FileOwnership)]) -> Vec<OwnershipContributor> {`
  - Purpose: Indexed function `aggregate_contributors` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:409-431]
- `write_owner_line` (function) component `write_owner_line [function]` (`8f1872b4-20b9-5cea-bb00-7bf461cac854`) lines 433-439 [crates/gcode/src/commands/codewiki/ownership.rs:433-439]
  - Signature: `fn write_owner_line(doc: &mut String, label: &str, owners: &[String]) {`
  - Purpose: Indexed function `write_owner_line` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:433-439]
- `write_contributor_line` (function) component `write_contributor_line [function]` (`890368f6-00dd-5477-b0a7-b16e3c4cb25b`) lines 441-463 [crates/gcode/src/commands/codewiki/ownership.rs:441-463]
  - Signature: `fn write_contributor_line(doc: &mut String, contributors: &[OwnershipContributor]) {`
  - Purpose: Indexed function `write_contributor_line` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:441-463]
- `codewiki_ownership_codeowners_only_maps_declared_owners` (function) component `codewiki_ownership_codeowners_only_maps_declared_owners [function]` (`9db352b3-4c52-5f9e-a28f-c01f407612b5`) lines 474-501 [crates/gcode/src/commands/codewiki/ownership.rs:474-501]
  - Signature: `fn codewiki_ownership_codeowners_only_maps_declared_owners() {`
  - Purpose: Indexed function `codewiki_ownership_codeowners_only_maps_declared_owners` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:474-501]
- `codewiki_ownership_derives_top_committers_from_gix_blame` (function) component `codewiki_ownership_derives_top_committers_from_gix_blame [function]` (`3b3080d8-81db-5b3d-b5a7-d2a2d2bcccaa`) lines 504-524 [crates/gcode/src/commands/codewiki/ownership.rs:504-524]
  - Signature: `fn codewiki_ownership_derives_top_committers_from_gix_blame() {`
  - Purpose: Indexed function `codewiki_ownership_derives_top_committers_from_gix_blame` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:504-524]
- `codewiki_ownership_declared_owners_take_primary_precedence` (function) component `codewiki_ownership_declared_owners_take_primary_precedence [function]` (`90d2a40b-94ff-5ec9-a567-80ad9dd153a5`) lines 527-548 [crates/gcode/src/commands/codewiki/ownership.rs:527-548]
  - Signature: `fn codewiki_ownership_declared_owners_take_primary_precedence() {`
  - Purpose: Indexed function `codewiki_ownership_declared_owners_take_primary_precedence` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:527-548]
- `codewiki_ownership_without_sources_degrades_to_unknown` (function) component `codewiki_ownership_without_sources_degrades_to_unknown [function]` (`fba1e7c8-a580-5700-8611-54de86d42267`) lines 551-574 [crates/gcode/src/commands/codewiki/ownership.rs:551-574]
  - Signature: `fn codewiki_ownership_without_sources_degrades_to_unknown() {`
  - Purpose: Indexed function `codewiki_ownership_without_sources_degrades_to_unknown` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:551-574]
- `codewiki_ownership_file_cap_marks_partial` (function) component `codewiki_ownership_file_cap_marks_partial [function]` (`07b3ea08-4c1c-5303-a7d4-ca5e4f7f0a87`) lines 577-596 [crates/gcode/src/commands/codewiki/ownership.rs:577-596]
  - Signature: `fn codewiki_ownership_file_cap_marks_partial() {`
  - Purpose: Indexed function `codewiki_ownership_file_cap_marks_partial` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:577-596]
- `modules` (function) component `modules [function]` (`53f6781b-60b1-59de-bc42-a775056e31a5`) lines 598-603 [crates/gcode/src/commands/codewiki/ownership.rs:598-603]
  - Signature: `fn modules<const N: usize>(items: [(&str, &str); N]) -> HashMap<String, String> {`
  - Purpose: Indexed function `modules` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:598-603]
- `git_project_with_history` (function) component `git_project_with_history [function]` (`5633aa61-d42e-5c04-a19b-511b80f65dc6`) lines 605-624 [crates/gcode/src/commands/codewiki/ownership.rs:605-624]
  - Signature: `fn git_project_with_history() -> tempfile::TempDir {`
  - Purpose: Indexed function `git_project_with_history` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:605-624]
- `git_project_with_two_files` (function) component `git_project_with_two_files [function]` (`1825a373-fc69-5c96-a04a-54a5295f61c3`) lines 626-635 [crates/gcode/src/commands/codewiki/ownership.rs:626-635]
  - Signature: `fn git_project_with_two_files() -> tempfile::TempDir {`
  - Purpose: Indexed function `git_project_with_two_files` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:626-635]
- `git_author` (function) component `git_author [function]` (`5961933e-9d02-55c5-9c45-471a1ef147ed`) lines 637-653 [crates/gcode/src/commands/codewiki/ownership.rs:637-653]
  - Signature: `fn git_author(repo: &Path, name: &str, email: &str, message: &str) {`
  - Purpose: Indexed function `git_author` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:637-653]
- `git` (function) component `git [function]` (`ba6c63ac-2506-53db-866d-024c7e86271a`) lines 655-663 [crates/gcode/src/commands/codewiki/ownership.rs:655-663]
  - Signature: `fn git(repo: &Path, args: &[&str]) {`
  - Purpose: Indexed function `git` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:655-663]

