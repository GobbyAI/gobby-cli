---
title: crates/gloc/src/config.rs
type: code_file
provenance:
- file: crates/gloc/src/config.rs
  ranges:
  - 13-22
  - 25-32
  - 34-42
  - 44-46
  - 48-50
  - 53-65
  - 67-138
  - 142-148
  - 155-160
  - 163-168
  - 171-182
  - 185-189
  - 192-207
  - 210-219
  - 222-226
  - 229-232
  - 235-238
  - 241-250
  - 253-262
  - 265-274
  - 277-288
  - 291-299
  - 302-307
  - 310-317
  - 320-327
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gloc/src/config.rs

Module: [[code/modules/crates/gloc/src|crates/gloc/src]]

## Purpose

`crates/gloc/src/config.rs` exposes 30 indexed API symbols.
[crates/gloc/src/config.rs:13-22]
[crates/gloc/src/config.rs:25-32]
[crates/gloc/src/config.rs:34-42]
[crates/gloc/src/config.rs:35-41]
[crates/gloc/src/config.rs:44-46]

## API Symbols

- `Config` (class) component `Config [class]` (`e4aeb1b6-b112-5577-b443-865dcc440b2c`) lines 13-22 [crates/gloc/src/config.rs:13-22]
  - Signature: `pub struct Config {`
  - Purpose: Config is a serde-deserializable struct that aggregates application settings, backend service definitions, named client configurations, and string-to-string aliases, with all fields defaulting during deserialization. [crates/gloc/src/config.rs:13-22]
- `Settings` (class) component `Settings [class]` (`40246c2c-bc9a-53d2-a5da-24858cd67e6d`) lines 25-32 [crates/gloc/src/config.rs:25-32]
  - Signature: `pub struct Settings {`
  - Purpose: `Settings` is a serde-compatible configuration struct that encapsulates a probe timeout duration and boolean flags for automatic loading and pulling behaviors with customizable defaults. [crates/gloc/src/config.rs:25-32]
- `Settings` (class) component `Settings [class]` (`3b989843-c2da-541d-908d-cf57f4f3759e`) lines 34-42 [crates/gloc/src/config.rs:34-42]
  - Signature: `impl Default for Settings {`
  - Purpose: `Default` trait implementation for `Settings` that initializes probe timeout and auto-load behavior via helper functions while disabling auto-pull. [crates/gloc/src/config.rs:34-42]
- `Settings.default` (method) component `Settings.default [method]` (`0de5951d-2ed3-58aa-905b-800fd4e0804b`) lines 35-41 [crates/gloc/src/config.rs:35-41]
  - Signature: `fn default() -> Self {`
  - Purpose: Implements the `Default` trait, constructing an instance with delegated `probe_timeout_ms` and `auto_load` defaults, and `auto_pull` explicitly set to `false`. [crates/gloc/src/config.rs:35-41]
- `default_probe_timeout_ms` (function) component `default_probe_timeout_ms [function]` (`123761e3-1ee3-58ad-9298-11ac7b82103f`) lines 44-46 [crates/gloc/src/config.rs:44-46]
  - Signature: `fn default_probe_timeout_ms() -> u64 {`
  - Purpose: This function returns a `u64` constant value of 500, representing the default probe timeout in milliseconds. [crates/gloc/src/config.rs:44-46]
- `default_auto_load` (function) component `default_auto_load [function]` (`89009b7e-536e-522d-a4a2-2cefee9baad0`) lines 48-50 [crates/gloc/src/config.rs:48-50]
  - Signature: `fn default_auto_load() -> bool {`
  - Purpose: Returns `true` to indicate that auto-loading is enabled by default. [crates/gloc/src/config.rs:48-50]
- `Client` (class) component `Client [class]` (`ec61d699-24de-5049-8e7c-7d3fc8ae4d8d`) lines 53-65 [crates/gloc/src/config.rs:53-65]
  - Signature: `pub struct Client {`
  - Purpose: `Client` is a serde-compatible configuration struct for executing a binary with customizable model selection, default command-line arguments, and environment variable management. [crates/gloc/src/config.rs:53-65]
- `Config` (class) component `Config [class]` (`c5648d9d-918e-5b51-bb23-0cca54761e20`) lines 67-138 [crates/gloc/src/config.rs:67-138]
  - Signature: `impl Config {`
  - Purpose: Config implements configuration loading via first-found-wins layered resolution from CLI/project/home/compiled-default YAML sources, model alias resolution, and formatted output serialization. [crates/gloc/src/config.rs:67-138]
- `Config.load` (method) component `Config.load [method]` (`091f53fb-cba2-5931-97be-23ed133fd4f6`) lines 72-89 [crates/gloc/src/config.rs:72-89]
  - Signature: `pub fn load(config_override: Option<&Path>) -> Self {`
  - Purpose: Loads a layered YAML configuration with an optional override path, falling back to a built-in default if unavailable, and exiting the process with diagnostics on parse errors. [crates/gloc/src/config.rs:72-89]
