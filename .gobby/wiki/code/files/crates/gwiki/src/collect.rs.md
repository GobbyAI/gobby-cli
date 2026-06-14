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

# crates/gwiki/src/collect.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements inbox collection for a wiki vault: it scans `vault_root/inbox`, skips sidecars, directories, oversized or ambiguous items, classifies each file or URL, and either accepts it into the source manifest or records a skipped action in a `CollectReport`. Accepted items are rendered into raw markdown or stored as assets, status sidecars and `log.md` are updated, and failures trigger cleanup and rollback helpers that preserve error context.

It also includes the supporting plumbing for URL extraction and validation, path and status-sidecar utilities, file writing, and tests that cover routing, indexing, skip behavior, logging, URL parsing, and cleanup error handling.
[crates/gwiki/src/collect.rs:18-21]
[crates/gwiki/src/collect.rs:24-30]
[crates/gwiki/src/collect.rs:34-37]
[crates/gwiki/src/collect.rs:39-42]
[crates/gwiki/src/collect.rs:44-46]

## API Symbols

- `CollectReport` (class) component `CollectReport [class]` (`a2a6ff71-4dc8-50a8-a76a-9f5fddfe583f`) lines 18-21 [crates/gwiki/src/collect.rs:18-21]
  - Signature: `pub struct CollectReport {`
  - Purpose: CollectReport is a struct that partitions CollectAction items into two vectors representing accepted and skipped results of a collection operation. [crates/gwiki/src/collect.rs:18-21]
- `CollectAction` (class) component `CollectAction [class]` (`d7d0df0c-b0d9-5951-a7b9-f4be0cc190c4`) lines 24-30 [crates/gwiki/src/collect.rs:24-30]
  - Signature: `pub struct CollectAction {`
  - Purpose: CollectAction is a struct that represents a collection operation with a required inbox destination path and status, plus optional metadata fields for classification kind, raw path, and operational reason. [crates/gwiki/src/collect.rs:24-30]
- `CollectStatus` (type) component `CollectStatus [type]` (`de97cf70-c4cd-58ad-92f7-211c2d47c156`) lines 34-37 [crates/gwiki/src/collect.rs:34-37]
  - Signature: `pub enum CollectStatus {`
  - Purpose: Indexed type `CollectStatus` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:34-37]
- `InboxKind` (type) component `InboxKind [type]` (`8c3d7c40-320b-5af0-96af-58df726b75b6`) lines 39-42 [crates/gwiki/src/collect.rs:39-42]
  - Signature: `enum InboxKind {`
  - Purpose: Indexed type `InboxKind` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:39-42]
- `collect_inbox` (function) component `collect_inbox [function]` (`e21fb410-42f5-536d-98a9-7de2dcf937fd`) lines 44-46 [crates/gwiki/src/collect.rs:44-46]
  - Signature: `pub fn collect_inbox(vault_root: &Path, fetched_at: &str) -> Result<CollectReport, WikiError> {`
  - Purpose: Collects and reports inbox items from a vault root at a specified timestamp, applying a maximum byte limit sourced from an environment variable via `collect_inbox_with_limit`. [crates/gwiki/src/collect.rs:44-46]
- `collect_inbox_with_limit` (function) component `collect_inbox_with_limit [function]` (`de9718bb-29aa-56f1-90f7-e2111b7c8ec1`) lines 48-140 [crates/gwiki/src/collect.rs:48-140]
  - Signature: `fn collect_inbox_with_limit(`
  - Purpose: Collects files from a vault inbox directory enforcing a maximum per-item byte limit, filtering out directories and oversized items, and returning a CollectReport of processed entries. [crates/gwiki/src/collect.rs:48-140]
- `collect_inbox_and_index` (function) component `collect_inbox_and_index [function]` (`4b012167-1d3b-5e5e-958b-a751463923a8`) lines 142-152 [crates/gwiki/src/collect.rs:142-152]
  - Signature: `pub fn collect_inbox_and_index(`
  - Purpose: Collects inbox items and conditionally reindexes the wiki store if any items are accepted. [crates/gwiki/src/collect.rs:142-152]
- `read_inbox_item_limited` (function) component `read_inbox_item_limited [function]` (`54050517-d717-5f21-ad95-08629a17fde7`) lines 154-165 [crates/gwiki/src/collect.rs:154-165]
  - Signature: `fn read_inbox_item_limited(path: &Path, max_item_bytes: u64) -> Result<Option<Vec<u8>>, WikiError> {`
  - Purpose: Reads a file and returns its complete byte contents if the file size does not exceed `max_item_bytes`, otherwise returns `None`. [crates/gwiki/src/collect.rs:154-165]
