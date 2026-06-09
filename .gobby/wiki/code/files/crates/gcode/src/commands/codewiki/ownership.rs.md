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
  - 171-196
  - 198-243
  - 245-247
  - 249-280
  - 282-303
  - 305-339
  - 307-322
  - 341-343
  - 345-371
  - 373-385
  - 387-397
  - 399-421
  - 423-429
  - 431-453
  - 464-491
  - 494-514
  - 517-538
  - 541-564
  - 567-586
  - 588-593
  - 595-614
  - 616-625
  - 627-643
  - 645-653
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
  - 171-196
  - 198-243
  - 245-247
  - 249-280
  - 282-303
  - 305-339
  - 307-322
  - 341-343
  - 345-371
  - 373-385
  - 387-397
  - 399-421
  - 423-429
  - 431-453
  - 464-491
  - 494-514
  - 517-538
  - 541-564
  - 567-586
  - 588-593
  - 595-614
  - 616-625
  - 627-643
  - 645-653
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
[crates/gcode/src/commands/codewiki/ownership.rs:130-148] [crates/gcode/src/commands/codewiki/ownership.rs:150-169] [crates/gcode/src/commands/codewiki/ownership.rs:171-196] [crates/gcode/src/commands/codewiki/ownership.rs:198-243]
[crates/gcode/src/commands/codewiki/ownership.rs:245-247] [crates/gcode/src/commands/codewiki/ownership.rs:249-280] [crates/gcode/src/commands/codewiki/ownership.rs:282-303] [crates/gcode/src/commands/codewiki/ownership.rs:305-339]
[crates/gcode/src/commands/codewiki/ownership.rs:307-322] [crates/gcode/src/commands/codewiki/ownership.rs:341-343] [crates/gcode/src/commands/codewiki/ownership.rs:345-371] [crates/gcode/src/commands/codewiki/ownership.rs:373-385]
[crates/gcode/src/commands/codewiki/ownership.rs:387-397] [crates/gcode/src/commands/codewiki/ownership.rs:399-421] [crates/gcode/src/commands/codewiki/ownership.rs:423-429] [crates/gcode/src/commands/codewiki/ownership.rs:431-453]
[crates/gcode/src/commands/codewiki/ownership.rs:464-491] [crates/gcode/src/commands/codewiki/ownership.rs:494-514] [crates/gcode/src/commands/codewiki/ownership.rs:517-538] [crates/gcode/src/commands/codewiki/ownership.rs:541-564]
[crates/gcode/src/commands/codewiki/ownership.rs:567-586] [crates/gcode/src/commands/codewiki/ownership.rs:588-593] [crates/gcode/src/commands/codewiki/ownership.rs:595-614] [crates/gcode/src/commands/codewiki/ownership.rs:616-625]
[crates/gcode/src/commands/codewiki/ownership.rs:627-643] [crates/gcode/src/commands/codewiki/ownership.rs:645-653]

## API Symbols

- `OwnershipOptions` (class) component `OwnershipOptions [class]` (`1a412fa9-ffc9-5eab-9e91-b90e886ab286`) lines 13-16 [crates/gcode/src/commands/codewiki/ownership.rs:13-16]
  - Signature: `pub(crate) struct OwnershipOptions {`
  - Purpose: `OwnershipOptions` is a crate-private configuration struct that encapsulates blame operation parameters: a file capacity limit and a timeout duration. [crates/gcode/src/commands/codewiki/ownership.rs:13-16]
- `OwnershipOptions` (class) component `OwnershipOptions [class]` (`fd470077-3483-5806-88fd-eb87dd55dc0b`) lines 18-25 [crates/gcode/src/commands/codewiki/ownership.rs:18-25]
  - Signature: `impl Default for OwnershipOptions {`
  - Purpose: A `Default` trait implementation that instantiates `OwnershipOptions` with a blame file capacity of 200 and a blame operation timeout of 20 seconds. [crates/gcode/src/commands/codewiki/ownership.rs:18-25]
