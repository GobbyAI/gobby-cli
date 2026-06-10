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
  - 243-247
  - 249-267
  - 270-273
  - 275-277
  - '279'
  - 281-296
  - 282-295
  - 305-357
  - 360-373
  - 376-385
  - 388-414
  - 417-440
  - 443-469
  - 471-474
  - 476-489
  - 477-484
  - 486-488
  - 491-504
  - 492-503
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/probe.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

`crates/gcore/src/ai/probe.rs` exposes 34 indexed API symbols.
[crates/gcore/src/ai/probe.rs:20-23]
[crates/gcore/src/ai/probe.rs:26-34]
[crates/gcore/src/ai/probe.rs:37-42]
[crates/gcore/src/ai/probe.rs:45-50]
[crates/gcore/src/ai/probe.rs:53-56]
[crates/gcore/src/ai/probe.rs:58-64]
[crates/gcore/src/ai/probe.rs:59-63]
[crates/gcore/src/ai/probe.rs:66-78]
[crates/gcore/src/ai/probe.rs:80-82]
[crates/gcore/src/ai/probe.rs:84-89]
[crates/gcore/src/ai/probe.rs:91-93]
[crates/gcore/src/ai/probe.rs:95-97]
[crates/gcore/src/ai/probe.rs:99-110]
[crates/gcore/src/ai/probe.rs:112-176]
[crates/gcore/src/ai/probe.rs:178-241]
[crates/gcore/src/ai/probe.rs:243-247]
[crates/gcore/src/ai/probe.rs:249-267]
[crates/gcore/src/ai/probe.rs:270-273]
[crates/gcore/src/ai/probe.rs:275-277]
[crates/gcore/src/ai/probe.rs:279]
[crates/gcore/src/ai/probe.rs:281-296]
[crates/gcore/src/ai/probe.rs:282-295]
[crates/gcore/src/ai/probe.rs:305-357]
[crates/gcore/src/ai/probe.rs:360-373]
[crates/gcore/src/ai/probe.rs:376-385]
[crates/gcore/src/ai/probe.rs:388-414]
[crates/gcore/src/ai/probe.rs:417-440]
[crates/gcore/src/ai/probe.rs:443-469]
[crates/gcore/src/ai/probe.rs:471-474]
[crates/gcore/src/ai/probe.rs:476-489]
[crates/gcore/src/ai/probe.rs:477-484]
[crates/gcore/src/ai/probe.rs:486-488]
[crates/gcore/src/ai/probe.rs:491-504]
[crates/gcore/src/ai/probe.rs:492-503]

## API Symbols

- `CapabilityStatusRoute` (class) component `CapabilityStatusRoute [class]` (`a6fd6091-6989-5495-bbf4-ee3bbfb68060`) lines 20-23 [crates/gcore/src/ai/probe.rs:20-23]
  - Signature: `pub struct CapabilityStatusRoute {`
  - Purpose: `CapabilityStatusRoute` is a struct that holds static string references for an HTTP method and path to define a capability status endpoint. [crates/gcore/src/ai/probe.rs:20-23]
- `CapabilityDegradationReason` (type) component `CapabilityDegradationReason [type]` (`26985c38-c0bb-55ac-9844-7f8dfa3af22b`) lines 26-34 [crates/gcore/src/ai/probe.rs:26-34]
  - Signature: `pub enum CapabilityDegradationReason {`
  - Purpose: Indexed type `CapabilityDegradationReason` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:26-34]
- `CapabilityDegradation` (class) component `CapabilityDegradation [class]` (`da7befb9-65bc-521f-af9a-28f36d32ff24`) lines 37-42 [crates/gcore/src/ai/probe.rs:37-42]
  - Signature: `pub struct CapabilityDegradation {`
  - Purpose: `CapabilityDegradation` is a struct that encapsulates metadata for a degraded AI capability, including the affected capability identifier, a reason classification, a descriptive message, and an optional HTTP status code. [crates/gcore/src/ai/probe.rs:37-42]
