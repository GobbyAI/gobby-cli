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
  - Purpose: `GraphClient` is a thin client-side wrapper that owns a `SyncGraph` instance and exposes it as the graph access point. [crates/gcore/src/falkor.rs:28-30]
- `ReadOnlySyncGraph` (class) component `ReadOnlySyncGraph [class]` (`5e0bb07b-f3a8-5356-a139-ddd3927c0050`) lines 36-38 [crates/gcore/src/falkor.rs:36-38]
  - Signature: `pub struct ReadOnlySyncGraph<'a> {`
  - Purpose: A lifetime-bound wrapper around a mutable `SyncGraph` reference that provides a read-only access interface while retaining exclusive borrow control over the underlying graph. [crates/gcore/src/falkor.rs:36-38]
- `graph_name` (function) component `graph_name [function]` (`477e66b5-c265-548c-b467-99fbb35a63e1`) lines 42-44 [crates/gcore/src/falkor.rs:42-44]
  - Signature: `pub fn graph_name(&self) -> &str {`
  - Purpose: Returns a string slice of the underlying graph’s name by delegating to `self.graph.graph_name()`. [crates/gcore/src/falkor.rs:42-44]
- `ro_query` (function) component `ro_query [function]` (`fb007b8f-24a5-57ab-b2ba-99e41c9cff4a`) lines 47-52 [crates/gcore/src/falkor.rs:47-52]
  - Signature: `pub fn ro_query<'b>(`
  - Purpose: Delegates the provided read-only query string to `self.graph.ro_query` and returns the resulting `QueryBuilder` configured to produce a `QueryResult<LazyResultSet<'b>>` over `SyncGraph`. [crates/gcore/src/falkor.rs:47-52]
- `GraphClient` (class) component `GraphClient [class]` (`ddecdd14-f7af-5ba6-9d22-6ddf3c0d2c77`) lines 55-127 [crates/gcore/src/falkor.rs:55-127]
  - Signature: `impl GraphClient {`
  - Purpose: `GraphClient` is a thin FalkorDB wrapper that builds a connection from `FalkorConfig`, selects a named graph, exposes a constrained read-only sync graph escape hatch, executes parameterized Cypher queries into parsed rows, and manages exact node indexes. [crates/gcore/src/falkor.rs:55-127]
- `GraphClient.from_config` (method) component `GraphClient.from_config [method]` (`f4e633f0-32d2-5fc8-83f6-0106a502b4ab`) lines 57-72 [crates/gcore/src/falkor.rs:57-72]
  - Signature: `pub fn from_config(config: &FalkorConfig, graph_name: &str) -> anyhow::Result<Self> {`
  - Purpose: `from_config` builds a FalkorDB client connection string from `FalkorConfig` by URL-encoding the optional password, creating `FalkorConnectionInfo`, constructing a `FalkorClient`, and returning `Self` with the selected `graph_name`, propagating any failures as `anyhow::Result`. [crates/gcore/src/falkor.rs:57-72]
- `GraphClient.with_sync_graph` (method) component `GraphClient.with_sync_graph [method]` (`9bf0e7c7-1034-5c48-836e-6bb38716fda8`) lines 79-87 [crates/gcore/src/falkor.rs:79-87]
  - Signature: `pub fn with_sync_graph<T>(`
  - Purpose: `with_sync_graph` creates a temporary `ReadOnlySyncGraph` view over `self.graph`, passes it to the provided closure for mutation-free access, and returns the closure’s `anyhow::Result<T>` unchanged. [crates/gcore/src/falkor.rs:79-87]
- `GraphClient.query` (method) component `GraphClient.query [method]` (`efd14ba7-7c17-55ec-bdcb-e7840247bf4f`) lines 90-105 [crates/gcore/src/falkor.rs:90-105]
  - Signature: `pub fn query(`
  - Purpose: Executes the given Cypher query against `self.graph` with optional string parameters, then converts the FalkorDB execution result into `Vec<Row>` and returns it as an `anyhow::Result`. [crates/gcore/src/falkor.rs:90-105]
