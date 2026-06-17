---
title: crates/ghook/src/source.rs
type: code_file
provenance:
- file: crates/ghook/src/source.rs
  ranges:
  - 3-14
  - 20-27
  - 29-35
  - '37'
  - 40-43
  - 47-49
  - 53-87
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/source.rs:3-14](crates/ghook/src/source.rs#L3-L14), [crates/ghook/src/source.rs:20-27](crates/ghook/src/source.rs#L20-L27), [crates/ghook/src/source.rs:29-35](crates/ghook/src/source.rs#L29-L35), [crates/ghook/src/source.rs:37](crates/ghook/src/source.rs#L37), [crates/ghook/src/source.rs:40-43](crates/ghook/src/source.rs#L40-L43), [crates/ghook/src/source.rs:47-49](crates/ghook/src/source.rs#L47-L49), [crates/ghook/src/source.rs:53-87](crates/ghook/src/source.rs#L53-L87)

</details>

# crates/ghook/src/source.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

This file resolves the effective CLI source name from `CliConfig`, only allowing `GOBBY_SOURCE` to override the configured source when the canonical source is `claude`; other sources pass through unchanged, and empty overrides are ignored. It also contains test-only helpers and an RAII guard to clear and restore the process-wide source-detection environment, plus a test that verifies the override behavior stays Claude-only and does not react to `CLAUDE_CODE_ENTRYPOINT` by itself.
[crates/ghook/src/source.rs:3-14]
[crates/ghook/src/source.rs:20-27]
[crates/ghook/src/source.rs:29-35]
[crates/ghook/src/source.rs:37]
[crates/ghook/src/source.rs:40-43]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `detect_source` | function | `pub(crate) fn detect_source(cfg: &CliConfig) -> String {` | `detect_source [function]` | `32182b88-ac1b-5a85-8084-efc7eee1e0c3` | 3-14 [crates/ghook/src/source.rs:3-14] | Indexed function `detect_source` in `crates/ghook/src/source.rs`. [crates/ghook/src/source.rs:3-14] |
| `clear_source_env` | function | `fn clear_source_env() {` | `clear_source_env [function]` | `97af9d03-cbf7-57d6-9a35-24425c730f05` | 20-27 [crates/ghook/src/source.rs:20-27] | Indexed function `clear_source_env` in `crates/ghook/src/source.rs`. [crates/ghook/src/source.rs:20-27] |
| `set_source_env` | function | `fn set_source_env(key: &str, value: &str) {` | `set_source_env [function]` | `7dd4ad00-7abe-5ed9-b923-e7646a56aca6` | 29-35 [crates/ghook/src/source.rs:29-35] | Indexed function `set_source_env` in `crates/ghook/src/source.rs`. [crates/ghook/src/source.rs:29-35] |
| `SourceEnvGuard` | class | `struct SourceEnvGuard;` | `SourceEnvGuard [class]` | `8cc10a88-b936-5ef0-a760-b71a29f4875b` | 37-37 [crates/ghook/src/source.rs:37] | Indexed class `SourceEnvGuard` in `crates/ghook/src/source.rs`. [crates/ghook/src/source.rs:37] |
| `SourceEnvGuard::new` | method | `fn new() -> Self {` | `SourceEnvGuard::new [method]` | `0a673d02-fe70-5e9d-97c3-8401533286eb` | 40-43 [crates/ghook/src/source.rs:40-43] | Indexed method `SourceEnvGuard::new` in `crates/ghook/src/source.rs`. [crates/ghook/src/source.rs:40-43] |
| `SourceEnvGuard::drop` | method | `fn drop(&mut self) {` | `SourceEnvGuard::drop [method]` | `a19d35be-177c-59aa-aebe-fb5e0bccc023` | 47-49 [crates/ghook/src/source.rs:47-49] | Indexed method `SourceEnvGuard::drop` in `crates/ghook/src/source.rs`. [crates/ghook/src/source.rs:47-49] |
| `detect_source_respects_override_only_for_claude` | function | `fn detect_source_respects_override_only_for_claude() {` | `detect_source_respects_override_only_for_claude [function]` | `9e829fba-d764-5165-bdfa-83cff325db90` | 53-87 [crates/ghook/src/source.rs:53-87] | Indexed function `detect_source_respects_override_only_for_claude` in `crates/ghook/src/source.rs`. [crates/ghook/src/source.rs:53-87] |
