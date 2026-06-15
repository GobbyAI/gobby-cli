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

# crates/gwiki/src/store/helpers.rs

Module: [[code/modules/crates/gwiki/src/store|crates/gwiki/src/store]]

## Purpose

This file provides store-side utility helpers for path handling, identifier construction, and a few small classification/configuration tasks. It normalizes paths into a display form, compares and validates stored chunk and link paths against an expected path, converts display paths back to platform paths, and builds scoped IDs that combine a prefix, store scope, path, optional suffixes, and a capped hash-backed length limit. It also maps document kinds and ingestion events to canonical strings, distinguishes wiki vs markdown links by inspecting the target, wraps transaction rollback logging for failed chunk/link replacements, and reads the optional memory index limit from the environment.
[crates/gwiki/src/store/helpers.rs:12-14]
[crates/gwiki/src/store/helpers.rs:16-21]
[crates/gwiki/src/store/helpers.rs:23-28]
[crates/gwiki/src/store/helpers.rs:30-46]
[crates/gwiki/src/store/helpers.rs:48-50]

## API Symbols

- `display_path` (function) component `display_path [function]` (`2a8dd597-78e1-51b5-a767-d34cbfc1998c`) lines 12-14 [crates/gwiki/src/store/helpers.rs:12-14]
  - Signature: `pub(super) fn display_path(path: &Path) -> String {`
  - Purpose: Converts a 'Path' to a lossy UTF-8 'String' and normalizes it by replacing all backslashes with forward slashes. [crates/gwiki/src/store/helpers.rs:12-14]
- `validate_chunk_paths` (function) component `validate_chunk_paths [function]` (`6df4dce1-50af-5d79-a23e-db5736fa15a6`) lines 16-21 [crates/gwiki/src/store/helpers.rs:16-21]
  - Signature: `pub(super) fn validate_chunk_paths(path: &Path, chunks: &[WikiChunk]) -> Result<(), StoreError> {`
  - Purpose: Validates that every 'WikiChunk' in 'chunks' has a 'path' matching the provided 'path', returning the first 'StoreError' from 'validate_matching_path' or 'Ok(())' if all match. [crates/gwiki/src/store/helpers.rs:16-21]
- `validate_link_paths` (function) component `validate_link_paths [function]` (`f32c6060-b5fa-5511-88c8-b26238a79877`) lines 23-28 [crates/gwiki/src/store/helpers.rs:23-28]
  - Signature: `pub(super) fn validate_link_paths(path: &Path, links: &[WikiLink]) -> Result<(), StoreError> {`
  - Purpose: Iterates over 'links' and returns the first 'StoreError' from 'validate_matching_path("link.path", path, &link.path)' if any link path does not match 'path', otherwise returns 'Ok(())'. [crates/gwiki/src/store/helpers.rs:23-28]
- `validate_matching_path` (function) component `validate_matching_path [function]` (`7e30ebcd-d714-5605-915b-e7e58576290b`) lines 30-46 [crates/gwiki/src/store/helpers.rs:30-46]
  - Signature: `pub(super) fn validate_matching_path(`
  - Purpose: Returns 'Ok(())' when 'expected' and 'found' are display-path equivalent, otherwise returns 'StoreError::InvalidData' for 'field' with a message reporting the expected and found paths. [crates/gwiki/src/store/helpers.rs:30-46]
- `equivalent_display_path` (function) component `equivalent_display_path [function]` (`88c1e57b-a93b-5ed2-9772-7b70f87c2f4c`) lines 48-50 [crates/gwiki/src/store/helpers.rs:48-50]
  - Signature: `pub(super) fn equivalent_display_path(left: &Path, right: &Path) -> bool {`
  - Purpose: Returns 'true' when 'left' and 'right' produce the same 'display_path' string, and 'false' otherwise. [crates/gwiki/src/store/helpers.rs:48-50]
- `platform_path_from_display` (function) component `platform_path_from_display [function]` (`758fad7b-a8b7-5499-8e52-f6ad8cf65fec`) lines 52-58 [crates/gwiki/src/store/helpers.rs:52-58]
  - Signature: `pub(super) fn platform_path_from_display(path: &str) -> PathBuf {`
  - Purpose: Converts a display-form path string into a platform-native 'PathBuf' by returning it unchanged on Unix-like systems and replacing '/' with the platform’s main separator on non-'/' platforms. [crates/gwiki/src/store/helpers.rs:52-58]
- `scoped_id` (function) component `scoped_id [function]` (`1dd28eca-1e3e-50e7-857c-c514f00a66e1`) lines 60-70 [crates/gwiki/src/store/helpers.rs:60-70]
  - Signature: `pub(super) fn scoped_id(`
  - Purpose: Returns a scoped text identifier by delegating to 'scoped_text_id' with the given 'prefix', 'scope', and 'path', appending a one-element suffix slice when 'suffix' is 'Some' and an empty slice when it is 'None'. [crates/gwiki/src/store/helpers.rs:60-70]
- `scoped_text_id` (function) component `scoped_text_id [function]` (`041f849e-720e-500c-8373-09cf0694550f`) lines 72-89 [crates/gwiki/src/store/helpers.rs:72-89]
  - Signature: `pub(super) fn scoped_text_id(`
  - Purpose: Builds a scoped identifier string from 'prefix', the scope kind and ID, and a display-form path, appends each provided suffix separated by colons, and then normalizes it with 'cap_scoped_id'. [crates/gwiki/src/store/helpers.rs:72-89]
