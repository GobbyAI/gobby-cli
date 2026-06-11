---
title: crates/gcore/src/ai/probe.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/probe.rs
  ranges:
  - 20-23
  - 26-34
  - 37-42
  - 45-50
  - 53-56
  - 58-64
  - 59-63
  - 66-78
  - 80-82
  - 84-89
  - 91-93
  - 95-97
  - 99-110
  - 112-176
  - 178-241
  - 243-251
  - 253-271
  - 274-277
  - 279-281
  - '283'
  - 285-300
  - 286-299
  - 309-361
  - 364-377
  - 380-389
  - 392-418
  - 421-444
  - 447-466
  - 469-495
  - 497-500
  - 502-515
  - 503-510
  - 512-514
  - 517-530
  - 518-529
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/probe.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

`crates/gcore/src/ai/probe.rs` exposes 35 indexed API symbols.
[crates/gcore/src/ai/probe.rs:20-23]
[crates/gcore/src/ai/probe.rs:26-34]
[crates/gcore/src/ai/probe.rs:37-42]
[crates/gcore/src/ai/probe.rs:45-50]
[crates/gcore/src/ai/probe.rs:53-56]

## API Symbols

- `CapabilityStatusRoute` (class) component `CapabilityStatusRoute [class]` (`a6fd6091-6989-5495-bbf4-ee3bbfb68060`) lines 20-23 [crates/gcore/src/ai/probe.rs:20-23]
  - Signature: `pub struct CapabilityStatusRoute {`
  - Purpose: CapabilityStatusRoute is a struct that stores static string references to an HTTP method and path for defining a capability status endpoint. [crates/gcore/src/ai/probe.rs:20-23]
- `CapabilityDegradationReason` (type) component `CapabilityDegradationReason [type]` (`26985c38-c0bb-55ac-9844-7f8dfa3af22b`) lines 26-34 [crates/gcore/src/ai/probe.rs:26-34]
  - Signature: `pub enum CapabilityDegradationReason {`
  - Purpose: Indexed type `CapabilityDegradationReason` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:26-34]
- `CapabilityDegradation` (class) component `CapabilityDegradation [class]` (`da7befb9-65bc-521f-af9a-28f36d32ff24`) lines 37-42 [crates/gcore/src/ai/probe.rs:37-42]
  - Signature: `pub struct CapabilityDegradation {`
  - Purpose: `CapabilityDegradation` is a struct that encapsulates metadata about a degraded AI capability, including the affected capability, its degradation reason, a descriptive message, and an optional HTTP status code. [crates/gcore/src/ai/probe.rs:37-42]
- `CapabilityAvailability` (class) component `CapabilityAvailability [class]` (`22a523c4-daff-5e38-92eb-055ecbbfbfd9`) lines 45-50 [crates/gcore/src/ai/probe.rs:45-50]
  - Signature: `pub struct CapabilityAvailability {`
  - Purpose: `CapabilityAvailability` is a struct that tracks the availability state of an `AiCapability`, optionally associating it with a status monitoring route and performance degradation information. [crates/gcore/src/ai/probe.rs:45-50]
- `CapabilityProbeReport` (class) component `CapabilityProbeReport [class]` (`61d12cc3-d985-5a84-aa90-3d38dc8b4ef6`) lines 53-56 [crates/gcore/src/ai/probe.rs:53-56]
  - Signature: `pub struct CapabilityProbeReport {`
  - Purpose: `CapabilityProbeReport` is a struct that aggregates the results of probing a base URL, containing the target URL and a vector of capability availability assessments for that endpoint. [crates/gcore/src/ai/probe.rs:53-56]
- `CapabilityProbeReport` (class) component `CapabilityProbeReport [class]` (`14ae42c2-3f1c-5a18-a330-a7e6af0ee76e`) lines 58-64 [crates/gcore/src/ai/probe.rs:58-64]
  - Signature: `impl CapabilityProbeReport {`
  - Purpose: `CapabilityProbeReport` implements a linear-search lookup method that retrieves an optional reference to a `CapabilityAvailability` by matching a given `AiCapability` against its internal capabilities collection. [crates/gcore/src/ai/probe.rs:58-64]
