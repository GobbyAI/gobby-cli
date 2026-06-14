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
  - 88-97
  - 165-168
  - 170-172
  - 174-247
  - 249-256
  - 258-275
  - 277-295
  - 297-329
  - 331-345
  - 354-356
  - 358-366
  - 368-375
  - 378-418
  - 421-431
  - 434-458
  - 461-480
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/daemon.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the daemon capability probing model for gwiki services: a set of capability enums, endpoint and degradation records, and a final report type that summarizes whether each daemon feature is available, required, and degraded. It ties those types together with static endpoint contracts, a transport abstraction, and probe helpers that inspect daemon endpoints, map HTTP or transport outcomes into `CapabilityAvailability` and `DaemonDegradation`, and assemble a `DaemonCapabilityReport`; the included test doubles and tests verify the fallback behavior for missing endpoints, method-not-allowed probes, transport failure, and probe panics.
[crates/gwiki/src/daemon.rs:11-18]
[crates/gwiki/src/daemon.rs:26-31]
[crates/gwiki/src/daemon.rs:34-40]
[crates/gwiki/src/daemon.rs:43-50]
[crates/gwiki/src/daemon.rs:53-62]

## API Symbols

- `DaemonCapability` (type) component `DaemonCapability [type]` (`2bb3f67a-d24d-59c9-9a10-941170305668`) lines 11-18 [crates/gwiki/src/daemon.rs:11-18]
  - Signature: `pub enum DaemonCapability {`
  - Purpose: Indexed type `DaemonCapability` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:11-18]
- `EndpointShape` (class) component `EndpointShape [class]` (`9b65b40e-e8b1-505a-8405-c7170602c48a`) lines 26-31 [crates/gwiki/src/daemon.rs:26-31]
  - Signature: `pub struct EndpointShape {`
  - Purpose: `EndpointShape` is a Rust struct that statically describes an API endpoint by storing its HTTP method, path, and the type/format descriptors for its request and response payloads. [crates/gwiki/src/daemon.rs:26-31]
- `CapabilityAvailability` (class) component `CapabilityAvailability [class]` (`470d0f23-45dc-5234-944f-10fc792cbd69`) lines 34-40 [crates/gwiki/src/daemon.rs:34-40]
  - Signature: `pub struct CapabilityAvailability {`
  - Purpose: `CapabilityAvailability` is a status record that pairs a `DaemonCapability` with its availability/requirement flags, the associated `EndpointShape`, and an optional `DaemonDegradation` describing any fallback or impairment state. [crates/gwiki/src/daemon.rs:34-40]
- `DaemonDegradation` (class) component `DaemonDegradation [class]` (`6467d103-434c-591e-bba3-8bb9c4298d9f`) lines 43-50 [crates/gwiki/src/daemon.rs:43-50]
  - Signature: `pub struct DaemonDegradation {`
  - Purpose: `DaemonDegradation` is a data structure that captures a specific daemon capability degradation, including the affected endpoint, the degradation reason, a human-readable message, a recommended fallback action, and an optional HTTP status code. [crates/gwiki/src/daemon.rs:43-50]
- `DaemonCapabilityReport` (class) component `DaemonCapabilityReport [class]` (`64bad598-c1cd-54ce-9e34-b7337a7b0682`) lines 53-62 [crates/gwiki/src/daemon.rs:53-62]
  - Signature: `pub struct DaemonCapabilityReport {`
  - Purpose: `DaemonCapabilityReport` is a daemon status struct that records the base URL plus per-feature availability for embeddings, synthesis, vision, transcription, agent dispatch, and session events, along with any active degradations. [crates/gwiki/src/daemon.rs:53-62]
- `EndpointContract` (class) component `EndpointContract [class]` (`f70c8e9b-22cd-58be-b88d-f11e3e694efe`) lines 65-74 [crates/gwiki/src/daemon.rs:65-74]
  - Signature: `struct EndpointContract {`
  - Purpose: `EndpointContract` is a static contract descriptor for a daemon capability endpoint, capturing whether it is required plus its canonical HTTP method, path, probe method, request and response shapes, and fallback implementation. [crates/gwiki/src/daemon.rs:65-74]
