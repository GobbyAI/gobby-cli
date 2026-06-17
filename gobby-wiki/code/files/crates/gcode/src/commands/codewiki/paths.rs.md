---
title: crates/gcode/src/commands/codewiki/paths.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/paths.rs
  ranges:
  - 3-14
  - 16-19
  - 21-33
  - 35-41
  - 43-55
  - 57-59
  - 61-68
  - 70-125
  - 130-138
  - 140-146
  - 148-156
  - 158-160
  - 162-164
  - 166-174
  - 176-178
  - 180-182
  - 184-186
  - 188-190
  - 192-194
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/paths.rs:3-14](crates/gcode/src/commands/codewiki/paths.rs#L3-L14), [crates/gcode/src/commands/codewiki/paths.rs:16-19](crates/gcode/src/commands/codewiki/paths.rs#L16-L19), [crates/gcode/src/commands/codewiki/paths.rs:21-33](crates/gcode/src/commands/codewiki/paths.rs#L21-L33), [crates/gcode/src/commands/codewiki/paths.rs:35-41](crates/gcode/src/commands/codewiki/paths.rs#L35-L41), [crates/gcode/src/commands/codewiki/paths.rs:43-55](crates/gcode/src/commands/codewiki/paths.rs#L43-L55), [crates/gcode/src/commands/codewiki/paths.rs:57-59](crates/gcode/src/commands/codewiki/paths.rs#L57-L59), [crates/gcode/src/commands/codewiki/paths.rs:61-68](crates/gcode/src/commands/codewiki/paths.rs#L61-L68), [crates/gcode/src/commands/codewiki/paths.rs:70-125](crates/gcode/src/commands/codewiki/paths.rs#L70-L125), [crates/gcode/src/commands/codewiki/paths.rs:130-138](crates/gcode/src/commands/codewiki/paths.rs#L130-L138), [crates/gcode/src/commands/codewiki/paths.rs:140-146](crates/gcode/src/commands/codewiki/paths.rs#L140-L146), [crates/gcode/src/commands/codewiki/paths.rs:148-156](crates/gcode/src/commands/codewiki/paths.rs#L148-L156), [crates/gcode/src/commands/codewiki/paths.rs:158-160](crates/gcode/src/commands/codewiki/paths.rs#L158-L160), [crates/gcode/src/commands/codewiki/paths.rs:162-164](crates/gcode/src/commands/codewiki/paths.rs#L162-L164), [crates/gcode/src/commands/codewiki/paths.rs:166-174](crates/gcode/src/commands/codewiki/paths.rs#L166-L174), [crates/gcode/src/commands/codewiki/paths.rs:176-178](crates/gcode/src/commands/codewiki/paths.rs#L176-L178), [crates/gcode/src/commands/codewiki/paths.rs:180-182](crates/gcode/src/commands/codewiki/paths.rs#L180-L182), [crates/gcode/src/commands/codewiki/paths.rs:184-186](crates/gcode/src/commands/codewiki/paths.rs#L184-L186), [crates/gcode/src/commands/codewiki/paths.rs:188-190](crates/gcode/src/commands/codewiki/paths.rs#L188-L190), [crates/gcode/src/commands/codewiki/paths.rs:192-194](crates/gcode/src/commands/codewiki/paths.rs#L192-L194)

</details>

# crates/gcode/src/commands/codewiki/paths.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Builds the codewiki’s path and Markdown formatting helpers: it normalizes inline code and table cells, writes table headers/rows, and provides small utilities like pluralization and component labels for symbols. It also defines the file/module classification and traversal logic used to decide whether a file is core, map files to modules and ancestor/child relationships, and derive doc paths and wiki links for file and module entries.
[crates/gcode/src/commands/codewiki/paths.rs:3-14]
[crates/gcode/src/commands/codewiki/paths.rs:16-19]
[crates/gcode/src/commands/codewiki/paths.rs:21-33]
[crates/gcode/src/commands/codewiki/paths.rs:35-41]
[crates/gcode/src/commands/codewiki/paths.rs:43-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `inline_code` | function | `pub(crate) fn inline_code(value: &str) -> String {` | `inline_code [function]` | `2482ea17-b327-536d-96d8-3904bc42d195` | 3-14 [crates/gcode/src/commands/codewiki/paths.rs:3-14] | Indexed function `inline_code` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:3-14] |
| `write_markdown_table_header` | function | `pub(crate) fn write_markdown_table_header(doc: &mut String, headers: &[&str]) {` | `write_markdown_table_header [function]` | `f8da6ec0-ee2a-5d79-901f-c2865c25c6ba` | 16-19 [crates/gcode/src/commands/codewiki/paths.rs:16-19] | Indexed function `write_markdown_table_header` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:16-19] |
| `write_markdown_table_row` | function | `pub(crate) fn write_markdown_table_row<I, S>(doc: &mut String, cells: I)` | `write_markdown_table_row [function]` | `55cd046b-884c-502c-a05b-92b7e278efaf` | 21-33 [crates/gcode/src/commands/codewiki/paths.rs:21-33] | Indexed function `write_markdown_table_row` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:21-33] |
| `markdown_table_cell` | function | `fn markdown_table_cell(value: &str) -> String {` | `markdown_table_cell [function]` | `cc9c6527-d72f-5a89-a18d-fcd6fccc9c0c` | 35-41 [crates/gcode/src/commands/codewiki/paths.rs:35-41] | Indexed function `markdown_table_cell` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:35-41] |
| `max_backtick_run` | function | `pub(crate) fn max_backtick_run(value: &str) -> usize {` | `max_backtick_run [function]` | `a3689204-7ba5-53ea-86c2-6dd0f652dc5e` | 43-55 [crates/gcode/src/commands/codewiki/paths.rs:43-55] | Indexed function `max_backtick_run` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:43-55] |
| `plural` | function | `pub(crate) fn plural(count: usize) -> &'static str {` | `plural [function]` | `fda35074-60be-5be2-b3b4-78ab67888349` | 57-59 [crates/gcode/src/commands/codewiki/paths.rs:57-59] | Indexed function `plural` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:57-59] |
| `component_label` | function | `pub(crate) fn component_label(symbol: &Symbol) -> String {` | `component_label [function]` | `c6bbe1d3-6faa-55a2-81f1-44f8613fe74c` | 61-68 [crates/gcode/src/commands/codewiki/paths.rs:61-68] | Indexed function `component_label` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:61-68] |
| `is_core_file` | function | `pub(crate) fn is_core_file(file: &str) -> bool {` | `is_core_file [function]` | `e1094292-25ba-5472-b1cc-ed174d011e8c` | 70-125 [crates/gcode/src/commands/codewiki/paths.rs:70-125] | Indexed function `is_core_file` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:70-125] |
| `in_scope` | function | `pub(crate) fn in_scope(file: &str, scopes: &[String]) -> bool {` | `in_scope [function]` | `0494544c-545f-58f9-8a1d-578187b5fbbb` | 130-138 [crates/gcode/src/commands/codewiki/paths.rs:130-138] | Indexed function `in_scope` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:130-138] |
| `module_for_file` | function | `pub(crate) fn module_for_file(file: &str) -> String {` | `module_for_file [function]` | `e643289f-77bd-5580-a116-9ebc9a6b6819` | 140-146 [crates/gcode/src/commands/codewiki/paths.rs:140-146] | Indexed function `module_for_file` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:140-146] |
| `module_ancestors` | function | `pub(crate) fn module_ancestors(module: &str) -> Vec<String> {` | `module_ancestors [function]` | `d314a6e3-95a4-55ff-8c7c-b291b3e79d1e` | 148-156 [crates/gcode/src/commands/codewiki/paths.rs:148-156] | Indexed function `module_ancestors` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:148-156] |
| `parent_module` | function | `pub(crate) fn parent_module(module: &str) -> Option<&str> {` | `parent_module [function]` | `1820419b-d1eb-5bfa-b6fd-649f48c0be1f` | 158-160 [crates/gcode/src/commands/codewiki/paths.rs:158-160] | Indexed function `parent_module` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:158-160] |
| `module_is_ancestor` | function | `pub(crate) fn module_is_ancestor(module: &str, child: &str) -> bool {` | `module_is_ancestor [function]` | `8fc35791-f33d-5bb1-a952-22541dde87b0` | 162-164 [crates/gcode/src/commands/codewiki/paths.rs:162-164] | Indexed function `module_is_ancestor` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:162-164] |
| `direct_child_modules` | function | `pub(crate) fn direct_child_modules<'a>(` | `direct_child_modules [function]` | `b9825e57-6381-5910-a947-7eb7a7e1b788` | 166-174 [crates/gcode/src/commands/codewiki/paths.rs:166-174] | Indexed function `direct_child_modules` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:166-174] |
| `module_depth` | function | `pub(crate) fn module_depth(module: &str) -> usize {` | `module_depth [function]` | `60e93f58-79fb-547d-a4e4-9c2b45b008bd` | 176-178 [crates/gcode/src/commands/codewiki/paths.rs:176-178] | Indexed function `module_depth` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:176-178] |
| `file_doc_path` | function | `pub(crate) fn file_doc_path(file: &str) -> String {` | `file_doc_path [function]` | `99b3c8b0-1ad0-5e88-9454-57373f7cffee` | 180-182 [crates/gcode/src/commands/codewiki/paths.rs:180-182] | Indexed function `file_doc_path` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:180-182] |
| `module_doc_path` | function | `pub(crate) fn module_doc_path(module: &str) -> String {` | `module_doc_path [function]` | `14512cee-8613-50af-bfab-e90b60644fe4` | 184-186 [crates/gcode/src/commands/codewiki/paths.rs:184-186] | Indexed function `module_doc_path` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:184-186] |
| `file_wikilink` | function | `pub(crate) fn file_wikilink(file: &str) -> String {` | `file_wikilink [function]` | `450db009-9ddc-5b6f-bd64-7adc0a004c70` | 188-190 [crates/gcode/src/commands/codewiki/paths.rs:188-190] | Indexed function `file_wikilink` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:188-190] |
| `module_wikilink` | function | `pub(crate) fn module_wikilink(module: &str) -> String {` | `module_wikilink [function]` | `0cee6b8a-47ac-5085-9f29-43d1d1e421d8` | 192-194 [crates/gcode/src/commands/codewiki/paths.rs:192-194] | Indexed function `module_wikilink` in `crates/gcode/src/commands/codewiki/paths.rs`. [crates/gcode/src/commands/codewiki/paths.rs:192-194] |
