---
title: crates/gwiki/src/daemon.rs
type: code_file
provenance:
- file: crates/gwiki/src/daemon.rs
  ranges:
  - 11-18
  - 22-27
  - 30-35
  - 38-44
  - 47-54
  - 57-66
  - 69-78
  - 81-84
  - 86-88
  - '90'
  - 92-101
  - 93-100
  - 169-172
  - 174-176
  - 178-251
  - 253-260
  - 262-279
  - 281-299
  - 301-333
  - 335-349
  - 358-360
  - 362-370
  - 363-369
  - 372-379
  - 373-378
  - 382-422
  - 425-435
  - 438-462
  - 439-441
  - 443-448
  - 444-447
  - 465-484
  - '466'
  - 468-475
  - 469-474
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/daemon.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/daemon.rs` exposes 35 indexed API symbols.
[crates/gwiki/src/daemon.rs:11-18]
[crates/gwiki/src/daemon.rs:22-27]
[crates/gwiki/src/daemon.rs:30-35]
[crates/gwiki/src/daemon.rs:38-44]
[crates/gwiki/src/daemon.rs:47-54]

## API Symbols

- `DaemonCapability` (type) component `DaemonCapability [type]` (`2bb3f67a-d24d-59c9-9a10-941170305668`) lines 11-18 [crates/gwiki/src/daemon.rs:11-18]
  - Signature: `pub enum DaemonCapability {`
  - Purpose: Indexed type `DaemonCapability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:11-18]
- `DegradationReason` (type) component `DegradationReason [type]` (`fc1a825f-0f6e-5992-b51a-e1fda8011496`) lines 22-27 [crates/gwiki/src/daemon.rs:22-27]
  - Signature: `pub enum DegradationReason {`
  - Purpose: Indexed type `DegradationReason` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:22-27]
- `EndpointShape` (class) component `EndpointShape [class]` (`4426175d-7e7d-5e9b-87c3-9853852d4584`) lines 30-35 [crates/gwiki/src/daemon.rs:30-35]
  - Signature: `pub struct EndpointShape {`
  - Purpose: EndpointShape is a static metadata descriptor for HTTP endpoints that holds the HTTP method, path, and request/response schema definitions as immutable string references. [crates/gwiki/src/daemon.rs:30-35]
- `CapabilityAvailability` (class) component `CapabilityAvailability [class]` (`9f603518-4730-59b3-b317-bbff58070c1a`) lines 38-44 [crates/gwiki/src/daemon.rs:38-44]
  - Signature: `pub struct CapabilityAvailability {`
  - Purpose: `CapabilityAvailability` is a struct that encapsulates the runtime availability state of a daemon capability, including its requirement level, endpoint configuration, and optional degradation information. [crates/gwiki/src/daemon.rs:38-44]
- `DaemonDegradation` (class) component `DaemonDegradation [class]` (`758ef269-dbbf-59cc-9b0c-cbd4ad9cae2e`) lines 47-54 [crates/gwiki/src/daemon.rs:47-54]
  - Signature: `pub struct DaemonDegradation {`
  - Purpose: `DaemonDegradation` is a struct that encapsulates metadata for a degraded daemon capability, including the affected capability type, its endpoint, degradation reason, descriptive message, fallback mechanism, and optional HTTP status code. [crates/gwiki/src/daemon.rs:47-54]
- `DaemonCapabilityReport` (class) component `DaemonCapabilityReport [class]` (`0e837597-92a0-54d9-91b7-5950286d56f8`) lines 57-66 [crates/gwiki/src/daemon.rs:57-66]
  - Signature: `pub struct DaemonCapabilityReport {`
  - Purpose: `DaemonCapabilityReport` is a struct that reports the availability status of multiple daemon capabilities (embeddings, synthesis, vision, transcription, agent dispatch, session events) along with the daemon's base URL and any associated performance degradations. [crates/gwiki/src/daemon.rs:57-66]
- `EndpointContract` (class) component `EndpointContract [class]` (`fe8bccb4-7888-56ae-a2fc-e4a3fbf9e6b7`) lines 69-78 [crates/gwiki/src/daemon.rs:69-78]
  - Signature: `struct EndpointContract {`
  - Purpose: `EndpointContract` is a static metadata struct that defines the complete contract for a daemon API endpoint, including its HTTP method, path, required capability, request/response schemas, probe method, and fallback behavior. [crates/gwiki/src/daemon.rs:69-78]