- `OwnershipOptions.default` (method) component `OwnershipOptions.default [method]` (`e652c60e-08d1-511e-9ab7-ef87f35db83e`) lines 19-24 [crates/gcode/src/commands/codewiki/ownership.rs:19-24]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a default `Self` instance with `blame_file_cap` set to 200 and `blame_timeout` set to 20 seconds. [crates/gcode/src/commands/codewiki/ownership.rs:19-24]
- `OwnershipMeta` (class) component `OwnershipMeta [class]` (`0db7980a-63e6-57ab-90a5-8848a79307da`) lines 28-31 [crates/gcode/src/commands/codewiki/ownership.rs:28-31]
  - Signature: `pub(crate) struct OwnershipMeta {`
  - Purpose: OwnershipMeta is a crate-internal struct that maintains a BTreeMap associating file paths to cached blame summaries with serde default initialization support. [crates/gcode/src/commands/codewiki/ownership.rs:28-31]
- `CachedBlameSummary` (class) component `CachedBlameSummary [class]` (`544abd88-cfbe-53ee-8f94-79488de3d5c0`) lines 34-37 [crates/gcode/src/commands/codewiki/ownership.rs:34-37]
  - Signature: `pub(crate) struct CachedBlameSummary {`
  - Purpose: CachedBlameSummary is a crate-internal cache structure that stores a content hash for invalidation and a vector of ownership contributors for blame/authorship tracking. [crates/gcode/src/commands/codewiki/ownership.rs:34-37]
- `OwnershipContributor` (class) component `OwnershipContributor [class]` (`4dfb9dd3-d878-5252-993a-f006dcf8a065`) lines 40-45 [crates/gcode/src/commands/codewiki/ownership.rs:40-45]
  - Signature: `pub(crate) struct OwnershipContributor {`
  - Purpose: `OwnershipContributor` is a crate-private struct that represents a code contributor with their name, optional email address, and line count contribution, conditionally serializing the email field only when present. [crates/gcode/src/commands/codewiki/ownership.rs:40-45]
- `Codeowners` (class) component `Codeowners [class]` (`2182266f-82fa-5c68-a9de-f21a035733ee`) lines 48-50 [crates/gcode/src/commands/codewiki/ownership.rs:48-50]
  - Signature: `struct Codeowners {`
  - Purpose: `Codeowners` is a struct that wraps a vector of `CodeownersEntry` items, representing a collection of parsed codeowner mappings. [crates/gcode/src/commands/codewiki/ownership.rs:48-50]
- `CodeownersEntry` (class) component `CodeownersEntry [class]` (`322902f3-e510-5ab1-a083-ba0449074ba8`) lines 53-56 [crates/gcode/src/commands/codewiki/ownership.rs:53-56]
  - Signature: `struct CodeownersEntry {`
  - Purpose: `CodeownersEntry` is a struct that maps a file pattern to a vector of owner identifiers for CODEOWNERS-based code ownership tracking. [crates/gcode/src/commands/codewiki/ownership.rs:53-56]
- `OwnershipStatus` (class) component `OwnershipStatus [class]` (`b214e5ab-4f69-5aaf-b156-b02260be38b5`) lines 59-63 [crates/gcode/src/commands/codewiki/ownership.rs:59-63]
  - Signature: `struct OwnershipStatus {`
  - Purpose: `OwnershipStatus` is a struct that tracks the availability of code ownership metadata through three boolean flags indicating whether codeowners data, git blame data, and partial status information are available. [crates/gcode/src/commands/codewiki/ownership.rs:59-63]
- `FileOwnership` (class) component `FileOwnership [class]` (`4e1a85d1-35a2-51ef-8b39-17035639dbbe`) lines 66-69 [crates/gcode/src/commands/codewiki/ownership.rs:66-69]
  - Signature: `struct FileOwnership {`
  - Purpose: `FileOwnership` is a struct that aggregates explicit ownership declarations (as `Vec<String>`) with inferred ownership information computed from `OwnershipContributor` entries. [crates/gcode/src/commands/codewiki/ownership.rs:66-69]
