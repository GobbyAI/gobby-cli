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
  - 133-135
  - 137-142
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/config/resolve.rs:11-21](crates/gcore/src/config/resolve.rs#L11-L21), [crates/gcore/src/config/resolve.rs:24-75](crates/gcore/src/config/resolve.rs#L24-L75), [crates/gcore/src/config/resolve.rs:78-84](crates/gcore/src/config/resolve.rs#L78-L84), [crates/gcore/src/config/resolve.rs:87-90](crates/gcore/src/config/resolve.rs#L87-L90), [crates/gcore/src/config/resolve.rs:93-95](crates/gcore/src/config/resolve.rs#L93-L95), [crates/gcore/src/config/resolve.rs:103-112](crates/gcore/src/config/resolve.rs#L103-L112), [crates/gcore/src/config/resolve.rs:114-126](crates/gcore/src/config/resolve.rs#L114-L126), [crates/gcore/src/config/resolve.rs:130](crates/gcore/src/config/resolve.rs#L130), [crates/gcore/src/config/resolve.rs:133-135](crates/gcore/src/config/resolve.rs#L133-L135), [crates/gcore/src/config/resolve.rs:137-142](crates/gcore/src/config/resolve.rs#L137-L142), [crates/gcore/src/config/resolve.rs:146-165](crates/gcore/src/config/resolve.rs#L146-L165), [crates/gcore/src/config/resolve.rs:168-174](crates/gcore/src/config/resolve.rs#L168-L174), [crates/gcore/src/config/resolve.rs:177-179](crates/gcore/src/config/resolve.rs#L177-L179), [crates/gcore/src/config/resolve.rs:182-189](crates/gcore/src/config/resolve.rs#L182-L189), [crates/gcore/src/config/resolve.rs:192-202](crates/gcore/src/config/resolve.rs#L192-L202), [crates/gcore/src/config/resolve.rs:205-240](crates/gcore/src/config/resolve.rs#L205-L240), [crates/gcore/src/config/resolve.rs:242-244](crates/gcore/src/config/resolve.rs#L242-L244), [crates/gcore/src/config/resolve.rs:247-254](crates/gcore/src/config/resolve.rs#L247-L254), [crates/gcore/src/config/resolve.rs:257-265](crates/gcore/src/config/resolve.rs#L257-L265), [crates/gcore/src/config/resolve.rs:268-279](crates/gcore/src/config/resolve.rs#L268-L279), [crates/gcore/src/config/resolve.rs:281-317](crates/gcore/src/config/resolve.rs#L281-L317), [crates/gcore/src/config/resolve.rs:319-341](crates/gcore/src/config/resolve.rs#L319-L341), [crates/gcore/src/config/resolve.rs:343-345](crates/gcore/src/config/resolve.rs#L343-L345), [crates/gcore/src/config/resolve.rs:347-350](crates/gcore/src/config/resolve.rs#L347-L350), [crates/gcore/src/config/resolve.rs:352-364](crates/gcore/src/config/resolve.rs#L352-L364), [crates/gcore/src/config/resolve.rs:366-375](crates/gcore/src/config/resolve.rs#L366-L375), [crates/gcore/src/config/resolve.rs:382-404](crates/gcore/src/config/resolve.rs#L382-L404), [crates/gcore/src/config/resolve.rs:406-408](crates/gcore/src/config/resolve.rs#L406-L408), [crates/gcore/src/config/resolve.rs:410-416](crates/gcore/src/config/resolve.rs#L410-L416), [crates/gcore/src/config/resolve.rs:418-435](crates/gcore/src/config/resolve.rs#L418-L435), [crates/gcore/src/config/resolve.rs:437-463](crates/gcore/src/config/resolve.rs#L437-L463), [crates/gcore/src/config/resolve.rs:465-485](crates/gcore/src/config/resolve.rs#L465-L485), [crates/gcore/src/config/resolve.rs:487-491](crates/gcore/src/config/resolve.rs#L487-L491)

</details>

# crates/gcore/src/config/resolve.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Purpose

Provides the config resolution layer for `gcore`, including defaults and helpers for decoding stored config values, expanding `${VAR}` and `${VAR:-default}` patterns, and reading values from the environment or layered sources. The file defines small source abstractions and a set of subsystem-specific resolvers for FalkorDB, Qdrant, embeddings, indexing, AI tuning, capability routing/bindings, booleans, ports, and non-empty settings, all built on shared helpers like `resolve_setting`, `resolve_value`, and `env_value` to normalize and validate configuration input.
[crates/gcore/src/config/resolve.rs:11-21]
[crates/gcore/src/config/resolve.rs:24-75]
[crates/gcore/src/config/resolve.rs:78-84]
[crates/gcore/src/config/resolve.rs:87-90]
[crates/gcore/src/config/resolve.rs:93-95]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `decode_config_value` | function | `pub fn decode_config_value(raw: &str) -> Option<String> {` | `decode_config_value [function]` | `80f412d7-fdce-5e09-9bb6-e594f1bfa53b` | 11-21 [crates/gcore/src/config/resolve.rs:11-21] | Indexed function `decode_config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:11-21] |
| `resolve_env_pattern` | function | `pub fn resolve_env_pattern(value: &str) -> anyhow::Result<Option<String>> {` | `resolve_env_pattern [function]` | `11c3db29-aa2f-5ead-b590-5910bec9a60f` | 24-75 [crates/gcore/src/config/resolve.rs:24-75] | Indexed function `resolve_env_pattern` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:24-75] |
| `ConfigSource` | type | `pub trait ConfigSource {` | `ConfigSource [type]` | `9069fc78-5045-51b0-8451-2486189e8dcd` | 78-84 [crates/gcore/src/config/resolve.rs:78-84] | Indexed type `ConfigSource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:78-84] |
| `LayeredConfigSource` | class | `pub struct LayeredConfigSource<P, F> {` | `LayeredConfigSource [class]` | `d7517547-edfe-50e0-8dff-30d6aadcc687` | 87-90 [crates/gcore/src/config/resolve.rs:87-90] | Indexed class `LayeredConfigSource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:87-90] |
| `new` | function | `pub fn new(primary: Option<P>, fallback: Option<F>) -> Self {` | `new [function]` | `7a9108ed-1fa2-52aa-aa9d-19ca17600742` | 93-95 [crates/gcore/src/config/resolve.rs:93-95] | Indexed function `new` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:93-95] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> Option<String> {` | `config_value [function]` | `83cc4770-9b91-5e73-8b1f-92360c580a51` | 103-112 [crates/gcore/src/config/resolve.rs:103-112] | Indexed function `config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:103-112] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `822f8c58-c511-5bc1-a03b-7b3ec0156fdc` | 114-126 [crates/gcore/src/config/resolve.rs:114-126] | Indexed function `resolve_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:114-126] |
| `EnvOnlySource` | class | `pub struct EnvOnlySource;` | `EnvOnlySource [class]` | `0ec7e5ae-6a70-505f-a6ce-69091b5ab153` | 130-130 [crates/gcore/src/config/resolve.rs:130] | Indexed class `EnvOnlySource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:130] |
| `EnvOnlySource::config_value` | method | `fn config_value(&mut self, _key: &str) -> Option<String> {` | `EnvOnlySource::config_value [method]` | `3d23ffbe-8cb0-5f0f-b9cd-8f153f36af7c` | 133-135 [crates/gcore/src/config/resolve.rs:133-135] | Indexed method `EnvOnlySource::config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:133-135] |
| `EnvOnlySource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `EnvOnlySource::resolve_value [method]` | `39f129c8-ad2a-5d0e-b063-4c83cfd3d696` | 137-142 [crates/gcore/src/config/resolve.rs:137-142] | Indexed method `EnvOnlySource::resolve_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:137-142] |
| `resolve_falkordb_config` | function | `pub fn resolve_falkordb_config(source: &mut impl ConfigSource) -> Option<FalkorConfig> {` | `resolve_falkordb_config [function]` | `366ad0f3-2c32-55e3-a73a-fdb15e5d0453` | 146-165 [crates/gcore/src/config/resolve.rs:146-165] | Indexed function `resolve_falkordb_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:146-165] |
| `resolve_qdrant_config` | function | `pub fn resolve_qdrant_config(source: &mut impl ConfigSource) -> Option<QdrantConfig> {` | `resolve_qdrant_config [function]` | `c5451f83-1ad9-5238-b232-b10f06122b01` | 168-174 [crates/gcore/src/config/resolve.rs:168-174] | Indexed function `resolve_qdrant_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:168-174] |
| `resolve_embedding_config` | function | `pub fn resolve_embedding_config(source: &mut impl ConfigSource) -> Option<EmbeddingConfig> {` | `resolve_embedding_config [function]` | `7fa9defe-5db2-597d-9306-e12694bd1135` | 177-179 [crates/gcore/src/config/resolve.rs:177-179] | Indexed function `resolve_embedding_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:177-179] |
| `resolve_indexing_config` | function | `pub fn resolve_indexing_config(source: &mut impl ConfigSource) -> anyhow::Result<IndexingConfig> {` | `resolve_indexing_config [function]` | `de1c5e68-9cbe-5715-ac48-cfb1b31f2a40` | 182-189 [crates/gcore/src/config/resolve.rs:182-189] | Indexed function `resolve_indexing_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:182-189] |
| `resolve_embedding_config_resolution` | function | `pub fn resolve_embedding_config_resolution(` | `resolve_embedding_config_resolution [function]` | `ee2c53d8-7d50-5a28-99f6-2994874d9877` | 192-202 [crates/gcore/src/config/resolve.rs:192-202] | Indexed function `resolve_embedding_config_resolution` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:192-202] |
| `resolve_embedding_config_from_binding` | function | `pub fn resolve_embedding_config_from_binding(` | `resolve_embedding_config_from_binding [function]` | `a98c8b97-e183-51de-b323-af60a89ce1de` | 205-240 [crates/gcore/src/config/resolve.rs:205-240] | Indexed function `resolve_embedding_config_from_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:205-240] |
| `resolve_embedding_setting` | function | `fn resolve_embedding_setting(source: &mut impl ConfigSource, config_key: &str) -> Option<String> {` | `resolve_embedding_setting [function]` | `a7032c76-16a5-549a-b010-7e16cd88ad4b` | 242-244 [crates/gcore/src/config/resolve.rs:242-244] | Indexed function `resolve_embedding_setting` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:242-244] |
| `resolve_capability_routing` | function | `pub fn resolve_capability_routing(` | `resolve_capability_routing [function]` | `d0c81530-58eb-5982-b298-44b2d00bceab` | 247-254 [crates/gcore/src/config/resolve.rs:247-254] | Indexed function `resolve_capability_routing` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:247-254] |
| `resolve_capability_binding` | function | `pub fn resolve_capability_binding(` | `resolve_capability_binding [function]` | `cb75b67a-2194-5bcc-9517-4e525b8720d5` | 257-265 [crates/gcore/src/config/resolve.rs:257-265] | Indexed function `resolve_capability_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:257-265] |
| `resolve_ai_tuning` | function | `pub fn resolve_ai_tuning(source: &mut impl ConfigSource) -> AiTuning {` | `resolve_ai_tuning [function]` | `e25c29fa-fd54-59c8-a411-512026cff2ba` | 268-279 [crates/gcore/src/config/resolve.rs:268-279] | Indexed function `resolve_ai_tuning` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:268-279] |
| `resolve_base_capability_binding` | function | `fn resolve_base_capability_binding(` | `resolve_base_capability_binding [function]` | `54e03bdf-1d5c-5ee0-ad31-8a48ae38e23e` | 281-317 [crates/gcore/src/config/resolve.rs:281-317] | Indexed function `resolve_base_capability_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:281-317] |
| `resolve_audio_translate_binding` | function | `fn resolve_audio_translate_binding(source: &mut impl ConfigSource) -> CapabilityBinding {` | `resolve_audio_translate_binding [function]` | `2a6506bc-efa8-518e-ac69-1e0f2a843422` | 319-341 [crates/gcore/src/config/resolve.rs:319-341] | Indexed function `resolve_audio_translate_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:319-341] |
| `resolve_ai_routing_value` | function | `fn resolve_ai_routing_value(source: &mut impl ConfigSource, config_key: &str) -> Option<AiRouting> {` | `resolve_ai_routing_value [function]` | `13f38e22-9d9a-57a3-89d3-2f989bfdb0f4` | 343-345 [crates/gcore/src/config/resolve.rs:343-345] | Indexed function `resolve_ai_routing_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:343-345] |
| `resolve_ai_config_value` | function | `fn resolve_ai_config_value(source: &mut impl ConfigSource, config_key: &str) -> Option<String> {` | `resolve_ai_config_value [function]` | `4674d845-e391-5592-a870-9070ea857dff` | 347-350 [crates/gcore/src/config/resolve.rs:347-350] | Indexed function `resolve_ai_config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:347-350] |
| `resolve_config_bool` | function | `fn resolve_config_bool(` | `resolve_config_bool [function]` | `14cccc07-ab22-586d-a781-25e8e5a06368` | 352-364 [crates/gcore/src/config/resolve.rs:352-364] | Indexed function `resolve_config_bool` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:352-364] |
| `parse_config_bool_or_default` | function | `fn parse_config_bool_or_default(source_key: &str, value: &str, default: bool) -> bool {` | `parse_config_bool_or_default [function]` | `cbc0cd4c-3885-56e1-ba7a-082d5b0f85c9` | 366-375 [crates/gcore/src/config/resolve.rs:366-375] | Indexed function `parse_config_bool_or_default` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:366-375] |
| `resolve_ai_non_empty` | function | `fn resolve_ai_non_empty(` | `resolve_ai_non_empty [function]` | `4ab9066e-593c-5a15-b28f-d5a743794205` | 382-404 [crates/gcore/src/config/resolve.rs:382-404] | Indexed function `resolve_ai_non_empty` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:382-404] |
| `contains_unresolved_env_pattern` | function | `fn contains_unresolved_env_pattern(value: &str) -> bool {` | `contains_unresolved_env_pattern [function]` | `a968f527-6082-5f78-8b77-eb5ff2928b18` | 406-408 [crates/gcore/src/config/resolve.rs:406-408] | Indexed function `contains_unresolved_env_pattern` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:406-408] |
| `resolve_setting` | function | `fn resolve_setting(` | `resolve_setting [function]` | `2d9eb742-31dc-56dd-8c20-300921ca0ef4` | 410-416 [crates/gcore/src/config/resolve.rs:410-416] | Indexed function `resolve_setting` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:410-416] |
| `resolve_setting_from_keys` | function | `fn resolve_setting_from_keys(` | `resolve_setting_from_keys [function]` | `bf5dbd32-f12c-528b-827c-fd424b368a09` | 418-435 [crates/gcore/src/config/resolve.rs:418-435] | Indexed function `resolve_setting_from_keys` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:418-435] |
| `resolve_port` | function | `fn resolve_port(` | `resolve_port [function]` | `a1ac57e7-05f8-5c88-b49f-f87951768859` | 437-463 [crates/gcore/src/config/resolve.rs:437-463] | Indexed function `resolve_port` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:437-463] |
| `resolve_non_empty` | function | `fn resolve_non_empty(` | `resolve_non_empty [function]` | `a6037978-5cab-5516-be3c-0317da28cd45` | 465-485 [crates/gcore/src/config/resolve.rs:465-485] | Indexed function `resolve_non_empty` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:465-485] |
| `env_value` | function | `fn env_value(key: &str) -> Option<String> {` | `env_value [function]` | `04692329-272a-5687-88a9-ddfd0dc4383d` | 487-491 [crates/gcore/src/config/resolve.rs:487-491] | Indexed function `env_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:487-491] |
