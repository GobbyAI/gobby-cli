---
title: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/onboarding.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/onboarding.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/onboarding.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_onboarding_doc` | function | Constructs an 'OnboardingDoc' by deriving entry points from 'files', computing a graph-ranked 'reading_order' only when graph data is 'Truncated' or 'Available', collecting the unique source spans referenced by both, and returning an undegraded document with empty 'degraded_sources'. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-43] |
| `onboarding_entry_points` | function | Builds a de-duplicated list of onboarding entry points by collecting Rust entry files ('main.rs' or library entry files) with their first available source span, then appending unique public API symbols with formatted descriptions and returning the accumulated 'OnboardingEntryPoint' vector. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:45-100] |
| `ranked_onboarding_steps` | function | The 'ranked_onboarding_steps' function generates a prioritized list of onboarding steps by mapping files and symbols to modules, constructing a module dependency graph, and executing topological and centrality graph analytics on the resulting network. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:102-192] |
| `step_source_spans` | function | Returns a cloned 'Vec<SourceSpan>' for the first 'ModuleDoc' whose 'module' field matches 'module', or an empty vector if no match is found. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:194-200] |
| `is_rust_entry_file` | function | Returns 'true' if 'file' is exactly 'main.rs' or 'lib.rs', or if its path ends with '/main.rs' or '/lib.rs', and 'false' otherwise. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-204] |
| `is_public_api_symbol` | function | Returns 'true' if the symbol’s signature, after leading whitespace is trimmed, is exactly 'pub' or begins with 'pub ', indicating a public API symbol. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:206-211] |
| `symbol_with_signature` | function | Constructs and returns a 'Symbol' for a Rust function named 'run' in 'crate::run', filling fixed metadata fields and setting 'signature' to 'Some(signature.to_string())' while leaving documentation, parent, summary, timestamps, and 'content_hash' empty or 'None'. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:217-238] |

_Verified by 2 in-file unit tests._

