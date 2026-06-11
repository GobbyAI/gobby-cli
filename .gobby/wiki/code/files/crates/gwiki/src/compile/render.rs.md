---
title: crates/gwiki/src/compile/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/render.rs
  ranges:
  - 11-47
  - 49-63
  - 65-105
  - 107-144
  - 146-182
  - 184-186
  - 188-190
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile/render.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Purpose

`crates/gwiki/src/compile/render.rs` exposes 7 indexed API symbols.
[crates/gwiki/src/compile/render.rs:11-47]
[crates/gwiki/src/compile/render.rs:49-63]
[crates/gwiki/src/compile/render.rs:65-105]
[crates/gwiki/src/compile/render.rs:107-144]
[crates/gwiki/src/compile/render.rs:146-182]

## API Symbols

- `render_bundle` (function) component `render_bundle [function]` (`56943c0d-cfe8-5f14-b11b-ef9f9ecc2475`) lines 11-47 [crates/gwiki/src/compile/render.rs:11-47]
  - Signature: `pub(crate) fn render_bundle(bundle: &CompileBundle) -> String {`
  - Purpose: Converts a `CompileBundle` struct into a markdown-formatted string representation containing the topic, outline, accepted sources with their chunks, citations, conflicting claims, and missing evidence. [crates/gwiki/src/compile/render.rs:11-47]
- `render_list_section` (function) component `render_list_section [function]` (`dd6472a3-a905-5843-99bf-6c5edb0de4c9`) lines 49-63 [crates/gwiki/src/compile/render.rs:49-63]
  - Signature: `fn render_list_section(rendered: &mut String, title: &str, values: &[String]) {`
  - Purpose: Appends a markdown section with a level-2 heading, title, and bulleted list of items (or "None recorded" if empty) to a mutable String buffer. [crates/gwiki/src/compile/render.rs:49-63]
- `write_target_page` (function) component `write_target_page [function]` (`be4b6643-5374-525e-8c59-cb225be17d24`) lines 65-105 [crates/gwiki/src/compile/render.rs:65-105]
  - Signature: `pub(crate) fn write_target_page(`
  - Purpose: Writes rendered content to a newly created file at the target path, creating parent directories and validating the location is within the vault root, while failing if the file already exists. [crates/gwiki/src/compile/render.rs:65-105]
- `ensure_compile_target_parent_inside_vault` (function) component `ensure_compile_target_parent_inside_vault [function]` (`e08cbe81-33d5-5e97-a81b-d4655ca63529`) lines 107-144 [crates/gwiki/src/compile/render.rs:107-144]
  - Signature: `fn ensure_compile_target_parent_inside_vault(`
  - Purpose: Validates that a compile target's parent directory—or its nearest canonical ancestor if intermediate paths don't exist—is contained within the vault root directory. [crates/gwiki/src/compile/render.rs:107-144]
- `normalize_target_page` (function) component `normalize_target_page [function]` (`ce3526ab-ec8a-5db7-ba9f-feebabfe95eb`) lines 146-182 [crates/gwiki/src/compile/render.rs:146-182]
  - Signature: `pub(crate) fn normalize_target_page(`
  - Purpose: # Summary

Validates that a target page is a relative, non-empty path containing only normal components (rejecting absolute paths, parent/root directory traversals, and drive prefixes), then returns it joined to the vault root. [crates/gwiki/src/compile/render.rs:146-182]
- `slugify` (function) component `slugify [function]` (`3ec66435-b542-5a7c-8216-4e8d22ef9b5f`) lines 184-186 [crates/gwiki/src/compile/render.rs:184-186]
  - Signature: `pub(crate) fn slugify(topic: &str) -> String {`
  - Purpose: This function is a crate-scoped wrapper that converts a topic string into a slug by delegating to `slugify_with_options` with hardcoded options `Some("handoff")` and `None`. [crates/gwiki/src/compile/render.rs:184-186]
- `unix_timestamp_ms` (function) component `unix_timestamp_ms [function]` (`abdea677-0cb5-5f29-8d6d-1d72dc6f098f`) lines 188-190 [crates/gwiki/src/compile/render.rs:188-190]
  - Signature: `pub(crate) fn unix_timestamp_ms() -> Result<u64, WikiError> {`
  - Purpose: Retrieves the current Unix timestamp in milliseconds as a u64, or returns a WikiError on failure. [crates/gwiki/src/compile/render.rs:188-190]

