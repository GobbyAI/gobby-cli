---
title: crates/gcode/src/commands/embeddings_doctor.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/embeddings_doctor.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/embeddings_doctor.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/embeddings_doctor.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcode/src/commands/embeddings_doctor.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `EmbeddingsDoctorExit` | class | 'EmbeddingsDoctorExit' is a Rust struct that bundles an 'EmbeddingsDoctorReport' payload with a 'u8' process exit code. [crates/gcode/src/commands/embeddings_doctor.rs:19-22] |
| `EmbeddingsDoctorExit::exit_code` | method | Returns the stored 'exit_code' field from 'self' as a 'u8'. [crates/gcode/src/commands/embeddings_doctor.rs:25-27] |
| `EmbeddingsDoctorExit::print` | method | Prints 'self.payload' as JSON by delegating to 'output::print_json', returning its 'anyhow::Result<()>'. [crates/gcode/src/commands/embeddings_doctor.rs:29-31] |
| `EmbeddingsDoctorExit::fmt` | method | Formats the value as the string 'embeddings doctor failed with exit {exit_code}', where '{exit_code}' is taken from 'self.exit_code', and returns the result of writing that text to the provided formatter. [crates/gcode/src/commands/embeddings_doctor.rs:35-37] |
| `EmbeddingsDoctorReport` | class | 'EmbeddingsDoctorReport' is a serializable diagnostic record for an embeddings configuration, capturing the configured endpoint, model, vector dimension, probe error, API key presence and fingerprint, resolved namespace, source, agreement status, and any detected drift entries. [crates/gcode/src/commands/embeddings_doctor.rs:43-55] |
| `EmbeddingsDoctorDrift` | class | 'EmbeddingsDoctorDrift' is a crate-visible Serde-serializable data container that records a field name plus two comparison values, 'self' (renamed as 'self_value') and 'peer', both stored as untyped 'Value's. [crates/gcode/src/commands/embeddings_doctor.rs:58-63] |
| `PeerDoctorReport` | class | 'PeerDoctorReport' is a data container struct holding optional peer diagnostics fields for 'endpoint' ('String'), 'model' ('String'), and 'dim' ('usize'). [crates/gcode/src/commands/embeddings_doctor.rs:66-70] |
| `PeerDoctorOutcome` | type | Indexed type `PeerDoctorOutcome` in `crates/gcode/src/commands/embeddings_doctor.rs`. [crates/gcode/src/commands/embeddings_doctor.rs:73-77] |
| `run` | function | Connects to the database read-only, resolves embedding configuration, fetches the daemon peer, builds a doctor report, and returns 'Ok(())' with JSON output when healthy or an 'EmbeddingsDoctorExit' error carrying the payload and exit code otherwise. [crates/gcode/src/commands/embeddings_doctor.rs:79-95] |
| `probe_dim` | function | Converts 'probe_embedding_dim(config)' into a 'Result<usize, String>' by returning the probed embedding dimension on success and mapping any error to its string representation on failure. [crates/gcode/src/commands/embeddings_doctor.rs:97-99] |
| `build_doctor_report` | function | 'build_doctor_report' constructs an 'EmbeddingsDoctorReport' and exit code from optional embedding config resolution, optionally probing the configured embedding dimension on demand, short-circuiting on missing config or probe failure, and otherwise comparing the local config against a peer doctor outcome to mark healthy or report configuration drift. [crates/gcode/src/commands/embeddings_doctor.rs:101-165] |
| `report_without_peer` | function | Builds an 'EmbeddingsDoctorReport' from 'base_report(resolution, dim)' while explicitly clearing the 'agrees' and 'drift' fields to 'None'. [crates/gcode/src/commands/embeddings_doctor.rs:167-176] |
| `base_report` | function | Constructs an 'EmbeddingsDoctorReport' from an 'EmbeddingConfigDetails' by copying the API base, model, namespace, and source into the report, attaching the optional embedding dimension, recording whether an API key is present and its fingerprint if available, and leaving probe/drift/agreement fields unset. [crates/gcode/src/commands/embeddings_doctor.rs:178-195] |
| `drift_fields` | function | Compares the local embedding config’s 'endpoint', 'model', and optional 'dim' against a peer report, collecting 'EmbeddingsDoctorDrift' entries for any mismatches. [crates/gcode/src/commands/embeddings_doctor.rs:197-223] |
| `push_drift` | function | Appends a drift record to 'drift' for 'field' only when 'self_value' and 'peer_value' differ, serializing each 'Option<&str>' into either JSON null or a JSON string. [crates/gcode/src/commands/embeddings_doctor.rs:225-239] |
| `fetch_daemon_peer` | function | Performs a blocking HTTP GET to 'daemon_url + DAEMON_DOCTOR_PATH' with a 2-second timeout and returns 'PeerDoctorOutcome::Absent' when no URL is provided or the endpoint returns 404, 'Present(report)' when a successful response parses as 'PeerDoctorReport', and 'TransportError' for client construction, request, non-2xx status, or JSON parse failures. [crates/gcode/src/commands/embeddings_doctor.rs:241-276] |
| `details` | function | Constructs and returns an 'EmbeddingConfigDetails' with a fixed 'EmbeddingConfig' targeting 'http://embeddings.local/v1' using model 'embed-small', an optional copied 'api_key', no 'query_prefix', a 10-second timeout, 'embedding_keys::AI_NAMESPACE' as the namespace, and '"config_store"' as the source. [crates/gcode/src/commands/embeddings_doctor.rs:283-295] |

_Verified by 1 in-file unit test._

