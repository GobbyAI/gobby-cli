---
title: crates/gwiki/src/ingest/file/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/tests.rs
  ranges:
  - 13-22
  - 24-30
  - 33-49
  - 52-105
  - 108-130
  - 133-147
  - 150-190
  - 193-220
  - 223-246
  - 249-321
  - 325-359
  - 363-389
  - 393-417
  - 421-445
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file/tests.rs

Module: [[code/modules/crates/gwiki/src/ingest/file|crates/gwiki/src/ingest/file]]

## Purpose

Test module for file ingestion in `gwiki`, with helpers that build a no-AI `AiContext` and default ingest options for deterministic test runs. The tests exercise `source_location`, `ingest_path`, and `ingest_stdin` across local files and media types, checking source hashing, source-kind detection, media/document dispatch, no-AI fallback behavior, and the resulting manifest/raw artifact records in `MemoryWikiStore`.
[crates/gwiki/src/ingest/file/tests.rs:13-22]
[crates/gwiki/src/ingest/file/tests.rs:24-30]
[crates/gwiki/src/ingest/file/tests.rs:33-49]
[crates/gwiki/src/ingest/file/tests.rs:52-105]
[crates/gwiki/src/ingest/file/tests.rs:108-130]

## API Symbols

- `no_ai_context` (function) component `no_ai_context [function]` (`10429e53-e6ce-58de-ba73-2cfec6172411`) lines 13-22 [crates/gwiki/src/ingest/file/tests.rs:13-22]
  - Signature: `fn no_ai_context() -> AiContext {`
  - Purpose: Constructs an 'AiContext' resolved from an 'EnvOnlySource', then applies 'IngestFileOptions' with 'no_ai: true' to mark the resulting context as AI-disabled before returning it. [crates/gwiki/src/ingest/file/tests.rs:13-22]
- `ingest_options` (function) component `ingest_options [function]` (`b1de1ef8-1fbf-53bf-a96f-76ce74c753c3`) lines 24-30 [crates/gwiki/src/ingest/file/tests.rs:24-30]
  - Signature: `fn ingest_options() -> IngestFileOptions {`
  - Purpose: Returns default 'IngestFileOptions' with 'no_ai' forced to 'true' and 'video_frame_interval_seconds' set to 'Some(0)'. [crates/gwiki/src/ingest/file/tests.rs:24-30]
- `source_location_preserves_external_canonical_path` (function) component `source_location_preserves_external_canonical_path [function]` (`95b83175-91e9-5a59-91bd-e5d25eb4379f`) lines 33-49 [crates/gwiki/src/ingest/file/tests.rs:33-49]
  - Signature: `fn source_location_preserves_external_canonical_path() {`
  - Purpose: Verifies that 'source_location' returns the canonicalized, forward-slash-normalized path of a source file outside the vault root rather than rewriting it relative to the vault. [crates/gwiki/src/ingest/file/tests.rs:33-49]
- `file_and_stdin_ingest_hash_sources` (function) component `file_and_stdin_ingest_hash_sources [function]` (`8b75c159-11d6-575b-968c-ebef4cd270a0`) lines 52-105 [crates/gwiki/src/ingest/file/tests.rs:52-105]
  - Signature: `fn file_and_stdin_ingest_hash_sources() {`
  - Purpose: Creates a temporary wiki store, ingests both a markdown file and a stdin snapshot into source-managed markdown artifacts, then verifies the source manifest records two entries with the expected content hashes and that the generated raw outputs contain the original text. [crates/gwiki/src/ingest/file/tests.rs:52-105]
- `common_audio_extensions_ingest_as_audio_assets` (function) component `common_audio_extensions_ingest_as_audio_assets [function]` (`a67767c7-903e-552e-af9e-d5e7def5b090`) lines 108-130 [crates/gwiki/src/ingest/file/tests.rs:108-130]
  - Signature: `fn common_audio_extensions_ingest_as_audio_assets() {`
  - Purpose: Creates a temporary '.mp3' file, ingests it with 'ingest_path', and asserts that the resulting record is classified as 'SourceKind::Audio' with a populated asset path. [crates/gwiki/src/ingest/file/tests.rs:108-130]
- `detects_audio_and_image_extensions` (function) component `detects_audio_and_image_extensions [function]` (`39d16249-97cd-51e4-8205-b8ab1a3ea149`) lines 133-147 [crates/gwiki/src/ingest/file/tests.rs:133-147]
  - Signature: `fn detects_audio_and_image_extensions() {`
  - Purpose: Verifies that 'detect_source_kind' classifies files with common audio extensions as 'SourceKind::Audio' and common image extensions as 'SourceKind::Image'. [crates/gwiki/src/ingest/file/tests.rs:133-147]
