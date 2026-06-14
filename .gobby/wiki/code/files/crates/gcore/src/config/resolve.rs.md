---
title: crates/gcore/src/config/resolve.rs
type: code_file
provenance:
- file: crates/gcore/src/config/resolve.rs
  ranges:
  - 11-21
  - 24-75
  - 78-84
  - 87-90
  - 93-95
  - 103-112
  - 114-126
  - '130'
  - 132-143
  - 146-165
  - 168-174
  - 177-179
  - 182-189
  - 192-202
  - 205-240
  - 242-244
  - 247-254
  - 257-265
  - 268-279
  - 281-317
  - 319-341
  - 343-345
  - 347-350
  - 352-364
  - 366-375
  - 382-404
  - 406-408
  - 410-416
  - 418-435
  - 437-463
  - 465-485
  - 487-491
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config/resolve.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Purpose

This file centralizes config resolution for the gcore crate: it decodes persisted config values, expands `${VAR}` and `${VAR:-default}` environment references, and provides a layered `ConfigSource` abstraction plus an `EnvOnlySource` for reading settings through different source strategies. On top of that, it defines a family of focused resolvers for specific domains like FalkorDB, Qdrant, embeddings, indexing, AI tuning, routing, booleans, ports, and non-empty values, with small helpers such as `env_value`, `resolve_setting`, and `resolve_setting_from_keys` composing those rules into final config outputs.
[crates/gcore/src/config/resolve.rs:11-21]
[crates/gcore/src/config/resolve.rs:24-75]
[crates/gcore/src/config/resolve.rs:78-84]
[crates/gcore/src/config/resolve.rs:87-90]
[crates/gcore/src/config/resolve.rs:93-95]

## API Symbols

- `decode_config_value` (function) component `decode_config_value [function]` (`80f412d7-fdce-5e09-9bb6-e594f1bfa53b`) lines 11-21 [crates/gcore/src/config/resolve.rs:11-21]
  - Signature: `pub fn decode_config_value(raw: &str) -> Option<String> {`
  - Purpose: Indexed function `decode_config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:11-21]
- `resolve_env_pattern` (function) component `resolve_env_pattern [function]` (`11c3db29-aa2f-5ead-b590-5910bec9a60f`) lines 24-75 [crates/gcore/src/config/resolve.rs:24-75]
  - Signature: `pub fn resolve_env_pattern(value: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Indexed function `resolve_env_pattern` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:24-75]
- `ConfigSource` (type) component `ConfigSource [type]` (`9069fc78-5045-51b0-8451-2486189e8dcd`) lines 78-84 [crates/gcore/src/config/resolve.rs:78-84]
  - Signature: `pub trait ConfigSource {`
  - Purpose: Indexed type `ConfigSource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:78-84]
- `LayeredConfigSource` (class) component `LayeredConfigSource [class]` (`d7517547-edfe-50e0-8dff-30d6aadcc687`) lines 87-90 [crates/gcore/src/config/resolve.rs:87-90]
  - Signature: `pub struct LayeredConfigSource<P, F> {`
  - Purpose: Indexed class `LayeredConfigSource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:87-90]
- `new` (function) component `new [function]` (`7a9108ed-1fa2-52aa-aa9d-19ca17600742`) lines 93-95 [crates/gcore/src/config/resolve.rs:93-95]
  - Signature: `pub fn new(primary: Option<P>, fallback: Option<F>) -> Self {`
  - Purpose: Indexed function `new` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:93-95]
- `config_value` (function) component `config_value [function]` (`83cc4770-9b91-5e73-8b1f-92360c580a51`) lines 103-112 [crates/gcore/src/config/resolve.rs:103-112]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed function `config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:103-112]
- `resolve_value` (function) component `resolve_value [function]` (`822f8c58-c511-5bc1-a03b-7b3ec0156fdc`) lines 114-126 [crates/gcore/src/config/resolve.rs:114-126]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:114-126]
- `EnvOnlySource` (class) component `EnvOnlySource [class]` (`0ec7e5ae-6a70-505f-a6ce-69091b5ab153`) lines 130-130 [crates/gcore/src/config/resolve.rs:130]
  - Signature: `pub struct EnvOnlySource;`
  - Purpose: Indexed class `EnvOnlySource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:130]
- `EnvOnlySource` (class) component `EnvOnlySource [class]` (`aaba9585-98c6-53ee-825d-db0c27a3faf6`) lines 132-143 [crates/gcore/src/config/resolve.rs:132-143]
  - Signature: `impl ConfigSource for EnvOnlySource {`
  - Purpose: Indexed class `EnvOnlySource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:132-143]
- `EnvOnlySource.config_value` (method) component `EnvOnlySource.config_value [method]` (`3d23ffbe-8cb0-5f0f-b9cd-8f153f36af7c`) lines 133-135 [crates/gcore/src/config/resolve.rs:133-135]
  - Signature: `fn config_value(&mut self, _key: &str) -> Option<String> {`
  - Purpose: Indexed method `EnvOnlySource.config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:133-135]
