---
title: crates/gloc/src/exec.rs
type: code_file
provenance:
- file: crates/gloc/src/exec.rs
  ranges:
  - 9-21
  - 24-36
  - 39-45
  - 51-80
  - 87-94
  - 96-109
  - 111-123
  - 126-134
  - 137-144
  - 147-150
  - 153-156
  - 159-163
  - 166-171
  - 174-188
  - 191-194
  - 197-199
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gloc/src/exec.rs

Module: [[code/modules/crates/gloc/src|crates/gloc/src]]

## Purpose

This file builds and launches a configured LLM client process. It merges template-resolved environment variables from `default_env` and `env`, assembles command-line arguments from an optional model flag, default args, and passthrough args, can locate binaries on `PATH`, and then either `exec`s or spawns the client binary depending on platform; the test helpers construct sample backend/client setups and verify the environment, argument, and binary lookup behavior.
[crates/gloc/src/exec.rs:9-21]
[crates/gloc/src/exec.rs:24-36]
[crates/gloc/src/exec.rs:39-45]
[crates/gloc/src/exec.rs:51-80]
[crates/gloc/src/exec.rs:87-94]

## API Symbols

- `build_env` (function) component `build_env [function]` (`5f667291-dbf4-517d-a474-fdd7b7d4dfce`) lines 9-21 [crates/gloc/src/exec.rs:9-21]
  - Signature: `pub fn build_env(client: &Client, backend: &Backend, model: &str) -> BTreeMap<String, String> {`
  - Purpose: 'build_env' constructs a 'BTreeMap<String, String>' by merging 'client.default_env' and then 'client.env', resolving each value through 'resolve_template(val, backend, model)' and letting entries in 'client.env' override defaults on key collisions. [crates/gloc/src/exec.rs:9-21]
- `build_args` (function) component `build_args [function]` (`3ef29eda-b6d2-5dbe-b208-162ea81f5f20`) lines 24-36 [crates/gloc/src/exec.rs:24-36]
  - Signature: `pub fn build_args(client: &Client, model: &str, passthrough: &[String]) -> Vec<String> {`
  - Purpose: Builds a command-line argument vector by conditionally prepending the client’s model flag and model name when both are non-empty, then appending the client’s default arguments and the caller-provided passthrough arguments in order. [crates/gloc/src/exec.rs:24-36]
- `which_binary` (function) component `which_binary [function]` (`b5293d60-b85e-5a3f-a15c-3de280834d85`) lines 39-45 [crates/gloc/src/exec.rs:39-45]
  - Signature: `pub fn which_binary(name: &str) -> Option<PathBuf> {`
  - Purpose: Searches the 'PATH' environment variable for the first entry whose joined path with 'name' exists as a regular file, returning that 'PathBuf' or 'None' if not found. [crates/gloc/src/exec.rs:39-45]
- `exec_client` (function) component `exec_client [function]` (`44053d16-a034-5247-9e93-82f38395b494`) lines 51-80 [crates/gloc/src/exec.rs:51-80]
  - Signature: `pub fn exec_client(client: &Client, backend: &Backend, model: &str, passthrough: &[String]) -> ! {`
  - Purpose: Constructs a 'Command' for 'client.binary' using environment variables from 'build_env' and arguments from 'build_args', then replaces the current process with it on Unix via 'exec()' or runs it and exits with the child status code on non-Unix platforms. [crates/gloc/src/exec.rs:51-80]
- `test_backend` (function) component `test_backend [function]` (`c0d554a5-0ee5-5ddb-bae2-cc4021fb3ed0`) lines 87-94 [crates/gloc/src/exec.rs:87-94]
  - Signature: `fn test_backend() -> Backend {`
  - Purpose: Constructs and returns a 'Backend' configured for local Ollama access with name 'ollama', base URL 'http://localhost:11434', probe endpoint '/api/tags', and auth token 'ollama'. [crates/gloc/src/exec.rs:87-94]
- `test_claude_client` (function) component `test_claude_client [function]` (`b32f228a-fea3-57c7-bbaf-095136afd61e`) lines 96-109 [crates/gloc/src/exec.rs:96-109]
  - Signature: `fn test_claude_client() -> Client {`
  - Purpose: Constructs a 'Client' configured for the 'claude' binary with Anthropic base URL and auth token environment variables pointing to the backend, an empty API key, '--model' as the model flag, 'qwen3-coder' as the default model, and no extra args or default env. [crates/gloc/src/exec.rs:96-109]
- `test_codex_client` (function) component `test_codex_client [function]` (`890d349c-d19a-5229-83bd-f48033ddab58`) lines 111-123 [crates/gloc/src/exec.rs:111-123]
  - Signature: `fn test_codex_client() -> Client {`
  - Purpose: Constructs and returns a 'Client' configured to invoke the 'codex' binary with OpenAI-compatible backend environment variables, '--provider openai' as default args, '--model' as the model flag, and 'qwen3-coder' as the default model. [crates/gloc/src/exec.rs:111-123]
