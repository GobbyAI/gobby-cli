---
title: crates/gwiki/src/store/helpers.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/helpers.rs
  ranges:
  - 12-14
  - 16-21
  - 23-28
  - 30-46
  - 48-50
  - 52-58
  - 60-70
  - 72-89
  - 91-94
  - 96-115
  - 117-125
  - 127-135
  - 137-144
  - 146-153
  - 155-159
  - 161-165
  - 167-180
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/store/helpers.rs:12-14](crates/gwiki/src/store/helpers.rs#L12-L14), [crates/gwiki/src/store/helpers.rs:16-21](crates/gwiki/src/store/helpers.rs#L16-L21), [crates/gwiki/src/store/helpers.rs:23-28](crates/gwiki/src/store/helpers.rs#L23-L28), [crates/gwiki/src/store/helpers.rs:30-46](crates/gwiki/src/store/helpers.rs#L30-L46), [crates/gwiki/src/store/helpers.rs:48-50](crates/gwiki/src/store/helpers.rs#L48-L50), [crates/gwiki/src/store/helpers.rs:52-58](crates/gwiki/src/store/helpers.rs#L52-L58), [crates/gwiki/src/store/helpers.rs:60-70](crates/gwiki/src/store/helpers.rs#L60-L70), [crates/gwiki/src/store/helpers.rs:72-89](crates/gwiki/src/store/helpers.rs#L72-L89), [crates/gwiki/src/store/helpers.rs:91-94](crates/gwiki/src/store/helpers.rs#L91-L94), [crates/gwiki/src/store/helpers.rs:96-115](crates/gwiki/src/store/helpers.rs#L96-L115), [crates/gwiki/src/store/helpers.rs:117-125](crates/gwiki/src/store/helpers.rs#L117-L125), [crates/gwiki/src/store/helpers.rs:127-135](crates/gwiki/src/store/helpers.rs#L127-L135), [crates/gwiki/src/store/helpers.rs:137-144](crates/gwiki/src/store/helpers.rs#L137-L144), [crates/gwiki/src/store/helpers.rs:146-153](crates/gwiki/src/store/helpers.rs#L146-L153), [crates/gwiki/src/store/helpers.rs:155-159](crates/gwiki/src/store/helpers.rs#L155-L159), [crates/gwiki/src/store/helpers.rs:161-165](crates/gwiki/src/store/helpers.rs#L161-L165), [crates/gwiki/src/store/helpers.rs:167-180](crates/gwiki/src/store/helpers.rs#L167-L180)

</details>

# crates/gwiki/src/store/helpers.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Utilities for the wiki store layer that normalize paths, validate chunk and link records against an expected file path, and build stable scoped IDs with optional suffixes while capping them to the repository’s ID length limit. It also maps document, ingestion, and link kinds to names, detects URI schemes, derives rollback replacement identifiers, and reads the configured memory index limit.
[crates/gwiki/src/store/helpers.rs:12-14]
[crates/gwiki/src/store/helpers.rs:16-21]
[crates/gwiki/src/store/helpers.rs:23-28]
[crates/gwiki/src/store/helpers.rs:30-46]
[crates/gwiki/src/store/helpers.rs:48-50]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `display_path` | function | `pub(super) fn display_path(path: &Path) -> String {` | `display_path [function]` | `2a8dd597-78e1-51b5-a767-d34cbfc1998c` | 12-14 [crates/gwiki/src/store/helpers.rs:12-14] | Indexed function `display_path` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:12-14] |
| `validate_chunk_paths` | function | `pub(super) fn validate_chunk_paths(path: &Path, chunks: &[WikiChunk]) -> Result<(), StoreError> {` | `validate_chunk_paths [function]` | `6df4dce1-50af-5d79-a23e-db5736fa15a6` | 16-21 [crates/gwiki/src/store/helpers.rs:16-21] | Indexed function `validate_chunk_paths` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:16-21] |
| `validate_link_paths` | function | `pub(super) fn validate_link_paths(path: &Path, links: &[WikiLink]) -> Result<(), StoreError> {` | `validate_link_paths [function]` | `f32c6060-b5fa-5511-88c8-b26238a79877` | 23-28 [crates/gwiki/src/store/helpers.rs:23-28] | Indexed function `validate_link_paths` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:23-28] |
| `validate_matching_path` | function | `pub(super) fn validate_matching_path(` | `validate_matching_path [function]` | `7e30ebcd-d714-5605-915b-e7e58576290b` | 30-46 [crates/gwiki/src/store/helpers.rs:30-46] | Indexed function `validate_matching_path` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:30-46] |
| `equivalent_display_path` | function | `pub(super) fn equivalent_display_path(left: &Path, right: &Path) -> bool {` | `equivalent_display_path [function]` | `88c1e57b-a93b-5ed2-9772-7b70f87c2f4c` | 48-50 [crates/gwiki/src/store/helpers.rs:48-50] | Indexed function `equivalent_display_path` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:48-50] |
| `platform_path_from_display` | function | `pub(super) fn platform_path_from_display(path: &str) -> PathBuf {` | `platform_path_from_display [function]` | `758fad7b-a8b7-5499-8e52-f6ad8cf65fec` | 52-58 [crates/gwiki/src/store/helpers.rs:52-58] | Indexed function `platform_path_from_display` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:52-58] |
| `scoped_id` | function | `pub(super) fn scoped_id(` | `scoped_id [function]` | `1dd28eca-1e3e-50e7-857c-c514f00a66e1` | 60-70 [crates/gwiki/src/store/helpers.rs:60-70] | Indexed function `scoped_id` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:60-70] |
| `scoped_text_id` | function | `pub(super) fn scoped_text_id(` | `scoped_text_id [function]` | `041f849e-720e-500c-8373-09cf0694550f` | 72-89 [crates/gwiki/src/store/helpers.rs:72-89] | Indexed function `scoped_text_id` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:72-89] |
| `cap_scoped_id` | function | `fn cap_scoped_id(id: String) -> String {` | `cap_scoped_id [function]` | `9aa33ced-929a-54ad-a23d-84bb6d6291d4` | 91-94 [crates/gwiki/src/store/helpers.rs:91-94] | Indexed function `cap_scoped_id` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:91-94] |
| `cap_scoped_id_with_hash` | function | `pub(super) fn cap_scoped_id_with_hash(id: String, hash: &str) -> String {` | `cap_scoped_id_with_hash [function]` | `89287596-2fa9-51fb-926f-059fdf821ee4` | 96-115 [crates/gwiki/src/store/helpers.rs:96-115] | Indexed function `cap_scoped_id_with_hash` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:96-115] |
| `document_kind_name` | function | `pub(super) fn document_kind_name(kind: WikiDocumentKind) -> &'static str {` | `document_kind_name [function]` | `9f65c057-0fbd-5612-b2b6-cef243e7e17d` | 117-125 [crates/gwiki/src/store/helpers.rs:117-125] | Indexed function `document_kind_name` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:117-125] |
| `ingestion_status` | function | `pub(super) fn ingestion_status(event: WikiIngestionEvent) -> &'static str {` | `ingestion_status [function]` | `be88c27d-70a1-54b5-9fd3-cdaabfc1eab4` | 127-135 [crates/gwiki/src/store/helpers.rs:127-135] | Indexed function `ingestion_status` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:127-135] |
| `link_kind` | function | `pub(crate) fn link_kind(target: &str) -> &'static str {` | `link_kind [function]` | `e04cec1c-fabf-527b-942d-f8417af86f43` | 137-144 [crates/gwiki/src/store/helpers.rs:137-144] | Indexed function `link_kind` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:137-144] |
| `has_uri_scheme` | function | `fn has_uri_scheme(target: &str) -> bool {` | `has_uri_scheme [function]` | `dff60475-953c-54e7-a949-143f48d4f651` | 146-153 [crates/gwiki/src/store/helpers.rs:146-153] | Indexed function `has_uri_scheme` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:146-153] |
| `rollback_link_replacement` | function | `pub(super) fn rollback_link_replacement(tx: Transaction<'_>, path: &str) {` | `rollback_link_replacement [function]` | `81cc13a7-54d5-5839-8581-0aaf116c4dfc` | 155-159 [crates/gwiki/src/store/helpers.rs:155-159] | Indexed function `rollback_link_replacement` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:155-159] |
| `rollback_chunk_replacement` | function | `pub(super) fn rollback_chunk_replacement(tx: Transaction<'_>, path: &str) {` | `rollback_chunk_replacement [function]` | `d0c1d948-f823-54d4-8726-f63e2cb24d3d` | 161-165 [crates/gwiki/src/store/helpers.rs:161-165] | Indexed function `rollback_chunk_replacement` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:161-165] |
| `configured_memory_index_limit_bytes` | function | `pub fn configured_memory_index_limit_bytes() -> Option<u64> {` | `configured_memory_index_limit_bytes [function]` | `f8d84331-d177-5eb5-96c7-f17ef9b3eac9` | 167-180 [crates/gwiki/src/store/helpers.rs:167-180] | Indexed function `configured_memory_index_limit_bytes` in `crates/gwiki/src/store/helpers.rs`. [crates/gwiki/src/store/helpers.rs:167-180] |