- `CapabilityProbeReport.availability` (method) component `CapabilityProbeReport.availability [method]` (`2519e391-063d-5f42-ba3e-64fcd9ac3574`) lines 59-63 [crates/gcore/src/ai/probe.rs:59-63]
  - Signature: `pub fn availability(&self, capability: AiCapability) -> Option<&CapabilityAvailability> {`
  - Purpose: Searches the capabilities collection and returns an optional reference to the first `CapabilityAvailability` entry matching the specified `AiCapability`. [crates/gcore/src/ai/probe.rs:59-63]
- `capability_status_route` (function) component `capability_status_route [function]` (`0fcc2a50-b69d-5539-a83c-b340710a09d2`) lines 66-78 [crates/gcore/src/ai/probe.rs:66-78]
  - Signature: `pub fn capability_status_route(capability: AiCapability) -> CapabilityStatusRoute {`
  - Purpose: Maps an `AiCapability` enum variant to its corresponding API status endpoint path and returns a GET request route as a `CapabilityStatusRoute` struct. [crates/gcore/src/ai/probe.rs:66-78]
- `probe_daemon_capability` (function) component `probe_daemon_capability [function]` (`2bc2f797-0568-50c2-98cc-d7612ccd729d`) lines 80-82 [crates/gcore/src/ai/probe.rs:80-82]
  - Signature: `pub fn probe_daemon_capability(capability: AiCapability) -> CapabilityAvailability {`
  - Purpose: This function probes the default daemon for the availability of a specified `AiCapability` and returns its corresponding `CapabilityAvailability` status. [crates/gcore/src/ai/probe.rs:80-82]
- `probe_daemon_capability_at` (function) component `probe_daemon_capability_at [function]` (`67450992-5bcf-5e64-bd07-1d21ee408767`) lines 84-89 [crates/gcore/src/ai/probe.rs:84-89]
  - Signature: `pub fn probe_daemon_capability_at(`
  - Purpose: Probes the availability of a specified AI capability at a daemon endpoint identified by the base URL using Ureq-based HTTP transport. [crates/gcore/src/ai/probe.rs:84-89]
- `probe_daemon_capabilities` (function) component `probe_daemon_capabilities [function]` (`be1b5939-6f20-500f-b1a7-355d28015624`) lines 91-93 [crates/gcore/src/ai/probe.rs:91-93]
  - Signature: `pub fn probe_daemon_capabilities() -> CapabilityProbeReport {`
  - Purpose: Probes the capabilities of the daemon at its default URL and returns a `CapabilityProbeReport`. [crates/gcore/src/ai/probe.rs:91-93]
- `probe_daemon_capabilities_at` (function) component `probe_daemon_capabilities_at [function]` (`5212eb3d-e62d-5c65-acde-2be543bfa4aa`) lines 95-97 [crates/gcore/src/ai/probe.rs:95-97]
  - Signature: `pub fn probe_daemon_capabilities_at(base_url: &str) -> CapabilityProbeReport {`
  - Purpose: Probes daemon capabilities at a specified base URL using the UreqProbeTransport HTTP transport. [crates/gcore/src/ai/probe.rs:95-97]
- `probe_daemon_capabilities_with` (function) component `probe_daemon_capabilities_with [function]` (`cc963b53-c2ac-5943-8e93-686cbc5e9e52`) lines 99-110 [crates/gcore/src/ai/probe.rs:99-110]
  - Signature: `fn probe_daemon_capabilities_with(`
  - Purpose: # Summary

