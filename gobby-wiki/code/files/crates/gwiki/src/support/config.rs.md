---
title: crates/gwiki/src/support/config.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/config.rs
  ranges:
  - 18-20
  - 23-29
  - 31-43
  - 46-61
  - 68-71
  - 74-79
  - 82-86
  - 88-93
  - 96-102
  - 104-111
  - 113-118
  - 120-127
  - 129-136
  - 138-142
  - 144-151
  - 153-168
  - 182-185
  - 188-200
  - 204-211
  - 214-220
  - 223-225
  - 228-231
  - 235-237
  - 239-241
  - 245-257
  - 260-279
  - 283-301
  - 304-316
  - 320-332
  - 336-363
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/config.rs:18-20](crates/gwiki/src/support/config.rs#L18-L20), [crates/gwiki/src/support/config.rs:23-29](crates/gwiki/src/support/config.rs#L23-L29), [crates/gwiki/src/support/config.rs:31-43](crates/gwiki/src/support/config.rs#L31-L43), [crates/gwiki/src/support/config.rs:46-61](crates/gwiki/src/support/config.rs#L46-L61), [crates/gwiki/src/support/config.rs:68-71](crates/gwiki/src/support/config.rs#L68-L71), [crates/gwiki/src/support/config.rs:74-79](crates/gwiki/src/support/config.rs#L74-L79), [crates/gwiki/src/support/config.rs:82-86](crates/gwiki/src/support/config.rs#L82-L86), [crates/gwiki/src/support/config.rs:88-93](crates/gwiki/src/support/config.rs#L88-L93), [crates/gwiki/src/support/config.rs:96-102](crates/gwiki/src/support/config.rs#L96-L102), [crates/gwiki/src/support/config.rs:104-111](crates/gwiki/src/support/config.rs#L104-L111), [crates/gwiki/src/support/config.rs:113-118](crates/gwiki/src/support/config.rs#L113-L118), [crates/gwiki/src/support/config.rs:120-127](crates/gwiki/src/support/config.rs#L120-L127), [crates/gwiki/src/support/config.rs:129-136](crates/gwiki/src/support/config.rs#L129-L136), [crates/gwiki/src/support/config.rs:138-142](crates/gwiki/src/support/config.rs#L138-L142), [crates/gwiki/src/support/config.rs:144-151](crates/gwiki/src/support/config.rs#L144-L151), [crates/gwiki/src/support/config.rs:153-168](crates/gwiki/src/support/config.rs#L153-L168), [crates/gwiki/src/support/config.rs:182-185](crates/gwiki/src/support/config.rs#L182-L185), [crates/gwiki/src/support/config.rs:188-200](crates/gwiki/src/support/config.rs#L188-L200), [crates/gwiki/src/support/config.rs:204-211](crates/gwiki/src/support/config.rs#L204-L211), [crates/gwiki/src/support/config.rs:214-220](crates/gwiki/src/support/config.rs#L214-L220), [crates/gwiki/src/support/config.rs:223-225](crates/gwiki/src/support/config.rs#L223-L225), [crates/gwiki/src/support/config.rs:228-231](crates/gwiki/src/support/config.rs#L228-L231), [crates/gwiki/src/support/config.rs:235-237](crates/gwiki/src/support/config.rs#L235-L237), [crates/gwiki/src/support/config.rs:239-241](crates/gwiki/src/support/config.rs#L239-L241), [crates/gwiki/src/support/config.rs:245-257](crates/gwiki/src/support/config.rs#L245-L257), [crates/gwiki/src/support/config.rs:260-279](crates/gwiki/src/support/config.rs#L260-L279), [crates/gwiki/src/support/config.rs:283-301](crates/gwiki/src/support/config.rs#L283-L301), [crates/gwiki/src/support/config.rs:304-316](crates/gwiki/src/support/config.rs#L304-L316), [crates/gwiki/src/support/config.rs:320-332](crates/gwiki/src/support/config.rs#L320-L332), [crates/gwiki/src/support/config.rs:336-363](crates/gwiki/src/support/config.rs#L336-L363)

</details>

# crates/gwiki/src/support/config.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file centralizes GWiki configuration resolution. It defines `HubPrimary`, a `ConfigSource` that reads config and resolves secret-backed values through a PostgreSQL hub when available, and `hub_ai_config_source`, which builds an AI config source from Gobby home plus an optional database connection. It also provides defaults and resolution helpers for shared code graph and indexing settings, including logic to read local `gcore.yaml`, prefer config over standalone defaults, and validate or clamp limit values. The remaining pieces are test/support utilities: `EnvGuard` and `write_file` manage temporary Gobby home state, while `TestSource` supplies a controllable `ConfigSource` for tests that verify defaults, precedence, YAML loading, and rejection of invalid limits.
[crates/gwiki/src/support/config.rs:18-20]
[crates/gwiki/src/support/config.rs:23-29]
[crates/gwiki/src/support/config.rs:31-43]
[crates/gwiki/src/support/config.rs:46-61]
[crates/gwiki/src/support/config.rs:68-71]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `HubPrimary` | class | `pub(crate) struct HubPrimary {` | `HubPrimary [class]` | `bf09877f-8772-5b79-a0ea-177a058fea73` | 18-20 [crates/gwiki/src/support/config.rs:18-20] | Indexed class `HubPrimary` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:18-20] |
| `HubPrimary::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `HubPrimary::config_value [method]` | `46a3fb54-b9ad-5717-be8e-31b1ea45da5f` | 23-29 [crates/gwiki/src/support/config.rs:23-29] | Indexed method `HubPrimary::config_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:23-29] |
| `HubPrimary::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `HubPrimary::resolve_value [method]` | `7e81b3d9-3fd8-5dce-b466-5aa424f98ba2` | 31-43 [crates/gwiki/src/support/config.rs:31-43] | Indexed method `HubPrimary::resolve_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:31-43] |
| `hub_ai_config_source` | function | `pub(crate) fn hub_ai_config_source(` | `hub_ai_config_source [function]` | `03673ec0-e042-5ecb-8465-83e2e29b50c4` | 46-61 [crates/gwiki/src/support/config.rs:46-61] | Indexed function `hub_ai_config_source` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:46-61] |
| `SharedCodeGraphLimits` | class | `pub(crate) struct SharedCodeGraphLimits {` | `SharedCodeGraphLimits [class]` | `faa4c6ea-6b38-5a26-b2f0-43a0a74136be` | 68-71 [crates/gwiki/src/support/config.rs:68-71] | Indexed class `SharedCodeGraphLimits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:68-71] |
| `SharedCodeGraphLimits::default` | method | `fn default() -> Self {` | `SharedCodeGraphLimits::default [method]` | `fe650e09-8172-5b62-82ad-66fb771a5059` | 74-79 [crates/gwiki/src/support/config.rs:74-79] | Indexed method `SharedCodeGraphLimits::default` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:74-79] |
| `local_index_options` | function | `pub(crate) fn local_index_options() -> Result<IndexOptions, WikiError> {` | `local_index_options [function]` | `410c7d5e-0ab7-5e59-965c-ebac3fe2d0a2` | 82-86 [crates/gwiki/src/support/config.rs:82-86] | Indexed function `local_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:82-86] |
| `index_options_from_conn` | function | `pub(crate) fn index_options_from_conn(conn: &mut Client) -> Result<IndexOptions, WikiError> {` | `index_options_from_conn [function]` | `f55cd370-a57f-5a75-a653-96990fbd8c19` | 88-93 [crates/gwiki/src/support/config.rs:88-93] | Indexed function `index_options_from_conn` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:88-93] |
| `local_shared_code_graph_limits` | function | `pub(crate) fn local_shared_code_graph_limits() -> Result<SharedCodeGraphLimits, WikiError> {` | `local_shared_code_graph_limits [function]` | `60853d35-bf82-58e6-ad93-cc1f079f8d0d` | 96-102 [crates/gwiki/src/support/config.rs:96-102] | Indexed function `local_shared_code_graph_limits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:96-102] |
| `shared_code_graph_limits_from_conn` | function | `pub(crate) fn shared_code_graph_limits_from_conn(` | `shared_code_graph_limits_from_conn [function]` | `d61deee2-96f4-5fde-ace0-2f4e6cd04042` | 104-111 [crates/gwiki/src/support/config.rs:104-111] | Indexed function `shared_code_graph_limits_from_conn` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:104-111] |
| `qdrant_config_has_url` | function | `pub(crate) fn qdrant_config_has_url(config: &QdrantConfig) -> bool {` | `qdrant_config_has_url [function]` | `d63925a8-cd8e-5d7e-82ab-f08e1213999a` | 113-118 [crates/gwiki/src/support/config.rs:113-118] | Indexed function `qdrant_config_has_url` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:113-118] |
| `read_standalone_config` | function | `fn read_standalone_config() -> Result<Option<StandaloneConfig>, WikiError> {` | `read_standalone_config [function]` | `fbc1bd41-cbfc-577a-aabe-3bcc8801eb76` | 120-127 [crates/gwiki/src/support/config.rs:120-127] | Indexed function `read_standalone_config` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:120-127] |
| `resolve_index_options` | function | `fn resolve_index_options(` | `resolve_index_options [function]` | `c35262bf-e907-56e5-a22b-192bcc35ddcf` | 129-136 [crates/gwiki/src/support/config.rs:129-136] | Indexed function `resolve_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:129-136] |
| `index_options_from_config` | function | `fn index_options_from_config(config: gobby_core::config::IndexingConfig) -> indexer::IndexOptions {` | `index_options_from_config [function]` | `8f6696ea-2c91-51c7-8c27-d72238555df6` | 138-142 [crates/gwiki/src/support/config.rs:138-142] | Indexed function `index_options_from_config` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:138-142] |
| `resolve_shared_code_graph_limits` | function | `fn resolve_shared_code_graph_limits(` | `resolve_shared_code_graph_limits [function]` | `d0057609-80cc-5913-9b05-63a231f0a13e` | 144-151 [crates/gwiki/src/support/config.rs:144-151] | Indexed function `resolve_shared_code_graph_limits` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:144-151] |
| `resolve_limit` | function | `fn resolve_limit(source: &mut impl ConfigSource, key: &'static str) -> Result<usize, WikiError> {` | `resolve_limit [function]` | `fef1c01e-4e64-5064-9a84-fedd43d43c67` | 153-168 [crates/gwiki/src/support/config.rs:153-168] | Indexed function `resolve_limit` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:153-168] |
| `EnvGuard` | class | `struct EnvGuard {` | `EnvGuard [class]` | `9b254d32-ba5e-511e-933d-54eb161a4d0d` | 182-185 [crates/gwiki/src/support/config.rs:182-185] | Indexed class `EnvGuard` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:182-185] |
| `EnvGuard::set_gobby_home` | method | `fn set_gobby_home(path: &Path) -> Self {` | `EnvGuard::set_gobby_home [method]` | `7d7aa43d-75b2-5e0a-8631-f66e995e198d` | 188-200 [crates/gwiki/src/support/config.rs:188-200] | Indexed method `EnvGuard::set_gobby_home` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:188-200] |
| `EnvGuard::drop` | method | `fn drop(&mut self) {` | `EnvGuard::drop [method]` | `562394c7-f0b4-5683-a08e-78c1833110e3` | 204-211 [crates/gwiki/src/support/config.rs:204-211] | Indexed method `EnvGuard::drop` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:204-211] |
| `write_file` | function | `fn write_file(root: &Path, rel: &str, contents: &str) {` | `write_file [function]` | `162348de-8b35-5292-872d-aae9d34f1e6a` | 214-220 [crates/gwiki/src/support/config.rs:214-220] | Indexed function `write_file` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:214-220] |
| `TestSource` | class | `struct TestSource {` | `TestSource [class]` | `6ce590b9-9982-5fc5-bba7-38ce4f07de55` | 223-225 [crates/gwiki/src/support/config.rs:223-225] | Indexed class `TestSource` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:223-225] |
| `TestSource::with` | method | `fn with(mut self, key: &str, value: &str) -> Self {` | `TestSource::with [method]` | `bbe05f32-4c07-5393-aa0e-c64985500da8` | 228-231 [crates/gwiki/src/support/config.rs:228-231] | Indexed method `TestSource::with` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:228-231] |
| `TestSource::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `TestSource::config_value [method]` | `a3921349-05db-58ca-aaf4-ca8caa1c947f` | 235-237 [crates/gwiki/src/support/config.rs:235-237] | Indexed method `TestSource::config_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:235-237] |
| `TestSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `TestSource::resolve_value [method]` | `18816624-9bb0-5bf6-92ae-cca2b4841b3e` | 239-241 [crates/gwiki/src/support/config.rs:239-241] | Indexed method `TestSource::resolve_value` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:239-241] |
| `shared_code_graph_limits_default_to_200` | function | `fn shared_code_graph_limits_default_to_200() {` | `shared_code_graph_limits_default_to_200 [function]` | `f1646dc9-8c4c-58f1-9150-c0f8cce540f5` | 245-257 [crates/gwiki/src/support/config.rs:245-257] | Indexed function `shared_code_graph_limits_default_to_200` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:245-257] |
| `shared_code_graph_limits_use_config_source_over_standalone` | function | `fn shared_code_graph_limits_use_config_source_over_standalone() {` | `shared_code_graph_limits_use_config_source_over_standalone [function]` | `cc49d970-fc85-595f-aae5-63d7e1050965` | 260-279 [crates/gwiki/src/support/config.rs:260-279] | Indexed function `shared_code_graph_limits_use_config_source_over_standalone` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:260-279] |
| `local_shared_code_graph_limits_read_gcore_yaml` | function | `fn local_shared_code_graph_limits_read_gcore_yaml() {` | `local_shared_code_graph_limits_read_gcore_yaml [function]` | `78da5e83-3767-5309-8c31-229eca2daee8` | 283-301 [crates/gwiki/src/support/config.rs:283-301] | Indexed function `local_shared_code_graph_limits_read_gcore_yaml` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:283-301] |
| `shared_code_graph_limits_reject_invalid_or_negative_values` | function | `fn shared_code_graph_limits_reject_invalid_or_negative_values() {` | `shared_code_graph_limits_reject_invalid_or_negative_values [function]` | `7bd819cf-723b-5c97-a07b-5e6035272491` | 304-316 [crates/gwiki/src/support/config.rs:304-316] | Indexed function `shared_code_graph_limits_reject_invalid_or_negative_values` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:304-316] |
| `local_index_options_read_gcore_yaml` | function | `fn local_index_options_read_gcore_yaml() {` | `local_index_options_read_gcore_yaml [function]` | `97fc85e9-83df-5235-9cd4-56db6ab3aba5` | 320-332 [crates/gwiki/src/support/config.rs:320-332] | Indexed function `local_index_options_read_gcore_yaml` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:320-332] |
| `memory_indexing_uses_local_index_options` | function | `fn memory_indexing_uses_local_index_options() {` | `memory_indexing_uses_local_index_options [function]` | `eaf58024-bf53-5d32-bbf3-478b8b17238d` | 336-363 [crates/gwiki/src/support/config.rs:336-363] | Indexed function `memory_indexing_uses_local_index_options` in `crates/gwiki/src/support/config.rs`. [crates/gwiki/src/support/config.rs:336-363] |