- `build_ownership_doc` (function) component `build_ownership_doc [function]` (`dac79f42-a25f-5a0a-be06-680dce7aeb45`) lines 71-116 [crates/gcode/src/commands/codewiki/ownership.rs:71-116]
  - Signature: `pub(crate) fn build_ownership_doc(`
  - Purpose: Generates a markdown document that aggregates declared (CODEOWNERS-based) and derived (git blame-based) code ownership information for specified project files. [crates/gcode/src/commands/codewiki/ownership.rs:71-116]
- `read_codeowners` (function) component `read_codeowners [function]` (`9dcf41a0-ef09-5f86-be61-df3ec6c3115b`) lines 118-128 [crates/gcode/src/commands/codewiki/ownership.rs:118-128]
  - Signature: `fn read_codeowners(project_root: &Path) -> anyhow::Result<Option<Codeowners>> {`
  - Purpose: Reads and parses a CODEOWNERS file from one of three conventional project paths (`CODEOWNERS`, `.github/CODEOWNERS`, or `docs/CODEOWNERS`), returning the parsed configuration on success or `None` if no file is found. [crates/gcode/src/commands/codewiki/ownership.rs:118-128]
- `parse_codeowners` (function) component `parse_codeowners [function]` (`8f44a134-477a-5025-b3b4-f0b53992a09d`) lines 130-148 [crates/gcode/src/commands/codewiki/ownership.rs:130-148]
  - Signature: `fn parse_codeowners(raw: &str) -> Codeowners {`
  - Purpose: Parses a CODEOWNERS file format string into a Codeowners struct by extracting file pattern and owner identifier pairs from non-empty, non-comment lines. [crates/gcode/src/commands/codewiki/ownership.rs:130-148]
- `declared_owners_for_files` (function) component `declared_owners_for_files [function]` (`a80586f6-12c1-5d4d-a4fe-095348149298`) lines 150-169 [crates/gcode/src/commands/codewiki/ownership.rs:150-169]
  - Signature: `fn declared_owners_for_files(`
  - Purpose: This function returns a BTreeMap that associates each input file with its declared owners by matching it against CODEOWNERS patterns in reverse iteration order, returning only files with matching patterns. [crates/gcode/src/commands/codewiki/ownership.rs:150-169]
- `codeowners_pattern_matches` (function) component `codeowners_pattern_matches [function]` (`16380659-8199-5345-8239-8262b27258a0`) lines 171-196 [crates/gcode/src/commands/codewiki/ownership.rs:171-196]
  - Signature: `fn codeowners_pattern_matches(pattern: &str, file: &str) -> bool {`
  - Purpose: Determines whether a file path matches a CODEOWNERS-style pattern by normalizing the pattern and applying directory prefix matching, glob wildcard expansion, or path-component matching rules. [crates/gcode/src/commands/codewiki/ownership.rs:171-196]
- `derived_owners_for_files` (function) component `derived_owners_for_files [function]` (`d8f4b0fb-7c06-51b3-9108-88f62eec16a1`) lines 198-243 [crates/gcode/src/commands/codewiki/ownership.rs:198-243]
  - Signature: `fn derived_owners_for_files(`
  - Purpose: Derives file ownership contributors through cached git blame analysis, with early termination based on file count and elapsed time limits. [crates/gcode/src/commands/codewiki/ownership.rs:198-243]
- `content_hash` (function) component `content_hash [function]` (`73020b57-8262-56fc-a32f-167b42bac26b`) lines 245-247 [crates/gcode/src/commands/codewiki/ownership.rs:245-247]
  - Signature: `fn content_hash(project_root: &Path, file: &str) -> Option<String> {`
  - Purpose: Computes the content hash of a file located at the resolved path (project_root/file), returning Some(hash) on success or None on error. [crates/gcode/src/commands/codewiki/ownership.rs:245-247]