- `EnvOnlySource.resolve_value` (method) component `EnvOnlySource.resolve_value [method]` (`39f129c8-ad2a-5d0e-b063-4c83cfd3d696`) lines 137-142 [crates/gcore/src/config/resolve.rs:137-142]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `EnvOnlySource.resolve_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:137-142]
- `resolve_falkordb_config` (function) component `resolve_falkordb_config [function]` (`366ad0f3-2c32-55e3-a73a-fdb15e5d0453`) lines 146-165 [crates/gcore/src/config/resolve.rs:146-165]
  - Signature: `pub fn resolve_falkordb_config(source: &mut impl ConfigSource) -> Option<FalkorConfig> {`
  - Purpose: Indexed function `resolve_falkordb_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:146-165]
- `resolve_qdrant_config` (function) component `resolve_qdrant_config [function]` (`c5451f83-1ad9-5238-b232-b10f06122b01`) lines 168-174 [crates/gcore/src/config/resolve.rs:168-174]
  - Signature: `pub fn resolve_qdrant_config(source: &mut impl ConfigSource) -> Option<QdrantConfig> {`
  - Purpose: Indexed function `resolve_qdrant_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:168-174]
- `resolve_embedding_config` (function) component `resolve_embedding_config [function]` (`7fa9defe-5db2-597d-9306-e12694bd1135`) lines 177-179 [crates/gcore/src/config/resolve.rs:177-179]
  - Signature: `pub fn resolve_embedding_config(source: &mut impl ConfigSource) -> Option<EmbeddingConfig> {`
  - Purpose: Indexed function `resolve_embedding_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:177-179]
- `resolve_indexing_config` (function) component `resolve_indexing_config [function]` (`de1c5e68-9cbe-5715-ac48-cfb1b31f2a40`) lines 182-189 [crates/gcore/src/config/resolve.rs:182-189]
  - Signature: `pub fn resolve_indexing_config(source: &mut impl ConfigSource) -> anyhow::Result<IndexingConfig> {`
  - Purpose: Indexed function `resolve_indexing_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:182-189]
- `resolve_embedding_config_resolution` (function) component `resolve_embedding_config_resolution [function]` (`ee2c53d8-7d50-5a28-99f6-2994874d9877`) lines 192-202 [crates/gcore/src/config/resolve.rs:192-202]
  - Signature: `pub fn resolve_embedding_config_resolution(`
  - Purpose: Indexed function `resolve_embedding_config_resolution` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:192-202]
- `resolve_embedding_config_from_binding` (function) component `resolve_embedding_config_from_binding [function]` (`a98c8b97-e183-51de-b323-af60a89ce1de`) lines 205-240 [crates/gcore/src/config/resolve.rs:205-240]
  - Signature: `pub fn resolve_embedding_config_from_binding(`
  - Purpose: Indexed function `resolve_embedding_config_from_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:205-240]
- `resolve_embedding_setting` (function) component `resolve_embedding_setting [function]` (`a7032c76-16a5-549a-b010-7e16cd88ad4b`) lines 242-244 [crates/gcore/src/config/resolve.rs:242-244]
  - Signature: `fn resolve_embedding_setting(source: &mut impl ConfigSource, config_key: &str) -> Option<String> {`
  - Purpose: Indexed function `resolve_embedding_setting` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:242-244]
- `resolve_capability_routing` (function) component `resolve_capability_routing [function]` (`d0c81530-58eb-5982-b298-44b2d00bceab`) lines 247-254 [crates/gcore/src/config/resolve.rs:247-254]
  - Signature: `pub fn resolve_capability_routing(`
  - Purpose: Indexed function `resolve_capability_routing` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:247-254]
