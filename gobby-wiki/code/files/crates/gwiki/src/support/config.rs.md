---
title: crates/gwiki/src/support/config.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/config.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/config.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/config.rs` exposes 30 indexed API symbols.

## How it fits

`crates/gwiki/src/support/config.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `HubPrimary` | class | Indexed class `HubPrimary` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:18-20] |
| `HubPrimary::config_value` | method | Indexed method `HubPrimary::config_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:23-29] |
| `HubPrimary::resolve_value` | method | Indexed method `HubPrimary::resolve_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:31-43] |
| `hub_ai_config_source` | function | Indexed function `hub_ai_config_source` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:46-61] |
| `SharedCodeGraphLimits` | class | Indexed class `SharedCodeGraphLimits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:68-71] |
| `SharedCodeGraphLimits::default` | method | Indexed method `SharedCodeGraphLimits::default` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:74-79] |
| `local_index_options` | function | Indexed function `local_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:82-86] |
| `index_options_from_conn` | function | Indexed function `index_options_from_conn` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:88-93] |
| `local_shared_code_graph_limits` | function | Indexed function `local_shared_code_graph_limits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:96-102] |
| `shared_code_graph_limits_from_conn` | function | Indexed function `shared_code_graph_limits_from_conn` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:104-111] |
| `qdrant_config_has_url` | function | Indexed function `qdrant_config_has_url` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:113-118] |
| `read_standalone_config` | function | Indexed function `read_standalone_config` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:120-127] |
| `resolve_index_options` | function | Indexed function `resolve_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:129-136] |
| `index_options_from_config` | function | Indexed function `index_options_from_config` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:138-142] |
| `resolve_shared_code_graph_limits` | function | Indexed function `resolve_shared_code_graph_limits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:144-151] |
| `resolve_limit` | function | Indexed function `resolve_limit` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:153-168] |
| `EnvGuard` | class | Indexed class `EnvGuard` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:182-185] |
| `EnvGuard::set_gobby_home` | method | Indexed method `EnvGuard::set_gobby_home` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:188-200] |
| `EnvGuard::drop` | method | Indexed method `EnvGuard::drop` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:204-211] |
| `write_file` | function | Indexed function `write_file` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:214-220] |
| `TestSource` | class | Indexed class `TestSource` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:223-225] |
| `TestSource::with` | method | Indexed method `TestSource::with` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:228-231] |
| `TestSource::config_value` | method | Indexed method `TestSource::config_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:235-237] |
| `TestSource::resolve_value` | method | Indexed method `TestSource::resolve_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:239-241] |
| `shared_code_graph_limits_default_to_200` | function | Indexed function `shared_code_graph_limits_default_to_200` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:245-257] |
| `shared_code_graph_limits_use_config_source_over_standalone` | function | Indexed function `shared_code_graph_limits_use_config_source_over_standalone` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:260-279] |
| `local_shared_code_graph_limits_read_gcore_yaml` | function | Indexed function `local_shared_code_graph_limits_read_gcore_yaml` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:283-301] |
| `shared_code_graph_limits_reject_invalid_or_negative_values` | function | Indexed function `shared_code_graph_limits_reject_invalid_or_negative_values` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:304-316] |
| `local_index_options_read_gcore_yaml` | function | Indexed function `local_index_options_read_gcore_yaml` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:320-332] |
| `memory_indexing_uses_local_index_options` | function | Indexed function `memory_indexing_uses_local_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:336-363] |

