---
title: crates/gcode/src/commands/embeddings_doctor.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/embeddings_doctor.rs
  ranges:
  - 19-22
  - 24-32
  - 25-27
  - 29-31
  - 34-38
  - 35-37
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
  - Purpose: `EmbeddingsDoctorExit` is a struct that encapsulates the results of an embeddings diagnostic operation, combining a diagnostic report payload with a u8 exit code. [crates/gcode/src/commands/embeddings_doctor.rs:19-22]
- `EmbeddingsDoctorExit` (class) component `EmbeddingsDoctorExit [class]` (`cb2a5a14-9402-504c-953c-a2354344c3cd`) lines 24-32 [crates/gcode/src/commands/embeddings_doctor.rs:24-32]
  - Signature: `impl EmbeddingsDoctorExit {`
  - Purpose: EmbeddingsDoctorExit provides methods to retrieve its exit code as a u8 and serialize its payload to JSON output. [crates/gcode/src/commands/embeddings_doctor.rs:24-32]
- `EmbeddingsDoctorExit.exit_code` (method) component `EmbeddingsDoctorExit.exit_code [method]` (`65ce4f1c-086b-5d3a-a976-55913e622d2b`) lines 25-27 [crates/gcode/src/commands/embeddings_doctor.rs:25-27]
  - Signature: `pub fn exit_code(&self) -> u8 {`
  - Purpose: Returns the exit code stored in the object as an unsigned 8-bit integer. [crates/gcode/src/commands/embeddings_doctor.rs:25-27]
- `EmbeddingsDoctorExit.print` (method) component `EmbeddingsDoctorExit.print [method]` (`fda4da2e-b9fa-5f7d-a085-5a41d0c15033`) lines 29-31 [crates/gcode/src/commands/embeddings_doctor.rs:29-31]
  - Signature: `pub fn print(&self) -> anyhow::Result<()> {`
  - Purpose: Delegates to `output::print_json` to serialize and output the instance's `payload` as JSON, returning an `anyhow::Result` that captures any serialization or I/O errors. [crates/gcode/src/commands/embeddings_doctor.rs:29-31]
- `EmbeddingsDoctorExit` (class) component `EmbeddingsDoctorExit [class]` (`7099d284-0e98-5e6f-8146-a8a26e7b0f17`) lines 34-38 [crates/gcode/src/commands/embeddings_doctor.rs:34-38]
  - Signature: `impl std::fmt::Display for EmbeddingsDoctorExit {`
  - Purpose: Implements the `Display` trait for `EmbeddingsDoctorExit` to format instances as a string message containing the embeddings doctor failure status and exit code. [crates/gcode/src/commands/embeddings_doctor.rs:34-38]
- `EmbeddingsDoctorExit.fmt` (method) component `EmbeddingsDoctorExit.fmt [method]` (`3c04e2c2-449c-5e4f-8428-7eed1f6a8617`) lines 35-37 [crates/gcode/src/commands/embeddings_doctor.rs:35-37]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Implements the `fmt` trait method to write a formatted error message displaying the embeddings doctor's exit code to the provided `Formatter`. [crates/gcode/src/commands/embeddings_doctor.rs:35-37]
- `EmbeddingsDoctorExit` (class) component `EmbeddingsDoctorExit [class]` (`1ca9b888-663a-5b5d-8970-352e87551a91`) lines 40-40 [crates/gcode/src/commands/embeddings_doctor.rs:40]
  - Signature: `impl std::error::Error for EmbeddingsDoctorExit {}`
  - Purpose: `EmbeddingsDoctorExit` implements the `std::error::Error` trait with default method implementations, enabling it to be used as an error type. [crates/gcode/src/commands/embeddings_doctor.rs:40]
- `EmbeddingsDoctorReport` (class) component `EmbeddingsDoctorReport [class]` (`43ae9df1-1856-5dd2-b305-c33cbfacd6c7`) lines 43-55 [crates/gcode/src/commands/embeddings_doctor.rs:43-55]
  - Signature: `pub(crate) struct EmbeddingsDoctorReport {`
  - Purpose: EmbeddingsDoctorReport is a crate-private struct that aggregates diagnostic information for embeddings service configuration, including endpoint/model metadata, API key validation, and configuration drift detection. [crates/gcode/src/commands/embeddings_doctor.rs:43-55]
- `EmbeddingsDoctorDrift` (class) component `EmbeddingsDoctorDrift [class]` (`211a83ad-ee72-5062-b837-06ed794edaac`) lines 58-63 [crates/gcode/src/commands/embeddings_doctor.rs:58-63]
  - Signature: `pub(crate) struct EmbeddingsDoctorDrift {`
  - Purpose: `EmbeddingsDoctorDrift` is a crate-internal struct that stores a field identifier and paired embedding values (self and peer) for comparative drift analysis or validation. [crates/gcode/src/commands/embeddings_doctor.rs:58-63]
- `PeerDoctorReport` (class) component `PeerDoctorReport [class]` (`94379149-0170-53f3-a099-785d235d3312`) lines 66-70 [crates/gcode/src/commands/embeddings_doctor.rs:66-70]
  - Signature: `struct PeerDoctorReport {`
  - Purpose: `PeerDoctorReport` is a struct containing three optional fields—endpoint (String), model (String), and dimension (usize)—for encapsulating peer doctor service metadata. [crates/gcode/src/commands/embeddings_doctor.rs:66-70]
- `PeerDoctorOutcome` (type) component `PeerDoctorOutcome [type]` (`6f4c2a6e-76cc-50b3-8302-548bd4d7d364`) lines 73-77 [crates/gcode/src/commands/embeddings_doctor.rs:73-77]
  - Signature: `enum PeerDoctorOutcome {`
  - Purpose: Indexed type `PeerDoctorOutcome` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:73-77]
