---
title: crates/ghook/src/statusline.rs
type: code_file
provenance:
- file: crates/ghook/src/statusline.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/statusline.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/statusline.rs` exposes 22 indexed API symbols.

## How it fits

`crates/ghook/src/statusline.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `is_statusline_hook` | function | Indexed function `is_statusline_hook` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:25-27] |
| `handle` | function | Indexed function `handle` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:29-35] |
| `handle_with` | function | Indexed function `handle_with` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:37-67] |
| `extract_payload` | function | Indexed function `extract_payload` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:69-104] |
| `post_to_daemon_best_effort` | function | Indexed function `post_to_daemon_best_effort` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:106-119] |
| `forward_downstream` | function | Indexed function `forward_downstream` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:121-168] |
| `terminate_downstream` | function | Indexed function `terminate_downstream` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:170-174] |
| `terminate_downstream_group` | function | Indexed function `terminate_downstream_group` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:177-183] |
| `terminate_downstream_group` | function | Indexed function `terminate_downstream_group` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:186] |
| `downstream_shell_command` | function | Indexed function `downstream_shell_command` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:189-194] |
| `downstream_shell_command` | function | Indexed function `downstream_shell_command` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:197-201] |
| `recognizes_only_claude_statusline_hook` | function | Indexed function `recognizes_only_claude_statusline_hook` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:217-222] |
| `extract_payload_matches_full_golden_fixture` | function | Indexed function `extract_payload_matches_full_golden_fixture` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:225-229] |
| `extract_payload_matches_default_golden_fixture` | function | Indexed function `extract_payload_matches_default_golden_fixture` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:232-236] |
| `extract_payload_returns_none_without_session_id` | function | Indexed function `extract_payload_returns_none_without_session_id` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:239-245] |
| `malformed_json_exits_success_without_stdout` | function | Indexed function `malformed_json_exits_success_without_stdout` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:248-253] |
| `posts_statusline_payload_to_daemon_endpoint` | function | Indexed function `posts_statusline_payload_to_daemon_endpoint` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:256-283] |
| `statusline_post_honors_gobby_daemon_url_override` | function | Indexed function `statusline_post_honors_gobby_daemon_url_override` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:286-310] |
| `downstream_stdout_passthrough_preserves_bytes` | function | Indexed function `downstream_stdout_passthrough_preserves_bytes` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:313-324] |
| `downstream_large_stdout_returns_full_output_quickly` | function | Indexed function `downstream_large_stdout_returns_full_output_quickly` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:327-344] |
| `downstream_timeout_returns_before_six_seconds` | function | Indexed function `downstream_timeout_returns_before_six_seconds` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:347-371] |
| `downstream_timeout_kills_pipeline_survivors_holding_stdout` | function | Indexed function `downstream_timeout_kills_pipeline_survivors_holding_stdout` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:374-397] |

