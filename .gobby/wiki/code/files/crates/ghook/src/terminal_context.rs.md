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

# crates/ghook/src/terminal_context.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/terminal_context.rs` exposes 17 indexed API symbols.
[crates/ghook/src/terminal_context.rs:18-23]
[crates/ghook/src/terminal_context.rs:25-32]
[crates/ghook/src/terminal_context.rs:34-65]
[crates/ghook/src/terminal_context.rs:71-77]
[crates/ghook/src/terminal_context.rs:79-84]

## API Symbols

- `capture` (function) component `capture [function]` (`032ab45d-17a0-5053-a16d-21bf4a58cdb3`) lines 18-23 [crates/ghook/src/terminal_context.rs:18-23]
  - Signature: `pub fn capture() -> Value {`
  - Purpose: The `capture` function builds and returns a `Value` by passing optional string references derived from the `TMUX` and `TMUX_PANE` environment variables to `build_context`. [crates/ghook/src/terminal_context.rs:18-23]
- `enabled_for_hook` (function) component `enabled_for_hook [function]` (`4be0ac35-4a63-5eaf-9eb8-f26f60ede61d`) lines 25-32 [crates/ghook/src/terminal_context.rs:25-32]
  - Signature: `pub fn enabled_for_hook(hook_type: &str) -> bool {`
  - Purpose: Returns `true` if the normalized hook type (lowercase with hyphens and underscores removed) equals "sessionstart". [crates/ghook/src/terminal_context.rs:25-32]
- `build_context` (function) component `build_context [function]` (`2e89661f-cc0d-5e6c-a0a0-8d2b5c0a111e`) lines 34-65 [crates/ghook/src/terminal_context.rs:34-65]
  - Signature: `fn build_context(tmux: Option<&str>, tmux_pane: Option<&str>) -> Value {`
  - Purpose: Constructs a JSON Value object containing process and terminal environment context by validating optional tmux session/pane parameters and aggregating parent PID, TTY name, tmux socket path, terminal program, and gobby-related session identifiers. [crates/ghook/src/terminal_context.rs:34-65]
- `inject` (function) component `inject [function]` (`d242772e-aa15-5f25-88e4-a6d95061eebd`) lines 71-77 [crates/ghook/src/terminal_context.rs:71-77]
  - Signature: `pub fn inject(input_data: &mut Value) {`
  - Purpose: Mutates the input JSON object by inserting a 'terminal_context' key with the result of `capture()` if the key is not already present. [crates/ghook/src/terminal_context.rs:71-77]
- `env_or_null` (function) component `env_or_null [function]` (`fb84c468-93b9-5ab0-8408-49a199163341`) lines 79-84 [crates/ghook/src/terminal_context.rs:79-84]
  - Signature: `fn env_or_null(key: &str) -> Value {`
  - Purpose: Attempts to retrieve an environment variable by the given key, returning it as a `Value::String` on success or `Value::Null` on any error. [crates/ghook/src/terminal_context.rs:79-84]
- `parent_pid_or_null` (function) component `parent_pid_or_null [function]` (`9a03c200-a64a-5b13-8149-3aad1b137c89`) lines 86-102 [crates/ghook/src/terminal_context.rs:86-102]
  - Signature: `fn parent_pid_or_null() -> Value {`
  - Purpose: Returns the parent process ID via unsafe `libc::getppid()` on Unix systems or `Value::Null` on Windows due to the absence of a direct parent-PID syscall. [crates/ghook/src/terminal_context.rs:86-102]
- `tty_name_or_null` (function) component `tty_name_or_null [function]` (`70194d1e-f9d9-5d3f-a7f0-91efdfaf18a8`) lines 104-126 [crates/ghook/src/terminal_context.rs:104-126]
  - Signature: `fn tty_name_or_null() -> Value {`
  - Purpose: Returns the name of the terminal connected to file descriptor 0 (stdin) as a UTF-8 string on Unix systems, or null on Windows and failure cases. [crates/ghook/src/terminal_context.rs:104-126]
- `is_valid_tmux_pane` (function) component `is_valid_tmux_pane [function]` (`ba1c1670-6c09-5a0f-9888-a0b28c8418bb`) lines 128-133 [crates/ghook/src/terminal_context.rs:128-133]
  - Signature: `fn is_valid_tmux_pane(pane: &str) -> bool {`
  - Purpose: Validates that a string is a valid tmux pane identifier by verifying it has a '%' prefix followed by one or more ASCII digits. [crates/ghook/src/terminal_context.rs:128-133]
