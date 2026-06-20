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

`crates/gwiki/src/daemon.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DaemonCapability` | type | Indexed type `DaemonCapability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:11-18] |
| `EndpointShape` | class | 'EndpointShape' is a static API endpoint descriptor that stores the HTTP method, path, request shape identifier, and response shape identifier as '&'static str' fields. [crates/gwiki/src/daemon.rs:26-31] |
| `CapabilityAvailability` | class | 'CapabilityAvailability' is a record that pairs a 'DaemonCapability' with its availability and required-status flags, the associated 'EndpointShape', and an optional 'DaemonDegradation' describing degraded behavior. [crates/gwiki/src/daemon.rs:34-40] |
| `DaemonDegradation` | class | 'DaemonDegradation' is a record describing a daemon capability’s degraded state, including the affected capability, endpoint, reason, human-readable message, fallback target, and an optional HTTP status code. [crates/gwiki/src/daemon.rs:43-50] |
| `DaemonCapabilityReport` | class | 'DaemonCapabilityReport' is a struct that aggregates a daemon’s base URL, per-capability availability statuses for embeddings, synthesis, vision, transcription, agent dispatch, and session events, plus a list of active degradation records. [crates/gwiki/src/daemon.rs:53-62] |
| `EndpointContract` | class | 'EndpointContract' is a struct that describes an HTTP endpoint binding by pairing a daemon capability with required/probe methods, path, request and response schema identifiers, a required flag, and a fallback endpoint string. [crates/gwiki/src/daemon.rs:65-74] |
| `ProbeObservation` | type | Indexed type `ProbeObservation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:77-80] |
| `DaemonProbeTransport` | type | Indexed type `DaemonProbeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:82-84] |
| `UreqProbeTransport` | class | An opaque zero-sized 'struct' named 'UreqProbeTransport' that acts as a marker/probe transport type. [crates/gwiki/src/daemon.rs:86] |
| `UreqProbeTransport::status` | method | Builds a request URL by concatenating 'base_url' without trailing slash and 'path', issues an HTTP request with 'ureq' using the given 'method' and 'PROBE_TIMEOUT', and returns 'ProbeObservation::HttpStatus' for both successful responses and HTTP status errors, or 'ProbeObservation::TransportError' with the error string for transport failures. [crates/gwiki/src/daemon.rs:89-96] |
| `probe_daemon_capabilities` | function | Resolves the daemon base URL via 'gobby_core::daemon_url::daemon_url()' and returns the capability report produced by 'probe_daemon_capabilities_at(&base_url)'. [crates/gwiki/src/daemon.rs:165-168] |
| `probe_daemon_capabilities_at` | function | Calls 'probe_daemon_capabilities_with' using the provided 'base_url' and the 'UreqProbeTransport' to return a 'DaemonCapabilityReport'. [crates/gwiki/src/daemon.rs:170-172] |
| `probe_daemon_capabilities_with` | function | Probes the daemon’s support for the EMBEDDINGS, SYNTHESIS, VISION, TRANSCRIPTION, AGENT_DISPATCH, and SESSION_EVENTS contracts via the provided transport, short-circuiting to “unreachable” results on an initial transport error, otherwise probing the remaining contracts concurrently and assembling a 'DaemonCapabilityReport' from the collected availability observations. [crates/gwiki/src/daemon.rs:174-247] |
| `probe_contract` | function | Invokes 'transport.status' against 'base_url' using the contract’s probe method and path, then maps the resulting observation to a 'CapabilityAvailability' via 'availability_for_observation'. [crates/gwiki/src/daemon.rs:249-256] |
| `availability_for_observation` | function | Constructs a 'CapabilityAvailability' record for a given 'EndpointContract' and 'ProbeObservation' by computing the observation-derived degradation, marking the capability available only when no degradation is present, and copying the contract’s capability, required flag, and endpoint shape fields into the result. [crates/gwiki/src/daemon.rs:258-275] |
| `unreachable_availability` | function | Constructs a 'CapabilityAvailability' marking the contract’s capability as unavailable, preserving its method/path/request/response shapes and required flag, and attaching an 'Unreachable' degradation with the message prefixed as 'daemon transport failed: ...'. [crates/gwiki/src/daemon.rs:277-295] |
| `degradation_for_observation` | function | Maps a 'ProbeObservation' into an optional 'DaemonDegradation', treating 2xx as healthy, suppressing '405' for 'OPTIONS' probes, and otherwise classifying '401/403' as unauthorized, '404' as missing endpoint, other HTTP statuses as unexpected status, and transport errors as unreachable. [crates/gwiki/src/daemon.rs:297-329] |
| `degradation` | function | Constructs and returns a 'DaemonDegradation' by copying 'capability', 'path', and 'fallback' from the given 'EndpointContract', converting 'message' into a 'String', and storing the provided 'reason' and optional 'http_status'. [crates/gwiki/src/daemon.rs:331-345] |
| `FakeTransport` | class | 'FakeTransport' is a struct that stores a 'HashMap<(&'static str, &'static str), ProbeObservation>' mapping string-pair keys to probe observations. [crates/gwiki/src/daemon.rs:354-356] |
| `FakeTransport::new` | method | Constructs a 'Self' by consuming an 'IntoIterator' of '((&'static str, &'static str), ProbeObservation)' pairs and collecting them into the 'statuses' field. [crates/gwiki/src/daemon.rs:359-365] |
| `FakeTransport::status` | method | Returns the configured 'ProbeObservation' for the exact '(method, path)' lookup in 'self.statuses', defaulting to 'ProbeObservation::HttpStatus(200)' when no entry exists. [crates/gwiki/src/daemon.rs:369-374] |
| `FailingTransport` | class | A transport stub that maintains an 'AtomicUsize' 'calls' counter to track invocation count. [crates/gwiki/src/daemon.rs:435-437] |
| `FailingTransport::status` | method | This method atomically increments 'self.calls' with sequential consistency and returns 'ProbeObservation::TransportError("connection refused")', ignoring all parameters. [crates/gwiki/src/daemon.rs:440-443] |
| `PanickingTransport` | class | 'PanickingTransport' is a zero-sized transport type placeholder. [crates/gwiki/src/daemon.rs:462] |

_1 more symbol(s) not shown — run `gcode outline crates/gwiki/src/daemon.rs` for the full list._

_Verified by 4 in-file unit tests._

