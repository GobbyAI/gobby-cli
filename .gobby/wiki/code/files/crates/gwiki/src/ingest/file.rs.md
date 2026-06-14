---
title: crates/gwiki/src/ingest/file.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file.rs
  ranges:
  - 53-57
  - 60-63
  - 65-78
  - 80-262
  - 264-310
  - 312-336
  - 338-345
  - 347-349
  - 352-354
  - 356-371
  - 373-379
  - 382-414
  - 416-431
  - 433-447
  - 449-461
  - 463-508
  - 521-530
  - 532-538
  - 541-557
  - 560-613
  - 616-638
  - 641-655
  - 658-698
  - 701-728
  - 731-754
  - 757-829
  - 833-867
  - 871-897
  - 901-925
  - 929-953
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

This file implements local ingestion into the wiki store for both filesystem paths and stdin snapshots. It detects the source kind from the path, builds source/location metadata, and routes each input through the right no-index pipeline: generic files are read, registered, optionally stored as assets, and rendered to raw markdown; media and document inputs are dispatched to audio, image, video, PDF, office, HTML, or document-specific ingest flows; and stdin is recorded as a draft source with raw markdown output and no asset path. It also updates replay metadata in the source manifest, formats degradation summaries for fallback cases, decides when to persist assets versus inline text, and provides helpers for path normalization, AI-disabled ingest context/options, and coverage tests that verify dispatch, hashing, storage, and feature-gated behavior.
[crates/gwiki/src/ingest/file.rs:53-57]
[crates/gwiki/src/ingest/file.rs:60-63]
[crates/gwiki/src/ingest/file.rs:65-78]
[crates/gwiki/src/ingest/file.rs:80-262]
[crates/gwiki/src/ingest/file.rs:264-310]

## API Symbols

- `StdinSnapshot` (class) component `StdinSnapshot [class]` (`9b8e3792-61bc-5a26-8499-4db9a5cc710d`) lines 53-57 [crates/gwiki/src/ingest/file.rs:53-57]
  - Signature: `pub struct StdinSnapshot {`
  - Purpose: 'StdinSnapshot' is a data-only Rust struct that records a stdin capture’s 'label', the 'fetched_at' timestamp, and the raw 'bytes' payload. [crates/gwiki/src/ingest/file.rs:53-57]
- `LocalFileIngestResult` (class) component `LocalFileIngestResult [class]` (`24fdbb89-caf6-5dd5-83b0-a57f6438c0e5`) lines 60-63 [crates/gwiki/src/ingest/file.rs:60-63]
  - Signature: `pub(crate) struct LocalFileIngestResult {`
  - Purpose: 'LocalFileIngestResult' is a crate-visible wrapper struct that pairs an 'IngestResult' with a 'Vec<String>' of degradation messages produced during local file ingestion. [crates/gwiki/src/ingest/file.rs:60-63]
- `ingest_path` (function) component `ingest_path [function]` (`a6f88179-3233-5c30-89e5-93c0d8542e45`) lines 65-78 [crates/gwiki/src/ingest/file.rs:65-78]
  - Signature: `pub fn ingest_path(`
  - Purpose: 'ingest_path' ingests the specified 'path' into the vault by delegating to 'ingest_path_without_index', then runs 'index_after_ingest' on 'vault_root', and returns the inner 'IngestResult' or any propagated 'WikiError'. [crates/gwiki/src/ingest/file.rs:65-78]
- `ingest_path_without_index` (function) component `ingest_path_without_index [function]` (`2f85c848-c235-5dfa-a615-7abbab08cb85`) lines 80-262 [crates/gwiki/src/ingest/file.rs:80-262]
  - Signature: `pub(crate) fn ingest_path_without_index(`
  - Purpose: This function detects the source kind for 'path', derives file/location metadata, and dispatches to the appropriate no-index ingestion pipeline for that kind (for example audio transcription or image vision), returning a 'LocalFileIngestResult' or propagating 'WikiError'. [crates/gwiki/src/ingest/file.rs:80-262]
- `ingest_generic_file_without_index` (function) component `ingest_generic_file_without_index [function]` (`e1055ae4-52c6-52ed-a3d6-97a432c43b35`) lines 264-310 [crates/gwiki/src/ingest/file.rs:264-310]
  - Signature: `fn ingest_generic_file_without_index(`
  - Purpose: Reads a source file’s bytes, registers a borrowed manifest entry with metadata, conditionally writes the file as an asset, renders and persists a raw markdown representation, and returns the resulting 'LocalFileIngestResult' with no degradations. [crates/gwiki/src/ingest/file.rs:264-310]
