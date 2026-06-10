---
title: crates/ghook/src/cli_config.rs
type: code_file
provenance:
- file: crates/ghook/src/cli_config.rs
  ranges:
  - 11-18
  - 20-61
  - 21-52
  - 54-56
  - 58-60
  - 68-74
  - 77-80
  - 83-88
  - 91-96
  - 99-101
  - 104-108
  - 111-116
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/cli_config.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/cli_config.rs` exposes 12 indexed API symbols.
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/cli_config.rs:20-61]
[crates/ghook/src/cli_config.rs:21-52]
[crates/ghook/src/cli_config.rs:54-56]
[crates/ghook/src/cli_config.rs:58-60]
[crates/ghook/src/cli_config.rs:68-74]
[crates/ghook/src/cli_config.rs:77-80]
[crates/ghook/src/cli_config.rs:83-88]
[crates/ghook/src/cli_config.rs:91-96]
[crates/ghook/src/cli_config.rs:99-101]
[crates/ghook/src/cli_config.rs:104-108]
[crates/ghook/src/cli_config.rs:111-116]

## API Symbols

- `CliConfig` (class) component `CliConfig [class]` (`dfe7d451-73f4-539e-9b59-32c8c9291990`) lines 11-18 [crates/ghook/src/cli_config.rs:11-18]
  - Signature: `pub struct CliConfig {`
  - Purpose: CliConfig is a configuration struct containing a daemon source identifier, a set of critical fail-closed hooks, and a JSON parsing error exit code aligned with Python dispatcher behavior. [crates/ghook/src/cli_config.rs:11-18]
- `CliConfig` (class) component `CliConfig [class]` (`8ee0a776-cf79-5255-b0fd-2f7f365b159d`) lines 20-61 [crates/ghook/src/cli_config.rs:20-61]
  - Signature: `impl CliConfig {`
  - Purpose: CliConfig implements factory methods to map CLI agent names (Claude, Gemini, Qwen, Codex, Droid) to their source identifiers, sets of critical execution hooks, and JSON error exit codes, with Claude as the fallback default. [crates/ghook/src/cli_config.rs:20-61]
- `CliConfig.for_cli` (method) component `CliConfig.for_cli [method]` (`c38c936b-fd31-5b98-9447-8cbc0e7c09af`) lines 21-52 [crates/ghook/src/cli_config.rs:21-52]
  - Signature: `pub fn for_cli(cli: &str) -> Option<Self> {`
  - Purpose: Returns a configured `Self` instance with CLI-specific `source`, `critical_hooks`, and `json_error_exit_code` fields for recognized CLI names (case-insensitive), or `None` for unrecognized inputs. [crates/ghook/src/cli_config.rs:21-52]
- `CliConfig.for_dispatch` (method) component `CliConfig.for_dispatch [method]` (`3c9c2a2b-aa89-5b2d-ab2e-bca9790720db`) lines 54-56 [crates/ghook/src/cli_config.rs:54-56]
  - Signature: `pub fn for_dispatch(cli: &str) -> Self {`
  - Purpose: This method constructs a configuration instance for the specified CLI tool, falling back to a "claude" configuration if the specified one is unavailable, and panicking if the fallback also fails. [crates/ghook/src/cli_config.rs:54-56]
- `CliConfig.is_critical_hook` (method) component `CliConfig.is_critical_hook [method]` (`f811c999-8711-59d2-8518-96c9feb5c664`) lines 58-60 [crates/ghook/src/cli_config.rs:58-60]
  - Signature: `pub fn is_critical_hook(&self, hook_type: &str) -> bool {`
  - Purpose: Checks whether the specified hook type string exists in the instance's `critical_hooks` collection. [crates/ghook/src/cli_config.rs:58-60]
- `claude_critical_hooks` (function) component `claude_critical_hooks [function]` (`f40c9f23-98da-522f-8c45-ca809b03e638`) lines 68-74 [crates/ghook/src/cli_config.rs:68-74]
  - Signature: `fn claude_critical_hooks() {`
  - Purpose: Unit test that validates CliConfig for 'claude' correctly populates critical_hooks with case-sensitive entries 'session-start' and 'pre-compact' while excluding 'SessionStart'. [crates/ghook/src/cli_config.rs:68-74]
- `gemini_json_parse_errors_exit_one` (function) component `gemini_json_parse_errors_exit_one [function]` (`943c844b-abc9-5669-93e6-7a2ccd3c947a`) lines 77-80 [crates/ghook/src/cli_config.rs:77-80]
  - Signature: `fn gemini_json_parse_errors_exit_one() {`
  - Purpose: This function asserts that the Gemini CLI configuration's `json_error_exit_code` field is set to 1. [crates/ghook/src/cli_config.rs:77-80]
- `codex_stop_is_critical` (function) component `codex_stop_is_critical [function]` (`1c881534-3659-5877-b67f-17bb4ac95d39`) lines 83-88 [crates/ghook/src/cli_config.rs:83-88]
  - Signature: `fn codex_stop_is_critical() {`
  - Purpose: This test function verifies that the 'codex' CLI configuration correctly designates 'Stop' as a critical hook, excludes 'PreToolUse' from critical hooks, and sets the JSON error exit code to 2. [crates/ghook/src/cli_config.rs:83-88]
- `droid_recognized_with_no_critical_hooks` (function) component `droid_recognized_with_no_critical_hooks [function]` (`4f9d118c-758a-5611-9b5e-6736994333ce`) lines 91-96 [crates/ghook/src/cli_config.rs:91-96]
  - Signature: `fn droid_recognized_with_no_critical_hooks() {`
  - Purpose: Asserts that `CliConfig::for_cli("droid")` produces a configuration with source='droid', empty critical_hooks, and json_error_exit_code=1. [crates/ghook/src/cli_config.rs:91-96]
- `unknown_cli_returns_none` (function) component `unknown_cli_returns_none [function]` (`c23e955a-627c-536c-a068-42631db416c2`) lines 99-101 [crates/ghook/src/cli_config.rs:99-101]
  - Signature: `fn unknown_cli_returns_none() {`
  - Purpose: This function asserts that `CliConfig::for_cli()` returns `None` when passed an unknown CLI identifier ("cursor"). [crates/ghook/src/cli_config.rs:99-101]
- `cli_name_is_case_insensitive` (function) component `cli_name_is_case_insensitive [function]` (`f8ca49f8-6f88-5ec9-8719-55a412bf2ebc`) lines 104-108 [crates/ghook/src/cli_config.rs:104-108]
  - Signature: `fn cli_name_is_case_insensitive() {`
  - Purpose: Tests that `CliConfig::for_cli()` performs case-insensitive CLI name resolution by asserting successful configuration retrieval for names in different case variations (uppercase, title case, mixed case). [crates/ghook/src/cli_config.rs:104-108]
- `unknown_cli_falls_back_to_claude_for_dispatch` (function) component `unknown_cli_falls_back_to_claude_for_dispatch [function]` (`bc5df029-37ae-5c56-a2c3-f5e9984de2d9`) lines 111-116 [crates/ghook/src/cli_config.rs:111-116]
  - Signature: `fn unknown_cli_falls_back_to_claude_for_dispatch() {`
  - Purpose: # Summary

Unit test that validates `CliConfig::for_dispatch()` falls back to "claude" as the source for unknown dispatchers, while asserting "session-start" is a critical hook and JSON error exit code equals 2. [crates/ghook/src/cli_config.rs:111-116]

