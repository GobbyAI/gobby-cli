---
title: crates/gcode/src/index/import_resolution/parser/scala.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/scala.rs
  ranges:
  - 6-23
  - 25-57
  - 59-103
  - 105-112
  - 114-131
  - 133-145
  - 147-155
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/scala.rs:6-23](crates/gcode/src/index/import_resolution/parser/scala.rs#L6-L23), [crates/gcode/src/index/import_resolution/parser/scala.rs:25-57](crates/gcode/src/index/import_resolution/parser/scala.rs#L25-L57), [crates/gcode/src/index/import_resolution/parser/scala.rs:59-103](crates/gcode/src/index/import_resolution/parser/scala.rs#L59-L103), [crates/gcode/src/index/import_resolution/parser/scala.rs:105-112](crates/gcode/src/index/import_resolution/parser/scala.rs#L105-L112), [crates/gcode/src/index/import_resolution/parser/scala.rs:114-131](crates/gcode/src/index/import_resolution/parser/scala.rs#L114-L131), [crates/gcode/src/index/import_resolution/parser/scala.rs:133-145](crates/gcode/src/index/import_resolution/parser/scala.rs#L133-L145), [crates/gcode/src/index/import_resolution/parser/scala.rs:147-155](crates/gcode/src/index/import_resolution/parser/scala.rs#L147-L155)

</details>

# crates/gcode/src/index/import_resolution/parser/scala.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file parses Scala `import` statements and records the resolved import relations. `parse_scala_import_statement` normalizes a statement, strips the `import` keyword, splits comma-separated top-level items, and forwards each one for handling. `register_scala_import_or_group` recursively expands grouped imports like brace selections, handles wildcard module imports, or delegates to `register_scala_import_item` for ordinary imports. `register_scala_import_item` splits aliases, stores the target import, and uses the import context to resolve package-qualified names and local bindings for aliasing. The remaining helpers support that flow by splitting grouped selectors, joining nested import paths, recognizing wildcard modules, and separating aliases from targets.
[crates/gcode/src/index/import_resolution/parser/scala.rs:6-23]
[crates/gcode/src/index/import_resolution/parser/scala.rs:25-57]
[crates/gcode/src/index/import_resolution/parser/scala.rs:59-103]
[crates/gcode/src/index/import_resolution/parser/scala.rs:105-112]
[crates/gcode/src/index/import_resolution/parser/scala.rs:114-131]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_scala_import_statement` | function | `pub(crate) fn parse_scala_import_statement(` | `parse_scala_import_statement [function]` | `7d3ce58b-953a-55ef-a126-e90d034de42d` | 6-23 [crates/gcode/src/index/import_resolution/parser/scala.rs:6-23] | Indexed function `parse_scala_import_statement` in `crates/gcode/src/index/import_resolution/parser/scala.rs`. [crates/gcode/src/index/import_resolution/parser/scala.rs:6-23] |
| `register_scala_import_or_group` | function | `fn register_scala_import_or_group(` | `register_scala_import_or_group [function]` | `d7996606-16e0-51a9-a896-dce9a2dbd8c0` | 25-57 [crates/gcode/src/index/import_resolution/parser/scala.rs:25-57] | Indexed function `register_scala_import_or_group` in `crates/gcode/src/index/import_resolution/parser/scala.rs`. [crates/gcode/src/index/import_resolution/parser/scala.rs:25-57] |
| `register_scala_import_item` | function | `fn register_scala_import_item(` | `register_scala_import_item [function]` | `397541f1-a3d9-5684-be7e-9530a0d25b80` | 59-103 [crates/gcode/src/index/import_resolution/parser/scala.rs:59-103] | Indexed function `register_scala_import_item` in `crates/gcode/src/index/import_resolution/parser/scala.rs`. [crates/gcode/src/index/import_resolution/parser/scala.rs:59-103] |
| `split_scala_import_group` | function | `fn split_scala_import_group(text: &str) -> Option<(&str, &str)> {` | `split_scala_import_group [function]` | `e0a8bab6-ca9e-5581-9afb-9657861db1e2` | 105-112 [crates/gcode/src/index/import_resolution/parser/scala.rs:105-112] | Indexed function `split_scala_import_group` in `crates/gcode/src/index/import_resolution/parser/scala.rs`. [crates/gcode/src/index/import_resolution/parser/scala.rs:105-112] |
| `scala_join_import_path` | function | `fn scala_join_import_path(prefix: &str, item: &str) -> Option<String> {` | `scala_join_import_path [function]` | `82cf3f94-1763-5110-9395-2c7ecf3c48f5` | 114-131 [crates/gcode/src/index/import_resolution/parser/scala.rs:114-131] | Indexed function `scala_join_import_path` in `crates/gcode/src/index/import_resolution/parser/scala.rs`. [crates/gcode/src/index/import_resolution/parser/scala.rs:114-131] |
| `scala_wildcard_module` | function | `fn scala_wildcard_module(item: &str) -> Option<String> {` | `scala_wildcard_module [function]` | `b6c03a59-0604-55b5-b214-1f438fd0ae27` | 133-145 [crates/gcode/src/index/import_resolution/parser/scala.rs:133-145] | Indexed function `scala_wildcard_module` in `crates/gcode/src/index/import_resolution/parser/scala.rs`. [crates/gcode/src/index/import_resolution/parser/scala.rs:133-145] |
| `split_scala_alias` | function | `fn split_scala_alias(text: &str) -> (&str, Option<&str>) {` | `split_scala_alias [function]` | `30661c80-e80c-55e5-9670-3eb7956be103` | 147-155 [crates/gcode/src/index/import_resolution/parser/scala.rs:147-155] | Indexed function `split_scala_alias` in `crates/gcode/src/index/import_resolution/parser/scala.rs`. [crates/gcode/src/index/import_resolution/parser/scala.rs:147-155] |
