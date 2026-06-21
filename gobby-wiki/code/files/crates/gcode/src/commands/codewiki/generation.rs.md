---
title: crates/gcode/src/commands/codewiki/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/generation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/generation.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/generation.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/generation.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `generate_hierarchical_docs` | function | The 'generate_hierarchical_docs' function generates hierarchical documentation from a 'CodewikiInput' and an optional 'TextGenerator' by calling 'generate_hierarchical_docs_with_graph_availability' and mapping the resulting documents into a vector of path-content string pairs. [crates/gcode/src/commands/codewiki/generation.rs:20-28] |
| `generate_hierarchical_docs_with_graph_availability` | function | This function generates a vector of symbol-level hierarchical documents from a 'CodewikiInput' and an optional 'TextGenerator' by invoking 'generate_hierarchical_docs_core' with silent progress tracking and an unscoped pruning scope, returning an empty vector if the core generation fails. [crates/gcode/src/commands/codewiki/generation.rs:30-58] |
| `generate_hierarchical_docs_with_ownership` | function | This crate-visible function generates hierarchical documentation by forwarding input parameters, optional ownership metadata, system and feature models, AI text generation and verification handlers, progress tracking state, and an emission callback to 'generate_hierarchical_docs_core'. [crates/gcode/src/commands/codewiki/generation.rs:61-89] |
| `repo_audit_links` | function | 'repo_audit_links' conditionally constructs and returns a vector of static string label-path tuples based on three boolean flags indicating the presence of audit, feature catalog, and infrastructure components. [crates/gcode/src/commands/codewiki/generation.rs:177-194] |
| `generate_hierarchical_docs_core` | function | # Summary Generates and emits hierarchical documentation for scope-filtered core code files and symbols, optionally augmented with deterministic system models, feature catalogs, and audit contexts via callback emission. [crates/gcode/src/commands/codewiki/generation.rs:200-528] |

_Verified by 3 in-file unit tests._

