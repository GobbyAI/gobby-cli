---
title: crates/gcore/src/falkor.rs
type: code_file
provenance:
- file: crates/gcore/src/falkor.rs
  ranges:
  - '22'
  - 28-30
  - 36-38
  - 42-44
  - 47-52
  - 55-127
  - 57-72
  - 79-87
  - 90-105
  - 108-126
  - 136-143
  - 145-172
  - 175-177
  - 180-182
  - 185-187
  - 190-193
  - 195-197
  - 202-215
  - 217-219
  - 221-236
  - 238-261
  - '270'
  - 272-278
  - 281-329
  - 332-340
  - 343-356
  - 359-384
  - 387-410
  - 413-436
  - 438-457
  - 460-469
  - 472-476
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/falkor.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/falkor.rs` exposes 32 indexed API symbols.
[crates/gcore/src/falkor.rs:22]
[crates/gcore/src/falkor.rs:28-30]
[crates/gcore/src/falkor.rs:36-38]
[crates/gcore/src/falkor.rs:42-44]
[crates/gcore/src/falkor.rs:47-52]

## API Symbols

- `Row` (type) component `Row [type]` (`cd52699d-7b01-54a5-b28f-ae85df71557a`) lines 22-22 [crates/gcore/src/falkor.rs:22]
  - Signature: `pub type Row = HashMap<String, Value>;`
  - Purpose: Indexed type `Row` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:22]
- `GraphClient` (class) component `GraphClient [class]` (`0ecd9258-5686-5f79-8b28-d1c5b0e7f20b`) lines 28-30 [crates/gcore/src/falkor.rs:28-30]
  - Signature: `pub struct GraphClient {`
  - Purpose: Indexed class `GraphClient` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:28-30]
- `ReadOnlySyncGraph` (class) component `ReadOnlySyncGraph [class]` (`5e0bb07b-f3a8-5356-a139-ddd3927c0050`) lines 36-38 [crates/gcore/src/falkor.rs:36-38]
  - Signature: `pub struct ReadOnlySyncGraph<'a> {`
  - Purpose: Indexed class `ReadOnlySyncGraph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:36-38]
- `graph_name` (function) component `graph_name [function]` (`477e66b5-c265-548c-b467-99fbb35a63e1`) lines 42-44 [crates/gcore/src/falkor.rs:42-44]
  - Signature: `pub fn graph_name(&self) -> &str {`
  - Purpose: Indexed function `graph_name` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:42-44]
- `ro_query` (function) component `ro_query [function]` (`fb007b8f-24a5-57ab-b2ba-99e41c9cff4a`) lines 47-52 [crates/gcore/src/falkor.rs:47-52]
  - Signature: `pub fn ro_query<'b>(`
  - Purpose: Indexed function `ro_query` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:47-52]
- `GraphClient` (class) component `GraphClient [class]` (`ddecdd14-f7af-5ba6-9d22-6ddf3c0d2c77`) lines 55-127 [crates/gcore/src/falkor.rs:55-127]
  - Signature: `impl GraphClient {`
  - Purpose: Indexed class `GraphClient` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:55-127]
- `GraphClient.from_config` (method) component `GraphClient.from_config [method]` (`f4e633f0-32d2-5fc8-83f6-0106a502b4ab`) lines 57-72 [crates/gcore/src/falkor.rs:57-72]
  - Signature: `pub fn from_config(config: &FalkorConfig, graph_name: &str) -> anyhow::Result<Self> {`
  - Purpose: Indexed method `GraphClient.from_config` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:57-72]
