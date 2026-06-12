---
title: crates/gcode/src/commands/embeddings_doctor.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/embeddings_doctor.rs
  ranges:
  - 19-22
  - 24-32
  - 34-38
  - '40'
  - 43-55
  - 58-63
  - 66-70
  - 73-77
  - 79-95
  - 97-99
  - 101-165
  - 167-176
  - 178-195
  - 197-223
  - 225-239
  - 241-276
  - 283-295
  - 298-362
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/embeddings_doctor.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/embeddings_doctor.rs` exposes 21 indexed API symbols.
[crates/gcode/src/commands/embeddings_doctor.rs:19-22]
[crates/gcode/src/commands/embeddings_doctor.rs:24-32]
[crates/gcode/src/commands/embeddings_doctor.rs:25-27]
[crates/gcode/src/commands/embeddings_doctor.rs:29-31]
[crates/gcode/src/commands/embeddings_doctor.rs:34-38]

## API Symbols

- `EmbeddingsDoctorExit` (class) component `EmbeddingsDoctorExit [class]` (`12434bb8-7bc0-59af-8fc2-579e71830d1e`) lines 19-22 [crates/gcode/src/commands/embeddings_doctor.rs:19-22]
  - Signature: `pub struct EmbeddingsDoctorExit {`
  - Purpose: Indexed class `EmbeddingsDoctorExit` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:19-22]
- `EmbeddingsDoctorExit` (class) component `EmbeddingsDoctorExit [class]` (`cb2a5a14-9402-504c-953c-a2354344c3cd`) lines 24-32 [crates/gcode/src/commands/embeddings_doctor.rs:24-32]
  - Signature: `impl EmbeddingsDoctorExit {`
  - Purpose: Indexed class `EmbeddingsDoctorExit` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:24-32]
- `EmbeddingsDoctorExit.exit_code` (method) component `EmbeddingsDoctorExit.exit_code [method]` (`65ce4f1c-086b-5d3a-a976-55913e622d2b`) lines 25-27 [crates/gcode/src/commands/embeddings_doctor.rs:25-27]
  - Signature: `pub fn exit_code(&self) -> u8 {`
  - Purpose: Indexed method `EmbeddingsDoctorExit.exit_code` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:25-27]
- `EmbeddingsDoctorExit.print` (method) component `EmbeddingsDoctorExit.print [method]` (`fda4da2e-b9fa-5f7d-a085-5a41d0c15033`) lines 29-31 [crates/gcode/src/commands/embeddings_doctor.rs:29-31]
  - Signature: `pub fn print(&self) -> anyhow::Result<()> {`
  - Purpose: Indexed method `EmbeddingsDoctorExit.print` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:29-31]
- `EmbeddingsDoctorExit` (class) component `EmbeddingsDoctorExit [class]` (`7099d284-0e98-5e6f-8146-a8a26e7b0f17`) lines 34-38 [crates/gcode/src/commands/embeddings_doctor.rs:34-38]
  - Signature: `impl std::fmt::Display for EmbeddingsDoctorExit {`
  - Purpose: Indexed class `EmbeddingsDoctorExit` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:34-38]
- `EmbeddingsDoctorExit.fmt` (method) component `EmbeddingsDoctorExit.fmt [method]` (`3c04e2c2-449c-5e4f-8428-7eed1f6a8617`) lines 35-37 [crates/gcode/src/commands/embeddings_doctor.rs:35-37]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Indexed method `EmbeddingsDoctorExit.fmt` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:35-37]
- `EmbeddingsDoctorExit` (class) component `EmbeddingsDoctorExit [class]` (`1ca9b888-663a-5b5d-8970-352e87551a91`) lines 40-40 [crates/gcode/src/commands/embeddings_doctor.rs:40]
  - Signature: `impl std::error::Error for EmbeddingsDoctorExit {}`
  - Purpose: Indexed class `EmbeddingsDoctorExit` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:40]
- `EmbeddingsDoctorReport` (class) component `EmbeddingsDoctorReport [class]` (`43ae9df1-1856-5dd2-b305-c33cbfacd6c7`) lines 43-55 [crates/gcode/src/commands/embeddings_doctor.rs:43-55]
  - Signature: `pub(crate) struct EmbeddingsDoctorReport {`
  - Purpose: Indexed class `EmbeddingsDoctorReport` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:43-55]
- `EmbeddingsDoctorDrift` (class) component `EmbeddingsDoctorDrift [class]` (`211a83ad-ee72-5062-b837-06ed794edaac`) lines 58-63 [crates/gcode/src/commands/embeddings_doctor.rs:58-63]
  - Signature: `pub(crate) struct EmbeddingsDoctorDrift {`
  - Purpose: Indexed class `EmbeddingsDoctorDrift` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:58-63]
- `PeerDoctorReport` (class) component `PeerDoctorReport [class]` (`94379149-0170-53f3-a099-785d235d3312`) lines 66-70 [crates/gcode/src/commands/embeddings_doctor.rs:66-70]
  - Signature: `struct PeerDoctorReport {`
  - Purpose: Indexed class `PeerDoctorReport` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:66-70]
- `PeerDoctorOutcome` (type) component `PeerDoctorOutcome [type]` (`6f4c2a6e-76cc-50b3-8302-548bd4d7d364`) lines 73-77 [crates/gcode/src/commands/embeddings_doctor.rs:73-77]
  - Signature: `enum PeerDoctorOutcome {`
  - Purpose: Indexed type `PeerDoctorOutcome` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:73-77]
- `run` (function) component `run [function]` (`8a6daa59-bd6e-542f-b2af-b47cb3dbe4c6`) lines 79-95 [crates/gcode/src/commands/embeddings_doctor.rs:79-95]
  - Signature: `pub fn run(ctx: &Context) -> anyhow::Result<()> {`
  - Purpose: Indexed function `run` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:79-95]
- `probe_dim` (function) component `probe_dim [function]` (`55263059-4a9f-5135-8fd6-911a3a1fc963`) lines 97-99 [crates/gcode/src/commands/embeddings_doctor.rs:97-99]
  - Signature: `fn probe_dim(config: &EmbeddingConfig) -> Result<usize, String> {`
  - Purpose: Indexed function `probe_dim` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:97-99]
- `build_doctor_report` (function) component `build_doctor_report [function]` (`15eefe31-f4fe-5eeb-8249-a1f2db4362d8`) lines 101-165 [crates/gcode/src/commands/embeddings_doctor.rs:101-165]
  - Signature: `fn build_doctor_report(`
  - Purpose: Indexed function `build_doctor_report` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:101-165]
- `report_without_peer` (function) component `report_without_peer [function]` (`51b4a01f-27bc-5f31-9175-c96dffe4c298`) lines 167-176 [crates/gcode/src/commands/embeddings_doctor.rs:167-176]
  - Signature: `fn report_without_peer(`
  - Purpose: Indexed function `report_without_peer` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:167-176]
- `base_report` (function) component `base_report [function]` (`c7c143ce-f13d-5ec7-8849-9b9ef631ec2c`) lines 178-195 [crates/gcode/src/commands/embeddings_doctor.rs:178-195]
  - Signature: `fn base_report(resolution: &EmbeddingConfigDetails, dim: Option<usize>) -> EmbeddingsDoctorReport {`
  - Purpose: Indexed function `base_report` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:178-195]
- `drift_fields` (function) component `drift_fields [function]` (`e2cccc41-6ceb-50a3-888b-93f2976e683a`) lines 197-223 [crates/gcode/src/commands/embeddings_doctor.rs:197-223]
  - Signature: `fn drift_fields(`
  - Purpose: Indexed function `drift_fields` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:197-223]
- `push_drift` (function) component `push_drift [function]` (`e7d4a144-96f7-5003-9c50-6c5e56e0fd5a`) lines 225-239 [crates/gcode/src/commands/embeddings_doctor.rs:225-239]
  - Signature: `fn push_drift(`
  - Purpose: Indexed function `push_drift` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:225-239]
- `fetch_daemon_peer` (function) component `fetch_daemon_peer [function]` (`46461ac9-c515-5d46-a7a9-28134d2c2739`) lines 241-276 [crates/gcode/src/commands/embeddings_doctor.rs:241-276]
  - Signature: `fn fetch_daemon_peer(daemon_url: Option<&str>) -> PeerDoctorOutcome {`
  - Purpose: Indexed function `fetch_daemon_peer` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:241-276]
- `details` (function) component `details [function]` (`1e0ecaf9-8d08-59fe-8915-e6980495a2b1`) lines 283-295 [crates/gcode/src/commands/embeddings_doctor.rs:283-295]
  - Signature: `fn details(api_key: Option<&str>) -> EmbeddingConfigDetails {`
  - Purpose: Indexed function `details` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:283-295]
- `doctor_json_and_exit_codes` (function) component `doctor_json_and_exit_codes [function]` (`a29450fb-51c5-5de5-a9ae-eaf9de617d48`) lines 298-362 [crates/gcode/src/commands/embeddings_doctor.rs:298-362]
  - Signature: `fn doctor_json_and_exit_codes() {`
  - Purpose: Indexed function `doctor_json_and_exit_codes` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:298-362]

