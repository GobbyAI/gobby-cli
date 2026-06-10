---
title: crates/gsqz/src/daemon.rs
type: code_file
provenance:
- file: crates/gsqz/src/daemon.rs
  ranges:
  - 11-23
  - 26-28
  - 32-43
  - 46-53
  - 60-80
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/daemon.rs

Module: [[code/modules/crates/gsqz/src|crates/gsqz/src]]

## Purpose

`crates/gsqz/src/daemon.rs` exposes 5 indexed API symbols.
[crates/gsqz/src/daemon.rs:11-23]
[crates/gsqz/src/daemon.rs:26-28]
[crates/gsqz/src/daemon.rs:32-43]
[crates/gsqz/src/daemon.rs:46-53]
[crates/gsqz/src/daemon.rs:60-80]

## API Symbols

- `fetch_daemon_config` (function) component `fetch_daemon_config [function]` (`0b8e338f-d1bc-5d06-b96c-33edf5fa41b8`) lines 11-23 [crates/gsqz/src/daemon.rs:11-23]
  - Signature: `pub fn fetch_daemon_config(base_url: &str) -> Option<(usize, usize)> {`
  - Purpose: Fetches output compression configuration parameters (minimum output length and maximum compressed lines) from a daemon's HTTP API endpoint via synchronous GET request with 1-second timeout, returning the thresholds as a tuple or None on failure. [crates/gsqz/src/daemon.rs:11-23]
- `fetch_daemon_config` (function) component `fetch_daemon_config [function]` (`4e16af20-55b1-5d02-82e2-d3287ca9a822`) lines 26-28 [crates/gsqz/src/daemon.rs:26-28]
  - Signature: `pub fn fetch_daemon_config(_base_url: &str) -> Option<(usize, usize)> {`
  - Purpose: This function is a stub implementation that unconditionally returns `None` instead of fetching daemon configuration parameters from the provided base URL as an `Option` containing a tuple of two `usize` values. [crates/gsqz/src/daemon.rs:26-28]
- `report_savings` (function) component `report_savings [function]` (`fd4f33a8-f75a-5dc4-b46a-0db4058614d4`) lines 32-43 [crates/gsqz/src/daemon.rs:32-43]
  - Signature: `pub fn report_savings(base_url: &str, strategy: &str, original_chars: usize, actual_chars: usize) {`
  - Purpose: Sends a fire-and-forget POST request to record compression metrics (original/actual character counts and strategy identifier) to a remote admin API endpoint with a 1-second timeout. [crates/gsqz/src/daemon.rs:32-43]
- `report_savings` (function) component `report_savings [function]` (`da6d2d31-de6d-5a53-a862-624222237f42`) lines 46-53 [crates/gsqz/src/daemon.rs:46-53]
  - Signature: `pub fn report_savings(`
  - Purpose: A feature-gated stub function that accepts compression strategy metadata and character count metrics for telemetry reporting but performs no operations without the `gobby` feature enabled. [crates/gsqz/src/daemon.rs:46-53]
- `resolve_daemon_url` (function) component `resolve_daemon_url [function]` (`9e68b30a-0806-52cd-bac9-4216c582b330`) lines 60-80 [crates/gsqz/src/daemon.rs:60-80]
  - Signature: `pub fn resolve_daemon_url(config_url: Option<&str>) -> Option<String> {`
  - Purpose: Resolves the Gobby daemon URL by performing `${GOBBY_PORT}` variable substitution on a config URL, falling back to constructing `http://localhost:{GOBBY_PORT}` from the environment variable, or defaulting to `http://localhost:60887`. [crates/gsqz/src/daemon.rs:60-80]

