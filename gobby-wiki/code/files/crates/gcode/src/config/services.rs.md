---
title: crates/gcode/src/config/services.rs
type: code_file
provenance:
- file: crates/gcode/src/config/services.rs
  ranges:
  - 20-22
  - 24-27
  - 29-39
  - 41-48
  - 51-57
  - 59-61
  - 64-67
  - 70-81
  - 83-85
  - 89-93
  - 95-99
  - 102-104
  - 108-125
  - 127-129
  - 132-135
  - 138-143
  - 150-162
  - 164-166
  - 169-178
  - 181-196
  - 199-221
  - 226-241
  - 244-247
  - 255-257
  - 259-261
  - 270-276
  - 278-280
  - 284-287
  - 295-301
  - 303-305
  - 309-322
  - 325-338
  - 341-354
  - 357-370
  - 373-384
  - 389-399
  - 401-416
  - 421-431
  - 433-442
  - 444-452
  - 454-469
  - 471-494
  - 501-511
  - 513-533
  - 535-545
  - 547-557
  - 559-568
  - 570-576
  - 578-587
  - 589-603
  - 605-611
  - 613-624
  - 626-635
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/config/services.rs:20-22](crates/gcode/src/config/services.rs#L20-L22), [crates/gcode/src/config/services.rs:24-27](crates/gcode/src/config/services.rs#L24-L27), [crates/gcode/src/config/services.rs:29-39](crates/gcode/src/config/services.rs#L29-L39), [crates/gcode/src/config/services.rs:41-48](crates/gcode/src/config/services.rs#L41-L48), [crates/gcode/src/config/services.rs:51-57](crates/gcode/src/config/services.rs#L51-L57), [crates/gcode/src/config/services.rs:59-61](crates/gcode/src/config/services.rs#L59-L61), [crates/gcode/src/config/services.rs:64-67](crates/gcode/src/config/services.rs#L64-L67), [crates/gcode/src/config/services.rs:70-81](crates/gcode/src/config/services.rs#L70-L81), [crates/gcode/src/config/services.rs:83-85](crates/gcode/src/config/services.rs#L83-L85), [crates/gcode/src/config/services.rs:89-93](crates/gcode/src/config/services.rs#L89-L93), [crates/gcode/src/config/services.rs:95-99](crates/gcode/src/config/services.rs#L95-L99), [crates/gcode/src/config/services.rs:102-104](crates/gcode/src/config/services.rs#L102-L104), [crates/gcode/src/config/services.rs:108-125](crates/gcode/src/config/services.rs#L108-L125), [crates/gcode/src/config/services.rs:127-129](crates/gcode/src/config/services.rs#L127-L129), [crates/gcode/src/config/services.rs:132-135](crates/gcode/src/config/services.rs#L132-L135), [crates/gcode/src/config/services.rs:138-143](crates/gcode/src/config/services.rs#L138-L143), [crates/gcode/src/config/services.rs:150-162](crates/gcode/src/config/services.rs#L150-L162), [crates/gcode/src/config/services.rs:164-166](crates/gcode/src/config/services.rs#L164-L166), [crates/gcode/src/config/services.rs:169-178](crates/gcode/src/config/services.rs#L169-L178), [crates/gcode/src/config/services.rs:181-196](crates/gcode/src/config/services.rs#L181-L196), [crates/gcode/src/config/services.rs:199-221](crates/gcode/src/config/services.rs#L199-L221), [crates/gcode/src/config/services.rs:226-241](crates/gcode/src/config/services.rs#L226-L241), [crates/gcode/src/config/services.rs:244-247](crates/gcode/src/config/services.rs#L244-L247), [crates/gcode/src/config/services.rs:255-257](crates/gcode/src/config/services.rs#L255-L257), [crates/gcode/src/config/services.rs:259-261](crates/gcode/src/config/services.rs#L259-L261), [crates/gcode/src/config/services.rs:270-276](crates/gcode/src/config/services.rs#L270-L276), [crates/gcode/src/config/services.rs:278-280](crates/gcode/src/config/services.rs#L278-L280), [crates/gcode/src/config/services.rs:284-287](crates/gcode/src/config/services.rs#L284-L287), [crates/gcode/src/config/services.rs:295-301](crates/gcode/src/config/services.rs#L295-L301), [crates/gcode/src/config/services.rs:303-305](crates/gcode/src/config/services.rs#L303-L305), [crates/gcode/src/config/services.rs:309-322](crates/gcode/src/config/services.rs#L309-L322), [crates/gcode/src/config/services.rs:325-338](crates/gcode/src/config/services.rs#L325-L338), [crates/gcode/src/config/services.rs:341-354](crates/gcode/src/config/services.rs#L341-L354), [crates/gcode/src/config/services.rs:357-370](crates/gcode/src/config/services.rs#L357-L370), [crates/gcode/src/config/services.rs:373-384](crates/gcode/src/config/services.rs#L373-L384), [crates/gcode/src/config/services.rs:389-399](crates/gcode/src/config/services.rs#L389-L399), [crates/gcode/src/config/services.rs:401-416](crates/gcode/src/config/services.rs#L401-L416), [crates/gcode/src/config/services.rs:421-431](crates/gcode/src/config/services.rs#L421-L431), [crates/gcode/src/config/services.rs:433-442](crates/gcode/src/config/services.rs#L433-L442), [crates/gcode/src/config/services.rs:444-452](crates/gcode/src/config/services.rs#L444-L452), [crates/gcode/src/config/services.rs:454-469](crates/gcode/src/config/services.rs#L454-L469), [crates/gcode/src/config/services.rs:471-494](crates/gcode/src/config/services.rs#L471-L494), [crates/gcode/src/config/services.rs:501-511](crates/gcode/src/config/services.rs#L501-L511), [crates/gcode/src/config/services.rs:513-533](crates/gcode/src/config/services.rs#L513-L533), [crates/gcode/src/config/services.rs:535-545](crates/gcode/src/config/services.rs#L535-L545), [crates/gcode/src/config/services.rs:547-557](crates/gcode/src/config/services.rs#L547-L557), [crates/gcode/src/config/services.rs:559-568](crates/gcode/src/config/services.rs#L559-L568), [crates/gcode/src/config/services.rs:570-576](crates/gcode/src/config/services.rs#L570-L576), [crates/gcode/src/config/services.rs:578-587](crates/gcode/src/config/services.rs#L578-L587), [crates/gcode/src/config/services.rs:589-603](crates/gcode/src/config/services.rs#L589-L603), [crates/gcode/src/config/services.rs:605-611](crates/gcode/src/config/services.rs#L605-L611), [crates/gcode/src/config/services.rs:613-624](crates/gcode/src/config/services.rs#L613-L624), [crates/gcode/src/config/services.rs:626-635](crates/gcode/src/config/services.rs#L626-L635)

</details>

# crates/gcode/src/config/services.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Provides the service-configuration layer for Gobby, resolving runtime settings from Postgres-backed config, environment variables, standalone config files, and fallbacks. The file defines a small `ServiceConfigSource` abstraction plus concrete sources and helpers that read raw values, detect missing config stores, resolve secret references, and then assemble validated service configs for FalkorDB, Qdrant, embeddings, code-vector settings, and indexing, including parsing and normalization such as ports and vector dimensions.
[crates/gcode/src/config/services.rs:20-22]
[crates/gcode/src/config/services.rs:24-27]
[crates/gcode/src/config/services.rs:29-39]
[crates/gcode/src/config/services.rs:41-48]
[crates/gcode/src/config/services.rs:51-57]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `PostgresConfigSource` | class | `struct PostgresConfigSource<'a> {` | `PostgresConfigSource [class]` | `2b5627ba-b022-5c99-835a-10b3270e595a` | 20-22 [crates/gcode/src/config/services.rs:20-22] | Indexed class `PostgresConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:20-22] |
| `ServiceConfigSource` | type | `trait ServiceConfigSource {` | `ServiceConfigSource [type]` | `376426c5-af74-5515-b43e-71c79b27ab8e` | 24-27 [crates/gcode/src/config/services.rs:24-27] | Indexed type `ServiceConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:24-27] |
| `service_env_value` | function | `fn service_env_value(key: &str) -> Option<String> {` | `service_env_value [function]` | `8c73cf1c-116b-549f-a285-656fb12318b7` | 29-39 [crates/gcode/src/config/services.rs:29-39] | Indexed function `service_env_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:29-39] |
| `config_store_missing` | function | `fn config_store_missing(error: &anyhow::Error) -> bool {` | `config_store_missing [function]` | `a1772b25-eb88-5555-acb1-3c9813b557a8` | 41-48 [crates/gcode/src/config/services.rs:41-48] | Indexed function `config_store_missing` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:41-48] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> anyhow::Result<Option<String>> {` | `config_value [function]` | `80bdc425-dbd1-58ce-b569-e6e623d260d5` | 51-57 [crates/gcode/src/config/services.rs:51-57] | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:51-57] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `802f41f9-6958-57bc-9239-5b29484e96c1` | 59-61 [crates/gcode/src/config/services.rs:59-61] | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:59-61] |
| `FallbackConfigSource` | class | `struct FallbackConfigSource<'a> {` | `FallbackConfigSource [class]` | `2b6de914-554a-5521-85c1-34566ed0e76f` | 64-67 [crates/gcode/src/config/services.rs:64-67] | Indexed class `FallbackConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:64-67] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> anyhow::Result<Option<String>> {` | `config_value [function]` | `3308f5d4-fe0e-5ddd-86b0-1a239ad5cbc4` | 70-81 [crates/gcode/src/config/services.rs:70-81] | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:70-81] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `195d3c75-4fd1-5d55-a58d-080bc7eadcdc` | 83-85 [crates/gcode/src/config/services.rs:83-85] | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:83-85] |
| `EmbeddingConfigDetails` | class | `pub(crate) struct EmbeddingConfigDetails {` | `EmbeddingConfigDetails [class]` | `bb3b2b04-75d3-55ea-8326-7ed800d721f2` | 89-93 [crates/gcode/src/config/services.rs:89-93] | Indexed class `EmbeddingConfigDetails` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:89-93] |
| `TracingFallbackConfigSource` | class | `struct TracingFallbackConfigSource<'a> {` | `TracingFallbackConfigSource [class]` | `f7c3b020-528e-516b-9c1d-e31527b7bc42` | 95-99 [crates/gcode/src/config/services.rs:95-99] | Indexed class `TracingFallbackConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:95-99] |
| `hit_source` | function | `fn hit_source(&self, key: &str) -> Option<&'static str> {` | `hit_source [function]` | `2fb164b7-eb7d-54c7-bd56-0099afebd78b` | 102-104 [crates/gcode/src/config/services.rs:102-104] | Indexed function `hit_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:102-104] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> anyhow::Result<Option<String>> {` | `config_value [function]` | `481ab8e0-920d-5092-82f8-60e726ec5b68` | 108-125 [crates/gcode/src/config/services.rs:108-125] | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:108-125] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `f022087b-8ec1-5b21-933f-28275f1a9573` | 127-129 [crates/gcode/src/config/services.rs:127-129] | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:127-129] |
| `ErrorCapturingConfigSource` | class | `struct ErrorCapturingConfigSource<'a, S> {` | `ErrorCapturingConfigSource [class]` | `59d8cbb2-3be8-53e7-abbb-6ec9ef356504` | 132-135 [crates/gcode/src/config/services.rs:132-135] | Indexed class `ErrorCapturingConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:132-135] |
| `finish` | function | `fn finish<T>(self, value: T) -> anyhow::Result<T> {` | `finish [function]` | `000f4592-81ca-57d8-9950-f933ff4a3b5b` | 138-143 [crates/gcode/src/config/services.rs:138-143] | Indexed function `finish` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:138-143] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> Option<String> {` | `config_value [function]` | `d72d83bd-5aba-5c26-9d16-8cf00cb01d4c` | 150-162 [crates/gcode/src/config/services.rs:150-162] | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:150-162] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `8dad6043-0fc8-5236-8061-0fc3a429e032` | 164-166 [crates/gcode/src/config/services.rs:164-166] | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:164-166] |
| `read_standalone_config_optional` | function | `pub(crate) fn read_standalone_config_optional() -> Option<StandaloneConfig> {` | `read_standalone_config_optional [function]` | `8331635c-e2f7-5a97-9965-1d6d996826fe` | 169-178 [crates/gcode/src/config/services.rs:169-178] | Indexed function `read_standalone_config_optional` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:169-178] |
| `StandaloneConfigReadError` | type | `pub(crate) enum StandaloneConfigReadError {` | `StandaloneConfigReadError [type]` | `254de7ef-9797-5f6a-9ca7-c0aa8622aaaa` | 181-196 [crates/gcode/src/config/services.rs:181-196] | Indexed type `StandaloneConfigReadError` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:181-196] |
| `StandaloneConfigReadError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `StandaloneConfigReadError::fmt [method]` | `da9d2337-c68c-5956-836f-8bf397465272` | 199-221 [crates/gcode/src/config/services.rs:199-221] | Indexed method `StandaloneConfigReadError::fmt` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:199-221] |
| `read_standalone_config` | function | `pub(crate) fn read_standalone_config() -> Result<StandaloneConfig, StandaloneConfigReadError> {` | `read_standalone_config [function]` | `8eb27418-fb2b-5858-97d5-ecd8a1d2c31d` | 226-241 [crates/gcode/src/config/services.rs:226-241] | Indexed function `read_standalone_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:226-241] |
| `ClosureConfigSource` | class | `struct ClosureConfigSource<R, S> {` | `ClosureConfigSource [class]` | `5e91dc97-455d-5172-9d43-060d723ef1b0` | 244-247 [crates/gcode/src/config/services.rs:244-247] | Indexed class `ClosureConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:244-247] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> Option<String> {` | `config_value [function]` | `4b90bf43-1cac-5d65-8f5e-0f85ba3713e2` | 255-257 [crates/gcode/src/config/services.rs:255-257] | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:255-257] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `e9344c04-d2a9-5560-b9ea-55e565b88e79` | 259-261 [crates/gcode/src/config/services.rs:259-261] | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:259-261] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> anyhow::Result<Option<String>> {` | `config_value [function]` | `1c0fa5fa-a8b0-5b8b-8d48-e43da3c43b16` | 270-276 [crates/gcode/src/config/services.rs:270-276] | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:270-276] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `d727e622-20ad-5169-8567-28f4c0624627` | 278-280 [crates/gcode/src/config/services.rs:278-280] | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:278-280] |
| `FallibleClosureConfigSource` | class | `struct FallibleClosureConfigSource<R, S> {` | `FallibleClosureConfigSource [class]` | `dbbe6486-153b-5779-9a08-bd7aa071b2bd` | 284-287 [crates/gcode/src/config/services.rs:284-287] | Indexed class `FallibleClosureConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:284-287] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> anyhow::Result<Option<String>> {` | `config_value [function]` | `d2fc1ff4-a198-505e-af3e-b2a9ef8899d1` | 295-301 [crates/gcode/src/config/services.rs:295-301] | Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:295-301] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `0e207cc9-a653-5aea-ba44-60ecfbfed306` | 303-305 [crates/gcode/src/config/services.rs:303-305] | Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:303-305] |
| `resolve_falkordb_config_from_values` | function | `pub(super) fn resolve_falkordb_config_from_values<R, S>(` | `resolve_falkordb_config_from_values [function]` | `cc9828a3-8814-52a1-b87c-59e38dc98650` | 309-322 [crates/gcode/src/config/services.rs:309-322] | Indexed function `resolve_falkordb_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:309-322] |
| `resolve_qdrant_config_from_values` | function | `pub(super) fn resolve_qdrant_config_from_values<R, S>(` | `resolve_qdrant_config_from_values [function]` | `9aba8a5f-536d-5453-b5ce-7771f6fb29e8` | 325-338 [crates/gcode/src/config/services.rs:325-338] | Indexed function `resolve_qdrant_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:325-338] |
| `resolve_embedding_config_from_values` | function | `pub(super) fn resolve_embedding_config_from_values<R, S>(` | `resolve_embedding_config_from_values [function]` | `9330a412-575b-5152-a1cf-135a7f308e3a` | 341-354 [crates/gcode/src/config/services.rs:341-354] | Indexed function `resolve_embedding_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:341-354] |
| `resolve_embedding_config_from_fallible_values` | function | `pub(super) fn resolve_embedding_config_from_fallible_values<R, S>(` | `resolve_embedding_config_from_fallible_values [function]` | `e103c19a-2c6c-527b-9159-a254b6795001` | 357-370 [crates/gcode/src/config/services.rs:357-370] | Indexed function `resolve_embedding_config_from_fallible_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:357-370] |
| `resolve_code_vector_settings_from_values` | function | `pub(super) fn resolve_code_vector_settings_from_values<R>(` | `resolve_code_vector_settings_from_values [function]` | `c13ee5b5-4dea-5d41-a3c4-6e3f6ec63209` | 373-384 [crates/gcode/src/config/services.rs:373-384] | Indexed function `resolve_code_vector_settings_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:373-384] |
| `resolve_falkordb_config` | function | `pub(super) fn resolve_falkordb_config(` | `resolve_falkordb_config [function]` | `c5730274-e339-57fc-bc15-d5abfecf7c0f` | 389-399 [crates/gcode/src/config/services.rs:389-399] | Indexed function `resolve_falkordb_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:389-399] |
| `resolve_falkordb_config_from_source` | function | `fn resolve_falkordb_config_from_source(` | `resolve_falkordb_config_from_source [function]` | `1f13e8b8-ed66-50e9-99cf-6e6a742d4c0c` | 401-416 [crates/gcode/src/config/services.rs:401-416] | Indexed function `resolve_falkordb_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:401-416] |
| `resolve_qdrant_config` | function | `pub(super) fn resolve_qdrant_config(` | `resolve_qdrant_config [function]` | `a4e3d0c0-846c-53fa-adc2-c86422c8ebb6` | 421-431 [crates/gcode/src/config/services.rs:421-431] | Indexed function `resolve_qdrant_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:421-431] |
| `resolve_qdrant_config_from_source` | function | `fn resolve_qdrant_config_from_source(` | `resolve_qdrant_config_from_source [function]` | `bdf63c4f-b439-55e6-b850-a837b76becdb` | 433-442 [crates/gcode/src/config/services.rs:433-442] | Indexed function `resolve_qdrant_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:433-442] |
| `resolve_service_setting` | function | `fn resolve_service_setting(` | `resolve_service_setting [function]` | `a5a01ca9-8086-52b4-97c9-132d324c6f85` | 444-452 [crates/gcode/src/config/services.rs:444-452] | Indexed function `resolve_service_setting` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:444-452] |
| `resolve_service_non_empty` | function | `fn resolve_service_non_empty(` | `resolve_service_non_empty [function]` | `c90f25cf-fbe0-5ed0-b097-77ef348556d1` | 454-469 [crates/gcode/src/config/services.rs:454-469] | Indexed function `resolve_service_non_empty` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:454-469] |
| `resolve_service_port` | function | `fn resolve_service_port(` | `resolve_service_port [function]` | `9138da44-4687-593a-95c5-29b8cbd7391a` | 471-494 [crates/gcode/src/config/services.rs:471-494] | Indexed function `resolve_service_port` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:471-494] |
| `resolve_embedding_config` | function | `pub(super) fn resolve_embedding_config(` | `resolve_embedding_config [function]` | `025b4846-7970-5700-99f0-0ccabc7ebfc4` | 501-511 [crates/gcode/src/config/services.rs:501-511] | Indexed function `resolve_embedding_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:501-511] |
| `resolve_embedding_config_details` | function | `pub(crate) fn resolve_embedding_config_details(` | `resolve_embedding_config_details [function]` | `b0c9bb0b-c7a0-5542-bd3c-95f25dd812df` | 513-533 [crates/gcode/src/config/services.rs:513-533] | Indexed function `resolve_embedding_config_details` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:513-533] |
| `resolve_embedding_config_from_service_source` | function | `fn resolve_embedding_config_from_service_source(` | `resolve_embedding_config_from_service_source [function]` | `ac53669b-29ee-5344-acd8-336ad0104d53` | 535-545 [crates/gcode/src/config/services.rs:535-545] | Indexed function `resolve_embedding_config_from_service_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:535-545] |
| `resolve_embedding_config_from_source` | function | `pub(crate) fn resolve_embedding_config_from_source(` | `resolve_embedding_config_from_source [function]` | `28c47d46-bd7b-5133-b7c7-372cfc12895e` | 547-557 [crates/gcode/src/config/services.rs:547-557] | Indexed function `resolve_embedding_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:547-557] |
| `embedding_binding_routes_direct` | function | `fn embedding_binding_routes_direct(binding: &CapabilityBinding) -> bool {` | `embedding_binding_routes_direct [function]` | `73a8e787-c170-5e1d-82eb-c9430da704fd` | 559-568 [crates/gcode/src/config/services.rs:559-568] | Indexed function `embedding_binding_routes_direct` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:559-568] |
| `embedding_binding_uses_openai_http` | function | `fn embedding_binding_uses_openai_http(binding: &CapabilityBinding) -> bool {` | `embedding_binding_uses_openai_http [function]` | `43346b4a-a439-52fb-b995-db9d5f53bc03` | 570-576 [crates/gcode/src/config/services.rs:570-576] | Indexed function `embedding_binding_uses_openai_http` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:570-576] |
| `resolve_code_vector_settings` | function | `pub(super) fn resolve_code_vector_settings(` | `resolve_code_vector_settings [function]` | `3a3fcf9e-3bc0-592a-936a-6c4014fc535f` | 578-587 [crates/gcode/src/config/services.rs:578-587] | Indexed function `resolve_code_vector_settings` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:578-587] |
| `resolve_indexing_settings` | function | `pub(super) fn resolve_indexing_settings(` | `resolve_indexing_settings [function]` | `89da399d-3b25-55ce-a12e-30c060540b8c` | 589-603 [crates/gcode/src/config/services.rs:589-603] | Indexed function `resolve_indexing_settings` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:589-603] |
| `resolve_code_vector_settings_from_source` | function | `fn resolve_code_vector_settings_from_source(` | `resolve_code_vector_settings_from_source [function]` | `a3104df3-262f-55d2-b96d-e90615651334` | 605-611 [crates/gcode/src/config/services.rs:605-611] | Indexed function `resolve_code_vector_settings_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:605-611] |
| `resolve_vector_dim` | function | `fn resolve_vector_dim(` | `resolve_vector_dim [function]` | `6b815bbb-2a31-5fae-9311-56606fe1ad6b` | 613-624 [crates/gcode/src/config/services.rs:613-624] | Indexed function `resolve_vector_dim` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:613-624] |
| `parse_vector_dim` | function | `fn parse_vector_dim(source: &'static str, value: &str) -> Result<usize, CodeVectorConfigError> {` | `parse_vector_dim [function]` | `688cb87e-bc31-5fda-a82d-3fd925232ac4` | 626-635 [crates/gcode/src/config/services.rs:626-635] | Indexed function `parse_vector_dim` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:626-635] |
