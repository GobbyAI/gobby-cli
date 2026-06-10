---
title: crates/gwiki/src/commands/refresh/selection.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/selection.rs
  ranges:
  - 4-75
  - 78-81
  - 83-110
  - 113-116
  - 119-122
  - 124-136
  - 138-144
  - 146-150
  - 152-166
  - 168-181
  - 183-206
  - 208-216
  - 218-220
  - 222-228
  - 230-235
  - 244-290
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/selection.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

`crates/gwiki/src/commands/refresh/selection.rs` exposes 16 indexed API symbols.
[crates/gwiki/src/commands/refresh/selection.rs:4-75]
[crates/gwiki/src/commands/refresh/selection.rs:78-81]
[crates/gwiki/src/commands/refresh/selection.rs:83-110]
[crates/gwiki/src/commands/refresh/selection.rs:113-116]
[crates/gwiki/src/commands/refresh/selection.rs:119-122]
[crates/gwiki/src/commands/refresh/selection.rs:124-136]
[crates/gwiki/src/commands/refresh/selection.rs:138-144]
[crates/gwiki/src/commands/refresh/selection.rs:146-150]
[crates/gwiki/src/commands/refresh/selection.rs:152-166]
[crates/gwiki/src/commands/refresh/selection.rs:168-181]
[crates/gwiki/src/commands/refresh/selection.rs:183-206]
[crates/gwiki/src/commands/refresh/selection.rs:208-216]
[crates/gwiki/src/commands/refresh/selection.rs:218-220]
[crates/gwiki/src/commands/refresh/selection.rs:222-228]
[crates/gwiki/src/commands/refresh/selection.rs:230-235]
[crates/gwiki/src/commands/refresh/selection.rs:244-290]

## API Symbols

- `select_sources` (function) component `select_sources [function]` (`50a5bf4b-66b9-5619-be11-1ef651641bf0`) lines 4-75 [crates/gwiki/src/commands/refresh/selection.rs:4-75]
  - Signature: `pub(crate) fn select_sources(entries: &[SourceRecord], source_ids: &[String]) -> Selection {`
  - Purpose: Indexed function `select_sources` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:4-75]
- `ChangeTriggeredSelection` (class) component `ChangeTriggeredSelection [class]` (`64688b30-b3c6-51a1-abc7-ba361633771c`) lines 78-81 [crates/gwiki/src/commands/refresh/selection.rs:78-81]
  - Signature: `pub(crate) struct ChangeTriggeredSelection {`
  - Purpose: Indexed class `ChangeTriggeredSelection` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:78-81]
- `select_change_triggered_refresh` (function) component `select_change_triggered_refresh [function]` (`d2da1068-b915-51b4-89a1-7f2e2f3a487c`) lines 83-110 [crates/gwiki/src/commands/refresh/selection.rs:83-110]
  - Signature: `pub(crate) fn select_change_triggered_refresh(`
  - Purpose: Indexed function `select_change_triggered_refresh` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:83-110]
- `ReplayKind` (type) component `ReplayKind [type]` (`39997ebd-f2a3-51a9-959b-7d6a49c1d64f`) lines 113-116 [crates/gwiki/src/commands/refresh/selection.rs:113-116]
  - Signature: `pub(crate) enum ReplayKind {`
  - Purpose: Indexed type `ReplayKind` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:113-116]
- `SelectionFailure` (type) component `SelectionFailure [type]` (`cc9363af-a2c9-593c-ab6c-d8b5a5b8e851`) lines 119-122 [crates/gwiki/src/commands/refresh/selection.rs:119-122]
  - Signature: `pub(crate) enum SelectionFailure {`
  - Purpose: Indexed type `SelectionFailure` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:119-122]
- `replay_kind` (function) component `replay_kind [function]` (`a15047df-bca9-539b-a3f8-7580205d6d79`) lines 124-136 [crates/gwiki/src/commands/refresh/selection.rs:124-136]
  - Signature: `pub(crate) fn replay_kind(record: &SourceRecord) -> Result<ReplayKind, SelectionFailure> {`
  - Purpose: Indexed function `replay_kind` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:124-136]
