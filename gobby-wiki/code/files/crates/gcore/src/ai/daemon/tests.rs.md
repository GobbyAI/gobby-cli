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
  - 102-123
  - 127-144
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/daemon/tests.rs:15-24](crates/gcore/src/ai/daemon/tests.rs#L15-L24), [crates/gcore/src/ai/daemon/tests.rs:26-29](crates/gcore/src/ai/daemon/tests.rs#L26-L29), [crates/gcore/src/ai/daemon/tests.rs:31-38](crates/gcore/src/ai/daemon/tests.rs#L31-L38), [crates/gcore/src/ai/daemon/tests.rs:40-42](crates/gcore/src/ai/daemon/tests.rs#L40-L42), [crates/gcore/src/ai/daemon/tests.rs:44-46](crates/gcore/src/ai/daemon/tests.rs#L44-L46), [crates/gcore/src/ai/daemon/tests.rs:48-57](crates/gcore/src/ai/daemon/tests.rs#L48-L57), [crates/gcore/src/ai/daemon/tests.rs:59-76](crates/gcore/src/ai/daemon/tests.rs#L59-L76), [crates/gcore/src/ai/daemon/tests.rs:78-91](crates/gcore/src/ai/daemon/tests.rs#L78-L91), [crates/gcore/src/ai/daemon/tests.rs:93-99](crates/gcore/src/ai/daemon/tests.rs#L93-L99), [crates/gcore/src/ai/daemon/tests.rs:102-123](crates/gcore/src/ai/daemon/tests.rs#L102-L123), [crates/gcore/src/ai/daemon/tests.rs:127-144](crates/gcore/src/ai/daemon/tests.rs#L127-L144)

</details>

# crates/gcore/src/ai/daemon/tests.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Purpose

This test file provides shared fixtures and request-inspection helpers for `ai::daemon` tests, plus submodules for the daemon’s embedding, environment, multipart, and text test cases. The helpers spin up a mock JSON server, parse and match HTTP request bodies/headers/multipart fields, create a temporary home directory, write daemon bootstrap/token files, and build a minimal `AiContext` with daemon routing and a single-concurrency limiter. `EnvGuard` wraps test environment setup by swapping `HOME` under the `TEST_ENV_LOCK` and restoring it on drop.
[crates/gcore/src/ai/daemon/tests.rs:15-24]
[crates/gcore/src/ai/daemon/tests.rs:26-29]
[crates/gcore/src/ai/daemon/tests.rs:31-38]
[crates/gcore/src/ai/daemon/tests.rs:40-42]
[crates/gcore/src/ai/daemon/tests.rs:44-46]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `spawn_server` | function | `fn spawn_server(response: &'static str) -> (u16, RequestHandle) {` | `spawn_server [function]` | `e45aa30d-af73-57f2-933f-7137f2dc251e` | 15-24 [crates/gcore/src/ai/daemon/tests.rs:15-24] | Indexed function `spawn_server` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:15-24] |
| `request_body_json` | function | `fn request_body_json(request: &str) -> serde_json::Value {` | `request_body_json [function]` | `1bd5e7cb-09cb-5caa-8f69-d63bf9995f1f` | 26-29 [crates/gcore/src/ai/daemon/tests.rs:26-29] | Indexed function `request_body_json` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:26-29] |
| `has_header` | function | `fn has_header(request: &str, name: &str, value: &str) -> bool {` | `has_header [function]` | `38fc88f5-dd60-5bd7-84d1-d0bd22ee3f63` | 31-38 [crates/gcore/src/ai/daemon/tests.rs:31-38] | Indexed function `has_header` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:31-38] |
| `multipart_has_field` | function | `fn multipart_has_field(request: &str, name: &str, value: &str) -> bool {` | `multipart_has_field [function]` | `db496884-0fb3-5980-aa7e-21f56ea4066c` | 40-42 [crates/gcore/src/ai/daemon/tests.rs:40-42] | Indexed function `multipart_has_field` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:40-42] |
| `temp_home` | function | `fn temp_home() -> tempfile::TempDir {` | `temp_home [function]` | `b4856859-5788-53d4-bade-e10f071785ad` | 44-46 [crates/gcore/src/ai/daemon/tests.rs:44-46] | Indexed function `temp_home` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:44-46] |
| `write_daemon_files` | function | `fn write_daemon_files(home: &Path, port: u16, token: &str) {` | `write_daemon_files [function]` | `609f8827-fe70-5a28-b7eb-d108e9ac597b` | 48-57 [crates/gcore/src/ai/daemon/tests.rs:48-57] | Indexed function `write_daemon_files` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:48-57] |
| `test_context` | function | `fn test_context(project_id: Option<&str>) -> AiContext {` | `test_context [function]` | `0f89d0b7-8ab9-5d37-9ce1-1c26fdc370eb` | 59-76 [crates/gcore/src/ai/daemon/tests.rs:59-76] | Indexed function `test_context` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:59-76] |
| `binding` | function | `fn binding() -> CapabilityBinding {` | `binding [function]` | `26a0f0e6-7e8c-5b93-97e1-3a8787a6a30f` | 78-91 [crates/gcore/src/ai/daemon/tests.rs:78-91] | Indexed function `binding` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:78-91] |
| `EnvGuard` | class | `struct EnvGuard {` | `EnvGuard [class]` | `e66f9531-5f14-596b-9b71-79667a322946` | 93-99 [crates/gcore/src/ai/daemon/tests.rs:93-99] | Indexed class `EnvGuard` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:93-99] |
| `EnvGuard::set_home` | method | `fn set_home(home: &Path) -> Self {` | `EnvGuard::set_home [method]` | `e071fd20-a387-530c-a03d-fa49be13d022` | 102-123 [crates/gcore/src/ai/daemon/tests.rs:102-123] | Indexed method `EnvGuard::set_home` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:102-123] |
| `EnvGuard::drop` | method | `fn drop(&mut self) {` | `EnvGuard::drop [method]` | `f1f018d4-5cd5-54f5-95e8-899673f18b1e` | 127-144 [crates/gcore/src/ai/daemon/tests.rs:127-144] | Indexed method `EnvGuard::drop` in `crates/gcore/src/ai/daemon/tests.rs`. [crates/gcore/src/ai/daemon/tests.rs:127-144] |
