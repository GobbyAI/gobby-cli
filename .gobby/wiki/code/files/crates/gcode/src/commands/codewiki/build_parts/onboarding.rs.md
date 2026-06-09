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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/onboarding.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

`crates/gcode/src/commands/codewiki/build_parts/onboarding.rs` exposes 6 indexed API symbols.
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-200]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-208] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:210-212] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:214-219]

## API Symbols

- `build_onboarding_doc` (function) component `build_onboarding_doc [function]` (`c2998ded-02bc-515a-a973-f9628d853a16`) lines 7-52 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
  - Signature: `pub(crate) fn build_onboarding_doc(`
  - Purpose: Constructs an `OnboardingDoc` by extracting entry points and computing a ranked reading order of modules based on code graph availability (with graceful fallback for unavailable/truncated states), while collecting source spans and tracking degraded data sources. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
- `onboarding_entry_points` (function) component `onboarding_entry_points [function]` (`512b74da-d547-5cf0-85b9-f47e18a6abf8`) lines 54-109 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
  - Signature: `fn onboarding_entry_points(files: &[FileDoc]) -> Vec<OnboardingEntryPoint> {`
  - Purpose: Collects and deduplicates onboarding entry points from Rust entry files and their public API symbols, returning a vector of entries containing file/symbol links, descriptions, and source span locations. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
- `ranked_onboarding_steps` (function) component `ranked_onboarding_steps [function]` (`4f8ee865-ff5d-5abc-83e5-4cb632aa0108`) lines 111-200 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-200]
  - Signature: `fn ranked_onboarding_steps(`
  - Purpose: # Summary

`ranked_onboarding_steps` generates ranked onboarding steps by computing graph centrality metrics on a module dependency network extracted from code symbols and imports to prioritize modules by their architectural importance. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-200]
- `step_source_spans` (function) component `step_source_spans [function]` (`35d266e1-588c-5922-be7b-59c73aac0fe6`) lines 202-208 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-208]
  - Signature: `fn step_source_spans(module: &str, modules: &[ModuleDoc]) -> Vec<SourceSpan> {`
  - Purpose: Searches a ModuleDoc slice for a matching module by name and returns its cloned source spans, or an empty vector if not found. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-208]
- `is_rust_entry_file` (function) component `is_rust_entry_file [function]` (`d18447d0-e856-5eee-8b40-6724ee638f03`) lines 210-212 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:210-212]
  - Signature: `fn is_rust_entry_file(file: &str) -> bool {`
  - Purpose: Returns `true` if the file path is or ends with a Rust entry point file (`main.rs` or `lib.rs`), regardless of directory depth. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:210-212]
- `is_public_api_symbol` (function) component `is_public_api_symbol [function]` (`84030109-023b-567c-ba3d-5f7793a04cd6`) lines 214-219 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:214-219]
  - Signature: `fn is_public_api_symbol(symbol: &Symbol) -> bool {`
  - Purpose: Determines whether a symbol is part of the public API by checking if its signature begins with `pub ` after trimming leading whitespace. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:214-219]

