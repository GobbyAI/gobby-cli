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
  - 39-44
  - 46-50
  - 53-82
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/source.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

This file resolves the effective CLI source name, with a special override path only for `claude`: `detect_source` returns the configured source unchanged for non-`claude` CLIs, but can substitute `GOBBY_SOURCE` when that environment variable is set to a non-empty value. The test-only helpers `clear_source_env`, `set_source_env`, and `SourceEnvGuard` manage process-wide environment state safely across tests by clearing it on setup and drop. The unit test verifies the override behavior, including that `CLAUDE_CODE_ENTRYPOINT` is ignored, empty overrides are skipped, and non-`claude` sources are left alone.
[crates/ghook/src/source.rs:3-14]
[crates/ghook/src/source.rs:20-27]
[crates/ghook/src/source.rs:29-35]
[crates/ghook/src/source.rs:37]
[crates/ghook/src/source.rs:39-44]

## API Symbols

- `detect_source` (function) component `detect_source [function]` (`32182b88-ac1b-5a85-8084-efc7eee1e0c3`) lines 3-14 [crates/ghook/src/source.rs:3-14]
  - Signature: `pub(crate) fn detect_source(cfg: &CliConfig) -> String {`
  - Purpose: Returns 'cfg.source' unless it is '"claude"' and the 'GOBBY_SOURCE' environment variable is set to a non-empty value, in which case it returns that environment value as a 'String'. [crates/ghook/src/source.rs:3-14]
- `clear_source_env` (function) component `clear_source_env [function]` (`97af9d03-cbf7-57d6-9a35-24425c730f05`) lines 20-27 [crates/ghook/src/source.rs:20-27]
  - Signature: `fn clear_source_env() {`
  - Purpose: Removes the process-wide 'GOBBY_SOURCE' and 'CLAUDE_CODE_ENTRYPOINT' environment variables to clear source-detection state. [crates/ghook/src/source.rs:20-27]
- `set_source_env` (function) component `set_source_env [function]` (`7dd4ad00-7abe-5ed9-b923-e7646a56aca6`) lines 29-35 [crates/ghook/src/source.rs:29-35]
  - Signature: `fn set_source_env(key: &str, value: &str) {`
  - Purpose: Sets the given process-wide environment variable by calling 'std::env::set_var' inside an 'unsafe' block, relying on the module’s exclusive access to these test-only source-detection variables. [crates/ghook/src/source.rs:29-35]
- `SourceEnvGuard` (class) component `SourceEnvGuard [class]` (`8cc10a88-b936-5ef0-a760-b71a29f4875b`) lines 37-37 [crates/ghook/src/source.rs:37]
  - Signature: `struct SourceEnvGuard;`
  - Purpose: 'SourceEnvGuard' is a guard-type struct intended to manage the lifetime of a source-related environment scope, typically by applying and then restoring or cleaning up environment state when the guard is dropped. [crates/ghook/src/source.rs:37]
- `SourceEnvGuard` (class) component `SourceEnvGuard [class]` (`e8eeea64-a990-57d2-85f5-0f49fd22ed66`) lines 39-44 [crates/ghook/src/source.rs:39-44]
  - Signature: `impl SourceEnvGuard {`
  - Purpose: 'SourceEnvGuard' is a zero-sized guard whose 'new()' constructor clears the source-related environment via 'clear_source_env()' and returns the guard, ensuring the environment is sanitized at creation time. [crates/ghook/src/source.rs:39-44]
- `SourceEnvGuard.new` (method) component `SourceEnvGuard.new [method]` (`0a673d02-fe70-5e9d-97c3-8401533286eb`) lines 40-43 [crates/ghook/src/source.rs:40-43]
  - Signature: `fn new() -> Self {`
  - Purpose: Constructs a new instance after clearing source-related environment variables, then returns 'Self'. [crates/ghook/src/source.rs:40-43]
- `SourceEnvGuard` (class) component `SourceEnvGuard [class]` (`9fe91193-cc60-5991-8139-693d88119cc8`) lines 46-50 [crates/ghook/src/source.rs:46-50]
  - Signature: `impl Drop for SourceEnvGuard {`
  - Purpose: 'SourceEnvGuard' is an RAII drop guard whose destructor clears the source-related environment by invoking 'clear_source_env()' when the guard goes out of scope. [crates/ghook/src/source.rs:46-50]
- `SourceEnvGuard.drop` (method) component `SourceEnvGuard.drop [method]` (`a19d35be-177c-59aa-aebe-fb5e0bccc023`) lines 47-49 [crates/ghook/src/source.rs:47-49]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Calls 'clear_source_env()' when the value is dropped, clearing the source environment during destruction. [crates/ghook/src/source.rs:47-49]
- `detect_source_respects_override_only_for_claude` (function) component `detect_source_respects_override_only_for_claude [function]` (`9e829fba-d764-5165-bdfa-83cff325db90`) lines 53-82 [crates/ghook/src/source.rs:53-82]
  - Signature: `fn detect_source_respects_override_only_for_claude() {`
  - Purpose: Verifies that 'detect_source' returns the canonical source for 'claude' unless 'GOBBY_SOURCE' is set to a non-empty override, while ignoring 'CLAUDE_CODE_ENTRYPOINT' and leaving non-'claude' CLIs unchanged. [crates/ghook/src/source.rs:53-82]

