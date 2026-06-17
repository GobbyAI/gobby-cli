---
title: crates/gcode/src/commands/graph/reads.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/reads.rs
  ranges:
  - 19-25
  - 27-35
  - 37-43
  - 45-49
  - 51-59
  - 61-84
  - 86-101
  - 103-129
  - 131-136
  - 138-144
  - 146-152
  - 155-159
  - 162-172
  - 174-181
  - 183-214
  - 216-251
  - 253-266
  - 268-280
  - 282-291
  - 295-301
  - 303-332
  - 334-348
  - 350-383
  - 385-436
  - 438-502
  - 504-539
  - 541-562
  - 564-623
  - 640-643
  - 645-652
  - 654-661
  - 663-666
  - 669-674
  - 678-689
  - 692-695
  - 697-711
  - 713-722
  - 724-735
  - 737-756
  - 767-793
  - 801-825
  - 833-867
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/graph/reads.rs:19-25](crates/gcode/src/commands/graph/reads.rs#L19-L25), [crates/gcode/src/commands/graph/reads.rs:27-35](crates/gcode/src/commands/graph/reads.rs#L27-L35), [crates/gcode/src/commands/graph/reads.rs:37-43](crates/gcode/src/commands/graph/reads.rs#L37-L43), [crates/gcode/src/commands/graph/reads.rs:45-49](crates/gcode/src/commands/graph/reads.rs#L45-L49), [crates/gcode/src/commands/graph/reads.rs:51-59](crates/gcode/src/commands/graph/reads.rs#L51-L59), [crates/gcode/src/commands/graph/reads.rs:61-84](crates/gcode/src/commands/graph/reads.rs#L61-L84), [crates/gcode/src/commands/graph/reads.rs:86-101](crates/gcode/src/commands/graph/reads.rs#L86-L101), [crates/gcode/src/commands/graph/reads.rs:103-129](crates/gcode/src/commands/graph/reads.rs#L103-L129), [crates/gcode/src/commands/graph/reads.rs:131-136](crates/gcode/src/commands/graph/reads.rs#L131-L136), [crates/gcode/src/commands/graph/reads.rs:138-144](crates/gcode/src/commands/graph/reads.rs#L138-L144), [crates/gcode/src/commands/graph/reads.rs:146-152](crates/gcode/src/commands/graph/reads.rs#L146-L152), [crates/gcode/src/commands/graph/reads.rs:155-159](crates/gcode/src/commands/graph/reads.rs#L155-L159), [crates/gcode/src/commands/graph/reads.rs:162-172](crates/gcode/src/commands/graph/reads.rs#L162-L172), [crates/gcode/src/commands/graph/reads.rs:174-181](crates/gcode/src/commands/graph/reads.rs#L174-L181), [crates/gcode/src/commands/graph/reads.rs:183-214](crates/gcode/src/commands/graph/reads.rs#L183-L214), [crates/gcode/src/commands/graph/reads.rs:216-251](crates/gcode/src/commands/graph/reads.rs#L216-L251), [crates/gcode/src/commands/graph/reads.rs:253-266](crates/gcode/src/commands/graph/reads.rs#L253-L266), [crates/gcode/src/commands/graph/reads.rs:268-280](crates/gcode/src/commands/graph/reads.rs#L268-L280), [crates/gcode/src/commands/graph/reads.rs:282-291](crates/gcode/src/commands/graph/reads.rs#L282-L291), [crates/gcode/src/commands/graph/reads.rs:295-301](crates/gcode/src/commands/graph/reads.rs#L295-L301), [crates/gcode/src/commands/graph/reads.rs:303-332](crates/gcode/src/commands/graph/reads.rs#L303-L332), [crates/gcode/src/commands/graph/reads.rs:334-348](crates/gcode/src/commands/graph/reads.rs#L334-L348), [crates/gcode/src/commands/graph/reads.rs:350-383](crates/gcode/src/commands/graph/reads.rs#L350-L383), [crates/gcode/src/commands/graph/reads.rs:385-436](crates/gcode/src/commands/graph/reads.rs#L385-L436), [crates/gcode/src/commands/graph/reads.rs:438-502](crates/gcode/src/commands/graph/reads.rs#L438-L502), [crates/gcode/src/commands/graph/reads.rs:504-539](crates/gcode/src/commands/graph/reads.rs#L504-L539), [crates/gcode/src/commands/graph/reads.rs:541-562](crates/gcode/src/commands/graph/reads.rs#L541-L562), [crates/gcode/src/commands/graph/reads.rs:564-623](crates/gcode/src/commands/graph/reads.rs#L564-L623), [crates/gcode/src/commands/graph/reads.rs:640-643](crates/gcode/src/commands/graph/reads.rs#L640-L643), [crates/gcode/src/commands/graph/reads.rs:645-652](crates/gcode/src/commands/graph/reads.rs#L645-L652), [crates/gcode/src/commands/graph/reads.rs:654-661](crates/gcode/src/commands/graph/reads.rs#L654-L661), [crates/gcode/src/commands/graph/reads.rs:663-666](crates/gcode/src/commands/graph/reads.rs#L663-L666), [crates/gcode/src/commands/graph/reads.rs:669-674](crates/gcode/src/commands/graph/reads.rs#L669-L674), [crates/gcode/src/commands/graph/reads.rs:678-689](crates/gcode/src/commands/graph/reads.rs#L678-L689), [crates/gcode/src/commands/graph/reads.rs:692-695](crates/gcode/src/commands/graph/reads.rs#L692-L695), [crates/gcode/src/commands/graph/reads.rs:697-711](crates/gcode/src/commands/graph/reads.rs#L697-L711), [crates/gcode/src/commands/graph/reads.rs:713-722](crates/gcode/src/commands/graph/reads.rs#L713-L722), [crates/gcode/src/commands/graph/reads.rs:724-735](crates/gcode/src/commands/graph/reads.rs#L724-L735), [crates/gcode/src/commands/graph/reads.rs:737-756](crates/gcode/src/commands/graph/reads.rs#L737-L756), [crates/gcode/src/commands/graph/reads.rs:767-793](crates/gcode/src/commands/graph/reads.rs#L767-L793), [crates/gcode/src/commands/graph/reads.rs:801-825](crates/gcode/src/commands/graph/reads.rs#L801-L825), [crates/gcode/src/commands/graph/reads.rs:833-867](crates/gcode/src/commands/graph/reads.rs#L833-L867)

</details>

# crates/gcode/src/commands/graph/reads.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

Provides the read-side graph commands for Gobby, including caller, usage, import, path, and blast-radius lookups plus the helpers needed to resolve symbols, page results, format output, and report backend availability or refinement hints. The top-level command functions delegate to shared resolution and formatting helpers, which either print JSON or text responses, surface FalkorDB-related errors as user hints, and fall back to empty paged responses when graph reads are unavailable. The lower section includes test setup and cleanup utilities for seeding projects, files, and symbols, along with regression tests covering UUID resolution, unknown UUID handling, and ambiguous name behavior.
[crates/gcode/src/commands/graph/reads.rs:19-25]
[crates/gcode/src/commands/graph/reads.rs:27-35]
[crates/gcode/src/commands/graph/reads.rs:37-43]
[crates/gcode/src/commands/graph/reads.rs:45-49]
[crates/gcode/src/commands/graph/reads.rs:51-59]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `hint_for` | function | `fn hint_for(ctx: &Context) -> Option<String> {` | `hint_for [function]` | `f81f7279-8978-5e45-9f05-e8cc357474ad` | 19-25 [crates/gcode/src/commands/graph/reads.rs:19-25] | Indexed function `hint_for` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:19-25] |
| `hint_for_error` | function | `fn hint_for_error(ctx: &Context, error: &anyhow::Error) -> Option<String> {` | `hint_for_error [function]` | `e47250b0-9454-5e37-a69f-cb4873f792f9` | 27-35 [crates/gcode/src/commands/graph/reads.rs:27-35] | Indexed function `hint_for_error` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:27-35] |
| `print_graph_hint_text` | function | `fn print_graph_hint_text(ctx: &Context, error: Option<&anyhow::Error>) {` | `print_graph_hint_text [function]` | `14ce3e29-d446-530a-b807-422a02c99c38` | 37-43 [crates/gcode/src/commands/graph/reads.rs:37-43] | Indexed function `print_graph_hint_text` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:37-43] |
| `print_hint_text` | function | `fn print_hint_text(hint: Option<&str>) {` | `print_hint_text [function]` | `82be435d-61ce-5807-b440-876950f50447` | 45-49 [crates/gcode/src/commands/graph/reads.rs:45-49] | Indexed function `print_hint_text` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:45-49] |
| `graph_read_unavailable` | function | `fn graph_read_unavailable(error: &anyhow::Error) -> bool {` | `graph_read_unavailable [function]` | `972118ff-f49d-53fd-bdce-4bf98f62be78` | 51-59 [crates/gcode/src/commands/graph/reads.rs:51-59] | Indexed function `graph_read_unavailable` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:51-59] |
| `empty_paged_response` | function | `fn empty_paged_response<T: Serialize>(` | `empty_paged_response [function]` | `d94b4f46-b23c-52a0-990b-8944ca12144b` | 61-84 [crates/gcode/src/commands/graph/reads.rs:61-84] | Indexed function `empty_paged_response` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:61-84] |
| `graph_read_or_empty` | function | `fn graph_read_or_empty<T: Serialize>(` | `graph_read_or_empty [function]` | `13f9a0a6-7524-54c3-94de-3d76835a4f0d` | 86-101 [crates/gcode/src/commands/graph/reads.rs:86-101] | Indexed function `graph_read_or_empty` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:86-101] |
| `format_grouped_graph_results` | function | `pub(super) fn format_grouped_graph_results<F>(results: &[GraphResult], format_line: F) -> String` | `format_grouped_graph_results [function]` | `0fb3d396-03c9-541a-9c73-d07f85490021` | 103-129 [crates/gcode/src/commands/graph/reads.rs:103-129] | Indexed function `format_grouped_graph_results` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:103-129] |
| `format_caller_result_line` | function | `pub(super) fn format_caller_result_line(result: &GraphResult, target_name: &str) -> String {` | `format_caller_result_line [function]` | `f745fee1-f580-517d-b725-914a4138f7dc` | 131-136 [crates/gcode/src/commands/graph/reads.rs:131-136] | Indexed function `format_caller_result_line` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:131-136] |
| `format_usage_result_line` | function | `pub(super) fn format_usage_result_line(result: &GraphResult, target_name: &str) -> String {` | `format_usage_result_line [function]` | `eb09a7bc-5e13-556f-b0e3-af278485cd73` | 138-144 [crates/gcode/src/commands/graph/reads.rs:138-144] | Indexed function `format_usage_result_line` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:138-144] |
| `format_blast_radius_result_line` | function | `pub(super) fn format_blast_radius_result_line(result: &GraphResult) -> String {` | `format_blast_radius_result_line [function]` | `169e35c6-12c3-5878-9de5-25e6328c8593` | 146-152 [crates/gcode/src/commands/graph/reads.rs:146-152] | Indexed function `format_blast_radius_result_line` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:146-152] |
| `GraphPathEndpoint` | class | `struct GraphPathEndpoint {` | `GraphPathEndpoint [class]` | `015162b9-3c95-5088-b757-3ae14791d783` | 155-159 [crates/gcode/src/commands/graph/reads.rs:155-159] | Indexed class `GraphPathEndpoint` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:155-159] |
| `GraphPathResponse` | class | `struct GraphPathResponse {` | `GraphPathResponse [class]` | `2ac82dd1-1540-5aaf-ba3b-9304b08b5af9` | 162-172 [crates/gcode/src/commands/graph/reads.rs:162-172] | Indexed class `GraphPathResponse` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:162-172] |
| `path_endpoint` | function | `fn path_endpoint(input: &str, resolved: Option<&ResolvedGraphSymbol>) -> GraphPathEndpoint {` | `path_endpoint [function]` | `63e8f0d9-fe96-57ee-874f-569512fd7b29` | 174-181 [crates/gcode/src/commands/graph/reads.rs:174-181] | Indexed function `path_endpoint` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:174-181] |
| `format_symbol_path_text` | function | `pub(super) fn format_symbol_path_text(` | `format_symbol_path_text [function]` | `77173330-fed6-575c-b03d-0b9557eaeaa6` | 183-214 [crates/gcode/src/commands/graph/reads.rs:183-214] | Indexed function `format_symbol_path_text` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:183-214] |
| `print_symbol_path_response` | function | `fn print_symbol_path_response(` | `print_symbol_path_response [function]` | `e62c3497-5a8e-5864-a03c-b46ce9f3552d` | 216-251 [crates/gcode/src/commands/graph/reads.rs:216-251] | Indexed function `print_symbol_path_response` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:216-251] |
| `resolve_symbol_with_connection` | function | `fn resolve_symbol_with_connection(` | `resolve_symbol_with_connection [function]` | `443cc001-2d98-5d61-8b65-e2f533220395` | 253-266 [crates/gcode/src/commands/graph/reads.rs:253-266] | Indexed function `resolve_symbol_with_connection` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:253-266] |
| `resolve_symbol_candidates` | function | `fn resolve_symbol_candidates(` | `resolve_symbol_candidates [function]` | `d3fae140-6b96-5b43-bc30-33764f38b7f4` | 268-280 [crates/gcode/src/commands/graph/reads.rs:268-280] | Indexed function `resolve_symbol_candidates` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:268-280] |
| `print_symbol_resolution_failure` | function | `fn print_symbol_resolution_failure(input: &str, suggestions: &[String]) {` | `print_symbol_resolution_failure [function]` | `6bfe6d6d-e482-536c-b18a-62ffd5a30089` | 282-291 [crates/gcode/src/commands/graph/reads.rs:282-291] | Indexed function `print_symbol_resolution_failure` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:282-291] |
| `resolve_symbol` | function | `fn resolve_symbol(ctx: &Context, input: &str) -> anyhow::Result<Option<ResolvedGraphSymbol>> {` | `resolve_symbol [function]` | `25486561-4cf6-553a-b2fa-99598f9b8282` | 295-301 [crates/gcode/src/commands/graph/reads.rs:295-301] | Indexed function `resolve_symbol` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:295-301] |
| `resolve_blast_radius_target` | function | `fn resolve_blast_radius_target(` | `resolve_blast_radius_target [function]` | `b3b5e81e-12d7-5acb-9fc4-01d9f63bf0f4` | 303-332 [crates/gcode/src/commands/graph/reads.rs:303-332] | Indexed function `resolve_blast_radius_target` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:303-332] |
| `resolve_symbol_or_empty_response` | function | `fn resolve_symbol_or_empty_response(` | `resolve_symbol_or_empty_response [function]` | `048e587f-6251-5283-8cbf-c5ec0110d70f` | 334-348 [crates/gcode/src/commands/graph/reads.rs:334-348] | Indexed function `resolve_symbol_or_empty_response` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:334-348] |
| `read_paged_symbol_graph_results` | function | `fn read_paged_symbol_graph_results(` | `read_paged_symbol_graph_results [function]` | `f2aecd7f-9a0e-5fc9-bd5b-9bc53ea93837` | 350-383 [crates/gcode/src/commands/graph/reads.rs:350-383] | Indexed function `read_paged_symbol_graph_results` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:350-383] |
| `callers` | function | `pub fn callers(` | `callers [function]` | `cb97cbc9-f10b-50cc-bfde-27552e9e63bb` | 385-436 [crates/gcode/src/commands/graph/reads.rs:385-436] | Indexed function `callers` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:385-436] |
| `usages` | function | `pub fn usages(` | `usages [function]` | `6228a8be-fbee-5193-b24c-14d28ed56367` | 438-502 [crates/gcode/src/commands/graph/reads.rs:438-502] | Indexed function `usages` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:438-502] |
| `imports` | function | `pub fn imports(ctx: &Context, file: &str, format: Format) -> anyhow::Result<()> {` | `imports [function]` | `c1ccc4a9-4661-59e9-b7ca-4206c4687fec` | 504-539 [crates/gcode/src/commands/graph/reads.rs:504-539] | Indexed function `imports` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:504-539] |
| `path` | function | `pub fn path(` | `path [function]` | `d9c34928-fab1-5011-8c73-79807399e840` | 541-562 [crates/gcode/src/commands/graph/reads.rs:541-562] | Indexed function `path` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:541-562] |
| `blast_radius` | function | `pub fn blast_radius(` | `blast_radius [function]` | `2115d586-cc0b-5558-b5e7-7945827071bf` | 564-623 [crates/gcode/src/commands/graph/reads.rs:564-623] | Indexed function `blast_radius` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:564-623] |
| `graph_resolution_database_url` | function | `fn graph_resolution_database_url() -> String {` | `graph_resolution_database_url [function]` | `1064255e-a372-5c5d-99fa-bba0b1882f0a` | 640-643 [crates/gcode/src/commands/graph/reads.rs:640-643] | Indexed function `graph_resolution_database_url` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:640-643] |
| `connect_graph_resolution_test_db` | function | `fn connect_graph_resolution_test_db() -> Client {` | `connect_graph_resolution_test_db [function]` | `1d6569ae-b841-5a48-bad6-f7a113a18530` | 645-652 [crates/gcode/src/commands/graph/reads.rs:645-652] | Indexed function `connect_graph_resolution_test_db` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:645-652] |
| `unique_uuid` | function | `fn unique_uuid(label: &str) -> String {` | `unique_uuid [function]` | `ee8266e4-16e2-5748-bec3-9bb4cab6e9e6` | 654-661 [crates/gcode/src/commands/graph/reads.rs:654-661] | Indexed function `unique_uuid` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:654-661] |
| `GraphResolutionProjectCleanup` | class | `struct GraphResolutionProjectCleanup {` | `GraphResolutionProjectCleanup [class]` | `f910138d-d753-5e66-9fcc-9dd3d89fa3a9` | 663-666 [crates/gcode/src/commands/graph/reads.rs:663-666] | Indexed class `GraphResolutionProjectCleanup` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:663-666] |
| `GraphResolutionProjectCleanup::new` | method | `fn new(project_id: &str) -> Self {` | `GraphResolutionProjectCleanup::new [method]` | `a914c2f3-b897-54ad-b505-1626fd7d8fc8` | 669-674 [crates/gcode/src/commands/graph/reads.rs:669-674] | Indexed method `GraphResolutionProjectCleanup::new` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:669-674] |
| `GraphResolutionProjectCleanup::drop` | method | `fn drop(&mut self) {` | `GraphResolutionProjectCleanup::drop [method]` | `604ce29b-1924-53a0-b174-858e57b580e9` | 678-689 [crates/gcode/src/commands/graph/reads.rs:678-689] | Indexed method `GraphResolutionProjectCleanup::drop` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:678-689] |
| `cleanup_graph_resolution_project` | function | `fn cleanup_graph_resolution_project(conn: &mut Client, project_id: &str) {` | `cleanup_graph_resolution_project [function]` | `f93e513c-4e8c-5637-bd13-c39f821a8f2b` | 692-695 [crates/gcode/src/commands/graph/reads.rs:692-695] | Indexed function `cleanup_graph_resolution_project` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:692-695] |
| `try_cleanup_graph_resolution_project` | function | `fn try_cleanup_graph_resolution_project(` | `try_cleanup_graph_resolution_project [function]` | `c2ccf457-53f5-52cd-921f-a6ca894cc79d` | 697-711 [crates/gcode/src/commands/graph/reads.rs:697-711] | Indexed function `try_cleanup_graph_resolution_project` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:697-711] |
| `insert_project` | function | `fn insert_project(conn: &mut Client, project_id: &str) {` | `insert_project [function]` | `087d30ea-8b7f-59be-91d6-6dcdbe545dd1` | 713-722 [crates/gcode/src/commands/graph/reads.rs:713-722] | Indexed function `insert_project` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:713-722] |
| `insert_file` | function | `fn insert_file(conn: &mut Client, project_id: &str, file_path: &str, symbol_count: i32) {` | `insert_file [function]` | `998fa8af-9973-57e2-931b-d02906885e25` | 724-735 [crates/gcode/src/commands/graph/reads.rs:724-735] | Indexed function `insert_file` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:724-735] |
| `insert_symbol` | function | `fn insert_symbol(` | `insert_symbol [function]` | `591b33ec-562f-59cb-864d-060a2a81e9e5` | 737-756 [crates/gcode/src/commands/graph/reads.rs:737-756] | Indexed function `insert_symbol` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:737-756] |
| `uuid_input_resolves_exact_symbol_for_active_project` | function | `fn uuid_input_resolves_exact_symbol_for_active_project() {` | `uuid_input_resolves_exact_symbol_for_active_project [function]` | `faecd264-a32f-562b-8639-e50d029ccb85` | 767-793 [crates/gcode/src/commands/graph/reads.rs:767-793] | Indexed function `uuid_input_resolves_exact_symbol_for_active_project` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:767-793] |
| `unknown_uuid_input_does_not_fall_back_to_name_resolution` | function | `fn unknown_uuid_input_does_not_fall_back_to_name_resolution() {` | `unknown_uuid_input_does_not_fall_back_to_name_resolution [function]` | `2048167d-b65b-5844-9116-ae6539902a39` | 801-825 [crates/gcode/src/commands/graph/reads.rs:801-825] | Indexed function `unknown_uuid_input_does_not_fall_back_to_name_resolution` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:801-825] |
| `ambiguous_name_behavior_remains_unchanged` | function | `fn ambiguous_name_behavior_remains_unchanged() {` | `ambiguous_name_behavior_remains_unchanged [function]` | `44efcb85-6330-501b-9f14-7aca6d56b4a4` | 833-867 [crates/gcode/src/commands/graph/reads.rs:833-867] | Indexed function `ambiguous_name_behavior_remains_unchanged` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:833-867] |
