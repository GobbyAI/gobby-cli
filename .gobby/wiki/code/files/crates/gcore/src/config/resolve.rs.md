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
  - 281-311
  - 313-334
  - 336-338
  - 340-343
  - 345-354
  - 356-362
  - 369-378
  - 380-382
  - 384-390
  - 392-409
  - 411-424
  - 426-434
  - 436-440
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config/resolve.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Purpose

`crates/gcore/src/config/resolve.rs` exposes 34 indexed API symbols.
[crates/gcore/src/config/resolve.rs:11-21]
[crates/gcore/src/config/resolve.rs:24-75]
[crates/gcore/src/config/resolve.rs:78-84]
[crates/gcore/src/config/resolve.rs:87-90]
[crates/gcore/src/config/resolve.rs:93-95]
[crates/gcore/src/config/resolve.rs:103-112]
[crates/gcore/src/config/resolve.rs:114-126]
[crates/gcore/src/config/resolve.rs:130]
[crates/gcore/src/config/resolve.rs:132-143]
[crates/gcore/src/config/resolve.rs:133-135]
[crates/gcore/src/config/resolve.rs:137-142]
[crates/gcore/src/config/resolve.rs:146-165]
[crates/gcore/src/config/resolve.rs:168-174]
[crates/gcore/src/config/resolve.rs:177-179]
[crates/gcore/src/config/resolve.rs:182-189]
[crates/gcore/src/config/resolve.rs:192-202]
[crates/gcore/src/config/resolve.rs:205-240]
[crates/gcore/src/config/resolve.rs:242-244]
[crates/gcore/src/config/resolve.rs:247-254]
[crates/gcore/src/config/resolve.rs:257-265]
[crates/gcore/src/config/resolve.rs:268-279]
[crates/gcore/src/config/resolve.rs:281-311]
[crates/gcore/src/config/resolve.rs:313-334]
[crates/gcore/src/config/resolve.rs:336-338]
[crates/gcore/src/config/resolve.rs:340-343]
[crates/gcore/src/config/resolve.rs:345-354]
[crates/gcore/src/config/resolve.rs:356-362]
[crates/gcore/src/config/resolve.rs:369-378]
[crates/gcore/src/config/resolve.rs:380-382]
[crates/gcore/src/config/resolve.rs:384-390]
[crates/gcore/src/config/resolve.rs:392-409]
[crates/gcore/src/config/resolve.rs:411-424]
[crates/gcore/src/config/resolve.rs:426-434]
[crates/gcore/src/config/resolve.rs:436-440]

## API Symbols

- `decode_config_value` (function) component `decode_config_value [function]` (`ffda9bee-e2b2-5a85-b8a5-d5264597bd68`) lines 11-21 [crates/gcore/src/config/resolve.rs:11-21]
  - Signature: `pub fn decode_config_value(raw: &str) -> Option<String> {`
  - Purpose: Indexed function `decode_config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:11-21]
- `resolve_env_pattern` (function) component `resolve_env_pattern [function]` (`2eda9199-61a3-5764-9294-9e869157122f`) lines 24-75 [crates/gcore/src/config/resolve.rs:24-75]
  - Signature: `pub fn resolve_env_pattern(value: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Indexed function `resolve_env_pattern` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:24-75]
- `ConfigSource` (type) component `ConfigSource [type]` (`e7391422-76ef-5e5a-b8d7-8f4df7c06fc3`) lines 78-84 [crates/gcore/src/config/resolve.rs:78-84]
  - Signature: `pub trait ConfigSource {`
  - Purpose: Indexed type `ConfigSource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:78-84]
- `LayeredConfigSource` (class) component `LayeredConfigSource [class]` (`f22fd710-7880-5444-9a95-6558552726d1`) lines 87-90 [crates/gcore/src/config/resolve.rs:87-90]
  - Signature: `pub struct LayeredConfigSource<P, F> {`
  - Purpose: Indexed class `LayeredConfigSource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:87-90]
- `new` (function) component `new [function]` (`37e2770b-91b5-5149-8ae1-24ee33aae643`) lines 93-95 [crates/gcore/src/config/resolve.rs:93-95]
  - Signature: `pub fn new(primary: Option<P>, fallback: Option<F>) -> Self {`
  - Purpose: Indexed function `new` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:93-95]
- `config_value` (function) component `config_value [function]` (`316b2ec9-f98f-577b-8d0c-0cb02419883e`) lines 103-112 [crates/gcore/src/config/resolve.rs:103-112]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed function `config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:103-112]
- `resolve_value` (function) component `resolve_value [function]` (`221e2b27-32cb-5904-9c9e-0e6dc8a55f48`) lines 114-126 [crates/gcore/src/config/resolve.rs:114-126]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:114-126]
- `EnvOnlySource` (class) component `EnvOnlySource [class]` (`65f10da6-91d2-5593-aea8-550ca546d25b`) lines 130-130 [crates/gcore/src/config/resolve.rs:130]
  - Signature: `pub struct EnvOnlySource;`
  - Purpose: Indexed class `EnvOnlySource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:130]
