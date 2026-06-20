---
title: crates/gcode/src/db/resolution.rs
type: code_file
provenance:
- file: crates/gcode/src/db/resolution.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/db/resolution.rs

Module: [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Overview

`crates/gcode/src/db/resolution.rs` exposes 55 indexed API symbols.

## How it fits

`crates/gcode/src/db/resolution.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `BrokerDatabaseUrlResponse` | class | 'BrokerDatabaseUrlResponse' is a struct that encapsulates a single 'database_url' field of type 'String', representing a broker-provided database connection URL. [crates/gcode/src/db/resolution.rs:16-18] |
| `BootstrapDatabase` | class | 'BootstrapDatabase' is a struct containing a required 'hub_backend' string and an optional 'database_url' string used to configure database bootstrap settings. [crates/gcode/src/db/resolution.rs:21-24] |
| `gobby_home` | function | Returns the result of 'gobby_core::gobby_home()' as an 'anyhow::Result<PathBuf>', delegating all path resolution to the core implementation. [crates/gcode/src/db/resolution.rs:27-29] |
| `bootstrap_path` | function | Returns the 'gobby_home()' directory joined with 'bootstrap.yaml' as a 'PathBuf', propagating any error from 'gobby_home()'. [crates/gcode/src/db/resolution.rs:31-33] |
| `resolve_database_url` | function | Resolves and returns the database URL by loading the Gobby home directory, then delegating to a source-selection routine that combines brokered bootstrap lookup, environment variables, readonly Postgres connectivity checks, and Postgres hub identity probing. [crates/gcode/src/db/resolution.rs:39-48] |
| `resolve_database_url_from_sources_with_identity_and_reachability` | function | Resolves the PostgreSQL URL by preferring 'GCODE_DATABASE_URL' from the environment, then a Gcore config value, then a broker-provided URL or bootstrap YAML value potentially overridden by a recorded hub database URL if reachability and identity checks pass, and otherwise returns an error instructing setup/configuration. [crates/gcode/src/db/resolution.rs:83-138] |
| `resolve_recorded_hub_database_url` | function | Wraps 'gobby_core::provisioning::resolve_recorded_hub_database_url', passing the candidate URL as 'Some(candidate_database_url)' and mapping any successful resolution to 'resolution.database_url', so it returns 'Ok(Some(database_url))', 'Ok(None)', or an error. [crates/gcode/src/db/resolution.rs:140-156] |
| `resolve_database_url_from_bootstrap_file` | function | Returns 'Ok(None)' if the given path does not exist, otherwise reads the bootstrap file as UTF-8, parses it into a bootstrap database config, resolves the database URL from that config, and wraps the result in 'Some', propagating any read or parse errors with context. [crates/gcode/src/db/resolution.rs:158-166] |
| `resolve_database_url_from_gcore_config` | function | Reads the GCore standalone config from 'home/GCORE_CONFIG_FILENAME' and returns the trimmed non-empty value of 'databases.postgres.dsn' as 'Some(String)', or 'None' if the config file is missing or the field is absent/blank. [crates/gcode/src/db/resolution.rs:168-175] |
| `resolve_database_url_from_env` | function | Returns the first non-empty trimmed database URL found by querying 'GCODE_DATABASE_URL_ENV' and then 'GOBBY_POSTGRES_DSN_ENV' from the provided environment accessor, or 'None' if neither is set. [crates/gcode/src/db/resolution.rs:177-186] |
| `parse_bootstrap_database` | function | Parses a YAML bootstrap database config into 'BootstrapDatabase', requiring the top-level document to be a mapping, validating 'hub_backend' as a non-empty string and 'database_url' as an optional non-empty string, and returning contextual errors on parse or schema violations. [crates/gcode/src/db/resolution.rs:188-211] |
| `resolve_database_url_from_bootstrap` | function | Returns the bootstrap database URL only when 'hub_backend' is 'postgres', otherwise it fails with an error if the backend is different or 'database_url' is missing. [crates/gcode/src/db/resolution.rs:213-226] |
| `non_empty_trimmed` | function | Returns 'None' for 'None' or for strings that are empty after trimming whitespace, otherwise returns a new 'String' containing the trimmed value. [crates/gcode/src/db/resolution.rs:228-235] |
| `resolve_brokered_database_url_at` | function | Reads a local CLI token from 'gobby_home', derives the daemon URL from 'bootstrap_path', and returns the brokered database URL by requesting it from the daemon. [crates/gcode/src/db/resolution.rs:237-244] |
| `read_local_cli_token_at` | function | Reads the local CLI token file under 'gobby_home', trims surrounding whitespace, and returns an error if the file is missing or the resulting token is empty. [crates/gcode/src/db/resolution.rs:246-255] |
| `request_broker_database_url` | function | Validates the daemon URL as loopback, POSTs to '{daemon_url}/api/local/runtime/database-url' with the 'X-Gobby-Local-Token' header and a broker timeout, parses the JSON response into 'BrokerDatabaseUrlResponse', trims the returned 'database_url', and validates it before returning it. [crates/gcode/src/db/resolution.rs:257-280] |
| `broker_timeout` | function | Returns the broker timeout 'Duration' by delegating to 'broker_timeout_from_env' with a closure that looks up each requested variable via 'std::env::var(name).ok()'. [crates/gcode/src/db/resolution.rs:282-284] |
| `broker_timeout_from_env` | function | Reads 'GCODE_BROKER_TIMEOUT_MS_ENV' from the provided environment accessor and returns a positive millisecond 'Duration' parsed from its trimmed 'u64' value, otherwise logs a warning and falls back to 'DEFAULT_BROKER_TIMEOUT'. [crates/gcode/src/db/resolution.rs:286-300] |
| `validate_loopback_daemon_url` | function | Parses the daemon URL, requires a host and port (explicit or scheme-derived), resolves the host to socket addresses, and returns 'Ok(())' only if every resolved address is loopback, otherwise it errors. [crates/gcode/src/db/resolution.rs:302-323] |
| `validate_broker_database_url` | function | Validates that 'database_url' is non-empty, uses the 'postgres://' or 'postgresql://' scheme, contains an authority with a non-empty host and a database path, and returns the original URL as a 'String' or an error via 'bail!' otherwise. [crates/gcode/src/db/resolution.rs:325-353] |
| `bootstrap` | function | Constructs and returns a 'BootstrapDatabase' by cloning 'hub_backend' into a 'String' and converting the optional 'database_url' to an owned 'Option<String>'. [crates/gcode/src/db/resolution.rs:362-367] |
| `write_bootstrap` | function | Creates 'bootstrap.yaml' under 'home' containing 'hub_backend: postgres', the provided 'daemon_port', and 'bind_host: 127.0.0.1', writes it to disk, and returns the file path. [crates/gcode/src/db/resolution.rs:746-754] |
| `http_response` | function | Constructs and returns a complete HTTP/1.1 response string with the given status line, a JSON content type, a 'Content-Length' computed from 'body.len()', 'Connection: close', a blank line separator, and the provided body payload. [crates/gcode/src/db/resolution.rs:756-761] |
| `spawn_http_response` | function | Returns the input HTTP response string together with a 'JoinHandle' by delegating to 'spawn_http_response_after' with a zero 'Duration' delay. [crates/gcode/src/db/resolution.rs:763-765] |

_1 more symbol(s) not shown — run `gcode outline crates/gcode/src/db/resolution.rs` for the full list._

_Verified by 30 in-file unit tests._

