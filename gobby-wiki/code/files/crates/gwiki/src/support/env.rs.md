---
title: crates/gwiki/src/support/env.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/env.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/env.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/env.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gwiki/src/support/env.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `HubBootstrap` | class | 'HubBootstrap' is a configuration struct containing optional 'hub_backend' and 'database_url' string fields used to bootstrap hub initialization. [crates/gwiki/src/support/env.rs:21-24] |
| `ValidatedDaemonUrl` | class | A 'ValidatedDaemonUrl' is a data container that stores a validated daemon request base URL and its corresponding host header as strings. [crates/gwiki/src/support/env.rs:27-30] |
| `database_url` | function | Returns the database URL as 'Some(String)' by first checking the environment, then attempting brokered resolution from 'gobby_home()/bootstrap.yaml', then a bootstrap file fallback, and finally the gcore config, propagating errors as 'anyhow::Result<Option<String>>'. [crates/gwiki/src/support/env.rs:32-49] |
| `database_url_for` | function | Returns the optional PostgreSQL database URL from 'database_url()', converting any resolution error into 'WikiError::Config' with a command-specific failure message. [crates/gwiki/src/support/env.rs:51-55] |
| `database_url_from_env` | function | Returns the first non-empty, trimmed environment variable value found among 'GWIKI_DATABASE_URL_ENV' and 'GOBBY_POSTGRES_DSN_ENV', or 'None' if neither is set to a non-blank string. [crates/gwiki/src/support/env.rs:57-66] |
| `resolve_database_url_from_gcore_config` | function | Reads the Gcore standalone config at 'home', returns 'Ok(None)' if the config is absent, otherwise extracts 'databases.postgres.dsn' and returns it as 'Some(String)' only if it is non-empty after trimming whitespace. [crates/gwiki/src/support/env.rs:68-75] |
| `resolve_database_url_from_bootstrap_file` | function | Returns 'Ok(None)' if the bootstrap file is missing or specifies a non-'postgres' 'hub_backend', otherwise reads and YAML-parses the file and returns the trimmed, non-empty 'database_url' field as 'Ok(Some(String))' or propagates read/parse errors. [crates/gwiki/src/support/env.rs:77-89] |
| `resolve_brokered_database_url_at` | function | Reads the local CLI token from 'gobby_home', derives the daemon URL from 'bootstrap_path', and returns the brokered database URL by requesting it from the daemon using that token. [crates/gwiki/src/support/env.rs:91-98] |
| `read_local_cli_token_at` | function | Reads the local CLI token file under 'gobby_home', trims surrounding whitespace, and returns it as a non-empty 'String', failing with context if the file is missing or the trimmed token is empty. [crates/gwiki/src/support/env.rs:100-109] |
| `request_broker_database_url` | function | Validates a loopback daemon URL, POSTs to '{request_base_url}/api/local/runtime/database-url' with the local token and host header under a broker timeout, parses the UTF-8 JSON response, extracts and trims a non-empty 'database_url' string, validates it, and returns it or a contextual error. [crates/gwiki/src/support/env.rs:111-142] |
| `broker_timeout` | function | Returns the broker timeout as a 'Duration', using the positive 'u64' millisecond value from 'GWIKI_BROKER_TIMEOUT_MS_ENV' if present and valid, otherwise falling back to 'DEFAULT_BROKER_TIMEOUT'. [crates/gwiki/src/support/env.rs:144-154] |
| `validate_loopback_daemon_url` | function | Parses 'daemon_url' as a URL, requires a host and port (explicit or scheme-derived), resolves the host to socket addresses, rejects empty or non-loopback resolutions, and returns a 'ValidatedDaemonUrl' with a computed 'request_base_url' and 'host_header'. [crates/gwiki/src/support/env.rs:156-180] |
| `request_base_url` | function | Constructs and returns a request URL by replacing the input URL’s authority with 'target_addr' while preserving its scheme, path, and query string. [crates/gwiki/src/support/env.rs:182-188] |
| `host_header` | function | Returns a correctly formatted HTTP Host header value by bracket-escaping unbracketed IPv6-like hosts containing ':' and appending ':<port>' when a port is provided. [crates/gwiki/src/support/env.rs:190-200] |
| `validate_database_url` | function | Parses and validates that a database URL is a PostgreSQL URL with a host and non-empty database name, then returns the trimmed original string or an error otherwise. [crates/gwiki/src/support/env.rs:202-218] |
| `non_empty_trimmed` | function | Returns the input string trimmed of leading and trailing whitespace, or 'None' if the input is 'None' or the trimmed result is empty. [crates/gwiki/src/support/env.rs:220-224] |
| `max_inbox_item_bytes_from_env` | function | Returns the 'GWIKI_MAX_INBOX_ITEM_BYTES' environment variable as a positive 'u64', falling back to 'DEFAULT_MAX_INBOX_ITEM_BYTES' if the variable is unset or invalid, and emitting a warning only for invalid values. [crates/gwiki/src/support/env.rs:226-234] |
| `parse_positive_u64` | function | Parses the trimmed string as a 'u64' and returns 'Some(value)' only if parsing succeeds and the value is greater than zero, otherwise 'None'. [crates/gwiki/src/support/env.rs:236-238] |
| `spawn_database_url_broker` | function | Binds a loopback TCP listener on an ephemeral port, spawns a thread that accepts one HTTP request, asserts the request includes the expected 'X-Gobby-Local-Token' header, responds with a JSON body containing 'database_url', and returns the port plus the join handle holding the raw request string. [crates/gwiki/src/support/env.rs:299-322] |

_Verified by 3 in-file unit tests._