- `ProbeObservation` (type) component `ProbeObservation [type]` (`f97de98c-a427-5387-8eba-3af520614475`) lines 81-84 [crates/gwiki/src/daemon.rs:81-84]
  - Signature: `enum ProbeObservation {`
  - Purpose: Indexed type `ProbeObservation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:81-84]
- `DaemonProbeTransport` (type) component `DaemonProbeTransport [type]` (`cce2046c-1449-5956-87b8-a45813204532`) lines 86-88 [crates/gwiki/src/daemon.rs:86-88]
  - Signature: `trait DaemonProbeTransport: Sync {`
  - Purpose: Indexed type `DaemonProbeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:86-88]
- `UreqProbeTransport` (class) component `UreqProbeTransport [class]` (`d3b991bc-258e-57cd-82ae-681b69622ecc`) lines 90-90 [crates/gwiki/src/daemon.rs:90]
  - Signature: `struct UreqProbeTransport;`
  - Purpose: UreqProbeTransport is an opaque struct type that abstracts the underlying transport mechanism for HTTP probe operations in the Ureq library. [crates/gwiki/src/daemon.rs:90]
- `UreqProbeTransport` (class) component `UreqProbeTransport [class]` (`ad6b5250-b4be-5153-87c6-780f9bcf11c8`) lines 92-101 [crates/gwiki/src/daemon.rs:92-101]
  - Signature: `impl DaemonProbeTransport for UreqProbeTransport {`
  - Purpose: UreqProbeTransport implements DaemonProbeTransport to issue HTTP requests with timeout to daemon endpoints and return ProbeObservation objects containing HTTP status codes or transport errors. [crates/gwiki/src/daemon.rs:92-101]
- `UreqProbeTransport.status` (method) component `UreqProbeTransport.status [method]` (`0488eae4-e40f-5e2f-92f9-4a79c0fa6373`) lines 93-100 [crates/gwiki/src/daemon.rs:93-100]
  - Signature: `fn status(&self, base_url: &str, method: &str, path: &str) -> ProbeObservation {`
  - Purpose: Sends an HTTP request with the specified method to a URL constructed from a base URL and path, returning a `ProbeObservation` enum containing either the HTTP status code or transport error. [crates/gwiki/src/daemon.rs:93-100]
- `probe_daemon_capabilities` (function) component `probe_daemon_capabilities [function]` (`037c9445-6642-5bfb-85aa-5122b76c5dcb`) lines 169-172 [crates/gwiki/src/daemon.rs:169-172]
  - Signature: `pub fn probe_daemon_capabilities() -> DaemonCapabilityReport {`
  - Purpose: Probes the daemon at the default configured URL and returns a report of its capabilities. [crates/gwiki/src/daemon.rs:169-172]
- `probe_daemon_capabilities_at` (function) component `probe_daemon_capabilities_at [function]` (`534d09e6-9184-5ee7-8ad4-90bd898b1478`) lines 174-176 [crates/gwiki/src/daemon.rs:174-176]
  - Signature: `pub fn probe_daemon_capabilities_at(base_url: &str) -> DaemonCapabilityReport {`
  - Purpose: Probes daemon capabilities at a specified base URL using the UreqProbeTransport HTTP client and returns a DaemonCapabilityReport. [crates/gwiki/src/daemon.rs:174-176]
- `probe_daemon_capabilities_with` (function) component `probe_daemon_capabilities_with [function]` (`1f9f4744-67f3-5aa1-aa4f-d50d935a240b`) lines 178-251 [crates/gwiki/src/daemon.rs:178-251]
  - Signature: `fn probe_daemon_capabilities_with(`
  - Purpose: Probes a daemon's availability across six capability contracts (embeddings, synthesis, vision, transcription, agent dispatch, and session events) by executing a synchronous probe of the first contract followed by concurrent thread-spawned probes of the remaining five, aggregating results into a `DaemonCapabilityReport`. [crates/gwiki/src/daemon.rs:178-251]
- `probe_contract` (function) component `probe_contract [function]` (`6ca68d23-84c3-5893-b23d-726c75cfd1d2`) lines 253-260 [crates/gwiki/src/daemon.rs:253-260]
  - Signature: `fn probe_contract(`
  - Purpose: # probe_contract

Probes an endpoint specified in a contract via the provided transport and returns its capability availability based on the resulting observation. [crates/gwiki/src/daemon.rs:253-260]
- `availability_for_observation` (function) component `availability_for_observation [function]` (`a2061cc6-98ee-5025-b151-8a9b78a9346f`) lines 262-279 [crates/gwiki/src/daemon.rs:262-279]
  - Signature: `fn availability_for_observation(`
  - Purpose: Determines endpoint capability availability by evaluating probe observation-induced degradation against an endpoint contract and returns a CapabilityAvailability record with availability status, endpoint shape, and degradation details. [crates/gwiki/src/daemon.rs:262-279]
