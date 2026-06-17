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
  - 171-185
  - 187-210
  - 212-220
  - 222-224
  - 226-232
  - 234-239
  - 248-294
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/refresh/selection.rs:4-75](crates/gwiki/src/commands/refresh/selection.rs#L4-L75), [crates/gwiki/src/commands/refresh/selection.rs:79-82](crates/gwiki/src/commands/refresh/selection.rs#L79-L82), [crates/gwiki/src/commands/refresh/selection.rs:85-112](crates/gwiki/src/commands/refresh/selection.rs#L85-L112), [crates/gwiki/src/commands/refresh/selection.rs:115-118](crates/gwiki/src/commands/refresh/selection.rs#L115-L118), [crates/gwiki/src/commands/refresh/selection.rs:121-124](crates/gwiki/src/commands/refresh/selection.rs#L121-L124), [crates/gwiki/src/commands/refresh/selection.rs:126-138](crates/gwiki/src/commands/refresh/selection.rs#L126-L138), [crates/gwiki/src/commands/refresh/selection.rs:140-146](crates/gwiki/src/commands/refresh/selection.rs#L140-L146), [crates/gwiki/src/commands/refresh/selection.rs:148-152](crates/gwiki/src/commands/refresh/selection.rs#L148-L152), [crates/gwiki/src/commands/refresh/selection.rs:155-169](crates/gwiki/src/commands/refresh/selection.rs#L155-L169), [crates/gwiki/src/commands/refresh/selection.rs:171-185](crates/gwiki/src/commands/refresh/selection.rs#L171-L185), [crates/gwiki/src/commands/refresh/selection.rs:187-210](crates/gwiki/src/commands/refresh/selection.rs#L187-L210), [crates/gwiki/src/commands/refresh/selection.rs:212-220](crates/gwiki/src/commands/refresh/selection.rs#L212-L220), [crates/gwiki/src/commands/refresh/selection.rs:222-224](crates/gwiki/src/commands/refresh/selection.rs#L222-L224), [crates/gwiki/src/commands/refresh/selection.rs:226-232](crates/gwiki/src/commands/refresh/selection.rs#L226-L232), [crates/gwiki/src/commands/refresh/selection.rs:234-239](crates/gwiki/src/commands/refresh/selection.rs#L234-L239), [crates/gwiki/src/commands/refresh/selection.rs:248-294](crates/gwiki/src/commands/refresh/selection.rs#L248-L294)

</details>

# crates/gwiki/src/commands/refresh/selection.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

This file builds the source-selection logic for refresh commands. `select_sources` turns either an explicit list of source IDs or the full set of entries into a `Selection` by deduplicating IDs, looking up records, checking whether each record has a supported replay contract via `replay_kind`, and then either converting it to a `RefreshPlan`, skipping unsupported kinds, or collecting structured failures. The surrounding helpers classify replay kinds and sources (`local_file_replay`, `is_markdown_replay`, `is_local_file_source_kind`, `is_url_source`, `is_http_url`), map errors into `SelectionFailure`, `RefreshFailure`, and `SkippedRefresh`, and `select_change_triggered_refresh`/`ChangeTriggeredSelection` provide the variant used when refresh is driven by page changes, including marking affected canonical pages stale and selecting markdown replay targets.
[crates/gwiki/src/commands/refresh/selection.rs:4-75]
[crates/gwiki/src/commands/refresh/selection.rs:79-82]
[crates/gwiki/src/commands/refresh/selection.rs:85-112]
[crates/gwiki/src/commands/refresh/selection.rs:115-118]
[crates/gwiki/src/commands/refresh/selection.rs:121-124]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `select_sources` | function | `pub(crate) fn select_sources(entries: &[SourceRecord], source_ids: &[String]) -> Selection {` | `select_sources [function]` | `50a5bf4b-66b9-5619-be11-1ef651641bf0` | 4-75 [crates/gwiki/src/commands/refresh/selection.rs:4-75] | Indexed function `select_sources` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:4-75] |
| `ChangeTriggeredSelection` | class | `pub(crate) struct ChangeTriggeredSelection {` | `ChangeTriggeredSelection [class]` | `ee53c758-21ec-5506-a8d4-9b002f676ebc` | 79-82 [crates/gwiki/src/commands/refresh/selection.rs:79-82] | Indexed class `ChangeTriggeredSelection` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:79-82] |
| `select_change_triggered_refresh` | function | `pub(crate) fn select_change_triggered_refresh(` | `select_change_triggered_refresh [function]` | `3ee83343-1ca7-5c10-b431-ada74ace7c65` | 85-112 [crates/gwiki/src/commands/refresh/selection.rs:85-112] | Indexed function `select_change_triggered_refresh` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:85-112] |
| `ReplayKind` | type | `pub(crate) enum ReplayKind {` | `ReplayKind [type]` | `4bd59b49-c1f1-513b-9e8f-6554606220c9` | 115-118 [crates/gwiki/src/commands/refresh/selection.rs:115-118] | Indexed type `ReplayKind` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:115-118] |
| `SelectionFailure` | type | `pub(crate) enum SelectionFailure {` | `SelectionFailure [type]` | `13fe3d85-b3cc-5dac-903e-ebd3b410ea6d` | 121-124 [crates/gwiki/src/commands/refresh/selection.rs:121-124] | Indexed type `SelectionFailure` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:121-124] |
| `replay_kind` | function | `pub(crate) fn replay_kind(record: &SourceRecord) -> Result<ReplayKind, SelectionFailure> {` | `replay_kind [function]` | `d1173452-7f8a-564b-b4b2-92e8dc483b7d` | 126-138 [crates/gwiki/src/commands/refresh/selection.rs:126-138] | Indexed function `replay_kind` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:126-138] |
| `replay_kind_name` | function | `pub(crate) fn replay_kind_name(record: &SourceRecord) -> &'static str {` | `replay_kind_name [function]` | `e2feea7b-762e-5d7b-9c45-3cebbae3e155` | 140-146 [crates/gwiki/src/commands/refresh/selection.rs:140-146] | Indexed function `replay_kind_name` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:140-146] |
| `local_file_replay` | function | `pub(crate) fn local_file_replay(record: &SourceRecord) -> Option<(&Path, &SourceReplayOptions)> {` | `local_file_replay [function]` | `1e76e1ca-3d5d-51f5-abee-1dc70c9dd7fd` | 148-152 [crates/gwiki/src/commands/refresh/selection.rs:148-152] | Indexed function `local_file_replay` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:148-152] |
| `is_markdown_replay` | function | `fn is_markdown_replay(record: &SourceRecord) -> bool {` | `is_markdown_replay [function]` | `818c5d2b-a7d3-5207-b7a9-0982b93c00f0` | 155-169 [crates/gwiki/src/commands/refresh/selection.rs:155-169] | Indexed function `is_markdown_replay` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:155-169] |
| `is_local_file_source_kind` | function | `fn is_local_file_source_kind(kind: &SourceKind) -> bool {` | `is_local_file_source_kind [function]` | `7a16b48f-42df-5dc6-b95e-b4c90b5826df` | 171-185 [crates/gwiki/src/commands/refresh/selection.rs:171-185] | Indexed function `is_local_file_source_kind` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:171-185] |
| `selection_failure` | function | `pub(crate) fn selection_failure(record: &SourceRecord, error: SelectionFailure) -> RefreshFailure {` | `selection_failure [function]` | `5f6b2966-be21-51ef-97c2-409b9ab5d1d9` | 187-210 [crates/gwiki/src/commands/refresh/selection.rs:187-210] | Indexed function `selection_failure` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:187-210] |
| `refresh_plan_failure` | function | `fn refresh_plan_failure(record: &SourceRecord, error: WikiError) -> RefreshFailure {` | `refresh_plan_failure [function]` | `936ca3b4-ff19-56a5-8167-1c50ffaed7ba` | 212-220 [crates/gwiki/src/commands/refresh/selection.rs:212-220] | Indexed function `refresh_plan_failure` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:212-220] |
| `is_url_source` | function | `fn is_url_source(record: &SourceRecord) -> bool {` | `is_url_source [function]` | `176be595-e509-5185-b2e8-12da390630cb` | 222-224 [crates/gwiki/src/commands/refresh/selection.rs:222-224] | Indexed function `is_url_source` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:222-224] |
| `refresh_url` | function | `pub(crate) fn refresh_url(record: &SourceRecord) -> &str {` | `refresh_url [function]` | `8073c0c6-35a0-55d8-bb29-619ff9da9e44` | 226-232 [crates/gwiki/src/commands/refresh/selection.rs:226-232] | Indexed function `refresh_url` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:226-232] |
| `is_http_url` | function | `fn is_http_url(value: &str) -> bool {` | `is_http_url [function]` | `12d84e5d-6a4c-56b7-a069-f999afc85f05` | 234-239 [crates/gwiki/src/commands/refresh/selection.rs:234-239] | Indexed function `is_http_url` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:234-239] |
| `change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages` | function | `fn change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages() {` | `change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages [function]` | `d6455523-8170-5017-b6ad-e435f0ec058b` | 248-294 [crates/gwiki/src/commands/refresh/selection.rs:248-294] | Indexed function `change_triggered_refresh_selects_markdown_replay_and_stales_canonical_pages` in `crates/gwiki/src/commands/refresh/selection.rs`. [crates/gwiki/src/commands/refresh/selection.rs:248-294] |
