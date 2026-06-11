---
title: crates/gcode/src/commands/symbols.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/symbols.rs
  ranges:
  - 21-80
  - 82-105
  - 107-128
  - 130-144
  - 146-169
  - 171-185
  - 187-202
  - 204-231
  - 233-241
  - 243-258
  - 260-306
  - 308-347
  - 349-362
  - 364-388
  - 396-423
  - 429-450
  - 453-459
  - 462-484
  - 487-496
  - 499-517
  - 520-522
  - 525-537
  - 540-563
  - 566-574
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/symbols.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/symbols.rs` exposes 24 indexed API symbols.
[crates/gcode/src/commands/symbols.rs:21-80]
[crates/gcode/src/commands/symbols.rs:82-105]
[crates/gcode/src/commands/symbols.rs:107-128]
[crates/gcode/src/commands/symbols.rs:130-144]
[crates/gcode/src/commands/symbols.rs:146-169]

## API Symbols

- `outline` (function) component `outline [function]` (`2bea4bc1-87fb-55dd-9bed-abd5a8f54a06`) lines 21-80 [crates/gcode/src/commands/symbols.rs:21-80]
  - Signature: `pub fn outline(`
  - Purpose: Retrieves visible symbols for a specified file from a readonly database and outputs them in JSON or text format, with optional summarization and storage efficiency reporting. [crates/gcode/src/commands/symbols.rs:21-80]
- `summarize_outline` (function) component `summarize_outline [function]` (`c04fc718-a0e2-5f0a-af1f-591b6d6ef8b0`) lines 82-105 [crates/gcode/src/commands/symbols.rs:82-105]
  - Signature: `fn summarize_outline(`
  - Purpose: # Summary

Generates an AI-powered text summary of a code file's outline using symbol information, with routing through either daemon or direct text generation based on configured AI capabilities and file size validation. [crates/gcode/src/commands/symbols.rs:82-105]
- `resolve_outline_ai_context` (function) component `resolve_outline_ai_context [function]` (`fd3eb540-2416-5a83-a541-ed2eba51f6d2`) lines 107-128 [crates/gcode/src/commands/symbols.rs:107-128]
  - Signature: `fn resolve_outline_ai_context(`
  - Purpose: Resolves an AiContext by composing a PostgreSQL-backed primary AI configuration source with optional standalone configuration, using either a provided or newly created read-only database connection keyed to the project ID. [crates/gcode/src/commands/symbols.rs:107-128]
- `summarize_outline_with` (function) component `summarize_outline_with [function]` (`675132d7-78b2-5f44-b379-5309da07aca8`) lines 130-144 [crates/gcode/src/commands/symbols.rs:130-144]
  - Signature: `fn summarize_outline_with(`
  - Purpose: This function generates an optional outline summary by constructing a prompt from source code and symbols, passing it to a generator callback function with a predefined system prompt, and returning the trimmed result only if both the input code and output are non-empty. [crates/gcode/src/commands/symbols.rs:130-144]
- `outline_summary_prompt` (function) component `outline_summary_prompt [function]` (`68d8731d-cbe8-5431-b52b-65b2f89ec570`) lines 146-169 [crates/gcode/src/commands/symbols.rs:146-169]
  - Signature: `fn outline_summary_prompt(file: &str, code: &str, symbols: &[Symbol]) -> String {`
  - Purpose: Constructs a formatted prompt string combining file metadata, indexed symbols with their locations and optional signatures, and source code content. [crates/gcode/src/commands/symbols.rs:146-169]
- `render_outline_text` (function) component `render_outline_text [function]` (`178a3242-1be9-51bf-9279-e66511b37ae8`) lines 171-185 [crates/gcode/src/commands/symbols.rs:171-185]
  - Signature: `fn render_outline_text(symbols: &[Symbol]) -> String {`
  - Purpose: Renders a hierarchically-indented outline string from symbols by calculating each symbol's depth in the parent-child relationship tree and applying proportional indentation (two spaces per level). [crates/gcode/src/commands/symbols.rs:171-185]
- `outline_depth` (function) component `outline_depth [function]` (`a00df07e-8384-56eb-aba2-1f883ef7a644`) lines 187-202 [crates/gcode/src/commands/symbols.rs:187-202]
  - Signature: `fn outline_depth(symbol: &Symbol, parent_by_id: &BTreeMap<&str, Option<&str>>) -> usize {`
  - Purpose: This function calculates the hierarchical depth of a symbol by traversing upward through its parent chain, counting ancestors until reaching a root node or detecting a cycle. [crates/gcode/src/commands/symbols.rs:187-202]
- `outline_missing_diagnostic` (function) component `outline_missing_diagnostic [function]` (`ab094e56-364f-5f25-a6b6-8ad4a982fffb`) lines 204-231 [crates/gcode/src/commands/symbols.rs:204-231]
  - Signature: `fn outline_missing_diagnostic(conn: &mut postgres::Client, ctx: &Context, file: &str) -> String {`
  - Purpose: Generates a diagnostic message explaining why a file is not indexed or inaccessible in the current project, based on its scope, indexing status, project ownership, and content presence. [crates/gcode/src/commands/symbols.rs:204-231]
- `unsupported_file_type_diagnostic` (function) component `unsupported_file_type_diagnostic [function]` (`a1660bfb-1cfc-5d64-a05f-bb6b8c7e2a9c`) lines 233-241 [crates/gcode/src/commands/symbols.rs:233-241]
  - Signature: `fn unsupported_file_type_diagnostic(file: &str) -> Option<String> {`
  - Purpose: Returns an optional diagnostic message when language detection fails, indicating the file will be indexed as text chunks without AST parsing support. [crates/gcode/src/commands/symbols.rs:233-241]
- `format_outline_text_line` (function) component `format_outline_text_line [function]` (`a189e064-1e87-50d6-89b9-c795ecc55f69`) lines 243-258 [crates/gcode/src/commands/symbols.rs:243-258]
  - Signature: `fn format_outline_text_line(symbol: &Symbol) -> String {`
  - Purpose: Formats a Symbol reference into a space-separated outline line containing its file path, line range, kind, qualified name, id, and optional signature. [crates/gcode/src/commands/symbols.rs:243-258]
- `symbol` (function) component `symbol [function]` (`ab554e34-0abd-528e-bbb3-a783158d09f9`) lines 260-306 [crates/gcode/src/commands/symbols.rs:260-306]
  - Signature: `pub fn symbol(ctx: &Context, id: &str, format: Format) -> anyhow::Result<()> {`
  - Purpose: Retrieves a symbol by ID from a read-only database, extracts its source code snippet from the corresponding file, optionally reports token savings metrics to a daemon, and outputs the result in the specified format (JSON or Text). [crates/gcode/src/commands/symbols.rs:260-306]
- `symbols` (function) component `symbols [function]` (`1a2955dd-20eb-59f7-8ce2-4c664d9c9eb6`) lines 308-347 [crates/gcode/src/commands/symbols.rs:308-347]
  - Signature: `pub fn symbols(ctx: &Context, ids: &[String], format: Format) -> anyhow::Result<()> {`
  - Purpose: Retrieves symbols by ID from a read-only database, calculates and reports aggregate file compression savings metrics to a daemon service, and outputs the results in the specified format (JSON or text). [crates/gcode/src/commands/symbols.rs:308-347]
- `kinds` (function) component `kinds [function]` (`22433aba-6503-533d-9898-b9037bed2e29`) lines 349-362 [crates/gcode/src/commands/symbols.rs:349-362]
  - Signature: `pub fn kinds(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Retrieves visibility-filtered kinds from a read-only database connection and outputs them in either JSON or plaintext format based on the provided format parameter. [crates/gcode/src/commands/symbols.rs:349-362]
- `tree` (function) component `tree [function]` (`39cade2e-3b68-5aff-961e-4b564dd897ac`) lines 364-388 [crates/gcode/src/commands/symbols.rs:364-388]
  - Signature: `pub fn tree(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Retrieves visible files from a read-only database, extracts their path, language, and symbol count metadata, and outputs the results in either JSON or text format based on the specified `Format` parameter. [crates/gcode/src/commands/symbols.rs:364-388]
- `format_tree_text` (function) component `format_tree_text [function]` (`9087b197-da6e-500d-aa81-33dbc7f2ed99`) lines 396-423 [crates/gcode/src/commands/symbols.rs:396-423]
  - Signature: `fn format_tree_text(files: &[serde_json::Value]) -> String {`
  - Purpose: Converts an array of JSON file objects into a newline-delimited, directory-grouped text representation where each file entry displays its basename, language, and symbol count. [crates/gcode/src/commands/symbols.rs:396-423]
- `symbol` (function) component `symbol [function]` (`0d0ee78a-0121-595f-be2f-7dcad3b316b0`) lines 429-450 [crates/gcode/src/commands/symbols.rs:429-450]
  - Signature: `fn symbol() -> Symbol {`
  - Purpose: Constructs and returns a `Symbol` struct instance populated with metadata for a Rust function named `outline` located in src/commands.rs (lines 7-63). [crates/gcode/src/commands/symbols.rs:429-450]
- `outline_text_line_includes_id_range_and_signature` (function) component `outline_text_line_includes_id_range_and_signature [function]` (`96a02a33-d726-55bc-a5a0-a0884042d976`) lines 453-459 [crates/gcode/src/commands/symbols.rs:453-459]
  - Signature: `fn outline_text_line_includes_id_range_and_signature() {`
  - Purpose: This test function asserts that `format_outline_text_line` generates a formatted string containing the source file location with line range and symbol type, a UUID-based identifier, and the function's signature. [crates/gcode/src/commands/symbols.rs:453-459]
- `outline_text_indents_by_parent_chain_depth` (function) component `outline_text_indents_by_parent_chain_depth [function]` (`d0e99dff-65ed-5360-99a2-cdc3fe4fb6c6`) lines 462-484 [crates/gcode/src/commands/symbols.rs:462-484]
  - Signature: `fn outline_text_indents_by_parent_chain_depth() {`
  - Purpose: This function tests that `render_outline_text()` indents outline entries by two spaces for each level of depth in the parent symbol hierarchy. [crates/gcode/src/commands/symbols.rs:462-484]
- `unsupported_file_type_diagnostic_mentions_text_only_indexing` (function) component `unsupported_file_type_diagnostic_mentions_text_only_indexing [function]` (`759c9f13-ed10-5fad-8d3d-b907653c2db5`) lines 487-496 [crates/gcode/src/commands/symbols.rs:487-496]
  - Signature: `fn unsupported_file_type_diagnostic_mentions_text_only_indexing() {`
  - Purpose: This test function verifies that `unsupported_file_type_diagnostic` returns a diagnostic message indicating text-only indexing for unsupported file types (e.g., Dockerfile) and `None` for AST-parseable file types (e.g., .rs files). [crates/gcode/src/commands/symbols.rs:487-496]
- `summarizes_when_configured` (function) component `summarizes_when_configured [function]` (`1bbf1ccc-4e43-5041-9662-9d2becd3a44b`) lines 499-517 [crates/gcode/src/commands/symbols.rs:499-517]
  - Signature: `fn summarizes_when_configured() {`
  - Purpose: Unit test verifying that `summarize_outline_with` correctly constructs a prompt containing file path, symbols, and code, then validates the callback's assertion checks and return value. [crates/gcode/src/commands/symbols.rs:499-517]
- `outline_summary_size_cap_is_one_mib` (function) component `outline_summary_size_cap_is_one_mib [function]` (`e6ff2d99-9378-57a7-bc0b-cedb6ce9be0c`) lines 520-522 [crates/gcode/src/commands/symbols.rs:520-522]
  - Signature: `fn outline_summary_size_cap_is_one_mib() {`
  - Purpose: This function is a test that asserts the `OUTLINE_SUMMARY_MAX_BYTES` constant equals exactly 1 MiB (1,048,576 bytes). [crates/gcode/src/commands/symbols.rs:520-522]
- `degrades_to_ast` (function) component `degrades_to_ast [function]` (`087123e4-f17a-5834-ae65-694943c5e4ad`) lines 525-537 [crates/gcode/src/commands/symbols.rs:525-537]
  - Signature: `fn degrades_to_ast() {`
  - Purpose: This test verifies that when outline summarization is unavailable (the prompt handler returns None), the system correctly defaults to the base AST outline representation. [crates/gcode/src/commands/symbols.rs:525-537]
- `tree_text_groups_files_by_directory` (function) component `tree_text_groups_files_by_directory [function]` (`590ed386-de6d-53b9-baf2-08a0aacefb77`) lines 540-563 [crates/gcode/src/commands/symbols.rs:540-563]
  - Signature: `fn tree_text_groups_files_by_directory() {`
  - Purpose: This test validates that `format_tree_text` generates a directory-grouped tree structure displaying each file's language and symbol count. [crates/gcode/src/commands/symbols.rs:540-563]
- `tree_text_treats_absolute_root_files_as_root_group` (function) component `tree_text_treats_absolute_root_files_as_root_group [function]` (`7c6eaa72-0701-5a5d-bae8-126c839ca840`) lines 566-574 [crates/gcode/src/commands/symbols.rs:566-574]
  - Signature: `fn tree_text_treats_absolute_root_files_as_root_group() {`
  - Purpose: This test verifies that `format_tree_text` treats absolute root-level files as child nodes indented under a root group indicator (`.`). [crates/gcode/src/commands/symbols.rs:566-574]