- `ensure_collect_paths` (function) component `ensure_collect_paths [function]` (`ebdbb025-23dc-52f1-84aa-3fbc89097ab9`) lines 167-179 [crates/gwiki/src/collect.rs:167-179]
  - Signature: `fn ensure_collect_paths(vault_root: &Path) -> Result<(), WikiError> {`
  - Purpose: This function initializes a vault's directory structure by creating required subdirectories (inbox, raw, raw/assets) and instantiating a log.md file if absent, returning a WikiError on I/O failure. [crates/gwiki/src/collect.rs:167-179]
- `classify_inbox_item` (function) component `classify_inbox_item [function]` (`f3940301-8a05-537c-a936-065d55d7da70`) lines 181-204 [crates/gwiki/src/collect.rs:181-204]
  - Signature: `fn classify_inbox_item(path: &Path, bytes: &[u8]) -> Result<InboxKind, &'static str> {`
  - Purpose: Classifies an inbox item by file extension into an InboxKind variant (typed file kinds or URL), with fallback URL extraction from content for extensionless items. [crates/gwiki/src/collect.rs:181-204]
- `accept_item` (function) component `accept_item [function]` (`81a74962-57ec-5ee4-a099-96a73bafc21e`) lines 206-327 [crates/gwiki/src/collect.rs:206-327]
  - Signature: `fn accept_item(`
  - Purpose: # Summary

Registers inbox items (URLs or files) to a vault manifest by creating source records, rendering them into appropriate formats, persisting the content, and rolling back on failure. [crates/gwiki/src/collect.rs:206-327]
- `rollback_registered_collect_source` (function) component `rollback_registered_collect_source [function]` (`b5db18f0-6142-5be6-a224-66cfe1154b8b`) lines 329-352 [crates/gwiki/src/collect.rs:329-352]
  - Signature: `fn rollback_registered_collect_source<T>(`
  - Purpose: Performs rollback of a failed source collection by cleaning up collected files, restoring the previous manifest state, and returning the original error or a rollback failure. [crates/gwiki/src/collect.rs:329-352]
- `cleanup_collect_file` (function) component `cleanup_collect_file [function]` (`76d1bca4-1b33-54e0-8369-b8a8656ad5f8`) lines 354-361 [crates/gwiki/src/collect.rs:354-361]
  - Signature: `fn cleanup_collect_file(vault_root: &Path, relative_path: &Path, cleanup_errors: &mut Vec<String>) {`
  - Purpose: Attempts to remove a file at the resolved path and accumulates any I/O errors (except NotFound) into the provided error vector. [crates/gwiki/src/collect.rs:354-361]
- `collect_error_with_cleanup` (function) component `collect_error_with_cleanup [function]` (`06f6d196-4db8-541d-a79b-f8d94be48e14`) lines 363-390 [crates/gwiki/src/collect.rs:363-390]
  - Signature: `fn collect_error_with_cleanup<T>(`
  - Purpose: Augments a WikiError with cleanup operation failures by appending collected cleanup details to the original error's message/detail fields and returning the combined error. [crates/gwiki/src/collect.rs:363-390]
- `collect_cleanup_detail` (function) component `collect_cleanup_detail [function]` (`49cf3dc1-b2bd-5bcb-bba0-5602a7470677`) lines 392-398 [crates/gwiki/src/collect.rs:392-398]
  - Signature: `fn collect_cleanup_detail(cleanup_errors: &[String]) -> String {`
  - Purpose: Formats cleanup errors into a semicolon-prefixed, semicolon-separated diagnostic string suffix, or returns an empty string if no errors are present. [crates/gwiki/src/collect.rs:392-398]
- `skip_item` (function) component `skip_item [function]` (`3f67c0c4-7be8-5f77-95df-632072c9dee1`) lines 400-418 [crates/gwiki/src/collect.rs:400-418]
  - Signature: `fn skip_item(`
  - Purpose: Persists a skipped item action (with optional reason) to a status sidecar file and appends it to a collection report. [crates/gwiki/src/collect.rs:400-418]
- `render_url_markdown` (function) component `render_url_markdown [function]` (`e4287291-209a-52fa-8222-d4455660de33`) lines 420-433 [crates/gwiki/src/collect.rs:420-433]
  - Signature: `fn render_url_markdown(url: &str, fetched_at: &str, source_hash: &str) -> String {`
  - Purpose: Constructs a markdown-formatted string containing fetch metadata (source kind, URL, timestamp, hash) and the URL rendered as both a heading and body reference. [crates/gwiki/src/collect.rs:420-433]
