---
title: crates/gcode/src/commands/codewiki/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/generation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/generation.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The `crates/gcode/src/commands/codewiki/generation.rs` file acts as the primary orchestrator for generating hierarchical, high-level, and detail-level documentation for a codebase. It defines a set of API entry points that transform codebase structural inputs into polished wiki-style documentation.

## How it fits

This file resides within the `codewiki` command module. It imports critical structures and helper builders (crates/gcode/src/commands/codewiki/generation.rs:6-14) such as `CodewikiInput`, `BuiltDoc`, `TextGenerator`, and module clusterers. It coordinates these components to pipeline raw workspace data into rendered documentation files.

The highest-level public interface is `generate_hierarchical_docs` (crates/gcode/src/commands/codewiki/generation.rs:16-24), which takes a `CodewikiInput` and returns a flat collection of path-to-content string tuples. It does this by driving `generate_hierarchical_docs_with_graph_availability` (crates/gcode/src/commands/codewiki/generation.rs:26-51) and mapping the resulting `BuiltDoc` objects.
[crates/gcode/src/commands/codewiki/generation.rs:16-24]
[crates/gcode/src/commands/codewiki/generation.rs:26-51]
[crates/gcode/src/commands/codewiki/generation.rs:54-76]
[crates/gcode/src/commands/codewiki/generation.rs:79-86]
[crates/gcode/src/commands/codewiki/generation.rs:90-117]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `generate_hierarchical_docs` | function | Calls 'generate_hierarchical_docs_with_graph_availability' with the provided input and optional generator, then converts each returned document into a '(path, content)' tuple and collects them into a 'Vec'. [crates/gcode/src/commands/codewiki/generation.rs:16-24] |
| `generate_hierarchical_docs_with_graph_availability` | function | Attempts to generate hierarchical docs at symbol depth without ownership metadata using a silent progress tracker and unscoped pruning, collecting emitted 'BuiltDoc's into a vector and returning an empty vector on core-generation error after logging a warning. [crates/gcode/src/commands/codewiki/generation.rs:26-51] |
| `generate_hierarchical_docs_with_ownership` | function | A thin wrapper that forwards all parameters to 'generate_hierarchical_docs_core', propagating optional ownership metadata, generator/verifier handles, reuse planning, progress tracking, pruning scope, and emitted 'BuiltDoc' results. [crates/gcode/src/commands/codewiki/generation.rs:54-76] |
| `generate_hierarchical_docs_with_progress` | function | Delegates hierarchical documentation generation to 'generate_hierarchical_docs_with_reuse' with no reuse cache ('None'), passing through the input, optional text generator, AI depth, and mutable progress tracker, and returns the resulting 'Vec<BuiltDoc>'. [crates/gcode/src/commands/codewiki/generation.rs:79-86] |
| `generate_hierarchical_docs_with_reuse` | function | Runs 'generate_hierarchical_docs_core' with an unscoped pruning scope and no ownership metadata, collecting emitted 'BuiltDoc's into a vector, logging a warning and returning an empty vector if generation fails. [crates/gcode/src/commands/codewiki/generation.rs:90-117] |
| `generate_hierarchical_docs_with_verify` | function | 'generate_hierarchical_docs_with_verify' invokes 'generate_hierarchical_docs_core' with silent progress and an unscoped prune scope to build a 'Vec<BuiltDoc>' from a 'CodewikiInput', optionally using provided generator/verifier handles, and returns an empty vector after logging a warning if core generation fails. [crates/gcode/src/commands/codewiki/generation.rs:123-152] |
| `generate_hierarchical_docs_core` | function | Generates hierarchical documentation for the core files in the requested scope by collecting and sorting scoped symbols, clustering file modules from the file graph, emitting progress, and building/emitting 'BuiltDoc' records using the provided generator, verifier, reuse plan, and ownership metadata. [crates/gcode/src/commands/codewiki/generation.rs:158-359] |

