---
title: crates/gcore/src/bootstrap.rs
type: code_file
provenance:
- file: crates/gcore/src/bootstrap.rs
  ranges:
  - 33-36
  - 39-44
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/bootstrap.rs:33-36](crates/gcore/src/bootstrap.rs#L33-L36), [crates/gcore/src/bootstrap.rs:39-44](crates/gcore/src/bootstrap.rs#L39-L44), [crates/gcore/src/bootstrap.rs:52-54](crates/gcore/src/bootstrap.rs#L52-L54), [crates/gcore/src/bootstrap.rs:60-65](crates/gcore/src/bootstrap.rs#L60-L65), [crates/gcore/src/bootstrap.rs:71-92](crates/gcore/src/bootstrap.rs#L71-L92), [crates/gcore/src/bootstrap.rs:101-105](crates/gcore/src/bootstrap.rs#L101-L105), [crates/gcore/src/bootstrap.rs:108-113](crates/gcore/src/bootstrap.rs#L108-L113), [crates/gcore/src/bootstrap.rs:116-121](crates/gcore/src/bootstrap.rs#L116-L121), [crates/gcore/src/bootstrap.rs:124-129](crates/gcore/src/bootstrap.rs#L124-L129), [crates/gcore/src/bootstrap.rs:132-139](crates/gcore/src/bootstrap.rs#L132-L139), [crates/gcore/src/bootstrap.rs:142-149](crates/gcore/src/bootstrap.rs#L142-L149), [crates/gcore/src/bootstrap.rs:152-157](crates/gcore/src/bootstrap.rs#L152-L157), [crates/gcore/src/bootstrap.rs:160-178](crates/gcore/src/bootstrap.rs#L160-L178)

</details>

# crates/gcore/src/bootstrap.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Resolves the Gobby daemon bootstrap config from `bootstrap.yaml`, using `GOBBY_HOME` when available and otherwise `~/.gobby`, then reads the advertised host/port into a `DaemonEndpoint`. The module keeps startup resilient by falling back to loopback defaults whenever the file is missing, unreadable, malformed, empty, incomplete, or contains an invalid port, while leaving any listen-address normalization to callers that build the final dial URL.
[crates/gcore/src/bootstrap.rs:33-36]
[crates/gcore/src/bootstrap.rs:39-44]
[crates/gcore/src/bootstrap.rs:52-54]
[crates/gcore/src/bootstrap.rs:60-65]
[crates/gcore/src/bootstrap.rs:71-92]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DaemonEndpoint` | class | `pub struct DaemonEndpoint {` | `DaemonEndpoint [class]` | `c3b26eba-26b7-5f88-a97e-86c91fff7a89` | 33-36 [crates/gcore/src/bootstrap.rs:33-36] | Indexed class `DaemonEndpoint` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:33-36] |
| `DaemonEndpoint::default` | method | `fn default() -> Self {` | `DaemonEndpoint::default [method]` | `15e6892c-5428-56cb-9bde-eaba7533a6c2` | 39-44 [crates/gcore/src/bootstrap.rs:39-44] | Indexed method `DaemonEndpoint::default` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:39-44] |
| `bootstrap_path` | function | `pub fn bootstrap_path() -> Option<PathBuf> {` | `bootstrap_path [function]` | `4e951fc6-cdc9-5aa5-b9ca-92f54b8225ef` | 52-54 [crates/gcore/src/bootstrap.rs:52-54] | Indexed function `bootstrap_path` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:52-54] |
| `read_daemon_endpoint` | function | `pub fn read_daemon_endpoint() -> DaemonEndpoint {` | `read_daemon_endpoint [function]` | `22f97c9c-6948-52ff-8ffe-da158404bd06` | 60-65 [crates/gcore/src/bootstrap.rs:60-65] | Indexed function `read_daemon_endpoint` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:60-65] |
| `read_daemon_endpoint_at` | function | `pub fn read_daemon_endpoint_at(path: &Path) -> DaemonEndpoint {` | `read_daemon_endpoint_at [function]` | `de617fe1-f5a2-5a5a-8b87-ff13183efa7c` | 71-92 [crates/gcore/src/bootstrap.rs:71-92] | Indexed function `read_daemon_endpoint_at` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:71-92] |
| `missing_file_returns_defaults` | function | `fn missing_file_returns_defaults() {` | `missing_file_returns_defaults [function]` | `7e5d3f8f-869e-52d6-977c-9c62c6ea6fe7` | 101-105 [crates/gcore/src/bootstrap.rs:101-105] | Indexed function `missing_file_returns_defaults` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:101-105] |
| `malformed_yaml_returns_defaults` | function | `fn malformed_yaml_returns_defaults() {` | `malformed_yaml_returns_defaults [function]` | `50591bb6-56a8-5837-8b35-8aed475ce17b` | 108-113 [crates/gcore/src/bootstrap.rs:108-113] | Indexed function `malformed_yaml_returns_defaults` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:108-113] |
| `empty_file_returns_defaults` | function | `fn empty_file_returns_defaults() {` | `empty_file_returns_defaults [function]` | `e574f5af-622e-5fbf-8252-3273785fbbd1` | 116-121 [crates/gcore/src/bootstrap.rs:116-121] | Indexed function `empty_file_returns_defaults` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:116-121] |
| `missing_fields_return_defaults` | function | `fn missing_fields_return_defaults() {` | `missing_fields_return_defaults [function]` | `5cb5972d-23bd-58cc-a989-0fc613b02a08` | 124-129 [crates/gcore/src/bootstrap.rs:124-129] | Indexed function `missing_fields_return_defaults` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:124-129] |
| `reads_custom_port` | function | `fn reads_custom_port() {` | `reads_custom_port [function]` | `8502fb16-e425-59e3-b138-f6da1646a6d3` | 132-139 [crates/gcore/src/bootstrap.rs:132-139] | Indexed function `reads_custom_port` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:132-139] |
| `reads_custom_host_and_port` | function | `fn reads_custom_host_and_port() {` | `reads_custom_host_and_port [function]` | `7c18690f-12d1-553d-a1ee-2cda3f2b9b34` | 142-149 [crates/gcore/src/bootstrap.rs:142-149] | Indexed function `reads_custom_host_and_port` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:142-149] |
| `out_of_range_port_falls_back` | function | `fn out_of_range_port_falls_back() {` | `out_of_range_port_falls_back [function]` | `34693950-6f95-523f-8bbc-d7c3ec6a07d4` | 152-157 [crates/gcore/src/bootstrap.rs:152-157] | Indexed function `out_of_range_port_falls_back` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:152-157] |
| `bootstrap_path_respects_gobby_home` | function | `fn bootstrap_path_respects_gobby_home() {` | `bootstrap_path_respects_gobby_home [function]` | `442bb434-494b-5ca4-ba0c-a79b9442976d` | 160-178 [crates/gcore/src/bootstrap.rs:160-178] | Indexed function `bootstrap_path_respects_gobby_home` in `crates/gcore/src/bootstrap.rs`. [crates/gcore/src/bootstrap.rs:160-178] |
