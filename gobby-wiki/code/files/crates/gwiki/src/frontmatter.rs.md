---
title: crates/gwiki/src/frontmatter.rs
type: code_file
provenance:
- file: crates/gwiki/src/frontmatter.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/frontmatter.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/frontmatter.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gwiki/src/frontmatter.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FrontmatterFormat` | type | Indexed type `FrontmatterFormat` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:10-13] |
| `WikiFrontmatter` | class | Indexed class `WikiFrontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:16-30] |
| `WikiFrontmatter::empty` | method | Indexed method `WikiFrontmatter::empty` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:33-48] |
| `WikiFrontmatter::as_json` | method | Indexed method `WikiFrontmatter::as_json` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:51-115] |
| `ParsedFrontmatter` | class | Indexed class `ParsedFrontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:119-125] |
| `FrontmatterError` | class | Indexed class `FrontmatterError` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:128-130] |
| `FrontmatterError::fmt` | method | Indexed method `FrontmatterError::fmt` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:133-135] |
| `parse_frontmatter` | function | Indexed function `parse_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:140-170] |
| `mark_stale_markdown` | function | Indexed function `mark_stale_markdown` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:173-191] |
| `FrontmatterError::new` | method | Indexed method `FrontmatterError::new` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:194-198] |
| `OpeningDelimiter` | class | Indexed class `OpeningDelimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:201-205] |
| `opening_delimiter` | function | Indexed function `opening_delimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:207-221] |
| `delimiter_content_start` | function | Indexed function `delimiter_content_start` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:223-232] |
| `find_closing_delimiter` | function | Indexed function `find_closing_delimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:234-264] |
| `parse_metadata` | function | Indexed function `parse_metadata` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:266-286] |
| `serialize_yaml_frontmatter` | function | Indexed function `serialize_yaml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:289-303] |
| `serialize_toml_frontmatter` | function | Indexed function `serialize_toml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:306-314] |
| `parse_yaml` | function | Indexed function `parse_yaml` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:316-329] |
| `parse_toml` | function | Indexed function `parse_toml` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:331-344] |
| `frontmatter_from_object` | function | Indexed function `frontmatter_from_object` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:346-394] |
| `string_value` | function | Indexed function `string_value` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:396-398] |
| `string_list` | function | Indexed function `string_list` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:400-406] |
| `string_value_str` | function | Indexed function `string_value_str` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:408-415] |
| `tag_list` | function | Indexed function `tag_list` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:419-434] |
| `parse_source_kind` | function | Indexed function `parse_source_kind` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:436-450] |
| `preserves_unknown_frontmatter` | function | Indexed function `preserves_unknown_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:457-524] |
| `legacy_source_files_remain_unknown_metadata` | function | Indexed function `legacy_source_files_remain_unknown_metadata` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:527-546] |
| `frontmatter_migration_parses_shared_contract_keys` | function | Indexed function `frontmatter_migration_parses_shared_contract_keys` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:549-578] |
| `codewiki_contract_golden_page_parses_into_contract_fields` | function | Indexed function `codewiki_contract_golden_page_parses_into_contract_fields` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:581-626] |
| `change_triggered_refresh_marks_page_stale_with_reason` | function | Indexed function `change_triggered_refresh_marks_page_stale_with_reason` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:629-659] |
| `change_triggered_refresh_preserves_toml_frontmatter` | function | Indexed function `change_triggered_refresh_preserves_toml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:662-691] |