- `CapabilityAvailability` (class) component `CapabilityAvailability [class]` (`22a523c4-daff-5e38-92eb-055ecbbfbfd9`) lines 45-50 [crates/gcore/src/ai/probe.rs:45-50]
  - Signature: `pub struct CapabilityAvailability {`
  - Purpose: `CapabilityAvailability` is a struct that encapsulates an AI capability's availability state along with its optional status routing and degradation information. [crates/gcore/src/ai/probe.rs:45-50]
- `CapabilityProbeReport` (class) component `CapabilityProbeReport [class]` (`61d12cc3-d985-5a84-aa90-3d38dc8b4ef6`) lines 53-56 [crates/gcore/src/ai/probe.rs:53-56]
  - Signature: `pub struct CapabilityProbeReport {`
  - Purpose: # Summary

`CapabilityProbeReport` is a struct that encapsulates the results of probing a given `base_url` for available capabilities, storing both the URL and a vector of `CapabilityAvailability` status indicators. [crates/gcore/src/ai/probe.rs:53-56]
- `CapabilityProbeReport` (class) component `CapabilityProbeReport [class]` (`14ae42c2-3f1c-5a18-a330-a7e6af0ee76e`) lines 58-64 [crates/gcore/src/ai/probe.rs:58-64]
  - Signature: `impl CapabilityProbeReport {`
  - Purpose: `CapabilityProbeReport` implements a method that performs a linear search through its capabilities collection and returns an optional reference to the `CapabilityAvailability` matching a given `AiCapability` type. [crates/gcore/src/ai/probe.rs:58-64]
- `CapabilityProbeReport.availability` (method) component `CapabilityProbeReport.availability [method]` (`2519e391-063d-5f42-ba3e-64fcd9ac3574`) lines 59-63 [crates/gcore/src/ai/probe.rs:59-63]
  - Signature: `pub fn availability(&self, capability: AiCapability) -> Option<&CapabilityAvailability> {`
  - Purpose: This method performs a linear search through the capabilities collection to locate and return a reference to the first `CapabilityAvailability` entry matching the provided `AiCapability`, or `None` if no match exists. [crates/gcore/src/ai/probe.rs:59-63]
- `capability_status_route` (function) component `capability_status_route [function]` (`0fcc2a50-b69d-5539-a83c-b340710a09d2`) lines 66-78 [crates/gcore/src/ai/probe.rs:66-78]
  - Signature: `pub fn capability_status_route(capability: AiCapability) -> CapabilityStatusRoute {`
  - Purpose: Maps an `AiCapability` enum variant to a `CapabilityStatusRoute` containing the corresponding GET status endpoint path. [crates/gcore/src/ai/probe.rs:66-78]
- `probe_daemon_capability` (function) component `probe_daemon_capability [function]` (`2bc2f797-0568-50c2-98cc-d7612ccd729d`) lines 80-82 [crates/gcore/src/ai/probe.rs:80-82]
  - Signature: `pub fn probe_daemon_capability(capability: AiCapability) -> CapabilityAvailability {`
  - Purpose: Probes the availability of a specified AI capability on the daemon using the default daemon URL. [crates/gcore/src/ai/probe.rs:80-82]
- `probe_daemon_capability_at` (function) component `probe_daemon_capability_at [function]` (`67450992-5bcf-5e64-bd07-1d21ee408767`) lines 84-89 [crates/gcore/src/ai/probe.rs:84-89]
  - Signature: `pub fn probe_daemon_capability_at(`
  - Purpose: Probes daemon capability availability at a specified base URL for a given AI capability using the default UreqProbeTransport. [crates/gcore/src/ai/probe.rs:84-89]
- `probe_daemon_capabilities` (function) component `probe_daemon_capabilities [function]` (`be1b5939-6f20-500f-b1a7-355d28015624`) lines 91-93 [crates/gcore/src/ai/probe.rs:91-93]
  - Signature: `pub fn probe_daemon_capabilities() -> CapabilityProbeReport {`
  - Purpose: Probes the daemon at its default URL and returns its capabilities as a `CapabilityProbeReport`. [crates/gcore/src/ai/probe.rs:91-93]
