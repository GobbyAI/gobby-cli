---
title: crates/gcore/src/daemon_url.rs
type: code_file
provenance:
- file: crates/gcore/src/daemon_url.rs
  ranges:
  - 28-34
  - 40-42
  - 47-59
  - 61-64
  - 72-78
  - 86-91
  - 94-98
  - 101-104
  - 107-114
  - 117-124
  - 127-130
  - 133-136
  - 139-146
  - 149-156
  - 159-164
  - 167-172
  - 175-180
  - 183-187
  - 190-192
  - 195-234
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/daemon_url.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Resolves the daemon’s dial URL for Gobby binaries, applying a shared precedence order: `GOBBY_DAEMON_URL` first, then `GOBBY_PORT`, then the persisted `bootstrap.yaml` endpoint. `daemon_url` and `daemon_url_at` provide the public entry points, `env_override` normalizes and validates environment overrides, and `endpoint_to_url` plus `dial_host` turn a bootstrap `DaemonEndpoint` into a usable `http://host:port` address by mapping unroutable wildcard hosts to loopback and formatting IPv6 correctly. The test helpers and cases verify the fallback order and host normalization rules.
[crates/gcore/src/daemon_url.rs:28-34]
[crates/gcore/src/daemon_url.rs:40-42]
[crates/gcore/src/daemon_url.rs:47-59]
[crates/gcore/src/daemon_url.rs:61-64]
[crates/gcore/src/daemon_url.rs:72-78]

## API Symbols

- `daemon_url` (function) component `daemon_url [function]` (`326f3e81-0586-5929-9847-dea92091ab82`) lines 28-34 [crates/gcore/src/daemon_url.rs:28-34]
  - Signature: `pub fn daemon_url() -> String {`
  - Purpose: Returns the daemon base URL by first consulting 'GOBBY_DAEMON_URL' and 'GOBBY_PORT' environment overrides via 'env_override', then falling back to converting the persisted daemon endpoint from 'read_daemon_endpoint()' with 'endpoint_to_url()'. [crates/gcore/src/daemon_url.rs:28-34]
- `daemon_url_at` (function) component `daemon_url_at [function]` (`cfcb2d54-4c9f-567e-837e-c03378a2f53d`) lines 40-42 [crates/gcore/src/daemon_url.rs:40-42]
  - Signature: `pub fn daemon_url_at(path: &Path) -> String {`
  - Purpose: Returns the URL string for the daemon endpoint read from the given filesystem path by delegating to 'read_daemon_endpoint_at(path)' and converting the result with 'endpoint_to_url'. [crates/gcore/src/daemon_url.rs:40-42]
- `env_override` (function) component `env_override [function]` (`4ace3e35-0f9e-51b8-8d62-264fbaac264d`) lines 47-59 [crates/gcore/src/daemon_url.rs:47-59]
  - Signature: `fn env_override(url: Option<&str>, port: Option<&str>) -> Option<String> {`
  - Purpose: Returns a normalized override URL by preferring a non-empty 'url' (trimmed and with any trailing '/' removed), otherwise parsing 'port' as a 'u16' and formatting 'http://127.0.0.1:{port}', or 'None' if neither yields a valid value. [crates/gcore/src/daemon_url.rs:47-59]
- `endpoint_to_url` (function) component `endpoint_to_url [function]` (`121a4f74-0310-5cc0-9249-4d77f94eca97`) lines 61-64 [crates/gcore/src/daemon_url.rs:61-64]
  - Signature: `fn endpoint_to_url(endpoint: &DaemonEndpoint) -> String {`
  - Purpose: Converts a 'DaemonEndpoint' into an 'http://host:port' URL string by normalizing 'endpoint.host' with 'dial_host' and formatting it with 'endpoint.port'. [crates/gcore/src/daemon_url.rs:61-64]
- `dial_host` (function) component `dial_host [function]` (`e6102bbd-d2ea-59e7-8b82-2b6273b47e29`) lines 72-78 [crates/gcore/src/daemon_url.rs:72-78]
  - Signature: `fn dial_host(host: &str) -> Cow<'_, str> {`
  - Purpose: Returns a normalized host string for dialing by mapping unspecified addresses to '127.0.0.1', wrapping bare IPv6 literals in brackets, and otherwise returning the trimmed host unchanged. [crates/gcore/src/daemon_url.rs:72-78]
