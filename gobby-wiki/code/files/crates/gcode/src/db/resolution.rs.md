---
title: crates/gcode/src/db/resolution.rs
type: code_file
provenance:
- file: crates/gcode/src/db/resolution.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/db/resolution.rs

Module: [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Overview

## How it fits

The entry point of this resolution process is the resolve_database_url function crates/gcode/src/db/resolution.rs:39-48. This function begins by retrieving the Gobby home directory via gobby_home crates/gcode/src/db/resolution.rs:27-29, which delegates path resolution to the core Gobby implementation.
[crates/gcode/src/db/resolution.rs:16-18]
[crates/gcode/src/db/resolution.rs:21-24]
[crates/gcode/src/db/resolution.rs:27-29]
[crates/gcode/src/db/resolution.rs:31-33]
[crates/gcode/src/db/resolution.rs:39-48]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `BrokerDatabaseUrlResponse` | class | 'BrokerDatabaseUrlResponse' is a struct that encapsulates a single 'database_url' field of type 'String', representing a broker-provided database connection URL. [crates/gcode/src/db/resolution.rs:16-18] |
| `BootstrapDatabase` | class | 'BootstrapDatabase' is a struct containing a required 'hub_backend' string and an optional 'database_url' string used to configure database bootstrap settings. [crates/gcode/src/db/resolution.rs:21-24] |
| `gobby_home` | function | Returns the result of 'gobby_core::gobby_home()' as an 'anyhow::Result<PathBuf>', delegating all path resolution to the core implementation. [crates/gcode/src/db/resolution.rs:27-29] |
| `bootstrap_path` | function | Returns the 'gobby_home()' directory joined with 'bootstrap.yaml' as a 'PathBuf', propagating any error from 'gobby_home()'. [crates/gcode/src/db/resolution.rs:31-33] |
| `resolve_database_url` | function | Resolves and returns the database URL by loading the Gobby home directory, then delegating to a source-selection routine that combines brokered bootstrap lookup, environment variables, readonly Postgres connectivity checks, and Postgres hub identity probing. [crates/gcode/src/db/resolution.rs:39-48] |
| `resolve_database_url_from_sources` | function | Delegates database URL resolution to 'resolve_database_url_from_sources_with_identity_and_reachability', using 'probe_postgres_hub_identity' as the identity probe while passing through the home path, broker resolver, environment-variable accessor, and database reachability check. [crates/gcode/src/db/resolution.rs:51-64] |
| `resolve_database_url_from_sources_with_identity` | function | A thin wrapper that forwards its arguments to 'resolve_database_url_from_sources_with_identity_and_reachability' and returns the resulting 'anyhow::Result<String>'. [crates/gcode/src/db/resolution.rs:67-81] |
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
| `database_url_env_prefers_gcode_specific_var` | function | Verifies that 'resolve_database_url_from_env' selects 'GCODE_DATABASE_URL_ENV' over 'GOBBY_POSTGRES_DSN_ENV' when both are present and trims surrounding whitespace from the chosen URL. [crates/gcode/src/db/resolution.rs:370-378] |
| `database_url_env_falls_back_to_gobby_postgres_dsn` | function | Verifies that 'resolve_database_url_from_env' trims and returns the 'GOBBY_POSTGRES_DSN_ENV' value when it is the only database URL environment variable present, yielding 'Some("postgresql://gobby/db")'. [crates/gcode/src/db/resolution.rs:381-388] |
| `database_url_env_ignores_empty_values` | function | Verifies that 'resolve_database_url_from_env' treats whitespace-only values in both 'GCODE_DATABASE_URL_ENV' and 'GOBBY_POSTGRES_DSN_ENV' as empty and returns 'None'. [crates/gcode/src/db/resolution.rs:391-399] |
| `database_url_sources_prefer_env_over_daemon_broker` | function | Verifies that 'resolve_database_url_from_sources' prefers the 'GCODE_DATABASE_URL_ENV' environment value ('postgresql://env/db') over the daemon broker-provided database URL when both are available. [crates/gcode/src/db/resolution.rs:402-417] |
| `database_url_sources_use_daemon_broker_after_env` | function | Verifies that 'resolve_database_url_from_sources' returns the daemon broker database URL ('postgresql://broker/db') when the broker source is available, even if the environment source is present. [crates/gcode/src/db/resolution.rs:420-432] |
| `database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable` | function | Verifies that 'resolve_database_url_from_sources' returns the inline 'database_url' from 'bootstrap.yaml' when the daemon lookup fails, yielding 'postgresql://inline/db'. [crates/gcode/src/db/resolution.rs:435-452] |
| `database_url_sources_use_gcore_after_daemon_and_bootstrap` | function | Verifies that 'resolve_database_url_from_sources' falls back to the Gcore config file in the home directory and returns its Postgres DSN when daemon lookup fails, bootstrap data is absent, and the bootstrap flag is enabled. [crates/gcode/src/db/resolution.rs:455-472] |
| `adopted_hub_resolves_without_conflict` | function | Verifies that 'resolve_database_url_from_sources_with_identity' returns the configured adopted PostgreSQL DSN unchanged when the hub identity is known and matches the target database without conflict. [crates/gcode/src/db/resolution.rs:475-500] |
| `postgres_bootstrap_accepts_inline_url` | function | Verifies that 'resolve_database_url_from_bootstrap' returns the inline PostgreSQL URL unchanged when the bootstrap is constructed with 'Some("postgresql://inline/db")'. [crates/gcode/src/db/resolution.rs:503-511] |
| `non_postgres_bootstrap_fails_clearly` | function | Asserts that resolving a database URL from bootstrap configuration fails for a non-Postgres backend and that the resulting error message explicitly mentions the required 'hub_backend: postgres' and the offending 'local-file' backend. [crates/gcode/src/db/resolution.rs:514-521] |
| `missing_hub_backend_fails_clearly` | function | Verifies that 'parse_bootstrap_database' returns an error when 'hub_backend' is omitted from a PostgreSQL bootstrap config, and that the error message explicitly mentions 'hub_backend: postgres'. [crates/gcode/src/db/resolution.rs:524-529] |
| `missing_postgres_dsn_fails_clearly` | function | Verifies that resolving a Postgres bootstrap configuration without a DSN returns an error whose message clearly mentions 'database_url'. [crates/gcode/src/db/resolution.rs:532-537] |
| `parse_bootstrap_database_reads_postgres_fields` | function | Verifies that 'parse_bootstrap_database' correctly parses 'hub_backend' as '"postgres"' and 'database_url' as 'Some("postgresql://inline/db")' from a bootstrap database configuration string. [crates/gcode/src/db/resolution.rs:540-552] |
| `broker_request_returns_database_url_and_sends_local_token` | function | Verifies that 'request_broker_database_url' returns the 'database_url' from a successful broker response and sends the local token in the 'X-Gobby-Local-Token' HTTP header on the POST request to '/api/local/runtime/database-url'. [crates/gcode/src/db/resolution.rs:555-572] |
| `broker_request_rejects_non_loopback_daemon_url_before_sending_local_token` | function | Verifies that 'request_broker_database_url' rejects a non-loopback daemon URL and returns an error containing 'must resolve only to loopback addresses' without succeeding with the provided local token. [crates/gcode/src/db/resolution.rs:575-583] |
| `broker_request_allows_cold_daemon_latency` | function | Verifies that 'request_broker_database_url' successfully resolves the broker’s database URL even when the HTTP response is delayed by 1100 ms, tolerating cold-daemon latency. [crates/gcode/src/db/resolution.rs:586-597] |
| `broker_timeout_defaults_to_seven_seconds` | function | Verifies that 'broker_timeout_from_env' returns a default timeout of 'Duration::from_millis(7000)' when the environment lookup yields no value. [crates/gcode/src/db/resolution.rs:600-604] |
| `broker_timeout_reads_positive_env_value` | function | Verifies that 'broker_timeout_from_env' parses a positive 'GCODE_BROKER_TIMEOUT_MS_ENV' value of '"1250"' and returns 'Duration::from_millis(1250)'. [crates/gcode/src/db/resolution.rs:607-613] |
| `broker_timeout_ignores_invalid_env_value` | function | Verifies that 'broker_timeout_from_env' treats the invalid 'GCODE_BROKER_TIMEOUT_MS_ENV' value '"0"' as unusable and returns 'DEFAULT_BROKER_TIMEOUT' instead. [crates/gcode/src/db/resolution.rs:616-622] |
| `broker_missing_token_fails` | function | Verifies that 'resolve_brokered_database_url_at' returns an error containing 'missing local CLI token' when the bootstrap exists but the local CLI token is absent. [crates/gcode/src/db/resolution.rs:625-633] |
| `broker_daemon_down_fails` | function | Creates a temporary home with a CLI token and bootstrap file, then verifies that 'resolve_brokered_database_url_at' returns an error containing 'database_url broker request failed' when the broker daemon is unavailable. [crates/gcode/src/db/resolution.rs:636-648] |
| `broker_auth_failure_fails` | function | Verifies that a broker database URL request with an invalid token returns an error, consumes the spawned HTTP request, and reports a 'database_url broker request failed' message. [crates/gcode/src/db/resolution.rs:651-665] |
| `broker_non_success_status_fails` | function | Verifies that 'request_broker_database_url' returns an error, rather than a successful result, when the broker responds with a non-2xx HTTP status ('503 Service Unavailable'), and that the error message includes 'database_url broker request failed'. [crates/gcode/src/db/resolution.rs:668-682] |
| `broker_invalid_json_fails` | function | Verifies that 'request_broker_database_url' returns an error and reports an invalid-JSON message when the broker responds with '200 OK' and a non-JSON body. [crates/gcode/src/db/resolution.rs:685-696] |
| `broker_empty_database_url_fails` | function | Verifies that 'request_broker_database_url' returns an error when the broker response contains a blank 'database_url' field, and that the error message includes 'database_url broker response was empty'. [crates/gcode/src/db/resolution.rs:699-711] |
| `broker_invalid_database_url_scheme_fails` | function | Verifies that 'validate_broker_database_url' rejects a broker database URL using a non-Postgres scheme ('http://') and returns an error mentioning that only 'postgres://' or 'postgresql://' are allowed. [crates/gcode/src/db/resolution.rs:714-722] |
| `broker_missing_database_url_host_fails` | function | Verifies that 'validate_broker_database_url("postgresql:///db")' returns an error when the URL omits a host, and that the error message states the broker response must include a host. [crates/gcode/src/db/resolution.rs:725-733] |
| `broker_missing_database_url_path_fails` | function | Verifies that 'validate_broker_database_url("postgresql://broker/")' returns an error when the broker database URL lacks a path, and that the error message states a database path is required. [crates/gcode/src/db/resolution.rs:736-744] |
| `write_bootstrap` | function | Creates 'bootstrap.yaml' under 'home' containing 'hub_backend: postgres', the provided 'daemon_port', and 'bind_host: 127.0.0.1', writes it to disk, and returns the file path. [crates/gcode/src/db/resolution.rs:746-754] |
| `http_response` | function | Constructs and returns a complete HTTP/1.1 response string with the given status line, a JSON content type, a 'Content-Length' computed from 'body.len()', 'Connection: close', a blank line separator, and the provided body payload. [crates/gcode/src/db/resolution.rs:756-761] |
| `spawn_http_response` | function | Returns the input HTTP response string together with a 'JoinHandle' by delegating to 'spawn_http_response_after' with a zero 'Duration' delay. [crates/gcode/src/db/resolution.rs:763-765] |
| `spawn_http_response_after` | function | Starts a loopback 'TcpListener' on an ephemeral port, spawns a thread that accepts one HTTP request, reads until the headers terminator '\r\n\r\n', sleeps for the specified 'delay', writes the provided response bytes, and returns the server URL plus a 'JoinHandle' that yields the captured request as a UTF-8 string. [crates/gcode/src/db/resolution.rs:767-794] |