- `EnvOnlySource` (class) component `EnvOnlySource [class]` (`46035bd8-d162-5096-9c80-2317202dbf62`) lines 132-143 [crates/gcore/src/config/resolve.rs:132-143]
  - Signature: `impl ConfigSource for EnvOnlySource {`
  - Purpose: Indexed class `EnvOnlySource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:132-143]
- `EnvOnlySource.config_value` (method) component `EnvOnlySource.config_value [method]` (`4ebcad6c-2c5b-5f22-9bbe-7bb0f8b2e4f7`) lines 133-135 [crates/gcore/src/config/resolve.rs:133-135]
  - Signature: `fn config_value(&mut self, _key: &str) -> Option<String> {`
  - Purpose: Indexed method `EnvOnlySource.config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:133-135]
- `EnvOnlySource.resolve_value` (method) component `EnvOnlySource.resolve_value [method]` (`64d4252b-1d29-5401-8681-9e1152c1d2be`) lines 137-142 [crates/gcore/src/config/resolve.rs:137-142]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `EnvOnlySource.resolve_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:137-142]
- `resolve_falkordb_config` (function) component `resolve_falkordb_config [function]` (`bbbae36a-fe46-5a54-9443-eead6e94fcb3`) lines 146-165 [crates/gcore/src/config/resolve.rs:146-165]
  - Signature: `pub fn resolve_falkordb_config(source: &mut impl ConfigSource) -> Option<FalkorConfig> {`
  - Purpose: Indexed function `resolve_falkordb_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:146-165]
- `resolve_qdrant_config` (function) component `resolve_qdrant_config [function]` (`6701da20-752e-51c7-a0d9-f8b8018f0974`) lines 168-174 [crates/gcore/src/config/resolve.rs:168-174]
  - Signature: `pub fn resolve_qdrant_config(source: &mut impl ConfigSource) -> Option<QdrantConfig> {`
  - Purpose: Indexed function `resolve_qdrant_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:168-174]
- `resolve_embedding_config` (function) component `resolve_embedding_config [function]` (`e96c2ca2-f13e-5ad1-b605-b8894857bd55`) lines 177-179 [crates/gcore/src/config/resolve.rs:177-179]
  - Signature: `pub fn resolve_embedding_config(source: &mut impl ConfigSource) -> Option<EmbeddingConfig> {`
  - Purpose: Indexed function `resolve_embedding_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:177-179]
- `resolve_indexing_config` (function) component `resolve_indexing_config [function]` (`5206d024-3dbb-5113-b4af-df387497e91d`) lines 182-189 [crates/gcore/src/config/resolve.rs:182-189]
  - Signature: `pub fn resolve_indexing_config(source: &mut impl ConfigSource) -> anyhow::Result<IndexingConfig> {`
  - Purpose: Indexed function `resolve_indexing_config` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:182-189]
- `resolve_embedding_config_resolution` (function) component `resolve_embedding_config_resolution [function]` (`bf8edc06-b676-5f07-b47f-e21a3ac320ea`) lines 192-202 [crates/gcore/src/config/resolve.rs:192-202]
  - Signature: `pub fn resolve_embedding_config_resolution(`
  - Purpose: Indexed function `resolve_embedding_config_resolution` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:192-202]