- `cap_scoped_id` (function) component `cap_scoped_id [function]` (`9aa33ced-929a-54ad-a23d-84bb6d6291d4`) lines 91-94 [crates/gwiki/src/store/helpers.rs:91-94]
  - Signature: `fn cap_scoped_id(id: String) -> String {`
  - Purpose: Computes a content hash of the input string’s bytes and returns the result of 'cap_scoped_id_with_hash(id, &hash)' using that hash. [crates/gwiki/src/store/helpers.rs:91-94]
- `cap_scoped_id_with_hash` (function) component `cap_scoped_id_with_hash [function]` (`89287596-2fa9-51fb-926f-059fdf821ee4`) lines 96-115 [crates/gwiki/src/store/helpers.rs:96-115]
  - Signature: `pub(super) fn cap_scoped_id_with_hash(id: String, hash: &str) -> String {`
  - Purpose: Returns 'id' unchanged when it is within 'MAX_ID_LEN', otherwise truncates 'id' on UTF-8 character boundaries to leave room for a '-' plus a hash suffix (clipped to 'HASH_SUFFIX_LEN'), and returns '"{prefix}-{suffix}"'. [crates/gwiki/src/store/helpers.rs:96-115]
- `document_kind_name` (function) component `document_kind_name [function]` (`9f65c057-0fbd-5612-b2b6-cef243e7e17d`) lines 117-125 [crates/gwiki/src/store/helpers.rs:117-125]
  - Signature: `pub(super) fn document_kind_name(kind: WikiDocumentKind) -> &'static str {`
  - Purpose: Returns the canonical static string identifier for a 'WikiDocumentKind' variant by matching 'SourceCatalog', 'SourceNote', 'Concept', 'Topic', and 'CodeDoc' to '"source_catalog"', '"source_note"', '"concept"', '"topic"', and '"code_doc"' respectively. [crates/gwiki/src/store/helpers.rs:117-125]
- `ingestion_status` (function) component `ingestion_status [function]` (`be88c27d-70a1-54b5-9fd3-cdaabfc1eab4`) lines 127-135 [crates/gwiki/src/store/helpers.rs:127-135]
  - Signature: `pub(super) fn ingestion_status(event: WikiIngestionEvent) -> &'static str {`
  - Purpose: Maps a 'WikiIngestionEvent' enum variant to its corresponding static status string: '"added"', '"changed"', '"deleted"', '"unchanged"', or '"skipped"'. [crates/gwiki/src/store/helpers.rs:127-135]
- `link_kind` (function) component `link_kind [function]` (`e04cec1c-fabf-527b-942d-f8417af86f43`) lines 137-144 [crates/gwiki/src/store/helpers.rs:137-144]
  - Signature: `pub(crate) fn link_kind(target: &str) -> &'static str {`
  - Purpose: Returns '"markdown"' for targets that are protocol-relative, UNC-style, or have a URI scheme after trimming whitespace, and '"wiki"' otherwise. [crates/gwiki/src/store/helpers.rs:137-144]
- `has_uri_scheme` (function) component `has_uri_scheme [function]` (`dff60475-953c-54e7-a949-143f48d4f651`) lines 146-153 [crates/gwiki/src/store/helpers.rs:146-153]
  - Signature: `fn has_uri_scheme(target: &str) -> bool {`
  - Purpose: Returns 'true' if 'target' contains a ':'-delimited prefix whose first character is ASCII alphabetic and whose remaining characters are all ASCII alphanumeric or one of '+', '.', or '-', otherwise 'false'. [crates/gwiki/src/store/helpers.rs:146-153]
- `rollback_link_replacement` (function) component `rollback_link_replacement [function]` (`81cc13a7-54d5-5839-8581-0aaf116c4dfc`) lines 155-159 [crates/gwiki/src/store/helpers.rs:155-159]
  - Signature: `pub(super) fn rollback_link_replacement(tx: Transaction<'_>, path: &str) {`
  - Purpose: Attempts to roll back the given transaction for a gwiki link replacement at 'path', and logs an error if the rollback fails. [crates/gwiki/src/store/helpers.rs:155-159]
- `rollback_chunk_replacement` (function) component `rollback_chunk_replacement [function]` (`d0c1d948-f823-54d4-8726-f63e2cb24d3d`) lines 161-165 [crates/gwiki/src/store/helpers.rs:161-165]
  - Signature: `pub(super) fn rollback_chunk_replacement(tx: Transaction<'_>, path: &str) {`
  - Purpose: Attempts to roll back the given transaction for a gwiki chunk replacement at 'path', and logs an error if the rollback fails. [crates/gwiki/src/store/helpers.rs:161-165]
- `configured_memory_index_limit_bytes` (function) component `configured_memory_index_limit_bytes [function]` (`f8d84331-d177-5eb5-96c7-f17ef9b3eac9`) lines 167-180 [crates/gwiki/src/store/helpers.rs:167-180]
  - Signature: `pub fn configured_memory_index_limit_bytes() -> Option<u64> {`
  - Purpose: Reads the 'MAX_MEMORY_INDEX_BYTES_ENV' environment variable and returns 'Some(u64)' only if it parses as a positive integer, otherwise returns 'None' and emits a warning for invalid set values. [crates/gwiki/src/store/helpers.rs:167-180]

