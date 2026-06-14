---
title: crates/gcode/src/commands/codewiki/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/generation.rs
  ranges:
  - 15-23
  - 25-49
  - 52-72
  - 75-82
  - 86-112
  - 118-306
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/generation.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This module provides the orchestration layer for hierarchical codewiki document generation. The top-level `generate_hierarchical_docs` converts generated `BuiltDoc` values into `(path, content)` pairs, while the wrapper helpers choose different execution modes: with no graph/ownership data, with ownership metadata, with progress tracking, or with reuse collection. All of them delegate to `generate_hierarchical_docs_core`, which performs the real work by filtering scoped core files and symbols, grouping and sorting them by file, clustering modules, reporting progress, and incrementally building and emitting the final hierarchical docs.
[crates/gcode/src/commands/codewiki/generation.rs:15-23]
[crates/gcode/src/commands/codewiki/generation.rs:25-49]
[crates/gcode/src/commands/codewiki/generation.rs:52-72]
[crates/gcode/src/commands/codewiki/generation.rs:75-82]
[crates/gcode/src/commands/codewiki/generation.rs:86-112]

## API Symbols

- `generate_hierarchical_docs` (function) component `generate_hierarchical_docs [function]` (`ad42f43e-49cb-540f-9c7d-75471c9538ac`) lines 15-23 [crates/gcode/src/commands/codewiki/generation.rs:15-23]
  - Signature: `pub fn generate_hierarchical_docs(`
  - Purpose: Transforms the result of 'generate_hierarchical_docs_with_graph_availability(input, generate)' into a 'Vec<(String, String)>' by mapping each document’s 'path' and 'content' into a tuple. [crates/gcode/src/commands/codewiki/generation.rs:15-23]
- `generate_hierarchical_docs_with_graph_availability` (function) component `generate_hierarchical_docs_with_graph_availability [function]` (`d463d412-2e38-5e08-888f-43bc4b543642`) lines 25-49 [crates/gcode/src/commands/codewiki/generation.rs:25-49]
  - Signature: `fn generate_hierarchical_docs_with_graph_availability(`
  - Purpose: Generates hierarchical codewiki documents at 'AiDepth::Symbols' without ownership metadata using a silent progress tracker and unscoped pruning, returning the accumulated 'BuiltDoc' list or an empty vector if core generation fails. [crates/gcode/src/commands/codewiki/generation.rs:25-49]
- `generate_hierarchical_docs_with_ownership` (function) component `generate_hierarchical_docs_with_ownership [function]` (`3c1831e8-14fe-5c31-8302-cd69d89333f9`) lines 52-72 [crates/gcode/src/commands/codewiki/generation.rs:52-72]
  - Signature: `pub(crate) fn generate_hierarchical_docs_with_ownership(`
  - Purpose: Delegates to 'generate_hierarchical_docs_core' to produce hierarchical documentation for a 'CodewikiInput', carrying optional ownership metadata, generator, reuse plan, progress tracking, prune scope, and an output callback, and returns any resulting error. [crates/gcode/src/commands/codewiki/generation.rs:52-72]
- `generate_hierarchical_docs_with_progress` (function) component `generate_hierarchical_docs_with_progress [function]` (`b229958b-946d-59db-bb55-da33469129a4`) lines 75-82 [crates/gcode/src/commands/codewiki/generation.rs:75-82]
  - Signature: `pub(crate) fn generate_hierarchical_docs_with_progress(`
  - Purpose: Wraps 'generate_hierarchical_docs_with_reuse', forwarding the input, optional text generator, AI depth, and progress tracker while always passing no reuse context, and returns the resulting 'Vec<BuiltDoc>'. [crates/gcode/src/commands/codewiki/generation.rs:75-82]
- `generate_hierarchical_docs_with_reuse` (function) component `generate_hierarchical_docs_with_reuse [function]` (`ccc5e752-9c46-5262-a364-856d5de7feee`) lines 86-112 [crates/gcode/src/commands/codewiki/generation.rs:86-112]
  - Signature: `pub(crate) fn generate_hierarchical_docs_with_reuse(`
  - Purpose: Runs 'generate_hierarchical_docs_core' with an unscoped 'DocPruneScope', collecting each emitted 'BuiltDoc' into a vector and returning it, or logging a warning and returning an empty vector if generation fails without ownership metadata. [crates/gcode/src/commands/codewiki/generation.rs:86-112]
- `generate_hierarchical_docs_core` (function) component `generate_hierarchical_docs_core [function]` (`08c84254-a46d-5eac-ad20-4d07c94a686f`) lines 118-306 [crates/gcode/src/commands/codewiki/generation.rs:118-306]
  - Signature: `pub(crate) fn generate_hierarchical_docs_core(`
  - Purpose: Filters the input to scoped core files and symbols, groups and sorts symbols by file, clusters file modules, reports progress, and incrementally builds and emits hierarchical file documentation using the provided generator, reuse plan, ownership metadata, and AI depth settings. [crates/gcode/src/commands/codewiki/generation.rs:118-306]

