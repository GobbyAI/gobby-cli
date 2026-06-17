---
title: crates/gcode/src/commands/codewiki/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/generation.rs
  ranges:
  - 16-24
  - 26-50
  - 53-73
  - 76-83
  - 87-113
  - 119-310
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/generation.rs:16-24](crates/gcode/src/commands/codewiki/generation.rs#L16-L24), [crates/gcode/src/commands/codewiki/generation.rs:26-50](crates/gcode/src/commands/codewiki/generation.rs#L26-L50), [crates/gcode/src/commands/codewiki/generation.rs:53-73](crates/gcode/src/commands/codewiki/generation.rs#L53-L73), [crates/gcode/src/commands/codewiki/generation.rs:76-83](crates/gcode/src/commands/codewiki/generation.rs#L76-L83), [crates/gcode/src/commands/codewiki/generation.rs:87-113](crates/gcode/src/commands/codewiki/generation.rs#L87-L113), [crates/gcode/src/commands/codewiki/generation.rs:119-310](crates/gcode/src/commands/codewiki/generation.rs#L119-L310)

</details>

# crates/gcode/src/commands/codewiki/generation.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Builds hierarchical codewiki documentation for an input repository by routing through a shared core generator and a few convenience wrappers. The public entry point returns path/content pairs, while the other functions adapt the core to different capabilities and contexts: silent graph-availability fallback, ownership-aware generation, test-progress reporting, and reuse planning.
[crates/gcode/src/commands/codewiki/generation.rs:16-24]
[crates/gcode/src/commands/codewiki/generation.rs:26-50]
[crates/gcode/src/commands/codewiki/generation.rs:53-73]
[crates/gcode/src/commands/codewiki/generation.rs:76-83]
[crates/gcode/src/commands/codewiki/generation.rs:87-113]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `generate_hierarchical_docs` | function | `pub fn generate_hierarchical_docs(` | `generate_hierarchical_docs [function]` | `28fea489-ff19-5da4-ae53-d46a8ae3cd2b` | 16-24 [crates/gcode/src/commands/codewiki/generation.rs:16-24] | Indexed function `generate_hierarchical_docs` in `crates/gcode/src/commands/codewiki/generation.rs`. [crates/gcode/src/commands/codewiki/generation.rs:16-24] |
| `generate_hierarchical_docs_with_graph_availability` | function | `fn generate_hierarchical_docs_with_graph_availability(` | `generate_hierarchical_docs_with_graph_availability [function]` | `7e4b0e75-8d4e-51aa-b4bd-91ffe5188703` | 26-50 [crates/gcode/src/commands/codewiki/generation.rs:26-50] | Indexed function `generate_hierarchical_docs_with_graph_availability` in `crates/gcode/src/commands/codewiki/generation.rs`. [crates/gcode/src/commands/codewiki/generation.rs:26-50] |
| `generate_hierarchical_docs_with_ownership` | function | `pub(crate) fn generate_hierarchical_docs_with_ownership(` | `generate_hierarchical_docs_with_ownership [function]` | `40c7cbbf-e86d-52ee-9724-583d90796dc6` | 53-73 [crates/gcode/src/commands/codewiki/generation.rs:53-73] | Indexed function `generate_hierarchical_docs_with_ownership` in `crates/gcode/src/commands/codewiki/generation.rs`. [crates/gcode/src/commands/codewiki/generation.rs:53-73] |
| `generate_hierarchical_docs_with_progress` | function | `pub(crate) fn generate_hierarchical_docs_with_progress(` | `generate_hierarchical_docs_with_progress [function]` | `168dbec4-23dc-54a2-a6d3-87bfdf93918c` | 76-83 [crates/gcode/src/commands/codewiki/generation.rs:76-83] | Indexed function `generate_hierarchical_docs_with_progress` in `crates/gcode/src/commands/codewiki/generation.rs`. [crates/gcode/src/commands/codewiki/generation.rs:76-83] |
| `generate_hierarchical_docs_with_reuse` | function | `pub(crate) fn generate_hierarchical_docs_with_reuse(` | `generate_hierarchical_docs_with_reuse [function]` | `350f0ef4-947c-572c-8527-e40dc37ef079` | 87-113 [crates/gcode/src/commands/codewiki/generation.rs:87-113] | Indexed function `generate_hierarchical_docs_with_reuse` in `crates/gcode/src/commands/codewiki/generation.rs`. [crates/gcode/src/commands/codewiki/generation.rs:87-113] |
| `generate_hierarchical_docs_core` | function | `pub(crate) fn generate_hierarchical_docs_core(` | `generate_hierarchical_docs_core [function]` | `eb460700-cc4e-5720-b3ad-91734571c7f9` | 119-310 [crates/gcode/src/commands/codewiki/generation.rs:119-310] | Indexed function `generate_hierarchical_docs_core` in `crates/gcode/src/commands/codewiki/generation.rs`. [crates/gcode/src/commands/codewiki/generation.rs:119-310] |
