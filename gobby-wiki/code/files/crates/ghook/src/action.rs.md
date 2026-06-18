---
title: crates/ghook/src/action.rs
type: code_file
provenance:
- file: crates/ghook/src/action.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/action.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/action.rs` exposes 28 indexed API symbols.

## How it fits

`crates/ghook/src/action.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `HookAction` | class | Indexed class `HookAction` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:9-13] |
| `continue_action` | function | Indexed function `continue_action` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:15-21] |
| `emit_empty_json` | function | Indexed function `emit_empty_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:23-25] |
| `emit_action` | function | Indexed function `emit_action` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:27-35] |
| `action_from_success_response` | function | Indexed function `action_from_success_response` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:37-107] |
| `action_from_droid_success` | function | Indexed function `action_from_droid_success` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:109-128] |
| `action_from_failure` | function | Indexed function `action_from_failure` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:130-190] |
| `is_blocked` | function | Indexed function `is_blocked` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:192-214] |
| `extract_reason` | function | Indexed function `extract_reason` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:216-244] |
| `action_from_success_forwards_sessionstart_context_json` | function | Indexed function `action_from_success_forwards_sessionstart_context_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:253-274] |
| `action_from_success_treats_codex_pretool_deny_as_json_block` | function | Indexed function `action_from_success_treats_codex_pretool_deny_as_json_block` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:277-293] |
| `action_from_success_surfaces_nested_permission_decision_reason` | function | Indexed function `action_from_success_surfaces_nested_permission_decision_reason` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:296-312] |
| `action_from_success_preserves_additional_context_on_claude_block` | function | Indexed function `action_from_success_preserves_additional_context_on_claude_block` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:315-332] |
| `action_from_success_preserves_user_prompt_submit_block_json` | function | Indexed function `action_from_success_preserves_user_prompt_submit_block_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:335-353] |
| `action_from_success_treats_stop_block_as_exit_two` | function | Indexed function `action_from_success_treats_stop_block_as_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:356-372] |
| `action_from_success_treats_lowercase_stop_block_as_exit_two` | function | Indexed function `action_from_success_treats_lowercase_stop_block_as_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:375-391] |
| `action_from_success_keeps_non_stop_grok_block_as_json` | function | Indexed function `action_from_success_keeps_non_stop_grok_block_as_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:394-408] |
| `action_from_success_claude_hard_stop_exits_two` | function | Indexed function `action_from_success_claude_hard_stop_exits_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:411-427] |
| `action_from_success_claude_stop_with_permission_deny_no_exit_two` | function | Indexed function `action_from_success_claude_stop_with_permission_deny_no_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:430-441] |
| `action_from_success_claude_continue_false_without_reason_does_not_exit_two` | function | Indexed function `action_from_success_claude_continue_false_without_reason_does_not_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:444-450] |
| `action_from_success_treats_droid_continue_false_as_exit_two_with_json` | function | Indexed function `action_from_success_treats_droid_continue_false_as_exit_two_with_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:453-469] |
| `action_from_success_preserves_droid_block_json_without_exit_two` | function | Indexed function `action_from_success_preserves_droid_block_json_without_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:472-486] |
| `action_from_failure_blocks_critical_hooks` | function | Indexed function `action_from_failure_blocks_critical_hooks` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:489-504] |
| `action_from_failure_returns_json_for_noncritical_hooks` | function | Indexed function `action_from_failure_returns_json_for_noncritical_hooks` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:507-520] |
| `action_from_failure_treats_timeout_like_python` | function | Indexed function `action_from_failure_treats_timeout_like_python` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:523-533] |
| `action_from_failure_treats_connect_on_critical_hook_as_exit_two` | function | Indexed function `action_from_failure_treats_connect_on_critical_hook_as_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:536-549] |
| `action_from_failure_returns_stderr_for_droid_transport_errors` | function | Indexed function `action_from_failure_returns_stderr_for_droid_transport_errors` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:552-565] |
| `is_blocked_matches_dispatcher_patterns` | function | Indexed function `is_blocked_matches_dispatcher_patterns` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:568-577] |