- `GraphClient.with_sync_graph` (method) component `GraphClient.with_sync_graph [method]` (`9bf0e7c7-1034-5c48-836e-6bb38716fda8`) lines 79-87 [crates/gcore/src/falkor.rs:79-87]
  - Signature: `pub fn with_sync_graph<T>(`
  - Purpose: Indexed method `GraphClient.with_sync_graph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:79-87]
- `GraphClient.query` (method) component `GraphClient.query [method]` (`efd14ba7-7c17-55ec-bdcb-e7840247bf4f`) lines 90-105 [crates/gcore/src/falkor.rs:90-105]
  - Signature: `pub fn query(`
  - Purpose: Indexed method `GraphClient.query` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:90-105]
- `GraphClient.ensure_exact_node_index` (method) component `GraphClient.ensure_exact_node_index [method]` (`582b6b7e-b027-5022-84a3-92dfde87ef7e`) lines 108-126 [crates/gcore/src/falkor.rs:108-126]
  - Signature: `pub fn ensure_exact_node_index(&mut self, label: &str, property: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed method `GraphClient.ensure_exact_node_index` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:108-126]
- `with_graph` (function) component `with_graph [function]` (`1a19a2a6-e709-5c01-8767-c1366d26dbb2`) lines 136-143 [crates/gcore/src/falkor.rs:136-143]
  - Signature: `pub fn with_graph<T>(`
  - Purpose: Indexed function `with_graph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:136-143]
- `with_graph_client` (function) component `with_graph_client [function]` (`3aae9263-ea31-5917-af73-cad6e901017c`) lines 145-172 [crates/gcore/src/falkor.rs:145-172]
  - Signature: `fn with_graph_client<T, C>(`
  - Purpose: Indexed function `with_graph_client` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:145-172]
- `escape_label` (function) component `escape_label [function]` (`74dd2788-abdb-583e-aac7-8857dac16aaa`) lines 175-177 [crates/gcore/src/falkor.rs:175-177]
  - Signature: `pub fn escape_label(label: &str) -> String {`
  - Purpose: Indexed function `escape_label` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:175-177]
- `escape_rel_type` (function) component `escape_rel_type [function]` (`815ad20e-7797-54ff-8c1f-bf82d998b8e7`) lines 180-182 [crates/gcore/src/falkor.rs:180-182]
  - Signature: `pub fn escape_rel_type(rel: &str) -> String {`
  - Purpose: Indexed function `escape_rel_type` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:180-182]
- `escape_property` (function) component `escape_property [function]` (`24f592ae-9d81-5897-9473-33adbf0eae06`) lines 185-187 [crates/gcore/src/falkor.rs:185-187]
  - Signature: `pub fn escape_property(key: &str) -> String {`
  - Purpose: Indexed function `escape_property` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:185-187]
- `escape_string` (function) component `escape_string [function]` (`fd1de4cc-0c15-58d4-a91d-4f35dac93819`) lines 190-193 [crates/gcore/src/falkor.rs:190-193]
  - Signature: `pub fn escape_string(value: &str) -> String {`
  - Purpose: Indexed function `escape_string` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:190-193]
- `escape_identifier` (function) component `escape_identifier [function]` (`8c424f11-bbcb-5146-8b52-2d1c3719841d`) lines 195-197 [crates/gcore/src/falkor.rs:195-197]
  - Signature: `fn escape_identifier(value: &str) -> String {`
  - Purpose: Indexed function `escape_identifier` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:195-197]
- `is_existing_index_error` (function) component `is_existing_index_error [function]` (`3e9bdbee-c529-5798-b8e2-67e237ae9cb8`) lines 202-215 [crates/gcore/src/falkor.rs:202-215]
  - Signature: `fn is_existing_index_error(error: &anyhow::Error) -> bool {`
  - Purpose: Indexed function `is_existing_index_error` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:202-215]
- `parse_falkor_result` (function) component `parse_falkor_result [function]` (`03b8b0b2-2379-5d70-8302-83330dbe5281`) lines 217-219 [crates/gcore/src/falkor.rs:217-219]
  - Signature: `fn parse_falkor_result(result: QueryResult<LazyResultSet<'_>>) -> Vec<Row> {`
  - Purpose: Indexed function `parse_falkor_result` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:217-219]
- `parse_falkor_records` (function) component `parse_falkor_records [function]` (`d2c2efd6-54ee-5f0a-b27b-e4eb24ffade3`) lines 221-236 [crates/gcore/src/falkor.rs:221-236]
  - Signature: `fn parse_falkor_records<I>(headers: Vec<String>, records: I) -> Vec<Row>`
  - Purpose: Indexed function `parse_falkor_records` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:221-236]
- `falkor_value_to_json` (function) component `falkor_value_to_json [function]` (`efa85cce-2a56-51c9-9228-c4eab5f5bfd1`) lines 238-261 [crates/gcore/src/falkor.rs:238-261]
  - Signature: `fn falkor_value_to_json(value: FalkorValue) -> Value {`
  - Purpose: Indexed function `falkor_value_to_json` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:238-261]
- `FakeGraphClient` (class) component `FakeGraphClient [class]` (`3d45c941-c14f-51c3-af23-b6e2dce0cffb`) lines 270-270 [crates/gcore/src/falkor.rs:270]
  - Signature: `struct FakeGraphClient;`
  - Purpose: Indexed class `FakeGraphClient` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:270]
- `test_config` (function) component `test_config [function]` (`1f4f7769-93a1-5da7-ac15-8f3f7b1678bd`) lines 272-278 [crates/gcore/src/falkor.rs:272-278]
  - Signature: `fn test_config() -> FalkorConfig {`
  - Purpose: Indexed function `test_config` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:272-278]
- `with_graph_degradation_contract` (function) component `with_graph_degradation_contract [function]` (`ba7c354d-16fe-5dce-874d-c2e9c12f964c`) lines 281-329 [crates/gcore/src/falkor.rs:281-329]
  - Signature: `fn with_graph_degradation_contract() {`
  - Purpose: Indexed function `with_graph_degradation_contract` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:281-329]
- `escapes_graph_tokens` (function) component `escapes_graph_tokens [function]` (`2f3ef373-5132-5c39-bfb5-aaf18bcebb6c`) lines 332-340 [crates/gcore/src/falkor.rs:332-340]
  - Signature: `fn escapes_graph_tokens() {`
  - Purpose: Indexed function `escapes_graph_tokens` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:332-340]
- `no_domain_labels_in_adapter` (function) component `no_domain_labels_in_adapter [function]` (`ea604493-2e48-5a99-b7c2-e7c54ead6c3b`) lines 343-356 [crates/gcore/src/falkor.rs:343-356]
  - Signature: `fn no_domain_labels_in_adapter() {`
  - Purpose: Indexed function `no_domain_labels_in_adapter` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:343-356]
- `graph_unavailable_is_not_empty_success` (function) component `graph_unavailable_is_not_empty_success [function]` (`3a143ccc-5f61-54c9-815d-494943d0a7ac`) lines 359-384 [crates/gcore/src/falkor.rs:359-384]
  - Signature: `fn graph_unavailable_is_not_empty_success() {`
  - Purpose: Indexed function `graph_unavailable_is_not_empty_success` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:359-384]
