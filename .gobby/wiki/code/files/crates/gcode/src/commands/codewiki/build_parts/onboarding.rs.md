---
title: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
  ranges:
  - 7-52
  - 54-109
  - 111-201
  - 203-209
  - 211-213
  - 215-220
  - 226-247
  - 250-256
  - 259-269
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/onboarding.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds the onboarding section of a codewiki document by combining entry-point discovery with an ordered reading path through the project. It collects Rust entry files and public API symbols as onboarding entry points, then computes a ranked module reading order from dependency graph data, falling back gracefully when graph analytics are unavailable or truncated. Helper routines support this by identifying Rust entry files, filtering public API symbols, looking up module source spans, and the tests verify the public-API detection rules.
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-201]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213]

## API Symbols

- `build_onboarding_doc` (function) component `build_onboarding_doc [function]` (`c2998ded-02bc-515a-a973-f9628d853a16`) lines 7-52 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
  - Signature: `pub(crate) fn build_onboarding_doc(`
  - Purpose: Constructs an OnboardingDoc by extracting entry points and computing a ranked reading order from code files and modules, gracefully degrading to empty or fallback steps when graph analytics are unavailable or truncated. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
- `onboarding_entry_points` (function) component `onboarding_entry_points [function]` (`512b74da-d547-5cf0-85b9-f47e18a6abf8`) lines 54-109 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
  - Signature: `fn onboarding_entry_points(files: &[FileDoc]) -> Vec<OnboardingEntryPoint> {`
  - Purpose: Extracts and deduplicates onboarding entry points from Rust entry files (main.rs and library files) and public API symbols, annotating each with source spans, descriptions, and wikilinks. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
- `ranked_onboarding_steps` (function) component `ranked_onboarding_steps [function]` (`4f8ee865-ff5d-5abc-83e5-4cb632aa0108`) lines 111-201 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-201]
  - Signature: `fn ranked_onboarding_steps(`
  - Purpose: Builds a ranked list of onboarding steps for non-empty modules by deriving module dependency edges from file symbols, analyzing the resulting import graph for topology and centrality, and using those metrics plus module summaries to order the steps. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-201]
- `step_source_spans` (function) component `step_source_spans [function]` (`37f458fa-507d-5795-8688-a9b9c8ee27ad`) lines 203-209 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209]
  - Signature: `fn step_source_spans(module: &str, modules: &[ModuleDoc]) -> Vec<SourceSpan> {`
  - Purpose: Returns the cloned 'source_spans' for the first 'ModuleDoc' whose 'module' matches the input string, or an empty 'Vec<SourceSpan>' if no match is found. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209]
- `is_rust_entry_file` (function) component `is_rust_entry_file [function]` (`76cd4247-f50b-54dc-8728-c1af6e567f71`) lines 211-213 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213]
  - Signature: `fn is_rust_entry_file(file: &str) -> bool {`
  - Purpose: Returns 'true' if the path is exactly 'main.rs' or 'lib.rs', or if it ends with '/main.rs' or '/lib.rs', identifying Rust entry-point source files. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213]
- `is_public_api_symbol` (function) component `is_public_api_symbol [function]` (`283593cc-043a-536d-9125-e7561752335b`) lines 215-220 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:215-220]
  - Signature: `fn is_public_api_symbol(symbol: &Symbol) -> bool {`
  - Purpose: Returns 'true' when the symbol’s signature, after leading whitespace is trimmed, begins with 'pub' as a standalone keyword or 'pub ', indicating it is a public API symbol. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:215-220]
- `symbol_with_signature` (function) component `symbol_with_signature [function]` (`144ef92a-220f-5fda-9231-ff7ec414a43a`) lines 226-247 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:226-247]
  - Signature: `fn symbol_with_signature(signature: &str) -> Symbol {`
  - Purpose: Constructs and returns a 'Symbol' for the Rust function 'crate::run' with fixed metadata, zeroed source spans, and the provided 'signature' stored as 'Some(signature.to_string())'. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:226-247]
- `public_api_symbol_accepts_plain_public_visibility` (function) component `public_api_symbol_accepts_plain_public_visibility [function]` (`01b794a3-d6cf-5d0f-a631-c7bea199c9de`) lines 250-256 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:250-256]
  - Signature: `fn public_api_symbol_accepts_plain_public_visibility() {`
  - Purpose: Verifies that 'is_public_api_symbol' classifies bare 'pub' visibility and public item declarations like 'pub fn' and 'pub struct' as public API symbols. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:250-256]
- `public_api_symbol_rejects_restricted_visibility` (function) component `public_api_symbol_rejects_restricted_visibility [function]` (`b7a92ce8-6196-5ff7-9295-e6d6aa7c170b`) lines 259-269 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:259-269]
  - Signature: `fn public_api_symbol_rejects_restricted_visibility() {`
  - Purpose: Verifies that 'is_public_api_symbol' returns 'false' for symbols with restricted visibility such as 'pub(crate)', 'pub(super)', and 'pub(in ...)'. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:259-269]