- `write_bootstrap` (function) component `write_bootstrap [function]` (`36ad539e-894c-5ed2-939b-1c78d64c3302`) lines 86-91 [crates/gcore/src/daemon_url.rs:86-91]
  - Signature: `fn write_bootstrap(contents: &str) -> (tempfile::TempDir, std::path::PathBuf) {`
  - Purpose: Creates a new temporary directory, writes 'contents' to 'bootstrap.yaml' inside it, and returns the 'TempDir' along with the file path. [crates/gcore/src/daemon_url.rs:86-91]
- `default_url_when_file_missing` (function) component `default_url_when_file_missing [function]` (`852e94ac-199c-5a57-a199-c97c9d5865f4`) lines 94-98 [crates/gcore/src/daemon_url.rs:94-98]
  - Signature: `fn default_url_when_file_missing() {`
  - Purpose: Verifies that 'daemon_url_at' returns the default daemon URL 'http://127.0.0.1:60887' when given a path to a missing file. [crates/gcore/src/daemon_url.rs:94-98]
- `wildcard_ipv4_normalizes_to_loopback` (function) component `wildcard_ipv4_normalizes_to_loopback [function]` (`2dfaca7b-c395-5429-9c23-f68a9bc89d7f`) lines 101-104 [crates/gcore/src/daemon_url.rs:101-104]
  - Signature: `fn wildcard_ipv4_normalizes_to_loopback() {`
  - Purpose: Verifies that a bootstrap config with 'bind_host: 0.0.0.0' is normalized by 'daemon_url_at' to use the loopback URL 'http://127.0.0.1:60887'. [crates/gcore/src/daemon_url.rs:101-104]
- `wildcard_ipv6_normalizes_to_loopback` (function) component `wildcard_ipv6_normalizes_to_loopback [function]` (`9b0f11b9-b1d9-5abc-b3e0-f7c906b13ef7`) lines 107-114 [crates/gcore/src/daemon_url.rs:107-114]
  - Signature: `fn wildcard_ipv6_normalizes_to_loopback() {`
  - Purpose: Verifies that a bootstrap config binding to IPv6 wildcard '::' is normalized by 'daemon_url_at' to 'http://127.0.0.1:60887' rather than preserving the wildcard host. [crates/gcore/src/daemon_url.rs:107-114]
- `wildcard_ipv6_zero_normalizes_to_loopback` (function) component `wildcard_ipv6_zero_normalizes_to_loopback [function]` (`f319eed9-b5ef-512f-a08d-0beace3700db`) lines 117-124 [crates/gcore/src/daemon_url.rs:117-124]
  - Signature: `fn wildcard_ipv6_zero_normalizes_to_loopback() {`
  - Purpose: Verifies that a bootstrap config with 'bind_host: "::0"' is normalized by 'daemon_url_at' to 'http://127.0.0.1:60887' rather than an IPv6 wildcard address. [crates/gcore/src/daemon_url.rs:117-124]
- `localhost_passes_through` (function) component `localhost_passes_through [function]` (`e1dee3b2-12bd-5639-980f-5619a68bbc06`) lines 127-130 [crates/gcore/src/daemon_url.rs:127-130]
  - Signature: `fn localhost_passes_through() {`
  - Purpose: Verifies that when the bootstrap config binds the daemon to 'localhost' on port '60887', 'daemon_url_at(&path)' returns the corresponding 'http://localhost:60887' URL. [crates/gcore/src/daemon_url.rs:127-130]
- `custom_port_and_host_compose` (function) component `custom_port_and_host_compose [function]` (`1e3f7ed5-12fb-507b-b07a-4517266efa47`) lines 133-136 [crates/gcore/src/daemon_url.rs:133-136]
  - Signature: `fn custom_port_and_host_compose() {`
  - Purpose: Verifies that 'daemon_url_at' composes an HTTP URL from bootstrap settings by combining a custom 'bind_host' and 'daemon_port' into 'http://10.0.0.5:61234'. [crates/gcore/src/daemon_url.rs:133-136]
