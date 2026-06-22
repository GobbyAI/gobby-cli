---
title: crates/gwiki/src/ai
type: code_module
provenance:
- file: crates/gwiki/src/ai/chunk.rs
- file: crates/gwiki/src/ai/clients.rs
- file: crates/gwiki/src/ai/mod.rs
- file: crates/gwiki/src/ai/translate.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## Module: crates/gwiki/src/ai

The `ai` module is gwiki's bridge between raw audio/video assets and the AI services provided by `gobby_core`. It is declared as three crate-internal sub-modules in `mod.rs` (ai/mod.rs:1-4): `chunk`, `clients`, and `translate`. Together they handle the full lifecycle of an AI-assisted transcription or translation job — splitting large files into manageable pieces, dispatching each piece to the appropriate AI back end, and reassembling the results into a single `TranscriptionOutput` or `VisionExtraction` that the rest of the crate consumes.

`chunk.rs` owns all audio-splitting concerns. It defines `AudioChunk`, `ChunkedTranscription`, and the `AudioChunker` trait (implemented by `MediaAudioChunker`), plus the constants that govern how audio is partitioned — a 10-minute default window (`DEFAULT_CHUNK_WINDOW`) with a 3-second overlap (`CHUNK_OVERLAP`) and a 24 MiB per-chunk upload ceiling (`MAX_AUDIO_UPLOAD_BYTES`) (chunk.rs:11-21). The `ChunkTranscriptionMode` enum encodes whether a chunk job is a plain transcription, a translate-to-English pass, or a segment-level translation into an arbitrary target language (chunk.rs:38-47). `chunk.rs` imports `translate` from the same module (chunk.rs:5) so that chunked segment translation flows back through the shared translation logic.

`clients.rs` provides the two concrete AI client structs that the wider crate wires up at runtime. `ProductionTranscriptionClient` wraps an `AiContext` and implements `TranscriptionClient` with five methods: `transcribe`, `translate_to_english`, `translate_segments`, `translate_segment_chunks`, and `translate_segment_batch`. Each method inspects the `effective_route` returned by `gobby_core::ai::effective_route` and dispatches to either a daemon path (`transcribe_via_daemon`, `describe_image_via_daemon`, `generate_via_daemon`) or a direct path (`transcribe`, `describe_image`, `generate_text`); `AiRouting::Off` and `AiRouting::Auto` surface a `route_unavailable` error (clients.rs:42-65). `ProductionVisionClient` follows the same pattern for image extraction, implementing `VisionClient`. Internal helpers `ai_error_to_wiki_error`, `transcription_output_from_core`, and `vision_extraction_from_core` convert `gobby_core` types into gwiki's own `WikiError` / domain types. The `IndexedTranslation` struct (clients.rs:20-23) carries per-segment translation results keyed by index and is parsed by `parse_indexed_translation` in `translate.rs`.

`translate.rs` orchestrates the higher-level translation strategies. `translate_audio` is the top-level entry point: if the target is English it attempts `translate_to_english` and falls back to transcribe-then-segment-translate on failure; for other languages it always transcribes first and then calls `translate_transcription_segments` (translate.rs:6-28). `translate_transcription_segments` resolves the source language, skips translation when source and target match, and zips translated segment texts back onto the mutable `TranscriptionOutput` (translate.rs:32-57). The helper `translate_segment_texts` calls `client.translate_segments` (which itself batches through `translate_segment_chunks` → `translate_segment_batch`) and retries segment-by-segment on any batch mismatch.

### Public API Symbols