- `test_build_env_claude` (function) component `test_build_env_claude [function]` (`3be65073-d21a-506e-b864-3d6c82092932`) lines 126-134 [crates/gloc/src/exec.rs:126-134]
  - Signature: `fn test_build_env_claude() {`
  - Purpose: Verifies that 'build_env' for a Claude client/backend with model 'qwen3-coder' produces environment variables 'ANTHROPIC_BASE_URL=http://localhost:11434', 'ANTHROPIC_AUTH_TOKEN=ollama', and 'ANTHROPIC_API_KEY=""'. [crates/gloc/src/exec.rs:126-134]
- `test_build_env_codex` (function) component `test_build_env_codex [function]` (`67ae0308-2886-5c79-add5-274fc79c51f1`) lines 137-144 [crates/gloc/src/exec.rs:137-144]
  - Signature: `fn test_build_env_codex() {`
  - Purpose: Verifies that 'build_env' for a Codex client/backend and the 'qwen3-coder' model sets 'OPENAI_BASE_URL' to 'http://localhost:11434/v1' and 'OPENAI_API_KEY' to 'ollama'. [crates/gloc/src/exec.rs:137-144]
- `test_build_args_with_model` (function) component `test_build_args_with_model [function]` (`1a718268-cb56-5f8f-9339-ce52e89cb9c9`) lines 147-150 [crates/gloc/src/exec.rs:147-150]
  - Signature: `fn test_build_args_with_model() {`
  - Purpose: Verifies that 'build_args' includes '--model' followed by the specified model name ('qwen3-coder') when called with no additional arguments. [crates/gloc/src/exec.rs:147-150]
- `test_build_args_codex_with_defaults` (function) component `test_build_args_codex_with_defaults [function]` (`1e60195b-5788-5f91-b6e2-6d960a13ecfb`) lines 153-156 [crates/gloc/src/exec.rs:153-156]
  - Signature: `fn test_build_args_codex_with_defaults() {`
  - Purpose: Verifies that 'build_args' for a Codex client with an empty argument list returns the default CLI arguments '["--model", "qwen3-coder", "--provider", "openai"]'. [crates/gloc/src/exec.rs:153-156]
- `test_build_args_with_passthrough` (function) component `test_build_args_with_passthrough [function]` (`cc9630db-6d87-5715-a8bb-40bcba35e833`) lines 159-163 [crates/gloc/src/exec.rs:159-163]
  - Signature: `fn test_build_args_with_passthrough() {`
  - Purpose: Verifies that 'build_args' prepends '--model qwen3-coder' to the base arguments while appending passthrough arguments unchanged, yielding '["--model", "qwen3-coder", "--verbose", "extra"]'. [crates/gloc/src/exec.rs:159-163]
- `test_build_args_empty_model_flag` (function) component `test_build_args_empty_model_flag [function]` (`f5e0fd53-b4db-5238-86ec-8e1ec7a8a469`) lines 166-171 [crates/gloc/src/exec.rs:166-171]
  - Signature: `fn test_build_args_empty_model_flag() {`
  - Purpose: Verifies that 'build_args' omits the '--model' argument when 'client.model_flag' is empty and returns only '["--provider", "openai"]' for the given client and model. [crates/gloc/src/exec.rs:166-171]
- `test_default_env_lower_priority` (function) component `test_default_env_lower_priority [function]` (`95c344df-65d7-58ed-b08b-55450937a506`) lines 174-188 [crates/gloc/src/exec.rs:174-188]
  - Signature: `fn test_default_env_lower_priority() {`
  - Purpose: Verifies that 'build_env' preserves arbitrary default environment variables while giving backend-derived 'ANTHROPIC_BASE_URL' higher precedence than 'client.default_env' and overriding it with 'http://localhost:11434'. [crates/gloc/src/exec.rs:174-188]
- `test_which_binary_finds_sh` (function) component `test_which_binary_finds_sh [function]` (`5f69128c-734d-54b7-9151-c41113ec6264`) lines 191-194 [crates/gloc/src/exec.rs:191-194]
  - Signature: `fn test_which_binary_finds_sh() {`
  - Purpose: Verifies that 'which_binary("sh")' returns 'Some', asserting the 'sh' shell binary is discoverable on Unix systems. [crates/gloc/src/exec.rs:191-194]
- `test_which_binary_not_found` (function) component `test_which_binary_not_found [function]` (`f7ac3ece-6fe9-57c8-a00d-dfb224d9db5d`) lines 197-199 [crates/gloc/src/exec.rs:197-199]
  - Signature: `fn test_which_binary_not_found() {`
  - Purpose: Verifies that 'which_binary' returns 'None' when given a nonexistent binary name ('"definitely_not_a_real_binary_xyz"'). [crates/gloc/src/exec.rs:197-199]

