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
  - 249-324
  - 327-365
  - 368-407
  - 410-451
  - 454-490
  - 493-531
  - 534-571
  - 574-612
  - 616-650
  - 654-680
  - 684-708
  - 712-736
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file/tests.rs:13-22](crates/gwiki/src/ingest/file/tests.rs#L13-L22), [crates/gwiki/src/ingest/file/tests.rs:24-30](crates/gwiki/src/ingest/file/tests.rs#L24-L30), [crates/gwiki/src/ingest/file/tests.rs:33-49](crates/gwiki/src/ingest/file/tests.rs#L33-L49), [crates/gwiki/src/ingest/file/tests.rs:52-105](crates/gwiki/src/ingest/file/tests.rs#L52-L105), [crates/gwiki/src/ingest/file/tests.rs:108-130](crates/gwiki/src/ingest/file/tests.rs#L108-L130), [crates/gwiki/src/ingest/file/tests.rs:133-147](crates/gwiki/src/ingest/file/tests.rs#L133-L147), [crates/gwiki/src/ingest/file/tests.rs:150-190](crates/gwiki/src/ingest/file/tests.rs#L150-L190), [crates/gwiki/src/ingest/file/tests.rs:193-220](crates/gwiki/src/ingest/file/tests.rs#L193-L220), [crates/gwiki/src/ingest/file/tests.rs:223-246](crates/gwiki/src/ingest/file/tests.rs#L223-L246), [crates/gwiki/src/ingest/file/tests.rs:249-324](crates/gwiki/src/ingest/file/tests.rs#L249-L324), [crates/gwiki/src/ingest/file/tests.rs:327-365](crates/gwiki/src/ingest/file/tests.rs#L327-L365), [crates/gwiki/src/ingest/file/tests.rs:368-407](crates/gwiki/src/ingest/file/tests.rs#L368-L407), [crates/gwiki/src/ingest/file/tests.rs:410-451](crates/gwiki/src/ingest/file/tests.rs#L410-L451), [crates/gwiki/src/ingest/file/tests.rs:454-490](crates/gwiki/src/ingest/file/tests.rs#L454-L490), [crates/gwiki/src/ingest/file/tests.rs:493-531](crates/gwiki/src/ingest/file/tests.rs#L493-L531), [crates/gwiki/src/ingest/file/tests.rs:534-571](crates/gwiki/src/ingest/file/tests.rs#L534-L571), [crates/gwiki/src/ingest/file/tests.rs:574-612](crates/gwiki/src/ingest/file/tests.rs#L574-L612), [crates/gwiki/src/ingest/file/tests.rs:616-650](crates/gwiki/src/ingest/file/tests.rs#L616-L650), [crates/gwiki/src/ingest/file/tests.rs:654-680](crates/gwiki/src/ingest/file/tests.rs#L654-L680), [crates/gwiki/src/ingest/file/tests.rs:684-708](crates/gwiki/src/ingest/file/tests.rs#L684-L708), [crates/gwiki/src/ingest/file/tests.rs:712-736](crates/gwiki/src/ingest/file/tests.rs#L712-L736)

</details>

# crates/gwiki/src/ingest/file/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This test module exercises the file-ingest pipeline end to end, with small helpers for building an AI context and ingest options. The tests verify source-location canonicalization, hashing for file and stdin inputs, media detection and dispatch, structured-document handling, and routing of multiple JSONL session formats to the correct orchestrators. It also checks office HTML and PDF dispatch behavior, including fallback to asset storage when document extraction is disabled.
[crates/gwiki/src/ingest/file/tests.rs:13-22]
[crates/gwiki/src/ingest/file/tests.rs:24-30]
[crates/gwiki/src/ingest/file/tests.rs:33-49]
[crates/gwiki/src/ingest/file/tests.rs:52-105]
[crates/gwiki/src/ingest/file/tests.rs:108-130]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `no_ai_context` | function | `fn no_ai_context() -> AiContext {` | `no_ai_context [function]` | `10429e53-e6ce-58de-ba73-2cfec6172411` | 13-22 [crates/gwiki/src/ingest/file/tests.rs:13-22] | Indexed function `no_ai_context` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:13-22] |
| `ingest_options` | function | `fn ingest_options() -> IngestFileOptions {` | `ingest_options [function]` | `b1de1ef8-1fbf-53bf-a96f-76ce74c753c3` | 24-30 [crates/gwiki/src/ingest/file/tests.rs:24-30] | Indexed function `ingest_options` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:24-30] |
| `source_location_preserves_external_canonical_path` | function | `fn source_location_preserves_external_canonical_path() {` | `source_location_preserves_external_canonical_path [function]` | `95b83175-91e9-5a59-91bd-e5d25eb4379f` | 33-49 [crates/gwiki/src/ingest/file/tests.rs:33-49] | Indexed function `source_location_preserves_external_canonical_path` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:33-49] |
| `file_and_stdin_ingest_hash_sources` | function | `fn file_and_stdin_ingest_hash_sources() {` | `file_and_stdin_ingest_hash_sources [function]` | `8b75c159-11d6-575b-968c-ebef4cd270a0` | 52-105 [crates/gwiki/src/ingest/file/tests.rs:52-105] | Indexed function `file_and_stdin_ingest_hash_sources` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:52-105] |
| `common_audio_extensions_ingest_as_audio_assets` | function | `fn common_audio_extensions_ingest_as_audio_assets() {` | `common_audio_extensions_ingest_as_audio_assets [function]` | `a67767c7-903e-552e-af9e-d5e7def5b090` | 108-130 [crates/gwiki/src/ingest/file/tests.rs:108-130] | Indexed function `common_audio_extensions_ingest_as_audio_assets` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:108-130] |
| `detects_audio_and_image_extensions` | function | `fn detects_audio_and_image_extensions() {` | `detects_audio_and_image_extensions [function]` | `39d16249-97cd-51e4-8205-b8ab1a3ea149` | 133-147 [crates/gwiki/src/ingest/file/tests.rs:133-147] | Indexed function `detects_audio_and_image_extensions` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:133-147] |
| `dispatches_media_to_orchestrators` | function | `fn dispatches_media_to_orchestrators() {` | `dispatches_media_to_orchestrators [function]` | `e7a24b77-e416-5e28-84fe-3e808eb3c84b` | 150-190 [crates/gwiki/src/ingest/file/tests.rs:150-190] | Indexed function `dispatches_media_to_orchestrators` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:150-190] |
| `no_ai_dispatch_degrades` | function | `fn no_ai_dispatch_degrades() {` | `no_ai_dispatch_degrades [function]` | `c332a148-a868-5a5c-9ade-e273cf9edd60` | 193-220 [crates/gwiki/src/ingest/file/tests.rs:193-220] | Indexed function `no_ai_dispatch_degrades` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:193-220] |
| `media_dispatch_registers_once` | function | `fn media_dispatch_registers_once() {` | `media_dispatch_registers_once [function]` | `1640a8b2-72ae-5998-b8fd-2de0bc496397` | 223-246 [crates/gwiki/src/ingest/file/tests.rs:223-246] | Indexed function `media_dispatch_registers_once` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:223-246] |
| `detects_documents_and_inlines_structured_text` | function | `fn detects_documents_and_inlines_structured_text() {` | `detects_documents_and_inlines_structured_text [function]` | `bab5386c-e7f2-5cae-bcce-36aca58a6b9c` | 249-324 [crates/gwiki/src/ingest/file/tests.rs:249-324] | Indexed function `detects_documents_and_inlines_structured_text` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:249-324] |
| `jsonl_session_archive_routes_to_session_orchestrator` | function | `fn jsonl_session_archive_routes_to_session_orchestrator() {` | `jsonl_session_archive_routes_to_session_orchestrator [function]` | `f4db65c2-d2e1-54af-9082-5bbaa9ec4d42` | 327-365 [crates/gwiki/src/ingest/file/tests.rs:327-365] | Indexed function `jsonl_session_archive_routes_to_session_orchestrator` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:327-365] |
| `raw_claude_jsonl_session_routes_to_session_orchestrator` | function | `fn raw_claude_jsonl_session_routes_to_session_orchestrator() {` | `raw_claude_jsonl_session_routes_to_session_orchestrator [function]` | `ee487ac7-a634-5421-8f78-37e77ed541f5` | 368-407 [crates/gwiki/src/ingest/file/tests.rs:368-407] | Indexed function `raw_claude_jsonl_session_routes_to_session_orchestrator` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:368-407] |
| `codex_jsonl_session_routes_to_session_orchestrator` | function | `fn codex_jsonl_session_routes_to_session_orchestrator() {` | `codex_jsonl_session_routes_to_session_orchestrator [function]` | `aa838a9d-afe9-5ca6-9d8d-935c2d2eb067` | 410-451 [crates/gwiki/src/ingest/file/tests.rs:410-451] | Indexed function `codex_jsonl_session_routes_to_session_orchestrator` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:410-451] |
| `gemini_jsonl_session_routes_to_session_orchestrator` | function | `fn gemini_jsonl_session_routes_to_session_orchestrator() {` | `gemini_jsonl_session_routes_to_session_orchestrator [function]` | `200e0dee-1ac8-53f7-9131-75285db99e7e` | 454-490 [crates/gwiki/src/ingest/file/tests.rs:454-490] | Indexed function `gemini_jsonl_session_routes_to_session_orchestrator` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:454-490] |
| `grok_jsonl_session_routes_to_session_orchestrator` | function | `fn grok_jsonl_session_routes_to_session_orchestrator() {` | `grok_jsonl_session_routes_to_session_orchestrator [function]` | `5cf84d93-e8e2-5119-b8b5-d9e576e2e8a3` | 493-531 [crates/gwiki/src/ingest/file/tests.rs:493-531] | Indexed function `grok_jsonl_session_routes_to_session_orchestrator` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:493-531] |
| `droid_jsonl_session_routes_to_session_orchestrator` | function | `fn droid_jsonl_session_routes_to_session_orchestrator() {` | `droid_jsonl_session_routes_to_session_orchestrator [function]` | `c026c53f-901f-56d8-a54e-8c783de48d95` | 534-571 [crates/gwiki/src/ingest/file/tests.rs:534-571] | Indexed function `droid_jsonl_session_routes_to_session_orchestrator` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:534-571] |
| `qwen_jsonl_session_routes_to_session_orchestrator` | function | `fn qwen_jsonl_session_routes_to_session_orchestrator() {` | `qwen_jsonl_session_routes_to_session_orchestrator [function]` | `5f02dc07-3cf9-50c1-9f29-0ed2dbd620b1` | 574-612 [crates/gwiki/src/ingest/file/tests.rs:574-612] | Indexed function `qwen_jsonl_session_routes_to_session_orchestrator` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:574-612] |
| `dispatches_office_html_to_document` | function | `fn dispatches_office_html_to_document() {` | `dispatches_office_html_to_document [function]` | `605baf1a-0732-5580-82bd-e1dc79a6956e` | 616-650 [crates/gwiki/src/ingest/file/tests.rs:616-650] | Indexed function `dispatches_office_html_to_document` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:616-650] |
| `dispatches_pdf_to_combined_path` | function | `fn dispatches_pdf_to_combined_path() {` | `dispatches_pdf_to_combined_path [function]` | `27f17fe5-b2c9-5987-bf3b-99184bad28b4` | 654-680 [crates/gwiki/src/ingest/file/tests.rs:654-680] | Indexed function `dispatches_pdf_to_combined_path` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:654-680] |
| `office_html_store_as_asset_without_documents_feature` | function | `fn office_html_store_as_asset_without_documents_feature() {` | `office_html_store_as_asset_without_documents_feature [function]` | `aca55119-6640-54ce-ab10-93f4ef71c5eb` | 684-708 [crates/gwiki/src/ingest/file/tests.rs:684-708] | Indexed function `office_html_store_as_asset_without_documents_feature` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:684-708] |
| `pdf_store_as_asset_without_documents_feature` | function | `fn pdf_store_as_asset_without_documents_feature() {` | `pdf_store_as_asset_without_documents_feature [function]` | `8a972c3f-1c22-54b2-b9e5-04c6290e1d44` | 712-736 [crates/gwiki/src/ingest/file/tests.rs:712-736] | Indexed function `pdf_store_as_asset_without_documents_feature` in `crates/gwiki/src/ingest/file/tests.rs`. [crates/gwiki/src/ingest/file/tests.rs:712-736] |
