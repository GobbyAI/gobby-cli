---
title: crates/gwiki/src/ingest/file.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file.rs
  ranges:
  - 51-55
  - 58-61
  - 63-76
  - 78-256
  - 258-304
  - 306-330
  - 332-339
  - 341-343
  - 346-348
  - 350-365
  - 367-373
  - 375-407
  - 409-424
  - 426-440
  - 442-454
  - 456-501
  - 503-512
  - 525-534
  - 536-542
  - 545-561
  - 564-617
  - 620-642
  - 645-659
  - 662-702
  - 705-732
  - 735-758
  - 761-833
  - 837-871
  - 875-901
  - 905-929
  - 933-957
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

`crates/gwiki/src/ingest/file.rs` exposes 31 indexed API symbols.
[crates/gwiki/src/ingest/file.rs:51-55]
[crates/gwiki/src/ingest/file.rs:58-61]
[crates/gwiki/src/ingest/file.rs:63-76]
[crates/gwiki/src/ingest/file.rs:78-256]
[crates/gwiki/src/ingest/file.rs:258-304]

## API Symbols

- `StdinSnapshot` (class) component `StdinSnapshot [class]` (`037adc4d-1760-55f1-a839-e5fe26dd678a`) lines 51-55 [crates/gwiki/src/ingest/file.rs:51-55]
  - Signature: `pub struct StdinSnapshot {`
  - Purpose: StdinSnapshot is a struct that encapsulates a labeled, timestamped capture of standard input data as a raw byte vector. [crates/gwiki/src/ingest/file.rs:51-55]
- `LocalFileIngestResult` (class) component `LocalFileIngestResult [class]` (`19c5635b-7177-5a23-b621-8ba3627527e5`) lines 58-61 [crates/gwiki/src/ingest/file.rs:58-61]
  - Signature: `pub(crate) struct LocalFileIngestResult {`
  - Purpose: LocalFileIngestResult is a crate-private struct that pairs an IngestResult with a Vec<String> of degradation messages encountered during file ingestion. [crates/gwiki/src/ingest/file.rs:58-61]
- `ingest_path` (function) component `ingest_path [function]` (`780f3b70-dcc9-5f1f-a31f-0d9f28f8126c`) lines 63-76 [crates/gwiki/src/ingest/file.rs:63-76]
  - Signature: `pub fn ingest_path(`
  - Purpose: Ingests a file at the specified path into a wiki vault and reindexes the WikiIndexStore. [crates/gwiki/src/ingest/file.rs:63-76]
- `ingest_path_without_index` (function) component `ingest_path_without_index [function]` (`047d19ca-d043-58a9-9a70-55bae9088303`) lines 78-256 [crates/gwiki/src/ingest/file.rs:78-256]
  - Signature: `pub(crate) fn ingest_path_without_index(`
  - Purpose: Ingests a file without index generation by detecting its source type and routing it through specialized pipelines for transcription (audio) or vision analysis (image), returning results with degradation metadata. [crates/gwiki/src/ingest/file.rs:78-256]
- `ingest_generic_file_without_index` (function) component `ingest_generic_file_without_index [function]` (`84b12f38-046c-50af-b9be-a68288d9bb47`) lines 258-304 [crates/gwiki/src/ingest/file.rs:258-304]
  - Signature: `fn ingest_generic_file_without_index(`
  - Purpose: Reads a generic file, registers it as a source manifest, conditionally stores it as an asset based on size, renders its content to markdown with metadata, and returns the ingestion result with the manifest record and file paths. [crates/gwiki/src/ingest/file.rs:258-304]
- `attach_replay_metadata` (function) component `attach_replay_metadata [function]` (`3ed8282d-7602-5bff-acfa-b893b1665078`) lines 306-330 [crates/gwiki/src/ingest/file.rs:306-330]
  - Signature: `fn attach_replay_metadata(`
  - Purpose: Attaches replay metadata from a local file to an ingest result record and its corresponding manifest entry, updating the manifest only if the replay value differs from the existing entry. [crates/gwiki/src/ingest/file.rs:306-330]
- `transcription_degradation_summary` (function) component `transcription_degradation_summary [function]` (`da60bd8b-d33c-5a3e-9a95-96e1e0197477`) lines 332-339 [crates/gwiki/src/ingest/file.rs:332-339]
  - Signature: `fn transcription_degradation_summary(`
  - Purpose: Formats a `TranscriptionDegradation` struct into a colon-delimited string with the pattern `audio_transcription:{reason}:{fallback}`. [crates/gwiki/src/ingest/file.rs:332-339]
