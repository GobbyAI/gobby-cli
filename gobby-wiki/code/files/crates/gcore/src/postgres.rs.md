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

`crates/gcore/src/postgres.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `connect_readonly` | function | Indexed function `connect_readonly` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:16-22] |
| `connect_readwrite` | function | Indexed function `connect_readwrite` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:25-27] |
| `read_config_value` | function | Indexed function `read_config_value` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:36-45] |
| `SchemaCheck` | class | Indexed class `SchemaCheck` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:49-58] |
| `validate_schema` | function | Indexed function `validate_schema` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:66-71] |
| `connect` | function | Indexed function `connect` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:73-101] |
| `RequestedSslMode` | type | Indexed type `RequestedSslMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:104-110] |
| `requested_ssl_mode_from_config` | function | Indexed function `requested_ssl_mode_from_config` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:112-119] |
| `requested_ssl_mode` | function | Indexed function `requested_ssl_mode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:121-134] |
| `sslmode_value` | function | Indexed function `sslmode_value` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:136-150] |
| `normalize_sslmode_for_parser` | function | Indexed function `normalize_sslmode_for_parser` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:152-167] |
| `normalize_sslmode_pair` | function | Indexed function `normalize_sslmode_pair` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:169-182] |
| `normalize_sslmode_token` | function | Indexed function `normalize_sslmode_token` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:184-189] |
| `connect_with_tls_unverified` | function | Indexed function `connect_with_tls_unverified` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:191-193] |
| `connect_with_tls_verify_ca` | function | Indexed function `connect_with_tls_verify_ca` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:195-197] |
| `connect_with_tls_verification` | function | Indexed function `connect_with_tls_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:199-209] |
| `connect_with_tls` | function | Indexed function `connect_with_tls` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:211-216] |
| `TlsConnectorMode` | type | Indexed type `TlsConnectorMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:219-223] |
| `TlsConnectorMode::verify_mode` | method | Indexed method `TlsConnectorMode::verify_mode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:226-231] |
| `TlsConnectorMode::uses_default_verify_paths` | method | Indexed method `TlsConnectorMode::uses_default_verify_paths` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:233-235] |
| `TlsConnectorMode::disables_hostname_verification` | method | Indexed method `TlsConnectorMode::disables_hostname_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:237-239] |
| `TlsConnectorBuilder` | class | Indexed class `TlsConnectorBuilder` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:242-247] |
| `tls_connector` | function | Indexed function `tls_connector` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:249-260] |
| `tls_connector_builder` | function | Indexed function `tls_connector_builder` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:262-278] |
| `run_schema_validator` | function | Indexed function `run_schema_validator` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:280-285] |
| `attached_validation_is_non_destructive` | function | Indexed function `attached_validation_is_non_destructive` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:292-310] |
| `schema_validator_is_domain_supplied` | function | Indexed function `schema_validator_is_domain_supplied` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:313-334] |
| `sslmode_parser_selects_tls_modes` | function | Indexed function `sslmode_parser_selects_tls_modes` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:337-347] |
| `quoted_verify_sslmodes_normalize_for_postgres_parser` | function | Indexed function `quoted_verify_sslmodes_normalize_for_postgres_parser` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:350-381] |
| `tls_connector_construction_unverified_disables_peer_verification` | function | Indexed function `tls_connector_construction_unverified_disables_peer_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:384-391] |
| `tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname` | function | Indexed function `tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:394-402] |
| `tls_connector_construction_verify_full_keeps_peer_and_hostname_verification` | function | Indexed function `tls_connector_construction_verify_full_keeps_peer_and_hostname_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:405-413] |

