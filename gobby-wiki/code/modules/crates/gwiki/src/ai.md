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

`crates/gwiki/src/ai` is the gwiki AI integration layer. Its module root exposes three internal submodules, `chunk`, `clients`, and `translate` [crates/gwiki/src/ai/mod.rs:1-4]. `chunk` owns audio chunk sizing and splitting abstractions, including upload/window constants, `AudioChunk`, `ChunkedTranscription`, `ChunkTranscriptionMode`, and the `AudioChunker` trait backed by `MediaAudioChunker` . `translate` owns language-normalization flow for audio translation: it prefers direct English translation, falls back to transcription plus segment translation on failure, and marks degraded output when that fallback is used .

The production client code bridges gwiki traits to `gobby_core` AI routing. `ProductionTranscriptionClient` implements `TranscriptionClient` by resolving an effective route, then calling daemon or direct transcription APIs for `AudioTranscribe`; unavailable `Off`/`Auto` routes become wiki errors through helper conversion functions . `ProductionVisionClient` follows the same responsibility for vision extraction, while helpers such as `transcription_output_from_core`, `vision_extraction_from_core`, and `ai_error_to_wiki_error` translate core-layer results into gwiki domain types.

Collaboration is centered on crate-local traits and core AI services. The module imports gwiki request/output types from `crate::transcribe`, vision types from `crate::vision`, and `WikiError` for error normalization  . It calls out to `crate::media::split_audio_file_with_overlap` for physical audio splitting , and to `gobby_core::ai` daemon/direct/text/vision/transcription APIs plus `AiContext`, `AiCapability`, and `AiRouting` for runtime AI execution .

| Area | Symbols |
| --- | --- |
| Chunking constants | `MAX_AUDIO_UPLOAD_BYTES`, `FIXED_PCM_SAMPLE_RATE_HZ`, `FIXED_PCM_CHANNELS`, `FIXED_PCM_BYTES_PER_SAMPLE`, `FIXED_PCM_WAV_HEADER_BYTES`, `DEFAULT_CHUNK_WINDOW`, `CHUNK_OVERLAP` |
| Chunking types | `AudioChunk`, `ChunkedTranscription`, `ChunkTranscriptionMode`, `AudioChunker`, `MediaAudioChunker` |
| Translation entry points | `translate_audio`, `translate_transcription_segments` |
| Production clients | `ProductionTranscriptionClient`, `ProductionVisionClient` |
| Client helpers | `route_unavailable`, `route_name`, `ai_error_to_wiki_error`, `transcription_output_from_core`, `vision_extraction_from_core` |
| Segment translation helpers | `segment_translation_prompt`, `parse_indexed_translation`, `warn_translation_batch_mismatch`, `IndexedTranslation` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ai/chunk.rs\|crates/gwiki/src/ai/chunk.rs]] | `crates/gwiki/src/ai/chunk.rs` exposes 42 indexed API symbols. |
| [[code/files/crates/gwiki/src/ai/clients.rs\|crates/gwiki/src/ai/clients.rs]] | `crates/gwiki/src/ai/clients.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/ai/mod.rs\|crates/gwiki/src/ai/mod.rs]] | `crates/gwiki/src/ai/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gwiki/src/ai/translate.rs\|crates/gwiki/src/ai/translate.rs]] | `crates/gwiki/src/ai/translate.rs` exposes 22 indexed API symbols. |

