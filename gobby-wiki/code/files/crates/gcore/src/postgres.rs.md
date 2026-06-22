---
title: crates/gcore/src/postgres.rs
type: code_file
provenance:
- file: crates/gcore/src/postgres.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/postgres.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/postgres.rs` exposes 32 indexed API symbols.

## How it fits

`crates/gcore/src/postgres.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `connect_readonly` | function | Establishes a PostgreSQL database client connection and configures it for read-only mode by executing 'SET default_transaction_read_only = on'. [crates/gcore/src/postgres.rs:16-22] |
| `connect_readwrite` | function | Establishes a database connection by delegating to the 'connect()' function with the provided database URL, returning an 'anyhow::Result<Client>'. [crates/gcore/src/postgres.rs:25-27] |
| `read_config_value` | function | Executes a parameterized SQL query to retrieve an optional string value from a config_store table by key, with error context propagation. [crates/gcore/src/postgres.rs:36-45] |
| `SchemaCheck` | class | SchemaCheck is a struct that encapsulates the result of a database schema validation check, containing the object name, check type, pass/fail status, and optional failure details. [crates/gcore/src/postgres.rs:49-58] |
| `validate_schema` | function | Executes a single-use validator closure against a mutable database client connection to perform schema validation, delegating to 'run_schema_validator' and returning a vector of schema checks. [crates/gcore/src/postgres.rs:66-71] |
| `connect` | function | Establishes a PostgreSQL client connection by parsing the provided database URL, extracting the requested SSL mode, and applying the appropriate TLS configuration (none, prefer, require, verify-ca, or verify-full) before returning a connected 'Client' instance. [crates/gcore/src/postgres.rs:73-101] |
| `RequestedSslMode` | type | Indexed type `RequestedSslMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:104-110] |
| `requested_ssl_mode_from_config` | function | Maps the SSL mode from a PostgreSQL configuration object to a 'RequestedSslMode' enum, defaulting to 'Prefer' for unhandled 'SslMode' variants. [crates/gcore/src/postgres.rs:112-119] |
| `requested_ssl_mode` | function | Parses the 'sslmode' query parameter from a PostgreSQL database URL string and maps it to a corresponding 'RequestedSslMode' enum variant, returning 'None' for unrecognized values. [crates/gcore/src/postgres.rs:121-134] |
| `sslmode_value` | function | Extracts and normalizes the 'sslmode' parameter value from a PostgreSQL database URL by first parsing the query string, then falling back to DSN keyword format if not found. [crates/gcore/src/postgres.rs:136-150] |
| `normalize_sslmode_for_parser` | function | Normalizes the sslmode parameter in a database URL by parsing it as either a URL query string or libpq keyword DSN format, applying normalization to each parameter pair, and returning the reformatted connection string. [crates/gcore/src/postgres.rs:152-167] |
| `normalize_sslmode_pair` | function | Normalizes an sslmode connection parameter by remapping verify-ca and verify-full modes to require while passing through unmodified pairs. [crates/gcore/src/postgres.rs:169-182] |
| `normalize_sslmode_token` | function | This function normalizes an SSL mode token string by removing surrounding single and double quote characters and converting the result to ASCII lowercase. [crates/gcore/src/postgres.rs:184-189] |
| `connect_with_tls_unverified` | function | Establishes a TLS connection to PostgreSQL with certificate verification disabled, returning a 'Result<Client>'. [crates/gcore/src/postgres.rs:191-193] |
| `connect_with_tls_verify_ca` | function | Establishes a PostgreSQL client connection with TLS encryption configured to verify the server certificate against a trusted certificate authority. [crates/gcore/src/postgres.rs:195-197] |
| `connect_with_tls_verification` | function | Establishes a PostgreSQL client connection with TLS certificate verification conditionally set to VerifyFull or Unverified based on the boolean 'verify' parameter. [crates/gcore/src/postgres.rs:199-209] |
| `connect_with_tls` | function | Establishes a TLS-secured PostgreSQL client connection using the provided configuration and connector mode, returning a 'Client' or an error with contextual messaging. [crates/gcore/src/postgres.rs:211-216] |
| `TlsConnectorMode` | type | Indexed type `TlsConnectorMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:219-223] |
| `TlsConnectorMode::verify_mode` | method | This method converts the enum variant to its corresponding 'SslVerifyMode', mapping 'Unverified' to 'NONE' and both 'VerifyCa' and 'VerifyFull' to 'PEER'. [crates/gcore/src/postgres.rs:226-231] |
| `TlsConnectorMode::uses_default_verify_paths` | method | This method returns 'true' if the instance is a 'VerifyCa' or 'VerifyFull' variant, otherwise 'false'. [crates/gcore/src/postgres.rs:233-235] |
| `TlsConnectorMode::disables_hostname_verification` | method | Returns 'true' if the enum variant is 'VerifyCa', indicating that hostname verification is disabled in this configuration. [crates/gcore/src/postgres.rs:237-239] |
| `TlsConnectorBuilder` | class | 'TlsConnectorBuilder' is a wrapper struct that encapsulates an 'SslConnectorBuilder' with a boolean flag to disable hostname verification and a test-only 'SslVerifyMode' field for SSL/TLS connection configuration. [crates/gcore/src/postgres.rs:242-247] |
| `tls_connector` | function | Creates a TLS connector from the specified mode with an optional callback to disable hostname verification if the builder configuration indicates it should be disabled. [crates/gcore/src/postgres.rs:249-260] |
| `tls_connector_builder` | function | Configures and returns a 'TlsConnectorBuilder' by initializing an OpenSSL TLS connector with certificate verification settings (paths and mode) determined by the input 'TlsConnectorMode'. [crates/gcore/src/postgres.rs:262-278] |

_1 more symbol(s) not shown — run `gcode outline crates/gcore/src/postgres.rs` for the full list._

_Verified by 7 in-file unit tests._

