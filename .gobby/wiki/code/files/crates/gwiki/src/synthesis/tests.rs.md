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

# crates/gwiki/src/synthesis/tests.rs

Module: [[code/modules/crates/gwiki/src/synthesis|crates/gwiki/src/synthesis]]

## Purpose

This file contains unit tests for the synthesis layer in `gwiki`, covering page creation and overwrite behavior, slug generation, article/source path allocation, path-safety checks, and YAML scalar escaping. Together the tests verify that synthesized content is written atomically and only within the allowed wiki root, that existing human-authored pages are protected unless merge intent is explicit, and that helper formatting and naming functions handle collisions and special characters correctly.
[crates/gwiki/src/synthesis/tests.rs:15-42]
[crates/gwiki/src/synthesis/tests.rs:45-67]
[crates/gwiki/src/synthesis/tests.rs:70-75]
[crates/gwiki/src/synthesis/tests.rs:78-91]
[crates/gwiki/src/synthesis/tests.rs:94-130]

## API Symbols

- `existing_page_requires_merge_intent` (function) component `existing_page_requires_merge_intent [function]` (`713a4c1d-6940-566f-afcb-3ca7ba69b958`) lines 15-42 [crates/gwiki/src/synthesis/tests.rs:15-42]
  - Signature: `fn existing_page_requires_merge_intent() {`
  - Purpose: Verifies that 'write_synthesized_page' rejects overwriting an existing page under 'WritePolicy::RequireMergeIntent' with a 'WikiError::InvalidInput' on 'write_intent', and leaves the original file contents unchanged. [crates/gwiki/src/synthesis/tests.rs:15-42]
- `synthesized_page_write_classifies_create_and_overwrite_atomically` (function) component `synthesized_page_write_classifies_create_and_overwrite_atomically [function]` (`e2fd588c-ce7b-51ff-9d77-f845016d4936`) lines 45-67 [crates/gwiki/src/synthesis/tests.rs:45-67]
  - Signature: `fn synthesized_page_write_classifies_create_and_overwrite_atomically() {`
  - Purpose: Verifies that 'write_synthesized_page' returns 'PageWriteKind::Created' on the first write and 'PageWriteKind::Overwritten' on a subsequent write to the same path under 'AllowOverwriteAfterMerge', while leaving the file contents as the synthesized markdown. [crates/gwiki/src/synthesis/tests.rs:45-67]
- `slugify_unique_falls_back_after_bounded_suffixes` (function) component `slugify_unique_falls_back_after_bounded_suffixes [function]` (`acb552ba-1c4d-52bc-9716-d73c66665457`) lines 70-75 [crates/gwiki/src/synthesis/tests.rs:70-75]
  - Signature: `fn slugify_unique_falls_back_after_bounded_suffixes() {`
  - Purpose: Verifies that 'slugify_unique("Collision", |_| true)' returns a slug beginning with 'collision-' and extending beyond that prefix after exhausting bounded suffix attempts. [crates/gwiki/src/synthesis/tests.rs:70-75]
- `source_page_paths_reserve_article_path` (function) component `source_page_paths_reserve_article_path [function]` (`74455708-d8b5-5b45-bcd5-c3269e570478`) lines 78-91 [crates/gwiki/src/synthesis/tests.rs:78-91]
  - Signature: `fn source_page_paths_reserve_article_path() {`
  - Purpose: Creates a temporary source tree and verifies that 'source_page_paths' does not return the reserved article path itself, instead placing the generated source path under 'knowledge/sources' within the temp directory. [crates/gwiki/src/synthesis/tests.rs:78-91]
- `synthesized_article_rejects_escaping_target_path` (function) component `synthesized_article_rejects_escaping_target_path [function]` (`b6403911-944c-5069-977b-cc33a95054d1`) lines 94-130 [crates/gwiki/src/synthesis/tests.rs:94-130]
  - Signature: `fn synthesized_article_rejects_escaping_target_path() {`
  - Purpose: Verifies that 'synthesize_article' rejects a target 'article_path' that escapes the provided temp directory by returning 'WikiError::InvalidInput' for the 'article_path' field. [crates/gwiki/src/synthesis/tests.rs:94-130]
- `synthesized_writer_rejects_escaping_page_path_before_write` (function) component `synthesized_writer_rejects_escaping_page_path_before_write [function]` (`aaa752b8-50ee-5afd-a991-01526f4eca10`) lines 133-161 [crates/gwiki/src/synthesis/tests.rs:133-161]
  - Signature: `fn synthesized_writer_rejects_escaping_page_path_before_write() {`
  - Purpose: Verifies that 'write_synthesized_page' rejects a 'SynthesizedPage' whose 'path' escapes the target root directory by returning 'WikiError::InvalidInput { field: "synthesized_page", .. }' and not creating the file outside the root. [crates/gwiki/src/synthesis/tests.rs:133-161]
- `synthesized_writer_rejects_symlinked_parent_before_create_dir_all` (function) component `synthesized_writer_rejects_symlinked_parent_before_create_dir_all [function]` (`233bda42-fb3c-5ffe-b219-475898bff7cf`) lines 165-191 [crates/gwiki/src/synthesis/tests.rs:165-191]
  - Signature: `fn synthesized_writer_rejects_symlinked_parent_before_create_dir_all() {`
  - Purpose: Ensures 'write_synthesized_page' rejects a synthesized page whose parent directory is a symlink escaping the target root, returning 'WikiError::InvalidInput' and not creating the file outside the root. [crates/gwiki/src/synthesis/tests.rs:165-191]
- `yaml_scalar_escapes_quoted_control_characters` (function) component `yaml_scalar_escapes_quoted_control_characters [function]` (`0c9c97b7-e2d7-5857-aac4-80d6339c4725`) lines 194-204 [crates/gwiki/src/synthesis/tests.rs:194-204]
  - Signature: `fn yaml_scalar_escapes_quoted_control_characters() {`
  - Purpose: Verifies that 'yaml_scalar' emits a double-quoted YAML scalar, preserving plain text unchanged while escaping backslashes, quotes, newline, carriage return, tab, and non-printable/control characters as YAML escape sequences. [crates/gwiki/src/synthesis/tests.rs:194-204]