Probes all predefined daemon capabilities at the specified base URL using the provided transport and returns an aggregated `CapabilityProbeReport`. [crates/gcore/src/ai/probe.rs:99-110]
- `probe_daemon_capability_with` (function) component `probe_daemon_capability_with [function]` (`03177fc3-a65a-553d-89df-cae5f70ccc6f`) lines 112-176 [crates/gcore/src/ai/probe.rs:112-176]
  - Signature: `fn probe_daemon_capability_with(`
  - Purpose: Probes a daemon's HTTP status endpoint to determine whether a specified AI capability is available, returning a structured `CapabilityAvailability` report that classifies the result with specific degradation reasons (e.g., unauthorized, missing endpoint, invalid response). [crates/gcore/src/ai/probe.rs:112-176]
- `status_body_advertises` (function) component `status_body_advertises [function]` (`f5b1ae31-d8ba-5980-98a9-a916753b17c8`) lines 178-241 [crates/gcore/src/ai/probe.rs:178-241]
  - Signature: `fn status_body_advertises(capability: AiCapability, body: Option<&str>) -> Result<bool, String> {`
  - Purpose: # Summary

This function parses a JSON daemon status body and checks whether a specified AI capability is advertised as enabled by searching for boolean flags at capability-specific JSON paths, returning `true` if enabled, `false` if disabled paths exist, or an error if no expected capability paths are found. [crates/gcore/src/ai/probe.rs:178-241]
- `bool_at_path` (function) component `bool_at_path [function]` (`e651da20-dce3-5f23-8047-6e4f41b1dd2b`) lines 243-251 [crates/gcore/src/ai/probe.rs:243-251]
  - Signature: `fn bool_at_path(value: &Value, path: &[&str]) -> Option<bool> {`
  - Purpose: Traverses a nested `Value` structure along the specified key path and returns the extracted boolean value, falling back to the 'available' field if the target value itself is not a boolean. [crates/gcore/src/ai/probe.rs:243-251]
- `unavailable` (function) component `unavailable [function]` (`4b57ee25-c217-531b-912e-8d2fec0a4168`) lines 253-271 [crates/gcore/src/ai/probe.rs:253-271]
  - Signature: `fn unavailable(`
  - Purpose: Constructs and returns a `CapabilityAvailability` struct marking the given AI capability as unavailable with specified degradation reason, message, and optional HTTP status code. [crates/gcore/src/ai/probe.rs:253-271]
- `ProbeObservation` (type) component `ProbeObservation [type]` (`58f0d3fc-0fc7-50cd-b064-27617a4f5433`) lines 274-277 [crates/gcore/src/ai/probe.rs:274-277]
  - Signature: `enum ProbeObservation {`
  - Purpose: Indexed type `ProbeObservation` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:274-277]
