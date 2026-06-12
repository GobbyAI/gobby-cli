---
title: crates/gcore/src/layered_config.rs
type: code_file
provenance:
- file: crates/gcore/src/layered_config.rs
  ranges:
  - 17-25
  - 32-63
  - 65-70
  - 72-77
  - 88-90
  - 94-98
  - 100-117
  - 119-130
  - 132-140
  - 143-159
  - 162-179
  - 182-198
  - 201-210
  - 213-232
  - 235-249
  - 252-261
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/layered_config.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/layered_config.rs` exposes 18 indexed API symbols.
[crates/gcore/src/layered_config.rs:17-25]
[crates/gcore/src/layered_config.rs:32-63]
[crates/gcore/src/layered_config.rs:65-70]
[crates/gcore/src/layered_config.rs:72-77]
[crates/gcore/src/layered_config.rs:88-90]

## API Symbols

- `LayeredConfigError` (type) component `LayeredConfigError [type]` (`77f14ccb-049e-53a7-aa41-95d26b40abe8`) lines 17-25 [crates/gcore/src/layered_config.rs:17-25]
  - Signature: `pub enum LayeredConfigError {`
  - Purpose: Indexed type `LayeredConfigError` in `crates/gcore/src/layered_config.rs`. [crates/gcore/src/layered_config.rs:17-25]
- `load_layered_yaml` (function) component `load_layered_yaml [function]` (`94506992-63e1-50a6-b802-633fa6f08c89`) lines 32-63 [crates/gcore/src/layered_config.rs:32-63]
  - Signature: `pub fn load_layered_yaml<T: DeserializeOwned>(`
  - Purpose: Deserializes a tool-specific YAML configuration file from a cascading hierarchy of paths (CLI override → local .gobby → project root .gobby → home directory) into a generic type T, returning the first match or None. [crates/gcore/src/layered_config.rs:32-63]
- `try_layer` (function) component `try_layer [function]` (`c9b117ed-05c4-53ff-b782-d2c4c3c96d59`) lines 65-70 [crates/gcore/src/layered_config.rs:65-70]
  - Signature: `fn try_layer<T: DeserializeOwned>(path: &Path) -> Result<Option<T>, LayeredConfigError> {`
  - Purpose: # Summary

The `try_layer` function attempts to read and deserialize a configuration file from a given path, returning `Some(T)` on successful parsing, `None` if the file is absent, or a `LayeredConfigError` if parsing fails. [crates/gcore/src/layered_config.rs:65-70]
- `parse` (function) component `parse [function]` (`f259a385-2032-59df-abb9-ac95bf371b87`) lines 72-77 [crates/gcore/src/layered_config.rs:72-77]
  - Signature: `fn parse<T: DeserializeOwned>(path: &Path, content: &str) -> Result<T, LayeredConfigError> {`
  - Purpose: Deserializes YAML content into a generic type `T`, mapping any deserialization errors to a `LayeredConfigError` variant that includes the source file path for error context. [crates/gcore/src/layered_config.rs:72-77]
- `TestConfig` (class) component `TestConfig [class]` (`ad7d1b2a-187b-590b-a832-119eaa9372ef`) lines 88-90 [crates/gcore/src/layered_config.rs:88-90]
  - Signature: `struct TestConfig {`
  - Purpose: TestConfig is a struct containing a single String field that holds a test configuration name. [crates/gcore/src/layered_config.rs:88-90]
- `CwdGuard` (class) component `CwdGuard [class]` (`c78ce928-4414-5fa0-be75-751a9945e86f`) lines 94-98 [crates/gcore/src/layered_config.rs:94-98]
  - Signature: `struct CwdGuard {`
  - Purpose: `CwdGuard` is a RAII guard that acquires a mutex lock while preserving the current working directory and HOME environment variable for automatic restoration upon scope exit. [crates/gcore/src/layered_config.rs:94-98]
- `CwdGuard` (class) component `CwdGuard [class]` (`cf8a898f-e136-533c-9721-241d2271ef1a`) lines 100-117 [crates/gcore/src/layered_config.rs:100-117]
  - Signature: `impl CwdGuard {`
  - Purpose: # CwdGuard Summary

CwdGuard is a RAII guard that atomically switches the process's current working directory and GOBBY_HOME environment variable within a serialized test lock, storing the previous state for restoration upon drop. [crates/gcore/src/layered_config.rs:100-117]
- `CwdGuard.enter` (method) component `CwdGuard.enter [method]` (`d8a93f4e-b76c-59fc-a0f7-8171553d88d7`) lines 101-116 [crates/gcore/src/layered_config.rs:101-116]
  - Signature: `fn enter(cwd: &Path, gobby_home: &Path) -> Self {`
  - Purpose: Returns a RAII guard that atomically saves the current environment state, switches to specified `cwd` and `GOBBY_HOME` values under a serialization lock, and restores the previous state upon drop. [crates/gcore/src/layered_config.rs:101-116]
- `CwdGuard` (class) component `CwdGuard [class]` (`70d29247-cb4d-53e1-ae9b-d230f8bda947`) lines 119-130 [crates/gcore/src/layered_config.rs:119-130]
  - Signature: `impl Drop for CwdGuard {`
  - Purpose: `CwdGuard` is a RAII guard that restores the previous working directory and `GOBBY_HOME` environment variable state upon being dropped. [crates/gcore/src/layered_config.rs:119-130]
- `CwdGuard.drop` (method) component `CwdGuard.drop [method]` (`954a572c-1219-5119-abd3-44448c837e78`) lines 120-129 [crates/gcore/src/layered_config.rs:120-129]
  - Signature: `fn drop(&mut self) {`
  - Purpose: This Drop implementation restores the working directory and GOBBY_HOME environment variable to their previous states when the object is destroyed. [crates/gcore/src/layered_config.rs:120-129]
- `project_with_config` (function) component `project_with_config [function]` (`4e3d269b-9244-5350-b1a4-400734e840c0`) lines 132-140 [crates/gcore/src/layered_config.rs:132-140]
  - Signature: `fn project_with_config(config_yaml: &str) -> TempDir {`
  - Purpose: Creates a temporary directory with a `.gobby` subdirectory containing a `project.json` file (with id "p1") and a `test-tool.yaml` configuration file initialized from the provided YAML string. [crates/gcore/src/layered_config.rs:132-140]
- `subdirectory_resolves_project_root_config` (function) component `subdirectory_resolves_project_root_config [function]` (`862a9fa5-3e27-5f91-a7d1-3c465fb8ea2f`) lines 143-159 [crates/gcore/src/layered_config.rs:143-159]
  - Signature: `fn subdirectory_resolves_project_root_config() {`
  - Purpose: Tests that `load_layered_yaml` successfully resolves and loads configuration from the project root when invoked from a nested subdirectory. [crates/gcore/src/layered_config.rs:143-159]
- `cwd_config_wins_without_project_marker` (function) component `cwd_config_wins_without_project_marker [function]` (`254ee22a-2aec-5b12-b01f-9872b169c884`) lines 162-179 [crates/gcore/src/layered_config.rs:162-179]
  - Signature: `fn cwd_config_wins_without_project_marker() {`
  - Purpose: Verifies that `load_layered_yaml()` retrieves configuration from the current working directory's `.gobby` directory without requiring a project marker in parent directories. [crates/gcore/src/layered_config.rs:162-179]
- `cli_override_beats_discovered_layers` (function) component `cli_override_beats_discovered_layers [function]` (`d6e6c1d9-ae9d-59e5-8177-7dd20ad91e38`) lines 182-198 [crates/gcore/src/layered_config.rs:182-198]
  - Signature: `fn cli_override_beats_discovered_layers() {`
  - Purpose: Tests that an explicitly-specified override YAML configuration file takes precedence over auto-discovered project configuration layers when loading layered YAML. [crates/gcore/src/layered_config.rs:182-198]
- `unreadable_cli_override_is_an_error` (function) component `unreadable_cli_override_is_an_error [function]` (`f6e045b2-fdfd-581b-8540-aed0dd17346f`) lines 201-210 [crates/gcore/src/layered_config.rs:201-210]
  - Signature: `fn unreadable_cli_override_is_an_error() {`
  - Purpose: This test verifies that attempting to load a layered YAML configuration with a non-existent CLI override file path returns a `LayeredConfigError::Read` error. [crates/gcore/src/layered_config.rs:201-210]
- `gobby_home_layer_is_used_when_no_project_config` (function) component `gobby_home_layer_is_used_when_no_project_config [function]` (`7acf7378-5def-5411-87fb-4e445795a57d`) lines 213-232 [crates/gcore/src/layered_config.rs:213-232]
  - Signature: `fn gobby_home_layer_is_used_when_no_project_config() {`
  - Purpose: This test verifies that `load_layered_yaml` falls back to loading configuration from the gobby home directory when no project-level configuration file exists. [crates/gcore/src/layered_config.rs:213-232]
- `broken_layer_config_is_an_error_not_a_fallthrough` (function) component `broken_layer_config_is_an_error_not_a_fallthrough [function]` (`3ce806e5-889d-5e80-a76b-99d11d4adac5`) lines 235-249 [crates/gcore/src/layered_config.rs:235-249]
  - Signature: `fn broken_layer_config_is_an_error_not_a_fallthrough() {`
  - Purpose: This test verifies that malformed YAML in a project-level configuration file causes layered configuration loading to fail with a `LayeredConfigError::Parse` rather than fall through to the global configuration. [crates/gcore/src/layered_config.rs:235-249]
- `no_layer_found_returns_none` (function) component `no_layer_found_returns_none [function]` (`f728bec2-7b3b-5d60-8951-0780c34210c4`) lines 252-261 [crates/gcore/src/layered_config.rs:252-261]
  - Signature: `fn no_layer_found_returns_none() {`
  - Purpose: This test verifies that `load_layered_yaml` returns `None` when no configuration files exist in the specified working and home directories. [crates/gcore/src/layered_config.rs:252-261]

