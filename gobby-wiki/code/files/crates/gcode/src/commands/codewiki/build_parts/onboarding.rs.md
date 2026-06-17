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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L7-L52), [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L54-L109), [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-201](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L111-L201), [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L203-L209), [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L211-L213), [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:215-220](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L215-L220), [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:226-247](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L226-L247), [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:250-256](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L250-L256), [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:259-269](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs#L259-L269)

</details>

# crates/gcode/src/commands/codewiki/build_parts/onboarding.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds the onboarding section of a codewiki document by combining Rust entry files with a ranked reading order for modules, then collecting the source spans that should be surfaced in the final `OnboardingDoc`. It chooses the reading order from graph analytics when available, falls back or degrades when graph data is truncated or unavailable, and deduplicates spans from entry points and referenced modules. The helper functions identify Rust entry files, filter public API symbols, and format symbol names with signatures so onboarding steps can point to the most relevant public-facing code.
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-201]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_onboarding_doc` | function | `pub(crate) fn build_onboarding_doc(` | `build_onboarding_doc [function]` | `c2998ded-02bc-515a-a973-f9628d853a16` | 7-52 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52] | Indexed function `build_onboarding_doc` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52] |
| `onboarding_entry_points` | function | `fn onboarding_entry_points(files: &[FileDoc]) -> Vec<OnboardingEntryPoint> {` | `onboarding_entry_points [function]` | `512b74da-d547-5cf0-85b9-f47e18a6abf8` | 54-109 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109] | Indexed function `onboarding_entry_points` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109] |
| `ranked_onboarding_steps` | function | `fn ranked_onboarding_steps(` | `ranked_onboarding_steps [function]` | `4f8ee865-ff5d-5abc-83e5-4cb632aa0108` | 111-201 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-201] | Indexed function `ranked_onboarding_steps` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-201] |
| `step_source_spans` | function | `fn step_source_spans(module: &str, modules: &[ModuleDoc]) -> Vec<SourceSpan> {` | `step_source_spans [function]` | `37f458fa-507d-5795-8688-a9b9c8ee27ad` | 203-209 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209] | Indexed function `step_source_spans` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209] |
| `is_rust_entry_file` | function | `fn is_rust_entry_file(file: &str) -> bool {` | `is_rust_entry_file [function]` | `76cd4247-f50b-54dc-8728-c1af6e567f71` | 211-213 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213] | Indexed function `is_rust_entry_file` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213] |
| `is_public_api_symbol` | function | `fn is_public_api_symbol(symbol: &Symbol) -> bool {` | `is_public_api_symbol [function]` | `283593cc-043a-536d-9125-e7561752335b` | 215-220 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:215-220] | Indexed function `is_public_api_symbol` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:215-220] |
| `symbol_with_signature` | function | `fn symbol_with_signature(signature: &str) -> Symbol {` | `symbol_with_signature [function]` | `144ef92a-220f-5fda-9231-ff7ec414a43a` | 226-247 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:226-247] | Indexed function `symbol_with_signature` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:226-247] |
| `public_api_symbol_accepts_plain_public_visibility` | function | `fn public_api_symbol_accepts_plain_public_visibility() {` | `public_api_symbol_accepts_plain_public_visibility [function]` | `01b794a3-d6cf-5d0f-a631-c7bea199c9de` | 250-256 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:250-256] | Indexed function `public_api_symbol_accepts_plain_public_visibility` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:250-256] |
| `public_api_symbol_rejects_restricted_visibility` | function | `fn public_api_symbol_rejects_restricted_visibility() {` | `public_api_symbol_rejects_restricted_visibility [function]` | `b7a92ce8-6196-5ff7-9295-e6d6aa7c170b` | 259-269 [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:259-269] | Indexed function `public_api_symbol_rejects_restricted_visibility` in `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs`. [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:259-269] |
