---
title: crates/gcore/src/bootstrap.rs
type: code_file
provenance:
- file: crates/gcore/src/bootstrap.rs
  ranges:
  - 33-36
  - 38-45
  - 52-54
  - 60-65
  - 71-92
  - 101-105
  - 108-113
  - 116-121
  - 124-129
  - 132-139
  - 142-149
  - 152-157
  - 160-178
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/bootstrap.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file resolves Gobby’s bootstrap configuration and turns it into a daemon endpoint. It defines `DaemonEndpoint` as the raw advertised host and port, with a `Default` that falls back to `127.0.0.1:60887`. `bootstrap_path()` builds `bootstrap.yaml` under `GOBBY_HOME` or `~/.gobby`, and `read_daemon_endpoint()` uses that path to load the endpoint, returning defaults whenever the file is missing, unreadable, malformed, or incomplete. `read_daemon_endpoint_at()` does the YAML parsing and field extraction, while the tests verify the fallback behavior and that custom host/port values and `GOBBY_HOME` resolution are handled correctly.
[crates/gcore/src/bootstrap.rs:33-36]
[crates/gcore/src/bootstrap.rs:38-45]
[crates/gcore/src/bootstrap.rs:39-44]
[crates/gcore/src/bootstrap.rs:52-54]
[crates/gcore/src/bootstrap.rs:60-65]

## API Symbols

- `DaemonEndpoint` (class) component `DaemonEndpoint [class]` (`c3b26eba-26b7-5f88-a97e-86c91fff7a89`) lines 33-36 [crates/gcore/src/bootstrap.rs:33-36]
  - Signature: `pub struct DaemonEndpoint {`
  - Purpose: `DaemonEndpoint` is a struct that holds the host address and port number required to establish a connection to a daemon service. [crates/gcore/src/bootstrap.rs:33-36]
- `DaemonEndpoint` (class) component `DaemonEndpoint [class]` (`a1bc4f64-7a5c-5beb-aec8-eaa0abb83786`) lines 38-45 [crates/gcore/src/bootstrap.rs:38-45]
  - Signature: `impl Default for DaemonEndpoint {`
  - Purpose: Implements the `Default` trait for `DaemonEndpoint`, constructing an instance with `DEFAULT_BIND_HOST` as the host and `DEFAULT_DAEMON_PORT` as the port. [crates/gcore/src/bootstrap.rs:38-45]
- `DaemonEndpoint.default` (method) component `DaemonEndpoint.default [method]` (`15e6892c-5428-56cb-9bde-eaba7533a6c2`) lines 39-44 [crates/gcore/src/bootstrap.rs:39-44]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a default Self instance initialized with DEFAULT_BIND_HOST (converted to a String) and DEFAULT_DAEMON_PORT constants. [crates/gcore/src/bootstrap.rs:39-44]
- `bootstrap_path` (function) component `bootstrap_path [function]` (`4e951fc6-cdc9-5aa5-b9ca-92f54b8225ef`) lines 52-54 [crates/gcore/src/bootstrap.rs:52-54]
  - Signature: `pub fn bootstrap_path() -> Option<PathBuf> {`
  - Purpose: Constructs and returns an optional path to the bootstrap file by joining the gobby home directory with a constant filename, or None if the home directory resolution fails. [crates/gcore/src/bootstrap.rs:52-54]
- `read_daemon_endpoint` (function) component `read_daemon_endpoint [function]` (`22f97c9c-6948-52ff-8ffe-da158404bd06`) lines 60-65 [crates/gcore/src/bootstrap.rs:60-65]
  - Signature: `pub fn read_daemon_endpoint() -> DaemonEndpoint {`
  - Purpose: Reads a `DaemonEndpoint` from the bootstrap path if it exists, otherwise returns the default `DaemonEndpoint`. [crates/gcore/src/bootstrap.rs:60-65]
- `read_daemon_endpoint_at` (function) component `read_daemon_endpoint_at [function]` (`de617fe1-f5a2-5a5a-8b87-ff13183efa7c`) lines 71-92 [crates/gcore/src/bootstrap.rs:71-92]
  - Signature: `pub fn read_daemon_endpoint_at(path: &Path) -> DaemonEndpoint {`
  - Purpose: Reads a YAML configuration file at the specified path and extracts daemon endpoint configuration (port and bind host) into a `DaemonEndpoint` struct, returning defaults if file reading or parsing fails. [crates/gcore/src/bootstrap.rs:71-92]