- `attach_replay_metadata` (function) component `attach_replay_metadata [function]` (`0cc6d692-4a13-5343-81ce-86889c63e31e`) lines 312-336 [crates/gwiki/src/ingest/file.rs:312-336]
  - Signature: `fn attach_replay_metadata(`
  - Purpose: 'attach_replay_metadata' builds a 'SourceReplay' for the ingested file, writes it into 'result.record.replay', and updates the matching 'SourceManifest' entry in 'vault_root' only when the stored replay is absent or different, returning whether the manifest changed. [crates/gwiki/src/ingest/file.rs:312-336]
- `transcription_degradation_summary` (function) component `transcription_degradation_summary [function]` (`61dc0bb5-2a36-5cbd-a745-c44ba6efe62c`) lines 338-345 [crates/gwiki/src/ingest/file.rs:338-345]
  - Signature: `fn transcription_degradation_summary(`
  - Purpose: Returns a 'String' formatted as 'audio_transcription:<reason>:<fallback>' by interpolating the 'reason' and 'fallback' fields from the provided 'TranscriptionDegradation'. [crates/gwiki/src/ingest/file.rs:338-345]
- `vision_degradation_summary` (function) component `vision_degradation_summary [function]` (`28ba99ef-edc1-57f0-9e6a-36196aadde47`) lines 347-349 [crates/gwiki/src/ingest/file.rs:347-349]
  - Signature: `fn vision_degradation_summary(degradation: &VisionDegradation) -> String {`
  - Purpose: Returns a formatted string 'vision:<reason>:<fallback>' using the 'reason' and 'fallback' fields from the provided 'VisionDegradation'. [crates/gwiki/src/ingest/file.rs:347-349]
- `document_degradation_summary` (function) component `document_degradation_summary [function]` (`1cf6491a-5f7c-5ea6-9d5c-8362eb8ef75b`) lines 352-354 [crates/gwiki/src/ingest/file.rs:352-354]
  - Signature: `fn document_degradation_summary(degradation: &crate::document::DocumentDegradation) -> String {`
  - Purpose: Formats a 'DocumentDegradation' as 'document:<reason>:<fallback>' by concatenating 'degradation.reason()' and 'degradation.fallback' with colon separators. [crates/gwiki/src/ingest/file.rs:352-354]
- `video_degradation_summaries` (function) component `video_degradation_summaries [function]` (`6ef83a82-c763-594a-af11-a170087e782d`) lines 356-371 [crates/gwiki/src/ingest/file.rs:356-371]
  - Signature: `fn video_degradation_summaries(result: &VideoIngestResult) -> Vec<String> {`
  - Purpose: Indexed function `video_degradation_summaries` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:356-371]
- `read_source_file` (function) component `read_source_file [function]` (`9c64f8e8-149c-5f68-a9e8-0d61b8a81f63`) lines 373-379 [crates/gwiki/src/ingest/file.rs:373-379]
  - Signature: `fn read_source_file(path: &Path) -> Result<Vec<u8>, WikiError> {`
  - Purpose: Reads all bytes from the given 'Path' with 'std::fs::read', converting any I/O failure into 'WikiError::Io' annotated with the '"read source file"' action and the offending path. [crates/gwiki/src/ingest/file.rs:373-379]
- `ingest_stdin` (function) component `ingest_stdin [function]` (`2cf827fd-51b3-5b43-94aa-a20a4aefc1d0`) lines 382-414 [crates/gwiki/src/ingest/file.rs:382-414]
  - Signature: `pub fn ingest_stdin(`
  - Purpose: 'ingest_stdin' registers a stdin-backed source draft in the vault, renders and writes its raw markdown representation, reindexes the store, and returns an 'IngestResult' containing the source record and raw file path with no asset path. [crates/gwiki/src/ingest/file.rs:382-414]
- `detect_source_kind` (function) component `detect_source_kind [function]` (`82a3b2b3-5c93-511e-96a6-f21e36891384`) lines 416-431 [crates/gwiki/src/ingest/file.rs:416-431]
  - Signature: `fn detect_source_kind(path: &Path) -> SourceKind {`
  - Purpose: 'detect_source_kind' classifies a 'Path' by its lowercase file extension into a 'SourceKind' variant for PDFs, office documents, HTML, audio, images, video, Markdown, or plain text, and returns 'SourceKind::File' for missing or unrecognized extensions. [crates/gwiki/src/ingest/file.rs:416-431]
