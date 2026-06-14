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
  - 43-98
  - 103-111
  - 113-119
  - 121-129
  - 131-133
  - 135-137
  - 139-147
  - 149-151
  - 153-155
  - 157-159
  - 161-163
  - 165-167
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/paths.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file provides utility functions for a code documentation wiki generator. It contains three categories of helpers:

**Markdown formatting** (`inline_code`, `max_backtick_run`, `plural`, `component_label`) handle converting code metadata into properly-formatted Markdown text, including intelligent backtick delimiting for inline code.

**File classification and scoping** (`is_core_file`, `in_scope`) filter files to identify core project code by excluding hidden paths, tests, generated code, and auxiliary directories like vendor or node_modules.

**Module hierarchy utilities** (`module_for_file`, `module_ancestors`, `parent_module`, `module_is_ancestor`, `direct_child_modules`, `module_depth`) manage module path operations—extracting parents, finding ancestors, checking relationships, and counting nesting depth.

**Documentation path generation** (`file_doc_path`, `module_doc_path`, `file_wikilink`, `module_wikilink`) construct wiki documentation file paths and link syntax by templating filenames and module names into standardized locations.

Together, these functions support building a searchable code documentation system by normalizing file metadata, determining what code to document, organizing it hierarchically, and generating consistent wiki cross-references.
[crates/gcode/src/commands/codewiki/paths.rs:3-14]
[crates/gcode/src/commands/codewiki/paths.rs:16-28]
[crates/gcode/src/commands/codewiki/paths.rs:30-32]
[crates/gcode/src/commands/codewiki/paths.rs:34-41]
[crates/gcode/src/commands/codewiki/paths.rs:43-98]

## API Symbols

- `inline_code` (function) component `inline_code [function]` (`2482ea17-b327-536d-96d8-3904bc42d195`) lines 3-14 [crates/gcode/src/commands/codewiki/paths.rs:3-14]
  - Signature: `pub(crate) fn inline_code(value: &str) -> String {`
  - Purpose: Transforms a string into Markdown inline code by normalizing whitespace and delimiting it with backticks (count equal to the longest contiguous backtick sequence plus one), adding padding spaces when the value starts or ends with backticks. [crates/gcode/src/commands/codewiki/paths.rs:3-14]
- `max_backtick_run` (function) component `max_backtick_run [function]` (`ec4098a0-25ed-5493-b157-ed20fa7aeb45`) lines 16-28 [crates/gcode/src/commands/codewiki/paths.rs:16-28]
  - Signature: `pub(crate) fn max_backtick_run(value: &str) -> usize {`
  - Purpose: This function returns the length of the longest consecutive sequence of backtick characters in the input string. [crates/gcode/src/commands/codewiki/paths.rs:16-28]
- `plural` (function) component `plural [function]` (`316a2e47-3aca-54d4-b838-e50b108b9a97`) lines 30-32 [crates/gcode/src/commands/codewiki/paths.rs:30-32]
  - Signature: `pub(crate) fn plural(count: usize) -> &'static str {`
  - Purpose: Returns a static pluralization suffix: an empty string if `count` equals 1, otherwise `"s"`. [crates/gcode/src/commands/codewiki/paths.rs:30-32]
- `component_label` (function) component `component_label [function]` (`04d65c23-d8aa-51ac-8bd4-1fab55e33e6e`) lines 34-41 [crates/gcode/src/commands/codewiki/paths.rs:34-41]
  - Signature: `pub(crate) fn component_label(symbol: &Symbol) -> String {`
  - Purpose: Generates a component label string by concatenating a symbol's qualified name (or simple name if unqualified) with its kind in square bracket notation. [crates/gcode/src/commands/codewiki/paths.rs:34-41]
- `is_core_file` (function) component `is_core_file [function]` (`71aaee14-3966-5290-9382-5d298386c508`) lines 43-98 [crates/gcode/src/commands/codewiki/paths.rs:43-98]
  - Signature: `pub(crate) fn is_core_file(file: &str) -> bool {`
  - Purpose: **Determines whether a file is core project code by excluding hidden paths, test-related files and directories, generated code, and auxiliary directories (vendor, build, node_modules, etc.).** [crates/gcode/src/commands/codewiki/paths.rs:43-98]
- `in_scope` (function) component `in_scope [function]` (`4eef7898-0dea-5cbb-a8b7-17dedca6b71a`) lines 103-111 [crates/gcode/src/commands/codewiki/paths.rs:103-111]
  - Signature: `pub(crate) fn in_scope(file: &str, scopes: &[String]) -> bool {`
  - Purpose: Determines whether a file path is contained within or exactly matches one of the provided scopes, returning true if scopes are empty, contain an empty string, or the file matches/is nested within a scope directory. [crates/gcode/src/commands/codewiki/paths.rs:103-111]
