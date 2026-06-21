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

`crates/gcore/src/provisioning/hub.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `EnsureHubOptions` | class | 'EnsureHubOptions' is a configuration struct that bundles parameters for hub initialization, comprising a filesystem path, Docker service options, candidate database URLs, and a provisioning flag. [crates/gcore/src/provisioning/hub.rs:4-9] |
| `EnsureHubOptions::new` | method | Constructs a new instance initialized with Docker service options derived from the provided gobby_home path, an empty candidate database URLs vector, and service provisioning enabled. [crates/gcore/src/provisioning/hub.rs:12-19] |
| `HubIdentity` | class | HubIdentity is a public struct that encapsulates a system identifier and database name as String fields for representing the identity of a hub. [crates/gcore/src/provisioning/hub.rs:23-26] |
| `HubIdentity::display_label` | method | Returns a formatted string containing the instance's system identifier and database name in the format "system_identifier={}, database={}". [crates/gcore/src/provisioning/hub.rs:29-34] |
| `HubIdentityProbeResult` | type | Indexed type `HubIdentityProbeResult` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:38-41] |
| `RecordedHubIdentityStatus` | type | Indexed type `RecordedHubIdentityStatus` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:44-48] |
| `RecordedHubResolution` | class | RecordedHubResolution is a struct that pairs a database URL string with a RecordedHubIdentityStatus to represent a resolved hub configuration. [crates/gcore/src/provisioning/hub.rs:51-54] |
| `ensure_hub` | function | Ensures hub provisioning by validating PostgreSQL database connectivity and identity while provisioning Docker services, returning a hub identifier and optional provisioning report. [crates/gcore/src/provisioning/hub.rs:56-66] |
| `ensure_hub_with_identity` | function | # Summary Ensures a hub's identity by resolving candidate database URLs from multiple sources (environment, Gcore config, bootstrap), validating their reachability and identity via probing, and returning the selected database URL alongside an optional Docker provisioning report. [crates/gcore/src/provisioning/hub.rs:89-167] |
| `resolve_recorded_hub_database_url` | function | Resolves a recorded hub database URL by selecting between existing and daemon candidates based on reachability verification and identity consistency status. [crates/gcore/src/provisioning/hub.rs:169-279] |
| `redacted_postgres_dsn_placeholder` | function | This function generates a redacted PostgreSQL DSN placeholder string by formatting the input source parameter as '<redacted-{source}-postgres-dsn>'. [crates/gcore/src/provisioning/hub.rs:281-283] |
| `probe_postgres_hub_identity` | function | This function probes a PostgreSQL database to retrieve its hub identity by validating the current user has execution privilege for 'pg_control_system()' and querying it to obtain the system identifier and current database name, returning either the identity result or an insufficient privilege error. [crates/gcore/src/provisioning/hub.rs:286-337] |
| `insufficient_privilege` | function | This function returns a boolean indicating whether the provided PostgreSQL error's SQL state code matches 'INSUFFICIENT_PRIVILEGE'. [crates/gcore/src/provisioning/hub.rs:290-292] |
| `probe_postgres_hub_identity` | function | This function unconditionally returns an 'UnknownInsufficientPrivilege' result, indicating that PostgreSQL hub identity probing is unavailable because gobby-core was compiled without PostgreSQL support. [crates/gcore/src/provisioning/hub.rs:340-344] |
| `HubDatabaseUrlSource` | type | Indexed type `HubDatabaseUrlSource` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:347-352] |
| `HubDatabaseUrl` | class | HubDatabaseUrl is a struct that pairs a database URL string with a HubDatabaseUrlSource type to track the origin of the database connection URL. [crates/gcore/src/provisioning/hub.rs:355-358] |
| `resolve_hub_database_urls` | function | Aggregates PostgreSQL database URLs from multiple sources (candidate options, GOBBY_POSTGRES_DSN environment variable, gcore configuration, and bootstrap.yaml) and returns them as a vector with source attribution. [crates/gcore/src/provisioning/hub.rs:360-396] |
| `resolve_database_url_from_gcore_config` | function | # Summary This function retrieves a non-empty PostgreSQL DSN string from a gcore standalone configuration file at the specified home path, returning 'None' if required directories, files, or configuration values are absent. [crates/gcore/src/provisioning/hub.rs:398-408] |
| `HubBootstrap` | class | HubBootstrap is a configuration struct containing two optional String fields for specifying the hub backend service endpoint and database connection URL. [crates/gcore/src/provisioning/hub.rs:411-414] |
| `resolve_database_url_from_bootstrap_file` | function | Parses a YAML bootstrap file and returns a non-empty trimmed database URL if the hub backend is configured as 'postgres', or None if the file is absent or uses a non-PostgreSQL backend. [crates/gcore/src/provisioning/hub.rs:416-428] |
| `non_empty_trimmed` | function | Transforms an 'Option<String>' by trimming whitespace and returning 'Some' of the trimmed string if non-empty, or 'None' otherwise. [crates/gcore/src/provisioning/hub.rs:430-437] |
| `postgres_database_reachable` | function | This function returns 'true' if a read-only connection to the PostgreSQL database at the provided URL can be successfully established, 'false' otherwise. [crates/gcore/src/provisioning/hub.rs:440-442] |
| `postgres_database_reachable` | function | This function accepts a PostgreSQL database URL string and unconditionally returns 'false', serving as a stub implementation for checking database reachability. [crates/gcore/src/provisioning/hub.rs:445-447] |
| `explicit_database_url_reachable` | function | This function invokes a provided mutable closure with a database URL string and returns its boolean reachability result. [crates/gcore/src/provisioning/hub.rs:450-455] |

_1 more symbol(s) not shown — run `gcode outline crates/gcore/src/provisioning/hub.rs` for the full list._

_Verified by 1 in-file unit test._