- `source_location` (function) component `source_location [function]` (`338edba2-7b6f-5cb1-9c2b-c86139d3d785`) lines 433-447 [crates/gwiki/src/ingest/file.rs:433-447]
  - Signature: `fn source_location(vault_root: &Path, path: &Path) -> String {`
  - Purpose: Returns a forward-slash-normalized string for 'path', using its 'vault_root'-relative path when possible, otherwise falling back to a canonicalized or original path. [crates/gwiki/src/ingest/file.rs:433-447]
- `should_store_asset` (function) component `should_store_asset [function]` (`0652ca60-05dc-53c1-988b-fa12d345a297`) lines 449-461 [crates/gwiki/src/ingest/file.rs:449-461]
  - Signature: `fn should_store_asset(kind: &SourceKind, byte_len: usize) -> bool {`
  - Purpose: Returns 'true' when the source should be stored externally, namely for any 'Audio', 'Image', 'Video', 'Pdf', 'Office', 'Html', or 'File' kind, or for 'Text' whose 'byte_len' exceeds 'TEXT_INLINE_LIMIT_BYTES'. [crates/gwiki/src/ingest/file.rs:449-461]
- `render_file_markdown` (function) component `render_file_markdown [function]` (`683c55be-1699-5f50-b792-8f27552bc94b`) lines 463-508 [crates/gwiki/src/ingest/file.rs:463-508]
  - Signature: `fn render_file_markdown(`
  - Purpose: Builds a markdown document with metadata for the source kind, location, fetch time, hash, and optional asset path, then appends the title and either lossy UTF-8 text content for Markdown/Text/Stdin inputs without an asset path or a placeholder note describing where the original artifact is stored. [crates/gwiki/src/ingest/file.rs:463-508]
- `no_ai_context` (function) component `no_ai_context [function]` (`944fa040-6581-5d6a-9403-31e6d9931563`) lines 521-530 [crates/gwiki/src/ingest/file.rs:521-530]
  - Signature: `fn no_ai_context() -> AiContext {`
  - Purpose: It constructs an 'AiContext' from environment-only resolution and then mutates it with 'IngestFileOptions { no_ai: true }' so the returned context is marked as AI-disabled. [crates/gwiki/src/ingest/file.rs:521-530]
- `ingest_options` (function) component `ingest_options [function]` (`c0686ad8-8257-5ff8-8823-fcfa817fff77`) lines 532-538 [crates/gwiki/src/ingest/file.rs:532-538]
  - Signature: `fn ingest_options() -> IngestFileOptions {`
  - Purpose: 'ingest_options' constructs and returns an 'IngestFileOptions' value with 'no_ai' set to 'true', 'video_frame_interval_seconds' set to 'Some(0)', and all other fields taken from 'IngestFileOptions::default()'. [crates/gwiki/src/ingest/file.rs:532-538]
- `source_location_preserves_external_canonical_path` (function) component `source_location_preserves_external_canonical_path [function]` (`4c41b68b-915b-538c-a10d-f40a4753e289`) lines 541-557 [crates/gwiki/src/ingest/file.rs:541-557]
  - Signature: `fn source_location_preserves_external_canonical_path() {`
  - Purpose: Verifies that 'source_location' returns the canonical, slash-normalized absolute path for a source file outside the vault instead of rewriting it relative to the vault root. [crates/gwiki/src/ingest/file.rs:541-557]
- `file_and_stdin_ingest_hash_sources` (function) component `file_and_stdin_ingest_hash_sources [function]` (`b3e07c68-6c09-51a4-a387-acd9ca0d73cb`) lines 560-613 [crates/gwiki/src/ingest/file.rs:560-613]
  - Signature: `fn file_and_stdin_ingest_hash_sources() {`
  - Purpose: It tests that ingesting a local markdown file and a stdin snapshot into 'MemoryWikiStore' produces a source manifest with two entries whose 'content_hash' values match the original byte payloads. [crates/gwiki/src/ingest/file.rs:560-613]
- `common_audio_extensions_ingest_as_audio_assets` (function) component `common_audio_extensions_ingest_as_audio_assets [function]` (`e83eb15b-2590-5c24-bfc7-810b04db6e75`) lines 616-638 [crates/gwiki/src/ingest/file.rs:616-638]
  - Signature: `fn common_audio_extensions_ingest_as_audio_assets() {`
  - Purpose: Indexed function `common_audio_extensions_ingest_as_audio_assets` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:616-638]
