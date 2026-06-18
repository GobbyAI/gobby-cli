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

`crates/gcode/src/commands/codewiki/build_parts/onboarding.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_onboarding_doc` | function | Constructs an 'OnboardingDoc' by deriving entry points from 'files', choosing a reading order from graph-ranked onboarding steps when graph analytics are available or truncated, tracking degraded graph sources and fallback state, and collecting the deduplicated source spans referenced by entry points and reading-order modules. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52] |
| `onboarding_entry_points` | function | Builds a deduplicated list of onboarding entry points by adding Rust entry files with a file-level span and description, then appending public API symbols with their signature-based descriptions and symbol spans. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109] |
| `ranked_onboarding_steps` | function | 'ranked_onboarding_steps' builds a module-level import graph from files and graph edges, computes dependency topology and graph analytics centrality for modules with direct files, and returns a ranked list of onboarding steps derived from those module summaries and scores. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-201] |
| `step_source_spans` | function | Returns the cloned 'source_spans' vector for the first 'ModuleDoc' whose 'module' field matches 'module', or an empty 'Vec<SourceSpan>' if no match is found. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209] |
| `is_rust_entry_file` | function | Returns 'true' when 'file' is exactly 'main.rs' or 'lib.rs', or when its path ends with '/main.rs' or '/lib.rs', and 'false' otherwise. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213] |
| `is_public_api_symbol` | function | Returns 'true' when the symbol’s signature, after leading-whitespace trimming, is exactly 'pub' or begins with 'pub ', indicating a public API symbol. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:215-220] |
| `symbol_with_signature` | function | Constructs and returns a 'Symbol' for a Rust function named 'run' in 'crate::run', with fixed metadata and the provided 'signature' stored as 'Some(signature.to_string())'. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:226-247] |
| `public_api_symbol_accepts_plain_public_visibility` | function | Verifies that 'is_public_api_symbol' returns 'true' for symbols declared with plain 'pub' visibility, including a 'pub' item with no signature, a 'pub fn', and a 'pub struct'. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:250-256] |
| `public_api_symbol_rejects_restricted_visibility` | function | Verifies that 'is_public_api_symbol' returns 'false' for symbols with restricted visibility modifiers such as 'pub(crate)', 'pub(super)', and 'pub(in crate::internal)'. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:259-269] |