- `resolve_embedding_config_from_binding` (function) component `resolve_embedding_config_from_binding [function]` (`06b30412-0b2e-5b9f-8660-a0444aa2310f`) lines 205-240 [crates/gcore/src/config/resolve.rs:205-240]
  - Signature: `pub fn resolve_embedding_config_from_binding(`
  - Purpose: Indexed function `resolve_embedding_config_from_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:205-240]
- `resolve_embedding_setting` (function) component `resolve_embedding_setting [function]` (`f572b7cb-acd5-5a5d-8d3d-f503dfa2609f`) lines 242-244 [crates/gcore/src/config/resolve.rs:242-244]
  - Signature: `fn resolve_embedding_setting(source: &mut impl ConfigSource, config_key: &str) -> Option<String> {`
  - Purpose: Indexed function `resolve_embedding_setting` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:242-244]
- `resolve_capability_routing` (function) component `resolve_capability_routing [function]` (`63246edd-b9f1-5f9e-9678-b546fb24f84b`) lines 247-254 [crates/gcore/src/config/resolve.rs:247-254]
  - Signature: `pub fn resolve_capability_routing(`
  - Purpose: Indexed function `resolve_capability_routing` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:247-254]
- `resolve_capability_binding` (function) component `resolve_capability_binding [function]` (`e0d2b5dd-c7ad-55a9-b05d-bdd549988304`) lines 257-265 [crates/gcore/src/config/resolve.rs:257-265]
  - Signature: `pub fn resolve_capability_binding(`
  - Purpose: Indexed function `resolve_capability_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:257-265]
- `resolve_ai_tuning` (function) component `resolve_ai_tuning [function]` (`c6a274d4-e7d3-5445-a13a-9e70ee4bf709`) lines 268-279 [crates/gcore/src/config/resolve.rs:268-279]
  - Signature: `pub fn resolve_ai_tuning(source: &mut impl ConfigSource) -> AiTuning {`
  - Purpose: Indexed function `resolve_ai_tuning` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:268-279]
- `resolve_base_capability_binding` (function) component `resolve_base_capability_binding [function]` (`3b0cfcc9-418e-5055-ae12-653fa5aa1cff`) lines 281-311 [crates/gcore/src/config/resolve.rs:281-311]
  - Signature: `fn resolve_base_capability_binding(`
  - Purpose: Indexed function `resolve_base_capability_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:281-311]
- `resolve_audio_translate_binding` (function) component `resolve_audio_translate_binding [function]` (`b82d91ed-83b2-5ace-b350-6ed0b8f4adb9`) lines 313-334 [crates/gcore/src/config/resolve.rs:313-334]
  - Signature: `fn resolve_audio_translate_binding(source: &mut impl ConfigSource) -> CapabilityBinding {`
  - Purpose: Indexed function `resolve_audio_translate_binding` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:313-334]
- `resolve_ai_routing_value` (function) component `resolve_ai_routing_value [function]` (`12931e0c-462f-5095-bbc7-8fd2fda9dec9`) lines 336-338 [crates/gcore/src/config/resolve.rs:336-338]
  - Signature: `fn resolve_ai_routing_value(source: &mut impl ConfigSource, config_key: &str) -> Option<AiRouting> {`
  - Purpose: Indexed function `resolve_ai_routing_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:336-338]
- `resolve_ai_config_value` (function) component `resolve_ai_config_value [function]` (`3c66acc0-d9db-59f8-8af7-3ae03c40492e`) lines 340-343 [crates/gcore/src/config/resolve.rs:340-343]
  - Signature: `fn resolve_ai_config_value(source: &mut impl ConfigSource, config_key: &str) -> Option<String> {`
  - Purpose: Indexed function `resolve_ai_config_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:340-343]
- `resolve_config_bool` (function) component `resolve_config_bool [function]` (`57af8444-c204-5b4c-859d-deb4343c1417`) lines 345-354 [crates/gcore/src/config/resolve.rs:345-354]
  - Signature: `fn resolve_config_bool(`
  - Purpose: Indexed function `resolve_config_bool` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:345-354]
- `parse_config_bool` (function) component `parse_config_bool [function]` (`5110e6d1-3413-58e8-9aee-637b5bed6fbc`) lines 356-362 [crates/gcore/src/config/resolve.rs:356-362]
  - Signature: `fn parse_config_bool(config_key: &'static str, value: &str) -> anyhow::Result<bool> {`
  - Purpose: Indexed function `parse_config_bool` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:356-362]
- `resolve_ai_non_empty` (function) component `resolve_ai_non_empty [function]` (`1f696bdf-92a9-545b-8c9a-5f000c04a75b`) lines 369-378 [crates/gcore/src/config/resolve.rs:369-378]
  - Signature: `fn resolve_ai_non_empty(source: &mut impl ConfigSource, value: &str) -> Option<String> {`
  - Purpose: Indexed function `resolve_ai_non_empty` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:369-378]
- `contains_unresolved_env_pattern` (function) component `contains_unresolved_env_pattern [function]` (`afbdd894-250e-5062-b969-fe6c296e3e6f`) lines 380-382 [crates/gcore/src/config/resolve.rs:380-382]
  - Signature: `fn contains_unresolved_env_pattern(value: &str) -> bool {`
  - Purpose: Indexed function `contains_unresolved_env_pattern` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:380-382]
- `resolve_setting` (function) component `resolve_setting [function]` (`0fefcdb8-95f2-5150-a95f-d30d7e78031e`) lines 384-390 [crates/gcore/src/config/resolve.rs:384-390]
  - Signature: `fn resolve_setting(`
  - Purpose: Indexed function `resolve_setting` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:384-390]
- `resolve_setting_from_keys` (function) component `resolve_setting_from_keys [function]` (`f72d24ab-e4fc-5c74-ad8f-4a648deca386`) lines 392-409 [crates/gcore/src/config/resolve.rs:392-409]
  - Signature: `fn resolve_setting_from_keys(`
  - Purpose: Indexed function `resolve_setting_from_keys` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:392-409]
- `resolve_port` (function) component `resolve_port [function]` (`61e891a9-f25b-5ab1-b1af-924a75937a93`) lines 411-424 [crates/gcore/src/config/resolve.rs:411-424]
  - Signature: `fn resolve_port(`
  - Purpose: Indexed function `resolve_port` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:411-424]
- `resolve_non_empty` (function) component `resolve_non_empty [function]` (`5d88a0e6-c857-5d5f-9d29-574d8ea33182`) lines 426-434 [crates/gcore/src/config/resolve.rs:426-434]
  - Signature: `fn resolve_non_empty(source: &mut impl ConfigSource, value: &str) -> Option<String> {`
  - Purpose: Indexed function `resolve_non_empty` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:426-434]
- `env_value` (function) component `env_value [function]` (`0c1f7b1f-c5fc-5053-b5f3-ccabc3b20108`) lines 436-440 [crates/gcore/src/config/resolve.rs:436-440]
  - Signature: `fn env_value(key: &str) -> Option<String> {`
  - Purpose: Indexed function `env_value` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:436-440]

