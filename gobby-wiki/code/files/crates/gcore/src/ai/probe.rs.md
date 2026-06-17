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
  - 286-299
  - 309-361
  - 364-377
  - 380-389
  - 392-418
  - 421-444
  - 447-466
  - 469-495
  - 497-500
  - 503-510
  - 512-514
  - 518-529
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai/probe.rs:20-23](crates/gcore/src/ai/probe.rs#L20-L23), [crates/gcore/src/ai/probe.rs:26-34](crates/gcore/src/ai/probe.rs#L26-L34), [crates/gcore/src/ai/probe.rs:37-42](crates/gcore/src/ai/probe.rs#L37-L42), [crates/gcore/src/ai/probe.rs:45-50](crates/gcore/src/ai/probe.rs#L45-L50), [crates/gcore/src/ai/probe.rs:53-56](crates/gcore/src/ai/probe.rs#L53-L56), [crates/gcore/src/ai/probe.rs:59-63](crates/gcore/src/ai/probe.rs#L59-L63), [crates/gcore/src/ai/probe.rs:66-78](crates/gcore/src/ai/probe.rs#L66-L78), [crates/gcore/src/ai/probe.rs:80-82](crates/gcore/src/ai/probe.rs#L80-L82), [crates/gcore/src/ai/probe.rs:84-89](crates/gcore/src/ai/probe.rs#L84-L89), [crates/gcore/src/ai/probe.rs:91-93](crates/gcore/src/ai/probe.rs#L91-L93), [crates/gcore/src/ai/probe.rs:95-97](crates/gcore/src/ai/probe.rs#L95-L97), [crates/gcore/src/ai/probe.rs:99-110](crates/gcore/src/ai/probe.rs#L99-L110), [crates/gcore/src/ai/probe.rs:112-176](crates/gcore/src/ai/probe.rs#L112-L176), [crates/gcore/src/ai/probe.rs:178-241](crates/gcore/src/ai/probe.rs#L178-L241), [crates/gcore/src/ai/probe.rs:243-251](crates/gcore/src/ai/probe.rs#L243-L251), [crates/gcore/src/ai/probe.rs:253-271](crates/gcore/src/ai/probe.rs#L253-L271), [crates/gcore/src/ai/probe.rs:274-277](crates/gcore/src/ai/probe.rs#L274-L277), [crates/gcore/src/ai/probe.rs:279-281](crates/gcore/src/ai/probe.rs#L279-L281), [crates/gcore/src/ai/probe.rs:283](crates/gcore/src/ai/probe.rs#L283), [crates/gcore/src/ai/probe.rs:286-299](crates/gcore/src/ai/probe.rs#L286-L299), [crates/gcore/src/ai/probe.rs:309-361](crates/gcore/src/ai/probe.rs#L309-L361), [crates/gcore/src/ai/probe.rs:364-377](crates/gcore/src/ai/probe.rs#L364-L377), [crates/gcore/src/ai/probe.rs:380-389](crates/gcore/src/ai/probe.rs#L380-L389), [crates/gcore/src/ai/probe.rs:392-418](crates/gcore/src/ai/probe.rs#L392-L418), [crates/gcore/src/ai/probe.rs:421-444](crates/gcore/src/ai/probe.rs#L421-L444), [crates/gcore/src/ai/probe.rs:447-466](crates/gcore/src/ai/probe.rs#L447-L466), [crates/gcore/src/ai/probe.rs:469-495](crates/gcore/src/ai/probe.rs#L469-L495), [crates/gcore/src/ai/probe.rs:497-500](crates/gcore/src/ai/probe.rs#L497-L500), [crates/gcore/src/ai/probe.rs:503-510](crates/gcore/src/ai/probe.rs#L503-L510), [crates/gcore/src/ai/probe.rs:512-514](crates/gcore/src/ai/probe.rs#L512-L514), [crates/gcore/src/ai/probe.rs:518-529](crates/gcore/src/ai/probe.rs#L518-L529)

</details>

# crates/gcore/src/ai/probe.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file probes the AI daemon’s capability endpoints and turns the results into a structured availability report. It defines the route and result types, maps each `AiCapability` to its status path, uses probe helpers and a transport abstraction to query the daemon, and records any degradation with a reason, message, and optional HTTP status; the lower section adds the status-body validation logic, plus a fake transport and tests/helpers for verifying route matching and body interpretation.
[crates/gcore/src/ai/probe.rs:20-23]
[crates/gcore/src/ai/probe.rs:26-34]
[crates/gcore/src/ai/probe.rs:37-42]
[crates/gcore/src/ai/probe.rs:45-50]
[crates/gcore/src/ai/probe.rs:53-56]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CapabilityStatusRoute` | class | `pub struct CapabilityStatusRoute {` | `CapabilityStatusRoute [class]` | `a6fd6091-6989-5495-bbf4-ee3bbfb68060` | 20-23 [crates/gcore/src/ai/probe.rs:20-23] | Indexed class `CapabilityStatusRoute` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:20-23] |
| `CapabilityDegradationReason` | type | `pub enum CapabilityDegradationReason {` | `CapabilityDegradationReason [type]` | `26985c38-c0bb-55ac-9844-7f8dfa3af22b` | 26-34 [crates/gcore/src/ai/probe.rs:26-34] | Indexed type `CapabilityDegradationReason` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:26-34] |
| `CapabilityDegradation` | class | `pub struct CapabilityDegradation {` | `CapabilityDegradation [class]` | `da7befb9-65bc-521f-af9a-28f36d32ff24` | 37-42 [crates/gcore/src/ai/probe.rs:37-42] | Indexed class `CapabilityDegradation` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:37-42] |
| `CapabilityAvailability` | class | `pub struct CapabilityAvailability {` | `CapabilityAvailability [class]` | `22a523c4-daff-5e38-92eb-055ecbbfbfd9` | 45-50 [crates/gcore/src/ai/probe.rs:45-50] | Indexed class `CapabilityAvailability` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:45-50] |
| `CapabilityProbeReport` | class | `pub struct CapabilityProbeReport {` | `CapabilityProbeReport [class]` | `61d12cc3-d985-5a84-aa90-3d38dc8b4ef6` | 53-56 [crates/gcore/src/ai/probe.rs:53-56] | Indexed class `CapabilityProbeReport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:53-56] |
| `CapabilityProbeReport::availability` | method | `pub fn availability(&self, capability: AiCapability) -> Option<&CapabilityAvailability> {` | `CapabilityProbeReport::availability [method]` | `2519e391-063d-5f42-ba3e-64fcd9ac3574` | 59-63 [crates/gcore/src/ai/probe.rs:59-63] | Indexed method `CapabilityProbeReport::availability` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:59-63] |
| `capability_status_route` | function | `pub fn capability_status_route(capability: AiCapability) -> CapabilityStatusRoute {` | `capability_status_route [function]` | `0fcc2a50-b69d-5539-a83c-b340710a09d2` | 66-78 [crates/gcore/src/ai/probe.rs:66-78] | Indexed function `capability_status_route` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:66-78] |
| `probe_daemon_capability` | function | `pub fn probe_daemon_capability(capability: AiCapability) -> CapabilityAvailability {` | `probe_daemon_capability [function]` | `2bc2f797-0568-50c2-98cc-d7612ccd729d` | 80-82 [crates/gcore/src/ai/probe.rs:80-82] | Indexed function `probe_daemon_capability` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:80-82] |
| `probe_daemon_capability_at` | function | `pub fn probe_daemon_capability_at(` | `probe_daemon_capability_at [function]` | `67450992-5bcf-5e64-bd07-1d21ee408767` | 84-89 [crates/gcore/src/ai/probe.rs:84-89] | Indexed function `probe_daemon_capability_at` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:84-89] |
| `probe_daemon_capabilities` | function | `pub fn probe_daemon_capabilities() -> CapabilityProbeReport {` | `probe_daemon_capabilities [function]` | `be1b5939-6f20-500f-b1a7-355d28015624` | 91-93 [crates/gcore/src/ai/probe.rs:91-93] | Indexed function `probe_daemon_capabilities` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:91-93] |
| `probe_daemon_capabilities_at` | function | `pub fn probe_daemon_capabilities_at(base_url: &str) -> CapabilityProbeReport {` | `probe_daemon_capabilities_at [function]` | `5212eb3d-e62d-5c65-acde-2be543bfa4aa` | 95-97 [crates/gcore/src/ai/probe.rs:95-97] | Indexed function `probe_daemon_capabilities_at` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:95-97] |
| `probe_daemon_capabilities_with` | function | `fn probe_daemon_capabilities_with(` | `probe_daemon_capabilities_with [function]` | `cc963b53-c2ac-5943-8e93-686cbc5e9e52` | 99-110 [crates/gcore/src/ai/probe.rs:99-110] | Indexed function `probe_daemon_capabilities_with` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:99-110] |
| `probe_daemon_capability_with` | function | `fn probe_daemon_capability_with(` | `probe_daemon_capability_with [function]` | `03177fc3-a65a-553d-89df-cae5f70ccc6f` | 112-176 [crates/gcore/src/ai/probe.rs:112-176] | Indexed function `probe_daemon_capability_with` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:112-176] |
| `status_body_advertises` | function | `fn status_body_advertises(capability: AiCapability, body: Option<&str>) -> Result<bool, String> {` | `status_body_advertises [function]` | `f5b1ae31-d8ba-5980-98a9-a916753b17c8` | 178-241 [crates/gcore/src/ai/probe.rs:178-241] | Indexed function `status_body_advertises` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:178-241] |
| `bool_at_path` | function | `fn bool_at_path(value: &Value, path: &[&str]) -> Option<bool> {` | `bool_at_path [function]` | `e651da20-dce3-5f23-8047-6e4f41b1dd2b` | 243-251 [crates/gcore/src/ai/probe.rs:243-251] | Indexed function `bool_at_path` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:243-251] |
| `unavailable` | function | `fn unavailable(` | `unavailable [function]` | `4b57ee25-c217-531b-912e-8d2fec0a4168` | 253-271 [crates/gcore/src/ai/probe.rs:253-271] | Indexed function `unavailable` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:253-271] |
| `ProbeObservation` | type | `enum ProbeObservation {` | `ProbeObservation [type]` | `58f0d3fc-0fc7-50cd-b064-27617a4f5433` | 274-277 [crates/gcore/src/ai/probe.rs:274-277] | Indexed type `ProbeObservation` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:274-277] |
| `DaemonProbeTransport` | type | `trait DaemonProbeTransport {` | `DaemonProbeTransport [type]` | `219ed1ce-997d-57ba-95e4-c6e4c95a2190` | 279-281 [crates/gcore/src/ai/probe.rs:279-281] | Indexed type `DaemonProbeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:279-281] |
| `UreqProbeTransport` | class | `struct UreqProbeTransport;` | `UreqProbeTransport [class]` | `59dbc989-926e-5cd4-847a-ecb79baf5046` | 283-283 [crates/gcore/src/ai/probe.rs:283] | Indexed class `UreqProbeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:283] |
| `UreqProbeTransport::status` | method | `fn status(&self, base_url: &str, method: &str, path: &str) -> ProbeObservation {` | `UreqProbeTransport::status [method]` | `d0b58e63-6901-5d95-9134-2178335f8a3c` | 286-299 [crates/gcore/src/ai/probe.rs:286-299] | Indexed method `UreqProbeTransport::status` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:286-299] |
| `capability_status_routes` | function | `fn capability_status_routes() {` | `capability_status_routes [function]` | `c5eca7e7-9a74-504b-8447-f0c88b2290a4` | 309-361 [crates/gcore/src/ai/probe.rs:309-361] | Indexed function `capability_status_routes` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:309-361] |
| `embed_status_body_requires_advertised_capability` | function | `fn embed_status_body_requires_advertised_capability() {` | `embed_status_body_requires_advertised_capability [function]` | `3cb85e98-2b51-569e-a47d-a6a3871814f7` | 364-377 [crates/gcore/src/ai/probe.rs:364-377] | Indexed function `embed_status_body_requires_advertised_capability` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:364-377] |
| `audio_status_body_accepts_generic_enabled_key` | function | `fn audio_status_body_accepts_generic_enabled_key() {` | `audio_status_body_accepts_generic_enabled_key [function]` | `42a1d57f-97eb-5e5b-b52e-da0a2c5d568a` | 380-389 [crates/gcore/src/ai/probe.rs:380-389] | Indexed function `audio_status_body_accepts_generic_enabled_key` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:380-389] |
| `attachments_not_vision_extraction` | function | `fn attachments_not_vision_extraction() {` | `attachments_not_vision_extraction [function]` | `817339ec-ff78-5493-af0d-ceab2c6faea8` | 392-418 [crates/gcore/src/ai/probe.rs:392-418] | Indexed function `attachments_not_vision_extraction` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:392-418] |
| `status_body_capability_truth` | function | `fn status_body_capability_truth() {` | `status_body_capability_truth [function]` | `7f899121-46ec-53c4-9e93-48e13f5464a5` | 421-444 [crates/gcore/src/ai/probe.rs:421-444] | Indexed function `status_body_capability_truth` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:421-444] |
| `status_body_accepts_capability_objects_with_available_field` | function | `fn status_body_accepts_capability_objects_with_available_field() {` | `status_body_accepts_capability_objects_with_available_field [function]` | `a82ce35f-4497-5861-b38e-82e45de66830` | 447-466 [crates/gcore/src/ai/probe.rs:447-466] | Indexed function `status_body_accepts_capability_objects_with_available_field` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:447-466] |
| `status_route_is_availability_truth` | function | `fn status_route_is_availability_truth() {` | `status_route_is_availability_truth [function]` | `13e8b8b5-4f2e-53a2-8766-fca00c5d8a3d` | 469-495 [crates/gcore/src/ai/probe.rs:469-495] | Indexed function `status_route_is_availability_truth` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:469-495] |
| `FakeTransport` | class | `struct FakeTransport {` | `FakeTransport [class]` | `f56b5cb2-c56f-5de2-a35a-83eac89520ea` | 497-500 [crates/gcore/src/ai/probe.rs:497-500] | Indexed class `FakeTransport` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:497-500] |
| `FakeTransport::new` | method | `fn new(` | `FakeTransport::new [method]` | `4f66b2af-08b9-539e-9c65-0ed291a7e9ac` | 503-510 [crates/gcore/src/ai/probe.rs:503-510] | Indexed method `FakeTransport::new` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:503-510] |
| `FakeTransport::requests` | method | `fn requests(&self) -> Vec<(String, String)> {` | `FakeTransport::requests [method]` | `9354b95d-3554-5531-a95c-560505fe603d` | 512-514 [crates/gcore/src/ai/probe.rs:512-514] | Indexed method `FakeTransport::requests` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:512-514] |
| `FakeTransport::status` | method | `fn status(&self, _base_url: &str, method: &str, path: &str) -> ProbeObservation {` | `FakeTransport::status [method]` | `8a9f4c08-2405-5339-bdb0-a96c7d0e2ec8` | 518-529 [crates/gcore/src/ai/probe.rs:518-529] | Indexed method `FakeTransport::status` in `crates/gcore/src/ai/probe.rs`. [crates/gcore/src/ai/probe.rs:518-529] |
