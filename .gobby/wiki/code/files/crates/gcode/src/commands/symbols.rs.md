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

# crates/gcode/src/commands/symbols.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/symbols.rs` exposes 24 indexed API symbols.
[crates/gcode/src/commands/symbols.rs:21-78]
[crates/gcode/src/commands/symbols.rs:80-103]
[crates/gcode/src/commands/symbols.rs:105-126]
[crates/gcode/src/commands/symbols.rs:128-142]
[crates/gcode/src/commands/symbols.rs:144-167]

## API Symbols

- `outline` (function) component `outline [function]` (`2bea4bc1-87fb-55dd-9bed-abd5a8f54a06`) lines 21-78 [crates/gcode/src/commands/symbols.rs:21-78]
  - Signature: `pub fn outline(`
  - Purpose: It normalizes the file path, queries the readonly database for that file’s visible symbols, optionally prints a missing-symbol diagnostic or synthesized summary, reports outline-vs-file size savings, and then emits either JSON (full or slim by `verbose`) or a rendered text outline based on `format`. [crates/gcode/src/commands/symbols.rs:21-78]
- `summarize_outline` (function) component `summarize_outline [function]` (`3535bbf7-0318-5635-ae4b-88c9fe4f4cfc`) lines 80-103 [crates/gcode/src/commands/symbols.rs:80-103]
  - Signature: `fn summarize_outline(`
  - Purpose: Returns `Some(summary)` only for project files under `OUTLINE_SUMMARY_MAX_BYTES` that can be read and summarized via resolved AI text-generation routing, otherwise `None`. [crates/gcode/src/commands/symbols.rs:80-103]
- `resolve_outline_ai_context` (function) component `resolve_outline_ai_context [function]` (`3155cb3f-4543-5070-adce-6a51afdade1a`) lines 105-126 [crates/gcode/src/commands/symbols.rs:105-126]
  - Signature: `fn resolve_outline_ai_context(`
  - Purpose: It resolves and returns an `AiContext` for `ctx.project_id` by composing standalone config with a Postgres-backed `AiConfigSource` (reusing the provided mutable `postgres::Client` if available, otherwise opening a read-only connection from `ctx.database_url`) and delegating to `AiContext::resolve`. [crates/gcode/src/commands/symbols.rs:105-126]
- `summarize_outline_with` (function) component `summarize_outline_with [function]` (`a6e7f7e9-82e6-532a-9af8-45be6a8eec2d`) lines 128-142 [crates/gcode/src/commands/symbols.rs:128-142]
  - Signature: `fn summarize_outline_with(`
  - Purpose: Returns `None` when `code` is all whitespace, otherwise builds an outline-summary prompt from `file`, `code`, and `symbols`, invokes `generate` with that prompt and `OUTLINE_SYSTEM_PROMPT`, and returns the trimmed non-empty result as `Some(String)`. [crates/gcode/src/commands/symbols.rs:128-142]
- `outline_summary_prompt` (function) component `outline_summary_prompt [function]` (`66af113c-9a06-5ee0-af25-7a23a1096bae`) lines 144-167 [crates/gcode/src/commands/symbols.rs:144-167]
  - Signature: `fn outline_summary_prompt(file: &str, code: &str, symbols: &[Symbol]) -> String {`
  - Purpose: Builds and returns a prompt string that includes the file path, a symbol inventory with each symbol’s qualified name, kind, line span, and optional non-empty signature (or a no-indexed-symbols placeholder), followed by the full source code. [crates/gcode/src/commands/symbols.rs:144-167]
- `render_outline_text` (function) component `render_outline_text [function]` (`c58daa35-639a-5714-a070-5d25b0e7cb50`) lines 169-183 [crates/gcode/src/commands/symbols.rs:169-183]
  - Signature: `fn render_outline_text(symbols: &[Symbol]) -> String {`
  - Purpose: It constructs a parent-id lookup from the input `Symbol` slice, then renders each symbol as an outline line prefixed by `2 * outline_depth` spaces and concatenates the lines with `\n`. [crates/gcode/src/commands/symbols.rs:169-183]
- `outline_depth` (function) component `outline_depth [function]` (`9b7ac049-fe01-5ffe-81c7-ad806e2571c3`) lines 185-200 [crates/gcode/src/commands/symbols.rs:185-200]
  - Signature: `fn outline_depth(symbol: &Symbol, parent_by_id: &BTreeMap<&str, Option<&str>>) -> usize {`
  - Purpose: `outline_depth` computes a symbol’s nesting depth by following `symbol.parent_symbol_id` through `parent_by_id`, incrementing for each reachable ancestor until it hits a missing parent, a root (`None`), or a detected cycle via `seen`. [crates/gcode/src/commands/symbols.rs:185-200]
