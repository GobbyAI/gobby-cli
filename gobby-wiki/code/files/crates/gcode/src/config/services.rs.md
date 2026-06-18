---
title: crates/gcode/src/config/services.rs
type: code_file
provenance:
- file: crates/gcode/src/config/services.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/services.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/config/services.rs` exposes 53 indexed API symbols.

## How it fits

`crates/gcode/src/config/services.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `PostgresConfigSource` | class | Indexed class `PostgresConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:20-22] |
| `ServiceConfigSource` | type | Indexed type `ServiceConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:24-27] |
| `service_env_value` | function | Indexed function `service_env_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:29-39] |
| `config_store_missing` | function | Indexed function `config_store_missing` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:41-48] |
| `config_value` | function | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:51-57] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:59-61] |
| `FallbackConfigSource` | class | Indexed class `FallbackConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:64-67] |
| `config_value` | function | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:70-81] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:83-85] |
| `EmbeddingConfigDetails` | class | Indexed class `EmbeddingConfigDetails` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:89-93] |
| `TracingFallbackConfigSource` | class | Indexed class `TracingFallbackConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:95-99] |
| `hit_source` | function | Indexed function `hit_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:102-104] |
| `config_value` | function | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:108-125] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:127-129] |
| `ErrorCapturingConfigSource` | class | Indexed class `ErrorCapturingConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:132-135] |
| `finish` | function | Indexed function `finish` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:138-143] |
| `config_value` | function | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:150-162] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:164-166] |
| `read_standalone_config_optional` | function | Indexed function `read_standalone_config_optional` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:169-178] |
| `StandaloneConfigReadError` | type | Indexed type `StandaloneConfigReadError` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:181-196] |
| `StandaloneConfigReadError::fmt` | method | Indexed method `StandaloneConfigReadError::fmt` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:199-221] |
| `read_standalone_config` | function | Indexed function `read_standalone_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:226-241] |
| `ClosureConfigSource` | class | Indexed class `ClosureConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:244-247] |
| `config_value` | function | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:255-257] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:259-261] |
| `config_value` | function | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:270-276] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:278-280] |
| `FallibleClosureConfigSource` | class | Indexed class `FallibleClosureConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:284-287] |
| `config_value` | function | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:295-301] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:303-305] |
| `resolve_falkordb_config_from_values` | function | Indexed function `resolve_falkordb_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:309-322] |
| `resolve_qdrant_config_from_values` | function | Indexed function `resolve_qdrant_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:325-338] |
| `resolve_embedding_config_from_values` | function | Indexed function `resolve_embedding_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:341-354] |
| `resolve_embedding_config_from_fallible_values` | function | Indexed function `resolve_embedding_config_from_fallible_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:357-370] |
| `resolve_code_vector_settings_from_values` | function | Indexed function `resolve_code_vector_settings_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:373-384] |
| `resolve_falkordb_config` | function | Indexed function `resolve_falkordb_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:389-399] |
| `resolve_falkordb_config_from_source` | function | Indexed function `resolve_falkordb_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:401-416] |
| `resolve_qdrant_config` | function | Indexed function `resolve_qdrant_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:421-431] |
| `resolve_qdrant_config_from_source` | function | Indexed function `resolve_qdrant_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:433-442] |
| `resolve_service_setting` | function | Indexed function `resolve_service_setting` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:444-452] |
| `resolve_service_non_empty` | function | Indexed function `resolve_service_non_empty` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:454-469] |
| `resolve_service_port` | function | Indexed function `resolve_service_port` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:471-494] |
| `resolve_embedding_config` | function | Indexed function `resolve_embedding_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:501-511] |
| `resolve_embedding_config_details` | function | Indexed function `resolve_embedding_config_details` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:513-533] |
| `resolve_embedding_config_from_service_source` | function | Indexed function `resolve_embedding_config_from_service_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:535-545] |
| `resolve_embedding_config_from_source` | function | Indexed function `resolve_embedding_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:547-557] |
| `embedding_binding_routes_direct` | function | Indexed function `embedding_binding_routes_direct` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:559-568] |
| `embedding_binding_uses_openai_http` | function | Indexed function `embedding_binding_uses_openai_http` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:570-576] |
| `resolve_code_vector_settings` | function | Indexed function `resolve_code_vector_settings` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:578-587] |
| `resolve_indexing_settings` | function | Indexed function `resolve_indexing_settings` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:589-603] |
| `resolve_code_vector_settings_from_source` | function | Indexed function `resolve_code_vector_settings_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:605-611] |
| `resolve_vector_dim` | function | Indexed function `resolve_vector_dim` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:613-624] |
| `parse_vector_dim` | function | Indexed function `parse_vector_dim` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:626-635] |