- `ProbeObservation` (type) component `ProbeObservation [type]` (`35495707-b8c1-5b3a-8189-a4ef95baa73e`) lines 77-80 [crates/gwiki/src/daemon.rs:77-80]
  - Signature: `enum ProbeObservation {`
  - Purpose: Indexed type `ProbeObservation` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:77-80]
- `DaemonProbeTransport` (type) component `DaemonProbeTransport [type]` (`d024b1e5-12f9-52b9-adb1-a9f058b11df7`) lines 82-84 [crates/gwiki/src/daemon.rs:82-84]
  - Signature: `trait DaemonProbeTransport: Sync {`
  - Purpose: Indexed type `DaemonProbeTransport` in `crates/gwiki/src/daemon.rs`. [crates/gwiki/src/daemon.rs:82-84]
- `UreqProbeTransport` (class) component `UreqProbeTransport [class]` (`f07d3927-7b91-54f9-a33f-094f55f7e502`) lines 86-86 [crates/gwiki/src/daemon.rs:86]
  - Signature: `struct UreqProbeTransport;`
  - Purpose: I’m checking the repository symbol usage so the summary reflects what `UreqProbeTransport` actually does, not just the empty declaration.`gcode` can’t reach the local Gobby database in this environment, so I’m falling back to direct source search to identify the transport’s role.I haven’t found the symbol in the repo itself, so I’m checking for nearby references to “probe transport” to avoid over-claiming its behavior.A zero-sized, fieldless Rust type representing a `ureq`-based probe transport. [crates/gwiki/src/daemon.rs:86]
- `UreqProbeTransport` (class) component `UreqProbeTransport [class]` (`c989c507-a1d4-556d-a0ac-c3e9de099090`) lines 88-97 [crates/gwiki/src/daemon.rs:88-97]
  - Signature: `impl DaemonProbeTransport for UreqProbeTransport {`
  - Purpose: `UreqProbeTransport` implements `DaemonProbeTransport` by sending a `ureq` request to `base_url + path` with `PROBE_TIMEOUT` and converting the result into `ProbeObservation::HttpStatus` for HTTP responses or `ProbeObservation::TransportError` for non-HTTP failures. [crates/gwiki/src/daemon.rs:88-97]
- `UreqProbeTransport.status` (method) component `UreqProbeTransport.status [method]` (`10e503f5-b349-54f6-a0aa-5fe4c4ec93df`) lines 89-96 [crates/gwiki/src/daemon.rs:89-96]
  - Signature: `fn status(&self, base_url: &str, method: &str, path: &str) -> ProbeObservation {`
  - Purpose: It trims any trailing slash from `base_url`, appends `path`, issues a `ureq` request with the given `method` and `PROBE_TIMEOUT`, and maps the result to `ProbeObservation::HttpStatus` for both successful and HTTP error responses or `ProbeObservation::TransportError` for other failures. [crates/gwiki/src/daemon.rs:89-96]
- `probe_daemon_capabilities` (function) component `probe_daemon_capabilities [function]` (`bf902180-b51c-53ec-b592-802369f34e3c`) lines 165-168 [crates/gwiki/src/daemon.rs:165-168]
  - Signature: `pub fn probe_daemon_capabilities() -> DaemonCapabilityReport {`
  - Purpose: Resolves the current daemon base URL via `gobby_core::daemon_url::daemon_url()` and returns the `DaemonCapabilityReport` produced by `probe_daemon_capabilities_at(&base_url)`. [crates/gwiki/src/daemon.rs:165-168]
- `probe_daemon_capabilities_at` (function) component `probe_daemon_capabilities_at [function]` (`be03c81f-30c9-51b0-850e-72690e62f09a`) lines 170-172 [crates/gwiki/src/daemon.rs:170-172]
  - Signature: `pub fn probe_daemon_capabilities_at(base_url: &str) -> DaemonCapabilityReport {`
  - Purpose: Probes the daemon’s capabilities at `base_url` by delegating to `probe_daemon_capabilities_with(base_url, &UreqProbeTransport)`. [crates/gwiki/src/daemon.rs:170-172]
