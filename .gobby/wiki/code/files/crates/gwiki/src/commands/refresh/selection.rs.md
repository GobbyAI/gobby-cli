---
title: crates/gwiki/src/commands/refresh/selection.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/selection.rs
  ranges:
  - 4-75
  - 79-82
  - 85-112
  - 115-118
  - 121-124
  - 126-138
  - 140-146
  - 148-152
  - 155-169
  - 171-184
  - 186-209
  - 211-219
  - 221-223
  - 225-231
  - 233-238
  - 247-293
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/selection.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

`crates/gwiki/src/commands/refresh/selection.rs` exposes 16 indexed API symbols.
[crates/gwiki/src/commands/refresh/selection.rs:4-75]
[crates/gwiki/src/commands/refresh/selection.rs:79-82]
[crates/gwiki/src/commands/refresh/selection.rs:85-112]
[crates/gwiki/src/commands/refresh/selection.rs:115-118]
[crates/gwiki/src/commands/refresh/selection.rs:121-124]

## API Symbols

- `select_sources` (function) component `select_sources [function]` (`50a5bf4b-66b9-5619-be11-1ef651641bf0`) lines 4-75 [crates/gwiki/src/commands/refresh/selection.rs:4-75]
  - Signature: `pub(crate) fn select_sources(entries: &[SourceRecord], source_ids: &[String]) -> Selection {`
  - Purpose: `select_sources` constructs a `Selection` by either scanning all `entries` when `source_ids` is empty or deduplicating and resolving the requested IDs against `entries`, then classifying each record into planned, skipped, or failed outcomes based on `replay_kind` and `RefreshPlan::from_record`, with missing or unsupported sources reported as failures or skips. [crates/gwiki/src/commands/refresh/selection.rs:4-75]
- `ChangeTriggeredSelection` (class) component `ChangeTriggeredSelection [class]` (`ee53c758-21ec-5506-a8d4-9b002f676ebc`) lines 79-82 [crates/gwiki/src/commands/refresh/selection.rs:79-82]
  - Signature: `pub(crate) struct ChangeTriggeredSelection {`
  - Purpose: `ChangeTriggeredSelection` is a crate-private data carrier that records which source IDs need refresh and which page paths should be marked stale after a change-triggered selection. [crates/gwiki/src/commands/refresh/selection.rs:79-82]
- `select_change_triggered_refresh` (function) component `select_change_triggered_refresh [function]` (`3ee83343-1ca7-5c10-b431-ada74ace7c65`) lines 85-112 [crates/gwiki/src/commands/refresh/selection.rs:85-112]
  - Signature: `pub(crate) fn select_change_triggered_refresh(`
  - Purpose: It computes a `ChangeTriggeredSelection` by scanning each affected page’s `source_ids`, collecting unique IDs that match an `entries` record and satisfy `is_markdown_replay` for refresh, and marking the page path stale when no refreshable sources are found. [crates/gwiki/src/commands/refresh/selection.rs:85-112]
- `ReplayKind` (type) component `ReplayKind [type]` (`4bd59b49-c1f1-513b-9e8f-6554606220c9`) lines 115-118 [crates/gwiki/src/commands/refresh/selection.rs:115-118]
  - Signature: `pub(crate) enum ReplayKind {`
  - Purpose: Indexed type `ReplayKind` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:115-118]
- `SelectionFailure` (type) component `SelectionFailure [type]` (`13fe3d85-b3cc-5dac-903e-ebd3b410ea6d`) lines 121-124 [crates/gwiki/src/commands/refresh/selection.rs:121-124]
  - Signature: `pub(crate) enum SelectionFailure {`
  - Purpose: Indexed type `SelectionFailure` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:121-124]
- `replay_kind` (function) component `replay_kind [function]` (`d1173452-7f8a-564b-b4b2-92e8dc483b7d`) lines 126-138 [crates/gwiki/src/commands/refresh/selection.rs:126-138]
  - Signature: `pub(crate) fn replay_kind(record: &SourceRecord) -> Result<ReplayKind, SelectionFailure> {`
  - Purpose: `replay_kind` classifies a `SourceRecord` as `ReplayKind::Url` if it is a URL source, `ReplayKind::LocalFile` if it can be resolved to a local-file replay, and otherwise returns `MissingReplayMetadata` for local-file source kinds or `UnsupportedSourceKind` for all other kinds. [crates/gwiki/src/commands/refresh/selection.rs:126-138]
- `replay_kind_name` (function) component `replay_kind_name [function]` (`e2feea7b-762e-5d7b-9c45-3cebbae3e155`) lines 140-146 [crates/gwiki/src/commands/refresh/selection.rs:140-146]
  - Signature: `pub(crate) fn replay_kind_name(record: &SourceRecord) -> &'static str {`
  - Purpose: Returns `"url"` or `"local_file"` based on `replay_kind(record)`, and returns `"unsupported"` if determining the replay kind fails. [crates/gwiki/src/commands/refresh/selection.rs:140-146]
