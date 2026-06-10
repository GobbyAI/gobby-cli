---
title: crates/gwiki/src/support/config.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/config.rs
  ranges:
  - 17-20
  - 22-29
  - 23-28
  - 31-35
  - 37-42
  - 45-51
  - 53-60
  - 62-67
  - 69-76
  - 78-85
  - 87-91
  - 93-100
  - 102-117
  - 131-134
  - 136-150
  - 137-149
  - 152-161
  - 153-160
  - 163-169
  - 172-174
  - 176-181
  - 177-180
  - 183-191
  - 184-186
  - 188-190
  - 194-206
  - 209-228
  - 232-250
  - 253-265
  - 269-281
  - 285-312
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/config.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

`crates/gwiki/src/support/config.rs` exposes 31 indexed API symbols.
[crates/gwiki/src/support/config.rs:17-20]
[crates/gwiki/src/support/config.rs:22-29]
[crates/gwiki/src/support/config.rs:23-28]
[crates/gwiki/src/support/config.rs:31-35]
[crates/gwiki/src/support/config.rs:37-42]
[crates/gwiki/src/support/config.rs:45-51]
[crates/gwiki/src/support/config.rs:53-60]
[crates/gwiki/src/support/config.rs:62-67]
[crates/gwiki/src/support/config.rs:69-76]
[crates/gwiki/src/support/config.rs:78-85]
[crates/gwiki/src/support/config.rs:87-91]
[crates/gwiki/src/support/config.rs:93-100]
[crates/gwiki/src/support/config.rs:102-117]
[crates/gwiki/src/support/config.rs:131-134]
[crates/gwiki/src/support/config.rs:136-150]
[crates/gwiki/src/support/config.rs:137-149]
[crates/gwiki/src/support/config.rs:152-161]
[crates/gwiki/src/support/config.rs:153-160]
[crates/gwiki/src/support/config.rs:163-169]
[crates/gwiki/src/support/config.rs:172-174]
[crates/gwiki/src/support/config.rs:176-181]
[crates/gwiki/src/support/config.rs:177-180]
[crates/gwiki/src/support/config.rs:183-191]
[crates/gwiki/src/support/config.rs:184-186]
[crates/gwiki/src/support/config.rs:188-190]
[crates/gwiki/src/support/config.rs:194-206]
[crates/gwiki/src/support/config.rs:209-228]
[crates/gwiki/src/support/config.rs:232-250]
[crates/gwiki/src/support/config.rs:253-265]
[crates/gwiki/src/support/config.rs:269-281]
[crates/gwiki/src/support/config.rs:285-312]

## API Symbols

- `SharedCodeGraphLimits` (class) component `SharedCodeGraphLimits [class]` (`ffa5899d-d273-54b0-ab38-79ab6532b2bb`) lines 17-20 [crates/gwiki/src/support/config.rs:17-20]
  - Signature: `pub(crate) struct SharedCodeGraphLimits {`
  - Purpose: Indexed class `SharedCodeGraphLimits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:17-20]
- `SharedCodeGraphLimits` (class) component `SharedCodeGraphLimits [class]` (`0bd6c9e6-097c-568f-9caf-6f5f4a2d0def`) lines 22-29 [crates/gwiki/src/support/config.rs:22-29]
  - Signature: `impl Default for SharedCodeGraphLimits {`
  - Purpose: Indexed class `SharedCodeGraphLimits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:22-29]
- `SharedCodeGraphLimits.default` (method) component `SharedCodeGraphLimits.default [method]` (`b04c09ab-89c5-594d-8c4b-672c97a634ce`) lines 23-28 [crates/gwiki/src/support/config.rs:23-28]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `SharedCodeGraphLimits.default` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:23-28]
- `local_index_options` (function) component `local_index_options [function]` (`1eda6d02-1fa5-5d69-bb27-294bdeaf70aa`) lines 31-35 [crates/gwiki/src/support/config.rs:31-35]
  - Signature: `pub(crate) fn local_index_options() -> Result<IndexOptions, WikiError> {`
  - Purpose: Indexed function `local_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:31-35]
- `index_options_from_conn` (function) component `index_options_from_conn [function]` (`16b3f22a-23f0-5158-98f3-80f02cbac55f`) lines 37-42 [crates/gwiki/src/support/config.rs:37-42]
  - Signature: `pub(crate) fn index_options_from_conn(conn: &mut Client) -> Result<IndexOptions, WikiError> {`
  - Purpose: Indexed function `index_options_from_conn` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:37-42]
- `local_shared_code_graph_limits` (function) component `local_shared_code_graph_limits [function]` (`42d8a2cb-4641-518e-84b0-13e45e109d00`) lines 45-51 [crates/gwiki/src/support/config.rs:45-51]
  - Signature: `pub(crate) fn local_shared_code_graph_limits() -> Result<SharedCodeGraphLimits, WikiError> {`
  - Purpose: Indexed function `local_shared_code_graph_limits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:45-51]
- `shared_code_graph_limits_from_conn` (function) component `shared_code_graph_limits_from_conn [function]` (`40e90727-f9fd-5938-8725-0f6d40857f33`) lines 53-60 [crates/gwiki/src/support/config.rs:53-60]
  - Signature: `pub(crate) fn shared_code_graph_limits_from_conn(`
  - Purpose: Indexed function `shared_code_graph_limits_from_conn` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:53-60]
