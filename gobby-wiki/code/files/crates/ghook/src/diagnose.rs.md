---
title: crates/ghook/src/diagnose.rs
type: code_file
provenance:
- file: crates/ghook/src/diagnose.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/diagnose.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/diagnose.rs` exposes 20 indexed API symbols.

## How it fits

`crates/ghook/src/diagnose.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DiagnoseOutput` | class | Indexed class `DiagnoseOutput` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:15-32] |
| `InstallSidecar` | class | Indexed class `InstallSidecar` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:42-45] |
| `read_install_provenance` | function | Indexed function `read_install_provenance` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:51-60] |
| `install_provenance_for_running_binary` | function | Indexed function `install_provenance_for_running_binary` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:62-70] |
| `diagnose` | function | Indexed function `diagnose` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:72-120] |
| `unknown_cli_marked_not_recognized` | function | Indexed function `unknown_cli_marked_not_recognized` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:128-134] |
| `claude_session_start_is_critical_with_terminal_context` | function | Indexed function `claude_session_start_is_critical_with_terminal_context` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:137-143] |
| `codex_pre_tool_use_noncritical_without_terminal_context` | function | Indexed function `codex_pre_tool_use_noncritical_without_terminal_context` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:146-152] |
| `droid_session_start_is_recognized_noncritical_with_terminal_context_enabled` | function | Indexed function `droid_session_start_is_recognized_noncritical_with_terminal_context_enabled` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:155-161] |
| `grok_session_start_is_recognized_critical_with_terminal_context_enabled` | function | Indexed function `grok_session_start_is_recognized_critical_with_terminal_context_enabled` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:164-170] |
| `grok_pre_tool_use_is_recognized_noncritical_without_terminal_context` | function | Indexed function `grok_pre_tool_use_is_recognized_noncritical_without_terminal_context` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:173-179] |
| `compile_v2_schema` | function | Indexed function `compile_v2_schema` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:181-188] |
| `assert_validates` | function | Indexed function `assert_validates` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:190-195] |
| `diagnose_output_validates_against_v2_schema` | function | Indexed function `diagnose_output_validates_against_v2_schema` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:198-210] |
| `diagnose_output_for_unknown_cli_validates` | function | Indexed function `diagnose_output_for_unknown_cli_validates` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:213-225] |
| `schema_version_is_two` | function | Indexed function `schema_version_is_two` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:228-231] |
| `install_provenance_absent_when_no_sidecar` | function | Indexed function `install_provenance_absent_when_no_sidecar` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:234-239] |
| `install_provenance_read_from_sidecar` | function | Indexed function `install_provenance_read_from_sidecar` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:242-264] |
| `install_provenance_partial_sidecar_returns_present_fields` | function | Indexed function `install_provenance_partial_sidecar_returns_present_fields` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:267-274] |
| `install_provenance_malformed_json_collapses_to_none` | function | Indexed function `install_provenance_malformed_json_collapses_to_none` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:277-284] |

