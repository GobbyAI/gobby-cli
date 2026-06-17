---
title: crates/gwiki/src/daemon.rs
type: code_file
provenance:
- file: crates/gwiki/src/daemon.rs
  ranges:
  - 11-18
  - 26-31
  - 34-40
  - 43-50
  - 53-62
  - 65-74
  - 77-80
  - 82-84
  - '86'
  - 89-96
  - 165-168
  - 170-172
  - 174-247
  - 249-256
  - 258-275
  - 277-295
  - 297-329
  - 331-345
  - 354-356
  - 359-365
  - 369-374
  - 378-418
  - 421-431
  - 434-458
  - 461-480
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/daemon.rs:11-18](crates/gwiki/src/daemon.rs#L11-L18), [crates/gwiki/src/daemon.rs:26-31](crates/gwiki/src/daemon.rs#L26-L31), [crates/gwiki/src/daemon.rs:34-40](crates/gwiki/src/daemon.rs#L34-L40), [crates/gwiki/src/daemon.rs:43-50](crates/gwiki/src/daemon.rs#L43-L50), [crates/gwiki/src/daemon.rs:53-62](crates/gwiki/src/daemon.rs#L53-L62), [crates/gwiki/src/daemon.rs:65-74](crates/gwiki/src/daemon.rs#L65-L74), [crates/gwiki/src/daemon.rs:77-80](crates/gwiki/src/daemon.rs#L77-L80), [crates/gwiki/src/daemon.rs:82-84](crates/gwiki/src/daemon.rs#L82-L84), [crates/gwiki/src/daemon.rs:86](crates/gwiki/src/daemon.rs#L86), [crates/gwiki/src/daemon.rs:89-96](crates/gwiki/src/daemon.rs#L89-L96), [crates/gwiki/src/daemon.rs:165-168](crates/gwiki/src/daemon.rs#L165-L168), [crates/gwiki/src/daemon.rs:170-172](crates/gwiki/src/daemon.rs#L170-L172), [crates/gwiki/src/daemon.rs:174-247](crates/gwiki/src/daemon.rs#L174-L247), [crates/gwiki/src/daemon.rs:249-256](crates/gwiki/src/daemon.rs#L249-L256), [crates/gwiki/src/daemon.rs:258-275](crates/gwiki/src/daemon.rs#L258-L275), [crates/gwiki/src/daemon.rs:277-295](crates/gwiki/src/daemon.rs#L277-L295), [crates/gwiki/src/daemon.rs:297-329](crates/gwiki/src/daemon.rs#L297-L329), [crates/gwiki/src/daemon.rs:331-345](crates/gwiki/src/daemon.rs#L331-L345), [crates/gwiki/src/daemon.rs:354-356](crates/gwiki/src/daemon.rs#L354-L356), [crates/gwiki/src/daemon.rs:359-365](crates/gwiki/src/daemon.rs#L359-L365), [crates/gwiki/src/daemon.rs:369-374](crates/gwiki/src/daemon.rs#L369-L374), [crates/gwiki/src/daemon.rs:378-418](crates/gwiki/src/daemon.rs#L378-L418), [crates/gwiki/src/daemon.rs:421-431](crates/gwiki/src/daemon.rs#L421-L431), [crates/gwiki/src/daemon.rs:434-458](crates/gwiki/src/daemon.rs#L434-L458), [crates/gwiki/src/daemon.rs:461-480](crates/gwiki/src/daemon.rs#L461-L480)

</details>

# crates/gwiki/src/daemon.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the Gobby daemon capability probe for required gwiki service sources. It defines the capability and endpoint-reporting data model (`DaemonCapability`, `EndpointShape`, `CapabilityAvailability`, `DaemonDegradation`, `DaemonCapabilityReport`) plus an `EndpointContract` that describes how each capability should be checked. A transport abstraction (`DaemonProbeTransport`) and concrete transports (`UreqProbeTransport`, `FakeTransport`, plus failing/panicking test transports) are used by the probe functions to query endpoints with a timeout, turn HTTP or transport outcomes into availability/degradation records, and collect the per-capability results into a full daemon report.
[crates/gwiki/src/daemon.rs:11-18]
[crates/gwiki/src/daemon.rs:26-31]
[crates/gwiki/src/daemon.rs:34-40]
[crates/gwiki/src/daemon.rs:43-50]
[crates/gwiki/src/daemon.rs:53-62]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DaemonCapability` | type | `pub enum DaemonCapability {` | `DaemonCapability [type]` | `2bb3f67a-d24d-59c9-9a10-941170305668` | 11-18 [crates/gwiki/src/daemon.rs:11-18] | Indexed type `DaemonCapability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:11-18] |
| `EndpointShape` | class | `pub struct EndpointShape {` | `EndpointShape [class]` | `9b65b40e-e8b1-505a-8405-c7170602c48a` | 26-31 [crates/gwiki/src/daemon.rs:26-31] | Indexed class `EndpointShape` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:26-31] |
| `CapabilityAvailability` | class | `pub struct CapabilityAvailability {` | `CapabilityAvailability [class]` | `470d0f23-45dc-5234-944f-10fc792cbd69` | 34-40 [crates/gwiki/src/daemon.rs:34-40] | Indexed class `CapabilityAvailability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:34-40] |
| `DaemonDegradation` | class | `pub struct DaemonDegradation {` | `DaemonDegradation [class]` | `6467d103-434c-591e-bba3-8bb9c4298d9f` | 43-50 [crates/gwiki/src/daemon.rs:43-50] | Indexed class `DaemonDegradation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:43-50] |
| `DaemonCapabilityReport` | class | `pub struct DaemonCapabilityReport {` | `DaemonCapabilityReport [class]` | `64bad598-c1cd-54ce-9e34-b7337a7b0682` | 53-62 [crates/gwiki/src/daemon.rs:53-62] | Indexed class `DaemonCapabilityReport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:53-62] |
| `EndpointContract` | class | `struct EndpointContract {` | `EndpointContract [class]` | `f70c8e9b-22cd-58be-b88d-f11e3e694efe` | 65-74 [crates/gwiki/src/daemon.rs:65-74] | Indexed class `EndpointContract` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:65-74] |
| `ProbeObservation` | type | `enum ProbeObservation {` | `ProbeObservation [type]` | `35495707-b8c1-5b3a-8189-a4ef95baa73e` | 77-80 [crates/gwiki/src/daemon.rs:77-80] | Indexed type `ProbeObservation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:77-80] |
| `DaemonProbeTransport` | type | `trait DaemonProbeTransport: Sync {` | `DaemonProbeTransport [type]` | `d024b1e5-12f9-52b9-adb1-a9f058b11df7` | 82-84 [crates/gwiki/src/daemon.rs:82-84] | Indexed type `DaemonProbeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:82-84] |
| `UreqProbeTransport` | class | `struct UreqProbeTransport;` | `UreqProbeTransport [class]` | `f07d3927-7b91-54f9-a33f-094f55f7e502` | 86-86 [crates/gwiki/src/daemon.rs:86] | Indexed class `UreqProbeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:86] |
| `UreqProbeTransport::status` | method | `fn status(&self, base_url: &str, method: &str, path: &str) -> ProbeObservation {` | `UreqProbeTransport::status [method]` | `10e503f5-b349-54f6-a0aa-5fe4c4ec93df` | 89-96 [crates/gwiki/src/daemon.rs:89-96] | Indexed method `UreqProbeTransport::status` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:89-96] |
| `probe_daemon_capabilities` | function | `pub fn probe_daemon_capabilities() -> DaemonCapabilityReport {` | `probe_daemon_capabilities [function]` | `bf902180-b51c-53ec-b592-802369f34e3c` | 165-168 [crates/gwiki/src/daemon.rs:165-168] | Indexed function `probe_daemon_capabilities` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:165-168] |
| `probe_daemon_capabilities_at` | function | `pub fn probe_daemon_capabilities_at(base_url: &str) -> DaemonCapabilityReport {` | `probe_daemon_capabilities_at [function]` | `be03c81f-30c9-51b0-850e-72690e62f09a` | 170-172 [crates/gwiki/src/daemon.rs:170-172] | Indexed function `probe_daemon_capabilities_at` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:170-172] |
| `probe_daemon_capabilities_with` | function | `fn probe_daemon_capabilities_with(` | `probe_daemon_capabilities_with [function]` | `98bc8483-3edc-5895-b718-d5335174c0c9` | 174-247 [crates/gwiki/src/daemon.rs:174-247] | Indexed function `probe_daemon_capabilities_with` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:174-247] |
| `probe_contract` | function | `fn probe_contract(` | `probe_contract [function]` | `3a7928ff-ba0d-5151-87c3-caac503be254` | 249-256 [crates/gwiki/src/daemon.rs:249-256] | Indexed function `probe_contract` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:249-256] |
| `availability_for_observation` | function | `fn availability_for_observation(` | `availability_for_observation [function]` | `6140e4ba-bee8-5e6b-b7ec-2bcf4f4e2f40` | 258-275 [crates/gwiki/src/daemon.rs:258-275] | Indexed function `availability_for_observation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:258-275] |
| `unreachable_availability` | function | `fn unreachable_availability(contract: EndpointContract, message: &str) -> CapabilityAvailability {` | `unreachable_availability [function]` | `b51027ae-f421-5fae-b719-4db97a5e4b2b` | 277-295 [crates/gwiki/src/daemon.rs:277-295] | Indexed function `unreachable_availability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:277-295] |
| `degradation_for_observation` | function | `fn degradation_for_observation(` | `degradation_for_observation [function]` | `a8051bde-03b1-5ce7-90db-d3973f88449b` | 297-329 [crates/gwiki/src/daemon.rs:297-329] | Indexed function `degradation_for_observation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:297-329] |
| `degradation` | function | `fn degradation(` | `degradation [function]` | `ff8b043d-3a01-5a3c-a598-33f6a0fc999e` | 331-345 [crates/gwiki/src/daemon.rs:331-345] | Indexed function `degradation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:331-345] |
| `FakeTransport` | class | `struct FakeTransport {` | `FakeTransport [class]` | `ac37924e-036f-598f-b2bd-56260562f4de` | 354-356 [crates/gwiki/src/daemon.rs:354-356] | Indexed class `FakeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:354-356] |
| `FakeTransport::new` | method | `fn new(` | `FakeTransport::new [method]` | `f7cf43e5-ce75-5a63-accc-0b0b1914d754` | 359-365 [crates/gwiki/src/daemon.rs:359-365] | Indexed method `FakeTransport::new` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:359-365] |
| `FakeTransport::status` | method | `fn status(&self, _base_url: &str, method: &str, path: &str) -> ProbeObservation {` | `FakeTransport::status [method]` | `c9181ad4-727f-5ba5-acb5-2dad36df5fcb` | 369-374 [crates/gwiki/src/daemon.rs:369-374] | Indexed method `FakeTransport::status` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:369-374] |
| `missing_required_endpoint_degrades` | function | `fn missing_required_endpoint_degrades() {` | `missing_required_endpoint_degrades [function]` | `18b6878e-2f0e-5ccd-9d67-30dda0748ea9` | 378-418 [crates/gwiki/src/daemon.rs:378-418] | Indexed function `missing_required_endpoint_degrades` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:378-418] |
| `safe_write_probe_method_not_allowed_still_means_endpoint_exists` | function | `fn safe_write_probe_method_not_allowed_still_means_endpoint_exists() {` | `safe_write_probe_method_not_allowed_still_means_endpoint_exists [function]` | `9ae46f72-ea94-5ccb-a31e-aa4846ea8d0d` | 421-431 [crates/gwiki/src/daemon.rs:421-431] | Indexed function `safe_write_probe_method_not_allowed_still_means_endpoint_exists` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:421-431] |
| `first_transport_failure_degrades_all_capabilities_without_more_probes` | function | `fn first_transport_failure_degrades_all_capabilities_without_more_probes() {` | `first_transport_failure_degrades_all_capabilities_without_more_probes [function]` | `a26680e1-d457-5002-b545-52d51cc518cc` | 434-458 [crates/gwiki/src/daemon.rs:434-458] | Indexed function `first_transport_failure_degrades_all_capabilities_without_more_probes` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:434-458] |
| `FailingTransport` | class | `struct FailingTransport {` | `FailingTransport [class]` | `782c72d8-766e-579b-8ffc-cfeeada924cd` | 435-437 [crates/gwiki/src/daemon.rs:435-437] | Indexed class `FailingTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:435-437] |
| `FailingTransport::status` | method | `fn status(&self, _base_url: &str, _method: &str, _path: &str) -> ProbeObservation {` | `FailingTransport::status [method]` | `59600276-ff4f-5a35-8e4b-800a130e01a8` | 440-443 [crates/gwiki/src/daemon.rs:440-443] | Indexed method `FailingTransport::status` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:440-443] |
| `probe_thread_panic_degrades_that_capability` | function | `fn probe_thread_panic_degrades_that_capability() {` | `probe_thread_panic_degrades_that_capability [function]` | `c3674c30-6fe5-5e76-a62e-5429d0806dbc` | 461-480 [crates/gwiki/src/daemon.rs:461-480] | Indexed function `probe_thread_panic_degrades_that_capability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:461-480] |
| `PanickingTransport` | class | `struct PanickingTransport;` | `PanickingTransport [class]` | `356313f0-595a-530d-a7e9-85e08203f48b` | 462-462 [crates/gwiki/src/daemon.rs:462] | Indexed class `PanickingTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:462] |
| `PanickingTransport::status` | method | `fn status(&self, _base_url: &str, _method: &str, path: &str) -> ProbeObservation {` | `PanickingTransport::status [method]` | `76940b1f-e0da-5a05-a9b7-8c5d3db14d66` | 465-470 [crates/gwiki/src/daemon.rs:465-470] | Indexed method `PanickingTransport::status` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:465-470] |
