---
title: crates/gcore/src/local_backend.rs
type: code_file
provenance:
- file: crates/gcore/src/local_backend.rs
  ranges:
  - 14-20
  - 23-28
  - 30-39
  - 31-38
  - 56-62
  - 64-66
  - 70-77
  - 81-114
  - 118-122
  - 125-154
  - 126-135
  - 137-143
  - 145-153
  - 157-183
  - 186-237
  - 240-248
  - 251-259
  - 266-272
  - 281-305
  - 307-314
  - 317-324
  - 327-345
  - 347-353
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/local_backend.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/local_backend.rs` exposes 23 indexed API symbols.
[crates/gcore/src/local_backend.rs:14-20]
[crates/gcore/src/local_backend.rs:23-28]
[crates/gcore/src/local_backend.rs:30-39]
[crates/gcore/src/local_backend.rs:31-38]
[crates/gcore/src/local_backend.rs:56-62]
[crates/gcore/src/local_backend.rs:64-66]
[crates/gcore/src/local_backend.rs:70-77]
[crates/gcore/src/local_backend.rs:81-114]
[crates/gcore/src/local_backend.rs:118-122]
[crates/gcore/src/local_backend.rs:125-154]
[crates/gcore/src/local_backend.rs:126-135]
[crates/gcore/src/local_backend.rs:137-143]
[crates/gcore/src/local_backend.rs:145-153]
[crates/gcore/src/local_backend.rs:157-183]
[crates/gcore/src/local_backend.rs:186-237]
[crates/gcore/src/local_backend.rs:240-248]
[crates/gcore/src/local_backend.rs:251-259]
[crates/gcore/src/local_backend.rs:266-272]
[crates/gcore/src/local_backend.rs:281-305]
[crates/gcore/src/local_backend.rs:307-314]
[crates/gcore/src/local_backend.rs:317-324]
[crates/gcore/src/local_backend.rs:327-345]
[crates/gcore/src/local_backend.rs:347-353]

## API Symbols

- `Backend` (class) component `Backend [class]` (`8f764ab9-4f93-51a5-b42d-1c8faa786352`) lines 14-20 [crates/gcore/src/local_backend.rs:14-20]
  - Signature: `pub struct Backend {`
  - Purpose: Indexed class `Backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:14-20]
- `BackendDefault` (class) component `BackendDefault [class]` (`06733738-8526-5bf9-9e8d-005f571dacb3`) lines 23-28 [crates/gcore/src/local_backend.rs:23-28]
  - Signature: `pub struct BackendDefault {`
  - Purpose: Indexed class `BackendDefault` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:23-28]
- `BackendDefault` (class) component `BackendDefault [class]` (`14dd1c84-3da6-529b-87e0-ed9964879410`) lines 30-39 [crates/gcore/src/local_backend.rs:30-39]
  - Signature: `impl BackendDefault {`
  - Purpose: Indexed class `BackendDefault` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:30-39]