- `probe_daemon_capabilities_at` (function) component `probe_daemon_capabilities_at [function]` (`5212eb3d-e62d-5c65-acde-2be543bfa4aa`) lines 95-97 [crates/gcore/src/ai/probe.rs:95-97]
  - Signature: `pub fn probe_daemon_capabilities_at(base_url: &str) -> CapabilityProbeReport {`
  - Purpose: Probes a daemon's capabilities at a given base URL using the Ureq HTTP transport and returns a CapabilityProbeReport. [crates/gcore/src/ai/probe.rs:95-97]
- `probe_daemon_capabilities_with` (function) component `probe_daemon_capabilities_with [function]` (`cc963b53-c2ac-5943-8e93-686cbc5e9e52`) lines 99-110 [crates/gcore/src/ai/probe.rs:99-110]
  - Signature: `fn probe_daemon_capabilities_with(`
  - Purpose: Probes all predefined daemon capabilities at a specified base URL using the provided transport implementation and returns a CapabilityProbeReport aggregating the base URL with individual capability probe results. [crates/gcore/src/ai/probe.rs:99-110]
- `probe_daemon_capability_with` (function) component `probe_daemon_capability_with [function]` (`03177fc3-a65a-553d-89df-cae5f70ccc6f`) lines 112-176 [crates/gcore/src/ai/probe.rs:112-176]
  - Signature: `fn probe_daemon_capability_with(`
  - Purpose: Probes a daemon's HTTP status endpoint via a transport abstraction to determine whether a specified AI capability is available, returning a `CapabilityAvailability` struct that indicates availability and diagnostic degradation reasons. [crates/gcore/src/ai/probe.rs:112-176]
- `status_body_advertises` (function) component `status_body_advertises [function]` (`f5b1ae31-d8ba-5980-98a9-a916753b17c8`) lines 178-241 [crates/gcore/src/ai/probe.rs:178-241]
  - Signature: `fn status_body_advertises(capability: AiCapability, body: Option<&str>) -> Result<bool, String> {`
  - Purpose: # Summary

This function parses a JSON daemon status body and searches for capability-specific field paths to determine whether the given AI capability is advertised as enabled, returning an error if no relevant configuration paths exist. [crates/gcore/src/ai/probe.rs:178-241]
- `bool_at_path` (function) component `bool_at_path [function]` (`e651da20-dce3-5f23-8047-6e4f41b1dd2b`) lines 243-247 [crates/gcore/src/ai/probe.rs:243-247]
  - Signature: `fn bool_at_path(value: &Value, path: &[&str]) -> Option<bool> {`
  - Purpose: Retrieves a boolean value from a nested `Value` structure by traversing a sequence of string keys, returning `None` if any intermediate lookup fails or the terminal value is not a boolean. [crates/gcore/src/ai/probe.rs:243-247]
- `unavailable` (function) component `unavailable [function]` (`1773b764-40c3-5031-bc41-8eec30a55647`) lines 249-267 [crates/gcore/src/ai/probe.rs:249-267]
  - Signature: `fn unavailable(`
  - Purpose: Constructs a `CapabilityAvailability` struct marking a capability as unavailable and encapsulating the degradation reason, message, and optional HTTP status code. [crates/gcore/src/ai/probe.rs:249-267]
- `ProbeObservation` (type) component `ProbeObservation [type]` (`b8503ae3-4511-5e9f-92c5-c40e78936c18`) lines 270-273 [crates/gcore/src/ai/probe.rs:270-273]
  - Signature: `enum ProbeObservation {`
  - Purpose: Indexed type `ProbeObservation` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:270-273]