- `render_file_markdown` (function) component `render_file_markdown [function]` (`1091d96f-a0a0-51c1-9029-e85ee43e3b77`) lines 435-480 [crates/gwiki/src/collect.rs:435-480]
  - Signature: `fn render_file_markdown(`
  - Purpose: Renders a file with its metadata into markdown format, embedding text content inline or referencing binary artifacts by their storage location. [crates/gwiki/src/collect.rs:435-480]
- `write_status_sidecar` (function) component `write_status_sidecar [function]` (`1100926e-4ecc-54ca-a5c9-2c11476cf377`) lines 482-501 [crates/gwiki/src/collect.rs:482-501]
  - Signature: `fn write_status_sidecar(`
  - Purpose: Serializes a `CollectAction` into a JSON sidecar file containing inbox item metadata (path, status, reason, and timestamp) with error handling for serialization and file I/O operations. [crates/gwiki/src/collect.rs:482-501]
- `append_log` (function) component `append_log [function]` (`9829051c-68ae-59a9-a98f-b0d1fef222de`) lines 503-550 [crates/gwiki/src/collect.rs:503-550]
  - Signature: `fn append_log(`
  - Purpose: Appends timestamped markdown-formatted entries documenting accepted and skipped collection actions from a report to a vault's log.md file. [crates/gwiki/src/collect.rs:503-550]
- `extract_url` (function) component `extract_url [function]` (`3d5daae1-47b3-514b-ad79-77d70e2cd3f6`) lines 552-572 [crates/gwiki/src/collect.rs:552-572]
  - Signature: `fn extract_url(text: &str) -> Option<String> {`
  - Purpose: Extracts and returns the first valid HTTP URL found in the input text by checking for `URL=` prefixed values, standalone HTTP URLs, or embedded URLs per line, or None if no URL is found. [crates/gwiki/src/collect.rs:552-572]
- `urls_from_embedded_text` (function) component `urls_from_embedded_text [function]` (`eeaf7156-ceaa-5444-9c40-411257d705b0`) lines 574-588 [crates/gwiki/src/collect.rs:574-588]
  - Signature: `fn urls_from_embedded_text(text: &str) -> Vec<String> {`
  - Purpose: Extracts all HTTP(S) URLs embedded in plain text by iteratively locating protocol prefixes and parsing URL-terminated tokens bounded by whitespace and punctuation characters. [crates/gwiki/src/collect.rs:574-588]
- `is_http_url` (function) component `is_http_url [function]` (`67d27d42-6b3b-5da9-ac29-15932ad626fb`) lines 590-592 [crates/gwiki/src/collect.rs:590-592]
  - Signature: `fn is_http_url(value: &str) -> bool {`
  - Purpose: Checks if a given string is a valid HTTP URL by attempting to parse it with `parse_http_url()` and returning true on successful parsing. [crates/gwiki/src/collect.rs:590-592]
- `parse_embedded_http_url` (function) component `parse_embedded_http_url [function]` (`9d7023b2-9d1e-58df-a5cc-a73c072315c3`) lines 594-604 [crates/gwiki/src/collect.rs:594-604]
  - Signature: `fn parse_embedded_http_url(candidate: &str) -> Option<String> {`
  - Purpose: Parses and extracts a valid HTTP URL from a candidate string by progressively removing trailing punctuation until a valid URL is found. [crates/gwiki/src/collect.rs:594-604]
- `trim_trailing_url_punctuation` (function) component `trim_trailing_url_punctuation [function]` (`f9fec537-bd99-50ce-83a0-b5c80ac604b0`) lines 606-610 [crates/gwiki/src/collect.rs:606-610]
  - Signature: `fn trim_trailing_url_punctuation(candidate: &str) -> Option<&str> {`
  - Purpose: Removes trailing URL punctuation characters (`,`, `.`, `;`, `)`, `]`) from a string and returns the trimmed result only if at least 2 characters were removed; otherwise returns `None`. [crates/gwiki/src/collect.rs:606-610]
- `parse_http_url` (function) component `parse_http_url [function]` (`20fe5bac-453e-5dbd-8fb7-f8615d8acb3c`) lines 612-615 [crates/gwiki/src/collect.rs:612-615]
  - Signature: `fn parse_http_url(value: &str) -> Option<String> {`
  - Purpose: Returns the input string if it is a valid URL with an http or https scheme, otherwise returns None. [crates/gwiki/src/collect.rs:612-615]
