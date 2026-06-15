---
title: crates/gcore/src/local_backend.rs
type: code_file
provenance:
- file: crates/gcore/src/local_backend.rs
  ranges:
  - 14-20
  - 24-31
  - 35-68
  - 72-76
  - 79-108
  - 111-137
  - 140-191
  - 194-202
  - 205-213
  - 224-248
  - 250-257
  - 260-267
  - 270-288
  - 290-296
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/local_backend.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file implements optional local-backend discovery and probing for the `local-backend` feature. It defines a serializable `Backend` descriptor, then `detect_backend` walks a list in order and returns the first backend that passes `validate_backend`, which builds the probe URL, parses it into an HTTP target, sends a timed GET probe with an optional Bearer token, and accepts only 2xx responses. The supporting `HttpProbeTarget`, authority/URL parsing, status parsing, and probe-request helpers handle HTTP formatting details such as IPv6 bracket syntax, `Host` header construction, and normalizing `url + probe` joins, while the test helpers exercise reachability, header injection, and URL normalization.
[crates/gcore/src/local_backend.rs:14-20]
[crates/gcore/src/local_backend.rs:24-31]
[crates/gcore/src/local_backend.rs:35-68]
[crates/gcore/src/local_backend.rs:72-76]
[crates/gcore/src/local_backend.rs:79-108]

## API Symbols

- `Backend` (class) component `Backend [class]` (`8f764ab9-4f93-51a5-b42d-1c8faa786352`) lines 14-20 [crates/gcore/src/local_backend.rs:14-20]
  - Signature: `pub struct Backend {`
  - Purpose: 'Backend' is a serializable Rust struct that models a backend endpoint with a 'name', 'url', 'probe' string, and an optional 'auth_token' field that defaults to an empty string when deserialized. [crates/gcore/src/local_backend.rs:14-20]
- `detect_backend` (function) component `detect_backend [function]` (`b9767dd0-2887-52cc-af09-dd7c52656aa0`) lines 24-31 [crates/gcore/src/local_backend.rs:24-31]
  - Signature: `pub fn detect_backend(backends: &[Backend], timeout_ms: u64) -> Option<Backend> {`
  - Purpose: Iterates through 'backends' in order, returns the first 'Backend' whose 'validate_backend' check succeeds within 'timeout_ms' by cloning it, and returns 'None' if no backend validates. [crates/gcore/src/local_backend.rs:24-31]
- `validate_backend` (function) component `validate_backend [function]` (`f37b7e76-f148-5739-9adb-5976aa54b8c8`) lines 35-68 [crates/gcore/src/local_backend.rs:35-68]
  - Signature: `pub fn validate_backend(backend: &Backend, timeout_ms: u64) -> bool {`
  - Purpose: 'validate_backend' builds a probe URL for the given backend, parses it as an HTTP target, sends a probe request with the backend’s trimmed auth token and the specified timeout, and returns 'true' only when the request succeeds with a 2xx status, otherwise logging a trace and returning 'false'. [crates/gcore/src/local_backend.rs:35-68]
- `HttpProbeTarget` (class) component `HttpProbeTarget [class]` (`9ad11345-29ca-5198-aa47-24c51bc78687`) lines 72-76 [crates/gcore/src/local_backend.rs:72-76]
  - Signature: `struct HttpProbeTarget {`
  - Purpose: 'HttpProbeTarget' is a data structure that identifies an HTTP probe endpoint by 'host', 'port', and request 'path'. [crates/gcore/src/local_backend.rs:72-76]
- `HttpProbeTarget` (class) component `HttpProbeTarget [class]` (`382ceeec-3b43-5f45-9eae-bf4815126a8a`) lines 79-108 [crates/gcore/src/local_backend.rs:79-108]
  - Signature: `impl HttpProbeTarget {`
  - Purpose: 'HttpProbeTarget' parses an 'http://' URL into 'host', 'port', and normalized 'path', and provides socket-address and HTTP 'Host' header formatting with IPv6 bracket handling and port elision for default port 80. [crates/gcore/src/local_backend.rs:79-108]
- `HttpProbeTarget.parse` (method) component `HttpProbeTarget.parse [method]` (`c65da890-ac6a-57f9-a6b8-f62e6fe0da03`) lines 80-89 [crates/gcore/src/local_backend.rs:80-89]
  - Signature: `fn parse(url: &str) -> Option<Self> {`
  - Purpose: Parses an 'http://' URL by stripping the scheme, splitting the remainder into authority and path, decoding the authority into 'host' and 'port', and returning 'Self' with 'path' normalized to a leading slash, or 'None' if the scheme or authority is invalid. [crates/gcore/src/local_backend.rs:80-89]
- `HttpProbeTarget.socket_addr` (method) component `HttpProbeTarget.socket_addr [method]` (`fd969576-6782-5812-b427-df729e9faad0`) lines 91-97 [crates/gcore/src/local_backend.rs:91-97]
  - Signature: `fn socket_addr(&self) -> String {`
  - Purpose: Returns the host and port as a socket address string, wrapping the host in brackets when it contains ':' so IPv6 literals are formatted correctly. [crates/gcore/src/local_backend.rs:91-97]