- `Config.resolve_alias` (method) component `Config.resolve_alias [method]` (`46ea3e45-a48b-5c2e-8ee8-3ad64ca4ec71`) lines 92-97 [crates/gloc/src/config.rs:92-97]
  - Signature: `pub fn resolve_alias(&self, model: &str) -> String {`
  - Purpose: Retrieves the aliased name for a given model from the internal aliases map, returning the original model name if no alias exists. [crates/gloc/src/config.rs:92-97]
- `Config.dump` (method) component `Config.dump [method]` (`937f8cc4-e5c9-50b0-b78e-43ef155208aa`) lines 100-131 [crates/gloc/src/config.rs:100-131]
  - Signature: `pub fn dump(&self) -> String {`
  - Purpose: Returns a formatted string representation of the configuration state, displaying settings, configured backends with URLs, clients with their binaries and default models, and any defined aliases. [crates/gloc/src/config.rs:100-131]
- `Config.load_builtin` (method) component `Config.load_builtin [method]` (`883628f7-9a2a-501d-b753-d2f012eb13f4`) lines 135-137 [crates/gloc/src/config.rs:135-137]
  - Signature: `pub fn load_builtin() -> Self {`
  - Purpose: Deserializes the DEFAULT_CONFIG YAML string into Self, panicking if the built-in configuration is invalid. [crates/gloc/src/config.rs:135-137]
- `resolve_template` (function) component `resolve_template [function]` (`44b0a98a-f234-5970-930e-8d6b63632257`) lines 142-148 [crates/gloc/src/config.rs:142-148]
  - Signature: `pub fn resolve_template(template: &str, backend: &Backend, model: &str) -> String {`
  - Purpose: Resolves template placeholders by interpolating backend configuration properties (`url`, `auth_token`, `name`) and model name into their corresponding `{...}` token positions. [crates/gloc/src/config.rs:142-148]
- `test_load_default_config` (function) component `test_load_default_config [function]` (`e9157a4a-4997-5589-a5e0-83dcfbe964c4`) lines 155-160 [crates/gloc/src/config.rs:155-160]
  - Signature: `fn test_load_default_config() {`
  - Purpose: This test verifies that `Config::load_builtin()` returns a configuration with `probe_timeout_ms=500`, `auto_load=true`, and `auto_pull=false`. [crates/gloc/src/config.rs:155-160]
- `test_default_config_has_backends` (function) component `test_default_config_has_backends [function]` (`9f7d4a5d-dcf3-563e-8e93-c55f3e583936`) lines 163-168 [crates/gloc/src/config.rs:163-168]
  - Signature: `fn test_default_config_has_backends() {`
  - Purpose: This test verifies that the built-in default `Config` contains exactly two backends named 'lmstudio' and 'ollama' in that sequential order. [crates/gloc/src/config.rs:163-168]
- `test_backend_fields` (function) component `test_backend_fields [function]` (`7c5ad7be-7a23-51c0-8b53-311a26d28f6c`) lines 171-182 [crates/gloc/src/config.rs:171-182]
  - Signature: `fn test_backend_fields() {`
  - Purpose: Tests that the built-in configuration correctly initializes the LM Studio and Ollama backend services with their expected URLs, probe endpoints, and authentication tokens. [crates/gloc/src/config.rs:171-182]
- `test_default_config_has_clients` (function) component `test_default_config_has_clients [function]` (`ac27f4f8-607c-55ab-99b8-671820619aef`) lines 185-189 [crates/gloc/src/config.rs:185-189]
  - Signature: `fn test_default_config_has_clients() {`
  - Purpose: Asserts that the built-in default configuration contains client entries for both "claude" and "codex". [crates/gloc/src/config.rs:185-189]
- `test_claude_client_env` (function) component `test_claude_client_env [function]` (`711eb0ad-3c1d-5bc1-8d21-6d5cd20cedfd`) lines 192-207 [crates/gloc/src/config.rs:192-207]
  - Signature: `fn test_claude_client_env() {`
  - Purpose: Tests that the built-in Config object correctly initializes a 'claude' client with the expected environment variables (ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, empty ANTHROPIC_API_KEY), model flag, and default model. [crates/gloc/src/config.rs:192-207]
- `test_codex_client_env` (function) component `test_codex_client_env [function]` (`ec49ad5a-88a9-5244-9fc7-cc709bd45c13`) lines 210-219 [crates/gloc/src/config.rs:210-219]
  - Signature: `fn test_codex_client_env() {`
  - Purpose: Asserts that the built-in 'codex' client configuration is correctly initialized with binary name "codex", OPENAI_BASE_URL environment variable "{backend.url}/v1", and default arguments ["--provider", "openai"]. [crates/gloc/src/config.rs:210-219]