- `qdrant_config_has_url` (function) component `qdrant_config_has_url [function]` (`307d488c-ba74-5142-82de-5eb320757836`) lines 62-67 [crates/gwiki/src/support/config.rs:62-67]
  - Signature: `pub(crate) fn qdrant_config_has_url(config: &QdrantConfig) -> bool {`
  - Purpose: Indexed function `qdrant_config_has_url` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:62-67]
- `read_standalone_config` (function) component `read_standalone_config [function]` (`ba7c38b2-b16d-50f8-8bf4-b0d23da13040`) lines 69-76 [crates/gwiki/src/support/config.rs:69-76]
  - Signature: `fn read_standalone_config() -> Result<Option<StandaloneConfig>, WikiError> {`
  - Purpose: Indexed function `read_standalone_config` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:69-76]
- `resolve_index_options` (function) component `resolve_index_options [function]` (`a8d3e8cc-b064-53c2-a44a-64e7c4b1ab9a`) lines 78-85 [crates/gwiki/src/support/config.rs:78-85]
  - Signature: `fn resolve_index_options(`
  - Purpose: Indexed function `resolve_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:78-85]
- `index_options_from_config` (function) component `index_options_from_config [function]` (`3d512a94-9084-5a93-b054-bbc87aed52fe`) lines 87-91 [crates/gwiki/src/support/config.rs:87-91]
  - Signature: `fn index_options_from_config(config: gobby_core::config::IndexingConfig) -> indexer::IndexOptions {`
  - Purpose: Indexed function `index_options_from_config` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:87-91]
- `resolve_shared_code_graph_limits` (function) component `resolve_shared_code_graph_limits [function]` (`26d2526d-de98-529b-ae5f-cc41756e4559`) lines 93-100 [crates/gwiki/src/support/config.rs:93-100]
  - Signature: `fn resolve_shared_code_graph_limits(`
  - Purpose: Indexed function `resolve_shared_code_graph_limits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:93-100]
- `resolve_limit` (function) component `resolve_limit [function]` (`bdc6ce54-eaaf-5226-9a52-7533273b5c01`) lines 102-117 [crates/gwiki/src/support/config.rs:102-117]
  - Signature: `fn resolve_limit(source: &mut impl ConfigSource, key: &'static str) -> Result<usize, WikiError> {`
  - Purpose: Indexed function `resolve_limit` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:102-117]
- `EnvGuard` (class) component `EnvGuard [class]` (`96ae673e-6ab4-5b9f-8c52-17ecc16afb54`) lines 131-134 [crates/gwiki/src/support/config.rs:131-134]
  - Signature: `struct EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:131-134]
- `EnvGuard` (class) component `EnvGuard [class]` (`b676767d-cd66-5192-b811-b4395817b540`) lines 136-150 [crates/gwiki/src/support/config.rs:136-150]
  - Signature: `impl EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:136-150]
- `EnvGuard.set_gobby_home` (method) component `EnvGuard.set_gobby_home [method]` (`52957757-34e4-56a1-bafc-229d38e5c270`) lines 137-149 [crates/gwiki/src/support/config.rs:137-149]
  - Signature: `fn set_gobby_home(path: &Path) -> Self {`
  - Purpose: Indexed method `EnvGuard.set_gobby_home` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:137-149]
- `EnvGuard` (class) component `EnvGuard [class]` (`bc79dfe7-405e-547d-9eb5-20121a8530c3`) lines 152-161 [crates/gwiki/src/support/config.rs:152-161]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:152-161]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`27b360ae-de7c-5ec0-9eb7-4067b6f812c5`) lines 153-160 [crates/gwiki/src/support/config.rs:153-160]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `EnvGuard.drop` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:153-160]
- `write_file` (function) component `write_file [function]` (`d38c4257-cc17-581c-9bb9-29c06576b003`) lines 163-169 [crates/gwiki/src/support/config.rs:163-169]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &str) {`
  - Purpose: Indexed function `write_file` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:163-169]
- `TestSource` (class) component `TestSource [class]` (`7fe5bc6b-cb98-5a58-9154-bfe1cf811c79`) lines 172-174 [crates/gwiki/src/support/config.rs:172-174]
  - Signature: `struct TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:172-174]