- `vision_degradation_summary` (function) component `vision_degradation_summary [function]` (`418e96a1-abcc-53c7-a8ae-54f71262a71b`) lines 341-343 [crates/gwiki/src/ingest/file.rs:341-343]
  - Signature: `fn vision_degradation_summary(degradation: &VisionDegradation) -> String {`
  - Purpose: This function formats and returns a colon-delimited string with the pattern "vision:{reason}:{fallback}" by extracting the reason and fallback fields from the input VisionDegradation struct. [crates/gwiki/src/ingest/file.rs:341-343]
- `document_degradation_summary` (function) component `document_degradation_summary [function]` (`fe94bf7d-54a2-5560-afb4-a88e5b49eb64`) lines 346-348 [crates/gwiki/src/ingest/file.rs:346-348]
  - Signature: `fn document_degradation_summary(degradation: &crate::document::DocumentDegradation) -> String {`
  - Purpose: Returns a formatted string representation of a `DocumentDegradation` by combining its reason and fallback fields in the format `"document:{reason}:{fallback}"`. [crates/gwiki/src/ingest/file.rs:346-348]
- `video_degradation_summaries` (function) component `video_degradation_summaries [function]` (`5cdc7973-566e-5c0f-9553-4587b8104265`) lines 350-365 [crates/gwiki/src/ingest/file.rs:350-365]
  - Signature: `fn video_degradation_summaries(result: &VideoIngestResult) -> Vec<String> {`
  - Purpose: Extracts and formats media degradations and an optional transcription degradation from a VideoIngestResult into a Vec of summary strings. [crates/gwiki/src/ingest/file.rs:350-365]
- `read_source_file` (function) component `read_source_file [function]` (`c0ab1717-b4ec-5ff9-9b5e-1d7d8c6720d6`) lines 367-373 [crates/gwiki/src/ingest/file.rs:367-373]
  - Signature: `fn read_source_file(path: &Path) -> Result<Vec<u8>, WikiError> {`
  - Purpose: Reads a file's complete contents as a byte vector, mapping any I/O errors to a `WikiError::Io` variant with contextual metadata about the operation. [crates/gwiki/src/ingest/file.rs:367-373]
- `ingest_stdin` (function) component `ingest_stdin [function]` (`ad153052-5be5-52c7-902d-ca3f36d800fd`) lines 375-407 [crates/gwiki/src/ingest/file.rs:375-407]
  - Signature: `pub fn ingest_stdin(`
  - Purpose: Ingests stdin content into a wiki vault by registering a source manifest entry, generating markdown representation, persisting to disk, and reindexing the store. [crates/gwiki/src/ingest/file.rs:375-407]
- `detect_source_kind` (function) component `detect_source_kind [function]` (`5fc6d669-623c-5d02-a97a-00bcf9b138f3`) lines 409-424 [crates/gwiki/src/ingest/file.rs:409-424]
  - Signature: `fn detect_source_kind(path: &Path) -> SourceKind {`
  - Purpose: Maps a file's lowercased extension to a corresponding `SourceKind` enum variant (PDF, Office, HTML, Audio, Image, Video, Markdown, Text), defaulting to generic `File` for unrecognized extensions. [crates/gwiki/src/ingest/file.rs:409-424]
- `source_location` (function) component `source_location [function]` (`f9ff722e-456f-5b4a-885d-5248b629cba5`) lines 426-440 [crates/gwiki/src/ingest/file.rs:426-440]
  - Signature: `fn source_location(vault_root: &Path, path: &Path) -> String {`
  - Purpose: Returns a normalized relative path string by stripping `vault_root` as a prefix from `path`, with canonicalization fallback for unresolvable paths, and conversion of backslashes to forward slashes. [crates/gwiki/src/ingest/file.rs:426-440]
- `should_store_asset` (function) component `should_store_asset [function]` (`9e226920-411e-53b9-a7cc-fce2c73ce9f5`) lines 442-454 [crates/gwiki/src/ingest/file.rs:442-454]
  - Signature: `fn should_store_asset(kind: &SourceKind, byte_len: usize) -> bool {`
  - Purpose: This function determines whether an asset should be stored based on whether its source kind is a binary/document type or if it's text exceeding the inline byte limit threshold. [crates/gwiki/src/ingest/file.rs:442-454]
