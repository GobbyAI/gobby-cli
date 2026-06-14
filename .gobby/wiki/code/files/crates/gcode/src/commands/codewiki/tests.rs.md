---
title: crates/gcode/src/commands/codewiki/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/tests.rs
  ranges:
  - 24-42
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/tests.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file contains tests for the codewiki command’s file-selection and related IO helpers. It pulls in shared support plus topic-specific test modules, and its main check verifies that `should_document_file` documents code and structured config files by default, skips content-only files like Markdown and licenses unless `include_docs` is enabled, and then includes those docs files when requested. [crates/gcode/src/commands/codewiki/tests.rs:24-42]

## API Symbols

- `documents_code_and_config_excludes_content_only_by_default` (function) component `documents_code_and_config_excludes_content_only_by_default [function]` (`33b1829b-f941-5402-8436-e1b029711bfa`) lines 24-42 [crates/gcode/src/commands/codewiki/tests.rs:24-42]
  - Signature: `fn documents_code_and_config_excludes_content_only_by_default() {`
  - Purpose: It verifies that 'should_document_file' includes code and structured config files by default, excludes content-only files like Markdown and licenses unless 'include_docs' is enabled, and returns 'true' for those docs files when explicitly included. [crates/gcode/src/commands/codewiki/tests.rs:24-42]