- `TestSource` (class) component `TestSource [class]` (`3d2d321f-1dc1-537e-a37a-38200b0453b7`) lines 176-181 [crates/gwiki/src/support/config.rs:176-181]
  - Signature: `impl TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:176-181]
- `TestSource.with` (method) component `TestSource.with [method]` (`53c3b772-1a31-5f18-b743-dc9e98f7e983`) lines 177-180 [crates/gwiki/src/support/config.rs:177-180]
  - Signature: `fn with(mut self, key: &str, value: &str) -> Self {`
  - Purpose: Indexed method `TestSource.with` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:177-180]
- `TestSource` (class) component `TestSource [class]` (`0e534a0e-443c-5651-8918-0389d26e259f`) lines 183-191 [crates/gwiki/src/support/config.rs:183-191]
  - Signature: `impl gobby_core::config::ConfigSource for TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:183-191]
- `TestSource.config_value` (method) component `TestSource.config_value [method]` (`6bc1c131-6a60-5ef3-9128-3215cac5d99f`) lines 184-186 [crates/gwiki/src/support/config.rs:184-186]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed method `TestSource.config_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:184-186]
- `TestSource.resolve_value` (method) component `TestSource.resolve_value [method]` (`11e8d499-3944-5b44-928f-63f38d739bb4`) lines 188-190 [crates/gwiki/src/support/config.rs:188-190]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `TestSource.resolve_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:188-190]
- `shared_code_graph_limits_default_to_200` (function) component `shared_code_graph_limits_default_to_200 [function]` (`57b47df4-03f5-5a87-9df3-301bd01d1dc7`) lines 194-206 [crates/gwiki/src/support/config.rs:194-206]
  - Signature: `fn shared_code_graph_limits_default_to_200() {`
  - Purpose: Indexed function `shared_code_graph_limits_default_to_200` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:194-206]
- `shared_code_graph_limits_use_config_source_over_standalone` (function) component `shared_code_graph_limits_use_config_source_over_standalone [function]` (`e99c6416-d8ea-5df3-b5cf-35b987c417b1`) lines 209-228 [crates/gwiki/src/support/config.rs:209-228]
  - Signature: `fn shared_code_graph_limits_use_config_source_over_standalone() {`
  - Purpose: Indexed function `shared_code_graph_limits_use_config_source_over_standalone` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:209-228]
- `local_shared_code_graph_limits_read_gcore_yaml` (function) component `local_shared_code_graph_limits_read_gcore_yaml [function]` (`afd70b74-3ab9-55bb-af01-3b64da8800f0`) lines 232-250 [crates/gwiki/src/support/config.rs:232-250]
  - Signature: `fn local_shared_code_graph_limits_read_gcore_yaml() {`
  - Purpose: Indexed function `local_shared_code_graph_limits_read_gcore_yaml` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:232-250]
- `shared_code_graph_limits_reject_invalid_or_negative_values` (function) component `shared_code_graph_limits_reject_invalid_or_negative_values [function]` (`20f16aa6-97ae-5411-971b-177524a2cebd`) lines 253-265 [crates/gwiki/src/support/config.rs:253-265]
  - Signature: `fn shared_code_graph_limits_reject_invalid_or_negative_values() {`
  - Purpose: Indexed function `shared_code_graph_limits_reject_invalid_or_negative_values` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:253-265]
- `local_index_options_read_gcore_yaml` (function) component `local_index_options_read_gcore_yaml [function]` (`129019ee-da8b-544a-9574-38e8d372f45c`) lines 269-281 [crates/gwiki/src/support/config.rs:269-281]
  - Signature: `fn local_index_options_read_gcore_yaml() {`
  - Purpose: Indexed function `local_index_options_read_gcore_yaml` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:269-281]
- `memory_indexing_uses_local_index_options` (function) component `memory_indexing_uses_local_index_options [function]` (`a49ec97f-8978-5704-a4a5-a2613b3f1052`) lines 285-312 [crates/gwiki/src/support/config.rs:285-312]
  - Signature: `fn memory_indexing_uses_local_index_options() {`
  - Purpose: Indexed function `memory_indexing_uses_local_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:285-312]

