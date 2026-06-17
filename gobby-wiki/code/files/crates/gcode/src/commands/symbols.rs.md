---
title: crates/gcode/src/commands/symbols.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/symbols.rs
  ranges:
  - 21-78
  - 80-103
  - 105-126
  - 128-142
  - 144-167
  - 169-183
  - 185-200
  - 202-229
  - 231-239
  - 241-256
  - 258-302
  - 304-341
  - 343-356
  - 358-382
  - 390-417
  - 423-444
  - 447-453
  - 456-478
  - 481-490
  - 493-511
  - 514-516
  - 519-531
  - 534-557
  - 560-568
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/symbols.rs:21-78](crates/gcode/src/commands/symbols.rs#L21-L78), [crates/gcode/src/commands/symbols.rs:80-103](crates/gcode/src/commands/symbols.rs#L80-L103), [crates/gcode/src/commands/symbols.rs:105-126](crates/gcode/src/commands/symbols.rs#L105-L126), [crates/gcode/src/commands/symbols.rs:128-142](crates/gcode/src/commands/symbols.rs#L128-L142), [crates/gcode/src/commands/symbols.rs:144-167](crates/gcode/src/commands/symbols.rs#L144-L167), [crates/gcode/src/commands/symbols.rs:169-183](crates/gcode/src/commands/symbols.rs#L169-L183), [crates/gcode/src/commands/symbols.rs:185-200](crates/gcode/src/commands/symbols.rs#L185-L200), [crates/gcode/src/commands/symbols.rs:202-229](crates/gcode/src/commands/symbols.rs#L202-L229), [crates/gcode/src/commands/symbols.rs:231-239](crates/gcode/src/commands/symbols.rs#L231-L239), [crates/gcode/src/commands/symbols.rs:241-256](crates/gcode/src/commands/symbols.rs#L241-L256), [crates/gcode/src/commands/symbols.rs:258-302](crates/gcode/src/commands/symbols.rs#L258-L302), [crates/gcode/src/commands/symbols.rs:304-341](crates/gcode/src/commands/symbols.rs#L304-L341), [crates/gcode/src/commands/symbols.rs:343-356](crates/gcode/src/commands/symbols.rs#L343-L356), [crates/gcode/src/commands/symbols.rs:358-382](crates/gcode/src/commands/symbols.rs#L358-L382), [crates/gcode/src/commands/symbols.rs:390-417](crates/gcode/src/commands/symbols.rs#L390-L417), [crates/gcode/src/commands/symbols.rs:423-444](crates/gcode/src/commands/symbols.rs#L423-L444), [crates/gcode/src/commands/symbols.rs:447-453](crates/gcode/src/commands/symbols.rs#L447-L453), [crates/gcode/src/commands/symbols.rs:456-478](crates/gcode/src/commands/symbols.rs#L456-L478), [crates/gcode/src/commands/symbols.rs:481-490](crates/gcode/src/commands/symbols.rs#L481-L490), [crates/gcode/src/commands/symbols.rs:493-511](crates/gcode/src/commands/symbols.rs#L493-L511), [crates/gcode/src/commands/symbols.rs:514-516](crates/gcode/src/commands/symbols.rs#L514-L516), [crates/gcode/src/commands/symbols.rs:519-531](crates/gcode/src/commands/symbols.rs#L519-L531), [crates/gcode/src/commands/symbols.rs:534-557](crates/gcode/src/commands/symbols.rs#L534-L557), [crates/gcode/src/commands/symbols.rs:560-568](crates/gcode/src/commands/symbols.rs#L560-L568)

</details>

# crates/gcode/src/commands/symbols.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

This file implements the `gcode` symbol-inspection commands for a file or project: it collects visible symbols, renders them as outline, symbol list, kinds, or tree text, and optionally returns JSON. The `outline` entry point ties the pieces together by normalizing the target file, querying the database for visible symbols, emitting a missing-symbol diagnostic when needed, optionally generating an AI summary through the outline-summary helpers, and reporting savings when the outline is smaller than the source file. Supporting helpers format outline and tree lines, compute indentation and depth, and build diagnostics for unsupported file types or empty results, while the tests assert the text rendering, grouping, size cap, and AI-summary behavior.
[crates/gcode/src/commands/symbols.rs:21-78]
[crates/gcode/src/commands/symbols.rs:80-103]
[crates/gcode/src/commands/symbols.rs:105-126]
[crates/gcode/src/commands/symbols.rs:128-142]
[crates/gcode/src/commands/symbols.rs:144-167]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `outline` | function | `pub fn outline(` | `outline [function]` | `2bea4bc1-87fb-55dd-9bed-abd5a8f54a06` | 21-78 [crates/gcode/src/commands/symbols.rs:21-78] | Indexed function `outline` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:21-78] |
| `summarize_outline` | function | `fn summarize_outline(` | `summarize_outline [function]` | `3535bbf7-0318-5635-ae4b-88c9fe4f4cfc` | 80-103 [crates/gcode/src/commands/symbols.rs:80-103] | Indexed function `summarize_outline` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:80-103] |
| `resolve_outline_ai_context` | function | `fn resolve_outline_ai_context(` | `resolve_outline_ai_context [function]` | `3155cb3f-4543-5070-adce-6a51afdade1a` | 105-126 [crates/gcode/src/commands/symbols.rs:105-126] | Indexed function `resolve_outline_ai_context` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:105-126] |
| `summarize_outline_with` | function | `fn summarize_outline_with(` | `summarize_outline_with [function]` | `a6e7f7e9-82e6-532a-9af8-45be6a8eec2d` | 128-142 [crates/gcode/src/commands/symbols.rs:128-142] | Indexed function `summarize_outline_with` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:128-142] |
| `outline_summary_prompt` | function | `fn outline_summary_prompt(file: &str, code: &str, symbols: &[Symbol]) -> String {` | `outline_summary_prompt [function]` | `66af113c-9a06-5ee0-af25-7a23a1096bae` | 144-167 [crates/gcode/src/commands/symbols.rs:144-167] | Indexed function `outline_summary_prompt` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:144-167] |
| `render_outline_text` | function | `fn render_outline_text(symbols: &[Symbol]) -> String {` | `render_outline_text [function]` | `c58daa35-639a-5714-a070-5d25b0e7cb50` | 169-183 [crates/gcode/src/commands/symbols.rs:169-183] | Indexed function `render_outline_text` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:169-183] |
| `outline_depth` | function | `fn outline_depth(symbol: &Symbol, parent_by_id: &BTreeMap<&str, Option<&str>>) -> usize {` | `outline_depth [function]` | `9b7ac049-fe01-5ffe-81c7-ad806e2571c3` | 185-200 [crates/gcode/src/commands/symbols.rs:185-200] | Indexed function `outline_depth` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:185-200] |
| `outline_missing_diagnostic` | function | `fn outline_missing_diagnostic(conn: &mut postgres::Client, ctx: &Context, file: &str) -> String {` | `outline_missing_diagnostic [function]` | `ebafebd4-9950-571e-8f46-6a86497dca40` | 202-229 [crates/gcode/src/commands/symbols.rs:202-229] | Indexed function `outline_missing_diagnostic` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:202-229] |
| `unsupported_file_type_diagnostic` | function | `fn unsupported_file_type_diagnostic(file: &str) -> Option<String> {` | `unsupported_file_type_diagnostic [function]` | `d175df56-582d-58a6-9514-2e05bdb9eb06` | 231-239 [crates/gcode/src/commands/symbols.rs:231-239] | Indexed function `unsupported_file_type_diagnostic` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:231-239] |
| `format_outline_text_line` | function | `fn format_outline_text_line(symbol: &Symbol) -> String {` | `format_outline_text_line [function]` | `2c0c9a6b-a82c-549a-b9a1-461293435c3c` | 241-256 [crates/gcode/src/commands/symbols.rs:241-256] | Indexed function `format_outline_text_line` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:241-256] |
| `symbol` | function | `pub fn symbol(ctx: &Context, id: &str, format: Format) -> anyhow::Result<()> {` | `symbol [function]` | `7ea78713-8eda-51aa-8c77-f5c0f4b9a04a` | 258-302 [crates/gcode/src/commands/symbols.rs:258-302] | Indexed function `symbol` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:258-302] |
| `symbols` | function | `pub fn symbols(ctx: &Context, ids: &[String], format: Format) -> anyhow::Result<()> {` | `symbols [function]` | `9521bf45-2eac-5781-83a6-21ec649b8b9f` | 304-341 [crates/gcode/src/commands/symbols.rs:304-341] | Indexed function `symbols` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:304-341] |
| `kinds` | function | `pub fn kinds(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `kinds [function]` | `b97216f5-cf26-58d7-b38d-9103fed8afb3` | 343-356 [crates/gcode/src/commands/symbols.rs:343-356] | Indexed function `kinds` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:343-356] |
| `tree` | function | `pub fn tree(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `tree [function]` | `24bed737-4fa7-5ab8-9bf3-e38c219e02ff` | 358-382 [crates/gcode/src/commands/symbols.rs:358-382] | Indexed function `tree` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:358-382] |
| `format_tree_text` | function | `fn format_tree_text(files: &[serde_json::Value]) -> String {` | `format_tree_text [function]` | `0351679b-ba05-5c7f-8d5e-657fe653fbf7` | 390-417 [crates/gcode/src/commands/symbols.rs:390-417] | Indexed function `format_tree_text` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:390-417] |
| `symbol` | function | `fn symbol() -> Symbol {` | `symbol [function]` | `ae9205d4-8378-5d81-99ea-e7a496b2501f` | 423-444 [crates/gcode/src/commands/symbols.rs:423-444] | Indexed function `symbol` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:423-444] |
| `outline_text_line_includes_id_range_and_signature` | function | `fn outline_text_line_includes_id_range_and_signature() {` | `outline_text_line_includes_id_range_and_signature [function]` | `3a495357-8ad7-5074-878a-4908ccf1d1eb` | 447-453 [crates/gcode/src/commands/symbols.rs:447-453] | Indexed function `outline_text_line_includes_id_range_and_signature` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:447-453] |
| `outline_text_indents_by_parent_chain_depth` | function | `fn outline_text_indents_by_parent_chain_depth() {` | `outline_text_indents_by_parent_chain_depth [function]` | `c0bead53-7fb9-56bd-be8f-756c377ae42a` | 456-478 [crates/gcode/src/commands/symbols.rs:456-478] | Indexed function `outline_text_indents_by_parent_chain_depth` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:456-478] |
| `unsupported_file_type_diagnostic_mentions_text_only_indexing` | function | `fn unsupported_file_type_diagnostic_mentions_text_only_indexing() {` | `unsupported_file_type_diagnostic_mentions_text_only_indexing [function]` | `a7af1ae1-49e9-59cd-a7ac-314fe41af555` | 481-490 [crates/gcode/src/commands/symbols.rs:481-490] | Indexed function `unsupported_file_type_diagnostic_mentions_text_only_indexing` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:481-490] |
| `summarizes_when_configured` | function | `fn summarizes_when_configured() {` | `summarizes_when_configured [function]` | `68778310-0ca8-57cb-bee4-a85498074174` | 493-511 [crates/gcode/src/commands/symbols.rs:493-511] | Indexed function `summarizes_when_configured` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:493-511] |
| `outline_summary_size_cap_is_one_mib` | function | `fn outline_summary_size_cap_is_one_mib() {` | `outline_summary_size_cap_is_one_mib [function]` | `1fd19515-7ef7-5b99-892e-29d8066c8e16` | 514-516 [crates/gcode/src/commands/symbols.rs:514-516] | Indexed function `outline_summary_size_cap_is_one_mib` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:514-516] |
| `degrades_to_ast` | function | `fn degrades_to_ast() {` | `degrades_to_ast [function]` | `2e07e1dd-bb99-50d4-97c2-fa9ec4982550` | 519-531 [crates/gcode/src/commands/symbols.rs:519-531] | Indexed function `degrades_to_ast` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:519-531] |
| `tree_text_groups_files_by_directory` | function | `fn tree_text_groups_files_by_directory() {` | `tree_text_groups_files_by_directory [function]` | `7e77fc44-3557-563d-8d38-3d4d018ee60a` | 534-557 [crates/gcode/src/commands/symbols.rs:534-557] | Indexed function `tree_text_groups_files_by_directory` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:534-557] |
| `tree_text_treats_absolute_root_files_as_root_group` | function | `fn tree_text_treats_absolute_root_files_as_root_group() {` | `tree_text_treats_absolute_root_files_as_root_group [function]` | `a74c1fe5-3e4d-53f8-a764-9aeaf39d607a` | 560-568 [crates/gcode/src/commands/symbols.rs:560-568] | Indexed function `tree_text_treats_absolute_root_files_as_root_group` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:560-568] |
