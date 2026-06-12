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

`crates/gcore/src/local_backend.rs` exposes 17 indexed API symbols.
[crates/gcore/src/local_backend.rs:14-20]
[crates/gcore/src/local_backend.rs:24-31]
[crates/gcore/src/local_backend.rs:35-68]
[crates/gcore/src/local_backend.rs:72-76]
[crates/gcore/src/local_backend.rs:79-108]

## API Symbols

- `Backend` (class) component `Backend [class]` (`8f764ab9-4f93-51a5-b42d-1c8faa786352`) lines 14-20 [crates/gcore/src/local_backend.rs:14-20]
  - Signature: `pub struct Backend {`
  - Purpose: Indexed class `Backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:14-20]
- `detect_backend` (function) component `detect_backend [function]` (`b9767dd0-2887-52cc-af09-dd7c52656aa0`) lines 24-31 [crates/gcore/src/local_backend.rs:24-31]
  - Signature: `pub fn detect_backend(backends: &[Backend], timeout_ms: u64) -> Option<Backend> {`
  - Purpose: Indexed function `detect_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:24-31]
- `validate_backend` (function) component `validate_backend [function]` (`f37b7e76-f148-5739-9adb-5976aa54b8c8`) lines 35-68 [crates/gcore/src/local_backend.rs:35-68]
  - Signature: `pub fn validate_backend(backend: &Backend, timeout_ms: u64) -> bool {`
  - Purpose: Indexed function `validate_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:35-68]
- `HttpProbeTarget` (class) component `HttpProbeTarget [class]` (`9ad11345-29ca-5198-aa47-24c51bc78687`) lines 72-76 [crates/gcore/src/local_backend.rs:72-76]
  - Signature: `struct HttpProbeTarget {`
  - Purpose: Indexed class `HttpProbeTarget` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:72-76]
- `HttpProbeTarget` (class) component `HttpProbeTarget [class]` (`382ceeec-3b43-5f45-9eae-bf4815126a8a`) lines 79-108 [crates/gcore/src/local_backend.rs:79-108]
  - Signature: `impl HttpProbeTarget {`
  - Purpose: Indexed class `HttpProbeTarget` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:79-108]
- `HttpProbeTarget.parse` (method) component `HttpProbeTarget.parse [method]` (`c65da890-ac6a-57f9-a6b8-f62e6fe0da03`) lines 80-89 [crates/gcore/src/local_backend.rs:80-89]
  - Signature: `fn parse(url: &str) -> Option<Self> {`
  - Purpose: Indexed method `HttpProbeTarget.parse` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:80-89]
- `HttpProbeTarget.socket_addr` (method) component `HttpProbeTarget.socket_addr [method]` (`fd969576-6782-5812-b427-df729e9faad0`) lines 91-97 [crates/gcore/src/local_backend.rs:91-97]
  - Signature: `fn socket_addr(&self) -> String {`
  - Purpose: Indexed method `HttpProbeTarget.socket_addr` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:91-97]
- `HttpProbeTarget.host_header` (method) component `HttpProbeTarget.host_header [method]` (`de49af97-73c1-5891-a322-f7916f51412c`) lines 99-107 [crates/gcore/src/local_backend.rs:99-107]
  - Signature: `fn host_header(&self) -> String {`
  - Purpose: Indexed method `HttpProbeTarget.host_header` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:99-107]
- `parse_http_authority` (function) component `parse_http_authority [function]` (`5c31baf3-943e-5e41-9d9e-6c892ac2b1c3`) lines 111-137 [crates/gcore/src/local_backend.rs:111-137]
  - Signature: `fn parse_http_authority(authority: &str) -> Option<(String, u16)> {`
  - Purpose: Indexed function `parse_http_authority` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:111-137]
- `send_probe_request` (function) component `send_probe_request [function]` (`b99604bd-179d-5cdc-bd71-067b39970c27`) lines 140-191 [crates/gcore/src/local_backend.rs:140-191]
  - Signature: `fn send_probe_request(`
  - Purpose: Indexed function `send_probe_request` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:140-191]
- `parse_http_status` (function) component `parse_http_status [function]` (`d9d89016-4c48-520c-8c0c-a2b5e3736fea`) lines 194-202 [crates/gcore/src/local_backend.rs:194-202]
  - Signature: `fn parse_http_status(response: &[u8]) -> io::Result<u16> {`
  - Purpose: Indexed function `parse_http_status` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:194-202]
- `backend_probe_url` (function) component `backend_probe_url [function]` (`6142d51d-673b-59e4-be7f-69c10ca830a3`) lines 205-213 [crates/gcore/src/local_backend.rs:205-213]
  - Signature: `fn backend_probe_url(backend: &Backend) -> String {`
  - Purpose: Indexed function `backend_probe_url` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:205-213]
- `reachable_backend` (function) component `reachable_backend [function]` (`d52f5265-5eb9-5ed3-bed8-cec69fbda34f`) lines 224-248 [crates/gcore/src/local_backend.rs:224-248]
  - Signature: `fn reachable_backend() -> (Backend, thread::JoinHandle<String>) {`
  - Purpose: Indexed function `reachable_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:224-248]
- `unreachable_backend` (function) component `unreachable_backend [function]` (`eead3423-e4f6-5825-9daa-b098e6d2698b`) lines 250-257 [crates/gcore/src/local_backend.rs:250-257]
  - Signature: `fn unreachable_backend() -> Backend {`
  - Purpose: Indexed function `unreachable_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:250-257]
- `detects_first_reachable` (function) component `detects_first_reachable [function]` (`65b13197-c879-59bc-b136-bce5f2a62693`) lines 260-267 [crates/gcore/src/local_backend.rs:260-267]
  - Signature: `fn detects_first_reachable() {`
  - Purpose: Indexed function `detects_first_reachable` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:260-267]
- `probe_url_uses_exactly_one_separator` (function) component `probe_url_uses_exactly_one_separator [function]` (`6332435c-cf0f-5ff3-8e1e-bb5464bd91e4`) lines 270-288 [crates/gcore/src/local_backend.rs:270-288]
  - Signature: `fn probe_url_uses_exactly_one_separator() {`
  - Purpose: Indexed function `probe_url_uses_exactly_one_separator` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:270-288]
- `has_header` (function) component `has_header [function]` (`e6dfb3b6-2641-5cd5-9200-96defea0bed2`) lines 290-296 [crates/gcore/src/local_backend.rs:290-296]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Indexed function `has_header` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:290-296]

