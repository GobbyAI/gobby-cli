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

# crates/gcore/src/ai/daemon/transport.rs

Module: [[code/modules/crates/gcore/src/ai/daemon|crates/gcore/src/ai/daemon]]

## Purpose

Provides the transport helpers for talking to the AI daemon over HTTP. It builds a default `reqwest` blocking client, constructs daemon URLs by joining the configured base daemon URL with a request path, reads and validates the local CLI token from `gobby_home()/local_cli_token`, converts home-directory and request setup failures into `AiError::not_configured`, and attaches the token to outgoing requests via the `X-Gobby-Local-Token` header.
[crates/gcore/src/ai/daemon/transport.rs:8-12]
[crates/gcore/src/ai/daemon/transport.rs:14-20]
[crates/gcore/src/ai/daemon/transport.rs:22-38]
[crates/gcore/src/ai/daemon/transport.rs:40-42]
[crates/gcore/src/ai/daemon/transport.rs:44-46]

## API Symbols

- `daemon_client` (function) component `daemon_client [function]` (`f64a51c8-7a4f-57ab-a1f5-31b0ee0b3bbd`) lines 8-12 [crates/gcore/src/ai/daemon/transport.rs:8-12]
  - Signature: `pub(super) fn daemon_client() -> Result<Client, AiError> {`
  - Purpose: Constructs and returns a 'reqwest::Client' using the default builder configuration, mapping any build failure into 'AiError' via 'super::super::reqwest_error'. [crates/gcore/src/ai/daemon/transport.rs:8-12]
- `daemon_url` (function) component `daemon_url [function]` (`7e526542-d67a-54ff-8d22-549373bc2421`) lines 14-20 [crates/gcore/src/ai/daemon/transport.rs:14-20]
  - Signature: `pub(super) fn daemon_url(path: &str) -> String {`
  - Purpose: Constructs a daemon URL by taking the base URL from 'crate::daemon_url::daemon_url()', stripping any trailing '/', and concatenating the provided 'path' onto it. [crates/gcore/src/ai/daemon/transport.rs:14-20]
- `read_local_cli_token` (function) component `read_local_cli_token [function]` (`902072cf-7f4a-56f8-b1be-98b746c3e0c8`) lines 22-38 [crates/gcore/src/ai/daemon/transport.rs:22-38]
  - Signature: `pub(super) fn read_local_cli_token() -> Result<String, AiError> {`
  - Purpose: Reads the local CLI token file from 'gobby_home()/LOCAL_CLI_TOKEN_FILENAME', trims whitespace, and returns the token as 'String' or a 'not_configured' 'AiError' if the file is missing, unreadable, or empty. [crates/gcore/src/ai/daemon/transport.rs:22-38]
- `gobby_home` (function) component `gobby_home [function]` (`12983cec-4752-53d4-ae32-e2d1183ddbae`) lines 40-42 [crates/gcore/src/ai/daemon/transport.rs:40-42]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, AiError> {`
  - Purpose: Returns 'crate::gobby_home()' on success, and on failure converts the underlying error into 'AiError::not_configured(None, error.to_string())'. [crates/gcore/src/ai/daemon/transport.rs:40-42]
- `with_local_token` (function) component `with_local_token [function]` (`b56e9dc5-9017-5773-b34f-97d6c29d98bf`) lines 44-46 [crates/gcore/src/ai/daemon/transport.rs:44-46]
  - Signature: `pub(super) fn with_local_token(request: RequestBuilder, token: &str) -> RequestBuilder {`
  - Purpose: Adds the 'LOCAL_TOKEN_HEADER' HTTP header to the provided 'RequestBuilder' with the given token value and returns the updated builder. [crates/gcore/src/ai/daemon/transport.rs:44-46]

