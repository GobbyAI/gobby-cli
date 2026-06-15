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

# crates/gcode/src/commands/codewiki/ownership/codeowners.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]

## Purpose

Parses CODEOWNERS files from a project root, stores the rules as pattern-to-owners entries, and resolves file ownership by matching each path against the last applicable rule. `read_codeowners` searches the standard CODEOWNERS locations and loads the first one it finds, `parse_codeowners` turns the file into structured entries while ignoring blanks, comments, and ownerless lines, `declared_owners_for_files` maps each input file to its matched owners, and `codeowners_pattern_matches` implements the path-matching rules used to compare patterns against file paths.
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:15-25]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:27-45]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:47-66]

## API Symbols

- `Codeowners` (class) component `Codeowners [class]` (`b7214f2b-5200-5b3b-8a05-ce29fa302ae5`) lines 5-7 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7]
  - Signature: `pub(super) struct Codeowners {`
  - Purpose: 'Codeowners' is a 'pub(super)' struct that encapsulates a 'Vec<CodeownersEntry>' named 'entries'. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7]
- `CodeownersEntry` (class) component `CodeownersEntry [class]` (`0b77a9c2-942f-57a0-8b0a-c397639e536d`) lines 10-13 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13]
  - Signature: `struct CodeownersEntry {`
  - Purpose: 'CodeownersEntry' is a struct that represents a CODEOWNERS rule by pairing a path 'pattern' string with a list of owning user or team identifiers in 'owners'. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13]
- `read_codeowners` (function) component `read_codeowners [function]` (`0eb87879-c0f9-507c-8a1b-b76628a55cd2`) lines 15-25 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:15-25]
  - Signature: `pub(super) fn read_codeowners(project_root: &Path) -> anyhow::Result<Option<Codeowners>> {`
  - Purpose: Attempts to read and parse the first existing 'CODEOWNERS' file found at 'CODEOWNERS', '.github/CODEOWNERS', or 'docs/CODEOWNERS' under 'project_root', returning 'Ok(Some(Codeowners))' on success, propagating non-'NotFound' I/O errors, and 'Ok(None)' if none exist. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:15-25]
- `parse_codeowners` (function) component `parse_codeowners [function]` (`384dc2ca-c42f-5ae2-b6a6-4ffc836578a9`) lines 27-45 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:27-45]
  - Signature: `fn parse_codeowners(raw: &str) -> Codeowners {`
  - Purpose: Parses a CODEOWNERS-formatted string into a 'Codeowners' by trimming each line, skipping blanks and comment-only lines, splitting remaining lines into a pattern and whitespace-separated owners up to an inline '#' comment, and collecting only entries with at least one owner. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:27-45]
- `declared_owners_for_files` (function) component `declared_owners_for_files [function]` (`a804138c-ec87-50d6-8d3a-8f8f8c23b1c5`) lines 47-66 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:47-66]
  - Signature: `pub(super) fn declared_owners_for_files(`
  - Purpose: Returns a 'BTreeMap' from each input file path to the owners from the last matching 'Codeowners' entry, or an empty map if no 'Codeowners' is provided. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:47-66]
- `codeowners_pattern_matches` (function) component `codeowners_pattern_matches [function]` (`06e9f2ac-39d4-5519-b820-9c91e7df61ba`) lines 68-103 [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:68-103]
  - Signature: `fn codeowners_pattern_matches(pattern: &str, file: &str) -> bool {`
  - Purpose: Returns 'true' when a CODEOWNERS pattern, after stripping a leading '/', matches the given file path by directory-prefix semantics for trailing '/', glob matching for '*', '?', or '[' patterns, exact-or-descendant path matching for slash-containing literals, and basename equality for simple literals. [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:68-103]