- `probe_daemon_capabilities_with` (function) component `probe_daemon_capabilities_with [function]` (`98bc8483-3edc-5895-b718-d5335174c0c9`) lines 174-247 [crates/gwiki/src/daemon.rs:174-247]
  - Signature: `fn probe_daemon_capabilities_with(`
  - Purpose: It probes a daemon’s capability contracts via the supplied transport, short-circuiting to all-unavailable on an initial transport error and otherwise checking the remaining contracts in parallel before assembling a `DaemonCapabilityReport`. [crates/gwiki/src/daemon.rs:174-247]
- `probe_contract` (function) component `probe_contract [function]` (`3a7928ff-ba0d-5151-87c3-caac503be254`) lines 249-256 [crates/gwiki/src/daemon.rs:249-256]
  - Signature: `fn probe_contract(`
  - Purpose: `probe_contract` probes `base_url` using `transport.status` with the `EndpointContract`’s `probe_method` and `path`, then converts the resulting observation into a `CapabilityAvailability` via `availability_for_observation`. [crates/gwiki/src/daemon.rs:249-256]
- `availability_for_observation` (function) component `availability_for_observation [function]` (`6140e4ba-bee8-5e6b-b7ec-2bcf4f4e2f40`) lines 258-275 [crates/gwiki/src/daemon.rs:258-275]
  - Signature: `fn availability_for_observation(`
  - Purpose: It derives the `degradation` for a given `contract`/`observation` pair and returns a `CapabilityAvailability` record that mirrors the contract’s capability, required flag, and endpoint shape while setting `available` to `true` only when no degradation is present. [crates/gwiki/src/daemon.rs:258-275]
- `unreachable_availability` (function) component `unreachable_availability [function]` (`b51027ae-f421-5fae-b719-4db97a5e4b2b`) lines 277-295 [crates/gwiki/src/daemon.rs:277-295]
  - Signature: `fn unreachable_availability(contract: EndpointContract, message: &str) -> CapabilityAvailability {`
  - Purpose: Builds a `CapabilityAvailability` for an unreachable endpoint by preserving the contract’s capability, required flag, and endpoint shape, forcing `available` to `false`, and attaching a `DegradationReason::Unreachable` record with the message `daemon transport failed: {message}`. [crates/gwiki/src/daemon.rs:277-295]
- `degradation_for_observation` (function) component `degradation_for_observation [function]` (`a8051bde-03b1-5ce7-90db-d3973f88449b`) lines 297-329 [crates/gwiki/src/daemon.rs:297-329]
  - Signature: `fn degradation_for_observation(`
  - Purpose: Maps a `ProbeObservation` to an optional `DaemonDegradation`, returning `None` for successful 2xx responses and `OPTIONS`-probe 405s, and otherwise classifying the observation as unauthorized, missing endpoint, unexpected HTTP status, or transport unreachable with a corresponding degradation record. [crates/gwiki/src/daemon.rs:297-329]
- `degradation` (function) component `degradation [function]` (`ff8b043d-3a01-5a3c-a598-33f6a0fc999e`) lines 331-345 [crates/gwiki/src/daemon.rs:331-345]
  - Signature: `fn degradation(`
  - Purpose: Constructs and returns a `DaemonDegradation` by transferring `contract.capability`, `contract.path`, and `contract.fallback`, converting `message` into a `String`, and storing the provided `reason` and optional `http_status`. [crates/gwiki/src/daemon.rs:331-345]
- `FakeTransport` (class) component `FakeTransport [class]` (`ac37924e-036f-598f-b2bd-56260562f4de`) lines 354-356 [crates/gwiki/src/daemon.rs:354-356]
  - Signature: `struct FakeTransport {`
  - Purpose: `FakeTransport` is a lightweight in-memory transport stub that maps pairs of `&'static str` keys to `ProbeObservation` values via its `statuses` `HashMap`. [crates/gwiki/src/daemon.rs:354-356]