- `blame_file_contributors` (function) component `blame_file_contributors [function]` (`a4620f28-afee-5fba-a5d0-8fe5148fe893`) lines 249-280 [crates/gcode/src/commands/codewiki/ownership.rs:249-280]
  - Signature: `fn blame_file_contributors(`
  - Purpose: This function performs git blame analysis on a specified file to aggregate authored lines by contributor (name and email), then returns the top 5 contributors sorted by line count in descending order. [crates/gcode/src/commands/codewiki/ownership.rs:249-280]
- `degraded_sources` (function) component `degraded_sources [function]` (`5bc744c8-59c9-5b7b-bfb6-70e4078112a3`) lines 282-303 [crates/gcode/src/commands/codewiki/ownership.rs:282-303]
  - Signature: `fn degraded_sources(`
  - Purpose: Returns a vector of string identifiers indicating specific sources of ownership information degradation: unavailable codeowners file, unavailable or partial git blame data, or absence of declared and derived ownership across all files. [crates/gcode/src/commands/codewiki/ownership.rs:282-303]
- `ownership_frontmatter` (function) component `ownership_frontmatter [function]` (`58a5e201-7b0d-5dcb-b616-f915b9383335`) lines 305-339 [crates/gcode/src/commands/codewiki/ownership.rs:305-339]
  - Signature: `fn ownership_frontmatter(partial: bool, degraded_sources: &[String]) -> String {`
  - Purpose: Serializes code ownership metadata into a YAML frontmatter string with conditional degradation status and partiality fields. [crates/gcode/src/commands/codewiki/ownership.rs:305-339]
- `Frontmatter` (class) component `Frontmatter [class]` (`ca082da0-d1d6-5a0b-b62b-68848e9213b7`) lines 307-322 [crates/gcode/src/commands/codewiki/ownership.rs:307-322]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: `Frontmatter` is a serializable metadata struct with lifetime-bounded string references that tracks content provenance, source quality metrics (trust, freshness), generation parameters, and degradation/partial-completion states with conditional field serialization rules. [crates/gcode/src/commands/codewiki/ownership.rs:307-322]
- `is_false` (function) component `is_false [function]` (`87851973-3388-5e07-98a9-d39ceaf45f04`) lines 341-343 [crates/gcode/src/commands/codewiki/ownership.rs:341-343]
  - Signature: `fn is_false(value: &bool) -> bool {`
  - Purpose: Dereferences a boolean reference and returns its logical negation. [crates/gcode/src/commands/codewiki/ownership.rs:341-343]
- `write_modules` (function) component `write_modules [function]` (`f6ca5087-f87d-5cb4-8d51-65ba9dfa47be`) lines 345-371 [crates/gcode/src/commands/codewiki/ownership.rs:345-371]
  - Signature: `fn write_modules(`
  - Purpose: Generates markdown documentation by grouping files from an ownership map by their assigned modules and writing aggregated primary owners and contributors for each module. [crates/gcode/src/commands/codewiki/ownership.rs:345-371]
- `write_files` (function) component `write_files [function]` (`b66b849c-fde7-5470-a558-399a383bb261`) lines 373-385 [crates/gcode/src/commands/codewiki/ownership.rs:373-385]
  - Signature: `fn write_files(doc: &mut String, by_file: &BTreeMap<String, FileOwnership>) {`
  - Purpose: Generates and appends a markdown section documenting file ownership by iterating through a BTreeMap and writing declared owners and derived contributors for each file, with fallback text for files with unknown ownership. [crates/gcode/src/commands/codewiki/ownership.rs:373-385]
