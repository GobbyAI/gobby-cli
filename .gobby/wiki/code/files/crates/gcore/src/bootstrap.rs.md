---
title: crates/gcore/src/bootstrap.rs
type: code_file
provenance:
- file: crates/gcore/src/bootstrap.rs
  ranges:
  - 33-36
  - 38-45
  - 39-44
  - 50-52
  - 58-63
  - 69-90
  - 99-103
  - 106-111
  - 114-119
  - 122-127
  - 130-137
  - 140-147
  - 150-155
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/bootstrap.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/bootstrap.rs` exposes 13 indexed API symbols.
[crates/gcore/src/bootstrap.rs:33-36]
[crates/gcore/src/bootstrap.rs:38-45]
[crates/gcore/src/bootstrap.rs:39-44]
[crates/gcore/src/bootstrap.rs:50-52]
[crates/gcore/src/bootstrap.rs:58-63]
[crates/gcore/src/bootstrap.rs:69-90]
[crates/gcore/src/bootstrap.rs:99-103]
[crates/gcore/src/bootstrap.rs:106-111]
[crates/gcore/src/bootstrap.rs:114-119]
[crates/gcore/src/bootstrap.rs:122-127]
[crates/gcore/src/bootstrap.rs:130-137]
[crates/gcore/src/bootstrap.rs:140-147]
[crates/gcore/src/bootstrap.rs:150-155]

## API Symbols

- `DaemonEndpoint` (class) component `DaemonEndpoint [class]` (`15ce0dd3-ad63-598e-969c-6746817a1946`) lines 33-36 [crates/gcore/src/bootstrap.rs:33-36]
  - Signature: `pub struct DaemonEndpoint {`
  - Purpose: `DaemonEndpoint` is a struct that encapsulates a daemon's network address, comprising a `String` hostname and a `u16` port number. [crates/gcore/src/bootstrap.rs:33-36]
- `DaemonEndpoint` (class) component `DaemonEndpoint [class]` (`b38e2dfd-ab3b-5e61-955a-11982175e067`) lines 38-45 [crates/gcore/src/bootstrap.rs:38-45]
  - Signature: `impl Default for DaemonEndpoint {`
  - Purpose: Default trait implementation for `DaemonEndpoint` that instantiates a daemon endpoint with `DEFAULT_BIND_HOST` and `DEFAULT_DAEMON_PORT` constants. [crates/gcore/src/bootstrap.rs:38-45]
- `DaemonEndpoint.default` (method) component `DaemonEndpoint.default [method]` (`d6b3a12f-8290-5b48-8674-32a807bda053`) lines 39-44 [crates/gcore/src/bootstrap.rs:39-44]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a Self instance initialized with `host` set to `DEFAULT_BIND_HOST` as a String and `port` set to `DEFAULT_DAEMON_PORT`. [crates/gcore/src/bootstrap.rs:39-44]
- `bootstrap_path` (function) component `bootstrap_path [function]` (`81f5b29d-e345-58bd-8c27-c5800f29ca72`) lines 50-52 [crates/gcore/src/bootstrap.rs:50-52]
  - Signature: `pub fn bootstrap_path() -> Option<PathBuf> {`
  - Purpose: Returns an `Option<PathBuf>` containing the absolute path to the bootstrap directory by joining the user's home directory with `BOOTSTRAP_RELATIVE_PATH`, or `None` if the home directory cannot be determined. [crates/gcore/src/bootstrap.rs:50-52]
- `read_daemon_endpoint` (function) component `read_daemon_endpoint [function]` (`7d07571b-4b7b-5d07-9ee5-3d46767e69b2`) lines 58-63 [crates/gcore/src/bootstrap.rs:58-63]
  - Signature: `pub fn read_daemon_endpoint() -> DaemonEndpoint {`
  - Purpose: Reads a `DaemonEndpoint` from the bootstrap path if available, otherwise returns `DaemonEndpoint::default()`. [crates/gcore/src/bootstrap.rs:58-63]
- `read_daemon_endpoint_at` (function) component `read_daemon_endpoint_at [function]` (`c81e7020-05ff-52dd-a765-cc9713124e1f`) lines 69-90 [crates/gcore/src/bootstrap.rs:69-90]
  - Signature: `pub fn read_daemon_endpoint_at(path: &Path) -> DaemonEndpoint {`
  - Purpose: Reads and parses a YAML configuration file at a given path to construct a `DaemonEndpoint` struct by extracting `daemon_port` (u16) and `bind_host` (String) fields, returning default values if the file cannot be accessed or parsed. [crates/gcore/src/bootstrap.rs:69-90]
- `missing_file_returns_defaults` (function) component `missing_file_returns_defaults [function]` (`a6a3576a-123c-503e-8146-e9fa1b3748e9`) lines 99-103 [crates/gcore/src/bootstrap.rs:99-103]
  - Signature: `fn missing_file_returns_defaults() {`
  - Purpose: A unit test that verifies `read_daemon_endpoint_at()` returns a `DaemonEndpoint::default()` instance when invoked with a non-existent file path. [crates/gcore/src/bootstrap.rs:99-103]
- `malformed_yaml_returns_defaults` (function) component `malformed_yaml_returns_defaults [function]` (`c03cf615-d33c-5c5c-a762-166714e7f845`) lines 106-111 [crates/gcore/src/bootstrap.rs:106-111]
  - Signature: `fn malformed_yaml_returns_defaults() {`
  - Purpose: This unit test verifies that `read_daemon_endpoint_at()` gracefully returns a default `DaemonEndpoint` instance when parsing a malformed YAML file. [crates/gcore/src/bootstrap.rs:106-111]
- `empty_file_returns_defaults` (function) component `empty_file_returns_defaults [function]` (`03b92131-f127-5d88-9de5-8832debd83f6`) lines 114-119 [crates/gcore/src/bootstrap.rs:114-119]
  - Signature: `fn empty_file_returns_defaults() {`
  - Purpose: This is a unit test that verifies `read_daemon_endpoint_at()` returns a default `DaemonEndpoint` instance when reading an empty YAML file. [crates/gcore/src/bootstrap.rs:114-119]
- `missing_fields_return_defaults` (function) component `missing_fields_return_defaults [function]` (`1600cb49-51e5-5823-9e3c-bb1f16a47532`) lines 122-127 [crates/gcore/src/bootstrap.rs:122-127]
  - Signature: `fn missing_fields_return_defaults() {`
  - Purpose: Tests that `read_daemon_endpoint_at` returns `DaemonEndpoint::default()` when parsing a YAML file with missing required daemon endpoint configuration fields. [crates/gcore/src/bootstrap.rs:122-127]
- `reads_custom_port` (function) component `reads_custom_port [function]` (`6233a04d-158a-5087-ac15-f7da470cfbd9`) lines 130-137 [crates/gcore/src/bootstrap.rs:130-137]
  - Signature: `fn reads_custom_port() {`
  - Purpose: Unit test that verifies `read_daemon_endpoint_at()` correctly deserializes a custom daemon port value from a YAML configuration file while preserving the default host binding. [crates/gcore/src/bootstrap.rs:130-137]
- `reads_custom_host_and_port` (function) component `reads_custom_host_and_port [function]` (`bc726c9d-2e86-5e3b-af88-22b656710eba`) lines 140-147 [crates/gcore/src/bootstrap.rs:140-147]
  - Signature: `fn reads_custom_host_and_port() {`
  - Purpose: Tests that `read_daemon_endpoint_at` correctly parses custom daemon port (60887) and bind host (0.0.0.0) from a bootstrap.yaml configuration file. [crates/gcore/src/bootstrap.rs:140-147]
- `out_of_range_port_falls_back` (function) component `out_of_range_port_falls_back [function]` (`63f13c1e-add3-5440-94f3-c43d246030a4`) lines 150-155 [crates/gcore/src/bootstrap.rs:150-155]
  - Signature: `fn out_of_range_port_falls_back() {`
  - Purpose: This test validates that `read_daemon_endpoint_at` falls back to `DEFAULT_DAEMON_PORT` when parsing a daemon_port value exceeding the valid port range. [crates/gcore/src/bootstrap.rs:150-155]