- `module_for_file` (function) component `module_for_file [function]` (`3eacba48-7f39-5861-a224-8d6d45de0ad3`) lines 113-119 [crates/gcode/src/commands/codewiki/paths.rs:113-119]
  - Signature: `pub(crate) fn module_for_file(file: &str) -> String {`
  - Purpose: Extracts the parent directory path from a file path, normalizes backslashes to forward slashes, and returns an empty string if no parent directory exists or the parent is the current directory. [crates/gcode/src/commands/codewiki/paths.rs:113-119]
- `module_ancestors` (function) component `module_ancestors [function]` (`8e064c8a-5105-556f-b625-fbd812efd9a1`) lines 121-129 [crates/gcode/src/commands/codewiki/paths.rs:121-129]
  - Signature: `pub(crate) fn module_ancestors(module: &str) -> Vec<String> {`
  - Purpose: Returns a vector containing the given module path and all its ancestor modules, ordered from most to least specific. [crates/gcode/src/commands/codewiki/paths.rs:121-129]
- `parent_module` (function) component `parent_module [function]` (`2e0d358b-6d7a-5ec1-aeb6-b22d2ee206e9`) lines 131-133 [crates/gcode/src/commands/codewiki/paths.rs:131-133]
  - Signature: `pub(crate) fn parent_module(module: &str) -> Option<&str> {`
  - Purpose: Extracts the parent module path component by splitting the module string on the rightmost '/' delimiter, returning `Some(parent)` if a parent exists or `None` otherwise. [crates/gcode/src/commands/codewiki/paths.rs:131-133]
- `module_is_ancestor` (function) component `module_is_ancestor [function]` (`f0efb105-6797-5faf-952f-c229b14adcc3`) lines 135-137 [crates/gcode/src/commands/codewiki/paths.rs:135-137]
  - Signature: `pub(crate) fn module_is_ancestor(module: &str, child: &str) -> bool {`
  - Purpose: Checks whether `module` is a non-empty ancestor module of `child` by verifying that `child`'s path starts with `module/`. [crates/gcode/src/commands/codewiki/paths.rs:135-137]
- `direct_child_modules` (function) component `direct_child_modules [function]` (`ffc15d98-88e0-59fa-84c9-550c5854f642`) lines 139-147 [crates/gcode/src/commands/codewiki/paths.rs:139-147]
  - Signature: `pub(crate) fn direct_child_modules<'a>(`
  - Purpose: Filters an iterator of module name candidates to return only those whose direct parent module matches the given module. [crates/gcode/src/commands/codewiki/paths.rs:139-147]
- `module_depth` (function) component `module_depth [function]` (`20940da9-9adb-57b7-ad68-cace1d4ed1ea`) lines 149-151 [crates/gcode/src/commands/codewiki/paths.rs:149-151]
  - Signature: `pub(crate) fn module_depth(module: &str) -> usize {`
  - Purpose: Counts the number of non-empty path segments in a forward-slash-delimited module path string. [crates/gcode/src/commands/codewiki/paths.rs:149-151]
- `file_doc_path` (function) component `file_doc_path [function]` (`e946705f-1af1-5fc3-8e6b-08de8ab0ce94`) lines 153-155 [crates/gcode/src/commands/codewiki/paths.rs:153-155]
  - Signature: `pub(crate) fn file_doc_path(file: &str) -> String {`
  - Purpose: This function constructs and returns a markdown documentation file path by formatting the input filename into the template `code/files/{file}.md`. [crates/gcode/src/commands/codewiki/paths.rs:153-155]
- `module_doc_path` (function) component `module_doc_path [function]` (`f561e669-c4b9-5f9b-a9df-113b63c832c8`) lines 157-159 [crates/gcode/src/commands/codewiki/paths.rs:157-159]
  - Signature: `pub(crate) fn module_doc_path(module: &str) -> String {`
  - Purpose: Constructs a markdown documentation file path for a module by formatting its name into the `code/modules/{module}.md` template. [crates/gcode/src/commands/codewiki/paths.rs:157-159]
- `file_wikilink` (function) component `file_wikilink [function]` (`96e25dd9-ae72-5cc3-bcc8-527b5c212902`) lines 161-163 [crates/gcode/src/commands/codewiki/paths.rs:161-163]
  - Signature: `pub(crate) fn file_wikilink(file: &str) -> String {`
  - Purpose: Generates a MediaWiki-style wikilink string that points to `code/files/{file}` with the filename as both the link target and display text. [crates/gcode/src/commands/codewiki/paths.rs:161-163]
- `module_wikilink` (function) component `module_wikilink [function]` (`6025330a-ba66-5966-aa90-318d5f7992ef`) lines 165-167 [crates/gcode/src/commands/codewiki/paths.rs:165-167]
  - Signature: `pub(crate) fn module_wikilink(module: &str) -> String {`
  - Purpose: Converts a module name string into a wikilink string with the format `[[code/modules/{module}|{module}]]`. [crates/gcode/src/commands/codewiki/paths.rs:165-167]