- `FakeTransport` (class) component `FakeTransport [class]` (`4e68274c-04ef-599e-939a-4774ffd87388`) lines 358-366 [crates/gwiki/src/daemon.rs:358-366]
  - Signature: `impl FakeTransport {`
  - Purpose: `FakeTransport` is a thin constructor wrapper that initializes its `statuses` field by collecting an iterator of `((&'static str, &'static str), ProbeObservation)` pairs into an internal map. [crates/gwiki/src/daemon.rs:358-366]
- `FakeTransport.new` (method) component `FakeTransport.new [method]` (`f7cf43e5-ce75-5a63-accc-0b0b1914d754`) lines 359-365 [crates/gwiki/src/daemon.rs:359-365]
  - Signature: `fn new(`
  - Purpose: Constructs `Self` by consuming an iterator of `((`static str, `static str), ProbeObservation)` pairs and collecting them into the `statuses` field. [crates/gwiki/src/daemon.rs:359-365]
- `FakeTransport` (class) component `FakeTransport [class]` (`f4d06eeb-fbb7-5ce5-a6e9-8c4ba095ebb3`) lines 368-375 [crates/gwiki/src/daemon.rs:368-375]
  - Signature: `impl DaemonProbeTransport for FakeTransport {`
  - Purpose: `FakeTransport` is a `DaemonProbeTransport` test double whose `status` method returns the cloned `ProbeObservation` registered for the `(method, path)` pair in `self.statuses`, or defaults to `ProbeObservation::HttpStatus(200)` when no entry exists. [crates/gwiki/src/daemon.rs:368-375]
- `FakeTransport.status` (method) component `FakeTransport.status [method]` (`c9181ad4-727f-5ba5-acb5-2dad36df5fcb`) lines 369-374 [crates/gwiki/src/daemon.rs:369-374]
  - Signature: `fn status(&self, _base_url: &str, method: &str, path: &str) -> ProbeObservation {`
  - Purpose: Returns the preconfigured `ProbeObservation` for the `(method, path)` pair from `self.statuses`, or `ProbeObservation::HttpStatus(200)` if no entry exists, ignoring `_base_url`. [crates/gwiki/src/daemon.rs:369-374]
- `missing_required_endpoint_degrades` (function) component `missing_required_endpoint_degrades [function]` (`18b6878e-2f0e-5ccd-9d67-30dda0748ea9`) lines 378-418 [crates/gwiki/src/daemon.rs:378-418]
  - Signature: `fn missing_required_endpoint_degrades() {`
  - Purpose: It verifies that when the daemon probe receives `404` for both `/api/llm/vision/status` and `/api/agents/spawn`, the `Vision` and `AgentDispatch` capabilities are marked unavailable with `DegradationReason::MissingEndpoint`, and the vision degradation record preserves the `404` status plus the raw-image fallback hint. [crates/gwiki/src/daemon.rs:378-418]
- `safe_write_probe_method_not_allowed_still_means_endpoint_exists` (function) component `safe_write_probe_method_not_allowed_still_means_endpoint_exists [function]` (`9ae46f72-ea94-5ccb-a31e-aa4846ea8d0d`) lines 421-431 [crates/gwiki/src/daemon.rs:421-431]
  - Signature: `fn safe_write_probe_method_not_allowed_still_means_endpoint_exists() {`
  - Purpose: This test verifies that an `OPTIONS` probe returning `405 Method Not Allowed` for `/api/memories/embeddings/reindex` is treated as proof the embeddings endpoint exists, so `report.embeddings.available` remains `true` and `report.embeddings.degradation` stays `None`. [crates/gwiki/src/daemon.rs:421-431]
