---
title: crates/gcore/src/ai/daemon/transport.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon/transport.rs
  ranges:
  - 8-12
  - 14-20
  - 22-38
  - 40-42
  - 44-46
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/daemon/transport.rs:8-12](crates/gcore/src/ai/daemon/transport.rs#L8-L12), [crates/gcore/src/ai/daemon/transport.rs:14-20](crates/gcore/src/ai/daemon/transport.rs#L14-L20), [crates/gcore/src/ai/daemon/transport.rs:22-38](crates/gcore/src/ai/daemon/transport.rs#L22-L38), [crates/gcore/src/ai/daemon/transport.rs:40-42](crates/gcore/src/ai/daemon/transport.rs#L40-L42), [crates/gcore/src/ai/daemon/transport.rs:44-46](crates/gcore/src/ai/daemon/transport.rs#L44-L46)

</details>

# crates/gcore/src/ai/daemon/transport.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Provides small transport helpers for talking to the daemon with `reqwest`. It builds a blocking HTTP client, constructs daemon URLs from the shared base daemon URL plus a path, reads and validates the local CLI token from `gobby_home()/local_cli_token`, and attaches that token to requests through the `X-Gobby-Local-Token` header. Errors from client creation, filesystem access, and missing or empty tokens are normalized into `AiError::not_configured` or the crate’s reqwest error wrapper.
[crates/gcore/src/ai/daemon/transport.rs:8-12]
[crates/gcore/src/ai/daemon/transport.rs:14-20]
[crates/gcore/src/ai/daemon/transport.rs:22-38]
[crates/gcore/src/ai/daemon/transport.rs:40-42]
[crates/gcore/src/ai/daemon/transport.rs:44-46]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `daemon_client` | function | `pub(super) fn daemon_client() -> Result<Client, AiError> {` | `daemon_client [function]` | `f64a51c8-7a4f-57ab-a1f5-31b0ee0b3bbd` | 8-12 [crates/gcore/src/ai/daemon/transport.rs:8-12] | Indexed function `daemon_client` in `crates/gcore/src/ai/daemon/transport.rs`. [crates/gcore/src/ai/daemon/transport.rs:8-12] |
| `daemon_url` | function | `pub(super) fn daemon_url(path: &str) -> String {` | `daemon_url [function]` | `7e526542-d67a-54ff-8d22-549373bc2421` | 14-20 [crates/gcore/src/ai/daemon/transport.rs:14-20] | Indexed function `daemon_url` in `crates/gcore/src/ai/daemon/transport.rs`. [crates/gcore/src/ai/daemon/transport.rs:14-20] |
| `read_local_cli_token` | function | `pub(super) fn read_local_cli_token() -> Result<String, AiError> {` | `read_local_cli_token [function]` | `902072cf-7f4a-56f8-b1be-98b746c3e0c8` | 22-38 [crates/gcore/src/ai/daemon/transport.rs:22-38] | Indexed function `read_local_cli_token` in `crates/gcore/src/ai/daemon/transport.rs`. [crates/gcore/src/ai/daemon/transport.rs:22-38] |
| `gobby_home` | function | `fn gobby_home() -> Result<std::path::PathBuf, AiError> {` | `gobby_home [function]` | `12983cec-4752-53d4-ae32-e2d1183ddbae` | 40-42 [crates/gcore/src/ai/daemon/transport.rs:40-42] | Indexed function `gobby_home` in `crates/gcore/src/ai/daemon/transport.rs`. [crates/gcore/src/ai/daemon/transport.rs:40-42] |
| `with_local_token` | function | `pub(super) fn with_local_token(request: RequestBuilder, token: &str) -> RequestBuilder {` | `with_local_token [function]` | `b56e9dc5-9017-5773-b34f-97d6c29d98bf` | 44-46 [crates/gcore/src/ai/daemon/transport.rs:44-46] | Indexed function `with_local_token` in `crates/gcore/src/ai/daemon/transport.rs`. [crates/gcore/src/ai/daemon/transport.rs:44-46] |
