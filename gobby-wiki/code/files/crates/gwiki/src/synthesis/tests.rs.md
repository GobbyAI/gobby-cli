---
title: crates/gwiki/src/synthesis/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/tests.rs
  ranges:
  - 15-42
  - 45-67
  - 70-75
  - 78-91
  - 94-130
  - 133-161
  - 165-191
  - 194-204
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/synthesis/tests.rs:15-42](crates/gwiki/src/synthesis/tests.rs#L15-L42), [crates/gwiki/src/synthesis/tests.rs:45-67](crates/gwiki/src/synthesis/tests.rs#L45-L67), [crates/gwiki/src/synthesis/tests.rs:70-75](crates/gwiki/src/synthesis/tests.rs#L70-L75), [crates/gwiki/src/synthesis/tests.rs:78-91](crates/gwiki/src/synthesis/tests.rs#L78-L91), [crates/gwiki/src/synthesis/tests.rs:94-130](crates/gwiki/src/synthesis/tests.rs#L94-L130), [crates/gwiki/src/synthesis/tests.rs:133-161](crates/gwiki/src/synthesis/tests.rs#L133-L161), [crates/gwiki/src/synthesis/tests.rs:165-191](crates/gwiki/src/synthesis/tests.rs#L165-L191), [crates/gwiki/src/synthesis/tests.rs:194-204](crates/gwiki/src/synthesis/tests.rs#L194-L204)

</details>

# crates/gwiki/src/synthesis/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Integration tests for the wiki synthesis layer. The file checks that synthesized pages respect write policy rules for existing content, distinguish create versus overwrite results correctly, and generate unique slugs with bounded fallback behavior. It also verifies path-safety controls around source page locations, article synthesis, and page writing prevent escaping the wiki root or following unsafe symlinked parents, and it confirms YAML scalar rendering properly escapes quoted control characters.
[crates/gwiki/src/synthesis/tests.rs:15-42]
[crates/gwiki/src/synthesis/tests.rs:45-67]
[crates/gwiki/src/synthesis/tests.rs:70-75]
[crates/gwiki/src/synthesis/tests.rs:78-91]
[crates/gwiki/src/synthesis/tests.rs:94-130]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `existing_page_requires_merge_intent` | function | `fn existing_page_requires_merge_intent() {` | `existing_page_requires_merge_intent [function]` | `713a4c1d-6940-566f-afcb-3ca7ba69b958` | 15-42 [crates/gwiki/src/synthesis/tests.rs:15-42] | Indexed function `existing_page_requires_merge_intent` in `crates/gwiki/src/synthesis/tests.rs`. [crates/gwiki/src/synthesis/tests.rs:15-42] |
| `synthesized_page_write_classifies_create_and_overwrite_atomically` | function | `fn synthesized_page_write_classifies_create_and_overwrite_atomically() {` | `synthesized_page_write_classifies_create_and_overwrite_atomically [function]` | `e2fd588c-ce7b-51ff-9d77-f845016d4936` | 45-67 [crates/gwiki/src/synthesis/tests.rs:45-67] | Indexed function `synthesized_page_write_classifies_create_and_overwrite_atomically` in `crates/gwiki/src/synthesis/tests.rs`. [crates/gwiki/src/synthesis/tests.rs:45-67] |
| `slugify_unique_falls_back_after_bounded_suffixes` | function | `fn slugify_unique_falls_back_after_bounded_suffixes() {` | `slugify_unique_falls_back_after_bounded_suffixes [function]` | `acb552ba-1c4d-52bc-9716-d73c66665457` | 70-75 [crates/gwiki/src/synthesis/tests.rs:70-75] | Indexed function `slugify_unique_falls_back_after_bounded_suffixes` in `crates/gwiki/src/synthesis/tests.rs`. [crates/gwiki/src/synthesis/tests.rs:70-75] |
| `source_page_paths_reserve_article_path` | function | `fn source_page_paths_reserve_article_path() {` | `source_page_paths_reserve_article_path [function]` | `74455708-d8b5-5b45-bcd5-c3269e570478` | 78-91 [crates/gwiki/src/synthesis/tests.rs:78-91] | Indexed function `source_page_paths_reserve_article_path` in `crates/gwiki/src/synthesis/tests.rs`. [crates/gwiki/src/synthesis/tests.rs:78-91] |
| `synthesized_article_rejects_escaping_target_path` | function | `fn synthesized_article_rejects_escaping_target_path() {` | `synthesized_article_rejects_escaping_target_path [function]` | `b6403911-944c-5069-977b-cc33a95054d1` | 94-130 [crates/gwiki/src/synthesis/tests.rs:94-130] | Indexed function `synthesized_article_rejects_escaping_target_path` in `crates/gwiki/src/synthesis/tests.rs`. [crates/gwiki/src/synthesis/tests.rs:94-130] |
| `synthesized_writer_rejects_escaping_page_path_before_write` | function | `fn synthesized_writer_rejects_escaping_page_path_before_write() {` | `synthesized_writer_rejects_escaping_page_path_before_write [function]` | `aaa752b8-50ee-5afd-a991-01526f4eca10` | 133-161 [crates/gwiki/src/synthesis/tests.rs:133-161] | Indexed function `synthesized_writer_rejects_escaping_page_path_before_write` in `crates/gwiki/src/synthesis/tests.rs`. [crates/gwiki/src/synthesis/tests.rs:133-161] |
| `synthesized_writer_rejects_symlinked_parent_before_create_dir_all` | function | `fn synthesized_writer_rejects_symlinked_parent_before_create_dir_all() {` | `synthesized_writer_rejects_symlinked_parent_before_create_dir_all [function]` | `233bda42-fb3c-5ffe-b219-475898bff7cf` | 165-191 [crates/gwiki/src/synthesis/tests.rs:165-191] | Indexed function `synthesized_writer_rejects_symlinked_parent_before_create_dir_all` in `crates/gwiki/src/synthesis/tests.rs`. [crates/gwiki/src/synthesis/tests.rs:165-191] |
| `yaml_scalar_escapes_quoted_control_characters` | function | `fn yaml_scalar_escapes_quoted_control_characters() {` | `yaml_scalar_escapes_quoted_control_characters [function]` | `0c9c97b7-e2d7-5857-aac4-80d6339c4725` | 194-204 [crates/gwiki/src/synthesis/tests.rs:194-204] | Indexed function `yaml_scalar_escapes_quoted_control_characters` in `crates/gwiki/src/synthesis/tests.rs`. [crates/gwiki/src/synthesis/tests.rs:194-204] |
