---
title: crates/gcode/src/commands/codewiki/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/tests.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The file contains the unit test `documents_code_and_config_excludes_content_only_by_default` crates/gcode/src/commands/codewiki/tests.rs:26-47. This test verifies that the `should_document_file` helper includes code and structured configuration files while excluding content-only files unless the override parameter is explicitly set to true.

## How it fits

It declares a wide array of submodules, such as `support`, `ai`, `architecture`, `incremental`, and `io_safety` crates/gcode/src/commands/codewiki/tests.rs:7-24, which keep the testing concerns separated. The test flow evaluates `should_document_file` against file paths like `crates/gcode/src/lib.rs` and `README.md` crates/gcode/src/commands/codewiki/tests.rs:28-36, ensuring that the command logic correctly routes code, configuration, and documentation assets during a codewiki execution. [crates/gcode/src/commands/codewiki/tests.rs:26-47]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `documents_code_and_config_excludes_content_only_by_default` | function | Verifies that 'should_document_file' includes code and structured config files by default, excludes content-only files unless 'include_docs' is 'true', and respects the override for markdown content. [crates/gcode/src/commands/codewiki/tests.rs:26-47] |