- `GraphClient.ensure_exact_node_index` (method) component `GraphClient.ensure_exact_node_index [method]` (`582b6b7e-b027-5022-84a3-92dfde87ef7e`) lines 108-126 [crates/gcore/src/falkor.rs:108-126]
  - Signature: `pub fn ensure_exact_node_index(&mut self, label: &str, property: &str) -> anyhow::Result<()> {`
  - Purpose: Creates an exact FalkorDB node index for the given `label` and `property` by running `CREATE INDEX`, returns success if the index already exists by suppressing that specific duplicate-index error, and propagates any other query error. [crates/gcore/src/falkor.rs:108-126]
- `with_graph` (function) component `with_graph [function]` (`1a19a2a6-e709-5c01-8767-c1366d26dbb2`) lines 136-143 [crates/gcore/src/falkor.rs:136-143]
  - Signature: `pub fn with_graph<T>(`
  - Purpose: `with_graph` is a thin generic wrapper that invokes `with_graph_client` with `GraphClient::from_config` to build a `GraphClient` for the specified graph, run the provided mutable-client closure, and return the closure result together with the resulting `ServiceState`. [crates/gcore/src/falkor.rs:136-143]
- `with_graph_client` (function) component `with_graph_client [function]` (`3aae9263-ea31-5917-af73-cad6e901017c`) lines 145-172 [crates/gcore/src/falkor.rs:145-172]
  - Signature: `fn with_graph_client<T, C>(`
  - Purpose: `with_graph_client` conditionally constructs a FalkorDB client from the optional `FalkorConfig`, runs a mutable-client closure and returns its result with `ServiceState::Available`, or otherwise returns the provided default with `NotConfigured` if config is missing or `Unreachable` if client creation fails. [crates/gcore/src/falkor.rs:145-172]
- `escape_label` (function) component `escape_label [function]` (`74dd2788-abdb-583e-aac7-8857dac16aaa`) lines 175-177 [crates/gcore/src/falkor.rs:175-177]
  - Signature: `pub fn escape_label(label: &str) -> String {`
  - Purpose: Delegates directly to `escape_identifier`, returning an escaped `String` representation of the input `label` using the identifier-escaping rules. [crates/gcore/src/falkor.rs:175-177]
- `escape_rel_type` (function) component `escape_rel_type [function]` (`815ad20e-7797-54ff-8c1f-bf82d998b8e7`) lines 180-182 [crates/gcore/src/falkor.rs:180-182]
  - Signature: `pub fn escape_rel_type(rel: &str) -> String {`
  - Purpose: Returns `rel` as an escaped `String` by delegating directly to `escape_identifier`, applying the same identifier-sanitization rules to relation-type names. [crates/gcore/src/falkor.rs:180-182]
- `escape_property` (function) component `escape_property [function]` (`24f592ae-9d81-5897-9473-33adbf0eae06`) lines 185-187 [crates/gcore/src/falkor.rs:185-187]
  - Signature: `pub fn escape_property(key: &str) -> String {`
  - Purpose: Returns `key` unchanged in meaning but escaped as an identifier by delegating directly to `escape_identifier`, yielding a `String` suitable for use as a property name. [crates/gcore/src/falkor.rs:185-187]
- `escape_string` (function) component `escape_string [function]` (`3b06c437-f062-561f-ac4d-d990fe9bf83b`) lines 195-198 [crates/gcore/src/falkor.rs:195-198]
  - Signature: `pub fn escape_string(value: &str) -> String {`
  - Purpose: Returns a new `String` containing `value` wrapped in single quotes, with every backslash escaped as `\\` and every single quote escaped as `\'`. [crates/gcore/src/falkor.rs:195-198]
- `escape_identifier` (function) component `escape_identifier [function]` (`50ebdc15-2314-5020-a5f3-7f84c604bb0c`) lines 200-202 [crates/gcore/src/falkor.rs:200-202]
  - Signature: `fn escape_identifier(value: &str) -> String {`
  - Purpose: Returns a backtick-delimited identifier string by escaping every internal backtick in `value` as ```` before wrapping it in outer backticks. [crates/gcore/src/falkor.rs:200-202]
- `is_existing_index_error` (function) component `is_existing_index_error [function]` (`1acf7309-ad18-5cf0-9b13-120dfc89cebf`) lines 207-220 [crates/gcore/src/falkor.rs:207-220]
  - Signature: `fn is_existing_index_error(error: &anyhow::Error) -> bool {`
  - Purpose: Returns `true` when the lowercase stringified `anyhow::Error` contains any of the known `EXISTING_INDEX_ERROR_PATTERNS` for FalkorDB duplicate-index failures, and otherwise logs a debug message for unmatched index-like errors before returning `false`. [crates/gcore/src/falkor.rs:207-220]
