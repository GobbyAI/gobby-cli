---
title: crates/gcore/src/falkor.rs
type: code_file
provenance:
- file: crates/gcore/src/falkor.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/falkor.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/falkor.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gcore/src/falkor.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Row` | type | Indexed type `Row` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:22] |
| `GraphClient` | class | Indexed class `GraphClient` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:28-30] |
| `ReadOnlySyncGraph` | class | Indexed class `ReadOnlySyncGraph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:36-38] |
| `graph_name` | function | Indexed function `graph_name` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:42-44] |
| `ro_query` | function | Indexed function `ro_query` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:47-52] |
| `GraphClient::from_config` | method | Indexed method `GraphClient::from_config` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:57-72] |
| `GraphClient::with_sync_graph` | method | Indexed method `GraphClient::with_sync_graph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:79-87] |
| `GraphClient::query` | method | Indexed method `GraphClient::query` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:90-105] |
| `GraphClient::ensure_exact_node_index` | method | Indexed method `GraphClient::ensure_exact_node_index` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:108-126] |
| `with_graph` | function | Indexed function `with_graph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:136-143] |
| `with_graph_client` | function | Indexed function `with_graph_client` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:145-172] |
| `escape_label` | function | Indexed function `escape_label` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:175-177] |
| `escape_rel_type` | function | Indexed function `escape_rel_type` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:180-182] |
| `escape_property` | function | Indexed function `escape_property` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:185-187] |
| `escape_string` | function | Indexed function `escape_string` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:195-198] |
| `escape_identifier` | function | Indexed function `escape_identifier` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:200-202] |
| `is_existing_index_error` | function | Indexed function `is_existing_index_error` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:207-220] |
| `parse_falkor_result` | function | Indexed function `parse_falkor_result` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:222-224] |
| `parse_falkor_records` | function | Indexed function `parse_falkor_records` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:226-241] |
| `falkor_value_to_json` | function | Indexed function `falkor_value_to_json` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:243-266] |
| `FakeGraphClient` | class | Indexed class `FakeGraphClient` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:275] |
| `test_config` | function | Indexed function `test_config` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:277-283] |
| `with_graph_degradation_contract` | function | Indexed function `with_graph_degradation_contract` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:286-334] |
| `escapes_graph_tokens` | function | Indexed function `escapes_graph_tokens` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:337-345] |
| `no_domain_labels_in_adapter` | function | Indexed function `no_domain_labels_in_adapter` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:348-361] |
| `graph_unavailable_is_not_empty_success` | function | Indexed function `graph_unavailable_is_not_empty_success` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:364-389] |
| `graph_name_is_consumer_supplied` | function | Indexed function `graph_name_is_consumer_supplied` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:392-415] |
| `live_sync_graph_read_is_env_gated` | function | Indexed function `live_sync_graph_read_is_env_gated` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:418-441] |
| `live_falkor_fixture` | function | Indexed function `live_falkor_fixture` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:443-462] |
| `existing_index_errors_are_recognized_case_insensitively` | function | Indexed function `existing_index_errors_are_recognized_case_insensitively` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:465-474] |
| `unrelated_index_errors_are_not_suppressed` | function | Indexed function `unrelated_index_errors_are_not_suppressed` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:477-481] |

