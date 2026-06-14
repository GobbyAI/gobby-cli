---
title: crates/ghook/src/cli_config.rs
type: code_file
provenance:
- file: crates/ghook/src/cli_config.rs
  ranges:
  - 11-18
  - 20-61
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

This file defines the compile-time `CliConfig` registry for Gobby’s hook dispatcher. It maps known CLI names to fixed per-host settings: a daemon source label, the set of hook types that must fail closed, and the malformed-JSON exit code. `for_cli` performs case-insensitive lookup for the supported CLIs, `for_dispatch` guarantees a usable config by falling back to `claude`, and `is_critical_hook` checks whether a hook should be treated as failure-critical. The tests lock in the expected CLI-specific critical-hook sets, exit codes, case-insensitive matching, and fallback behavior.
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/cli_config.rs:20-61]
[crates/ghook/src/cli_config.rs:21-52]
[crates/ghook/src/cli_config.rs:54-56]
[crates/ghook/src/cli_config.rs:58-60]

## API Symbols

- `CliConfig` (class) component `CliConfig [class]` (`dfe7d451-73f4-539e-9b59-32c8c9291990`) lines 11-18 [crates/ghook/src/cli_config.rs:11-18]
  - Signature: `pub struct CliConfig {`
  - Purpose: CliConfig is a struct containing a daemon source identifier, a set of critical hooks enforcing fail-closed failure semantics, and an exit code for malformed JSON input. [crates/ghook/src/cli_config.rs:11-18]
- `CliConfig` (class) component `CliConfig [class]` (`8ee0a776-cf79-5255-b0fd-2f7f365b159d`) lines 20-61 [crates/ghook/src/cli_config.rs:20-61]
  - Signature: `impl CliConfig {`
  - Purpose: `CliConfig` provides factory methods that map CLI tool names (Claude, Gemini, Qwen, Codex, Droid) to their respective configurations, including critical hook sets and JSON error exit codes, with Claude as the default fallback. [crates/ghook/src/cli_config.rs:20-61]
- `CliConfig.for_cli` (method) component `CliConfig.for_cli [method]` (`c38c936b-fd31-5b98-9447-8cbc0e7c09af`) lines 21-52 [crates/ghook/src/cli_config.rs:21-52]
  - Signature: `pub fn for_cli(cli: &str) -> Option<Self> {`
  - Purpose: A constructor that returns an `Option<Self>` configured with provider-specific critical hooks and JSON error exit codes based on the case-insensitive CLI name, or `None` if unrecognized. [crates/ghook/src/cli_config.rs:21-52]
- `CliConfig.for_dispatch` (method) component `CliConfig.for_dispatch [method]` (`3c9c2a2b-aa89-5b2d-ab2e-bca9790720db`) lines 54-56 [crates/ghook/src/cli_config.rs:54-56]
  - Signature: `pub fn for_dispatch(cli: &str) -> Self {`
  - Purpose: This method returns a configuration instance for the given CLI string, falling back to a hardcoded "claude" configuration with a panic guarantee if both initialization attempts fail. [crates/ghook/src/cli_config.rs:54-56]
- `CliConfig.is_critical_hook` (method) component `CliConfig.is_critical_hook [method]` (`f811c999-8711-59d2-8518-96c9feb5c664`) lines 58-60 [crates/ghook/src/cli_config.rs:58-60]
  - Signature: `pub fn is_critical_hook(&self, hook_type: &str) -> bool {`
  - Purpose: This method returns a boolean indicating whether the provided `hook_type` string is present in the instance's `critical_hooks` collection. [crates/ghook/src/cli_config.rs:58-60]
- `claude_critical_hooks` (function) component `claude_critical_hooks [function]` (`f40c9f23-98da-522f-8c45-ca809b03e638`) lines 68-74 [crates/ghook/src/cli_config.rs:68-74]
  - Signature: `fn claude_critical_hooks() {`
  - Purpose: Tests that `CliConfig` for "claude" initializes with the correct source and critical_hooks containing "session-start" and "pre-compact" while excluding the case-variant "SessionStart". [crates/ghook/src/cli_config.rs:68-74]
- `gemini_json_parse_errors_exit_one` (function) component `gemini_json_parse_errors_exit_one [function]` (`943c844b-abc9-5669-93e6-7a2ccd3c947a`) lines 77-80 [crates/ghook/src/cli_config.rs:77-80]
  - Signature: `fn gemini_json_parse_errors_exit_one() {`
  - Purpose: Asserts that the Gemini CLI's CliConfig has a json_error_exit_code property equal to 1. [crates/ghook/src/cli_config.rs:77-80]
- `codex_stop_is_critical` (function) component `codex_stop_is_critical [function]` (`1c881534-3659-5877-b67f-17bb4ac95d39`) lines 83-88 [crates/ghook/src/cli_config.rs:83-88]
  - Signature: `fn codex_stop_is_critical() {`
  - Purpose: This test function verifies that the "codex" CLI configuration designates "Stop" as a critical hook, "PreToolUse" as non-critical, and sets the JSON error exit code to 2. [crates/ghook/src/cli_config.rs:83-88]
- `droid_recognized_with_no_critical_hooks` (function) component `droid_recognized_with_no_critical_hooks [function]` (`4f9d118c-758a-5611-9b5e-6736994333ce`) lines 91-96 [crates/ghook/src/cli_config.rs:91-96]
  - Signature: `fn droid_recognized_with_no_critical_hooks() {`
  - Purpose: Unit test asserting that `CliConfig` for "droid" has source "droid", empty `critical_hooks`, and `json_error_exit_code` of 1. [crates/ghook/src/cli_config.rs:91-96]
- `unknown_cli_returns_none` (function) component `unknown_cli_returns_none [function]` (`c23e955a-627c-536c-a068-42631db416c2`) lines 99-101 [crates/ghook/src/cli_config.rs:99-101]
  - Signature: `fn unknown_cli_returns_none() {`
  - Purpose: Asserts that `CliConfig::for_cli("cursor")` returns `None`, verifying that unknown CLI identifiers are not recognized by the configuration system. [crates/ghook/src/cli_config.rs:99-101]
- `cli_name_is_case_insensitive` (function) component `cli_name_is_case_insensitive [function]` (`f8ca49f8-6f88-5ec9-8719-55a412bf2ebc`) lines 104-108 [crates/ghook/src/cli_config.rs:104-108]
  - Signature: `fn cli_name_is_case_insensitive() {`
  - Purpose: This test function verifies that `CliConfig::for_cli()` performs case-insensitive name matching by asserting successful lookups for the same CLI names in different case variations. [crates/ghook/src/cli_config.rs:104-108]
- `unknown_cli_falls_back_to_claude_for_dispatch` (function) component `unknown_cli_falls_back_to_claude_for_dispatch [function]` (`bc5df029-37ae-5c56-a2c3-f5e9984de2d9`) lines 111-116 [crates/ghook/src/cli_config.rs:111-116]
  - Signature: `fn unknown_cli_falls_back_to_claude_for_dispatch() {`
  - Purpose: Tests that `CliConfig::for_dispatch("cursor")` falls back to "claude" as the source while asserting "session-start" is a critical hook and the JSON error exit code is 2. [crates/ghook/src/cli_config.rs:111-116]