- `should_store_asset` (function) component `should_store_asset [function]` (`b4415446-3cb3-5a71-ab54-94f6fa617e09`) lines 617-622 [crates/gwiki/src/collect.rs:617-622]
  - Signature: `fn should_store_asset(kind: &SourceKind) -> bool {`
  - Purpose: Determines whether a given `SourceKind` should be persisted as an asset by returning `true` for Audio, Pdf, Video, or File variants, and `false` for all others. [crates/gwiki/src/collect.rs:617-622]
- `is_status_sidecar` (function) component `is_status_sidecar [function]` (`b8175220-06f5-5597-b71a-cf8361cb275e`) lines 624-628 [crates/gwiki/src/collect.rs:624-628]
  - Signature: `fn is_status_sidecar(path: &Path) -> bool {`
  - Purpose: Returns `true` if the file name of the given path ends with `.status.json`, `false` otherwise. [crates/gwiki/src/collect.rs:624-628]
- `status_sidecar_path` (function) component `status_sidecar_path [function]` (`7460e7f6-5a6b-5a3a-bdcb-636448958a60`) lines 630-636 [crates/gwiki/src/collect.rs:630-636]
  - Signature: `fn status_sidecar_path(path: &Path) -> PathBuf {`
  - Purpose: Creates and returns a `PathBuf` with the same directory as the input path but with the filename replaced by the original filename suffixed with `.status.json`, defaulting to `item.status.json` if filename extraction fails. [crates/gwiki/src/collect.rs:630-636]
- `relative_to_vault` (function) component `relative_to_vault [function]` (`5509d7f2-df40-5634-b064-5de0f47500ed`) lines 638-642 [crates/gwiki/src/collect.rs:638-642]
  - Signature: `fn relative_to_vault(vault_root: &Path, path: &Path) -> String {`
  - Purpose: Strips the `vault_root` prefix from `path` and converts to a string, falling back to the stringified absolute path if the prefix cannot be removed. [crates/gwiki/src/collect.rs:638-642]
- `path_to_string` (function) component `path_to_string [function]` (`a706c15d-d00f-584e-a27c-426fdcd88be1`) lines 644-646 [crates/gwiki/src/collect.rs:644-646]
  - Signature: `fn path_to_string(path: &Path) -> String {`
  - Purpose: Converts a `Path` to a `String` with all backslashes replaced by forward slashes, using lossy UTF-8 conversion. [crates/gwiki/src/collect.rs:644-646]
- `io_error` (function) component `io_error [function]` (`17c06b58-d133-58f8-a2a0-0b9c5a407986`) lines 648-654 [crates/gwiki/src/collect.rs:648-654]
  - Signature: `fn io_error(action: &'static str, path: &Path, error: std::io::Error) -> WikiError {`
  - Purpose: Constructs a `WikiError::Io` variant by wrapping an `std::io::Error` with contextual action and file path information. [crates/gwiki/src/collect.rs:648-654]
- `write_file` (function) component `write_file [function]` (`e8969c87-376a-5075-9ed0-eee4af5ecb1b`) lines 665-671 [crates/gwiki/src/collect.rs:665-671]
  - Signature: `fn write_file(root: &Path, relative: &str, contents: &[u8]) {`
  - Purpose: Writes byte contents to a file at `root/relative`, creating all necessary parent directories if they don't exist. [crates/gwiki/src/collect.rs:665-671]
- `collect_routes_known_items` (function) component `collect_routes_known_items [function]` (`ce6da4de-1046-5298-b467-e7ee15671ded`) lines 674-736 [crates/gwiki/src/collect.rs:674-736]
  - Signature: `fn collect_routes_known_items() {`
  - Purpose: Tests that the `collect_inbox` function correctly ingests and routes six heterogeneous file types (URL shortcuts, PDF, Markdown, plain text, audio, and CSV) from an inbox directory into a SourceManifest with appropriately classified SourceKind entries. [crates/gwiki/src/collect.rs:674-736]
- `collect_indexes_accepted_sources` (function) component `collect_indexes_accepted_sources [function]` (`e181ae5f-452e-5411-8598-1cab333b931a`) lines 739-768 [crates/gwiki/src/collect.rs:739-768]
  - Signature: `fn collect_indexes_accepted_sources() {`
  - Purpose: Tests that `collect_inbox_and_index` correctly processes accepted source files from the inbox, generates a SourceCatalog index at `raw/INDEX.md` with proper metadata, and records the corresponding ingestion event. [crates/gwiki/src/collect.rs:739-768]
