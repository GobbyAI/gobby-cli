---
title: crates/ghook/src/cli_config.rs
type: code_file
provenance:
- file: crates/ghook/src/cli_config.rs
  ranges:
  - 11-18
  - 21-59
  - 61-63
  - 65-67
  - 75-81
  - 84-87
  - 90-95
  - 98-107
  - 110-115
  - 118-120
  - 123-128
  - 131-136
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/cli_config.rs:11-18](crates/ghook/src/cli_config.rs#L11-L18), [crates/ghook/src/cli_config.rs:21-59](crates/ghook/src/cli_config.rs#L21-L59), [crates/ghook/src/cli_config.rs:61-63](crates/ghook/src/cli_config.rs#L61-L63), [crates/ghook/src/cli_config.rs:65-67](crates/ghook/src/cli_config.rs#L65-L67), [crates/ghook/src/cli_config.rs:75-81](crates/ghook/src/cli_config.rs#L75-L81), [crates/ghook/src/cli_config.rs:84-87](crates/ghook/src/cli_config.rs#L84-L87), [crates/ghook/src/cli_config.rs:90-95](crates/ghook/src/cli_config.rs#L90-L95), [crates/ghook/src/cli_config.rs:98-107](crates/ghook/src/cli_config.rs#L98-L107), [crates/ghook/src/cli_config.rs:110-115](crates/ghook/src/cli_config.rs#L110-L115), [crates/ghook/src/cli_config.rs:118-120](crates/ghook/src/cli_config.rs#L118-L120), [crates/ghook/src/cli_config.rs:123-128](crates/ghook/src/cli_config.rs#L123-L128), [crates/ghook/src/cli_config.rs:131-136](crates/ghook/src/cli_config.rs#L131-L136)

</details>

# crates/ghook/src/cli_config.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Defines the per-CLI hook-dispatch configuration used by Gobby to mirror the Python dispatcher’s `CLIConfig` registry. `CliConfig::for_cli` does a case-insensitive lookup of a known CLI name and returns the corresponding compile-time config: the daemon source identifier, the set of critical hooks that must fail closed, and the JSON parse error exit code. `for_dispatch` falls back to the Claude config for unknown CLIs, and `is_critical_hook` checks whether a hook should be treated as critical. The free functions encode the per-CLI critical-hook rules and error-code expectations for the supported CLIs.
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/cli_config.rs:21-59]
[crates/ghook/src/cli_config.rs:61-63]
[crates/ghook/src/cli_config.rs:65-67]
[crates/ghook/src/cli_config.rs:75-81]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CliConfig` | class | `pub struct CliConfig {` | `CliConfig [class]` | `dfe7d451-73f4-539e-9b59-32c8c9291990` | 11-18 [crates/ghook/src/cli_config.rs:11-18] | Indexed class `CliConfig` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:11-18] |
| `CliConfig::for_cli` | method | `pub fn for_cli(cli: &str) -> Option<Self> {` | `CliConfig::for_cli [method]` | `c38c936b-fd31-5b98-9447-8cbc0e7c09af` | 21-59 [crates/ghook/src/cli_config.rs:21-59] | Indexed method `CliConfig::for_cli` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:21-59] |
| `CliConfig::for_dispatch` | method | `pub fn for_dispatch(cli: &str) -> Self {` | `CliConfig::for_dispatch [method]` | `d580bbf8-b7e1-585d-942f-b6db0a5d75f9` | 61-63 [crates/ghook/src/cli_config.rs:61-63] | Indexed method `CliConfig::for_dispatch` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:61-63] |
| `CliConfig::is_critical_hook` | method | `pub fn is_critical_hook(&self, hook_type: &str) -> bool {` | `CliConfig::is_critical_hook [method]` | `ee02c19d-79c7-5e9e-b683-20e08e142672` | 65-67 [crates/ghook/src/cli_config.rs:65-67] | Indexed method `CliConfig::is_critical_hook` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:65-67] |
| `claude_critical_hooks` | function | `fn claude_critical_hooks() {` | `claude_critical_hooks [function]` | `4c197514-aff0-53b7-9fba-e0b892dc4252` | 75-81 [crates/ghook/src/cli_config.rs:75-81] | Indexed function `claude_critical_hooks` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:75-81] |
| `gemini_json_parse_errors_exit_one` | function | `fn gemini_json_parse_errors_exit_one() {` | `gemini_json_parse_errors_exit_one [function]` | `9f13cd10-1e99-5d6e-8c7c-f207f5501728` | 84-87 [crates/ghook/src/cli_config.rs:84-87] | Indexed function `gemini_json_parse_errors_exit_one` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:84-87] |
| `codex_stop_is_critical` | function | `fn codex_stop_is_critical() {` | `codex_stop_is_critical [function]` | `fcef067e-f0fc-5a7f-8d4e-6486a4d830a4` | 90-95 [crates/ghook/src/cli_config.rs:90-95] | Indexed function `codex_stop_is_critical` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:90-95] |
| `grok_registry_uses_native_snake_case_hooks` | function | `fn grok_registry_uses_native_snake_case_hooks() {` | `grok_registry_uses_native_snake_case_hooks [function]` | `ccc147b6-83ca-544b-a020-827ab53ea8fe` | 98-107 [crates/ghook/src/cli_config.rs:98-107] | Indexed function `grok_registry_uses_native_snake_case_hooks` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:98-107] |
| `droid_recognized_with_no_critical_hooks` | function | `fn droid_recognized_with_no_critical_hooks() {` | `droid_recognized_with_no_critical_hooks [function]` | `b2f6e2aa-0e08-50cf-8504-217733176eb4` | 110-115 [crates/ghook/src/cli_config.rs:110-115] | Indexed function `droid_recognized_with_no_critical_hooks` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:110-115] |
| `unknown_cli_returns_none` | function | `fn unknown_cli_returns_none() {` | `unknown_cli_returns_none [function]` | `f71adb51-ca63-5eda-85d1-4dd54e8e7a16` | 118-120 [crates/ghook/src/cli_config.rs:118-120] | Indexed function `unknown_cli_returns_none` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:118-120] |
| `cli_name_is_case_insensitive` | function | `fn cli_name_is_case_insensitive() {` | `cli_name_is_case_insensitive [function]` | `e8b6b1a4-3eed-59fd-bb1a-c074571e9525` | 123-128 [crates/ghook/src/cli_config.rs:123-128] | Indexed function `cli_name_is_case_insensitive` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:123-128] |
| `unknown_cli_falls_back_to_claude_for_dispatch` | function | `fn unknown_cli_falls_back_to_claude_for_dispatch() {` | `unknown_cli_falls_back_to_claude_for_dispatch [function]` | `43df18c6-5b87-5506-b908-9216a025fb7b` | 131-136 [crates/ghook/src/cli_config.rs:131-136] | Indexed function `unknown_cli_falls_back_to_claude_for_dispatch` in `crates/ghook/src/cli_config.rs`. [crates/ghook/src/cli_config.rs:131-136] |