- `parse_falkor_result` (function) component `parse_falkor_result [function]` (`47de66f2-e1b0-5fd3-9c5d-8f7a084c805e`) lines 222-224 [crates/gcore/src/falkor.rs:222-224]
  - Signature: `fn parse_falkor_result(result: QueryResult<LazyResultSet<'_>>) -> Vec<Row> {`
  - Purpose: It transforms a `QueryResult<LazyResultSet<'_>>` into a `Vec<Row>` by passing `result.header` and `result.data` to `parse_falkor_records`. [crates/gcore/src/falkor.rs:222-224]
- `parse_falkor_records` (function) component `parse_falkor_records [function]` (`d5d955fc-7aff-57d3-90ab-12bac2bc18c8`) lines 226-241 [crates/gcore/src/falkor.rs:226-241]
  - Signature: `fn parse_falkor_records<I>(headers: Vec<String>, records: I) -> Vec<Row>`
  - Purpose: `parse_falkor_records` converts each `Vec<FalkorValue>` record into a `Row` map by zipping it against the provided `headers`, converting each value to JSON with `falkor_value_to_json`, and filling any missing columns with `FalkorValue::None`, then collects all rows into a `Vec<Row>`. [crates/gcore/src/falkor.rs:226-241]
- `falkor_value_to_json` (function) component `falkor_value_to_json [function]` (`9bf38797-80d2-5f84-888d-d043c5325f79`) lines 243-266 [crates/gcore/src/falkor.rs:243-266]
  - Signature: `fn falkor_value_to_json(value: FalkorValue) -> Value {`
  - Purpose: `falkor_value_to_json` recursively converts a `FalkorValue` into a `serde_json::Value`, preserving strings/bools/integers, mapping finite `f64` values to JSON numbers and non-finite ones to `null`, converting arrays and maps elementwise, returning `null` for `None`, and falling back to a debug-string `Value::String` for any other variant. [crates/gcore/src/falkor.rs:243-266]
- `FakeGraphClient` (class) component `FakeGraphClient [class]` (`6bed3401-ecfd-5004-8256-6bcb44d92857`) lines 275-275 [crates/gcore/src/falkor.rs:275]
  - Signature: `struct FakeGraphClient;`
  - Purpose: I’m checking whether `FakeGraphClient` is defined elsewhere in the repo so I can give a precise one-sentence summary instead of guessing from the forward declaration alone.`FakeGraphClient` does not appear in the current checkout by name, so I’m checking the code index for nearby definitions and usages before I summarize it.A forward declaration of `FakeGraphClient` that introduces the struct type without defining its fields, layout, or member functions in this translation unit. [crates/gcore/src/falkor.rs:275]
- `test_config` (function) component `test_config [function]` (`58efabc6-0026-58d1-a463-b176831fbd17`) lines 277-283 [crates/gcore/src/falkor.rs:277-283]
  - Signature: `fn test_config() -> FalkorConfig {`
  - Purpose: Returns a `FalkorConfig` test fixture with `host` set to `127.0.0.1`, `port` set to `1`, and `password` unset (`None`). [crates/gcore/src/falkor.rs:277-283]
- `with_graph_degradation_contract` (function) component `with_graph_degradation_contract [function]` (`c8b1088c-9625-520a-9e77-7508ff837fc3`) lines 286-334 [crates/gcore/src/falkor.rs:286-334]
  - Signature: `fn with_graph_degradation_contract() {`
  - Purpose: Verifies that `with_graph`/`with_graph_client` degrade to the supplied default with `ServiceState::NotConfigured` or `ServiceState::Unreachable` on missing config or client construction failure, return `ServiceState::Available` on success, and propagate closure errors unchanged. [crates/gcore/src/falkor.rs:286-334]
- `escapes_graph_tokens` (function) component `escapes_graph_tokens [function]` (`880a393e-fd24-5cd9-b561-aec6fc7b843e`) lines 337-345 [crates/gcore/src/falkor.rs:337-345]
  - Signature: `fn escapes_graph_tokens() {`
  - Purpose: It verifies that graph token escaping correctly backtick-escapes labels, relationship types, and property names by doubling internal backticks, and that string escaping produces a single-quoted literal with backslashes and apostrophes escaped. [crates/gcore/src/falkor.rs:337-345]