- `graph_name_is_consumer_supplied` (function) component `graph_name_is_consumer_supplied [function]` (`67b11b5c-5d17-5ff0-904a-39ca65e6bc6c`) lines 387-410 [crates/gcore/src/falkor.rs:387-410]
  - Signature: `fn graph_name_is_consumer_supplied() {`
  - Purpose: Indexed function `graph_name_is_consumer_supplied` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:387-410]
- `live_sync_graph_read_is_env_gated` (function) component `live_sync_graph_read_is_env_gated [function]` (`3c38d0c4-20ac-5f5b-b0fe-1cbda977fe5e`) lines 413-436 [crates/gcore/src/falkor.rs:413-436]
  - Signature: `fn live_sync_graph_read_is_env_gated() {`
  - Purpose: Indexed function `live_sync_graph_read_is_env_gated` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:413-436]
- `live_falkor_fixture` (function) component `live_falkor_fixture [function]` (`4a23dbf5-2590-50c2-afb1-31960035e737`) lines 438-457 [crates/gcore/src/falkor.rs:438-457]
  - Signature: `fn live_falkor_fixture() -> Option<(FalkorConfig, String)> {`
  - Purpose: Indexed function `live_falkor_fixture` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:438-457]
- `existing_index_errors_are_recognized_case_insensitively` (function) component `existing_index_errors_are_recognized_case_insensitively [function]` (`6d11bec2-3e01-5180-80ba-f7676f108414`) lines 460-469 [crates/gcore/src/falkor.rs:460-469]
  - Signature: `fn existing_index_errors_are_recognized_case_insensitively() {`
  - Purpose: Indexed function `existing_index_errors_are_recognized_case_insensitively` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:460-469]
- `unrelated_index_errors_are_not_suppressed` (function) component `unrelated_index_errors_are_not_suppressed [function]` (`4d06efa3-340f-5caa-b86d-9c3620115ad0`) lines 472-476 [crates/gcore/src/falkor.rs:472-476]
  - Signature: `fn unrelated_index_errors_are_not_suppressed() {`
  - Purpose: Indexed function `unrelated_index_errors_are_not_suppressed` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:472-476]