- `DaemonProbeTransport` (type) component `DaemonProbeTransport [type]` (`2e67506d-8aa0-5282-9a99-cafe0120aa32`) lines 275-277 [crates/gcore/src/ai/probe.rs:275-277]
  - Signature: `trait DaemonProbeTransport {`
  - Purpose: Indexed type `DaemonProbeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:275-277]
- `UreqProbeTransport` (class) component `UreqProbeTransport [class]` (`6e6e06ef-5d21-59b5-98bb-8bf0e7c72299`) lines 279-279 [crates/gcore/src/ai/probe.rs:279]
  - Signature: `struct UreqProbeTransport;`
  - Purpose: `UreqProbeTransport` is a struct that implements an HTTP transport layer for probe operations using the ureq HTTP client library. [crates/gcore/src/ai/probe.rs:279]
- `UreqProbeTransport` (class) component `UreqProbeTransport [class]` (`4b122fbf-e5e0-5079-81b7-5c0b6e0a716c`) lines 281-296 [crates/gcore/src/ai/probe.rs:281-296]
  - Signature: `impl DaemonProbeTransport for UreqProbeTransport {`
  - Purpose: `UreqProbeTransport` is a `DaemonProbeTransport` implementation that executes HTTP requests using the ureq library and returns `ProbeObservation` results containing response status/body or transport errors. [crates/gcore/src/ai/probe.rs:281-296]
- `UreqProbeTransport.status` (method) component `UreqProbeTransport.status [method]` (`34320345-b5bd-5cd4-9357-206596a243b5`) lines 282-295 [crates/gcore/src/ai/probe.rs:282-295]
  - Signature: `fn status(&self, base_url: &str, method: &str, path: &str) -> ProbeObservation {`
  - Purpose: This method performs an HTTP request with a specified method to a constructed URL (base_url + path) and returns a `ProbeObservation` containing either the HTTP status code with optional response body, or a transport error string. [crates/gcore/src/ai/probe.rs:282-295]
- `capability_status_routes` (function) component `capability_status_routes [function]` (`9094e2f0-81d5-59c4-bec5-b6de50710418`) lines 305-357 [crates/gcore/src/ai/probe.rs:305-357]
  - Signature: `fn capability_status_routes() {`
  - Purpose: Unit test that validates correct status endpoint route mappings for AI capabilities and verifies daemon capability availability reporting behavior through a mocked HTTP transport. [crates/gcore/src/ai/probe.rs:305-357]
- `embed_status_body_requires_advertised_capability` (function) component `embed_status_body_requires_advertised_capability [function]` (`17450391-4823-58da-b847-830179c792c7`) lines 360-373 [crates/gcore/src/ai/probe.rs:360-373]
  - Signature: `fn embed_status_body_requires_advertised_capability() {`
  - Purpose: Unit test verifying that `status_body_advertises` correctly identifies the Embed capability when declared via either the `embedding_enabled` or `capabilities.embed` field, and returns an error when the capability is not advertised. [crates/gcore/src/ai/probe.rs:360-373]
- `audio_status_body_accepts_generic_enabled_key` (function) component `audio_status_body_accepts_generic_enabled_key [function]` (`c60e79a2-ddbc-5e01-97fc-78af67af3ff4`) lines 376-385 [crates/gcore/src/ai/probe.rs:376-385]
  - Signature: `fn audio_status_body_accepts_generic_enabled_key() {`
  - Purpose: Verifies that `status_body_advertises` correctly parses and returns the boolean value of the `enabled` key from JSON status bodies for audio transcription and translation capabilities. [crates/gcore/src/ai/probe.rs:376-385]
- `attachments_not_vision_extraction` (function) component `attachments_not_vision_extraction [function]` (`2568d186-e75e-51e8-bb50-fec97cb2314e`) lines 388-414 [crates/gcore/src/ai/probe.rs:388-414]
  - Signature: `fn attachments_not_vision_extraction() {`
  - Purpose: This unit test verifies that daemon capability probing correctly identifies VisionExtract as unavailable by querying the `/api/llm/vision/status` endpoint, rather than relying on the `/api/chat/attachments` endpoint. [crates/gcore/src/ai/probe.rs:388-414]
- `status_body_capability_truth` (function) component `status_body_capability_truth [function]` (`d57bfaef-f55f-52b5-9130-581d6a79473e`) lines 417-440 [crates/gcore/src/ai/probe.rs:417-440]
  - Signature: `fn status_body_capability_truth() {`
  - Purpose: Unit test verifying that `probe_daemon_capabilities_with` accurately parses an HTTP daemon status response and correctly maps JSON fields to capability availability states for audio transcription and translation. [crates/gcore/src/ai/probe.rs:417-440]
- `status_route_is_availability_truth` (function) component `status_route_is_availability_truth [function]` (`19efb58c-dd7a-55cc-83c9-b1e0384c6368`) lines 443-469 [crates/gcore/src/ai/probe.rs:443-469]
  - Signature: `fn status_route_is_availability_truth() {`
  - Purpose: This test verifies that the `/api/llm/status` endpoint, not `/api/providers/models`, is the authoritative source for probing daemon capability availability. [crates/gcore/src/ai/probe.rs:443-469]
- `FakeTransport` (class) component `FakeTransport [class]` (`5aaa5543-44d1-553f-8e2f-0add59eb95b3`) lines 471-474 [crates/gcore/src/ai/probe.rs:471-474]
  - Signature: `struct FakeTransport {`
  - Purpose: FakeTransport is a mock transport that maps static request tuple patterns to pre-configured ProbeObservation responses while recording all requests made through it using interior mutability. [crates/gcore/src/ai/probe.rs:471-474]
- `FakeTransport` (class) component `FakeTransport [class]` (`043ed49a-9ad6-5f7e-a66a-775b6f76d306`) lines 476-489 [crates/gcore/src/ai/probe.rs:476-489]
  - Signature: `impl FakeTransport {`
  - Purpose: FakeTransport is a mock transport that maps static request key pairs to ProbeObservation responses and maintains a RefCell-wrapped vector of actual requests for test verification. [crates/gcore/src/ai/probe.rs:476-489]
- `FakeTransport.new` (method) component `FakeTransport.new [method]` (`6accea45-f966-539e-8359-ec68f0d1cf55`) lines 477-484 [crates/gcore/src/ai/probe.rs:477-484]
  - Signature: `fn new(`
  - Purpose: Constructs a new instance by consuming an `IntoIterator` of response tuples into a `responses` field while initializing `requests` as an empty `RefCell`-wrapped vector for interior mutability. [crates/gcore/src/ai/probe.rs:477-484]
- `FakeTransport.requests` (method) component `FakeTransport.requests [method]` (`ca1163f2-2a07-544b-a54e-82a12d0b3b7e`) lines 486-488 [crates/gcore/src/ai/probe.rs:486-488]
  - Signature: `fn requests(&self) -> Vec<(String, String)> {`
  - Purpose: Returns a cloned copy of the RefCell-wrapped vector of string tuples through runtime borrow checking. [crates/gcore/src/ai/probe.rs:486-488]
- `FakeTransport` (class) component `FakeTransport [class]` (`17bf429d-4020-5f53-b6a7-08543074c90c`) lines 491-504 [crates/gcore/src/ai/probe.rs:491-504]
  - Signature: `impl DaemonProbeTransport for FakeTransport {`
  - Purpose: FakeTransport implements DaemonProbeTransport as a test double that records HTTP requests and returns pre-configured mock responses from an internal map, defaulting to HTTP 404 for unmapped endpoints. [crates/gcore/src/ai/probe.rs:491-504]
- `FakeTransport.status` (method) component `FakeTransport.status [method]` (`cf0ef9f3-2bc8-5b8d-9507-f3c9a36a6e9e`) lines 492-503 [crates/gcore/src/ai/probe.rs:492-503]
  - Signature: `fn status(&self, _base_url: &str, method: &str, path: &str) -> ProbeObservation {`
  - Purpose: This method logs an HTTP request by appending its method and path to a request buffer, then returns a mocked ProbeObservation from an internal responses map, defaulting to HTTP 404 if the method-path combination is absent. [crates/gcore/src/ai/probe.rs:492-503]

