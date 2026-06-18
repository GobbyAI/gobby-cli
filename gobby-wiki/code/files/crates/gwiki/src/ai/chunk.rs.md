---
title: crates/gwiki/src/ai/chunk.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/chunk.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai/chunk.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ai/chunk.rs` exposes 42 indexed API symbols.

## How it fits

`crates/gwiki/src/ai/chunk.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AudioChunk` | class | Indexed class `AudioChunk` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:24-30] |
| `ChunkedTranscription` | class | Indexed class `ChunkedTranscription` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:33-35] |
| `ChunkTranscriptionMode` | type | Indexed type `ChunkTranscriptionMode` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:38-47] |
| `AudioChunker` | type | Indexed type `AudioChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:49-56] |
| `MediaAudioChunker` | class | Indexed class `MediaAudioChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:58] |
| `MediaAudioChunker::split` | method | Indexed method `MediaAudioChunker::split` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:61-90] |
| `transcribe_audio_request` | function | Indexed function `transcribe_audio_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:93-99] |
| `transcribe_audio_request_with_chunker` | function | Indexed function `transcribe_audio_request_with_chunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:101-113] |
| `requires_chunking` | function | Indexed function `requires_chunking` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:115-117] |
| `fixed_codec_bytes_for_duration` | function | Indexed function `fixed_codec_bytes_for_duration` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:120-131] |
| `transcribe_chunks` | function | Indexed function `transcribe_chunks` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:133-197] |
| `transcribe_single_request` | function | Indexed function `transcribe_single_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:199-214] |
| `transcribe_chunk_request` | function | Indexed function `transcribe_chunk_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:216-229] |
| `empty_output` | function | Indexed function `empty_output` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:231-245] |
| `merge_metadata` | function | Indexed function `merge_metadata` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:247-265] |
| `offset_segments` | function | Indexed function `offset_segments` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:267-272] |
| `append_deduped` | function | Indexed function `append_deduped` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:274-281] |
| `is_overlap_duplicate` | function | Indexed function `is_overlap_duplicate` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:283-289] |
| `duration_ms` | function | Indexed function `duration_ms` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:291-293] |
| `TestChunkGuard` | class | Indexed class `TestChunkGuard` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:301] |
| `TestChunkGuard::drop` | method | Indexed method `TestChunkGuard::drop` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:305-309] |
| `install_test_chunks` | function | Indexed function `install_test_chunks` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:313-319] |
| `take_test_chunks` | function | Indexed function `take_test_chunks` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:322-324] |
| `chunks_under_limit_fixed_codec` | function | Indexed function `chunks_under_limit_fixed_codec` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:335-343] |
| `fixed_codec_bytes_include_subsecond_durations` | function | Indexed function `fixed_codec_bytes_include_subsecond_durations` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:346-351] |
| `offsets_and_dedups` | function | Indexed function `offsets_and_dedups` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:354-385] |
| `short_audio_bypasses_ffmpeg` | function | Indexed function `short_audio_bypasses_ffmpeg` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:388-403] |
| `short_translate_segments_translates_without_chunking` | function | Indexed function `short_translate_segments_translates_without_chunking` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:406-432] |
| `partial_chunk_outcome` | function | Indexed function `partial_chunk_outcome` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:435-487] |
| `FakeChunker` | class | Indexed class `FakeChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:489-492] |
| `FakeChunker::new` | method | Indexed method `FakeChunker::new` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:495-500] |
| `FakeChunker::split` | method | Indexed method `FakeChunker::split` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:504-512] |
| `ScriptedClient` | class | Indexed class `ScriptedClient` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:515-517] |
| `ScriptedClient::new` | method | Indexed method `ScriptedClient::new` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:520-524] |
| `ScriptedClient::transcribe` | method | Indexed method `ScriptedClient::transcribe` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:528-533] |
| `TranslatingClient` | class | Indexed class `TranslatingClient` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:536-539] |
| `TranslatingClient::transcribe` | method | Indexed method `TranslatingClient::transcribe` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:542-548] |
| `TranslatingClient::translate_segments` | method | Indexed method `TranslatingClient::translate_segments` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:550-561] |
| `short_request` | function | Indexed function `short_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:564-571] |
| `long_request` | function | Indexed function `long_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:574-584] |
| `chunk` | function | Indexed function `chunk` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:586-594] |
| `output` | function | Indexed function `output` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:596-617] |

