---
title: crates/gcode/src/commands/embeddings_doctor.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/embeddings_doctor.rs
  ranges:
  - 19-22
  - 25-27
  - 29-31
  - 35-37
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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/embeddings_doctor.rs:19-22](crates/gcode/src/commands/embeddings_doctor.rs#L19-L22), [crates/gcode/src/commands/embeddings_doctor.rs:25-27](crates/gcode/src/commands/embeddings_doctor.rs#L25-L27), [crates/gcode/src/commands/embeddings_doctor.rs:29-31](crates/gcode/src/commands/embeddings_doctor.rs#L29-L31), [crates/gcode/src/commands/embeddings_doctor.rs:35-37](crates/gcode/src/commands/embeddings_doctor.rs#L35-L37), [crates/gcode/src/commands/embeddings_doctor.rs:43-55](crates/gcode/src/commands/embeddings_doctor.rs#L43-L55), [crates/gcode/src/commands/embeddings_doctor.rs:58-63](crates/gcode/src/commands/embeddings_doctor.rs#L58-L63), [crates/gcode/src/commands/embeddings_doctor.rs:66-70](crates/gcode/src/commands/embeddings_doctor.rs#L66-L70), [crates/gcode/src/commands/embeddings_doctor.rs:73-77](crates/gcode/src/commands/embeddings_doctor.rs#L73-L77), [crates/gcode/src/commands/embeddings_doctor.rs:79-95](crates/gcode/src/commands/embeddings_doctor.rs#L79-L95), [crates/gcode/src/commands/embeddings_doctor.rs:97-99](crates/gcode/src/commands/embeddings_doctor.rs#L97-L99), [crates/gcode/src/commands/embeddings_doctor.rs:101-165](crates/gcode/src/commands/embeddings_doctor.rs#L101-L165), [crates/gcode/src/commands/embeddings_doctor.rs:167-176](crates/gcode/src/commands/embeddings_doctor.rs#L167-L176), [crates/gcode/src/commands/embeddings_doctor.rs:178-195](crates/gcode/src/commands/embeddings_doctor.rs#L178-L195), [crates/gcode/src/commands/embeddings_doctor.rs:197-223](crates/gcode/src/commands/embeddings_doctor.rs#L197-L223), [crates/gcode/src/commands/embeddings_doctor.rs:225-239](crates/gcode/src/commands/embeddings_doctor.rs#L225-L239), [crates/gcode/src/commands/embeddings_doctor.rs:241-276](crates/gcode/src/commands/embeddings_doctor.rs#L241-L276), [crates/gcode/src/commands/embeddings_doctor.rs:283-295](crates/gcode/src/commands/embeddings_doctor.rs#L283-L295), [crates/gcode/src/commands/embeddings_doctor.rs:298-362](crates/gcode/src/commands/embeddings_doctor.rs#L298-L362)

</details>

# crates/gcode/src/commands/embeddings_doctor.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Implements the `embeddings doctor` command for checking embedding configuration health and consistency. It resolves the local embedding config from the database and standalone config, probes the embedding model dimension, optionally fetches a peer report from the daemon, and builds an `EmbeddingsDoctorReport` that includes endpoint/model/dim, API key fingerprint status, namespace/source information, drift details, and whether local and peer settings agree. `EmbeddingsDoctorExit` wraps that report with an exit code and printable JSON output, while helper functions assemble the base report, derive drift fields, classify peer outcomes, and map report states to the command’s exit codes.
[crates/gcode/src/commands/embeddings_doctor.rs:19-22]
[crates/gcode/src/commands/embeddings_doctor.rs:25-27]
[crates/gcode/src/commands/embeddings_doctor.rs:29-31]
[crates/gcode/src/commands/embeddings_doctor.rs:35-37]
[crates/gcode/src/commands/embeddings_doctor.rs:43-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `EmbeddingsDoctorExit` | class | `pub struct EmbeddingsDoctorExit {` | `EmbeddingsDoctorExit [class]` | `12434bb8-7bc0-59af-8fc2-579e71830d1e` | 19-22 [crates/gcode/src/commands/embeddings_doctor.rs:19-22] | Indexed class `EmbeddingsDoctorExit` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:19-22] |
| `EmbeddingsDoctorExit::exit_code` | method | `pub fn exit_code(&self) -> u8 {` | `EmbeddingsDoctorExit::exit_code [method]` | `65ce4f1c-086b-5d3a-a976-55913e622d2b` | 25-27 [crates/gcode/src/commands/embeddings_doctor.rs:25-27] | Indexed method `EmbeddingsDoctorExit::exit_code` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:25-27] |
| `EmbeddingsDoctorExit::print` | method | `pub fn print(&self) -> anyhow::Result<()> {` | `EmbeddingsDoctorExit::print [method]` | `fda4da2e-b9fa-5f7d-a085-5a41d0c15033` | 29-31 [crates/gcode/src/commands/embeddings_doctor.rs:29-31] | Indexed method `EmbeddingsDoctorExit::print` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:29-31] |
| `EmbeddingsDoctorExit::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `EmbeddingsDoctorExit::fmt [method]` | `3c04e2c2-449c-5e4f-8428-7eed1f6a8617` | 35-37 [crates/gcode/src/commands/embeddings_doctor.rs:35-37] | Indexed method `EmbeddingsDoctorExit::fmt` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:35-37] |
| `EmbeddingsDoctorReport` | class | `pub(crate) struct EmbeddingsDoctorReport {` | `EmbeddingsDoctorReport [class]` | `43ae9df1-1856-5dd2-b305-c33cbfacd6c7` | 43-55 [crates/gcode/src/commands/embeddings_doctor.rs:43-55] | Indexed class `EmbeddingsDoctorReport` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:43-55] |
| `EmbeddingsDoctorDrift` | class | `pub(crate) struct EmbeddingsDoctorDrift {` | `EmbeddingsDoctorDrift [class]` | `211a83ad-ee72-5062-b837-06ed794edaac` | 58-63 [crates/gcode/src/commands/embeddings_doctor.rs:58-63] | Indexed class `EmbeddingsDoctorDrift` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:58-63] |
| `PeerDoctorReport` | class | `struct PeerDoctorReport {` | `PeerDoctorReport [class]` | `94379149-0170-53f3-a099-785d235d3312` | 66-70 [crates/gcode/src/commands/embeddings_doctor.rs:66-70] | Indexed class `PeerDoctorReport` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:66-70] |
| `PeerDoctorOutcome` | type | `enum PeerDoctorOutcome {` | `PeerDoctorOutcome [type]` | `6f4c2a6e-76cc-50b3-8302-548bd4d7d364` | 73-77 [crates/gcode/src/commands/embeddings_doctor.rs:73-77] | Indexed type `PeerDoctorOutcome` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:73-77] |
| `run` | function | `pub fn run(ctx: &Context) -> anyhow::Result<()> {` | `run [function]` | `8a6daa59-bd6e-542f-b2af-b47cb3dbe4c6` | 79-95 [crates/gcode/src/commands/embeddings_doctor.rs:79-95] | Indexed function `run` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:79-95] |
| `probe_dim` | function | `fn probe_dim(config: &EmbeddingConfig) -> Result<usize, String> {` | `probe_dim [function]` | `55263059-4a9f-5135-8fd6-911a3a1fc963` | 97-99 [crates/gcode/src/commands/embeddings_doctor.rs:97-99] | Indexed function `probe_dim` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:97-99] |
| `build_doctor_report` | function | `fn build_doctor_report(` | `build_doctor_report [function]` | `15eefe31-f4fe-5eeb-8249-a1f2db4362d8` | 101-165 [crates/gcode/src/commands/embeddings_doctor.rs:101-165] | Indexed function `build_doctor_report` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:101-165] |
| `report_without_peer` | function | `fn report_without_peer(` | `report_without_peer [function]` | `51b4a01f-27bc-5f31-9175-c96dffe4c298` | 167-176 [crates/gcode/src/commands/embeddings_doctor.rs:167-176] | Indexed function `report_without_peer` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:167-176] |
| `base_report` | function | `fn base_report(resolution: &EmbeddingConfigDetails, dim: Option<usize>) -> EmbeddingsDoctorReport {` | `base_report [function]` | `c7c143ce-f13d-5ec7-8849-9b9ef631ec2c` | 178-195 [crates/gcode/src/commands/embeddings_doctor.rs:178-195] | Indexed function `base_report` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:178-195] |
| `drift_fields` | function | `fn drift_fields(` | `drift_fields [function]` | `e2cccc41-6ceb-50a3-888b-93f2976e683a` | 197-223 [crates/gcode/src/commands/embeddings_doctor.rs:197-223] | Indexed function `drift_fields` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:197-223] |
| `push_drift` | function | `fn push_drift(` | `push_drift [function]` | `e7d4a144-96f7-5003-9c50-6c5e56e0fd5a` | 225-239 [crates/gcode/src/commands/embeddings_doctor.rs:225-239] | Indexed function `push_drift` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:225-239] |
| `fetch_daemon_peer` | function | `fn fetch_daemon_peer(daemon_url: Option<&str>) -> PeerDoctorOutcome {` | `fetch_daemon_peer [function]` | `46461ac9-c515-5d46-a7a9-28134d2c2739` | 241-276 [crates/gcode/src/commands/embeddings_doctor.rs:241-276] | Indexed function `fetch_daemon_peer` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:241-276] |
| `details` | function | `fn details(api_key: Option<&str>) -> EmbeddingConfigDetails {` | `details [function]` | `1e0ecaf9-8d08-59fe-8915-e6980495a2b1` | 283-295 [crates/gcode/src/commands/embeddings_doctor.rs:283-295] | Indexed function `details` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:283-295] |
| `doctor_json_and_exit_codes` | function | `fn doctor_json_and_exit_codes() {` | `doctor_json_and_exit_codes [function]` | `a29450fb-51c5-5de5-a9ae-eaf9de617d48` | 298-362 [crates/gcode/src/commands/embeddings_doctor.rs:298-362] | Indexed function `doctor_json_and_exit_codes` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:298-362] |