- `aggregate_primary` (function) component `aggregate_primary [function]` (`f7bb8be3-3dea-5005-9f34-f242bc889788`) lines 387-397 [crates/gcode/src/commands/codewiki/ownership.rs:387-397]
  - Signature: `fn aggregate_primary(files: &[(&String, &FileOwnership)]) -> Vec<String> {`
  - Purpose: Aggregates primary owners from multiple files by collecting declared owners or, if absent, the first derived owner per file, then returns a deduplicated sorted vector of owner names. [crates/gcode/src/commands/codewiki/ownership.rs:387-397]
- `aggregate_contributors` (function) component `aggregate_contributors [function]` (`291bc225-1c4c-5343-8bc7-0a3e7a7fa0c7`) lines 399-421 [crates/gcode/src/commands/codewiki/ownership.rs:399-421]
  - Signature: `fn aggregate_contributors(files: &[(&String, &FileOwnership)]) -> Vec<OwnershipContributor> {`
  - Purpose: Aggregates and counts lines contributed by each (name, email) pair across multiple files, sorts by lines descending with secondary sorts on name and email, and returns the top 5 contributors. [crates/gcode/src/commands/codewiki/ownership.rs:399-421]
- `write_owner_line` (function) component `write_owner_line [function]` (`d857744a-7d59-5910-8b5b-03abee37771d`) lines 423-429 [crates/gcode/src/commands/codewiki/ownership.rs:423-429]
  - Signature: `fn write_owner_line(doc: &mut String, label: &str, owners: &[String]) {`
  - Purpose: Appends a formatted line to a mutable String containing a label paired with either "unknown" or a comma-separated list of owner names. [crates/gcode/src/commands/codewiki/ownership.rs:423-429]
- `write_contributor_line` (function) component `write_contributor_line [function]` (`9e74b9ff-1a2a-544d-97ad-9aeea79429c7`) lines 431-453 [crates/gcode/src/commands/codewiki/ownership.rs:431-453]
  - Signature: `fn write_contributor_line(doc: &mut String, contributors: &[OwnershipContributor]) {`
  - Purpose: Appends a formatted "Top contributors" line to a mutable string, displaying each contributor's name and line count (with correct singular/plural inflection), or "unknown" if the contributors slice is empty. [crates/gcode/src/commands/codewiki/ownership.rs:431-453]
- `codewiki_ownership_codeowners_only_maps_declared_owners` (function) component `codewiki_ownership_codeowners_only_maps_declared_owners [function]` (`396dbe67-3b75-5b7b-8e2e-8a96243d2269`) lines 464-491 [crates/gcode/src/commands/codewiki/ownership.rs:464-491]
  - Signature: `fn codewiki_ownership_codeowners_only_maps_declared_owners() {`
  - Purpose: Tests that the ownership document builder correctly maps declared owners from a CODEOWNERS file to modules and marks the result as degraded when git blame is unavailable. [crates/gcode/src/commands/codewiki/ownership.rs:464-491]
- `codewiki_ownership_derives_top_committers_from_gix_blame` (function) component `codewiki_ownership_derives_top_committers_from_gix_blame [function]` (`336dede6-56eb-591c-b2b2-bbbaf3b8e106`) lines 494-514 [crates/gcode/src/commands/codewiki/ownership.rs:494-514]
  - Signature: `fn codewiki_ownership_derives_top_committers_from_gix_blame() {`
  - Purpose: This test verifies that the ownership documentation builder correctly derives and lists top committers (identified via gix blame analysis) in the generated ownership metadata for a source file. [crates/gcode/src/commands/codewiki/ownership.rs:494-514]
- `codewiki_ownership_declared_owners_take_primary_precedence` (function) component `codewiki_ownership_declared_owners_take_primary_precedence [function]` (`0bd61aca-c99e-5b46-aa6e-c50007e4bcdd`) lines 517-538 [crates/gcode/src/commands/codewiki/ownership.rs:517-538]
  - Signature: `fn codewiki_ownership_declared_owners_take_primary_precedence() {`
  - Purpose: Verifies that declared owners specified in CODEOWNERS take primary precedence over blame-based contributors in the generated ownership documentation, ensuring declared owners appear while blame-derived contributors do not. [crates/gcode/src/commands/codewiki/ownership.rs:517-538]
