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
  - 57-72
  - 79-87
  - 90-105
  - 108-126
  - 136-143
  - 145-172
  - 175-177
  - 180-182
  - 185-187
  - 195-198
  - 200-202
  - 207-220
  - 222-224
  - 226-241
  - 243-266
  - '275'
  - 277-283
  - 286-334
  - 337-345
  - 348-361
  - 364-389
  - 392-415
  - 418-441
  - 443-462
  - 465-474
  - 477-481
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/falkor.rs:22](crates/gcore/src/falkor.rs#L22), [crates/gcore/src/falkor.rs:28-30](crates/gcore/src/falkor.rs#L28-L30), [crates/gcore/src/falkor.rs:36-38](crates/gcore/src/falkor.rs#L36-L38), [crates/gcore/src/falkor.rs:42-44](crates/gcore/src/falkor.rs#L42-L44), [crates/gcore/src/falkor.rs:47-52](crates/gcore/src/falkor.rs#L47-L52), [crates/gcore/src/falkor.rs:57-72](crates/gcore/src/falkor.rs#L57-L72), [crates/gcore/src/falkor.rs:79-87](crates/gcore/src/falkor.rs#L79-L87), [crates/gcore/src/falkor.rs:90-105](crates/gcore/src/falkor.rs#L90-L105), [crates/gcore/src/falkor.rs:108-126](crates/gcore/src/falkor.rs#L108-L126), [crates/gcore/src/falkor.rs:136-143](crates/gcore/src/falkor.rs#L136-L143), [crates/gcore/src/falkor.rs:145-172](crates/gcore/src/falkor.rs#L145-L172), [crates/gcore/src/falkor.rs:175-177](crates/gcore/src/falkor.rs#L175-L177), [crates/gcore/src/falkor.rs:180-182](crates/gcore/src/falkor.rs#L180-L182), [crates/gcore/src/falkor.rs:185-187](crates/gcore/src/falkor.rs#L185-L187), [crates/gcore/src/falkor.rs:195-198](crates/gcore/src/falkor.rs#L195-L198), [crates/gcore/src/falkor.rs:200-202](crates/gcore/src/falkor.rs#L200-L202), [crates/gcore/src/falkor.rs:207-220](crates/gcore/src/falkor.rs#L207-L220), [crates/gcore/src/falkor.rs:222-224](crates/gcore/src/falkor.rs#L222-L224), [crates/gcore/src/falkor.rs:226-241](crates/gcore/src/falkor.rs#L226-L241), [crates/gcore/src/falkor.rs:243-266](crates/gcore/src/falkor.rs#L243-L266), [crates/gcore/src/falkor.rs:275](crates/gcore/src/falkor.rs#L275), [crates/gcore/src/falkor.rs:277-283](crates/gcore/src/falkor.rs#L277-L283), [crates/gcore/src/falkor.rs:286-334](crates/gcore/src/falkor.rs#L286-L334), [crates/gcore/src/falkor.rs:337-345](crates/gcore/src/falkor.rs#L337-L345), [crates/gcore/src/falkor.rs:348-361](crates/gcore/src/falkor.rs#L348-L361), [crates/gcore/src/falkor.rs:364-389](crates/gcore/src/falkor.rs#L364-L389), [crates/gcore/src/falkor.rs:392-415](crates/gcore/src/falkor.rs#L392-L415), [crates/gcore/src/falkor.rs:418-441](crates/gcore/src/falkor.rs#L418-L441), [crates/gcore/src/falkor.rs:443-462](crates/gcore/src/falkor.rs#L443-L462), [crates/gcore/src/falkor.rs:465-474](crates/gcore/src/falkor.rs#L465-L474), [crates/gcore/src/falkor.rs:477-481](crates/gcore/src/falkor.rs#L477-L481)

</details>

# crates/gcore/src/falkor.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

FalkorDB adapter boundary for the `gcore` crate. It wraps the `falkordb` client in a `GraphClient` and a read-only `SyncGraph` view, builds connections from `FalkorConfig`, runs queries, and handles index creation with duplicate-index suppression. The module also provides escaping helpers for Cypher tokens and strings, converts Falkor query results into JSON-style rows, and includes env-gated/live tests plus contract tests covering graph-name handling, degraded/unavailable behavior, token escaping, and error recognition.
[crates/gcore/src/falkor.rs:22]
[crates/gcore/src/falkor.rs:28-30]
[crates/gcore/src/falkor.rs:36-38]
[crates/gcore/src/falkor.rs:42-44]
[crates/gcore/src/falkor.rs:47-52]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Row` | type | `pub type Row = HashMap<String, Value>;` | `Row [type]` | `cd52699d-7b01-54a5-b28f-ae85df71557a` | 22-22 [crates/gcore/src/falkor.rs:22] | Indexed type `Row` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:22] |
| `GraphClient` | class | `pub struct GraphClient {` | `GraphClient [class]` | `0ecd9258-5686-5f79-8b28-d1c5b0e7f20b` | 28-30 [crates/gcore/src/falkor.rs:28-30] | Indexed class `GraphClient` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:28-30] |
| `ReadOnlySyncGraph` | class | `pub struct ReadOnlySyncGraph<'a> {` | `ReadOnlySyncGraph [class]` | `5e0bb07b-f3a8-5356-a139-ddd3927c0050` | 36-38 [crates/gcore/src/falkor.rs:36-38] | Indexed class `ReadOnlySyncGraph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:36-38] |
| `graph_name` | function | `pub fn graph_name(&self) -> &str {` | `graph_name [function]` | `477e66b5-c265-548c-b467-99fbb35a63e1` | 42-44 [crates/gcore/src/falkor.rs:42-44] | Indexed function `graph_name` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:42-44] |
| `ro_query` | function | `pub fn ro_query<'b>(` | `ro_query [function]` | `fb007b8f-24a5-57ab-b2ba-99e41c9cff4a` | 47-52 [crates/gcore/src/falkor.rs:47-52] | Indexed function `ro_query` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:47-52] |
| `GraphClient::from_config` | method | `pub fn from_config(config: &FalkorConfig, graph_name: &str) -> anyhow::Result<Self> {` | `GraphClient::from_config [method]` | `f4e633f0-32d2-5fc8-83f6-0106a502b4ab` | 57-72 [crates/gcore/src/falkor.rs:57-72] | Indexed method `GraphClient::from_config` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:57-72] |
| `GraphClient::with_sync_graph` | method | `pub fn with_sync_graph<T>(` | `GraphClient::with_sync_graph [method]` | `9bf0e7c7-1034-5c48-836e-6bb38716fda8` | 79-87 [crates/gcore/src/falkor.rs:79-87] | Indexed method `GraphClient::with_sync_graph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:79-87] |
| `GraphClient::query` | method | `pub fn query(` | `GraphClient::query [method]` | `efd14ba7-7c17-55ec-bdcb-e7840247bf4f` | 90-105 [crates/gcore/src/falkor.rs:90-105] | Indexed method `GraphClient::query` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:90-105] |
| `GraphClient::ensure_exact_node_index` | method | `pub fn ensure_exact_node_index(&mut self, label: &str, property: &str) -> anyhow::Result<()> {` | `GraphClient::ensure_exact_node_index [method]` | `582b6b7e-b027-5022-84a3-92dfde87ef7e` | 108-126 [crates/gcore/src/falkor.rs:108-126] | Indexed method `GraphClient::ensure_exact_node_index` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:108-126] |
| `with_graph` | function | `pub fn with_graph<T>(` | `with_graph [function]` | `1a19a2a6-e709-5c01-8767-c1366d26dbb2` | 136-143 [crates/gcore/src/falkor.rs:136-143] | Indexed function `with_graph` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:136-143] |
| `with_graph_client` | function | `fn with_graph_client<T, C>(` | `with_graph_client [function]` | `3aae9263-ea31-5917-af73-cad6e901017c` | 145-172 [crates/gcore/src/falkor.rs:145-172] | Indexed function `with_graph_client` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:145-172] |
| `escape_label` | function | `pub fn escape_label(label: &str) -> String {` | `escape_label [function]` | `74dd2788-abdb-583e-aac7-8857dac16aaa` | 175-177 [crates/gcore/src/falkor.rs:175-177] | Indexed function `escape_label` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:175-177] |
| `escape_rel_type` | function | `pub fn escape_rel_type(rel: &str) -> String {` | `escape_rel_type [function]` | `815ad20e-7797-54ff-8c1f-bf82d998b8e7` | 180-182 [crates/gcore/src/falkor.rs:180-182] | Indexed function `escape_rel_type` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:180-182] |
| `escape_property` | function | `pub fn escape_property(key: &str) -> String {` | `escape_property [function]` | `24f592ae-9d81-5897-9473-33adbf0eae06` | 185-187 [crates/gcore/src/falkor.rs:185-187] | Indexed function `escape_property` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:185-187] |
| `escape_string` | function | `pub fn escape_string(value: &str) -> String {` | `escape_string [function]` | `3b06c437-f062-561f-ac4d-d990fe9bf83b` | 195-198 [crates/gcore/src/falkor.rs:195-198] | Indexed function `escape_string` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:195-198] |
| `escape_identifier` | function | `fn escape_identifier(value: &str) -> String {` | `escape_identifier [function]` | `50ebdc15-2314-5020-a5f3-7f84c604bb0c` | 200-202 [crates/gcore/src/falkor.rs:200-202] | Indexed function `escape_identifier` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:200-202] |
| `is_existing_index_error` | function | `fn is_existing_index_error(error: &anyhow::Error) -> bool {` | `is_existing_index_error [function]` | `1acf7309-ad18-5cf0-9b13-120dfc89cebf` | 207-220 [crates/gcore/src/falkor.rs:207-220] | Indexed function `is_existing_index_error` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:207-220] |
| `parse_falkor_result` | function | `fn parse_falkor_result(result: QueryResult<LazyResultSet<'_>>) -> Vec<Row> {` | `parse_falkor_result [function]` | `47de66f2-e1b0-5fd3-9c5d-8f7a084c805e` | 222-224 [crates/gcore/src/falkor.rs:222-224] | Indexed function `parse_falkor_result` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:222-224] |
| `parse_falkor_records` | function | `fn parse_falkor_records<I>(headers: Vec<String>, records: I) -> Vec<Row>` | `parse_falkor_records [function]` | `d5d955fc-7aff-57d3-90ab-12bac2bc18c8` | 226-241 [crates/gcore/src/falkor.rs:226-241] | Indexed function `parse_falkor_records` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:226-241] |
| `falkor_value_to_json` | function | `fn falkor_value_to_json(value: FalkorValue) -> Value {` | `falkor_value_to_json [function]` | `9bf38797-80d2-5f84-888d-d043c5325f79` | 243-266 [crates/gcore/src/falkor.rs:243-266] | Indexed function `falkor_value_to_json` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:243-266] |
| `FakeGraphClient` | class | `struct FakeGraphClient;` | `FakeGraphClient [class]` | `6bed3401-ecfd-5004-8256-6bcb44d92857` | 275-275 [crates/gcore/src/falkor.rs:275] | Indexed class `FakeGraphClient` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:275] |
| `test_config` | function | `fn test_config() -> FalkorConfig {` | `test_config [function]` | `58efabc6-0026-58d1-a463-b176831fbd17` | 277-283 [crates/gcore/src/falkor.rs:277-283] | Indexed function `test_config` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:277-283] |
| `with_graph_degradation_contract` | function | `fn with_graph_degradation_contract() {` | `with_graph_degradation_contract [function]` | `c8b1088c-9625-520a-9e77-7508ff837fc3` | 286-334 [crates/gcore/src/falkor.rs:286-334] | Indexed function `with_graph_degradation_contract` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:286-334] |
| `escapes_graph_tokens` | function | `fn escapes_graph_tokens() {` | `escapes_graph_tokens [function]` | `880a393e-fd24-5cd9-b561-aec6fc7b843e` | 337-345 [crates/gcore/src/falkor.rs:337-345] | Indexed function `escapes_graph_tokens` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:337-345] |
| `no_domain_labels_in_adapter` | function | `fn no_domain_labels_in_adapter() {` | `no_domain_labels_in_adapter [function]` | `6af0b9da-5a9e-5d03-998b-fb76a35ffd42` | 348-361 [crates/gcore/src/falkor.rs:348-361] | Indexed function `no_domain_labels_in_adapter` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:348-361] |
| `graph_unavailable_is_not_empty_success` | function | `fn graph_unavailable_is_not_empty_success() {` | `graph_unavailable_is_not_empty_success [function]` | `e6987e14-c9a1-52c4-8b30-4c748985e3ba` | 364-389 [crates/gcore/src/falkor.rs:364-389] | Indexed function `graph_unavailable_is_not_empty_success` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:364-389] |
| `graph_name_is_consumer_supplied` | function | `fn graph_name_is_consumer_supplied() {` | `graph_name_is_consumer_supplied [function]` | `b8b28536-da74-5a0e-bd44-3587bd136a92` | 392-415 [crates/gcore/src/falkor.rs:392-415] | Indexed function `graph_name_is_consumer_supplied` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:392-415] |
| `live_sync_graph_read_is_env_gated` | function | `fn live_sync_graph_read_is_env_gated() {` | `live_sync_graph_read_is_env_gated [function]` | `d57ac864-29ed-5a52-878d-dde86c6ab1d7` | 418-441 [crates/gcore/src/falkor.rs:418-441] | Indexed function `live_sync_graph_read_is_env_gated` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:418-441] |
| `live_falkor_fixture` | function | `fn live_falkor_fixture() -> Option<(FalkorConfig, String)> {` | `live_falkor_fixture [function]` | `642bd3d3-baea-5129-995d-712111ef62ae` | 443-462 [crates/gcore/src/falkor.rs:443-462] | Indexed function `live_falkor_fixture` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:443-462] |
| `existing_index_errors_are_recognized_case_insensitively` | function | `fn existing_index_errors_are_recognized_case_insensitively() {` | `existing_index_errors_are_recognized_case_insensitively [function]` | `6deda299-f372-52f7-a747-a26ff569d896` | 465-474 [crates/gcore/src/falkor.rs:465-474] | Indexed function `existing_index_errors_are_recognized_case_insensitively` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:465-474] |
| `unrelated_index_errors_are_not_suppressed` | function | `fn unrelated_index_errors_are_not_suppressed() {` | `unrelated_index_errors_are_not_suppressed [function]` | `1bc452ad-d5e3-5238-91e4-07cae0cbe6d3` | 477-481 [crates/gcore/src/falkor.rs:477-481] | Indexed function `unrelated_index_errors_are_not_suppressed` in `crates/gcore/src/falkor.rs`. [crates/gcore/src/falkor.rs:477-481] |
