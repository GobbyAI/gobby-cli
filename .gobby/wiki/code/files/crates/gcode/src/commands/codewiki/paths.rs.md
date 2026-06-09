---
title: crates/gcode/src/commands/codewiki/paths.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/paths.rs
  ranges:
  - 3-14
  - 16-28
  - 30-32
  - 34-41
  - 43-88
  - 93-101
  - 103-109
  - 111-119
  - 121-123
  - 125-127
  - 129-137
  - 139-141
  - 143-145
  - 147-149
  - 151-153
  - 155-157
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/paths.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/paths.rs` exposes 16 indexed API symbols.
[crates/gcode/src/commands/codewiki/paths.rs:3-14] [crates/gcode/src/commands/codewiki/paths.rs:16-28] [crates/gcode/src/commands/codewiki/paths.rs:30-32] [crates/gcode/src/commands/codewiki/paths.rs:34-41]
[crates/gcode/src/commands/codewiki/paths.rs:43-88] [crates/gcode/src/commands/codewiki/paths.rs:93-101] [crates/gcode/src/commands/codewiki/paths.rs:103-109] [crates/gcode/src/commands/codewiki/paths.rs:111-119]
[crates/gcode/src/commands/codewiki/paths.rs:121-123] [crates/gcode/src/commands/codewiki/paths.rs:125-127] [crates/gcode/src/commands/codewiki/paths.rs:129-137] [crates/gcode/src/commands/codewiki/paths.rs:139-141]
[crates/gcode/src/commands/codewiki/paths.rs:143-145] [crates/gcode/src/commands/codewiki/paths.rs:147-149] [crates/gcode/src/commands/codewiki/paths.rs:151-153] [crates/gcode/src/commands/codewiki/paths.rs:155-157]

## API Symbols

- `inline_code` (function) component `inline_code [function]` (`2482ea17-b327-536d-96d8-3904bc42d195`) lines 3-14 [crates/gcode/src/commands/codewiki/paths.rs:3-14]
  - Signature: `pub(crate) fn inline_code(value: &str) -> String {`
  - Purpose: Formats a string as markdown inline code by collapsing newlines to spaces and wrapping it with a backtick delimiter sized to exceed the longest consecutive backtick sequence in the value. [crates/gcode/src/commands/codewiki/paths.rs:3-14]
- `max_backtick_run` (function) component `max_backtick_run [function]` (`486922ed-7bb3-57b1-b8f2-acaceaef8a1a`) lines 16-28 [crates/gcode/src/commands/codewiki/paths.rs:16-28]
  - Signature: `pub(crate) fn max_backtick_run(value: &str) -> usize {`
  - Purpose: This function computes and returns the length of the longest consecutive sequence of backtick characters in the input string. [crates/gcode/src/commands/codewiki/paths.rs:16-28]
- `plural` (function) component `plural [function]` (`8d64f358-8e09-57a3-a913-ff04cbc92b4d`) lines 30-32 [crates/gcode/src/commands/codewiki/paths.rs:30-32]
  - Signature: `pub(crate) fn plural(count: usize) -> &'static str {`
  - Purpose: Returns a static string suffix for English pluralization—an empty string if count equals 1, otherwise "s". [crates/gcode/src/commands/codewiki/paths.rs:30-32]
- `component_label` (function) component `component_label [function]` (`d55b1cdc-aa9a-567f-b831-3741fd4d646e`) lines 34-41 [crates/gcode/src/commands/codewiki/paths.rs:34-41]
  - Signature: `pub(crate) fn component_label(symbol: &Symbol) -> String {`
  - Purpose: This function returns a formatted string combining a Symbol's qualified name (or simple name if unavailable) with its kind in square brackets. [crates/gcode/src/commands/codewiki/paths.rs:34-41]
- `is_core_file` (function) component `is_core_file [function]` (`2a66d8af-c33f-5163-a4ce-df42be815f1e`) lines 43-88 [crates/gcode/src/commands/codewiki/paths.rs:43-88]
  - Signature: `pub(crate) fn is_core_file(file: &str) -> bool {`
  - Purpose: Returns `true` if the file is a core source file, excluding generated files, test files, and paths containing test, mock, fixture, vendor, or build-related directories. [crates/gcode/src/commands/codewiki/paths.rs:43-88]
- `in_scope` (function) component `in_scope [function]` (`6efdf593-ef1c-5df4-b49f-31b9034cef81`) lines 93-101 [crates/gcode/src/commands/codewiki/paths.rs:93-101]
  - Signature: `pub(crate) fn in_scope(file: &str, scopes: &[String]) -> bool {`
  - Purpose: Returns true if the file path exactly matches or is a descendant of any scope directory, or if scope filtering is disabled. [crates/gcode/src/commands/codewiki/paths.rs:93-101]
- `module_for_file` (function) component `module_for_file [function]` (`ad7bc592-5e0f-5b9a-8343-88f1503468c3`) lines 103-109 [crates/gcode/src/commands/codewiki/paths.rs:103-109]
  - Signature: `pub(crate) fn module_for_file(file: &str) -> String {`
  - Purpose: This function extracts the parent directory path from a file path, normalizes it to forward slashes, and returns an empty string if the parent is the current directory. [crates/gcode/src/commands/codewiki/paths.rs:103-109]
- `module_ancestors` (function) component `module_ancestors [function]` (`f35f2a23-4469-530d-b9ba-6a9c5a83d9b5`) lines 111-119 [crates/gcode/src/commands/codewiki/paths.rs:111-119]
  - Signature: `pub(crate) fn module_ancestors(module: &str) -> Vec<String> {`
  - Purpose: Returns a vector containing the given module and all of its ancestor modules by iteratively calling `parent_module` until reaching the root. [crates/gcode/src/commands/codewiki/paths.rs:111-119]
- `parent_module` (function) component `parent_module [function]` (`6e0c56eb-74e0-5ba5-851a-6ba437c3ff84`) lines 121-123 [crates/gcode/src/commands/codewiki/paths.rs:121-123]
  - Signature: `pub(crate) fn parent_module(module: &str) -> Option<&str> {`
  - Purpose: This function returns the parent module path by splitting the input module string on the rightmost '/' delimiter and returning the preceding substring, or `None` if no delimiter exists. [crates/gcode/src/commands/codewiki/paths.rs:121-123]
- `module_is_ancestor` (function) component `module_is_ancestor [function]` (`c821f8e3-5898-5178-83d4-5154f524a736`) lines 125-127 [crates/gcode/src/commands/codewiki/paths.rs:125-127]
  - Signature: `pub(crate) fn module_is_ancestor(module: &str, child: &str) -> bool {`
  - Purpose: Returns `true` if `module` is a non-empty ancestor of `child` in a module hierarchy by verifying that `child` starts with the prefix `module/`. [crates/gcode/src/commands/codewiki/paths.rs:125-127]
- `direct_child_modules` (function) component `direct_child_modules [function]` (`054c7865-0233-57bd-947b-ef296f0b98cf`) lines 129-137 [crates/gcode/src/commands/codewiki/paths.rs:129-137]
  - Signature: `pub(crate) fn direct_child_modules<'a>(`
  - Purpose: Filters an iterator of candidate module names and returns those whose immediate parent module matches the specified module. [crates/gcode/src/commands/codewiki/paths.rs:129-137]
- `module_depth` (function) component `module_depth [function]` (`99961a57-d75e-5273-b955-c8f109980c62`) lines 139-141 [crates/gcode/src/commands/codewiki/paths.rs:139-141]
  - Signature: `pub(crate) fn module_depth(module: &str) -> usize {`
  - Purpose: Returns the number of non-empty path components in a forward-slash-separated module string. [crates/gcode/src/commands/codewiki/paths.rs:139-141]
- `file_doc_path` (function) component `file_doc_path [function]` (`aa11fac8-2a20-5585-83fa-1f777b63a709`) lines 143-145 [crates/gcode/src/commands/codewiki/paths.rs:143-145]
  - Signature: `pub(crate) fn file_doc_path(file: &str) -> String {`
  - Purpose: This crate-private function constructs a markdown documentation file path by formatting the input filename into the `code/files/{file}.md` pattern. [crates/gcode/src/commands/codewiki/paths.rs:143-145]
- `module_doc_path` (function) component `module_doc_path [function]` (`4c9ad7d1-1c67-5486-865d-635fb1638dbe`) lines 147-149 [crates/gcode/src/commands/codewiki/paths.rs:147-149]
  - Signature: `pub(crate) fn module_doc_path(module: &str) -> String {`
  - Purpose: Generates a markdown documentation file path by interpolating the given module name into the pattern `code/modules/{module}.md`. [crates/gcode/src/commands/codewiki/paths.rs:147-149]
- `file_wikilink` (function) component `file_wikilink [function]` (`64da2255-b49a-510b-8efd-9e8da203da38`) lines 151-153 [crates/gcode/src/commands/codewiki/paths.rs:151-153]
  - Signature: `pub(crate) fn file_wikilink(file: &str) -> String {`
  - Purpose: Generates a wikilink string pointing to `code/files/{file}` with the filename as the display text. [crates/gcode/src/commands/codewiki/paths.rs:151-153]
- `module_wikilink` (function) component `module_wikilink [function]` (`923953c3-cd3c-54bd-ab13-e0cccf3d1d46`) lines 155-157 [crates/gcode/src/commands/codewiki/paths.rs:155-157]
  - Signature: `pub(crate) fn module_wikilink(module: &str) -> String {`
  - Purpose: Constructs a wiki-link string in the format `[[code/modules/{module}|{module}]]` that links to a module's documentation path with the module name as display text. [crates/gcode/src/commands/codewiki/paths.rs:155-157]

