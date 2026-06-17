---
title: crates/gcode/src/commands/codewiki/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/tests.rs
  ranges:
  - 25-46
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/tests.rs:25-46](crates/gcode/src/commands/codewiki/tests.rs#L25-L46)

</details>

# crates/gcode/src/commands/codewiki/tests.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This test file exercises the `codewiki` command’s file-selection rules. It imports supporting I/O helpers and a set of sibling test modules, then defines a focused test that verifies `should_document_file` includes source code and structured config files by default, excludes content-only files like Markdown and license text unless `--include-docs` is enabled, and thereby documents the intended boundary between code/config documentation and gwiki-style content. [crates/gcode/src/commands/codewiki/tests.rs:25-46]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `documents_code_and_config_excludes_content_only_by_default` | function | `fn documents_code_and_config_excludes_content_only_by_default() {` | `documents_code_and_config_excludes_content_only_by_default [function]` | `fbc69530-db73-580d-8f56-dead9bd3be6f` | 25-46 [crates/gcode/src/commands/codewiki/tests.rs:25-46] | Indexed function `documents_code_and_config_excludes_content_only_by_default` in `crates/gcode/src/commands/codewiki/tests.rs`. [crates/gcode/src/commands/codewiki/tests.rs:25-46] |