- `parse_tmux_socket_path` (function) component `parse_tmux_socket_path [function]` (`0897e27e-b9c0-58f8-8cfd-fe2c0131f65a`) lines 138-145 [crates/ghook/src/terminal_context.rs:138-145]
  - Signature: `fn parse_tmux_socket_path(tmux_env: &str) -> Option<String> {`
  - Purpose: Extracts and returns the first comma-delimited token from a tmux environment variable string after trimming whitespace, or `None` if the token is empty or absent. [crates/ghook/src/terminal_context.rs:138-145]
- `parse_socket_path_extracts_leading_segment` (function) component `parse_socket_path_extracts_leading_segment [function]` (`d065c630-b5fd-56ab-81b2-6976a000ef19`) lines 153-158 [crates/ghook/src/terminal_context.rs:153-158]
  - Signature: `fn parse_socket_path_extracts_leading_segment() {`
  - Purpose: Unit test verifying that `parse_tmux_socket_path` correctly extracts the leading socket path segment (everything before the comma delimiter) from a tmux socket identifier string. [crates/ghook/src/terminal_context.rs:153-158]
- `parse_socket_path_handles_empty` (function) component `parse_socket_path_handles_empty [function]` (`50b499f0-980b-5ef0-b787-91b728960634`) lines 161-164 [crates/ghook/src/terminal_context.rs:161-164]
  - Signature: `fn parse_socket_path_handles_empty() {`
  - Purpose: This test validates that `parse_tmux_socket_path` returns `None` for empty and malformed socket path inputs. [crates/ghook/src/terminal_context.rs:161-164]
- `build_context_sets_tmux_pane_verbatim` (function) component `build_context_sets_tmux_pane_verbatim [function]` (`33abafd6-98c6-5317-a520-c2a754c02cb9`) lines 167-171 [crates/ghook/src/terminal_context.rs:167-171]
  - Signature: `fn build_context_sets_tmux_pane_verbatim() {`
  - Purpose: This test function verifies that `build_context` correctly extracts and populates the tmux pane identifier (`%42`) and socket path (`/private/tmp/tmux-501/default`) from its input parameters into the returned context map. [crates/ghook/src/terminal_context.rs:167-171]
- `build_context_nulls_missing_empty_or_invalid_tmux_fields` (function) component `build_context_nulls_missing_empty_or_invalid_tmux_fields [function]` (`7c984ae4-de71-5f3b-89a9-07defc4ae74a`) lines 174-187 [crates/ghook/src/terminal_context.rs:174-187]
  - Signature: `fn build_context_nulls_missing_empty_or_invalid_tmux_fields() {`
  - Purpose: This test validates that `build_context()` returns null values for both `tmux_pane` and `tmux_socket_path` fields across various combinations of missing, empty, or malformed tmux socket paths and pane identifiers. [crates/ghook/src/terminal_context.rs:174-187]
- `valid_tmux_pane_matches_daemon_contract` (function) component `valid_tmux_pane_matches_daemon_contract [function]` (`4447068e-b3cc-512a-88ff-2405163f28d6`) lines 190-198 [crates/ghook/src/terminal_context.rs:190-198]
  - Signature: `fn valid_tmux_pane_matches_daemon_contract() {`
  - Purpose: This test verifies that `is_valid_tmux_pane()` correctly validates tmux pane identifiers matching the format `%<digits>` while rejecting empty strings, incomplete prefixes, numeric-only inputs, and whitespace variations. [crates/ghook/src/terminal_context.rs:190-198]
- `inject_respects_existing_terminal_context` (function) component `inject_respects_existing_terminal_context [function]` (`f629e177-1cde-5057-b69c-4f3032b9864a`) lines 201-209 [crates/ghook/src/terminal_context.rs:201-209]
  - Signature: `fn inject_respects_existing_terminal_context() {`
  - Purpose: Tests that `inject()` preserves existing terminal_context fields without adding a parent_pid field. [crates/ghook/src/terminal_context.rs:201-209]
- `inject_no_op_on_non_object` (function) component `inject_no_op_on_non_object [function]` (`8d707487-2178-5ece-8d22-7bd6cd8e886f`) lines 212-216 [crates/ghook/src/terminal_context.rs:212-216]
  - Signature: `fn inject_no_op_on_non_object() {`
  - Purpose: A unit test verifying that the `inject` function performs no operation on non-object JSON values (string literals). [crates/ghook/src/terminal_context.rs:212-216]
- `capture_emits_expected_keys` (function) component `capture_emits_expected_keys [function]` (`c8c3ae50-4e71-5ac5-b79c-8f3f4caa9b4b`) lines 219-237 [crates/ghook/src/terminal_context.rs:219-237]
  - Signature: `fn capture_emits_expected_keys() {`
  - Purpose: Test function that asserts `build_context()` populates the context object with all twelve required keys encompassing process identifiers, terminal properties, tmux socket configuration, and Gobby workflow metadata. [crates/ghook/src/terminal_context.rs:219-237]

