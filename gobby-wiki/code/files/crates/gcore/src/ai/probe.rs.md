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

`crates/gcore/src/ai/probe.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CapabilityStatusRoute` | class | CapabilityStatusRoute is a public struct that encapsulates a static HTTP route definition with two fields: a method identifier and a path string. [crates/gcore/src/ai/probe.rs:20-23] |
| `CapabilityDegradationReason` | type | Indexed type `CapabilityDegradationReason` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:26-34] |
| `CapabilityDegradation` | class | CapabilityDegradation is a public struct that encodes metadata about an AI capability degradation event, comprising the affected capability type, degradation reason, descriptive message, and optional HTTP status code. [crates/gcore/src/ai/probe.rs:37-42] |
| `CapabilityAvailability` | class | 'CapabilityAvailability' is a struct that encodes the availability status of an 'AiCapability' alongside optional 'CapabilityStatusRoute' and 'CapabilityDegradation' metadata. [crates/gcore/src/ai/probe.rs:45-50] |
| `CapabilityProbeReport` | class | 'CapabilityProbeReport' is a Rust struct that encapsulates a base URL and a vector of 'CapabilityAvailability' items representing the results of probing capabilities at a given endpoint. [crates/gcore/src/ai/probe.rs:53-56] |
| `CapabilityProbeReport::availability` | method | Searches the capabilities collection for and returns an optional reference to the 'CapabilityAvailability' entry matching the specified 'AiCapability' parameter. [crates/gcore/src/ai/probe.rs:59-63] |
| `capability_status_route` | function | This function maps an 'AiCapability' enum variant to its corresponding REST API status endpoint path and returns a 'CapabilityStatusRoute' struct configured with the GET method. [crates/gcore/src/ai/probe.rs:66-78] |
| `probe_daemon_capability` | function | This function probes whether a specified AI capability is available on the daemon running at the default URL, returning a 'CapabilityAvailability' status. [crates/gcore/src/ai/probe.rs:80-82] |
| `probe_daemon_capability_at` | function | Probes the availability of a specified AI capability on a daemon at a given base URL using the default 'UreqProbeTransport' HTTP client, returning a 'CapabilityAvailability' result. [crates/gcore/src/ai/probe.rs:84-89] |
| `probe_daemon_capabilities` | function | This function probes the capabilities of the daemon at its default URL (obtained from 'daemon_url()') and returns a 'CapabilityProbeReport'. [crates/gcore/src/ai/probe.rs:91-93] |
| `probe_daemon_capabilities_at` | function | This function probes a daemon's capabilities at the specified base URL using the default 'UreqProbeTransport' implementation and returns a 'CapabilityProbeReport'. [crates/gcore/src/ai/probe.rs:95-97] |
| `probe_daemon_capabilities_with` | function | Probes all daemon capabilities at a specified base URL using the provided transport implementation and returns a CapabilityProbeReport aggregating the results. [crates/gcore/src/ai/probe.rs:99-110] |
| `probe_daemon_capability_with` | function | # Summary This function probes a daemon's capability status endpoint via the provided transport and returns a 'CapabilityAvailability' object indicating whether the specified AI capability is available, with detailed degradation reasons for failure modes including authorization errors, missing endpoints, and invalid response bodies. [crates/gcore/src/ai/probe.rs:112-176] |
| `status_body_advertises` | function | # Summary This function determines whether a daemon's status JSON body advertises support for a specified AI capability by parsing it and checking multiple capability-specific JSON paths for a true boolean value. [crates/gcore/src/ai/probe.rs:178-241] |
| `bool_at_path` | function | 'bool_at_path' navigates a 'Value' object along a specified path and returns an 'Option<bool>' containing the boolean value at that location, or falls back to the boolean value of an "available" field if the target value is not directly a boolean. [crates/gcore/src/ai/probe.rs:243-251] |
| `unavailable` | function | Returns a 'CapabilityAvailability' struct with 'available' set to 'false' and a populated 'CapabilityDegradation' containing the provided reason, message, and optional HTTP status code. [crates/gcore/src/ai/probe.rs:253-271] |
| `ProbeObservation` | type | Indexed type `ProbeObservation` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:274-277] |
| `DaemonProbeTransport` | type | Indexed type `DaemonProbeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:279-281] |
| `UreqProbeTransport` | class | UreqProbeTransport is an opaque struct that abstracts a transport mechanism for HTTP probing operations within the ureq library. [crates/gcore/src/ai/probe.rs:283] |
| `UreqProbeTransport::status` | method | Sends an HTTP request to a constructed URL (base_url + path) using the specified method with timeout, returning a ProbeObservation containing the HTTP status and response body, or a transport error if the request fails. [crates/gcore/src/ai/probe.rs:286-299] |
| `FakeTransport` | class | FakeTransport is a mock transport stub that stores pre-configured ProbeObservation responses indexed by pairs of static strings and uses interior mutability (RefCell) to track request invocations as string tuples. [crates/gcore/src/ai/probe.rs:497-500] |
| `FakeTransport::new` | method | Constructs an instance by collecting an iterator of static string pairs paired with ProbeObservations into a 'responses' field and initializing an empty RefCell-wrapped 'requests' vector for interior-mutable tracking. [crates/gcore/src/ai/probe.rs:503-510] |
| `FakeTransport::requests` | method | # Summary This method returns a cloned copy of the internal requests vector of string tuple pairs, accessed from a RefCell using interior mutability. [crates/gcore/src/ai/probe.rs:512-514] |
| `FakeTransport::status` | method | # Summary Records an HTTP request (method and path) to an internal buffer and returns a pre-cached 'ProbeObservation' response for that method-path combination, or a default HTTP 404 response if not found. [crates/gcore/src/ai/probe.rs:518-529] |

_Verified by 7 in-file unit tests._

