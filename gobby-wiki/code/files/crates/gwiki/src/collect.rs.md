---
title: crates/gwiki/src/collect.rs
type: code_file
provenance:
- file: crates/gwiki/src/collect.rs
  ranges:
  - 18-21
  - 24-30
  - 34-37
  - 39-42
  - 44-46
  - 48-140
  - 142-152
  - 154-165
  - 167-179
  - 181-204
  - 206-327
  - 329-352
  - 354-361
  - 363-390
  - 392-398
  - 400-418
  - 420-433
  - 435-480
  - 482-501
  - 503-550
  - 552-572
  - 574-588
  - 590-592
  - 594-604
  - 606-610
  - 612-615
  - 617-622
  - 624-628
  - 630-636
  - 638-642
  - 644-646
  - 648-654
  - 665-671
  - 674-736
  - 739-768
  - 771-781
  - 784-789
  - 792-797
  - 800-815
  - 818-830
  - 833-847
  - 850-866
  - 869-892
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/collect.rs:18-21](crates/gwiki/src/collect.rs#L18-L21), [crates/gwiki/src/collect.rs:24-30](crates/gwiki/src/collect.rs#L24-L30), [crates/gwiki/src/collect.rs:34-37](crates/gwiki/src/collect.rs#L34-L37), [crates/gwiki/src/collect.rs:39-42](crates/gwiki/src/collect.rs#L39-L42), [crates/gwiki/src/collect.rs:44-46](crates/gwiki/src/collect.rs#L44-L46), [crates/gwiki/src/collect.rs:48-140](crates/gwiki/src/collect.rs#L48-L140), [crates/gwiki/src/collect.rs:142-152](crates/gwiki/src/collect.rs#L142-L152), [crates/gwiki/src/collect.rs:154-165](crates/gwiki/src/collect.rs#L154-L165), [crates/gwiki/src/collect.rs:167-179](crates/gwiki/src/collect.rs#L167-L179), [crates/gwiki/src/collect.rs:181-204](crates/gwiki/src/collect.rs#L181-L204), [crates/gwiki/src/collect.rs:206-327](crates/gwiki/src/collect.rs#L206-L327), [crates/gwiki/src/collect.rs:329-352](crates/gwiki/src/collect.rs#L329-L352), [crates/gwiki/src/collect.rs:354-361](crates/gwiki/src/collect.rs#L354-L361), [crates/gwiki/src/collect.rs:363-390](crates/gwiki/src/collect.rs#L363-L390), [crates/gwiki/src/collect.rs:392-398](crates/gwiki/src/collect.rs#L392-L398), [crates/gwiki/src/collect.rs:400-418](crates/gwiki/src/collect.rs#L400-L418), [crates/gwiki/src/collect.rs:420-433](crates/gwiki/src/collect.rs#L420-L433), [crates/gwiki/src/collect.rs:435-480](crates/gwiki/src/collect.rs#L435-L480), [crates/gwiki/src/collect.rs:482-501](crates/gwiki/src/collect.rs#L482-L501), [crates/gwiki/src/collect.rs:503-550](crates/gwiki/src/collect.rs#L503-L550), [crates/gwiki/src/collect.rs:552-572](crates/gwiki/src/collect.rs#L552-L572), [crates/gwiki/src/collect.rs:574-588](crates/gwiki/src/collect.rs#L574-L588), [crates/gwiki/src/collect.rs:590-592](crates/gwiki/src/collect.rs#L590-L592), [crates/gwiki/src/collect.rs:594-604](crates/gwiki/src/collect.rs#L594-L604), [crates/gwiki/src/collect.rs:606-610](crates/gwiki/src/collect.rs#L606-L610), [crates/gwiki/src/collect.rs:612-615](crates/gwiki/src/collect.rs#L612-L615), [crates/gwiki/src/collect.rs:617-622](crates/gwiki/src/collect.rs#L617-L622), [crates/gwiki/src/collect.rs:624-628](crates/gwiki/src/collect.rs#L624-L628), [crates/gwiki/src/collect.rs:630-636](crates/gwiki/src/collect.rs#L630-L636), [crates/gwiki/src/collect.rs:638-642](crates/gwiki/src/collect.rs#L638-L642), [crates/gwiki/src/collect.rs:644-646](crates/gwiki/src/collect.rs#L644-L646), [crates/gwiki/src/collect.rs:648-654](crates/gwiki/src/collect.rs#L648-L654), [crates/gwiki/src/collect.rs:665-671](crates/gwiki/src/collect.rs#L665-L671), [crates/gwiki/src/collect.rs:674-736](crates/gwiki/src/collect.rs#L674-L736), [crates/gwiki/src/collect.rs:739-768](crates/gwiki/src/collect.rs#L739-L768), [crates/gwiki/src/collect.rs:771-781](crates/gwiki/src/collect.rs#L771-L781), [crates/gwiki/src/collect.rs:784-789](crates/gwiki/src/collect.rs#L784-L789), [crates/gwiki/src/collect.rs:792-797](crates/gwiki/src/collect.rs#L792-L797), [crates/gwiki/src/collect.rs:800-815](crates/gwiki/src/collect.rs#L800-L815), [crates/gwiki/src/collect.rs:818-830](crates/gwiki/src/collect.rs#L818-L830), [crates/gwiki/src/collect.rs:833-847](crates/gwiki/src/collect.rs#L833-L847), [crates/gwiki/src/collect.rs:850-866](crates/gwiki/src/collect.rs#L850-L866), [crates/gwiki/src/collect.rs:869-892](crates/gwiki/src/collect.rs#L869-L892)

</details>

# crates/gwiki/src/collect.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Collects items from a wiki vault’s `inbox`, classifies each entry as a URL or file, and either accepts it into ingestion/indexing or skips it with a recorded reason. `CollectReport`, `CollectAction`, and `CollectStatus` capture the outcome, while helper functions handle path setup, URL/file parsing, asset and sidecar writes, cleanup, and logging so collection stays consistent and recoverable.
[crates/gwiki/src/collect.rs:18-21]
[crates/gwiki/src/collect.rs:24-30]
[crates/gwiki/src/collect.rs:34-37]
[crates/gwiki/src/collect.rs:39-42]
[crates/gwiki/src/collect.rs:44-46]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CollectReport` | class | `pub struct CollectReport {` | `CollectReport [class]` | `a2a6ff71-4dc8-50a8-a76a-9f5fddfe583f` | 18-21 [crates/gwiki/src/collect.rs:18-21] | Indexed class `CollectReport` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:18-21] |
| `CollectAction` | class | `pub struct CollectAction {` | `CollectAction [class]` | `d7d0df0c-b0d9-5951-a7b9-f4be0cc190c4` | 24-30 [crates/gwiki/src/collect.rs:24-30] | Indexed class `CollectAction` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:24-30] |
| `CollectStatus` | type | `pub enum CollectStatus {` | `CollectStatus [type]` | `de97cf70-c4cd-58ad-92f7-211c2d47c156` | 34-37 [crates/gwiki/src/collect.rs:34-37] | Indexed type `CollectStatus` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:34-37] |
| `InboxKind` | type | `enum InboxKind {` | `InboxKind [type]` | `8c3d7c40-320b-5af0-96af-58df726b75b6` | 39-42 [crates/gwiki/src/collect.rs:39-42] | Indexed type `InboxKind` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:39-42] |
| `collect_inbox` | function | `pub fn collect_inbox(vault_root: &Path, fetched_at: &str) -> Result<CollectReport, WikiError> {` | `collect_inbox [function]` | `e21fb410-42f5-536d-98a9-7de2dcf937fd` | 44-46 [crates/gwiki/src/collect.rs:44-46] | Indexed function `collect_inbox` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:44-46] |
| `collect_inbox_with_limit` | function | `fn collect_inbox_with_limit(` | `collect_inbox_with_limit [function]` | `de9718bb-29aa-56f1-90f7-e2111b7c8ec1` | 48-140 [crates/gwiki/src/collect.rs:48-140] | Indexed function `collect_inbox_with_limit` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:48-140] |
| `collect_inbox_and_index` | function | `pub fn collect_inbox_and_index(` | `collect_inbox_and_index [function]` | `4b012167-1d3b-5e5e-958b-a751463923a8` | 142-152 [crates/gwiki/src/collect.rs:142-152] | Indexed function `collect_inbox_and_index` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:142-152] |
| `read_inbox_item_limited` | function | `fn read_inbox_item_limited(path: &Path, max_item_bytes: u64) -> Result<Option<Vec<u8>>, WikiError> {` | `read_inbox_item_limited [function]` | `54050517-d717-5f21-ad95-08629a17fde7` | 154-165 [crates/gwiki/src/collect.rs:154-165] | Indexed function `read_inbox_item_limited` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:154-165] |
| `ensure_collect_paths` | function | `fn ensure_collect_paths(vault_root: &Path) -> Result<(), WikiError> {` | `ensure_collect_paths [function]` | `ebdbb025-23dc-52f1-84aa-3fbc89097ab9` | 167-179 [crates/gwiki/src/collect.rs:167-179] | Indexed function `ensure_collect_paths` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:167-179] |
| `classify_inbox_item` | function | `fn classify_inbox_item(path: &Path, bytes: &[u8]) -> Result<InboxKind, &'static str> {` | `classify_inbox_item [function]` | `f3940301-8a05-537c-a936-065d55d7da70` | 181-204 [crates/gwiki/src/collect.rs:181-204] | Indexed function `classify_inbox_item` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:181-204] |
| `accept_item` | function | `fn accept_item(` | `accept_item [function]` | `81a74962-57ec-5ee4-a099-96a73bafc21e` | 206-327 [crates/gwiki/src/collect.rs:206-327] | Indexed function `accept_item` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:206-327] |
| `rollback_registered_collect_source` | function | `fn rollback_registered_collect_source<T>(` | `rollback_registered_collect_source [function]` | `b5db18f0-6142-5be6-a224-66cfe1154b8b` | 329-352 [crates/gwiki/src/collect.rs:329-352] | Indexed function `rollback_registered_collect_source` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:329-352] |
| `cleanup_collect_file` | function | `fn cleanup_collect_file(vault_root: &Path, relative_path: &Path, cleanup_errors: &mut Vec<String>) {` | `cleanup_collect_file [function]` | `76d1bca4-1b33-54e0-8369-b8a8656ad5f8` | 354-361 [crates/gwiki/src/collect.rs:354-361] | Indexed function `cleanup_collect_file` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:354-361] |
| `collect_error_with_cleanup` | function | `fn collect_error_with_cleanup<T>(` | `collect_error_with_cleanup [function]` | `06f6d196-4db8-541d-a79b-f8d94be48e14` | 363-390 [crates/gwiki/src/collect.rs:363-390] | Indexed function `collect_error_with_cleanup` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:363-390] |
| `collect_cleanup_detail` | function | `fn collect_cleanup_detail(cleanup_errors: &[String]) -> String {` | `collect_cleanup_detail [function]` | `49cf3dc1-b2bd-5bcb-bba0-5602a7470677` | 392-398 [crates/gwiki/src/collect.rs:392-398] | Indexed function `collect_cleanup_detail` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:392-398] |
| `skip_item` | function | `fn skip_item(` | `skip_item [function]` | `3f67c0c4-7be8-5f77-95df-632072c9dee1` | 400-418 [crates/gwiki/src/collect.rs:400-418] | Indexed function `skip_item` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:400-418] |
| `render_url_markdown` | function | `fn render_url_markdown(url: &str, fetched_at: &str, source_hash: &str) -> String {` | `render_url_markdown [function]` | `e4287291-209a-52fa-8222-d4455660de33` | 420-433 [crates/gwiki/src/collect.rs:420-433] | Indexed function `render_url_markdown` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:420-433] |
| `render_file_markdown` | function | `fn render_file_markdown(` | `render_file_markdown [function]` | `1091d96f-a0a0-51c1-9029-e85ee43e3b77` | 435-480 [crates/gwiki/src/collect.rs:435-480] | Indexed function `render_file_markdown` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:435-480] |
| `write_status_sidecar` | function | `fn write_status_sidecar(` | `write_status_sidecar [function]` | `1100926e-4ecc-54ca-a5c9-2c11476cf377` | 482-501 [crates/gwiki/src/collect.rs:482-501] | Indexed function `write_status_sidecar` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:482-501] |
| `append_log` | function | `fn append_log(` | `append_log [function]` | `9829051c-68ae-59a9-a98f-b0d1fef222de` | 503-550 [crates/gwiki/src/collect.rs:503-550] | Indexed function `append_log` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:503-550] |
| `extract_url` | function | `fn extract_url(text: &str) -> Option<String> {` | `extract_url [function]` | `3d5daae1-47b3-514b-ad79-77d70e2cd3f6` | 552-572 [crates/gwiki/src/collect.rs:552-572] | Indexed function `extract_url` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:552-572] |
| `urls_from_embedded_text` | function | `fn urls_from_embedded_text(text: &str) -> Vec<String> {` | `urls_from_embedded_text [function]` | `eeaf7156-ceaa-5444-9c40-411257d705b0` | 574-588 [crates/gwiki/src/collect.rs:574-588] | Indexed function `urls_from_embedded_text` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:574-588] |
| `is_http_url` | function | `fn is_http_url(value: &str) -> bool {` | `is_http_url [function]` | `67d27d42-6b3b-5da9-ac29-15932ad626fb` | 590-592 [crates/gwiki/src/collect.rs:590-592] | Indexed function `is_http_url` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:590-592] |
| `parse_embedded_http_url` | function | `fn parse_embedded_http_url(candidate: &str) -> Option<String> {` | `parse_embedded_http_url [function]` | `9d7023b2-9d1e-58df-a5cc-a73c072315c3` | 594-604 [crates/gwiki/src/collect.rs:594-604] | Indexed function `parse_embedded_http_url` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:594-604] |
| `trim_trailing_url_punctuation` | function | `fn trim_trailing_url_punctuation(candidate: &str) -> Option<&str> {` | `trim_trailing_url_punctuation [function]` | `f9fec537-bd99-50ce-83a0-b5c80ac604b0` | 606-610 [crates/gwiki/src/collect.rs:606-610] | Indexed function `trim_trailing_url_punctuation` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:606-610] |
| `parse_http_url` | function | `fn parse_http_url(value: &str) -> Option<String> {` | `parse_http_url [function]` | `20fe5bac-453e-5dbd-8fb7-f8615d8acb3c` | 612-615 [crates/gwiki/src/collect.rs:612-615] | Indexed function `parse_http_url` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:612-615] |
| `should_store_asset` | function | `fn should_store_asset(kind: &SourceKind) -> bool {` | `should_store_asset [function]` | `b4415446-3cb3-5a71-ab54-94f6fa617e09` | 617-622 [crates/gwiki/src/collect.rs:617-622] | Indexed function `should_store_asset` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:617-622] |
| `is_status_sidecar` | function | `fn is_status_sidecar(path: &Path) -> bool {` | `is_status_sidecar [function]` | `b8175220-06f5-5597-b71a-cf8361cb275e` | 624-628 [crates/gwiki/src/collect.rs:624-628] | Indexed function `is_status_sidecar` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:624-628] |
| `status_sidecar_path` | function | `fn status_sidecar_path(path: &Path) -> PathBuf {` | `status_sidecar_path [function]` | `7460e7f6-5a6b-5a3a-bdcb-636448958a60` | 630-636 [crates/gwiki/src/collect.rs:630-636] | Indexed function `status_sidecar_path` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:630-636] |
| `relative_to_vault` | function | `fn relative_to_vault(vault_root: &Path, path: &Path) -> String {` | `relative_to_vault [function]` | `5509d7f2-df40-5634-b064-5de0f47500ed` | 638-642 [crates/gwiki/src/collect.rs:638-642] | Indexed function `relative_to_vault` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:638-642] |
| `path_to_string` | function | `fn path_to_string(path: &Path) -> String {` | `path_to_string [function]` | `a706c15d-d00f-584e-a27c-426fdcd88be1` | 644-646 [crates/gwiki/src/collect.rs:644-646] | Indexed function `path_to_string` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:644-646] |
| `io_error` | function | `fn io_error(action: &'static str, path: &Path, error: std::io::Error) -> WikiError {` | `io_error [function]` | `17c06b58-d133-58f8-a2a0-0b9c5a407986` | 648-654 [crates/gwiki/src/collect.rs:648-654] | Indexed function `io_error` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:648-654] |
| `write_file` | function | `fn write_file(root: &Path, relative: &str, contents: &[u8]) {` | `write_file [function]` | `e8969c87-376a-5075-9ed0-eee4af5ecb1b` | 665-671 [crates/gwiki/src/collect.rs:665-671] | Indexed function `write_file` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:665-671] |
| `collect_routes_known_items` | function | `fn collect_routes_known_items() {` | `collect_routes_known_items [function]` | `ce6da4de-1046-5298-b467-e7ee15671ded` | 674-736 [crates/gwiki/src/collect.rs:674-736] | Indexed function `collect_routes_known_items` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:674-736] |
| `collect_indexes_accepted_sources` | function | `fn collect_indexes_accepted_sources() {` | `collect_indexes_accepted_sources [function]` | `e181ae5f-452e-5411-8598-1cab333b931a` | 739-768 [crates/gwiki/src/collect.rs:739-768] | Indexed function `collect_indexes_accepted_sources` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:739-768] |
| `embedded_url_parser_returns_all_urls_in_order` | function | `fn embedded_url_parser_returns_all_urls_in_order() {` | `embedded_url_parser_returns_all_urls_in_order [function]` | `84d25ba4-2fe3-52dd-b8ce-a238de98d11a` | 771-781 [crates/gwiki/src/collect.rs:771-781] | Indexed function `embedded_url_parser_returns_all_urls_in_order` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:771-781] |
| `embedded_url_parser_preserves_valid_punctuation_before_trimming` | function | `fn embedded_url_parser_preserves_valid_punctuation_before_trimming() {` | `embedded_url_parser_preserves_valid_punctuation_before_trimming [function]` | `96fb7602-8ea7-52a8-994f-56d14c3146aa` | 784-789 [crates/gwiki/src/collect.rs:784-789] | Indexed function `embedded_url_parser_preserves_valid_punctuation_before_trimming` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:784-789] |
| `embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds` | function | `fn embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds() {` | `embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds [function]` | `2f4dc5ac-dd6a-5f3d-a2f4-e15822b0efac` | 792-797 [crates/gwiki/src/collect.rs:792-797] | Indexed function `embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:792-797] |
| `ambiguous_items_remain_in_inbox` | function | `fn ambiguous_items_remain_in_inbox() {` | `ambiguous_items_remain_in_inbox [function]` | `e9296cdf-0d5f-5f52-a4af-dd4c88e8b63a` | 800-815 [crates/gwiki/src/collect.rs:800-815] | Indexed function `ambiguous_items_remain_in_inbox` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:800-815] |
| `collect_logs_actions` | function | `fn collect_logs_actions() {` | `collect_logs_actions [function]` | `631705bc-3e5e-507f-95d2-0196ef8fd29b` | 818-830 [crates/gwiki/src/collect.rs:818-830] | Indexed function `collect_logs_actions` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:818-830] |
| `oversized_items_are_skipped_before_reading` | function | `fn oversized_items_are_skipped_before_reading() {` | `oversized_items_are_skipped_before_reading [function]` | `43badfb1-a579-5a21-9ca0-54ed2febbf79` | 833-847 [crates/gwiki/src/collect.rs:833-847] | Indexed function `oversized_items_are_skipped_before_reading` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:833-847] |
| `collect_cleanup_context_preserves_config_error_variant` | function | `fn collect_cleanup_context_preserves_config_error_variant() {` | `collect_cleanup_context_preserves_config_error_variant [function]` | `23dc38f9-8e0a-5ce8-bffe-b69cd802cccd` | 850-866 [crates/gwiki/src/collect.rs:850-866] | Indexed function `collect_cleanup_context_preserves_config_error_variant` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:850-866] |
| `collect_cleanup_context_preserves_io_error_variant` | function | `fn collect_cleanup_context_preserves_io_error_variant() {` | `collect_cleanup_context_preserves_io_error_variant [function]` | `93c73948-fc3a-5b6b-be41-64c0fe135b29` | 869-892 [crates/gwiki/src/collect.rs:869-892] | Indexed function `collect_cleanup_context_preserves_io_error_variant` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:869-892] |
