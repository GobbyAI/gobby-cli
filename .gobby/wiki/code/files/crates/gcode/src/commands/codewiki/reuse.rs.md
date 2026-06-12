---
title: crates/gcode/src/commands/codewiki/reuse.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/reuse.rs
  ranges:
  - 11-19
  - 21-101
  - 105-107
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/reuse.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/reuse.rs` exposes 8 indexed API symbols.
[crates/gcode/src/commands/codewiki/reuse.rs:11-19]
[crates/gcode/src/commands/codewiki/reuse.rs:21-101]
[crates/gcode/src/commands/codewiki/reuse.rs:22-31]
[crates/gcode/src/commands/codewiki/reuse.rs:36-46]
[crates/gcode/src/commands/codewiki/reuse.rs:49-57]

## API Symbols

- `ReusePlan` (class) component `ReusePlan [class]` (`eec87db6-f257-5625-9121-33908d777619`) lines 11-19 [crates/gcode/src/commands/codewiki/reuse.rs:11-19]
  - Signature: `pub(crate) struct ReusePlan {`
  - Purpose: `ReusePlan` is an internal planning struct that records the project root, output directory, AI mode, document metadata, and lazily cached current-content hashes to determine which generated codewiki docs can be safely reused, while treating unhashable files as one-time-probed non-reusable inputs. [crates/gcode/src/commands/codewiki/reuse.rs:11-19]
- `ReusePlan` (class) component `ReusePlan [class]` (`cce1752d-eb6f-5274-b167-b70c61f01758`) lines 21-101 [crates/gcode/src/commands/codewiki/reuse.rs:21-101]
  - Signature: `impl ReusePlan {`
  - Purpose: `ReusePlan` loads prior codewiki metadata for a project and uses the current `ai_mode`, output directory, and source-hash set to decide whether a documentation page and its recorded summary can be reused verbatim from disk or must be regenerated. [crates/gcode/src/commands/codewiki/reuse.rs:21-101]
- `ReusePlan.load` (method) component `ReusePlan.load [method]` (`cce62242-a527-5177-9502-c73105dbc509`) lines 22-31 [crates/gcode/src/commands/codewiki/reuse.rs:22-31]
  - Signature: `pub(crate) fn load(project_root: &Path, out_dir: &Path, ai_mode: &str) -> anyhow::Result<Self> {`
  - Purpose: `load` reads the existing codewiki metadata from `out_dir` and returns a new instance initialized with the provided `project_root`, `out_dir`, and `ai_mode`, reusing the previously stored `docs` while resetting `current_hashes` to an empty `BTreeMap`. [crates/gcode/src/commands/codewiki/reuse.rs:22-31]
- `ReusePlan.reusable_page` (method) component `ReusePlan.reusable_page [method]` (`c4fae48a-685c-593e-831c-dab9e872d3af`) lines 36-46 [crates/gcode/src/commands/codewiki/reuse.rs:36-46]
  - Signature: `pub(crate) fn reusable_page(`
  - Purpose: Returns `Some(contents)` by first verifying `doc_path` is reusable for the given `sources`, then resolving a safe output path under `out_dir` and reading that file as UTF-8 text, otherwise returns `None` on any check or I/O failure. [crates/gcode/src/commands/codewiki/reuse.rs:36-46]
- `ReusePlan.reusable_page_with_summary` (method) component `ReusePlan.reusable_page_with_summary [method]` (`015125b2-7388-5621-8d0d-9cb2a00b81fb`) lines 49-57 [crates/gcode/src/commands/codewiki/reuse.rs:49-57]
  - Signature: `pub(crate) fn reusable_page_with_summary(`
  - Purpose: It clones the stored summary for `doc_path`, then returns it paired with `reusable_page(doc_path, sources)` as `Some((page, summary))`, or `None` if the document, summary, or reusable page cannot be retrieved. [crates/gcode/src/commands/codewiki/reuse.rs:49-57]
- `ReusePlan.reusable` (method) component `ReusePlan.reusable [method]` (`ef01acbe-dd9e-560c-b4b6-ff06c49ab56f`) lines 59-91 [crates/gcode/src/commands/codewiki/reuse.rs:59-91]
  - Signature: `fn reusable(&mut self, doc_path: &str, sources: &BTreeSet<String>) -> bool {`
  - Purpose: Returns `true` only if the cached doc entry exists, is not degraded, was generated under the current `ai_mode`, has a non-empty source-hash snapshot whose file set exactly matches `sources`, every recorded source file still hashes to the stored value, and the output document still exists on disk. [crates/gcode/src/commands/codewiki/reuse.rs:59-91]
- `ReusePlan.current_hash` (method) component `ReusePlan.current_hash [method]` (`4d7e3036-508e-5281-bd5a-1c49a210d308`) lines 93-100 [crates/gcode/src/commands/codewiki/reuse.rs:93-100]
  - Signature: `fn current_hash(&mut self, file: &str) -> Option<String> {`
  - Purpose: Returns the cached content hash for `file` if available, otherwise computes `hasher::file_content_hash` for `project_root/file`, stores the resulting `Option<String>` in `current_hashes`, and returns it. [crates/gcode/src/commands/codewiki/reuse.rs:93-100]
- `span_files` (function) component `span_files [function]` (`c68e20a4-c96a-58c0-9831-4973554fd9a8`) lines 105-107 [crates/gcode/src/commands/codewiki/reuse.rs:105-107]
  - Signature: `pub(crate) fn span_files(spans: &[SourceSpan]) -> BTreeSet<String> {`
  - Purpose: Returns a `BTreeSet<String>` containing the distinct `file` values cloned from every `SourceSpan` in the input slice. [crates/gcode/src/commands/codewiki/reuse.rs:105-107]

