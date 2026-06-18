---
title: crates/ghook/src/terminal_context.rs
type: code_file
provenance:
- file: crates/ghook/src/terminal_context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/terminal_context.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/terminal_context.rs` exposes 17 indexed API symbols.

## How it fits

`crates/ghook/src/terminal_context.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `capture` | function | Indexed function `capture` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:18-23] |
| `enabled_for_hook` | function | Indexed function `enabled_for_hook` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:25-32] |
| `build_context` | function | Indexed function `build_context` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:34-65] |
| `inject` | function | Indexed function `inject` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:71-77] |
| `env_or_null` | function | Indexed function `env_or_null` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:79-84] |
| `parent_pid_or_null` | function | Indexed function `parent_pid_or_null` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:86-102] |
| `tty_name_or_null` | function | Indexed function `tty_name_or_null` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:104-126] |
| `is_valid_tmux_pane` | function | Indexed function `is_valid_tmux_pane` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:128-133] |
| `parse_tmux_socket_path` | function | Indexed function `parse_tmux_socket_path` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:138-145] |
| `parse_socket_path_extracts_leading_segment` | function | Indexed function `parse_socket_path_extracts_leading_segment` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:153-158] |
| `parse_socket_path_handles_empty` | function | Indexed function `parse_socket_path_handles_empty` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:161-164] |
| `build_context_sets_tmux_pane_verbatim` | function | Indexed function `build_context_sets_tmux_pane_verbatim` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:167-171] |
| `build_context_nulls_missing_empty_or_invalid_tmux_fields` | function | Indexed function `build_context_nulls_missing_empty_or_invalid_tmux_fields` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:174-187] |
| `valid_tmux_pane_matches_daemon_contract` | function | Indexed function `valid_tmux_pane_matches_daemon_contract` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:190-198] |
| `inject_respects_existing_terminal_context` | function | Indexed function `inject_respects_existing_terminal_context` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:201-209] |
| `inject_no_op_on_non_object` | function | Indexed function `inject_no_op_on_non_object` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:212-216] |
| `capture_emits_expected_keys` | function | Indexed function `capture_emits_expected_keys` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:219-237] |

