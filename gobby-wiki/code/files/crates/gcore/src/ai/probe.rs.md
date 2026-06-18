---
title: crates/gcore/src/ai/probe.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/probe.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/probe.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai/probe.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gcore/src/ai/probe.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CapabilityStatusRoute` | class | Indexed class `CapabilityStatusRoute` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:20-23] |
| `CapabilityDegradationReason` | type | Indexed type `CapabilityDegradationReason` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:26-34] |
| `CapabilityDegradation` | class | Indexed class `CapabilityDegradation` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:37-42] |
| `CapabilityAvailability` | class | Indexed class `CapabilityAvailability` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:45-50] |
| `CapabilityProbeReport` | class | Indexed class `CapabilityProbeReport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:53-56] |
| `CapabilityProbeReport::availability` | method | Indexed method `CapabilityProbeReport::availability` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:59-63] |
| `capability_status_route` | function | Indexed function `capability_status_route` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:66-78] |
| `probe_daemon_capability` | function | Indexed function `probe_daemon_capability` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:80-82] |
| `probe_daemon_capability_at` | function | Indexed function `probe_daemon_capability_at` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:84-89] |
| `probe_daemon_capabilities` | function | Indexed function `probe_daemon_capabilities` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:91-93] |
| `probe_daemon_capabilities_at` | function | Indexed function `probe_daemon_capabilities_at` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:95-97] |
| `probe_daemon_capabilities_with` | function | Indexed function `probe_daemon_capabilities_with` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:99-110] |
| `probe_daemon_capability_with` | function | Indexed function `probe_daemon_capability_with` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:112-176] |
| `status_body_advertises` | function | Indexed function `status_body_advertises` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:178-241] |
| `bool_at_path` | function | Indexed function `bool_at_path` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:243-251] |
| `unavailable` | function | Indexed function `unavailable` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:253-271] |
| `ProbeObservation` | type | Indexed type `ProbeObservation` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:274-277] |
| `DaemonProbeTransport` | type | Indexed type `DaemonProbeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:279-281] |
| `UreqProbeTransport` | class | Indexed class `UreqProbeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:283] |
| `UreqProbeTransport::status` | method | Indexed method `UreqProbeTransport::status` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:286-299] |
| `capability_status_routes` | function | Indexed function `capability_status_routes` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:309-361] |
| `embed_status_body_requires_advertised_capability` | function | Indexed function `embed_status_body_requires_advertised_capability` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:364-377] |
| `audio_status_body_accepts_generic_enabled_key` | function | Indexed function `audio_status_body_accepts_generic_enabled_key` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:380-389] |
| `attachments_not_vision_extraction` | function | Indexed function `attachments_not_vision_extraction` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:392-418] |
| `status_body_capability_truth` | function | Indexed function `status_body_capability_truth` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:421-444] |
| `status_body_accepts_capability_objects_with_available_field` | function | Indexed function `status_body_accepts_capability_objects_with_available_field` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:447-466] |
| `status_route_is_availability_truth` | function | Indexed function `status_route_is_availability_truth` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:469-495] |
| `FakeTransport` | class | Indexed class `FakeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:497-500] |
| `FakeTransport::new` | method | Indexed method `FakeTransport::new` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:503-510] |
| `FakeTransport::requests` | method | Indexed method `FakeTransport::requests` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:512-514] |
| `FakeTransport::status` | method | Indexed method `FakeTransport::status` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:518-529] |

