---
title: crates/gcore/src/daemon_url.rs
type: code_file
provenance:
- file: crates/gcore/src/daemon_url.rs
  ranges:
  - 15-17
  - 22-24
  - 26-29
  - 38-43
  - 51-56
  - 59-63
  - 66-69
  - 72-79
  - 82-89
  - 92-95
  - 98-101
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/daemon_url.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/daemon_url.rs` exposes 11 indexed API symbols.
[crates/gcore/src/daemon_url.rs:15-17]
[crates/gcore/src/daemon_url.rs:22-24]
[crates/gcore/src/daemon_url.rs:26-29]
[crates/gcore/src/daemon_url.rs:38-43]
[crates/gcore/src/daemon_url.rs:51-56]

## API Symbols

- `daemon_url` (function) component `daemon_url [function]` (`77c90aec-890d-55f3-8677-ef2dbedd1928`) lines 15-17 [crates/gcore/src/daemon_url.rs:15-17]
  - Signature: `pub fn daemon_url() -> String {`
  - Purpose: This function reads the daemon endpoint from configuration and converts it to a URL string. [crates/gcore/src/daemon_url.rs:15-17]
- `daemon_url_at` (function) component `daemon_url_at [function]` (`74c8f034-23be-57b0-8366-93d2f619b1c7`) lines 22-24 [crates/gcore/src/daemon_url.rs:22-24]
  - Signature: `pub fn daemon_url_at(path: &Path) -> String {`
  - Purpose: Reads a daemon endpoint configuration from the specified file path and converts it to a URL string. [crates/gcore/src/daemon_url.rs:22-24]
- `endpoint_to_url` (function) component `endpoint_to_url [function]` (`1d2e623e-69e7-5d6e-ab1b-5b70dcc154ea`) lines 26-29 [crates/gcore/src/daemon_url.rs:26-29]
  - Signature: `fn endpoint_to_url(endpoint: &DaemonEndpoint) -> String {`
  - Purpose: Constructs an HTTP URL string from a `DaemonEndpoint` by resolving its host through `dial_host()` and combining it with its port number. [crates/gcore/src/daemon_url.rs:26-29]
- `dial_host` (function) component `dial_host [function]` (`237dfb56-36e3-59b3-875f-945c6043f985`) lines 38-43 [crates/gcore/src/daemon_url.rs:38-43]
  - Signature: `fn dial_host(host: &str) -> &str {`
  - Purpose: Remaps wildcard addresses (0.0.0.0, ::, ::0) to the localhost address 127.0.0.1, passing through all other hosts unchanged. [crates/gcore/src/daemon_url.rs:38-43]
- `write_bootstrap` (function) component `write_bootstrap [function]` (`d41c75f1-4154-5e9e-a244-da66b9573c65`) lines 51-56 [crates/gcore/src/daemon_url.rs:51-56]
  - Signature: `fn write_bootstrap(contents: &str) -> (tempfile::TempDir, std::path::PathBuf) {`
  - Purpose: Creates a temporary directory containing a `bootstrap.yaml` file with the provided contents and returns a tuple of the temporary directory and file path. [crates/gcore/src/daemon_url.rs:51-56]
- `default_url_when_file_missing` (function) component `default_url_when_file_missing [function]` (`537dd631-5cf1-58fb-8d83-641e6669b34c`) lines 59-63 [crates/gcore/src/daemon_url.rs:59-63]
  - Signature: `fn default_url_when_file_missing() {`
  - Purpose: Tests that `daemon_url_at()` returns the default daemon URL `"http://127.0.0.1:60887"` when called with a non-existent file path. [crates/gcore/src/daemon_url.rs:59-63]
- `wildcard_ipv4_normalizes_to_loopback` (function) component `wildcard_ipv4_normalizes_to_loopback [function]` (`fe0c0b0b-f1ae-5151-83a9-fe2aae5931c7`) lines 66-69 [crates/gcore/src/daemon_url.rs:66-69]
  - Signature: `fn wildcard_ipv4_normalizes_to_loopback() {`
  - Purpose: This test verifies that a wildcard IPv4 bind address (0.0.0.0) normalizes to the loopback address (127.0.0.1) when constructing the daemon URL. [crates/gcore/src/daemon_url.rs:66-69]
- `wildcard_ipv6_normalizes_to_loopback` (function) component `wildcard_ipv6_normalizes_to_loopback [function]` (`a17ab5d0-b8e2-538b-85d9-da3ae06e235a`) lines 72-79 [crates/gcore/src/daemon_url.rs:72-79]
  - Signature: `fn wildcard_ipv6_normalizes_to_loopback() {`
  - Purpose: This function asserts that a daemon configured to bind to the IPv6 wildcard address `::` normalizes its URL to the IPv4 loopback address `http://127.0.0.1:60887`. [crates/gcore/src/daemon_url.rs:72-79]
- `wildcard_ipv6_zero_normalizes_to_loopback` (function) component `wildcard_ipv6_zero_normalizes_to_loopback [function]` (`8e6649d6-4f18-5836-be2b-1d4a3bb4aa6d`) lines 82-89 [crates/gcore/src/daemon_url.rs:82-89]
  - Signature: `fn wildcard_ipv6_zero_normalizes_to_loopback() {`
  - Purpose: This test verifies that a daemon configured with wildcard IPv6 bind address `::0` normalizes its URL to the IPv4 loopback address `127.0.0.1:60887`. [crates/gcore/src/daemon_url.rs:82-89]
- `localhost_passes_through` (function) component `localhost_passes_through [function]` (`0c144c58-3159-5bdc-9dc2-515fb1483fd2`) lines 92-95 [crates/gcore/src/daemon_url.rs:92-95]
  - Signature: `fn localhost_passes_through() {`
  - Purpose: This function tests that `daemon_url_at()` correctly constructs the URL `http://localhost:60887` when parsing a bootstrap configuration with `daemon_port: 60887` and `bind_host: localhost`. [crates/gcore/src/daemon_url.rs:92-95]
- `custom_port_and_host_compose` (function) component `custom_port_and_host_compose [function]` (`b11a8d54-a1e7-557e-88dc-03456a5e5a5d`) lines 98-101 [crates/gcore/src/daemon_url.rs:98-101]
  - Signature: `fn custom_port_and_host_compose() {`
  - Purpose: Tests that `daemon_url_at()` correctly composes an HTTP daemon URL from custom port and bind host values specified in the bootstrap configuration. [crates/gcore/src/daemon_url.rs:98-101]