- `unreachable_availability` (function) component `unreachable_availability [function]` (`b4f6e34f-4e73-5dae-bdf8-140bda9d78f9`) lines 281-299 [crates/gwiki/src/daemon.rs:281-299]
  - Signature: `fn unreachable_availability(contract: EndpointContract, message: &str) -> CapabilityAvailability {`
  - Purpose: Constructs a `CapabilityAvailability` struct marking a capability as unavailable with `Unreachable` degradation status due to daemon transport failure. [crates/gwiki/src/daemon.rs:281-299]
- `degradation_for_observation` (function) component `degradation_for_observation [function]` (`44fd365c-06af-5678-97d6-5997c3fc0865`) lines 301-333 [crates/gwiki/src/daemon.rs:301-333]
  - Signature: `fn degradation_for_observation(`
  - Purpose: Maps HTTP probe observations to optional daemon degradation states, returning `None` for successful responses (2xx or 405 with OPTIONS) and `Some` with categorized failure reasons (Unauthorized, MissingEndpoint, UnexpectedStatus, or Unreachable) for error conditions. [crates/gwiki/src/daemon.rs:301-333]
- `degradation` (function) component `degradation [function]` (`ce0487e9-faf8-5874-8ac7-8deb817cffc8`) lines 335-349 [crates/gwiki/src/daemon.rs:335-349]
  - Signature: `fn degradation(`
  - Purpose: Constructs a `DaemonDegradation` struct by combining endpoint contract metadata with a degradation reason, message, and optional HTTP status code. [crates/gwiki/src/daemon.rs:335-349]
- `FakeTransport` (class) component `FakeTransport [class]` (`e96cdfcd-ae36-52e3-838b-c1bb2d9df3d1`) lines 358-360 [crates/gwiki/src/daemon.rs:358-360]
  - Signature: `struct FakeTransport {`
  - Purpose: `FakeTransport` is a struct that stores a `HashMap` mapping tuples of static string references to `ProbeObservation` instances. [crates/gwiki/src/daemon.rs:358-360]
- `FakeTransport` (class) component `FakeTransport [class]` (`6a5798ea-66f1-56a6-b5b9-175de9eaaaa4`) lines 362-370 [crates/gwiki/src/daemon.rs:362-370]
  - Signature: `impl FakeTransport {`
  - Purpose: FakeTransport::new constructs an instance by collecting an iterator of ((&'static str, &'static str), ProbeObservation) pairs into a statuses field. [crates/gwiki/src/daemon.rs:362-370]
- `FakeTransport.new` (method) component `FakeTransport.new [method]` (`972ff6c8-6ceb-53f6-9011-183d35e34c79`) lines 363-369 [crates/gwiki/src/daemon.rs:363-369]
  - Signature: `fn new(`
  - Purpose: Constructs a new instance by collecting an iterable of status pairs—each mapping a tuple of two static string references to a `ProbeObservation` value—into the `statuses` field. [crates/gwiki/src/daemon.rs:363-369]
- `FakeTransport` (class) component `FakeTransport [class]` (`230eb219-a3cf-5471-9a5f-d0aac85fb858`) lines 372-379 [crates/gwiki/src/daemon.rs:372-379]
  - Signature: `impl DaemonProbeTransport for FakeTransport {`
  - Purpose: `FakeTransport` implements `DaemonProbeTransport` to return mocked probe observations from a lookup table keyed by (method, path) tuples, defaulting to HTTP 200 status. [crates/gwiki/src/daemon.rs:372-379]
- `FakeTransport.status` (method) component `FakeTransport.status [method]` (`8af3ccca-45f8-5664-b6d7-1f682cb2b5fb`) lines 373-378 [crates/gwiki/src/daemon.rs:373-378]
  - Signature: `fn status(&self, _base_url: &str, method: &str, path: &str) -> ProbeObservation {`
  - Purpose: Retrieves a cached `ProbeObservation` for the given HTTP method and path from an internal map, defaulting to HTTP 200 OK status if no matching entry exists. [crates/gwiki/src/daemon.rs:373-378]
- `missing_required_endpoint_degrades` (function) component `missing_required_endpoint_degrades [function]` (`b30d0427-605e-5fcd-a87c-acacbe945594`) lines 382-422 [crates/gwiki/src/daemon.rs:382-422]
  - Signature: `fn missing_required_endpoint_degrades() {`
  - Purpose: Tests that missing required daemon capability endpoints (404 responses) are correctly reported as unavailable capabilities with `MissingEndpoint` degradation reasons. [crates/gwiki/src/daemon.rs:382-422]
