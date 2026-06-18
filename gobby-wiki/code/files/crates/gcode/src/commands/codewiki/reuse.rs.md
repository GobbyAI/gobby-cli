---
title: crates/gcode/src/commands/codewiki/reuse.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/reuse.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/reuse.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The primary orchestrator is the ReusePlan struct crates/gcode/src/commands/codewiki/reuse.rs:11-19, which tracks the project root, output directory, active AI mode, and documentation metadata. It lazily computes and caches hashes of source files to determine reuse feasibility, permanently marking missing or unhashable sources as non-reusable to avoid repeated disk probing.

## How it fits

This file bridges the gap between stored documentation outputs on disk and the current state of the workspace. During initialization, ReusePlan::load crates/gcode/src/commands/codewiki/reuse.rs:22-31 constructs the planning state by reading existing codewiki metadata and copying relevant path configurations.

To resolve cache hits, ReusePlan::reusable_page crates/gcode/src/commands/codewiki/reuse.rs:36-46 fetches the existing on-disk content of a page when its sources match. This is extended by ReusePlan::reusable_page_with_summary crates/gcode/src/commands/codewiki/reuse.rs:49-57, which bundles the cached page text together with its recorded summary.
[crates/gcode/src/commands/codewiki/reuse.rs:11-19]
[crates/gcode/src/commands/codewiki/reuse.rs:22-31]
[crates/gcode/src/commands/codewiki/reuse.rs:36-46]
[crates/gcode/src/commands/codewiki/reuse.rs:49-57]
[crates/gcode/src/commands/codewiki/reuse.rs:59-88]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ReusePlan` | class | 'ReusePlan' is a crate-private plan object that tracks a project root, output directory, AI mode, documentation metadata, and lazily computed current-content hashes to decide whether files can be safely reused, with unhashable sources permanently marked as non-reusable. [crates/gcode/src/commands/codewiki/reuse.rs:11-19] |
| `ReusePlan::load` | method | Constructs and returns a 'Self' by reading existing codewiki metadata from 'out_dir', copying 'project_root' and 'out_dir' into owned paths, storing 'ai_mode' as a 'String', reusing 'previous.docs', and initializing 'current_hashes' as an empty 'BTreeMap'. [crates/gcode/src/commands/codewiki/reuse.rs:22-31] |
| `ReusePlan::reusable_page` | method | Returns the existing rendered document as 'String' from the safe output-path corresponding to 'doc_path' only when 'self.reusable(doc_path, sources)' is true, otherwise 'None', propagating any path-safety or file-read failure as 'None'. [crates/gcode/src/commands/codewiki/reuse.rs:36-46] |
| `ReusePlan::reusable_page_with_summary` | method | Returns 'Some((page, summary))' by cloning the cached summary for 'doc_path' from 'self.docs', constructing a reusable page via 'self.reusable_page(doc_path, sources)', and yielding 'None' if either the document or summary is missing or the page cannot be reused. [crates/gcode/src/commands/codewiki/reuse.rs:49-57] |
| `ReusePlan::reusable_pages_with_prefixes` | method | Collects all 'docs' entries whose paths start with any of the supplied prefixes, rebuilds each via 'reusable_page' using its source-hash keys and cloned summary, returns the resulting 'BuiltDoc' list sorted by path, or 'None' if no paths match. [crates/gcode/src/commands/codewiki/reuse.rs:59-88] |
| `ReusePlan::reusable` | method | Returns 'true' only when the document exists in 'self.docs' and is not degraded, the AI mode and render version match, the stored source-hash set is nonempty and exactly matches 'sources', every tracked source file currently hashes to the stored value, and the rendered output path resolves safely and still exists on disk. [crates/gcode/src/commands/codewiki/reuse.rs:90-126] |
| `ReusePlan::current_hash` | method | Returns the cached content hash for 'file' if present, otherwise computes it from 'project_root/file', stores the resulting 'Option<String>' in 'current_hashes', and returns it. [crates/gcode/src/commands/codewiki/reuse.rs:128-135] |
| `span_files` | function | Returns a 'BTreeSet<String>' containing the distinct 'file' values cloned from each 'SourceSpan' in 'spans'. [crates/gcode/src/commands/codewiki/reuse.rs:140-142] |