- `render_file_markdown` (function) component `render_file_markdown [function]` (`86ae9fd7-23fc-5c75-9973-c43df94daa5f`) lines 456-501 [crates/gwiki/src/ingest/file.rs:456-501]
  - Signature: `fn render_file_markdown(`
  - Purpose: Generates a markdown document containing source metadata and either the decoded text content inline or a reference to a stored artifact, depending on the source kind and asset availability. [crates/gwiki/src/ingest/file.rs:456-501]
- `vision_degradation` (function) component `vision_degradation [function]` (`bc6a7eba-2ce5-5bb4-a525-5e6490b02668`) lines 503-512 [crates/gwiki/src/ingest/file.rs:503-512]
  - Signature: `fn vision_degradation(routing: AiRouting) -> VisionDegradation {`
  - Purpose: Returns a `VisionDegradation` struct that classifies vision processing failures as either "disabled" (when routing is `Off`) or "missing_endpoint" (for other routing modes), with a fallback instruction to extract only the PDF text layer and skip raster vision. [crates/gwiki/src/ingest/file.rs:503-512]
- `no_ai_context` (function) component `no_ai_context [function]` (`944fa040-6581-5d6a-9403-31e6d9931563`) lines 525-534 [crates/gwiki/src/ingest/file.rs:525-534]
  - Signature: `fn no_ai_context() -> AiContext {`
  - Purpose: Returns an `AiContext` initialized from environment variables with AI ingestion explicitly disabled via the `no_ai` flag. [crates/gwiki/src/ingest/file.rs:525-534]
- `ingest_options` (function) component `ingest_options [function]` (`c0686ad8-8257-5ff8-8823-fcfa817fff77`) lines 536-542 [crates/gwiki/src/ingest/file.rs:536-542]
  - Signature: `fn ingest_options() -> IngestFileOptions {`
  - Purpose: Returns an `IngestFileOptions` struct with AI processing disabled and video frame extraction at zero-second intervals (every frame). [crates/gwiki/src/ingest/file.rs:536-542]
- `source_location_preserves_external_canonical_path` (function) component `source_location_preserves_external_canonical_path [function]` (`4c41b68b-915b-538c-a10d-f40a4753e289`) lines 545-561 [crates/gwiki/src/ingest/file.rs:545-561]
  - Signature: `fn source_location_preserves_external_canonical_path() {`
  - Purpose: This test verifies that the `source_location` function returns the canonicalized absolute path when given a file located outside the vault directory. [crates/gwiki/src/ingest/file.rs:545-561]
- `file_and_stdin_ingest_hash_sources` (function) component `file_and_stdin_ingest_hash_sources [function]` (`b3e07c68-6c09-51a4-a387-acd9ca0d73cb`) lines 564-617 [crates/gwiki/src/ingest/file.rs:564-617]
  - Signature: `fn file_and_stdin_ingest_hash_sources() {`
  - Purpose: Tests that file and stdin sources are correctly ingested into a MemoryWikiStore and their computed content hashes accurately match entries in the generated SourceManifest. [crates/gwiki/src/ingest/file.rs:564-617]
- `common_audio_extensions_ingest_as_audio_assets` (function) component `common_audio_extensions_ingest_as_audio_assets [function]` (`e83eb15b-2590-5c24-bfc7-810b04db6e75`) lines 620-642 [crates/gwiki/src/ingest/file.rs:620-642]
  - Signature: `fn common_audio_extensions_ingest_as_audio_assets() {`
  - Purpose: Tests that audio files with common extensions (e.g., `.mp3`) are correctly ingested as `SourceKind::Audio` assets with generated asset paths in a `MemoryWikiStore`. [crates/gwiki/src/ingest/file.rs:620-642]
- `detects_audio_and_image_extensions` (function) component `detects_audio_and_image_extensions [function]` (`c5507b09-eeba-5441-a1d9-362668391565`) lines 645-659 [crates/gwiki/src/ingest/file.rs:645-659]
  - Signature: `fn detects_audio_and_image_extensions() {`
  - Purpose: A unit test that verifies `detect_source_kind()` correctly classifies common audio and image file extensions to their corresponding `SourceKind::Audio` and `SourceKind::Image` variants. [crates/gwiki/src/ingest/file.rs:645-659]