- `bare_ipv6_literal_is_bracketed` (function) component `bare_ipv6_literal_is_bracketed [function]` (`a116da61-3342-523d-ad1c-e4a7627ac8f5`) lines 139-146 [crates/gcore/src/daemon_url.rs:139-146]
  - Signature: `fn bare_ipv6_literal_is_bracketed() {`
  - Purpose: Verifies that when the daemon is configured with the bare IPv6 host '::1' and port '61234', 'daemon_url_at' formats the URL as 'http://:61234' with the IPv6 literal bracketed. [crates/gcore/src/daemon_url.rs:139-146]
- `bracketed_ipv6_literal_passes_through` (function) component `bracketed_ipv6_literal_passes_through [function]` (`d54a7599-b7c1-5a37-8535-f76fbe9f75e1`) lines 149-156 [crates/gcore/src/daemon_url.rs:149-156]
  - Signature: `fn bracketed_ipv6_literal_passes_through() {`
  - Purpose: Verifies that a bootstrap config with 'bind_host' set to the bracketed IPv6 loopback literal '""' is preserved by 'daemon_url_at', yielding 'http://:61234'. [crates/gcore/src/daemon_url.rs:149-156]
- `env_override_url_beats_port` (function) component `env_override_url_beats_port [function]` (`d081cffc-518e-5684-ab97-23ebb4152bee`) lines 159-164 [crates/gcore/src/daemon_url.rs:159-164]
  - Signature: `fn env_override_url_beats_port() {`
  - Purpose: Verifies that when both an override URL and a port are provided, 'env_override' returns the override URL unchanged instead of constructing a URL from the port. [crates/gcore/src/daemon_url.rs:159-164]
- `env_override_url_trims_trailing_slashes` (function) component `env_override_url_trims_trailing_slashes [function]` (`fd901039-e803-5509-9664-2392f6c61fbf`) lines 167-172 [crates/gcore/src/daemon_url.rs:167-172]
  - Signature: `fn env_override_url_trims_trailing_slashes() {`
  - Purpose: Verifies that 'env_override' strips a trailing slash from an override URL provided via the environment and returns the normalized URL string. [crates/gcore/src/daemon_url.rs:167-172]
- `env_override_empty_url_falls_back_to_port` (function) component `env_override_empty_url_falls_back_to_port [function]` (`421354aa-d3e4-5ebf-a8e7-e836d53d7653`) lines 175-180 [crates/gcore/src/daemon_url.rs:175-180]
  - Signature: `fn env_override_empty_url_falls_back_to_port() {`
  - Purpose: Verifies that when the URL environment override is an empty string and a port is provided, 'env_override' falls back to constructing 'http://127.0.0.1:<port>' instead of returning an empty URL. [crates/gcore/src/daemon_url.rs:175-180]
- `env_override_ignores_unparseable_or_empty_port` (function) component `env_override_ignores_unparseable_or_empty_port [function]` (`faad7146-3356-5d8c-8e49-a228d9fd4393`) lines 183-187 [crates/gcore/src/daemon_url.rs:183-187]
  - Signature: `fn env_override_ignores_unparseable_or_empty_port() {`
  - Purpose: It verifies that 'env_override' returns 'None' when the port override is empty, non-numeric, or out of the valid 'u16' port range. [crates/gcore/src/daemon_url.rs:183-187]
- `env_override_absent_returns_none` (function) component `env_override_absent_returns_none [function]` (`4c0aa8b1-cbbf-57e9-a614-b07e61161cd3`) lines 190-192 [crates/gcore/src/daemon_url.rs:190-192]
  - Signature: `fn env_override_absent_returns_none() {`
  - Purpose: It asserts that 'env_override(None, None)' returns 'None' when no environment override value is provided. [crates/gcore/src/daemon_url.rs:190-192]
- `daemon_url_honors_env_contract_over_bootstrap` (function) component `daemon_url_honors_env_contract_over_bootstrap [function]` (`22349b45-d22c-5dd3-b804-8ed299221aed`) lines 195-234 [crates/gcore/src/daemon_url.rs:195-234]
  - Signature: `fn daemon_url_honors_env_contract_over_bootstrap() {`
  - Purpose: Verifies that 'daemon_url()' resolves in priority order 'GOBBY_DAEMON_URL' override, then 'GOBBY_PORT', then 'bootstrap.yaml'’s 'daemon_port', and normalizes each into a 'http://127.0.0.1:<port>' URL unless an explicit URL override is set. [crates/gcore/src/daemon_url.rs:195-234]

