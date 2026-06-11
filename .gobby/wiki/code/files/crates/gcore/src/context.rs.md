---
title: crates/gcore/src/context.rs
type: code_file
provenance:
- file: crates/gcore/src/context.rs
  ranges:
  - 16-31
  - 33-84
  - 35-55
  - 57-59
  - 61-63
  - 65-67
  - 69-71
  - 73-75
  - 77-79
  - 81-83
  - 93-95
  - 97-125
  - 98-106
  - 108-120
  - 122-124
  - 127-131
  - 128-130
  - 133-135
  - 137-146
  - 138-145
  - 148-156
  - 149-151
  - 153-155
  - 159-173
  - 176-205
  - 208-222
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/context.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/context.rs` exposes 26 indexed API symbols.
[crates/gcore/src/context.rs:16-31]
[crates/gcore/src/context.rs:33-84]
[crates/gcore/src/context.rs:35-55]
[crates/gcore/src/context.rs:57-59]
[crates/gcore/src/context.rs:61-63]

## API Symbols

- `CoreContext` (class) component `CoreContext [class]` (`ec8f68d8-f760-5b8e-9ea5-24c931c20fd2`) lines 16-31 [crates/gcore/src/context.rs:16-31]
  - Signature: `pub struct CoreContext {`
  - Purpose: Indexed class `CoreContext` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:16-31]
- `CoreContext` (class) component `CoreContext [class]` (`c271c0a4-aff6-5398-9a47-bb5e757c6061`) lines 33-84 [crates/gcore/src/context.rs:33-84]
  - Signature: `impl CoreContext {`
  - Purpose: Indexed class `CoreContext` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:33-84]
- `CoreContext.build` (method) component `CoreContext.build [method]` (`97acbcc2-cdaa-50d0-af19-2f2e0d9f205b`) lines 35-55 [crates/gcore/src/context.rs:35-55]
  - Signature: `pub fn build(`
  - Purpose: Indexed method `CoreContext.build` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:35-55]
- `CoreContext.project_root` (method) component `CoreContext.project_root [method]` (`223ea409-12c3-51c2-b2dc-cb4433680649`) lines 57-59 [crates/gcore/src/context.rs:57-59]
  - Signature: `pub fn project_root(&self) -> &Path {`
  - Purpose: Indexed method `CoreContext.project_root` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:57-59]
- `CoreContext.project_id` (method) component `CoreContext.project_id [method]` (`49a05235-715a-5a93-857e-1af48e620d42`) lines 61-63 [crates/gcore/src/context.rs:61-63]
  - Signature: `pub fn project_id(&self) -> &str {`
  - Purpose: Indexed method `CoreContext.project_id` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:61-63]
- `CoreContext.database_url` (method) component `CoreContext.database_url [method]` (`b98f056f-d708-5e27-a5e4-bc81810d1973`) lines 65-67 [crates/gcore/src/context.rs:65-67]
  - Signature: `pub fn database_url(&self) -> Option<&str> {`
  - Purpose: Indexed method `CoreContext.database_url` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:65-67]
- `CoreContext.falkordb` (method) component `CoreContext.falkordb [method]` (`5fc82ba4-af99-58cc-929c-c2666e2000eb`) lines 69-71 [crates/gcore/src/context.rs:69-71]
  - Signature: `pub fn falkordb(&self) -> Option<&FalkorConfig> {`
  - Purpose: Indexed method `CoreContext.falkordb` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:69-71]
- `CoreContext.qdrant` (method) component `CoreContext.qdrant [method]` (`a71512d2-d3f1-57e0-913a-ce1a558fa2af`) lines 73-75 [crates/gcore/src/context.rs:73-75]
  - Signature: `pub fn qdrant(&self) -> Option<&QdrantConfig> {`
  - Purpose: Indexed method `CoreContext.qdrant` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:73-75]
- `CoreContext.embedding` (method) component `CoreContext.embedding [method]` (`7ca04a91-4cb4-58f9-95f5-6522bed7c009`) lines 77-79 [crates/gcore/src/context.rs:77-79]
  - Signature: `pub fn embedding(&self) -> Option<&EmbeddingConfig> {`
  - Purpose: Indexed method `CoreContext.embedding` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:77-79]
- `CoreContext.daemon_url` (method) component `CoreContext.daemon_url [method]` (`50fb5e02-d55b-52f5-bd71-a666e47fa3c0`) lines 81-83 [crates/gcore/src/context.rs:81-83]
  - Signature: `pub fn daemon_url(&self) -> &str {`
  - Purpose: Indexed method `CoreContext.daemon_url` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:81-83]
- `EnvGuard` (class) component `EnvGuard [class]` (`3bc76907-2419-512c-9691-65a59a45cbb3`) lines 93-95 [crates/gcore/src/context.rs:93-95]
  - Signature: `struct EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:93-95]
- `EnvGuard` (class) component `EnvGuard [class]` (`53a35fcc-feb6-5b0e-8879-58def325c84e`) lines 97-125 [crates/gcore/src/context.rs:97-125]
  - Signature: `impl EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:97-125]
- `EnvGuard.new` (method) component `EnvGuard.new [method]` (`2167282f-0f46-5e5d-8458-b180841a8f7e`) lines 98-106 [crates/gcore/src/context.rs:98-106]
  - Signature: `fn new() -> Self {`
  - Purpose: Indexed method `EnvGuard.new` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:98-106]
- `EnvGuard.clear` (method) component `EnvGuard.clear [method]` (`5d899f84-fa21-5a80-b861-79f158556dff`) lines 108-120 [crates/gcore/src/context.rs:108-120]
  - Signature: `fn clear(&self) {`
  - Purpose: Indexed method `EnvGuard.clear` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:108-120]
- `EnvGuard.set` (method) component `EnvGuard.set [method]` (`c51b7e94-1cbe-575b-a3a9-46816a03c868`) lines 122-124 [crates/gcore/src/context.rs:122-124]
  - Signature: `fn set(&self, key: &str, value: &str) {`
  - Purpose: Indexed method `EnvGuard.set` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:122-124]
- `EnvGuard` (class) component `EnvGuard [class]` (`855a4fcc-aa8b-53cd-a45d-319c16306db9`) lines 127-131 [crates/gcore/src/context.rs:127-131]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:127-131]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`86a0b0b2-04bb-5c43-bd23-be7065a86954`) lines 128-130 [crates/gcore/src/context.rs:128-130]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `EnvGuard.drop` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:128-130]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`761dee47-2323-5839-94eb-54f67c437c01`) lines 133-135 [crates/gcore/src/context.rs:133-135]
  - Signature: `struct TestConfigSource {`
  - Purpose: Indexed class `TestConfigSource` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:133-135]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`fc73db06-13ef-5eca-96af-a960f505eb7c`) lines 137-146 [crates/gcore/src/context.rs:137-146]
  - Signature: `impl TestConfigSource {`
  - Purpose: Indexed class `TestConfigSource` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:137-146]
- `TestConfigSource.with_values` (method) component `TestConfigSource.with_values [method]` (`3a66a8ac-1486-5b1f-95dd-7c573a8b1954`) lines 138-145 [crates/gcore/src/context.rs:138-145]
  - Signature: `fn with_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {`
  - Purpose: Indexed method `TestConfigSource.with_values` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:138-145]
- `TestConfigSource` (class) component `TestConfigSource [class]` (`f5f5c986-b41c-5a22-bbd1-ac64d8aa758c`) lines 148-156 [crates/gcore/src/context.rs:148-156]
  - Signature: `impl ConfigSource for TestConfigSource {`
  - Purpose: Indexed class `TestConfigSource` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:148-156]
- `TestConfigSource.config_value` (method) component `TestConfigSource.config_value [method]` (`346478b4-9e15-58b7-b4d4-5be9b850c700`) lines 149-151 [crates/gcore/src/context.rs:149-151]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed method `TestConfigSource.config_value` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:149-151]
- `TestConfigSource.resolve_value` (method) component `TestConfigSource.resolve_value [method]` (`c3bd516f-3116-593e-847b-9cf54164f2bf`) lines 153-155 [crates/gcore/src/context.rs:153-155]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `TestConfigSource.resolve_value` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:153-155]
- `missing_diagnostic_service_config_is_none` (function) component `missing_diagnostic_service_config_is_none [function]` (`80c87170-5868-5342-8edf-440096d9c977`) lines 159-173 [crates/gcore/src/context.rs:159-173]
  - Signature: `fn missing_diagnostic_service_config_is_none() {`
  - Purpose: Indexed function `missing_diagnostic_service_config_is_none` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:159-173]
- `build_with_env_only_source` (function) component `build_with_env_only_source [function]` (`ff8cfd91-eb61-5e19-a722-08f74384c0b1`) lines 176-205 [crates/gcore/src/context.rs:176-205]
  - Signature: `fn build_with_env_only_source() {`
  - Purpose: Indexed function `build_with_env_only_source` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:176-205]
- `build_with_config_source_embedding` (function) component `build_with_config_source_embedding [function]` (`1fb89c5e-9c5a-58c0-be4d-3671407f62f8`) lines 208-222 [crates/gcore/src/context.rs:208-222]
  - Signature: `fn build_with_config_source_embedding() {`
  - Purpose: Indexed function `build_with_config_source_embedding` in `crates/gcore/src/context.rs`. [crates/gcore/src/context.rs:208-222]