- `dispatches_media_to_orchestrators` (function) component `dispatches_media_to_orchestrators [function]` (`764b80db-be44-51b1-966a-acc729b14de5`) lines 662-702 [crates/gwiki/src/ingest/file.rs:662-702]
  - Signature: `fn dispatches_media_to_orchestrators() {`
  - Purpose: # Summary

This test function verifies that the `ingest_path` function correctly dispatches heterogeneous media types (audio, image, video) to their respective media orchestrators and produces the expected document artifacts containing type-specific processing indicators. [crates/gwiki/src/ingest/file.rs:662-702]
- `no_ai_dispatch_degrades` (function) component `no_ai_dispatch_degrades [function]` (`2b58efa9-d0ac-5e0d-9fea-19e43c2696dd`) lines 705-732 [crates/gwiki/src/ingest/file.rs:705-732]
  - Signature: `fn no_ai_dispatch_degrades() {`
  - Purpose: Tests that `ingest_path` degrades gracefully when vision AI is unavailable, still storing the asset while inserting a "Vision Unavailable" marker into the ingested document. [crates/gwiki/src/ingest/file.rs:705-732]
- `media_dispatch_registers_once` (function) component `media_dispatch_registers_once [function]` (`e0bff932-28de-5ee8-92e7-d6f50970d2a9`) lines 735-758 [crates/gwiki/src/ingest/file.rs:735-758]
  - Signature: `fn media_dispatch_registers_once() {`
  - Purpose: This test verifies that ingesting an audio file registers exactly one entry in the SourceManifest with SourceKind::Audio. [crates/gwiki/src/ingest/file.rs:735-758]
- `detects_documents_and_inlines_structured_text` (function) component `detects_documents_and_inlines_structured_text [function]` (`726695e0-ae38-582d-b7cf-4b58998074a9`) lines 761-833 [crates/gwiki/src/ingest/file.rs:761-833]
  - Signature: `fn detects_documents_and_inlines_structured_text() {`
  - Purpose: This unit test validates that `detect_source_kind()` correctly classifies various document formats (PDF, Office, HTML, and structured text) by file extension, and verifies `ingest_path()` properly ingests small and large structured text files into a memory wiki store. [crates/gwiki/src/ingest/file.rs:761-833]
- `dispatches_office_html_to_document` (function) component `dispatches_office_html_to_document [function]` (`8f1d3079-db6c-56ac-bb78-66ebc21887ce`) lines 837-871 [crates/gwiki/src/ingest/file.rs:837-871]
  - Signature: `fn dispatches_office_html_to_document() {`
  - Purpose: Tests that `ingest_path` correctly ingests an HTML file into a MemoryWikiStore, verifying document content preservation, asset creation, and manifest entry generation. [crates/gwiki/src/ingest/file.rs:837-871]
- `dispatches_pdf_to_combined_path` (function) component `dispatches_pdf_to_combined_path [function]` (`a376df42-ea5e-55d2-8f32-2873e2467913`) lines 875-901 [crates/gwiki/src/ingest/file.rs:875-901]
  - Signature: `fn dispatches_pdf_to_combined_path() {`
  - Purpose: Verifies that `ingest_path` correctly ingests a PDF file and produces the expected result record kind, asset path, and raw source metadata output. [crates/gwiki/src/ingest/file.rs:875-901]
- `office_html_store_as_asset_without_documents_feature` (function) component `office_html_store_as_asset_without_documents_feature [function]` (`921ca8ab-5fc6-5adc-b40b-56815ff7c7cd`) lines 905-929 [crates/gwiki/src/ingest/file.rs:905-929]
  - Signature: `fn office_html_store_as_asset_without_documents_feature() {`
  - Purpose: Verifies that ingesting an HTML file without documents creates an asset record with an asset path and generates a raw source file containing artifact storage metadata. [crates/gwiki/src/ingest/file.rs:905-929]
- `pdf_store_as_asset_without_documents_feature` (function) component `pdf_store_as_asset_without_documents_feature [function]` (`6868ecb1-de40-56a5-a038-808eb1b71fbf`) lines 933-957 [crates/gwiki/src/ingest/file.rs:933-957]
  - Signature: `fn pdf_store_as_asset_without_documents_feature() {`
  - Purpose: Tests that PDF ingestion generates a SourceKind::Pdf asset with metadata documenting the original artifact storage location, functioning correctly without the documents feature. [crates/gwiki/src/ingest/file.rs:933-957]