- `local_file_replay` (function) component `local_file_replay [function]` (`1e76e1ca-3d5d-51f5-abee-1dc70c9dd7fd`) lines 148-152 [crates/gwiki/src/commands/refresh/selection.rs:148-152]
  - Signature: `pub(crate) fn local_file_replay(record: &SourceRecord) -> Option<(&Path, &SourceReplayOptions)> {`
  - Purpose: Returns `Some((path, options))` when `record.replay` is `SourceReplay::LocalFile`, borrowing the local file `Path` and associated `SourceReplayOptions` from the record, and returns `None` otherwise. [crates/gwiki/src/commands/refresh/selection.rs:148-152]
- `is_markdown_replay` (function) component `is_markdown_replay [function]` (`818c5d2b-a7d3-5207-b7a9-0982b93c00f0`) lines 155-169 [crates/gwiki/src/commands/refresh/selection.rs:155-169]
  - Signature: `fn is_markdown_replay(record: &SourceRecord) -> bool {`
  - Purpose: Returns `true` only for records that resolve to a local file replay and are either explicitly `SourceKind::Markdown` or have a case-insensitive `.md`, `.mdown`, or `.markdown` file extension. [crates/gwiki/src/commands/refresh/selection.rs:155-169]
- `is_local_file_source_kind` (function) component `is_local_file_source_kind [function]` (`7a16b48f-42df-5dc6-b95e-b4c90b5826df`) lines 171-184 [crates/gwiki/src/commands/refresh/selection.rs:171-184]
  - Signature: `fn is_local_file_source_kind(kind: &SourceKind) -> bool {`
  - Purpose: Returns `true` when `kind` is one of the local file-backed `SourceKind` variants (`Audio`, `Image`, `Video`, `Pdf`, `Office`, `Html`, `Markdown`, `Text`, or `File`), and `false` otherwise. [crates/gwiki/src/commands/refresh/selection.rs:171-184]
- `selection_failure` (function) component `selection_failure [function]` (`483ca9cb-9481-55df-839d-c197df1de45a`) lines 186-209 [crates/gwiki/src/commands/refresh/selection.rs:186-209]
  - Signature: `pub(crate) fn selection_failure(record: &SourceRecord, error: SelectionFailure) -> RefreshFailure {`
  - Purpose: Converts a `SelectionFailure` for a `SourceRecord` into a structured `RefreshFailure`, preserving the record’s `id`, `location`, and `kind` and assigning a variant-specific error code and message. [crates/gwiki/src/commands/refresh/selection.rs:186-209]
- `refresh_plan_failure` (function) component `refresh_plan_failure [function]` (`528f535e-3cd4-5b50-b98c-cc875272b7ac`) lines 211-219 [crates/gwiki/src/commands/refresh/selection.rs:211-219]
  - Signature: `fn refresh_plan_failure(record: &SourceRecord, error: WikiError) -> RefreshFailure {`
  - Purpose: Constructs a `RefreshFailure` by copying the `SourceRecord`’s `id`, `location`, and `kind`, setting `code` to `"invalid_source_id"`, and using the `WikiError`’s string representation as the failure message. [crates/gwiki/src/commands/refresh/selection.rs:211-219]
- `is_url_source` (function) component `is_url_source [function]` (`e733c3aa-3b58-594e-8a62-037430ca201f`) lines 221-223 [crates/gwiki/src/commands/refresh/selection.rs:221-223]
  - Signature: `fn is_url_source(record: &SourceRecord) -> bool {`
  - Purpose: Returns `true` when either `record.location` or `record.canonical_location` satisfies `is_http_url`, indicating the source record points to an HTTP URL in either field. [crates/gwiki/src/commands/refresh/selection.rs:221-223]
- `refresh_url` (function) component `refresh_url [function]` (`0a582330-0595-5b2b-9522-47613d96a768`) lines 225-231 [crates/gwiki/src/commands/refresh/selection.rs:225-231]
  - Signature: `pub(crate) fn refresh_url(record: &SourceRecord) -> &str {`
  - Purpose: Returns `record.location` when it is an HTTP URL, otherwise returns `record.canonical_location`. [crates/gwiki/src/commands/refresh/selection.rs:225-231]
- `is_http_url` (function) component `is_http_url [function]` (`d7676da4-be25-5d7a-ac13-fb52966d8da1`) lines 233-238 [crates/gwiki/src/commands/refresh/selection.rs:233-238]
  - Signature: `fn is_http_url(value: &str) -> bool {`
  - Purpose: Returns `true` only when `value.trim()` parses as a `url::Url` whose scheme is `http` or `https` and whose host component is present and non-empty, otherwise `false`. [crates/gwiki/src/commands/refresh/selection.rs:233-238]
- `change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages` (function) component `change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages [function]` (`82c6cfa6-a432-5503-848a-1c92ea7b7008`) lines 247-293 [crates/gwiki/src/commands/refresh/selection.rs:247-293]
  - Signature: `fn change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages() {`
  - Purpose: It verifies that `select_change_triggered_refresh` schedules the Markdown `SourceRecord` with a local-file replay (`source-derived`) for refresh and marks the unrelated canonical affected page (`code/canonical.md`) as stale. [crates/gwiki/src/commands/refresh/selection.rs:247-293]