- `run` (function) component `run [function]` (`8a6daa59-bd6e-542f-b2af-b47cb3dbe4c6`) lines 79-95 [crates/gcode/src/commands/embeddings_doctor.rs:79-95]
  - Signature: `pub fn run(ctx: &Context) -> anyhow::Result<()> {`
  - Purpose: Executes an embedding configuration health diagnostic by resolving database and daemon peer state, returning diagnostic results as JSON on success or an error-wrapped diagnostic payload on failure. [crates/gcode/src/commands/embeddings_doctor.rs:79-95]
- `probe_dim` (function) component `probe_dim [function]` (`4f070f22-e1f0-58df-932f-07e241a7c139`) lines 97-99 [crates/gcode/src/commands/embeddings_doctor.rs:97-99]
  - Signature: `fn probe_dim(config: &EmbeddingConfig) -> Result<usize, String> {`
  - Purpose: `probe_dim` determines the embedding dimension from a provided configuration, converting any error into a `String` error type via the `probe_embedding_dim` wrapper function. [crates/gcode/src/commands/embeddings_doctor.rs:97-99]
- `build_doctor_report` (function) component `build_doctor_report [function]` (`e5ce60bc-37e1-5343-a43b-7967ccddb4b5`) lines 101-165 [crates/gcode/src/commands/embeddings_doctor.rs:101-165]
  - Signature: `fn build_doctor_report(`
  - Purpose: Generates a diagnostic report that validates embedding configuration by probing dimensions and detecting configuration drift against a peer state, returning both the report and an exit status code. [crates/gcode/src/commands/embeddings_doctor.rs:101-165]
- `report_without_peer` (function) component `report_without_peer [function]` (`f0b436a4-269f-5dac-a1ce-106903c85d16`) lines 167-176 [crates/gcode/src/commands/embeddings_doctor.rs:167-176]
  - Signature: `fn report_without_peer(`
  - Purpose: Constructs an `EmbeddingsDoctorReport` with `agrees` and `drift` fields explicitly set to `None`, while preserving other fields from a base report derived from embedding configuration details and an optional dimension parameter. [crates/gcode/src/commands/embeddings_doctor.rs:167-176]
- `base_report` (function) component `base_report [function]` (`9490fdaf-3d1f-5d2e-99ea-de03193bc57e`) lines 178-195 [crates/gcode/src/commands/embeddings_doctor.rs:178-195]
  - Signature: `fn base_report(resolution: &EmbeddingConfigDetails, dim: Option<usize>) -> EmbeddingsDoctorReport {`
  - Purpose: Constructs an `EmbeddingsDoctorReport` by extracting API configuration and computing an API key fingerprint from the provided `EmbeddingConfigDetails`, while leaving diagnostic fields (`probe_error`, `agrees`, `drift`) uninitialized. [crates/gcode/src/commands/embeddings_doctor.rs:178-195]
- `drift_fields` (function) component `drift_fields [function]` (`d03feac3-535d-5648-9f53-0fbd1f9e40f5`) lines 197-223 [crates/gcode/src/commands/embeddings_doctor.rs:197-223]
  - Signature: `fn drift_fields(`
  - Purpose: Compares local embedding configuration (endpoint, model, dimension) against a peer report and returns a vector of detected configuration drift records for mismatched fields. [crates/gcode/src/commands/embeddings_doctor.rs:197-223]
- `push_drift` (function) component `push_drift [function]` (`f4690711-443b-594e-9f23-caf75279da14`) lines 225-239 [crates/gcode/src/commands/embeddings_doctor.rs:225-239]
  - Signature: `fn push_drift(`
  - Purpose: Appends a drift record to a vector only if the provided self and peer optional string values differ, converting both to JSON representations. [crates/gcode/src/commands/embeddings_doctor.rs:225-239]
- `fetch_daemon_peer` (function) component `fetch_daemon_peer [function]` (`eeff7fc5-e760-558b-8b93-d0653ff5c574`) lines 241-276 [crates/gcode/src/commands/embeddings_doctor.rs:241-276]
  - Signature: `fn fetch_daemon_peer(daemon_url: Option<&str>) -> PeerDoctorOutcome {`
  - Purpose: Fetches and deserializes a `PeerDoctorReport` from an optional daemon's HTTP endpoint, returning either the parsed report, an absence state, or a transport error. [crates/gcode/src/commands/embeddings_doctor.rs:241-276]
- `details` (function) component `details [function]` (`1314a11b-cde3-581f-9cf2-0e9bb03e47bd`) lines 283-295 [crates/gcode/src/commands/embeddings_doctor.rs:283-295]
  - Signature: `fn details(api_key: Option<&str>) -> EmbeddingConfigDetails {`
  - Purpose: This function constructs and returns an `EmbeddingConfigDetails` struct configured for a local embedding service endpoint ("embed-small" model) with optional API key authentication, a 10-second timeout, and an AI namespace identifier. [crates/gcode/src/commands/embeddings_doctor.rs:283-295]
- `doctor_json_and_exit_codes` (function) component `doctor_json_and_exit_codes [function]` (`e034bb1c-42a5-5fc7-aab3-a3d41b715d2a`) lines 298-362 [crates/gcode/src/commands/embeddings_doctor.rs:298-362]
  - Signature: `fn doctor_json_and_exit_codes() {`
  - Purpose: This test function verifies that `build_doctor_report` correctly generates appropriate exit codes (CONFIG_MISSING, HEALTHY, DRIFT) and JSON-serializable diagnostic reports for various embedding service configuration states. [crates/gcode/src/commands/embeddings_doctor.rs:298-362]