- `HttpProbeTarget.host_header` (method) component `HttpProbeTarget.host_header [method]` (`de49af97-73c1-5891-a322-f7916f51412c`) lines 99-107 [crates/gcore/src/local_backend.rs:99-107]
  - Signature: `fn host_header(&self) -> String {`
  - Purpose: Returns the HTTP 'Host' header value by emitting the bare host for port 80, wrapping IPv6 literals in brackets with the port appended for non-80 ports, and otherwise formatting 'host:port'. [crates/gcore/src/local_backend.rs:99-107]
- `parse_http_authority` (function) component `parse_http_authority [function]` (`5c31baf3-943e-5e41-9d9e-6c892ac2b1c3`) lines 111-137 [crates/gcore/src/local_backend.rs:111-137]
  - Signature: `fn parse_http_authority(authority: &str) -> Option<(String, u16)> {`
  - Purpose: Parses an HTTP authority string into a '(host, port)' pair by rejecting empty, userinfo-bearing, or malformed bracketed/colon forms, accepting IPv6 literals in '[...]' with an optional ':port', and defaulting the port to '80' when absent. [crates/gcore/src/local_backend.rs:111-137]
- `send_probe_request` (function) component `send_probe_request [function]` (`b99604bd-179d-5cdc-bd71-067b39970c27`) lines 140-191 [crates/gcore/src/local_backend.rs:140-191]
  - Signature: `fn send_probe_request(`
  - Purpose: Resolves the target host, opens a TCP connection with the given timeout, sends an HTTP/1.1 'GET' probe request with optional Bearer auth, then reads up to the first response line and returns the parsed HTTP status code as 'io::Result<u16>'. [crates/gcore/src/local_backend.rs:140-191]
- `parse_http_status` (function) component `parse_http_status [function]` (`d9d89016-4c48-520c-8c0c-a2b5e3736fea`) lines 194-202 [crates/gcore/src/local_backend.rs:194-202]
  - Signature: `fn parse_http_status(response: &[u8]) -> io::Result<u16> {`
  - Purpose: Parses the first line of an HTTP response as UTF-8 lossily, extracts the second whitespace-delimited token as the status code, and returns it as 'u16' or an 'InvalidData' I/O error if the status is missing or unparsable. [crates/gcore/src/local_backend.rs:194-202]
- `backend_probe_url` (function) component `backend_probe_url [function]` (`6142d51d-673b-59e4-be7f-69c10ca830a3`) lines 205-213 [crates/gcore/src/local_backend.rs:205-213]
  - Signature: `fn backend_probe_url(backend: &Backend) -> String {`
  - Purpose: Returns the backend’s probe URL by removing trailing slashes from 'backend.url', removing leading slashes from 'backend.probe', and joining them with a single '/' unless the probe path is empty, in which case it returns the base URL unchanged. [crates/gcore/src/local_backend.rs:205-213]
- `reachable_backend` (function) component `reachable_backend [function]` (`d52f5265-5eb9-5ed3-bed8-cec69fbda34f`) lines 224-248 [crates/gcore/src/local_backend.rs:224-248]
  - Signature: `fn reachable_backend() -> (Backend, thread::JoinHandle<String>) {`
  - Purpose: Creates a loopback TCP listener on an ephemeral port, spawns a thread that accepts one HTTP request and replies with '200 OK' while capturing the request bytes, and returns a 'Backend' configured to probe 'http://<addr>/v1/models' with a fixed auth token plus the join handle. [crates/gcore/src/local_backend.rs:224-248]
- `unreachable_backend` (function) component `unreachable_backend [function]` (`eead3423-e4f6-5825-9daa-b098e6d2698b`) lines 250-257 [crates/gcore/src/local_backend.rs:250-257]
  - Signature: `fn unreachable_backend() -> Backend {`
  - Purpose: Returns a 'Backend' descriptor named 'unreachable' that points to 'http://127.0.0.1:9' with probe path '/' and an empty auth token. [crates/gcore/src/local_backend.rs:250-257]
- `detects_first_reachable` (function) component `detects_first_reachable [function]` (`65b13197-c879-59bc-b136-bce5f2a62693`) lines 260-267 [crates/gcore/src/local_backend.rs:260-267]
  - Signature: `fn detects_first_reachable() {`
  - Purpose: Verifies that 'detect_backend' returns the first reachable backend from a list within the timeout and that the probe request includes the 'Authorization: Bearer token' header. [crates/gcore/src/local_backend.rs:260-267]
- `probe_url_uses_exactly_one_separator` (function) component `probe_url_uses_exactly_one_separator [function]` (`6332435c-cf0f-5ff3-8e1e-bb5464bd91e4`) lines 270-288 [crates/gcore/src/local_backend.rs:270-288]
  - Signature: `fn probe_url_uses_exactly_one_separator() {`
  - Purpose: Verifies that 'backend_probe_url' normalizes URL/probe concatenation to use exactly one '/' separator, and omits the trailing slash entirely when the probe path is empty. [crates/gcore/src/local_backend.rs:270-288]
- `has_header` (function) component `has_header [function]` (`e6dfb3b6-2641-5cd5-9200-96defea0bed2`) lines 290-296 [crates/gcore/src/local_backend.rs:290-296]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Returns 'true' if any line in 'request' contains a 'name: value' header whose field name matches 'name' case-insensitively after trimming and whose trimmed field value exactly equals 'value'; otherwise returns 'false'. [crates/gcore/src/local_backend.rs:290-296]