- `detects_audio_and_image_extensions` (function) component `detects_audio_and_image_extensions [function]` (`c5507b09-eeba-5441-a1d9-362668391565`) lines 641-655 [crates/gwiki/src/ingest/file.rs:641-655]
  - Signature: `fn detects_audio_and_image_extensions() {`
  - Purpose: Indexed function `detects_audio_and_image_extensions` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:641-655]
- `dispatches_media_to_orchestrators` (function) component `dispatches_media_to_orchestrators [function]` (`764b80db-be44-51b1-966a-acc729b14de5`) lines 658-698 [crates/gwiki/src/ingest/file.rs:658-698]
  - Signature: `fn dispatches_media_to_orchestrators() {`
  - Purpose: Creates temporary audio, image, and video files, ingests each via 'ingest_path', and asserts that the resulting record kind and stored wiki document body indicate the correct media-specific orchestrator handled the file. [crates/gwiki/src/ingest/file.rs:658-698]
- `no_ai_dispatch_degrades` (function) component `no_ai_dispatch_degrades [function]` (`2b58efa9-d0ac-5e0d-9fea-19e43c2696dd`) lines 701-728 [crates/gwiki/src/ingest/file.rs:701-728]
  - Signature: `fn no_ai_dispatch_degrades() {`
  - Purpose: Creates a temporary PNG, ingests it into 'MemoryWikiStore' with 'no_ai_context()', and asserts that the image is stored as an asset while the generated document falls back to a '## Vision Unavailable' section when AI dispatch is disabled. [crates/gwiki/src/ingest/file.rs:701-728]
- `media_dispatch_registers_once` (function) component `media_dispatch_registers_once [function]` (`e0bff932-28de-5ee8-92e7-d6f50970d2a9`) lines 731-754 [crates/gwiki/src/ingest/file.rs:731-754]
  - Signature: `fn media_dispatch_registers_once() {`
  - Purpose: Verifies that 'ingest_path' processes a temporary '.mp3' file exactly once and records a single 'SourceKind::Audio' entry in the source manifest. [crates/gwiki/src/ingest/file.rs:731-754]
- `detects_documents_and_inlines_structured_text` (function) component `detects_documents_and_inlines_structured_text [function]` (`726695e0-ae38-582d-b7cf-4b58998074a9`) lines 757-829 [crates/gwiki/src/ingest/file.rs:757-829]
  - Signature: `fn detects_documents_and_inlines_structured_text() {`
  - Purpose: Indexed function `detects_documents_and_inlines_structured_text` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:757-829]
- `dispatches_office_html_to_document` (function) component `dispatches_office_html_to_document [function]` (`8f1d3079-db6c-56ac-bb78-66ebc21887ce`) lines 833-867 [crates/gwiki/src/ingest/file.rs:833-867]
  - Signature: `fn dispatches_office_html_to_document() {`
  - Purpose: Indexed function `dispatches_office_html_to_document` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:833-867]
- `dispatches_pdf_to_combined_path` (function) component `dispatches_pdf_to_combined_path [function]` (`a376df42-ea5e-55d2-8f32-2873e2467913`) lines 871-897 [crates/gwiki/src/ingest/file.rs:871-897]
  - Signature: `fn dispatches_pdf_to_combined_path() {`
  - Purpose: Indexed function `dispatches_pdf_to_combined_path` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:871-897]
- `office_html_store_as_asset_without_documents_feature` (function) component `office_html_store_as_asset_without_documents_feature [function]` (`921ca8ab-5fc6-5adc-b40b-56815ff7c7cd`) lines 901-925 [crates/gwiki/src/ingest/file.rs:901-925]
  - Signature: `fn office_html_store_as_asset_without_documents_feature() {`
  - Purpose: Indexed function `office_html_store_as_asset_without_documents_feature` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:901-925]
- `pdf_store_as_asset_without_documents_feature` (function) component `pdf_store_as_asset_without_documents_feature [function]` (`6868ecb1-de40-56a5-a038-808eb1b71fbf`) lines 929-953 [crates/gwiki/src/ingest/file.rs:929-953]
  - Signature: `fn pdf_store_as_asset_without_documents_feature() {`
  - Purpose: Indexed function `pdf_store_as_asset_without_documents_feature` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:929-953]

