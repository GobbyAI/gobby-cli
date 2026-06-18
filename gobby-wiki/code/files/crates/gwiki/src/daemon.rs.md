---
title: crates/gwiki/src/daemon.rs
type: code_file
provenance:
- file: crates/gwiki/src/daemon.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/daemon.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/daemon.rs` exposes 29 indexed API symbols.

## How it fits

`crates/gwiki/src/daemon.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DaemonCapability` | type | Indexed type `DaemonCapability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:11-18] |
| `EndpointShape` | class | Indexed class `EndpointShape` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:26-31] |
| `CapabilityAvailability` | class | Indexed class `CapabilityAvailability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:34-40] |
| `DaemonDegradation` | class | Indexed class `DaemonDegradation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:43-50] |
| `DaemonCapabilityReport` | class | Indexed class `DaemonCapabilityReport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:53-62] |
| `EndpointContract` | class | Indexed class `EndpointContract` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:65-74] |
| `ProbeObservation` | type | Indexed type `ProbeObservation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:77-80] |
| `DaemonProbeTransport` | type | Indexed type `DaemonProbeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:82-84] |
| `UreqProbeTransport` | class | Indexed class `UreqProbeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:86] |
| `UreqProbeTransport::status` | method | Indexed method `UreqProbeTransport::status` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:89-96] |
| `probe_daemon_capabilities` | function | Indexed function `probe_daemon_capabilities` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:165-168] |
| `probe_daemon_capabilities_at` | function | Indexed function `probe_daemon_capabilities_at` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:170-172] |
| `probe_daemon_capabilities_with` | function | Indexed function `probe_daemon_capabilities_with` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:174-247] |
| `probe_contract` | function | Indexed function `probe_contract` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:249-256] |
| `availability_for_observation` | function | Indexed function `availability_for_observation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:258-275] |
| `unreachable_availability` | function | Indexed function `unreachable_availability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:277-295] |
| `degradation_for_observation` | function | Indexed function `degradation_for_observation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:297-329] |
| `degradation` | function | Indexed function `degradation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:331-345] |
| `FakeTransport` | class | Indexed class `FakeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:354-356] |
| `FakeTransport::new` | method | Indexed method `FakeTransport::new` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:359-365] |
| `FakeTransport::status` | method | Indexed method `FakeTransport::status` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:369-374] |
| `missing_required_endpoint_degrades` | function | Indexed function `missing_required_endpoint_degrades` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:378-418] |
| `safe_write_probe_method_not_allowed_still_means_endpoint_exists` | function | Indexed function `safe_write_probe_method_not_allowed_still_means_endpoint_exists` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:421-431] |
| `first_transport_failure_degrades_all_capabilities_without_more_probes` | function | Indexed function `first_transport_failure_degrades_all_capabilities_without_more_probes` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:434-458] |
| `FailingTransport` | class | Indexed class `FailingTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:435-437] |
| `FailingTransport::status` | method | Indexed method `FailingTransport::status` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:440-443] |
| `probe_thread_panic_degrades_that_capability` | function | Indexed function `probe_thread_panic_degrades_that_capability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:461-480] |
| `PanickingTransport` | class | Indexed class `PanickingTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:462] |
| `PanickingTransport::status` | method | Indexed method `PanickingTransport::status` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:465-470] |

