---
title: crates/gwiki/src/commands/index.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/index.rs
  ranges:
  - 35-38
  - 40-46
  - 48-52
  - 54-86
  - 88-153
  - 155-191
  - 193-205
  - 207-229
  - 231-254
  - 256-258
  - 260-266
  - 268-272
  - 274-281
  - 283-288
  - 290-314
  - 316-367
  - 369-371
  - 373-375
  - 377-387
  - 389-394
  - 396-431
  - 433-457
  - 459-469
  - 471-512
  - 514-569
  - 571-641
  - 643-653
  - 659-661
  - 664-668
  - 670-672
  - 676-683
  - 686-703
  - 706-730
  - 734-739
  - 741-749
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/index.rs:35-38](crates/gwiki/src/commands/index.rs#L35-L38), [crates/gwiki/src/commands/index.rs:40-46](crates/gwiki/src/commands/index.rs#L40-L46), [crates/gwiki/src/commands/index.rs:48-52](crates/gwiki/src/commands/index.rs#L48-L52), [crates/gwiki/src/commands/index.rs:54-86](crates/gwiki/src/commands/index.rs#L54-L86), [crates/gwiki/src/commands/index.rs:88-153](crates/gwiki/src/commands/index.rs#L88-L153), [crates/gwiki/src/commands/index.rs:155-191](crates/gwiki/src/commands/index.rs#L155-L191), [crates/gwiki/src/commands/index.rs:193-205](crates/gwiki/src/commands/index.rs#L193-L205), [crates/gwiki/src/commands/index.rs:207-229](crates/gwiki/src/commands/index.rs#L207-L229), [crates/gwiki/src/commands/index.rs:231-254](crates/gwiki/src/commands/index.rs#L231-L254), [crates/gwiki/src/commands/index.rs:256-258](crates/gwiki/src/commands/index.rs#L256-L258), [crates/gwiki/src/commands/index.rs:260-266](crates/gwiki/src/commands/index.rs#L260-L266), [crates/gwiki/src/commands/index.rs:268-272](crates/gwiki/src/commands/index.rs#L268-L272), [crates/gwiki/src/commands/index.rs:274-281](crates/gwiki/src/commands/index.rs#L274-L281), [crates/gwiki/src/commands/index.rs:283-288](crates/gwiki/src/commands/index.rs#L283-L288), [crates/gwiki/src/commands/index.rs:290-314](crates/gwiki/src/commands/index.rs#L290-L314), [crates/gwiki/src/commands/index.rs:316-367](crates/gwiki/src/commands/index.rs#L316-L367), [crates/gwiki/src/commands/index.rs:369-371](crates/gwiki/src/commands/index.rs#L369-L371), [crates/gwiki/src/commands/index.rs:373-375](crates/gwiki/src/commands/index.rs#L373-L375), [crates/gwiki/src/commands/index.rs:377-387](crates/gwiki/src/commands/index.rs#L377-L387), [crates/gwiki/src/commands/index.rs:389-394](crates/gwiki/src/commands/index.rs#L389-L394), [crates/gwiki/src/commands/index.rs:396-431](crates/gwiki/src/commands/index.rs#L396-L431), [crates/gwiki/src/commands/index.rs:433-457](crates/gwiki/src/commands/index.rs#L433-L457), [crates/gwiki/src/commands/index.rs:459-469](crates/gwiki/src/commands/index.rs#L459-L469), [crates/gwiki/src/commands/index.rs:471-512](crates/gwiki/src/commands/index.rs#L471-L512), [crates/gwiki/src/commands/index.rs:514-569](crates/gwiki/src/commands/index.rs#L514-L569), [crates/gwiki/src/commands/index.rs:571-641](crates/gwiki/src/commands/index.rs#L571-L641), [crates/gwiki/src/commands/index.rs:643-653](crates/gwiki/src/commands/index.rs#L643-L653), [crates/gwiki/src/commands/index.rs:659-661](crates/gwiki/src/commands/index.rs#L659-L661), [crates/gwiki/src/commands/index.rs:664-668](crates/gwiki/src/commands/index.rs#L664-L668), [crates/gwiki/src/commands/index.rs:670-672](crates/gwiki/src/commands/index.rs#L670-L672), [crates/gwiki/src/commands/index.rs:676-683](crates/gwiki/src/commands/index.rs#L676-L683), [crates/gwiki/src/commands/index.rs:686-703](crates/gwiki/src/commands/index.rs#L686-L703), [crates/gwiki/src/commands/index.rs:706-730](crates/gwiki/src/commands/index.rs#L706-L730), [crates/gwiki/src/commands/index.rs:734-739](crates/gwiki/src/commands/index.rs#L734-L739), [crates/gwiki/src/commands/index.rs:741-749](crates/gwiki/src/commands/index.rs#L741-L749)

</details>

# crates/gwiki/src/commands/index.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `gwiki index` command for a resolved scope: it ensures the scope is rooted, indexes content into Postgres, FalkorDB, and Qdrant when configured, resolves AI/embedding settings and fallback routes, and records any service degradations encountered during sync. It also includes rendering helpers for the index and ingest views, configuration and connection helpers, scope setup, and tests covering invalid video frame intervals, degradation reporting, and embedding fallback behavior.
[crates/gwiki/src/commands/index.rs:35-38]
[crates/gwiki/src/commands/index.rs:40-46]
[crates/gwiki/src/commands/index.rs:48-52]
[crates/gwiki/src/commands/index.rs:54-86]
[crates/gwiki/src/commands/index.rs:88-153]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IndexReport` | class | `struct IndexReport {` | `IndexReport [class]` | `841f90e8-756b-5f27-999e-57a7ec5d9b09` | 35-38 [crates/gwiki/src/commands/index.rs:35-38] | Indexed class `IndexReport` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:35-38] |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `678c88e9-6753-57dc-a8e3-e1e21e3ecfbc` | 40-46 [crates/gwiki/src/commands/index.rs:40-46] | Indexed function `execute` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:40-46] |
| `index_resolved_scope` | function | `pub(crate) fn index_resolved_scope(` | `index_resolved_scope [function]` | `37703920-7301-538b-8d5e-31f0b51a00ea` | 48-52 [crates/gwiki/src/commands/index.rs:48-52] | Indexed function `index_resolved_scope` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:48-52] |
| `index_resolved_scope_report` | function | `fn index_resolved_scope_report(` | `index_resolved_scope_report [function]` | `e7aa8d66-45f1-53aa-83e0-dc2c1689cc42` | 54-86 [crates/gwiki/src/commands/index.rs:54-86] | Indexed function `index_resolved_scope_report` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:54-86] |
| `execute_ingest_file` | function | `pub(crate) fn execute_ingest_file(` | `execute_ingest_file [function]` | `77dbe63b-0177-50c3-8465-0a851f1d031b` | 88-153 [crates/gwiki/src/commands/index.rs:88-153] | Indexed function `execute_ingest_file` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:88-153] |
| `execute_ingest_url` | function | `pub(crate) fn execute_ingest_url(` | `execute_ingest_url [function]` | `ecf220bb-76ab-5eb1-bfd5-660fa389652d` | 155-191 [crates/gwiki/src/commands/index.rs:155-191] | Indexed function `execute_ingest_url` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:155-191] |
| `resolve_ingest_ai_context` | function | `fn resolve_ingest_ai_context(` | `resolve_ingest_ai_context [function]` | `9729101d-7abb-55a0-a226-979234dd085a` | 193-205 [crates/gwiki/src/commands/index.rs:193-205] | Indexed function `resolve_ingest_ai_context` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:193-205] |
| `resolve_ingest_file_ai_context` | function | `pub(crate) fn resolve_ingest_file_ai_context(` | `resolve_ingest_file_ai_context [function]` | `cfbe3467-16d0-567b-94b9-2c6e77dba77b` | 207-229 [crates/gwiki/src/commands/index.rs:207-229] | Indexed function `resolve_ingest_file_ai_context` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:207-229] |
| `resolve_video_frame_interval_seconds` | function | `fn resolve_video_frame_interval_seconds(source: &mut impl ConfigSource) -> Result<u32, WikiError> {` | `resolve_video_frame_interval_seconds [function]` | `59c4b099-4d0e-521f-958b-c4bdd8c0d5f2` | 231-254 [crates/gwiki/src/commands/index.rs:231-254] | Indexed function `resolve_video_frame_interval_seconds` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:231-254] |
| `ai_project_id` | function | `fn ai_project_id(scope: &ScopeIdentity) -> Option<String> {` | `ai_project_id [function]` | `c64a5c44-b124-5b2c-9f89-31495292256a` | 256-258 [crates/gwiki/src/commands/index.rs:256-258] | Indexed function `ai_project_id` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:256-258] |
| `ai_project_id_for_search` | function | `fn ai_project_id_for_search(scope: &SearchScope) -> Option<String> {` | `ai_project_id_for_search [function]` | `c009b1dd-36e8-58ec-9f9b-f4695741fd3c` | 260-266 [crates/gwiki/src/commands/index.rs:260-266] | Indexed function `ai_project_id_for_search` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:260-266] |
| `gobby_home` | function | `fn gobby_home() -> Result<PathBuf, WikiError> {` | `gobby_home [function]` | `2be8454c-2cb6-5653-a99f-2738e4b40648` | 268-272 [crates/gwiki/src/commands/index.rs:268-272] | Indexed function `gobby_home` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:268-272] |
| `connect_postgres_index` | function | `pub(crate) fn connect_postgres_index(` | `connect_postgres_index [function]` | `017829fc-abe9-5a85-93fb-fcc437d7ce86` | 274-281 [crates/gwiki/src/commands/index.rs:274-281] | Indexed function `connect_postgres_index` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:274-281] |
| `postgres_store_for_search` | function | `pub(crate) fn postgres_store_for_search<'a>(` | `postgres_store_for_search [function]` | `c91455af-08ad-528e-aa02-216b0139ee5a` | 283-288 [crates/gwiki/src/commands/index.rs:283-288] | Indexed function `postgres_store_for_search` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:283-288] |
| `sync_falkor_graph` | function | `pub(crate) fn sync_falkor_graph(` | `sync_falkor_graph [function]` | `c59e77d6-1349-51c4-afca-de579c5061a0` | 290-314 [crates/gwiki/src/commands/index.rs:290-314] | Indexed function `sync_falkor_graph` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:290-314] |
| `sync_qdrant_vectors` | function | `pub(crate) fn sync_qdrant_vectors(` | `sync_qdrant_vectors [function]` | `10baeb3a-a503-5f88-849b-57091ca43562` | 316-367 [crates/gwiki/src/commands/index.rs:316-367] | Indexed function `sync_qdrant_vectors` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:316-367] |
| `qdrant_sync_degradation` | function | `fn qdrant_sync_degradation(error: vector::WikiVectorError) -> DegradationKind {` | `qdrant_sync_degradation [function]` | `05120f24-5264-5bf8-882f-44192a8ec13f` | 369-371 [crates/gwiki/src/commands/index.rs:369-371] | Indexed function `qdrant_sync_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:369-371] |
| `not_configured_degradation` | function | `fn not_configured_degradation(service: &'static str) -> DegradationKind {` | `not_configured_degradation [function]` | `91ecb7ce-057d-5d92-b5bb-e053aab62811` | 373-375 [crates/gwiki/src/commands/index.rs:373-375] | Indexed function `not_configured_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:373-375] |
| `unreachable_degradation` | function | `fn unreachable_degradation(` | `unreachable_degradation [function]` | `7cda6d41-3536-520c-8c04-0ee5234a0005` | 377-387 [crates/gwiki/src/commands/index.rs:377-387] | Indexed function `unreachable_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:377-387] |
| `service_unavailable_degradation` | function | `fn service_unavailable_degradation(service: &'static str, state: ServiceState) -> DegradationKind {` | `service_unavailable_degradation [function]` | `88c2f3bc-7002-515a-9314-843b6f3b4e7d` | 389-394 [crates/gwiki/src/commands/index.rs:389-394] | Indexed function `service_unavailable_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:389-394] |
| `resolve_vector_embedding` | function | `fn resolve_vector_embedding(` | `resolve_vector_embedding [function]` | `62748350-39ce-5563-b414-a27e611517ae` | 396-431 [crates/gwiki/src/commands/index.rs:396-431] | Indexed function `resolve_vector_embedding` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:396-431] |
| `effective_embedding_route` | function | `fn effective_embedding_route(context: &AiContext) -> AiRouting {` | `effective_embedding_route [function]` | `9375464e-566e-5f4a-9ff2-347ecd87c323` | 433-457 [crates/gwiki/src/commands/index.rs:433-457] | Indexed function `effective_embedding_route` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:433-457] |
| `indexed_counts_for_postgres` | function | `pub(crate) fn indexed_counts_for_postgres(` | `indexed_counts_for_postgres [function]` | `1b3f2a45-adca-5f0e-aa75-d93bf7f85ca8` | 459-469 [crates/gwiki/src/commands/index.rs:459-469] | Indexed function `indexed_counts_for_postgres` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:459-469] |
| `render_index` | function | `fn render_index(scope: ScopeIdentity, root: &Path, report: IndexReport) -> CommandOutcome {` | `render_index [function]` | `603f7c72-47ab-5ca9-b4c9-6ea98ffdcad0` | 471-512 [crates/gwiki/src/commands/index.rs:471-512] | Indexed function `render_index` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:471-512] |
| `render_ingest_file` | function | `fn render_ingest_file(` | `render_ingest_file [function]` | `f1233874-88a5-5a1d-b7eb-7050222be3f9` | 514-569 [crates/gwiki/src/commands/index.rs:514-569] | Indexed function `render_ingest_file` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:514-569] |
| `render_ingest_url` | function | `fn render_ingest_url(` | `render_ingest_url [function]` | `8c9334cd-28d9-50d7-b473-3f8156fb43b4` | 571-641 [crates/gwiki/src/commands/index.rs:571-641] | Indexed function `render_ingest_url` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:571-641] |
| `ensure_scope_root` | function | `fn ensure_scope_root(scope: &crate::scope::ResolvedScope) -> Result<(), WikiError> {` | `ensure_scope_root [function]` | `90912db1-5290-573c-8abf-30b10e5023aa` | 643-653 [crates/gwiki/src/commands/index.rs:643-653] | Indexed function `ensure_scope_root` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:643-653] |
| `TestConfigSource` | class | `struct TestConfigSource {` | `TestConfigSource [class]` | `0158f309-b3f0-52de-bf24-0a95bea82d7b` | 659-661 [crates/gwiki/src/commands/index.rs:659-661] | Indexed class `TestConfigSource` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:659-661] |
| `TestConfigSource::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `TestConfigSource::config_value [method]` | `cdb8e45d-c306-521f-8209-e9811c2e38c7` | 664-668 [crates/gwiki/src/commands/index.rs:664-668] | Indexed method `TestConfigSource::config_value` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:664-668] |
| `TestConfigSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `TestConfigSource::resolve_value [method]` | `460ca48f-3a85-5f1e-9a89-405de48ac9bc` | 670-672 [crates/gwiki/src/commands/index.rs:670-672] | Indexed method `TestConfigSource::resolve_value` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:670-672] |
| `video_frame_interval_zero_is_invalid` | function | `fn video_frame_interval_zero_is_invalid() {` | `video_frame_interval_zero_is_invalid [function]` | `61424c80-3c71-52e7-8079-b41b7995d8a7` | 676-683 [crates/gwiki/src/commands/index.rs:676-683] | Indexed function `video_frame_interval_zero_is_invalid` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:676-683] |
| `index_render_includes_empty_degradations` | function | `fn index_render_includes_empty_degradations() {` | `index_render_includes_empty_degradations [function]` | `7341585c-00d0-596f-8a7a-92bf69ae07a6` | 686-703 [crates/gwiki/src/commands/index.rs:686-703] | Indexed function `index_render_includes_empty_degradations` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:686-703] |
| `index_render_reports_qdrant_sync_failure_degradation` | function | `fn index_render_reports_qdrant_sync_failure_degradation() {` | `index_render_reports_qdrant_sync_failure_degradation [function]` | `fd10def5-a300-5d2e-af98-e670d51fe509` | 706-730 [crates/gwiki/src/commands/index.rs:706-730] | Indexed function `index_render_reports_qdrant_sync_failure_degradation` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:706-730] |
| `auto_embedding_route_falls_back_to_direct_without_ai` | function | `fn auto_embedding_route_falls_back_to_direct_without_ai() {` | `auto_embedding_route_falls_back_to_direct_without_ai [function]` | `02f7443f-238f-5c55-8f31-8000a6693f50` | 734-739 [crates/gwiki/src/commands/index.rs:734-739] | Indexed function `auto_embedding_route_falls_back_to_direct_without_ai` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:734-739] |
| `sample_counts` | function | `fn sample_counts() -> IndexCounts {` | `sample_counts [function]` | `c7cc715c-b9a9-5a7a-82de-9e217fe8c7fb` | 741-749 [crates/gwiki/src/commands/index.rs:741-749] | Indexed function `sample_counts` in `crates/gwiki/src/commands/index.rs`. [crates/gwiki/src/commands/index.rs:741-749] |