- `embedded_url_parser_returns_all_urls_in_order` (function) component `embedded_url_parser_returns_all_urls_in_order [function]` (`84d25ba4-2fe3-52dd-b8ce-a238de98d11a`) lines 771-781 [crates/gwiki/src/collect.rs:771-781]
  - Signature: `fn embedded_url_parser_returns_all_urls_in_order() {`
  - Purpose: This test verifies that `urls_from_embedded_text` extracts all URLs from mixed text in order while preserving adjacent punctuation characters. [crates/gwiki/src/collect.rs:771-781]
- `embedded_url_parser_preserves_valid_punctuation_before_trimming` (function) component `embedded_url_parser_preserves_valid_punctuation_before_trimming [function]` (`96fb7602-8ea7-52a8-994f-56d14c3146aa`) lines 784-789 [crates/gwiki/src/collect.rs:784-789]
  - Signature: `fn embedded_url_parser_preserves_valid_punctuation_before_trimming() {`
  - Purpose: This test verifies that the `urls_from_embedded_text` function correctly preserves valid punctuation characters (parentheses) within extracted URLs without trimming them during parsing. [crates/gwiki/src/collect.rs:784-789]
- `embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds` (function) component `embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds [function]` (`2f4dc5ac-dd6a-5f3d-a2f4-e15822b0efac`) lines 792-797 [crates/gwiki/src/collect.rs:792-797]
  - Signature: `fn embedded_url_parser_returns_trimmed_candidate_when_trimmed_parse_succeeds() {`
  - Purpose: This test verifies that `urls_from_embedded_text` correctly extracts and returns a URL stripped of its surrounding square bracket delimiters from embedded text. [crates/gwiki/src/collect.rs:792-797]
- `ambiguous_items_remain_in_inbox` (function) component `ambiguous_items_remain_in_inbox [function]` (`e9296cdf-0d5f-5f52-a4af-dd4c88e8b63a`) lines 800-815 [crates/gwiki/src/collect.rs:800-815]
  - Signature: `fn ambiguous_items_remain_in_inbox() {`
  - Purpose: Tests that `collect_inbox()` skips extensionless (ambiguous) inbox items and creates a `.status.json` sidecar file documenting the skip status. [crates/gwiki/src/collect.rs:800-815]
- `collect_logs_actions` (function) component `collect_logs_actions [function]` (`631705bc-3e5e-507f-95d2-0196ef8fd29b`) lines 818-830 [crates/gwiki/src/collect.rs:818-830]
  - Signature: `fn collect_logs_actions() {`
  - Purpose: A unit test that verifies `collect_inbox()` generates log entries with timestamps, action types (accepted or skipped), and processed file paths. [crates/gwiki/src/collect.rs:818-830]
- `oversized_items_are_skipped_before_reading` (function) component `oversized_items_are_skipped_before_reading [function]` (`43badfb1-a579-5a21-9ca0-54ed2febbf79`) lines 833-847 [crates/gwiki/src/collect.rs:833-847]
  - Signature: `fn oversized_items_are_skipped_before_reading() {`
  - Purpose: This test verifies that `collect_inbox_with_limit()` skips inbox items exceeding the specified byte limit before reading them and reports the appropriate skip reason. [crates/gwiki/src/collect.rs:833-847]
- `collect_cleanup_context_preserves_config_error_variant` (function) component `collect_cleanup_context_preserves_config_error_variant [function]` (`23dc38f9-8e0a-5ce8-bffe-b69cd802cccd`) lines 850-866 [crates/gwiki/src/collect.rs:850-866]
  - Signature: `fn collect_cleanup_context_preserves_config_error_variant() {`
  - Purpose: This test verifies that `collect_error_with_cleanup` preserves the `WikiError::Config` variant while appending cleanup failure details to the error's detail field. [crates/gwiki/src/collect.rs:850-866]
- `collect_cleanup_context_preserves_io_error_variant` (function) component `collect_cleanup_context_preserves_io_error_variant [function]` (`93c73948-fc3a-5b6b-be41-64c0fe135b29`) lines 869-892 [crates/gwiki/src/collect.rs:869-892]
  - Signature: `fn collect_cleanup_context_preserves_io_error_variant() {`
  - Purpose: This test verifies that `collect_error_with_cleanup` preserves the `WikiError::Io` variant and its underlying error kind while appending cleanup failure context to the error message. [crates/gwiki/src/collect.rs:869-892]