- `safe_write_probe_method_not_allowed_still_means_endpoint_exists` (function) component `safe_write_probe_method_not_allowed_still_means_endpoint_exists [function]` (`8cd62133-ed27-5460-9386-2c3435fd0078`) lines 425-435 [crates/gwiki/src/daemon.rs:425-435]
  - Signature: `fn safe_write_probe_method_not_allowed_still_means_endpoint_exists() {`
  - Purpose: # Summary

Tests that HTTP 405 (Method Not Allowed) responses to endpoint probes correctly infer endpoint availability despite the probe method being disallowed. [crates/gwiki/src/daemon.rs:425-435]
- `first_transport_failure_degrades_all_capabilities_without_more_probes` (function) component `first_transport_failure_degrades_all_capabilities_without_more_probes [function]` (`10ebcb63-7683-56b6-bd40-eb1d3654d8f2`) lines 438-462 [crates/gwiki/src/daemon.rs:438-462]
  - Signature: `fn first_transport_failure_degrades_all_capabilities_without_more_probes() {`
  - Purpose: This test verifies that a single transport connection failure during daemon probing causes all six capabilities to be marked as degraded with an `Unreachable` reason containing the connection error message. [crates/gwiki/src/daemon.rs:438-462]
- `FailingTransport` (class) component `FailingTransport [class]` (`5e00fc84-6115-5ca3-a703-cd6f5d7dc27d`) lines 439-441 [crates/gwiki/src/daemon.rs:439-441]
  - Signature: `struct FailingTransport {`
  - Purpose: `FailingTransport` is a struct that wraps an `AtomicUsize` counter to track the number of transport invocations, typically for testing or failure scenario simulation. [crates/gwiki/src/daemon.rs:439-441]
- `FailingTransport` (class) component `FailingTransport [class]` (`18cfde77-168c-5816-b85e-0753e19d8b39`) lines 443-448 [crates/gwiki/src/daemon.rs:443-448]
  - Signature: `impl DaemonProbeTransport for FailingTransport {`
  - Purpose: `FailingTransport` is a mock implementation of `DaemonProbeTransport` that simulates a transport failure by always returning a `TransportError` with "connection refused" while atomically tracking invocation count. [crates/gwiki/src/daemon.rs:443-448]
- `FailingTransport.status` (method) component `FailingTransport.status [method]` (`8d00c8d7-faca-57d6-a486-55d645d416e2`) lines 444-447 [crates/gwiki/src/daemon.rs:444-447]
  - Signature: `fn status(&self, _base_url: &str, _method: &str, _path: &str) -> ProbeObservation {`
  - Purpose: Increments an atomic call counter with sequential consistency ordering and unconditionally returns a `ProbeObservation::TransportError` with a "connection refused" message, disregarding all input parameters. [crates/gwiki/src/daemon.rs:444-447]
- `probe_thread_panic_degrades_that_capability` (function) component `probe_thread_panic_degrades_that_capability [function]` (`6388ce29-786e-50ed-8cb4-85a7c2bcf1ee`) lines 465-484 [crates/gwiki/src/daemon.rs:465-484]
  - Signature: `fn probe_thread_panic_degrades_that_capability() {`
  - Purpose: This function tests that when a daemon capability probe panics (specifically for the vision capability), that capability is marked unavailable with an `Unreachable` degradation reason and a panic-related error message, while other capabilities remain available. [crates/gwiki/src/daemon.rs:465-484]
- `PanickingTransport` (class) component `PanickingTransport [class]` (`4fe07044-7edb-5165-a152-da00b36db200`) lines 466-466 [crates/gwiki/src/daemon.rs:466]
  - Signature: `struct PanickingTransport;`
  - Purpose: `PanickingTransport` is a zero-sized unit struct that implements a transport interface designed to panic upon invocation, typically used as a test fixture for error handling. [crates/gwiki/src/daemon.rs:466]
- `PanickingTransport` (class) component `PanickingTransport [class]` (`19069393-bc0b-5890-a32a-392321a4c538`) lines 468-475 [crates/gwiki/src/daemon.rs:468-475]
  - Signature: `impl DaemonProbeTransport for PanickingTransport {`
  - Purpose: `PanickingTransport` is a mock `DaemonProbeTransport` implementation that returns HTTP 200 status for all probe requests except the vision endpoint, which deliberately panics for testing error handling. [crates/gwiki/src/daemon.rs:468-475]
- `PanickingTransport.status` (method) component `PanickingTransport.status [method]` (`1538d8d0-2a92-53be-9da9-c7283b04ad44`) lines 469-474 [crates/gwiki/src/daemon.rs:469-474]
  - Signature: `fn status(&self, _base_url: &str, _method: &str, path: &str) -> ProbeObservation {`
  - Purpose: Returns an HTTP 200 status observation unless the path matches `VISION.path`, in which case it panics. [crates/gwiki/src/daemon.rs:469-474]

