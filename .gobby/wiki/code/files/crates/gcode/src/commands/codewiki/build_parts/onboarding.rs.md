---
title: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
  ranges:
  - 7-52
  - 54-109
  - 111-200
  - 202-208
  - 210-212
  - 214-219
  - 225-246
  - 249-255
  - 258-268
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/onboarding.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

`crates/gcode/src/commands/codewiki/build_parts/onboarding.rs` exposes 9 indexed API symbols.
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-200]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-208]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:210-212]

## API Symbols

- `build_onboarding_doc` (function) component `build_onboarding_doc [function]` (`c2998ded-02bc-515a-a973-f9628d853a16`) lines 7-52 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
  - Signature: `pub(crate) fn build_onboarding_doc(`
  - Purpose: Constructs an OnboardingDoc by extracting entry points and computing a ranked reading order from code files and modules, gracefully degrading to empty or fallback steps when graph analytics are unavailable or truncated. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
- `onboarding_entry_points` (function) component `onboarding_entry_points [function]` (`512b74da-d547-5cf0-85b9-f47e18a6abf8`) lines 54-109 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
  - Signature: `fn onboarding_entry_points(files: &[FileDoc]) -> Vec<OnboardingEntryPoint> {`
  - Purpose: Extracts and deduplicates onboarding entry points from Rust entry files (main.rs and library files) and public API symbols, annotating each with source spans, descriptions, and wikilinks. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
- `ranked_onboarding_steps` (function) component `ranked_onboarding_steps [function]` (`4f8ee865-ff5d-5abc-83e5-4cb632aa0108`) lines 111-200 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-200]
  - Signature: `fn ranked_onboarding_steps(`
  - Purpose: Generates an ordered onboarding sequence by constructing a module dependency graph and ranking modules by their centrality scores computed via graph analytics. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-200]
- `step_source_spans` (function) component `step_source_spans [function]` (`35d266e1-588c-5922-be7b-59c73aac0fe6`) lines 202-208 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-208]
  - Signature: `fn step_source_spans(module: &str, modules: &[ModuleDoc]) -> Vec<SourceSpan> {`
  - Purpose: Returns the cloned source spans for a module identified by name from a ModuleDoc slice, or an empty vector if no matching module exists. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-208]
- `is_rust_entry_file` (function) component `is_rust_entry_file [function]` (`d18447d0-e856-5eee-8b40-6724ee638f03`) lines 210-212 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:210-212]
  - Signature: `fn is_rust_entry_file(file: &str) -> bool {`
  - Purpose: Returns `true` if the file path is or ends with a Rust crate entry point (`main.rs` or `lib.rs`). [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:210-212]
- `is_public_api_symbol` (function) component `is_public_api_symbol [function]` (`84030109-023b-567c-ba3d-5f7793a04cd6`) lines 214-219 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:214-219]
  - Signature: `fn is_public_api_symbol(symbol: &Symbol) -> bool {`
  - Purpose: Determines whether a symbol is a public API member by checking if its signature, after trimming leading whitespace, is exactly "pub" or begins with "pub ". [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:214-219]
- `symbol_with_signature` (function) component `symbol_with_signature [function]` (`c329e461-dea4-5cd0-8053-478bd08fe594`) lines 225-246 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:225-246]
  - Signature: `fn symbol_with_signature(signature: &str) -> Symbol {`
  - Purpose: Creates a Symbol struct with hardcoded metadata fields (id, project, file path, etc.) and the provided signature string as the sole variable parameter. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:225-246]
- `public_api_symbol_accepts_plain_public_visibility` (function) component `public_api_symbol_accepts_plain_public_visibility [function]` (`05c77be0-fc54-5ebc-8aea-e4920a40c314`) lines 249-255 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:249-255]
  - Signature: `fn public_api_symbol_accepts_plain_public_visibility() {`
  - Purpose: Unit test verifying that `is_public_api_symbol()` correctly identifies items with plain `pub` visibility as public API symbols. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:249-255]
- `public_api_symbol_rejects_restricted_visibility` (function) component `public_api_symbol_rejects_restricted_visibility [function]` (`0e815d94-2c0b-56d5-b834-0d9d89a09442`) lines 258-268 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:258-268]
  - Signature: `fn public_api_symbol_rejects_restricted_visibility() {`
  - Purpose: This test verifies that the `is_public_api_symbol()` function returns false for symbols with restricted visibility modifiers (`pub(crate)`, `pub(super)`, and `pub(in path)`). [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:258-268]