- `missing_file_returns_defaults` (function) component `missing_file_returns_defaults [function]` (`7e5d3f8f-869e-52d6-977c-9c62c6ea6fe7`) lines 101-105 [crates/gcore/src/bootstrap.rs:101-105]
  - Signature: `fn missing_file_returns_defaults() {`
  - Purpose: This test verifies that `read_daemon_endpoint_at()` returns `DaemonEndpoint::default()` when the specified YAML file does not exist. [crates/gcore/src/bootstrap.rs:101-105]
- `malformed_yaml_returns_defaults` (function) component `malformed_yaml_returns_defaults [function]` (`50591bb6-56a8-5837-8b35-8aed475ce17b`) lines 108-113 [crates/gcore/src/bootstrap.rs:108-113]
  - Signature: `fn malformed_yaml_returns_defaults() {`
  - Purpose: This test verifies that `read_daemon_endpoint_at` returns a default `DaemonEndpoint` instance when parsing a malformed YAML file. [crates/gcore/src/bootstrap.rs:108-113]
- `empty_file_returns_defaults` (function) component `empty_file_returns_defaults [function]` (`e574f5af-622e-5fbf-8252-3273785fbbd1`) lines 116-121 [crates/gcore/src/bootstrap.rs:116-121]
  - Signature: `fn empty_file_returns_defaults() {`
  - Purpose: This test verifies that reading an empty `bootstrap.yaml` file returns a default `DaemonEndpoint` instance. [crates/gcore/src/bootstrap.rs:116-121]
- `missing_fields_return_defaults` (function) component `missing_fields_return_defaults [function]` (`5cb5972d-23bd-58cc-a989-0fc613b02a08`) lines 124-129 [crates/gcore/src/bootstrap.rs:124-129]
  - Signature: `fn missing_fields_return_defaults() {`
  - Purpose: This test verifies that `read_daemon_endpoint_at()` returns a default `DaemonEndpoint` when parsing a YAML configuration file that lacks daemon endpoint fields. [crates/gcore/src/bootstrap.rs:124-129]
- `reads_custom_port` (function) component `reads_custom_port [function]` (`8502fb16-e425-59e3-b138-f6da1646a6d3`) lines 132-139 [crates/gcore/src/bootstrap.rs:132-139]
  - Signature: `fn reads_custom_port() {`
  - Purpose: This test verifies that `read_daemon_endpoint_at` correctly parses a custom daemon port from a YAML configuration file while defaulting to the standard bind host. [crates/gcore/src/bootstrap.rs:132-139]
- `reads_custom_host_and_port` (function) component `reads_custom_host_and_port [function]` (`7c18690f-12d1-553d-a1ee-2cda3f2b9b34`) lines 142-149 [crates/gcore/src/bootstrap.rs:142-149]
  - Signature: `fn reads_custom_host_and_port() {`
  - Purpose: Tests that `read_daemon_endpoint_at()` correctly parses a bootstrap.yaml file to extract custom daemon port (60887) and bind host (0.0.0.0) values into a daemon endpoint object. [crates/gcore/src/bootstrap.rs:142-149]
- `out_of_range_port_falls_back` (function) component `out_of_range_port_falls_back [function]` (`34693950-6f95-523f-8bbc-d7c3ec6a07d4`) lines 152-157 [crates/gcore/src/bootstrap.rs:152-157]
  - Signature: `fn out_of_range_port_falls_back() {`
  - Purpose: This test verifies that when a daemon configuration file specifies an out-of-range port (70000), `read_daemon_endpoint_at()` returns the `DEFAULT_DAEMON_PORT` as a fallback. [crates/gcore/src/bootstrap.rs:152-157]
- `bootstrap_path_respects_gobby_home` (function) component `bootstrap_path_respects_gobby_home [function]` (`442bb434-494b-5ca4-ba0c-a79b9442976d`) lines 160-178 [crates/gcore/src/bootstrap.rs:160-178]
  - Signature: `fn bootstrap_path_respects_gobby_home() {`
  - Purpose: This test function verifies that `bootstrap_path()` correctly resolves to `<GOBBY_HOME>/bootstrap.yaml` by temporarily setting GOBBY_HOME to a temporary directory and asserting the returned path matches the expected result. [crates/gcore/src/bootstrap.rs:160-178]