- `outline_missing_diagnostic` (function) component `outline_missing_diagnostic [function]` (`ebafebd4-9950-571e-8f46-6a86497dca40`) lines 202-229 [crates/gcode/src/commands/symbols.rs:202-229]
  - Signature: `fn outline_missing_diagnostic(conn: &mut postgres::Client, ctx: &Context, file: &str) -> String {`
  - Purpose: Returns a context-sensitive diagnostic string for `file` by checking whether it exists in the current project, is indexed, is an unsupported type, belongs to another indexed project, or has indexed chunks without a matching checkout, and otherwise falls back to reporting that it is not indexed in the current project. [crates/gcode/src/commands/symbols.rs:202-229]
- `unsupported_file_type_diagnostic` (function) component `unsupported_file_type_diagnostic [function]` (`d175df56-582d-58a6-9514-2e05bdb9eb06`) lines 231-239 [crates/gcode/src/commands/symbols.rs:231-239]
  - Signature: `fn unsupported_file_type_diagnostic(file: &str) -> Option<String> {`
  - Purpose: Returns `None` when `languages::detect_language(file)` recognizes the file, otherwise returns `Some(...)` with a diagnostic stating that the file type has no AST parser support and will be indexed only as text chunks. [crates/gcode/src/commands/symbols.rs:231-239]
- `format_outline_text_line` (function) component `format_outline_text_line [function]` (`2c0c9a6b-a82c-549a-b9a1-461293435c3c`) lines 241-256 [crates/gcode/src/commands/symbols.rs:241-256]
  - Signature: `fn format_outline_text_line(symbol: &Symbol) -> String {`
  - Purpose: Formats a `Symbol` into a single outline text line containing its file path, line range, kind, qualified name, and `id`, and appends `sig=<signature>` only when `signature` is present and non-empty. [crates/gcode/src/commands/symbols.rs:241-256]
- `symbol` (function) component `symbol [function]` (`7ea78713-8eda-51aa-8c77-f5c0f4b9a04a`) lines 258-302 [crates/gcode/src/commands/symbols.rs:258-302]
  - Signature: `pub fn symbol(ctx: &Context, id: &str, format: Format) -> anyhow::Result<()> {`
  - Purpose: Resolves a visible symbol by ID from the readonly database, reads and slices its source file when present to print either JSON with an injected `source` field or raw text while optionally reporting byte-savings, falls back to metadata-only output if the file is missing, and errors if no symbol is found. [crates/gcode/src/commands/symbols.rs:258-302]
- `symbols` (function) component `symbols [function]` (`9521bf45-2eac-5781-83a6-21ec649b8b9f`) lines 304-341 [crates/gcode/src/commands/symbols.rs:304-341]
  - Signature: `pub fn symbols(ctx: &Context, ids: &[String], format: Format) -> anyhow::Result<()> {`
  - Purpose: Fetches the visible symbols for the given IDs from the readonly database, emits aggregate savings telemetry when applicable, and prints the results either as JSON or as `file_path:line_start [kind] qualified_name` text. [crates/gcode/src/commands/symbols.rs:304-341]