- `replay_kind_name` (function) component `replay_kind_name [function]` (`fe34ccee-568f-525d-a4ff-4add664c2e2b`) lines 138-144 [crates/gwiki/src/commands/refresh/selection.rs:138-144]
  - Signature: `pub(crate) fn replay_kind_name(record: &SourceRecord) -> &'static str {`
  - Purpose: Indexed function `replay_kind_name` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:138-144]
- `local_file_replay` (function) component `local_file_replay [function]` (`4ac2cdad-4ebf-5740-8ce9-02091e3f4f47`) lines 146-150 [crates/gwiki/src/commands/refresh/selection.rs:146-150]
  - Signature: `pub(crate) fn local_file_replay(record: &SourceRecord) -> Option<(&Path, &SourceReplayOptions)> {`
  - Purpose: Indexed function `local_file_replay` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:146-150]
- `is_markdown_replay` (function) component `is_markdown_replay [function]` (`53628105-4d35-56b1-ace1-4b8071e44803`) lines 152-166 [crates/gwiki/src/commands/refresh/selection.rs:152-166]
  - Signature: `fn is_markdown_replay(record: &SourceRecord) -> bool {`
  - Purpose: Indexed function `is_markdown_replay` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:152-166]
- `is_local_file_source_kind` (function) component `is_local_file_source_kind [function]` (`d7268323-3e3c-55ce-adfa-ae6ec4b855fd`) lines 168-181 [crates/gwiki/src/commands/refresh/selection.rs:168-181]
  - Signature: `fn is_local_file_source_kind(kind: &SourceKind) -> bool {`
  - Purpose: Indexed function `is_local_file_source_kind` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:168-181]
- `selection_failure` (function) component `selection_failure [function]` (`27b7e1a4-7251-53e9-832a-a2437abc7cd2`) lines 183-206 [crates/gwiki/src/commands/refresh/selection.rs:183-206]
  - Signature: `pub(crate) fn selection_failure(record: &SourceRecord, error: SelectionFailure) -> RefreshFailure {`
  - Purpose: Indexed function `selection_failure` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:183-206]
- `refresh_plan_failure` (function) component `refresh_plan_failure [function]` (`a73fe07b-22e6-570a-84e4-963bdce68f84`) lines 208-216 [crates/gwiki/src/commands/refresh/selection.rs:208-216]
  - Signature: `fn refresh_plan_failure(record: &SourceRecord, error: WikiError) -> RefreshFailure {`
  - Purpose: Indexed function `refresh_plan_failure` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:208-216]
- `is_url_source` (function) component `is_url_source [function]` (`3f55b8fd-a8d5-590e-8eb4-63fef81b71a9`) lines 218-220 [crates/gwiki/src/commands/refresh/selection.rs:218-220]
  - Signature: `fn is_url_source(record: &SourceRecord) -> bool {`
  - Purpose: Indexed function `is_url_source` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:218-220]
- `refresh_url` (function) component `refresh_url [function]` (`b3d2d10a-509c-5f0d-942e-c9a3e0ee7c6e`) lines 222-228 [crates/gwiki/src/commands/refresh/selection.rs:222-228]
  - Signature: `pub(crate) fn refresh_url(record: &SourceRecord) -> &str {`
  - Purpose: Indexed function `refresh_url` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:222-228]
- `is_http_url` (function) component `is_http_url [function]` (`1da5a4a4-9ee2-5155-9f00-416c1fe4a381`) lines 230-235 [crates/gwiki/src/commands/refresh/selection.rs:230-235]
  - Signature: `fn is_http_url(value: &str) -> bool {`
  - Purpose: Indexed function `is_http_url` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:230-235]
- `change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages` (function) component `change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages [function]` (`f73f4006-211d-5a0f-807a-1c2b33bd3644`) lines 244-290 [crates/gwiki/src/commands/refresh/selection.rs:244-290]
  - Signature: `fn change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages() {`
  - Purpose: Indexed function `change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:244-290]

