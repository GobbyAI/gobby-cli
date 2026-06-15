---
title: crates/gcore/src/ai/daemon/tests.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/tests.rs
  ranges:
  - 15-24
  - 26-29
  - 31-38
  - 40-42
  - 44-46
  - 48-57
  - 59-76
  - 78-91
  - 93-99
  - 101-124
  - 126-145
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon/tests.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Purpose

Test support for the AI daemon, with helper functions that spawn a mock JSON server, parse and inspect HTTP requests, create temporary home directories, write daemon bootstrap/token files, and build a minimal `AiContext`/daemon `CapabilityBinding` for tests. It also defines `EnvGuard`, a mutex-protected RAII guard that snapshots and restores `HOME`, `GOBBY_HOME`, `GOBBY_DAEMON_URL`, and `GOBBY_PORT` so daemon tests can mutate environment state safely without leaking across cases.
[crates/gcore/src/ai/daemon/tests.rs:15-24]
[crates/gcore/src/ai/daemon/tests.rs:26-29]
[crates/gcore/src/ai/daemon/tests.rs:31-38]
[crates/gcore/src/ai/daemon/tests.rs:40-42]
[crates/gcore/src/ai/daemon/tests.rs:44-46]

## API Symbols

- `spawn_server` (function) component `spawn_server [function]` (`e45aa30d-af73-57f2-933f-7137f2dc251e`) lines 15-24 [crates/gcore/src/ai/daemon/tests.rs:15-24]
  - Signature: `fn spawn_server(response: &'static str) -> (u16, RequestHandle) {`
  - Purpose: Starts a test JSON-response server with the given static response body, extracts and parses the server port from the returned base URL, and returns the port together with the 'RequestHandle'. [crates/gcore/src/ai/daemon/tests.rs:15-24]
- `request_body_json` (function) component `request_body_json [function]` (`1bd5e7cb-09cb-5caa-8f69-d63bf9995f1f`) lines 26-29 [crates/gcore/src/ai/daemon/tests.rs:26-29]
  - Signature: `fn request_body_json(request: &str) -> serde_json::Value {`
  - Purpose: Splits the request string on the first CRLF-CRLF boundary, takes the remainder as the HTTP body, and parses it as JSON into a 'serde_json::Value', panicking if the delimiter is missing or the body is invalid JSON. [crates/gcore/src/ai/daemon/tests.rs:26-29]