- `kinds` (function) component `kinds [function]` (`b97216f5-cf26-58d7-b38d-9103fed8afb3`) lines 343-356 [crates/gcode/src/commands/symbols.rs:343-356]
  - Signature: `pub fn kinds(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Connects to the database in read-only mode, computes the kinds visible in `ctx` via `visibility::visible_kinds`, and emits them as JSON or one per line in text mode, propagating any errors as `anyhow::Result<()>`. [crates/gcode/src/commands/symbols.rs:343-356]
- `tree` (function) component `tree [function]` (`24bed737-4fa7-5ab8-9bf3-e38c219e02ff`) lines 358-382 [crates/gcode/src/commands/symbols.rs:358-382]
  - Signature: `pub fn tree(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: `tree` opens a read-only database connection, collects the visible file tree into `{file_path, language, symbol_count}` JSON objects, and emits either JSON or formatted text (no-op on empty text), propagating any errors via `anyhow::Result<()>`. [crates/gcode/src/commands/symbols.rs:358-382]
- `format_tree_text` (function) component `format_tree_text [function]` (`0351679b-ba05-5c7f-8d5e-657fe653fbf7`) lines 390-417 [crates/gcode/src/commands/symbols.rs:390-417]
  - Signature: `fn format_tree_text(files: &[serde_json::Value]) -> String {`
  - Purpose: It groups the input file records by directory inferred from `file_path`, formats each entry as `basename [language] (symbol_count symbols)`, and returns the directory headings plus their entries joined by newline characters in sorted directory order. [crates/gcode/src/commands/symbols.rs:390-417]
- `symbol` (function) component `symbol [function]` (`ae9205d4-8378-5d81-99ea-e7a496b2501f`) lines 423-444 [crates/gcode/src/commands/symbols.rs:423-444]
  - Signature: `fn symbol() -> Symbol {`
  - Purpose: Returns a `Symbol` struct populated with hard-coded metadata for the Rust `outline` function, including its IDs, file path, byte and line span, signature, and empty optional fields. [crates/gcode/src/commands/symbols.rs:423-444]
- `outline_text_line_includes_id_range_and_signature` (function) component `outline_text_line_includes_id_range_and_signature [function]` (`3a495357-8ad7-5074-878a-4908ccf1d1eb`) lines 447-453 [crates/gcode/src/commands/symbols.rs:447-453]
  - Signature: `fn outline_text_line_includes_id_range_and_signature() {`
  - Purpose: Verifies that `format_outline_text_line(&symbol())` includes the expected source range and kind (`src/commands.rs:7-63 [function] outline`), the symbol UUID, and the function signature string. [crates/gcode/src/commands/symbols.rs:447-453]
- `outline_text_indents_by_parent_chain_depth` (function) component `outline_text_indents_by_parent_chain_depth [function]` (`c0bead53-7fb9-56bd-be8f-756c377ae42a`) lines 456-478 [crates/gcode/src/commands/symbols.rs:456-478]
  - Signature: `fn outline_text_indents_by_parent_chain_depth() {`
  - Purpose: This test verifies that `render_outline_text` indents each successive symbol line by two spaces per parent-chain depth, producing progressively deeper indentation for parent, child, and grandchild entries. [crates/gcode/src/commands/symbols.rs:456-478]
- `unsupported_file_type_diagnostic_mentions_text_only_indexing` (function) component `unsupported_file_type_diagnostic_mentions_text_only_indexing [function]` (`a7af1ae1-49e9-59cd-a7ac-314fe41af555`) lines 481-490 [crates/gcode/src/commands/symbols.rs:481-490]
  - Signature: `fn unsupported_file_type_diagnostic_mentions_text_only_indexing() {`
  - Purpose: This test verifies that `unsupported_file_type_diagnostic` returns the “no AST parser support; indexed as text chunks only” message for `Dockerfile` and `None` for a supported Rust source file (`src/lib.rs`). [crates/gcode/src/commands/symbols.rs:481-490]
- `summarizes_when_configured` (function) component `summarizes_when_configured [function]` (`68778310-0ca8-57cb-bee4-a85498074174`) lines 493-511 [crates/gcode/src/commands/symbols.rs:493-511]
  - Signature: `fn summarizes_when_configured() {`
  - Purpose: It verifies that `summarize_outline_with` passes the expected system prompt and file/symbol context to the summarizer, then returns the callback-provided natural-language outline when summarization is enabled. [crates/gcode/src/commands/symbols.rs:493-511]
- `outline_summary_size_cap_is_one_mib` (function) component `outline_summary_size_cap_is_one_mib [function]` (`1fd19515-7ef7-5b99-892e-29d8066c8e16`) lines 514-516 [crates/gcode/src/commands/symbols.rs:514-516]
  - Signature: `fn outline_summary_size_cap_is_one_mib() {`
  - Purpose: This test verifies that `OUTLINE_SUMMARY_MAX_BYTES` is defined as exactly `1,048,576` bytes, i.e. `1 MiB`. [crates/gcode/src/commands/symbols.rs:514-516]
- `degrades_to_ast` (function) component `degrades_to_ast [function]` (`2e07e1dd-bb99-50d4-97c2-fa9ec4982550`) lines 519-531 [crates/gcode/src/commands/symbols.rs:519-531]
  - Signature: `fn degrades_to_ast() {`
  - Purpose: Tests that `summarize_outline_with` falls back to the AST outline rendered by `render_outline_text` when the summarizer callback returns `None`, and asserts the fallback output matches that AST outline exactly. [crates/gcode/src/commands/symbols.rs:519-531]
- `tree_text_groups_files_by_directory` (function) component `tree_text_groups_files_by_directory [function]` (`7e77fc44-3557-563d-8d38-3d4d018ee60a`) lines 534-557 [crates/gcode/src/commands/symbols.rs:534-557]
  - Signature: `fn tree_text_groups_files_by_directory() {`
  - Purpose: Constructs three file-metadata JSON entries and asserts that `format_tree_text` renders them as a directory-grouped tree rooted at `.`, with each file listed under its parent directory and annotated with language and symbol count. [crates/gcode/src/commands/symbols.rs:534-557]
- `tree_text_treats_absolute_root_files_as_root_group` (function) component `tree_text_treats_absolute_root_files_as_root_group [function]` (`a74c1fe5-3e4d-53f8-a764-9aeaf39d607a`) lines 560-568 [crates/gcode/src/commands/symbols.rs:560-568]
  - Signature: `fn tree_text_treats_absolute_root_files_as_root_group() {`
  - Purpose: Indexed function `tree_text_treats_absolute_root_files_as_root_group` in `crates/gcode/src/commands/symbols.rs`. [crates/gcode/src/commands/symbols.rs:560-568]

