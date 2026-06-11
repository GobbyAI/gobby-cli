---
title: crates/gcode/src/commands/codewiki/reuse.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/reuse.rs
  ranges:
  - 11-19
  - 21-96
  - 22-31
  - 36-46
  - 49-57
  - 59-86
  - 88-95
  - 100-102
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/reuse.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/reuse.rs` exposes 8 indexed API symbols.
[crates/gcode/src/commands/codewiki/reuse.rs:11-19]
[crates/gcode/src/commands/codewiki/reuse.rs:21-96]
[crates/gcode/src/commands/codewiki/reuse.rs:22-31]
[crates/gcode/src/commands/codewiki/reuse.rs:36-46]
[crates/gcode/src/commands/codewiki/reuse.rs:49-57]

## API Symbols

- `ReusePlan` (class) component `ReusePlan [class]` (`eec87db6-f257-5625-9121-33908d777619`) lines 11-19 [crates/gcode/src/commands/codewiki/reuse.rs:11-19]
  - Signature: `pub(crate) struct ReusePlan {`
  - Purpose: ReusePlan caches documentation metadata and file-content hashes with lazy evaluation to enable incremental content reuse across a project, using `None` sentinel values to mark unhashable sources that should not be reprocessed. [crates/gcode/src/commands/codewiki/reuse.rs:11-19]
- `ReusePlan` (class) component `ReusePlan [class]` (`cce1752d-eb6f-5274-b167-b70c61f01758`) lines 21-96 [crates/gcode/src/commands/codewiki/reuse.rs:21-96]
  - Signature: `impl ReusePlan {`
  - Purpose: ReusePlan is an incremental documentation cache that determines whether previously generated pages can be reused by validating that source file hashes, dependency sets, and AI mode remain unchanged. [crates/gcode/src/commands/codewiki/reuse.rs:21-96]
- `ReusePlan.load` (method) component `ReusePlan.load [method]` (`cce62242-a527-5177-9502-c73105dbc509`) lines 22-31 [crates/gcode/src/commands/codewiki/reuse.rs:22-31]
  - Signature: `pub(crate) fn load(project_root: &Path, out_dir: &Path, ai_mode: &str) -> anyhow::Result<Self> {`
  - Purpose: Constructs a Self instance by reading persisted codewiki metadata from the output directory and initializing fields with the provided project root, output directory, AI mode, and an empty hash map. [crates/gcode/src/commands/codewiki/reuse.rs:22-31]
- `ReusePlan.reusable_page` (method) component `ReusePlan.reusable_page [method]` (`c4fae48a-685c-593e-831c-dab9e872d3af`) lines 36-46 [crates/gcode/src/commands/codewiki/reuse.rs:36-46]
  - Signature: `pub(crate) fn reusable_page(`
  - Purpose: Reads and returns the file contents of a document at a sanitized output path if the document is marked as reusable for the given sources, otherwise returns None. [crates/gcode/src/commands/codewiki/reuse.rs:36-46]
- `ReusePlan.reusable_page_with_summary` (method) component `ReusePlan.reusable_page_with_summary [method]` (`015125b2-7388-5621-8d0d-9cb2a00b81fb`) lines 49-57 [crates/gcode/src/commands/codewiki/reuse.rs:49-57]
  - Signature: `pub(crate) fn reusable_page_with_summary(`
  - Purpose: Retrieves and returns an optional tuple containing a document's reusable page representation and cloned summary for a given path, or `None` if either resource is unavailable. [crates/gcode/src/commands/codewiki/reuse.rs:49-57]
- `ReusePlan.reusable` (method) component `ReusePlan.reusable [method]` (`ef01acbe-dd9e-560c-b4b6-ff06c49ab56f`) lines 59-86 [crates/gcode/src/commands/codewiki/reuse.rs:59-86]
  - Signature: `fn reusable(&mut self, doc_path: &str, sources: &BTreeSet<String>) -> bool {`
  - Purpose: Validates whether a cached document entry is reusable by confirming it is non-degraded, has consistent AI mode, matching source file hashes, and an existing output document. [crates/gcode/src/commands/codewiki/reuse.rs:59-86]
- `ReusePlan.current_hash` (method) component `ReusePlan.current_hash [method]` (`fdaca5c2-56ed-533e-9e35-f57fdf7045e1`) lines 88-95 [crates/gcode/src/commands/codewiki/reuse.rs:88-95]
  - Signature: `fn current_hash(&mut self, file: &str) -> Option<String> {`
  - Purpose: Computes and caches the content hash of a file, returning the memoized result on subsequent accesses. [crates/gcode/src/commands/codewiki/reuse.rs:88-95]
- `span_files` (function) component `span_files [function]` (`a7cc51b8-68bb-59e7-8c5a-8d02dc1e585a`) lines 100-102 [crates/gcode/src/commands/codewiki/reuse.rs:100-102]
  - Signature: `pub(crate) fn span_files(spans: &[SourceSpan]) -> BTreeSet<String> {`
  - Purpose: Extracts the file paths from a slice of `SourceSpan` objects into a sorted, deduplicated set of strings via `BTreeSet`. [crates/gcode/src/commands/codewiki/reuse.rs:100-102]