- `has_header` (function) component `has_header [function]` (`38fc88f5-dd60-5bd7-84d1-d0bd22ee3f63`) lines 31-38 [crates/gcore/src/ai/daemon/tests.rs:31-38]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Returns 'true' if any line in 'request' contains a colon-separated header whose name matches 'name' case-insensitively and whose trimmed value is exactly 'value', otherwise 'false'. [crates/gcore/src/ai/daemon/tests.rs:31-38]
- `multipart_has_field` (function) component `multipart_has_field [function]` (`db496884-0fb3-5980-aa7e-21f56ea4066c`) lines 40-42 [crates/gcore/src/ai/daemon/tests.rs:40-42]
  - Signature: `fn multipart_has_field(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Returns 'true' if the multipart request string contains a form field header 'name="{name}"' immediately followed by a blank line and the exact 'value' payload, otherwise 'false'. [crates/gcore/src/ai/daemon/tests.rs:40-42]
- `temp_home` (function) component `temp_home [function]` (`b4856859-5788-53d4-bade-e10f071785ad`) lines 44-46 [crates/gcore/src/ai/daemon/tests.rs:44-46]
  - Signature: `fn temp_home() -> tempfile::TempDir {`
  - Purpose: Creates and returns a newly allocated temporary directory, panicking on failure by unwrapping the 'tempfile::tempdir()' result. [crates/gcore/src/ai/daemon/tests.rs:44-46]
- `write_daemon_files` (function) component `write_daemon_files [function]` (`609f8827-fe70-5a28-b7eb-d108e9ac597b`) lines 48-57 [crates/gcore/src/ai/daemon/tests.rs:48-57]
  - Signature: `fn write_daemon_files(home: &Path, port: u16, token: &str) {`
  - Purpose: Creates '~/.gobby', writes 'bootstrap.yaml' containing the daemon port and '127.0.0.1' bind host, and writes 'local_cli_token' containing the provided token followed by a newline. [crates/gcore/src/ai/daemon/tests.rs:48-57]
- `test_context` (function) component `test_context [function]` (`0f89d0b7-8ab9-5d37-9ce1-1c26fdc370eb`) lines 59-76 [crates/gcore/src/ai/daemon/tests.rs:59-76]
  - Signature: `fn test_context(project_id: Option<&str>) -> AiContext {`
  - Purpose: Constructs an 'AiContext' using a single shared test 'binding' for all AI binding slots, sets 'max_concurrency' to '1', leaves 'keep_alive' unset, initializes 'AiLimiter' with capacity '1', and copies the optional 'project_id' into an owned 'String'. [crates/gcore/src/ai/daemon/tests.rs:59-76]
- `binding` (function) component `binding [function]` (`26a0f0e6-7e8c-5b93-97e1-3a8787a6a30f`) lines 78-91 [crates/gcore/src/ai/daemon/tests.rs:78-91]
  - Signature: `fn binding() -> CapabilityBinding {`
  - Purpose: Returns a 'CapabilityBinding' configured for daemon routing with all optional fields unset except 'model' set to '"daemon-model"' and 'provider' set to '"daemon-provider"'. [crates/gcore/src/ai/daemon/tests.rs:78-91]
- `EnvGuard` (class) component `EnvGuard [class]` (`e66f9531-5f14-596b-9b71-79667a322946`) lines 93-99 [crates/gcore/src/ai/daemon/tests.rs:93-99]
  - Signature: `struct EnvGuard {`
  - Purpose: 'EnvGuard' is a mutex-guarded RAII state holder that caches optional 'HOME', 'GOBBY_HOME', 'DAEMON_URL', and 'PORT' environment values as 'OsString's for later restoration. [crates/gcore/src/ai/daemon/tests.rs:93-99]
- `EnvGuard` (class) component `EnvGuard [class]` (`468f210a-4ca9-5f2e-8c14-1e7324a73f74`) lines 101-124 [crates/gcore/src/ai/daemon/tests.rs:101-124]
  - Signature: `impl EnvGuard {`
  - Purpose: 'EnvGuard' is a test-only RAII guard that serializes environment mutation, snapshots 'HOME', 'GOBBY_HOME', 'GOBBY_DAEMON_URL', and 'GOBBY_PORT', then temporarily sets 'HOME' and 'GOBBY_HOME' while clearing daemon URL/port overrides to prevent leakage into bootstrap behavior. [crates/gcore/src/ai/daemon/tests.rs:101-124]
- `EnvGuard.set_home` (method) component `EnvGuard.set_home [method]` (`e071fd20-a387-530c-a03d-fa49be13d022`) lines 102-123 [crates/gcore/src/ai/daemon/tests.rs:102-123]
  - Signature: `fn set_home(home: &Path) -> Self {`
  - Purpose: Acquires 'TEST_ENV_LOCK', snapshots the current 'HOME', 'GOBBY_HOME', 'GOBBY_DAEMON_URL', and 'GOBBY_PORT' values into an 'EnvGuard', then sets 'HOME' to 'home', 'GOBBY_HOME' to 'home/.gobby', clears 'GOBBY_DAEMON_URL' and 'GOBBY_PORT', and returns the guard for later restoration. [crates/gcore/src/ai/daemon/tests.rs:102-123]
- `EnvGuard` (class) component `EnvGuard [class]` (`1888ca68-cddb-5ec6-a4fd-e2b3f1498abb`) lines 126-145 [crates/gcore/src/ai/daemon/tests.rs:126-145]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: 'EnvGuard' is a drop guard that restores the process environment for 'HOME', 'GOBBY_HOME', 'GOBBY_DAEMON_URL', and 'GOBBY_PORT' to their saved values, or removes them if they were originally unset. [crates/gcore/src/ai/daemon/tests.rs:126-145]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`f1f018d4-5cd5-54f5-95e8-899673f18b1e`) lines 127-144 [crates/gcore/src/ai/daemon/tests.rs:127-144]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Restores the original 'HOME', 'GOBBY_HOME', 'GOBBY_DAEMON_URL', and 'GOBBY_PORT' environment variables by setting each saved value or removing the variable if no prior value existed. [crates/gcore/src/ai/daemon/tests.rs:127-144]