- `dispatches_media_to_orchestrators` (function) component `dispatches_media_to_orchestrators [function]` (`e7a24b77-e416-5e28-84fe-3e808eb3c84b`) lines 150-190 [crates/gwiki/src/ingest/file/tests.rs:150-190]
  - Signature: `fn dispatches_media_to_orchestrators() {`
  - Purpose: Creates temporary audio, image, and video files and verifies that 'ingest_path' routes each to the correct media kind, returns a record with the expected 'SourceKind', produces an asset path, and stores a document containing the corresponding orchestrator-specific fallback section. [crates/gwiki/src/ingest/file/tests.rs:150-190]
- `no_ai_dispatch_degrades` (function) component `no_ai_dispatch_degrades [function]` (`c332a148-a868-5a5c-9ade-e273cf9edd60`) lines 193-220 [crates/gwiki/src/ingest/file/tests.rs:193-220]
  - Signature: `fn no_ai_dispatch_degrades() {`
  - Purpose: Verifies that ingesting a local image file with a no-AI context still succeeds and degrades gracefully by producing an asset path while inserting a document body that contains the '## Vision Unavailable' fallback. [crates/gwiki/src/ingest/file/tests.rs:193-220]
- `media_dispatch_registers_once` (function) component `media_dispatch_registers_once [function]` (`1640a8b2-72ae-5998-b8fd-2de0bc496397`) lines 223-246 [crates/gwiki/src/ingest/file/tests.rs:223-246]
  - Signature: `fn media_dispatch_registers_once() {`
  - Purpose: Creates a temporary '.mp3' file, ingests it into a 'MemoryWikiStore' via 'ingest_path', and verifies the resulting source manifest contains exactly one 'SourceKind::Audio' entry. [crates/gwiki/src/ingest/file/tests.rs:223-246]
- `detects_documents_and_inlines_structured_text` (function) component `detects_documents_and_inlines_structured_text [function]` (`bab5386c-e7f2-5cae-bcce-36aca58a6b9c`) lines 249-321 [crates/gwiki/src/ingest/file/tests.rs:249-321]
  - Signature: `fn detects_documents_and_inlines_structured_text() {`
  - Purpose: Verifies 'detect_source_kind' classifies PDFs, Office files, HTML, and common structured text formats correctly, and that ingesting a small structured-text file yields 'SourceKind::Text' without an asset path. [crates/gwiki/src/ingest/file/tests.rs:249-321]
- `dispatches_office_html_to_document` (function) component `dispatches_office_html_to_document [function]` (`7415e42f-748d-52f5-8e6c-e7dfce775e0f`) lines 325-359 [crates/gwiki/src/ingest/file/tests.rs:325-359]
  - Signature: `fn dispatches_office_html_to_document() {`
  - Purpose: Creates a temporary HTML file, ingests it through 'ingest_path', and asserts the result is classified as 'SourceKind::Html', produces an asset path, persists the page body into the memory store, and records exactly one manifest entry. [crates/gwiki/src/ingest/file/tests.rs:325-359]
- `dispatches_pdf_to_combined_path` (function) component `dispatches_pdf_to_combined_path [function]` (`6d55bb83-50aa-5ab6-b167-69648a379210`) lines 363-389 [crates/gwiki/src/ingest/file/tests.rs:363-389]
  - Signature: `fn dispatches_pdf_to_combined_path() {`
  - Purpose: Verifies that ingesting a PDF through 'ingest_path' produces a 'SourceKind::Pdf' record with a populated asset path and raw metadata including 'source_kind: pdf', a 'page_count', and 'vision_used: "false"'. [crates/gwiki/src/ingest/file/tests.rs:363-389]
- `office_html_store_as_asset_without_documents_feature` (function) component `office_html_store_as_asset_without_documents_feature [function]` (`60b5dca8-3d53-5d7a-abb4-a6fac808bc20`) lines 393-417 [crates/gwiki/src/ingest/file/tests.rs:393-417]
  - Signature: `fn office_html_store_as_asset_without_documents_feature() {`
  - Purpose: Verifies that ingesting a standalone HTML file into a 'MemoryWikiStore' without any documents classifies the record as 'SourceKind::Html', persists an asset path, and writes a raw source file containing the “Original artifact stored under” marker. [crates/gwiki/src/ingest/file/tests.rs:393-417]
- `pdf_store_as_asset_without_documents_feature` (function) component `pdf_store_as_asset_without_documents_feature [function]` (`28c3a49e-6dc1-55cd-a38f-97158ba4aea3`) lines 421-445 [crates/gwiki/src/ingest/file/tests.rs:421-445]
  - Signature: `fn pdf_store_as_asset_without_documents_feature() {`
  - Purpose: Creates a temporary PDF, ingests it into a 'MemoryWikiStore' without the documents feature, and asserts the result is recorded as 'SourceKind::Pdf' with an asset path and a raw source file noting the original artifact location. [crates/gwiki/src/ingest/file/tests.rs:421-445]

