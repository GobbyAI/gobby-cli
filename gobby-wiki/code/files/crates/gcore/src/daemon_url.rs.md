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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/daemon_url.rs:28-34](crates/gcore/src/daemon_url.rs#L28-L34), [crates/gcore/src/daemon_url.rs:40-42](crates/gcore/src/daemon_url.rs#L40-L42), [crates/gcore/src/daemon_url.rs:47-59](crates/gcore/src/daemon_url.rs#L47-L59), [crates/gcore/src/daemon_url.rs:61-64](crates/gcore/src/daemon_url.rs#L61-L64), [crates/gcore/src/daemon_url.rs:72-78](crates/gcore/src/daemon_url.rs#L72-L78), [crates/gcore/src/daemon_url.rs:86-91](crates/gcore/src/daemon_url.rs#L86-L91), [crates/gcore/src/daemon_url.rs:94-98](crates/gcore/src/daemon_url.rs#L94-L98), [crates/gcore/src/daemon_url.rs:101-104](crates/gcore/src/daemon_url.rs#L101-L104), [crates/gcore/src/daemon_url.rs:107-114](crates/gcore/src/daemon_url.rs#L107-L114), [crates/gcore/src/daemon_url.rs:117-124](crates/gcore/src/daemon_url.rs#L117-L124), [crates/gcore/src/daemon_url.rs:127-130](crates/gcore/src/daemon_url.rs#L127-L130), [crates/gcore/src/daemon_url.rs:133-136](crates/gcore/src/daemon_url.rs#L133-L136), [crates/gcore/src/daemon_url.rs:139-146](crates/gcore/src/daemon_url.rs#L139-L146), [crates/gcore/src/daemon_url.rs:149-156](crates/gcore/src/daemon_url.rs#L149-L156), [crates/gcore/src/daemon_url.rs:159-164](crates/gcore/src/daemon_url.rs#L159-L164), [crates/gcore/src/daemon_url.rs:167-172](crates/gcore/src/daemon_url.rs#L167-L172), [crates/gcore/src/daemon_url.rs:175-180](crates/gcore/src/daemon_url.rs#L175-L180), [crates/gcore/src/daemon_url.rs:183-187](crates/gcore/src/daemon_url.rs#L183-L187), [crates/gcore/src/daemon_url.rs:190-192](crates/gcore/src/daemon_url.rs#L190-L192), [crates/gcore/src/daemon_url.rs:195-234](crates/gcore/src/daemon_url.rs#L195-L234)

</details>

# crates/gcore/src/daemon_url.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file centralizes daemon dial-URL resolution for Gobby binaries. `daemon_url` and `daemon_url_at` produce the final URL from either environment overrides or a specific `bootstrap.yaml` endpoint, while `env_override` enforces the override precedence (`GOBBY_DAEMON_URL` first, then `GOBBY_PORT`, otherwise bootstrap). The remaining helpers convert a `DaemonEndpoint` into a URL, normalize wildcard listen addresses to loopback for dialing, and trim or reject invalid override values; the tests cover these cases and verify the contract end to end.
[crates/gcore/src/daemon_url.rs:28-34]
[crates/gcore/src/daemon_url.rs:40-42]
[crates/gcore/src/daemon_url.rs:47-59]
[crates/gcore/src/daemon_url.rs:61-64]
[crates/gcore/src/daemon_url.rs:72-78]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `daemon_url` | function | `pub fn daemon_url() -> String {` | `daemon_url [function]` | `326f3e81-0586-5929-9847-dea92091ab82` | 28-34 [crates/gcore/src/daemon_url.rs:28-34] | Indexed function `daemon_url` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:28-34] |
| `daemon_url_at` | function | `pub fn daemon_url_at(path: &Path) -> String {` | `daemon_url_at [function]` | `cfcb2d54-4c9f-567e-837e-c03378a2f53d` | 40-42 [crates/gcore/src/daemon_url.rs:40-42] | Indexed function `daemon_url_at` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:40-42] |
| `env_override` | function | `fn env_override(url: Option<&str>, port: Option<&str>) -> Option<String> {` | `env_override [function]` | `4ace3e35-0f9e-51b8-8d62-264fbaac264d` | 47-59 [crates/gcore/src/daemon_url.rs:47-59] | Indexed function `env_override` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:47-59] |
| `endpoint_to_url` | function | `fn endpoint_to_url(endpoint: &DaemonEndpoint) -> String {` | `endpoint_to_url [function]` | `121a4f74-0310-5cc0-9249-4d77f94eca97` | 61-64 [crates/gcore/src/daemon_url.rs:61-64] | Indexed function `endpoint_to_url` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:61-64] |
| `dial_host` | function | `fn dial_host(host: &str) -> Cow<'_, str> {` | `dial_host [function]` | `e6102bbd-d2ea-59e7-8b82-2b6273b47e29` | 72-78 [crates/gcore/src/daemon_url.rs:72-78] | Indexed function `dial_host` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:72-78] |
| `write_bootstrap` | function | `fn write_bootstrap(contents: &str) -> (tempfile::TempDir, std::path::PathBuf) {` | `write_bootstrap [function]` | `36ad539e-894c-5ed2-939b-1c78d64c3302` | 86-91 [crates/gcore/src/daemon_url.rs:86-91] | Indexed function `write_bootstrap` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:86-91] |
| `default_url_when_file_missing` | function | `fn default_url_when_file_missing() {` | `default_url_when_file_missing [function]` | `852e94ac-199c-5a57-a199-c97c9d5865f4` | 94-98 [crates/gcore/src/daemon_url.rs:94-98] | Indexed function `default_url_when_file_missing` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:94-98] |
| `wildcard_ipv4_normalizes_to_loopback` | function | `fn wildcard_ipv4_normalizes_to_loopback() {` | `wildcard_ipv4_normalizes_to_loopback [function]` | `2dfaca7b-c395-5429-9c23-f68a9bc89d7f` | 101-104 [crates/gcore/src/daemon_url.rs:101-104] | Indexed function `wildcard_ipv4_normalizes_to_loopback` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:101-104] |
| `wildcard_ipv6_normalizes_to_loopback` | function | `fn wildcard_ipv6_normalizes_to_loopback() {` | `wildcard_ipv6_normalizes_to_loopback [function]` | `9b0f11b9-b1d9-5abc-b3e0-f7c906b13ef7` | 107-114 [crates/gcore/src/daemon_url.rs:107-114] | Indexed function `wildcard_ipv6_normalizes_to_loopback` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:107-114] |
| `wildcard_ipv6_zero_normalizes_to_loopback` | function | `fn wildcard_ipv6_zero_normalizes_to_loopback() {` | `wildcard_ipv6_zero_normalizes_to_loopback [function]` | `f319eed9-b5ef-512f-a08d-0beace3700db` | 117-124 [crates/gcore/src/daemon_url.rs:117-124] | Indexed function `wildcard_ipv6_zero_normalizes_to_loopback` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:117-124] |
| `localhost_passes_through` | function | `fn localhost_passes_through() {` | `localhost_passes_through [function]` | `e1dee3b2-12bd-5639-980f-5619a68bbc06` | 127-130 [crates/gcore/src/daemon_url.rs:127-130] | Indexed function `localhost_passes_through` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:127-130] |
| `custom_port_and_host_compose` | function | `fn custom_port_and_host_compose() {` | `custom_port_and_host_compose [function]` | `1e3f7ed5-12fb-507b-b07a-4517266efa47` | 133-136 [crates/gcore/src/daemon_url.rs:133-136] | Indexed function `custom_port_and_host_compose` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:133-136] |
| `bare_ipv6_literal_is_bracketed` | function | `fn bare_ipv6_literal_is_bracketed() {` | `bare_ipv6_literal_is_bracketed [function]` | `a116da61-3342-523d-ad1c-e4a7627ac8f5` | 139-146 [crates/gcore/src/daemon_url.rs:139-146] | Indexed function `bare_ipv6_literal_is_bracketed` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:139-146] |
| `bracketed_ipv6_literal_passes_through` | function | `fn bracketed_ipv6_literal_passes_through() {` | `bracketed_ipv6_literal_passes_through [function]` | `d54a7599-b7c1-5a37-8535-f76fbe9f75e1` | 149-156 [crates/gcore/src/daemon_url.rs:149-156] | Indexed function `bracketed_ipv6_literal_passes_through` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:149-156] |
| `env_override_url_beats_port` | function | `fn env_override_url_beats_port() {` | `env_override_url_beats_port [function]` | `d081cffc-518e-5684-ab97-23ebb4152bee` | 159-164 [crates/gcore/src/daemon_url.rs:159-164] | Indexed function `env_override_url_beats_port` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:159-164] |
| `env_override_url_trims_trailing_slashes` | function | `fn env_override_url_trims_trailing_slashes() {` | `env_override_url_trims_trailing_slashes [function]` | `fd901039-e803-5509-9664-2392f6c61fbf` | 167-172 [crates/gcore/src/daemon_url.rs:167-172] | Indexed function `env_override_url_trims_trailing_slashes` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:167-172] |
| `env_override_empty_url_falls_back_to_port` | function | `fn env_override_empty_url_falls_back_to_port() {` | `env_override_empty_url_falls_back_to_port [function]` | `421354aa-d3e4-5ebf-a8e7-e836d53d7653` | 175-180 [crates/gcore/src/daemon_url.rs:175-180] | Indexed function `env_override_empty_url_falls_back_to_port` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:175-180] |
| `env_override_ignores_unparseable_or_empty_port` | function | `fn env_override_ignores_unparseable_or_empty_port() {` | `env_override_ignores_unparseable_or_empty_port [function]` | `faad7146-3356-5d8c-8e49-a228d9fd4393` | 183-187 [crates/gcore/src/daemon_url.rs:183-187] | Indexed function `env_override_ignores_unparseable_or_empty_port` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:183-187] |
| `env_override_absent_returns_none` | function | `fn env_override_absent_returns_none() {` | `env_override_absent_returns_none [function]` | `4c0aa8b1-cbbf-57e9-a614-b07e61161cd3` | 190-192 [crates/gcore/src/daemon_url.rs:190-192] | Indexed function `env_override_absent_returns_none` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:190-192] |
| `daemon_url_honors_env_contract_over_bootstrap` | function | `fn daemon_url_honors_env_contract_over_bootstrap() {` | `daemon_url_honors_env_contract_over_bootstrap [function]` | `22349b45-d22c-5dd3-b804-8ed299221aed` | 195-234 [crates/gcore/src/daemon_url.rs:195-234] | Indexed function `daemon_url_honors_env_contract_over_bootstrap` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:195-234] |