| Symbol | Kind | File | Notes |
|---|---|---|---|
| `ProductionTranscriptionClient` | struct | clients.rs | Wraps `AiContext`; implements `TranscriptionClient` |
| `ProductionTranscriptionClient::new` | method | clients.rs | Accepts `AiContext` |
| `ProductionTranscriptionClient::transcribe` | method | clients.rs | Routes via daemon or direct |
| `ProductionTranscriptionClient::translate_to_english` | method | clients.rs | Whisper translate task |
| `ProductionTranscriptionClient::translate_segments` | method | clients.rs | Chunks → batch LLM translate |
| `ProductionTranscriptionClient::translate_segment_chunks` | method | clients.rs | Splits segment list into batches |
| `ProductionTranscriptionClient::translate_segment_batch` | method | clients.rs | Single LLM call for one batch |
| `ProductionVisionClient` | struct | clients.rs | Implements `VisionClient` |
| `ProductionVisionClient::new` | method | clients.rs | Accepts `AiContext` |
| `ProductionVisionClient::extract` | method | clients.rs | Image description via daemon or direct |
| `AudioChunk` | struct | chunk.rs | Carries bytes + timing metadata |
| `ChunkedTranscription` | struct | chunk.rs | Wraps a reassembled `TranscriptionOutput` |
| `ChunkTranscriptionMode` | enum | chunk.rs | `Transcribe` / `TranslateToEnglish` / `TranslateSegments` |
| `AudioChunker` | trait | chunk.rs | `split(request, window, overlap)` |
| `MediaAudioChunker` | struct | chunk.rs | Production `AudioChunker` impl |
| `IndexedTranslation` | struct | clients.rs | `{ i: usize, text: String }` deserialized from LLM JSON |
| `segment_translation_prompt` | fn | translate.rs | Builds LLM prompt for batch translation |
| `parse_indexed_translation` | fn | translate.rs | Deserialises `IndexedTranslation` list |
| `warn_translation_batch_mismatch` | fn | translate.rs | Logs count mismatches between input and output |
| `ai_error_to_wiki_error` | fn | clients.rs | `AiError` → `WikiError` adapter |
| `transcription_output_from_core` | fn | clients.rs | `CoreTranscriptionResult` → `TranscriptionOutput` |
| `vision_extraction_from_core` | fn | clients.rs | `VisionResult` → `VisionExtraction` |

### Key Constants (chunk.rs:11-21)

| Constant | Value | Meaning |
|---|---|---|
| `MAX_AUDIO_UPLOAD_BYTES` | 24 MiB | Per-chunk size ceiling |
| `DEFAULT_CHUNK_WINDOW` | 10 min | Default audio split window |
| `CHUNK_OVERLAP` | 3 s | Overlap between adjacent chunks |
| `FIXED_PCM_SAMPLE_RATE_HZ` | 16 000 Hz | Reserved PCM format constant |
| `FIXED_PCM_CHANNELS` | 1 | Reserved PCM format constant |
| `FIXED_PCM_BYTES_PER_SAMPLE` | 2 | Reserved PCM format constant |
| `FIXED_PCM_WAV_HEADER_BYTES` | 44 | Reserved WAV header size |

### External Dependencies

| Direction | Symbol | Source |
|---|---|---|
| Imports | `transcribe_via_daemon`, `describe_image_via_daemon`, `generate_via_daemon` | `gobby_core::ai::daemon` (clients.rs:1-4) |
| Imports | `effective_route` | `gobby_core::ai::effective_route` (clients.rs:5) |
| Imports | `generate_text` | `gobby_core::ai::text` (clients.rs:6) |
| Imports | `transcribe`, `TranscriptionTask` | `gobby_core::ai::transcription` (clients.rs:7) |
| Imports | `describe_image` | `gobby_core::ai::vision` (clients.rs:8) |
| Imports | `AiContext` | `gobby_core::ai_context` (clients.rs:9) |
| Imports | `AiError`, `TranscriptionResult`, `VisionResult` | `gobby_core::ai_types` (clients.rs:10) |
| Imports | `AiCapability`, `AiRouting` | `gobby_core::config` (clients.rs:11) |
| Exports to | `crate::transcribe` traits/types | Consumed by caller supplying `TranscriptionRequest` |
| Exports to | `crate::vision` traits/types | Consumed by caller supplying `VisionRequest` |
[crates/gwiki/src/ai/chunk.rs:24-30]
[crates/gwiki/src/ai/clients.rs:20-23]
[crates/gwiki/src/ai/mod.rs:1-4]
[crates/gwiki/src/ai/translate.rs:6-29]
[crates/gwiki/src/ai/chunk.rs:33-35]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ai/chunk.rs\|crates/gwiki/src/ai/chunk.rs]] | `crates/gwiki/src/ai/chunk.rs` exposes 42 indexed API symbols. |
| [[code/files/crates/gwiki/src/ai/clients.rs\|crates/gwiki/src/ai/clients.rs]] | `crates/gwiki/src/ai/clients.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/ai/mod.rs\|crates/gwiki/src/ai/mod.rs]] | `crates/gwiki/src/ai/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gwiki/src/ai/translate.rs\|crates/gwiki/src/ai/translate.rs]] | `crates/gwiki/src/ai/translate.rs` exposes 22 indexed API symbols. |