- `resolve_capability_binding` (function) component `resolve_capability_binding [function]` (`cb75b67a-2194-5bcc-9517-4e525b8720d5`) lines 257-265 [crates/gcore/src/config/resolve.rs:257-265]
  - Signature: `pub fn resolve_capability_binding(`
  - Purpose: Indexed function `resolve_capability_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:257-265]
- `resolve_ai_tuning` (function) component `resolve_ai_tuning [function]` (`e25c29fa-fd54-59c8-a411-512026cff2ba`) lines 268-279 [crates/gcore/src/config/resolve.rs:268-279]
  - Signature: `pub fn resolve_ai_tuning(source: &mut impl ConfigSource) -> AiTuning {`
  - Purpose: Indexed function `resolve_ai_tuning` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:268-279]
- `resolve_base_capability_binding` (function) component `resolve_base_capability_binding [function]` (`54e03bdf-1d5c-5ee0-ad31-8a48ae38e23e`) lines 281-317 [crates/gcore/src/config/resolve.rs:281-317]
  - Signature: `fn resolve_base_capability_binding(`
  - Purpose: Indexed function `resolve_base_capability_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:281-317]
- `resolve_audio_translate_binding` (function) component `resolve_audio_translate_binding [function]` (`2a6506bc-efa8-518e-ac69-1e0f2a843422`) lines 319-341 [crates/gcore/src/config/resolve.rs:319-341]
  - Signature: `fn resolve_audio_translate_binding(source: &mut impl ConfigSource) -> CapabilityBinding {`
  - Purpose: Indexed function `resolve_audio_translate_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:319-341]
- `resolve_ai_routing_value` (function) component `resolve_ai_routing_value [function]` (`13f38e22-9d9a-57a3-89d3-2f989bfdb0f4`) lines 343-345 [crates/gcore/src/config/resolve.rs:343-345]
  - Signature: `fn resolve_ai_routing_value(source: &mut impl ConfigSource, config_key: &str) -> Option<AiRouting> {`
  - Purpose: Indexed function `resolve_ai_routing_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:343-345]
- `resolve_ai_config_value` (function) component `resolve_ai_config_value [function]` (`4674d845-e391-5592-a870-9070ea857dff`) lines 347-350 [crates/gcore/src/config/resolve.rs:347-350]
  - Signature: `fn resolve_ai_config_value(source: &mut impl ConfigSource, config_key: &str) -> Option<String> {`
  - Purpose: Indexed function `resolve_ai_config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:347-350]
- `resolve_config_bool` (function) component `resolve_config_bool [function]` (`14cccc07-ab22-586d-a781-25e8e5a06368`) lines 352-364 [crates/gcore/src/config/resolve.rs:352-364]
  - Signature: `fn resolve_config_bool(`
  - Purpose: Indexed function `resolve_config_bool` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:352-364]
- `parse_config_bool_or_default` (function) component `parse_config_bool_or_default [function]` (`cbc0cd4c-3885-56e1-ba7a-082d5b0f85c9`) lines 366-375 [crates/gcore/src/config/resolve.rs:366-375]
  - Signature: `fn parse_config_bool_or_default(source_key: &str, value: &str, default: bool) -> bool {`
  - Purpose: Indexed function `parse_config_bool_or_default` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:366-375]
- `resolve_ai_non_empty` (function) component `resolve_ai_non_empty [function]` (`4ab9066e-593c-5a15-b28f-d5a743794205`) lines 382-404 [crates/gcore/src/config/resolve.rs:382-404]
  - Signature: `fn resolve_ai_non_empty(`
  - Purpose: Indexed function `resolve_ai_non_empty` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:382-404]
- `contains_unresolved_env_pattern` (function) component `contains_unresolved_env_pattern [function]` (`a968f527-6082-5f78-8b77-eb5ff2928b18`) lines 406-408 [crates/gcore/src/config/resolve.rs:406-408]
  - Signature: `fn contains_unresolved_env_pattern(value: &str) -> bool {`
  - Purpose: Indexed function `contains_unresolved_env_pattern` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:406-408]
- `resolve_setting` (function) component `resolve_setting [function]` (`2d9eb742-31dc-56dd-8c20-300921ca0ef4`) lines 410-416 [crates/gcore/src/config/resolve.rs:410-416]
  - Signature: `fn resolve_setting(`
  - Purpose: Indexed function `resolve_setting` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:410-416]
- `resolve_setting_from_keys` (function) component `resolve_setting_from_keys [function]` (`bf5dbd32-f12c-528b-827c-fd424b368a09`) lines 418-435 [crates/gcore/src/config/resolve.rs:418-435]
  - Signature: `fn resolve_setting_from_keys(`
  - Purpose: Indexed function `resolve_setting_from_keys` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:418-435]
- `resolve_port` (function) component `resolve_port [function]` (`a1ac57e7-05f8-5c88-b49f-f87951768859`) lines 437-463 [crates/gcore/src/config/resolve.rs:437-463]
  - Signature: `fn resolve_port(`
  - Purpose: Indexed function `resolve_port` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:437-463]
- `resolve_non_empty` (function) component `resolve_non_empty [function]` (`a6037978-5cab-5516-be3c-0317da28cd45`) lines 465-485 [crates/gcore/src/config/resolve.rs:465-485]
  - Signature: `fn resolve_non_empty(`
  - Purpose: Indexed function `resolve_non_empty` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:465-485]
- `env_value` (function) component `env_value [function]` (`04692329-272a-5687-88a9-ddfd0dc4383d`) lines 487-491 [crates/gcore/src/config/resolve.rs:487-491]
  - Signature: `fn env_value(key: &str) -> Option<String> {`
  - Purpose: Indexed function `env_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:487-491]

