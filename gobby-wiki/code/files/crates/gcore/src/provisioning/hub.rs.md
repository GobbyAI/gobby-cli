---
title: crates/gcore/src/provisioning/hub.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/hub.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/hub.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/provisioning/hub.rs` exposes 26 indexed API symbols.

## How it fits

`crates/gcore/src/provisioning/hub.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `EnsureHubOptions` | class | Indexed class `EnsureHubOptions` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:4-9] |
| `EnsureHubOptions::new` | method | Indexed method `EnsureHubOptions::new` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:12-19] |
| `HubIdentity` | class | Indexed class `HubIdentity` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:23-26] |
| `HubIdentity::display_label` | method | Indexed method `HubIdentity::display_label` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:29-34] |
| `HubIdentityProbeResult` | type | Indexed type `HubIdentityProbeResult` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:38-41] |
| `RecordedHubIdentityStatus` | type | Indexed type `RecordedHubIdentityStatus` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:44-48] |
| `RecordedHubResolution` | class | Indexed class `RecordedHubResolution` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:51-54] |
| `ensure_hub` | function | Indexed function `ensure_hub` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:56-66] |
| `ensure_hub_with` | function | Indexed function `ensure_hub_with` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:69-87] |
| `ensure_hub_with_identity` | function | Indexed function `ensure_hub_with_identity` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:89-167] |
| `resolve_recorded_hub_database_url` | function | Indexed function `resolve_recorded_hub_database_url` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:169-279] |
| `redacted_postgres_dsn_placeholder` | function | Indexed function `redacted_postgres_dsn_placeholder` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:281-283] |
| `probe_postgres_hub_identity` | function | Indexed function `probe_postgres_hub_identity` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:286-337] |
| `insufficient_privilege` | function | Indexed function `insufficient_privilege` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:290-292] |
| `probe_postgres_hub_identity` | function | Indexed function `probe_postgres_hub_identity` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:340-344] |
| `HubDatabaseUrlSource` | type | Indexed type `HubDatabaseUrlSource` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:347-352] |
| `HubDatabaseUrl` | class | Indexed class `HubDatabaseUrl` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:355-358] |
| `resolve_hub_database_urls` | function | Indexed function `resolve_hub_database_urls` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:360-396] |
| `resolve_database_url_from_gcore_config` | function | Indexed function `resolve_database_url_from_gcore_config` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:398-408] |
| `HubBootstrap` | class | Indexed class `HubBootstrap` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:411-414] |
| `resolve_database_url_from_bootstrap_file` | function | Indexed function `resolve_database_url_from_bootstrap_file` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:416-428] |
| `non_empty_trimmed` | function | Indexed function `non_empty_trimmed` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:430-437] |
| `postgres_database_reachable` | function | Indexed function `postgres_database_reachable` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:440-442] |
| `postgres_database_reachable` | function | Indexed function `postgres_database_reachable` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:445-447] |
| `explicit_database_url_reachable` | function | Indexed function `explicit_database_url_reachable` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:450-455] |
| `explicit_database_url_reachable` | function | Indexed function `explicit_database_url_reachable` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:458-470] |