- `BackendDefault.to_backend` (method) component `BackendDefault.to_backend [method]` (`63354b9c-6e35-5e53-92df-b65783487364`) lines 31-38 [crates/gcore/src/local_backend.rs:31-38]
  - Signature: `pub fn to_backend(self) -> Backend {`
  - Purpose: Indexed method `BackendDefault.to_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:31-38]
- `default_backends` (function) component `default_backends [function]` (`ee81e33c-d1f4-5c82-846f-8ae5427081e9`) lines 56-62 [crates/gcore/src/local_backend.rs:56-62]
  - Signature: `pub fn default_backends() -> Vec<Backend> {`
  - Purpose: Indexed function `default_backends` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:56-62]
- `backend_api_base` (function) component `backend_api_base [function]` (`31641bc9-fd97-5c26-9fa8-bd8ed78b5703`) lines 64-66 [crates/gcore/src/local_backend.rs:64-66]
  - Signature: `pub fn backend_api_base(backend: &Backend) -> String {`
  - Purpose: Indexed function `backend_api_base` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:64-66]
- `detect_backend` (function) component `detect_backend [function]` (`9d4f4cce-4f01-544d-8e0a-acda12a4f2cb`) lines 70-77 [crates/gcore/src/local_backend.rs:70-77]
  - Signature: `pub fn detect_backend(backends: &[Backend], timeout_ms: u64) -> Option<Backend> {`
  - Purpose: Indexed function `detect_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:70-77]
- `validate_backend` (function) component `validate_backend [function]` (`5dd83892-2cf8-5b9b-9751-d1dae8592455`) lines 81-114 [crates/gcore/src/local_backend.rs:81-114]
  - Signature: `pub fn validate_backend(backend: &Backend, timeout_ms: u64) -> bool {`
  - Purpose: Indexed function `validate_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:81-114]
- `HttpProbeTarget` (class) component `HttpProbeTarget [class]` (`11ac7e5f-7a79-5804-92df-dae687c177dc`) lines 118-122 [crates/gcore/src/local_backend.rs:118-122]
  - Signature: `struct HttpProbeTarget {`
  - Purpose: Indexed class `HttpProbeTarget` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:118-122]
- `HttpProbeTarget` (class) component `HttpProbeTarget [class]` (`2121337e-81b5-575b-a8f0-d941edf97795`) lines 125-154 [crates/gcore/src/local_backend.rs:125-154]
  - Signature: `impl HttpProbeTarget {`
  - Purpose: Indexed class `HttpProbeTarget` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:125-154]
- `HttpProbeTarget.parse` (method) component `HttpProbeTarget.parse [method]` (`96df3436-154d-535f-84d5-6ab69adc2568`) lines 126-135 [crates/gcore/src/local_backend.rs:126-135]
  - Signature: `fn parse(url: &str) -> Option<Self> {`
  - Purpose: Indexed method `HttpProbeTarget.parse` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:126-135]
- `HttpProbeTarget.socket_addr` (method) component `HttpProbeTarget.socket_addr [method]` (`d5950e34-ec06-5636-81c5-ccf9534ba64f`) lines 137-143 [crates/gcore/src/local_backend.rs:137-143]
  - Signature: `fn socket_addr(&self) -> String {`
  - Purpose: Indexed method `HttpProbeTarget.socket_addr` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:137-143]
- `HttpProbeTarget.host_header` (method) component `HttpProbeTarget.host_header [method]` (`af3e1f61-706a-5e5c-ad6b-11c36e81da05`) lines 145-153 [crates/gcore/src/local_backend.rs:145-153]
  - Signature: `fn host_header(&self) -> String {`
  - Purpose: Indexed method `HttpProbeTarget.host_header` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:145-153]
- `parse_http_authority` (function) component `parse_http_authority [function]` (`6db72fe0-3552-59df-a6f8-d38ca5c8b1e6`) lines 157-183 [crates/gcore/src/local_backend.rs:157-183]
  - Signature: `fn parse_http_authority(authority: &str) -> Option<(String, u16)> {`
  - Purpose: Indexed function `parse_http_authority` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:157-183]
- `send_probe_request` (function) component `send_probe_request [function]` (`0096bbf1-3d6d-5189-bbb9-15bebabb1a81`) lines 186-237 [crates/gcore/src/local_backend.rs:186-237]
  - Signature: `fn send_probe_request(`
  - Purpose: Indexed function `send_probe_request` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:186-237]
- `parse_http_status` (function) component `parse_http_status [function]` (`4cbf0ad0-8a0d-5509-aad3-790de1271fb2`) lines 240-248 [crates/gcore/src/local_backend.rs:240-248]
  - Signature: `fn parse_http_status(response: &[u8]) -> io::Result<u16> {`
  - Purpose: Indexed function `parse_http_status` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:240-248]
- `backend_probe_url` (function) component `backend_probe_url [function]` (`77f0a43b-7080-5015-99f1-1ebbaba180ae`) lines 251-259 [crates/gcore/src/local_backend.rs:251-259]
  - Signature: `fn backend_probe_url(backend: &Backend) -> String {`
  - Purpose: Indexed function `backend_probe_url` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:251-259]
- `default_local_backends_do_not_send_auth_tokens` (function) component `default_local_backends_do_not_send_auth_tokens [function]` (`6f3142b2-82cd-57c3-adaa-27d23e975e93`) lines 266-272 [crates/gcore/src/local_backend.rs:266-272]
  - Signature: `fn default_local_backends_do_not_send_auth_tokens() {`
  - Purpose: Indexed function `default_local_backends_do_not_send_auth_tokens` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:266-272]
- `reachable_backend` (function) component `reachable_backend [function]` (`46d5bf9a-4f18-5142-9fbf-d9e096607484`) lines 281-305 [crates/gcore/src/local_backend.rs:281-305]
  - Signature: `fn reachable_backend() -> (Backend, thread::JoinHandle<String>) {`
  - Purpose: Indexed function `reachable_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:281-305]
- `unreachable_backend` (function) component `unreachable_backend [function]` (`38a3ff64-7f46-5ed4-b489-50bd9524a16c`) lines 307-314 [crates/gcore/src/local_backend.rs:307-314]
  - Signature: `fn unreachable_backend() -> Backend {`
  - Purpose: Indexed function `unreachable_backend` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:307-314]
- `detects_first_reachable` (function) component `detects_first_reachable [function]` (`b60afff1-a8a8-57a5-9598-a86acf7264b8`) lines 317-324 [crates/gcore/src/local_backend.rs:317-324]
  - Signature: `fn detects_first_reachable() {`
  - Purpose: Indexed function `detects_first_reachable` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:317-324]
- `probe_url_uses_exactly_one_separator` (function) component `probe_url_uses_exactly_one_separator [function]` (`6e3e7b71-ecd9-5a35-8ef4-8c80f79f47b3`) lines 327-345 [crates/gcore/src/local_backend.rs:327-345]
  - Signature: `fn probe_url_uses_exactly_one_separator() {`
  - Purpose: Indexed function `probe_url_uses_exactly_one_separator` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:327-345]
- `has_header` (function) component `has_header [function]` (`ebf1ded2-59f5-578b-868e-0356607950bf`) lines 347-353 [crates/gcore/src/local_backend.rs:347-353]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Indexed function `has_header` in `crates/gcore/src/local_backend.rs`. [crates/gcore/src/local_backend.rs:347-353]

