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
  - 62-76
  - 79-83
  - 90-95
  - 98-105
  - 108-126
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/daemon.rs

Module: [[code/modules/crates/gsqz/src|crates/gsqz/src]]

## Purpose

This module provides best-effort integration with the Gobby daemon behind the `gobby` feature flag: it fetches compression settings from the daemon’s config endpoint, reports compression savings to an admin endpoint, and resolves the daemon base URL from either a config override with `${GOBBY_PORT}` expansion or a shared fallback resolver. When the feature is disabled, the same APIs degrade to no-ops that return `None` or do nothing, and the tests verify passthrough behavior, environment-variable expansion, and bootstrap-based URL resolution.
[crates/gsqz/src/daemon.rs:11-23]
[crates/gsqz/src/daemon.rs:26-28]
[crates/gsqz/src/daemon.rs:32-43]
[crates/gsqz/src/daemon.rs:46-53]
[crates/gsqz/src/daemon.rs:62-76]

## API Symbols

- `fetch_daemon_config` (function) component `fetch_daemon_config [function]` (`0b8e338f-d1bc-5d06-b96c-33edf5fa41b8`) lines 11-23 [crates/gsqz/src/daemon.rs:11-23]
  - Signature: `pub fn fetch_daemon_config(base_url: &str) -> Option<(usize, usize)> {`
  - Purpose: Fetches output compression configuration parameters (minimum output length and maximum compressed lines) from a remote daemon's HTTP API endpoint and returns them as a `(usize, usize)` tuple, or `None` if the request or JSON extraction fails. [crates/gsqz/src/daemon.rs:11-23]
- `fetch_daemon_config` (function) component `fetch_daemon_config [function]` (`4e16af20-55b1-5d02-82e2-d3287ca9a822`) lines 26-28 [crates/gsqz/src/daemon.rs:26-28]
  - Signature: `pub fn fetch_daemon_config(_base_url: &str) -> Option<(usize, usize)> {`
  - Purpose: This function is a stub implementation that unconditionally returns `None` instead of fetching daemon configuration data (represented as a tuple of two `usize` values) from the provided base URL. [crates/gsqz/src/daemon.rs:26-28]
- `report_savings` (function) component `report_savings [function]` (`fd4f33a8-f75a-5dc4-b46a-0db4058614d4`) lines 32-43 [crates/gsqz/src/daemon.rs:32-43]
  - Signature: `pub fn report_savings(base_url: &str, strategy: &str, original_chars: usize, actual_chars: usize) {`
  - Purpose: POSTs compression savings metrics (original and actual character counts with strategy metadata) to a remote admin API endpoint with a 1-second timeout, ignoring the response. [crates/gsqz/src/daemon.rs:32-43]
- `report_savings` (function) component `report_savings [function]` (`da6d2d31-de6d-5a53-a862-624222237f42`) lines 46-53 [crates/gsqz/src/daemon.rs:46-53]
  - Signature: `pub fn report_savings(`
  - Purpose: A feature-gated no-op placeholder function that accepts a base URL, strategy identifier, and character count metrics (original vs. actual) but performs no operations when the gobby feature is disabled. [crates/gsqz/src/daemon.rs:46-53]
- `resolve_daemon_url` (function) component `resolve_daemon_url [function]` (`1f4837e5-07a9-54ab-ae65-808fef0937c5`) lines 62-76 [crates/gsqz/src/daemon.rs:62-76]
  - Signature: `pub fn resolve_daemon_url(config_url: Option<&str>) -> Option<String> {`
  - Purpose: Resolves a daemon URL by substituting the `GOBBY_PORT` environment variable into `${GOBBY_PORT}` placeholders within a provided configuration URL, or falls back to the default daemon URL resolver if none is provided or the environment variable is unset. [crates/gsqz/src/daemon.rs:62-76]
- `resolve_daemon_url` (function) component `resolve_daemon_url [function]` (`5257d186-f60a-596a-a9a9-5b71f341d9ed`) lines 79-83 [crates/gsqz/src/daemon.rs:79-83]
  - Signature: `pub fn resolve_daemon_url(_config_url: Option<&str>) -> Option<String> {`
  - Purpose: Unconditionally returns `None`, providing a feature-disabled no-op implementation of daemon URL resolution. [crates/gsqz/src/daemon.rs:79-83]
- `config_url_passes_through` (function) component `config_url_passes_through [function]` (`850e7143-4c06-5d9d-97e5-7115ab51a19b`) lines 90-95 [crates/gsqz/src/daemon.rs:90-95]
  - Signature: `fn config_url_passes_through() {`
  - Purpose: Verifies that `resolve_daemon_url` returns the input custom daemon URL (`http://custom:9999`) unmodified when supplied with a `Some` value. [crates/gsqz/src/daemon.rs:90-95]
- `config_url_expands_gobby_port` (function) component `config_url_expands_gobby_port [function]` (`53136695-8e03-52ae-897c-e81b6fcf860b`) lines 98-105 [crates/gsqz/src/daemon.rs:98-105]
  - Signature: `fn config_url_expands_gobby_port() {`
  - Purpose: Unit test verifying that `resolve_daemon_url` correctly performs environment variable substitution of `${GOBBY_PORT}` in a configuration URL. [crates/gsqz/src/daemon.rs:98-105]
- `no_config_reads_bootstrap_daemon_port` (function) component `no_config_reads_bootstrap_daemon_port [function]` (`93008e10-d1c6-51cb-8a49-f51dbb842f13`) lines 108-126 [crates/gsqz/src/daemon.rs:108-126]
  - Signature: `fn no_config_reads_bootstrap_daemon_port() {`
  - Purpose: Tests that `resolve_daemon_url(None)` correctly resolves the daemon URL from a bootstrap.yaml configuration file when environment variables `GOBBY_DAEMON_URL` and `GOBBY_PORT` are unset. [crates/gsqz/src/daemon.rs:108-126]