- `first_transport_failure_degrades_all_capabilities_without_more_probes` (function) component `first_transport_failure_degrades_all_capabilities_without_more_probes [function]` (`a26680e1-d457-5002-b545-52d51cc518cc`) lines 434-458 [crates/gwiki/src/daemon.rs:434-458]
  - Signature: `fn first_transport_failure_degrades_all_capabilities_without_more_probes() {`
  - Purpose: Verifies that a single transport-level failure during daemon capability probing triggers exactly one probe call and marks all six capabilities as `Unreachable` with the transport error message propagated. [crates/gwiki/src/daemon.rs:434-458]
- `FailingTransport` (class) component `FailingTransport [class]` (`782c72d8-766e-579b-8ffc-cfeeada924cd`) lines 435-437 [crates/gwiki/src/daemon.rs:435-437]
  - Signature: `struct FailingTransport {`
  - Purpose: `FailingTransport` is a transport test double that records invocation count in an `AtomicUsize` via its `calls` field, likely to support failure-path verification. [crates/gwiki/src/daemon.rs:435-437]
- `FailingTransport` (class) component `FailingTransport [class]` (`aefeac50-d0f8-526c-9b97-32a846520758`) lines 439-444 [crates/gwiki/src/daemon.rs:439-444]
  - Signature: `impl DaemonProbeTransport for FailingTransport {`
  - Purpose: `FailingTransport` is a `DaemonProbeTransport` test double that atomically counts `status` invocations and deterministically returns `ProbeObservation::TransportError("connection refused")` for every probe. [crates/gwiki/src/daemon.rs:439-444]
- `FailingTransport.status` (method) component `FailingTransport.status [method]` (`59600276-ff4f-5a35-8e4b-800a130e01a8`) lines 440-443 [crates/gwiki/src/daemon.rs:440-443]
  - Signature: `fn status(&self, _base_url: &str, _method: &str, _path: &str) -> ProbeObservation {`
  - Purpose: Atomically increments the call counter and unconditionally returns `ProbeObservation::TransportError("connection refused")`, ignoring the `base_url`, `method`, and `path` inputs. [crates/gwiki/src/daemon.rs:440-443]
- `probe_thread_panic_degrades_that_capability` (function) component `probe_thread_panic_degrades_that_capability [function]` (`c3674c30-6fe5-5e76-a62e-5429d0806dbc`) lines 461-480 [crates/gwiki/src/daemon.rs:461-480]
  - Signature: `fn probe_thread_panic_degrades_that_capability() {`
  - Purpose: Verifies that a panic in the vision probe causes only the vision capability to be marked unavailable and degraded with `DegradationReason::Unreachable` and a panic-related message, while other capabilities like embeddings remain available. [crates/gwiki/src/daemon.rs:461-480]
- `PanickingTransport` (class) component `PanickingTransport [class]` (`356313f0-595a-530d-a7e9-85e08203f48b`) lines 462-462 [crates/gwiki/src/daemon.rs:462]
  - Signature: `struct PanickingTransport;`
  - Purpose: `PanickingTransport` is a zero-sized, unit-like transport struct with no fields or behavior defined in the provided source. [crates/gwiki/src/daemon.rs:462]
- `PanickingTransport` (class) component `PanickingTransport [class]` (`b5aff140-8f0a-5a0e-a23c-b45128c25030`) lines 464-471 [crates/gwiki/src/daemon.rs:464-471]
  - Signature: `impl DaemonProbeTransport for PanickingTransport {`
  - Purpose: `PanickingTransport` is a `DaemonProbeTransport` implementation that returns `ProbeObservation::HttpStatus(200)` for every probe path except `VISION.path`, where it intentionally panics with `vision probe panic`. [crates/gwiki/src/daemon.rs:464-471]
- `PanickingTransport.status` (method) component `PanickingTransport.status [method]` (`76940b1f-e0da-5a05-a9b7-8c5d3db14d66`) lines 465-470 [crates/gwiki/src/daemon.rs:465-470]
  - Signature: `fn status(&self, _base_url: &str, _method: &str, path: &str) -> ProbeObservation {`
  - Purpose: Returns `ProbeObservation::HttpStatus(200)` for all paths except `VISION.path`, where it deliberately panics with `"vision probe panic"`. [crates/gwiki/src/daemon.rs:465-470]

