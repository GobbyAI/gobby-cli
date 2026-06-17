---
title: crates/ghook/src/terminal_context.rs
type: code_file
provenance:
- file: crates/ghook/src/terminal_context.rs
  ranges:
  - 18-23
  - 25-32
  - 34-65
  - 71-77
  - 79-84
  - 86-102
  - 104-126
  - 128-133
  - 138-145
  - 153-158
  - 161-164
  - 167-171
  - 174-187
  - 190-198
  - 201-209
  - 212-216
  - 219-237
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/terminal_context.rs:18-23](crates/ghook/src/terminal_context.rs#L18-L23), [crates/ghook/src/terminal_context.rs:25-32](crates/ghook/src/terminal_context.rs#L25-L32), [crates/ghook/src/terminal_context.rs:34-65](crates/ghook/src/terminal_context.rs#L34-L65), [crates/ghook/src/terminal_context.rs:71-77](crates/ghook/src/terminal_context.rs#L71-L77), [crates/ghook/src/terminal_context.rs:79-84](crates/ghook/src/terminal_context.rs#L79-L84), [crates/ghook/src/terminal_context.rs:86-102](crates/ghook/src/terminal_context.rs#L86-L102), [crates/ghook/src/terminal_context.rs:104-126](crates/ghook/src/terminal_context.rs#L104-L126), [crates/ghook/src/terminal_context.rs:128-133](crates/ghook/src/terminal_context.rs#L128-L133), [crates/ghook/src/terminal_context.rs:138-145](crates/ghook/src/terminal_context.rs#L138-L145), [crates/ghook/src/terminal_context.rs:153-158](crates/ghook/src/terminal_context.rs#L153-L158), [crates/ghook/src/terminal_context.rs:161-164](crates/ghook/src/terminal_context.rs#L161-L164), [crates/ghook/src/terminal_context.rs:167-171](crates/ghook/src/terminal_context.rs#L167-L171), [crates/ghook/src/terminal_context.rs:174-187](crates/ghook/src/terminal_context.rs#L174-L187), [crates/ghook/src/terminal_context.rs:190-198](crates/ghook/src/terminal_context.rs#L190-L198), [crates/ghook/src/terminal_context.rs:201-209](crates/ghook/src/terminal_context.rs#L201-L209), [crates/ghook/src/terminal_context.rs:212-216](crates/ghook/src/terminal_context.rs#L212-L216), [crates/ghook/src/terminal_context.rs:219-237](crates/ghook/src/terminal_context.rs#L219-L237)

</details>

# crates/ghook/src/terminal_context.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Builds and injects a `terminal_context` object for hook/session-start handling, capturing process and terminal metadata so the daemon can reconcile spawned terminal agents. `capture` and `build_context` assemble `parent_pid`, `tty`, `tmux_*`, `TERM_PROGRAM`, and `GOBBY_*` fields; helper functions validate tmux pane/socket values, `enabled_for_hook` gates this logic to `session-start`, and `inject` inserts the context without overwriting existing non-object data.
[crates/ghook/src/terminal_context.rs:18-23]
[crates/ghook/src/terminal_context.rs:25-32]
[crates/ghook/src/terminal_context.rs:34-65]
[crates/ghook/src/terminal_context.rs:71-77]
[crates/ghook/src/terminal_context.rs:79-84]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `capture` | function | `pub fn capture() -> Value {` | `capture [function]` | `032ab45d-17a0-5053-a16d-21bf4a58cdb3` | 18-23 [crates/ghook/src/terminal_context.rs:18-23] | Indexed function `capture` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:18-23] |
| `enabled_for_hook` | function | `pub fn enabled_for_hook(hook_type: &str) -> bool {` | `enabled_for_hook [function]` | `4be0ac35-4a63-5eaf-9eb8-f26f60ede61d` | 25-32 [crates/ghook/src/terminal_context.rs:25-32] | Indexed function `enabled_for_hook` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:25-32] |
| `build_context` | function | `fn build_context(tmux: Option<&str>, tmux_pane: Option<&str>) -> Value {` | `build_context [function]` | `2e89661f-cc0d-5e6c-a0a0-8d2b5c0a111e` | 34-65 [crates/ghook/src/terminal_context.rs:34-65] | Indexed function `build_context` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:34-65] |
| `inject` | function | `pub fn inject(input_data: &mut Value) {` | `inject [function]` | `d242772e-aa15-5f25-88e4-a6d95061eebd` | 71-77 [crates/ghook/src/terminal_context.rs:71-77] | Indexed function `inject` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:71-77] |
| `env_or_null` | function | `fn env_or_null(key: &str) -> Value {` | `env_or_null [function]` | `fb84c468-93b9-5ab0-8408-49a199163341` | 79-84 [crates/ghook/src/terminal_context.rs:79-84] | Indexed function `env_or_null` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:79-84] |
| `parent_pid_or_null` | function | `fn parent_pid_or_null() -> Value {` | `parent_pid_or_null [function]` | `9a03c200-a64a-5b13-8149-3aad1b137c89` | 86-102 [crates/ghook/src/terminal_context.rs:86-102] | Indexed function `parent_pid_or_null` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:86-102] |
| `tty_name_or_null` | function | `fn tty_name_or_null() -> Value {` | `tty_name_or_null [function]` | `70194d1e-f9d9-5d3f-a7f0-91efdfaf18a8` | 104-126 [crates/ghook/src/terminal_context.rs:104-126] | Indexed function `tty_name_or_null` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:104-126] |
| `is_valid_tmux_pane` | function | `fn is_valid_tmux_pane(pane: &str) -> bool {` | `is_valid_tmux_pane [function]` | `ba1c1670-6c09-5a0f-9888-a0b28c8418bb` | 128-133 [crates/ghook/src/terminal_context.rs:128-133] | Indexed function `is_valid_tmux_pane` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:128-133] |
| `parse_tmux_socket_path` | function | `fn parse_tmux_socket_path(tmux_env: &str) -> Option<String> {` | `parse_tmux_socket_path [function]` | `0897e27e-b9c0-58f8-8cfd-fe2c0131f65a` | 138-145 [crates/ghook/src/terminal_context.rs:138-145] | Indexed function `parse_tmux_socket_path` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:138-145] |
| `parse_socket_path_extracts_leading_segment` | function | `fn parse_socket_path_extracts_leading_segment() {` | `parse_socket_path_extracts_leading_segment [function]` | `d065c630-b5fd-56ab-81b2-6976a000ef19` | 153-158 [crates/ghook/src/terminal_context.rs:153-158] | Indexed function `parse_socket_path_extracts_leading_segment` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:153-158] |
| `parse_socket_path_handles_empty` | function | `fn parse_socket_path_handles_empty() {` | `parse_socket_path_handles_empty [function]` | `50b499f0-980b-5ef0-b787-91b728960634` | 161-164 [crates/ghook/src/terminal_context.rs:161-164] | Indexed function `parse_socket_path_handles_empty` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:161-164] |
| `build_context_sets_tmux_pane_verbatim` | function | `fn build_context_sets_tmux_pane_verbatim() {` | `build_context_sets_tmux_pane_verbatim [function]` | `33abafd6-98c6-5317-a520-c2a754c02cb9` | 167-171 [crates/ghook/src/terminal_context.rs:167-171] | Indexed function `build_context_sets_tmux_pane_verbatim` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:167-171] |
| `build_context_nulls_missing_empty_or_invalid_tmux_fields` | function | `fn build_context_nulls_missing_empty_or_invalid_tmux_fields() {` | `build_context_nulls_missing_empty_or_invalid_tmux_fields [function]` | `7c984ae4-de71-5f3b-89a9-07defc4ae74a` | 174-187 [crates/ghook/src/terminal_context.rs:174-187] | Indexed function `build_context_nulls_missing_empty_or_invalid_tmux_fields` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:174-187] |
| `valid_tmux_pane_matches_daemon_contract` | function | `fn valid_tmux_pane_matches_daemon_contract() {` | `valid_tmux_pane_matches_daemon_contract [function]` | `4447068e-b3cc-512a-88ff-2405163f28d6` | 190-198 [crates/ghook/src/terminal_context.rs:190-198] | Indexed function `valid_tmux_pane_matches_daemon_contract` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:190-198] |
| `inject_respects_existing_terminal_context` | function | `fn inject_respects_existing_terminal_context() {` | `inject_respects_existing_terminal_context [function]` | `f629e177-1cde-5057-b69c-4f3032b9864a` | 201-209 [crates/ghook/src/terminal_context.rs:201-209] | Indexed function `inject_respects_existing_terminal_context` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:201-209] |
| `inject_no_op_on_non_object` | function | `fn inject_no_op_on_non_object() {` | `inject_no_op_on_non_object [function]` | `8d707487-2178-5ece-8d22-7bd6cd8e886f` | 212-216 [crates/ghook/src/terminal_context.rs:212-216] | Indexed function `inject_no_op_on_non_object` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:212-216] |
| `capture_emits_expected_keys` | function | `fn capture_emits_expected_keys() {` | `capture_emits_expected_keys [function]` | `c8c3ae50-4e71-5ac5-b79c-8f3f4caa9b4b` | 219-237 [crates/ghook/src/terminal_context.rs:219-237] | Indexed function `capture_emits_expected_keys` in `crates/ghook/src/terminal_context.rs`. [crates/ghook/src/terminal_context.rs:219-237] |
