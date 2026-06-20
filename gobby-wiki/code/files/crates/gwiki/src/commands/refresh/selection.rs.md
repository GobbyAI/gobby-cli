---
title: crates/gwiki/src/commands/refresh/selection.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/selection.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/selection.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Overview

`crates/gwiki/src/commands/refresh/selection.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/refresh/selection.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `select_sources` | function | 'select_sources' builds a 'Selection' of refresh plans by either selecting all replay-capable 'entries' when 'source_ids' is empty or, otherwise, de-duplicating requested IDs, matching them to records, and recording missing/invalid/unsupported sources as failures or skips. [crates/gwiki/src/commands/refresh/selection.rs:4-75] |
| `ChangeTriggeredSelection` | class | 'ChangeTriggeredSelection' is an internal data structure that tracks a set of source IDs to refresh and filesystem paths for pages that should be marked stale in response to a change. [crates/gwiki/src/commands/refresh/selection.rs:79-82] |
| `select_change_triggered_refresh` | function | It scans each affected page’s source IDs against 'entries', collects unique markdown-replay source record IDs to refresh, and marks the page path stale when no matching refreshable source is found, returning both lists in a 'ChangeTriggeredSelection'. [crates/gwiki/src/commands/refresh/selection.rs:85-112] |
| `ReplayKind` | type | Indexed type `ReplayKind` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:115-118] |
| `SelectionFailure` | type | Indexed type `SelectionFailure` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:121-124] |
| `replay_kind` | function | Returns 'ReplayKind::Url' for URL sources, 'ReplayKind::LocalFile' when 'local_file_replay(record)' yields a value, and otherwise maps local-file kinds to 'SelectionFailure::MissingReplayMetadata' or all other kinds to 'SelectionFailure::UnsupportedSourceKind'. [crates/gwiki/src/commands/refresh/selection.rs:126-138] |
| `replay_kind_name` | function | Returns a static string label for a 'SourceRecord'’s replay kind by mapping 'ReplayKind::Url' to '"url"', 'ReplayKind::LocalFile' to '"local_file"', and any error to '"unsupported"'. [crates/gwiki/src/commands/refresh/selection.rs:140-146] |
| `local_file_replay` | function | Returns the '(Path, SourceReplayOptions)' pair for a 'SourceRecord' only when 'record.replay' is 'Some(SourceReplay::LocalFile { .. })', otherwise 'None'. [crates/gwiki/src/commands/refresh/selection.rs:148-152] |
| `is_markdown_replay` | function | Returns 'true' only for records that are eligible for local-file replay and are either explicitly 'SourceKind::Markdown' or point to a file whose lowercase extension is 'md', 'mdown', or 'markdown'. [crates/gwiki/src/commands/refresh/selection.rs:155-169] |
| `is_local_file_source_kind` | function | Returns 'true' when 'kind' is one of the local file-backed source variants ('Audio', 'Image', 'Video', 'Pdf', 'Office', 'Html', 'Markdown', 'Text', 'Session', or 'File'), and 'false' otherwise. [crates/gwiki/src/commands/refresh/selection.rs:171-185] |
| `selection_failure` | function | Constructs a 'RefreshFailure' from a 'SourceRecord' and 'SelectionFailure' by cloning the record’s identifiers and kind, then mapping each variant to a specific error code and descriptive message. [crates/gwiki/src/commands/refresh/selection.rs:187-210] |
| `refresh_plan_failure` | function | Constructs a 'RefreshFailure' from a 'SourceRecord' and 'WikiError' by copying the record’s 'id', 'location', and 'kind', setting 'code' to '"invalid_source_id"', and using the error’s string form as the message. [crates/gwiki/src/commands/refresh/selection.rs:212-220] |
| `is_url_source` | function | Returns 'true' if either 'record.location' or 'record.canonical_location' is an HTTP URL, and 'false' otherwise. [crates/gwiki/src/commands/refresh/selection.rs:222-224] |
| `refresh_url` | function | Returns 'record.location' when it is an HTTP URL, otherwise returns 'record.canonical_location'. [crates/gwiki/src/commands/refresh/selection.rs:226-232] |
| `is_http_url` | function | Returns 'true' only if the trimmed input parses as a URL with scheme 'http' or 'https' and a non-empty host, otherwise 'false'. [crates/gwiki/src/commands/refresh/selection.rs:234-239] |

_Verified by 1 in-file unit test._