- `test_default_config_has_aliases` (function) component `test_default_config_has_aliases [function]` (`1cb22630-78d7-5072-b82e-3c360e808f34`) lines 222-226 [crates/gloc/src/config.rs:222-226]
  - Signature: `fn test_default_config_has_aliases() {`
  - Purpose: This test verifies that the built-in configuration contains the expected model aliases mapping "qwen" to "qwen3-coder" and "glm" to "glm-4.7:cloud". [crates/gloc/src/config.rs:222-226]
- `test_resolve_alias_hit` (function) component `test_resolve_alias_hit [function]` (`c7ea4c03-f6f0-508d-beef-93a0dafc0afd`) lines 229-232 [crates/gloc/src/config.rs:229-232]
  - Signature: `fn test_resolve_alias_hit() {`
  - Purpose: This test verifies that the builtin configuration correctly resolves the alias "qwen" to "qwen3-coder". [crates/gloc/src/config.rs:229-232]
- `test_resolve_alias_miss` (function) component `test_resolve_alias_miss [function]` (`2f955a74-2e66-5c22-ab0e-2bda34c868d8`) lines 235-238 [crates/gloc/src/config.rs:235-238]
  - Signature: `fn test_resolve_alias_miss() {`
  - Purpose: Unit test verifying that `Config::resolve_alias` returns the input string unchanged when passed an unmapped alias. [crates/gloc/src/config.rs:235-238]
- `test_resolve_template_all_vars` (function) component `test_resolve_template_all_vars [function]` (`57e0bedf-06fb-5481-8bc0-306975e46e39`) lines 241-250 [crates/gloc/src/config.rs:241-250]
  - Signature: `fn test_resolve_template_all_vars() {`
  - Purpose: Verifies that `resolve_template` correctly interpolates the `{backend.url}` placeholder in a template string with the actual backend URL value. [crates/gloc/src/config.rs:241-250]
- `test_resolve_template_auth_token` (function) component `test_resolve_template_auth_token [function]` (`71393741-4aa0-525f-b77a-083b99d45201`) lines 253-262 [crates/gloc/src/config.rs:253-262]
  - Signature: `fn test_resolve_template_auth_token() {`
  - Purpose: Unit test that verifies `resolve_template` correctly resolves the template placeholder `{backend.auth_token}` to the backend instance's auth_token field value. [crates/gloc/src/config.rs:253-262]
- `test_resolve_template_model` (function) component `test_resolve_template_model [function]` (`40a6142a-2255-5000-b2bc-ed6d91bd0a5f`) lines 265-274 [crates/gloc/src/config.rs:265-274]
  - Signature: `fn test_resolve_template_model() {`
  - Purpose: This function tests that `resolve_template` correctly interpolates the `{model}` placeholder in a template string with the provided model identifier "qwen3-coder". [crates/gloc/src/config.rs:265-274]
- `test_resolve_template_no_vars` (function) component `test_resolve_template_no_vars [function]` (`2b08bf02-1815-51a3-b499-4039d8aa4d6d`) lines 277-288 [crates/gloc/src/config.rs:277-288]
  - Signature: `fn test_resolve_template_no_vars() {`
  - Purpose: This test verifies that `resolve_template()` returns the input string unmodified when the template contains no variables to substitute. [crates/gloc/src/config.rs:277-288]
- `test_resolve_template_empty` (function) component `test_resolve_template_empty [function]` (`0055e704-44e7-59e6-b6b4-d15e258d8dd5`) lines 291-299 [crates/gloc/src/config.rs:291-299]
  - Signature: `fn test_resolve_template_empty() {`
  - Purpose: Verifies that `resolve_template` returns an empty string when invoked with an empty template string. [crates/gloc/src/config.rs:291-299]
- `test_settings_default` (function) component `test_settings_default [function]` (`5fd23c31-1ec9-5670-a964-8bc2b2f6ae6b`) lines 302-307 [crates/gloc/src/config.rs:302-307]
  - Signature: `fn test_settings_default() {`
  - Purpose: Asserts that the default `Settings` instance initializes `probe_timeout_ms` to 500, `auto_load` to true, and `auto_pull` to false. [crates/gloc/src/config.rs:302-307]
- `test_dump_contains_key_sections` (function) component `test_dump_contains_key_sections [function]` (`ad501f95-e599-580e-a835-459e13800a47`) lines 310-317 [crates/gloc/src/config.rs:310-317]
  - Signature: `fn test_dump_contains_key_sections() {`
  - Purpose: Verifies that a builtin Config's `dump()` method output contains expected key configuration sections: probe_timeout_ms (500ms), 2 backends, 2 clients, and 2 aliases. [crates/gloc/src/config.rs:310-317]
- `test_config_from_valid_override` (function) component `test_config_from_valid_override [function]` (`f1af90af-966b-593c-92fa-88ec6df56024`) lines 320-327 [crates/gloc/src/config.rs:320-327]
  - Signature: `fn test_config_from_valid_override() {`
  - Purpose: Verifies that `Config::load()` successfully loads a configuration from an explicit file path override, asserting that both the backends and clients collections are populated. [crates/gloc/src/config.rs:320-327]