- `codewiki_ownership_without_sources_degrades_to_unknown` (function) component `codewiki_ownership_without_sources_degrades_to_unknown [function]` (`b073a8a4-a30b-5885-a92c-fe3680002fdc`) lines 541-564 [crates/gcode/src/commands/codewiki/ownership.rs:541-564]
  - Signature: `fn codewiki_ownership_without_sources_degrades_to_unknown() {`
  - Purpose: Tests that ownership documentation degrades to an unknown state when neither CODEOWNERS nor git blame data sources are available. [crates/gcode/src/commands/codewiki/ownership.rs:541-564]
- `codewiki_ownership_file_cap_marks_partial` (function) component `codewiki_ownership_file_cap_marks_partial [function]` (`153bba6b-3c40-52b0-985e-1bab0ec0b872`) lines 567-586 [crates/gcode/src/commands/codewiki/ownership.rs:567-586]
  - Signature: `fn codewiki_ownership_file_cap_marks_partial() {`
  - Purpose: Tests that a `blame_file_cap` constraint correctly marks an ownership document as partial and limits file processing when fewer files are processed than requested. [crates/gcode/src/commands/codewiki/ownership.rs:567-586]
- `modules` (function) component `modules [function]` (`90890558-f2cb-58ca-aa73-c5a8db55ed59`) lines 588-593 [crates/gcode/src/commands/codewiki/ownership.rs:588-593]
  - Signature: `fn modules<const N: usize>(items: [(&str, &str); N]) -> HashMap<String, String> {`
  - Purpose: Converts a const-generic-sized array of (file, module) string reference pairs into a HashMap with owned String keys and values. [crates/gcode/src/commands/codewiki/ownership.rs:588-593]
- `git_project_with_history` (function) component `git_project_with_history [function]` (`331e6ded-bbaf-549d-92e6-db67432ff715`) lines 595-614 [crates/gcode/src/commands/codewiki/ownership.rs:595-614]
  - Signature: `fn git_project_with_history() -> tempfile::TempDir {`
  - Purpose: Creates and returns a temporary directory containing a git repository initialized with two sequential commits that track modifications to `src/lib.rs` from different authors. [crates/gcode/src/commands/codewiki/ownership.rs:595-614]
- `git_project_with_two_files` (function) component `git_project_with_two_files [function]` (`e1c89552-06a3-5893-9de8-7fa78c8b80fd`) lines 616-625 [crates/gcode/src/commands/codewiki/ownership.rs:616-625]
  - Signature: `fn git_project_with_two_files() -> tempfile::TempDir {`
  - Purpose: Creates and returns a temporary directory containing a git-initialized Rust project with two source files (`src/a.rs` and `src/b.rs`) staged and committed by author Alice. [crates/gcode/src/commands/codewiki/ownership.rs:616-625]
- `git_author` (function) component `git_author [function]` (`7ea608a9-235e-506e-b72a-53d652f528b0`) lines 627-643 [crates/gcode/src/commands/codewiki/ownership.rs:627-643]
  - Signature: `fn git_author(repo: &Path, name: &str, email: &str, message: &str) {`
  - Purpose: Executes a git commit in the specified repository with temporary author configuration (name and email), panicking if the operation fails. [crates/gcode/src/commands/codewiki/ownership.rs:627-643]
- `git` (function) component `git [function]` (`16d6f495-24c5-55db-81d3-dcd5717d5c52`) lines 645-653 [crates/gcode/src/commands/codewiki/ownership.rs:645-653]
  - Signature: `fn git(repo: &Path, args: &[&str]) {`
  - Purpose: Executes a git command in a specified repository directory, panicking if the command fails to execute or returns a non-zero exit status. [crates/gcode/src/commands/codewiki/ownership.rs:645-653]

