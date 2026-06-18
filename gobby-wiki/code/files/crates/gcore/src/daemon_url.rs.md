---
title: crates/gcore/src/daemon_url.rs
type: code_file
provenance:
- file: crates/gcore/src/daemon_url.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/daemon_url.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/daemon_url.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gcore/src/daemon_url.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `daemon_url` | function | Indexed function `daemon_url` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:28-34] |
| `daemon_url_at` | function | Indexed function `daemon_url_at` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:40-42] |
| `env_override` | function | Indexed function `env_override` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:47-59] |
| `endpoint_to_url` | function | Indexed function `endpoint_to_url` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:61-64] |
| `dial_host` | function | Indexed function `dial_host` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:72-78] |
| `write_bootstrap` | function | Indexed function `write_bootstrap` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:86-91] |
| `default_url_when_file_missing` | function | Indexed function `default_url_when_file_missing` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:94-98] |
| `wildcard_ipv4_normalizes_to_loopback` | function | Indexed function `wildcard_ipv4_normalizes_to_loopback` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:101-104] |
| `wildcard_ipv6_normalizes_to_loopback` | function | Indexed function `wildcard_ipv6_normalizes_to_loopback` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:107-114] |
| `wildcard_ipv6_zero_normalizes_to_loopback` | function | Indexed function `wildcard_ipv6_zero_normalizes_to_loopback` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:117-124] |
| `localhost_passes_through` | function | Indexed function `localhost_passes_through` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:127-130] |
| `custom_port_and_host_compose` | function | Indexed function `custom_port_and_host_compose` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:133-136] |
| `bare_ipv6_literal_is_bracketed` | function | Indexed function `bare_ipv6_literal_is_bracketed` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:139-146] |
| `bracketed_ipv6_literal_passes_through` | function | Indexed function `bracketed_ipv6_literal_passes_through` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:149-156] |
| `env_override_url_beats_port` | function | Indexed function `env_override_url_beats_port` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:159-164] |
| `env_override_url_trims_trailing_slashes` | function | Indexed function `env_override_url_trims_trailing_slashes` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:167-172] |
| `env_override_empty_url_falls_back_to_port` | function | Indexed function `env_override_empty_url_falls_back_to_port` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:175-180] |
| `env_override_ignores_unparseable_or_empty_port` | function | Indexed function `env_override_ignores_unparseable_or_empty_port` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:183-187] |
| `env_override_absent_returns_none` | function | Indexed function `env_override_absent_returns_none` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:190-192] |
| `daemon_url_honors_env_contract_over_bootstrap` | function | Indexed function `daemon_url_honors_env_contract_over_bootstrap` in `crates/gcore/src/daemon_url.rs`. [crates/gcore/src/daemon_url.rs:195-234] |