- `no_domain_labels_in_adapter` (function) component `no_domain_labels_in_adapter [function]` (`6af0b9da-5a9e-5d03-998b-fb76a35ffd42`) lines 348-361 [crates/gcore/src/falkor.rs:348-361]
  - Signature: `fn no_domain_labels_in_adapter() {`
  - Purpose: It loads the `falkor.rs` source as a string and asserts that none of the listed forbidden label substrings appear in it, failing with a leak message if any token is present. [crates/gcore/src/falkor.rs:348-361]
- `graph_unavailable_is_not_empty_success` (function) component `graph_unavailable_is_not_empty_success [function]` (`e6987e14-c9a1-52c4-8b30-4c748985e3ba`) lines 364-389 [crates/gcore/src/falkor.rs:364-389]
  - Signature: `fn graph_unavailable_is_not_empty_success() {`
  - Purpose: It verifies that `with_graph_client` turns a graph connection failure into an empty row set with `ServiceState::Unreachable`, while an empty but successful query returns an empty row set with `ServiceState::Available`. [crates/gcore/src/falkor.rs:364-389]
- `graph_name_is_consumer_supplied` (function) component `graph_name_is_consumer_supplied [function]` (`b8b28536-da74-5a0e-bd44-3587bd136a92`) lines 392-415 [crates/gcore/src/falkor.rs:392-415]
  - Signature: `fn graph_name_is_consumer_supplied() {`
  - Purpose: This test verifies that `with_graph_client` forwards the caller-supplied graph name (`"consumer_graph"`) to the client factory, returns `((), ServiceState::Available)`, and that the adapter source does not hardcode the internal `"gobby_code"` graph name. [crates/gcore/src/falkor.rs:392-415]
- `live_sync_graph_read_is_env_gated` (function) component `live_sync_graph_read_is_env_gated [function]` (`d57ac864-29ed-5a52-878d-dde86c6ab1d7`) lines 418-441 [crates/gcore/src/falkor.rs:418-441]
  - Signature: `fn live_sync_graph_read_is_env_gated() {`
  - Purpose: This live integration test is environment-gated on `GOBBY_FALKORDB_HOST`, skips if a `GraphClient` cannot be created, and otherwise verifies `SyncGraph` read execution by asserting that `RETURN 1 AS value` produces a first row with `value == 1`. [crates/gcore/src/falkor.rs:418-441]
- `live_falkor_fixture` (function) component `live_falkor_fixture [function]` (`642bd3d3-baea-5129-995d-712111ef62ae`) lines 443-462 [crates/gcore/src/falkor.rs:443-462]
  - Signature: `fn live_falkor_fixture() -> Option<(FalkorConfig, String)> {`
  - Purpose: Returns `Some((FalkorConfig, graph_name))` only when `GOBBY_FALKORDB_HOST` is set, using `GOBBY_FALKORDB_PORT` parsed as `u16` with default `16379`, an optional non-empty `GOBBY_FALKORDB_PASSWORD`, and `GOBBY_FALKORDB_TEST_GRAPH` with default `"gobby_core_live_test"`, otherwise returns `None`. [crates/gcore/src/falkor.rs:443-462]
- `existing_index_errors_are_recognized_case_insensitively` (function) component `existing_index_errors_are_recognized_case_insensitively [function]` (`6deda299-f372-52f7-a747-a26ff569d896`) lines 465-474 [crates/gcore/src/falkor.rs:465-474]
  - Signature: `fn existing_index_errors_are_recognized_case_insensitively() {`
  - Purpose: This test verifies that `is_existing_index_error` returns `true` for multiple “index already exists” error संदेश variants, confirming the matcher recognizes existing-index errors case-insensitively. [crates/gcore/src/falkor.rs:465-474]
- `unrelated_index_errors_are_not_suppressed` (function) component `unrelated_index_errors_are_not_suppressed [function]` (`1bc452ad-d5e3-5238-91e4-07cae0cbe6d3`) lines 477-481 [crates/gcore/src/falkor.rs:477-481]
  - Signature: `fn unrelated_index_errors_are_not_suppressed() {`
  - Purpose: This test verifies that an unrelated `anyhow` error containing the message `syntax error near CREATE INDEX` is not misclassified as an existing-index error by `is_existing_index_error`. [crates/gcore/src/falkor.rs:477-481]