- `DaemonProbeTransport` (type) component `DaemonProbeTransport [type]` (`219ed1ce-997d-57ba-95e4-c6e4c95a2190`) lines 279-281 [crates/gcore/src/ai/probe.rs:279-281]
  - Signature: `trait DaemonProbeTransport {`
  - Purpose: Indexed type `DaemonProbeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:279-281]
- `UreqProbeTransport` (class) component `UreqProbeTransport [class]` (`59dbc989-926e-5cd4-847a-ecb79baf5046`) lines 283-283 [crates/gcore/src/ai/probe.rs:283]
  - Signature: `struct UreqProbeTransport;`
  - Purpose: `UreqProbeTransport` is an opaque struct (forward declaration) that likely represents a transport layer implementation for the ureq HTTP client library to handle probe or diagnostic requests.

*Note: Without the struct definition body, fields, or documentation, this summary is inferred from the name only.* [crates/gcore/src/ai/probe.rs:283]
- `UreqProbeTransport` (class) component `UreqProbeTransport [class]` (`2b1eb3a2-0cf5-5e23-ab32-f73ceb2693b4`) lines 285-300 [crates/gcore/src/ai/probe.rs:285-300]
  - Signature: `impl DaemonProbeTransport for UreqProbeTransport {`
  - Purpose: `UreqProbeTransport` implements `DaemonProbeTransport` to execute HTTP requests with a configurable timeout and return `ProbeObservation` results containing HTTP response status/body or transport errors. [crates/gcore/src/ai/probe.rs:285-300]
- `UreqProbeTransport.status` (method) component `UreqProbeTransport.status [method]` (`d0b58e63-6901-5d95-9134-2178335f8a3c`) lines 286-299 [crates/gcore/src/ai/probe.rs:286-299]
  - Signature: `fn status(&self, base_url: &str, method: &str, path: &str) -> ProbeObservation {`
  - Purpose: Performs an HTTP request to a constructed URL using the specified method and returns a `ProbeObservation` containing the response status and body, or a transport error if the request fails. [crates/gcore/src/ai/probe.rs:286-299]
- `capability_status_routes` (function) component `capability_status_routes [function]` (`c5eca7e7-9a74-504b-8447-f0c88b2290a4`) lines 309-361 [crates/gcore/src/ai/probe.rs:309-361]
  - Signature: `fn capability_status_routes() {`
  - Purpose: A unit test that verifies AI capability-to-status-endpoint route mappings and asserts that probing daemon capabilities with an empty HTTP transport yields unavailable status for all queried capabilities. [crates/gcore/src/ai/probe.rs:309-361]
- `embed_status_body_requires_advertised_capability` (function) component `embed_status_body_requires_advertised_capability [function]` (`3cb85e98-2b51-569e-a47d-a6a3871814f7`) lines 364-377 [crates/gcore/src/ai/probe.rs:364-377]
  - Signature: `fn embed_status_body_requires_advertised_capability() {`
  - Purpose: This unit test verifies that `status_body_advertises` correctly identifies the Embed capability in JSON status bodies through either the `embedding_enabled` or `capabilities.embed` fields, and returns an error when neither is present. [crates/gcore/src/ai/probe.rs:364-377]
- `audio_status_body_accepts_generic_enabled_key` (function) component `audio_status_body_accepts_generic_enabled_key [function]` (`42a1d57f-97eb-5e5b-b52e-da0a2c5d568a`) lines 380-389 [crates/gcore/src/ai/probe.rs:380-389]
  - Signature: `fn audio_status_body_accepts_generic_enabled_key() {`
  - Purpose: This test function verifies that `status_body_advertises` correctly interprets the generic `"enabled"` key from JSON status body responses for audio capabilities (AudioTranscribe and AudioTranslate). [crates/gcore/src/ai/probe.rs:380-389]
- `attachments_not_vision_extraction` (function) component `attachments_not_vision_extraction [function]` (`817339ec-ff78-5493-af0d-ceab2c6faea8`) lines 392-418 [crates/gcore/src/ai/probe.rs:392-418]
  - Signature: `fn attachments_not_vision_extraction() {`
  - Purpose: This test verifies that daemon capability probing correctly identifies the VisionExtract capability as unavailable by querying the `/api/llm/vision/status` endpoint, independent of attachment support status. [crates/gcore/src/ai/probe.rs:392-418]
- `status_body_capability_truth` (function) component `status_body_capability_truth [function]` (`7f899121-46ec-53c4-9e93-48e13f5464a5`) lines 421-444 [crates/gcore/src/ai/probe.rs:421-444]
  - Signature: `fn status_body_capability_truth() {`
  - Purpose: Tests that `probe_daemon_capabilities_with` correctly interprets a voice status endpoint response to determine AudioTranscribe capability as available and AudioTranslate as unavailable based on the JSON body flags. [crates/gcore/src/ai/probe.rs:421-444]
- `status_body_accepts_capability_objects_with_available_field` (function) component `status_body_accepts_capability_objects_with_available_field [function]` (`a82ce35f-4497-5861-b38e-82e45de66830`) lines 447-466 [crates/gcore/src/ai/probe.rs:447-466]
  - Signature: `fn status_body_accepts_capability_objects_with_available_field() {`
  - Purpose: This test verifies that the capability probing function correctly extracts and reports the `available` field from a capability object in the daemon's HTTP status response. [crates/gcore/src/ai/probe.rs:447-466]
- `status_route_is_availability_truth` (function) component `status_route_is_availability_truth [function]` (`13e8b8b5-4f2e-53a2-8766-fca00c5d8a3d`) lines 469-495 [crates/gcore/src/ai/probe.rs:469-495]
  - Signature: `fn status_route_is_availability_truth() {`
  - Purpose: This test verifies that daemon capability availability is determined by querying the `/api/llm/status` endpoint rather than `/api/providers/models`, establishing the status route as the authoritative source of truth. [crates/gcore/src/ai/probe.rs:469-495]
- `FakeTransport` (class) component `FakeTransport [class]` (`f56b5cb2-c56f-5de2-a35a-83eac89520ea`) lines 497-500 [crates/gcore/src/ai/probe.rs:497-500]
  - Signature: `struct FakeTransport {`
  - Purpose: `FakeTransport` is a test mock that stores pre-configured `ProbeObservation` responses indexed by static string key pairs and records all requests made to it via interior-mutable RefCell tracking. [crates/gcore/src/ai/probe.rs:497-500]
- `FakeTransport` (class) component `FakeTransport [class]` (`686ee12e-8441-55d0-96d8-74c4e0d6f57f`) lines 502-515 [crates/gcore/src/ai/probe.rs:502-515]
  - Signature: `impl FakeTransport {`
  - Purpose: FakeTransport is a test double that maps static string key pairs to ProbeObservation responses and tracks all requests made against it via a RefCell-guarded vector. [crates/gcore/src/ai/probe.rs:502-515]
- `FakeTransport.new` (method) component `FakeTransport.new [method]` (`4f66b2af-08b9-539e-9c65-0ed291a7e9ac`) lines 503-510 [crates/gcore/src/ai/probe.rs:503-510]
  - Signature: `fn new(`
  - Purpose: Constructs an instance by collecting probe observation response mappings from an iterator of (static string pair, ProbeObservation) tuples and initializing an empty requests vector wrapped in a RefCell for interior mutability. [crates/gcore/src/ai/probe.rs:503-510]
- `FakeTransport.requests` (method) component `FakeTransport.requests [method]` (`9354b95d-3554-5531-a95c-560505fe603d`) lines 512-514 [crates/gcore/src/ai/probe.rs:512-514]
  - Signature: `fn requests(&self) -> Vec<(String, String)> {`
  - Purpose: # Summary

This method borrows the RefCell-wrapped vector of string tuples and returns a cloned copy of it. [crates/gcore/src/ai/probe.rs:512-514]
- `FakeTransport` (class) component `FakeTransport [class]` (`9e6dc112-f5f8-5e7d-b310-e7497215dfc4`) lines 517-530 [crates/gcore/src/ai/probe.rs:517-530]
  - Signature: `impl DaemonProbeTransport for FakeTransport {`
  - Purpose: FakeTransport implements DaemonProbeTransport as a test mock that records HTTP requests and returns pre-configured responses keyed by method and path, defaulting to a 404 error for unmapped entries. [crates/gcore/src/ai/probe.rs:517-530]
- `FakeTransport.status` (method) component `FakeTransport.status [method]` (`8a9f4c08-2405-5339-bdb0-a96c7d0e2ec8`) lines 518-529 [crates/gcore/src/ai/probe.rs:518-529]
  - Signature: `fn status(&self, _base_url: &str, method: &str, path: &str) -> ProbeObservation {`
  - Purpose: Records the HTTP request (method, path) and returns a pre-configured mocked response from an internal map, defaulting to HTTP 404 if the key is not found. [crates/gcore/src/ai/probe.rs:518-529]

