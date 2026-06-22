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

`crates/gwiki/src/ai/chunk.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AudioChunk` | class | 'AudioChunk' is an internal data container representing a time-bounded audio segment, storing its start and end timestamps in milliseconds, associated filename and filesystem path, and the raw audio bytes. [crates/gwiki/src/ai/chunk.rs:24-30] |
| `ChunkedTranscription` | class | 'ChunkedTranscription' is a crate-visible struct that wraps a single 'TranscriptionOutput' value in its 'output' field, representing chunked transcription state or result. [crates/gwiki/src/ai/chunk.rs:33-35] |
| `ChunkTranscriptionMode` | type | Indexed type `ChunkTranscriptionMode` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:38-47] |
| `AudioChunker` | type | Indexed type `AudioChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:49-56] |
| `MediaAudioChunker` | class | 'MediaAudioChunker' is a crate-private zero-sized struct that serves as a type marker or namespace for media audio chunking behavior. [crates/gwiki/src/ai/chunk.rs:58] |
| `MediaAudioChunker::split` | method | 'split' divides the transcription asset into overlapping audio windows, reads each generated chunk file into memory, and returns a 'Vec<AudioChunk>' with the original start/end timestamps and indexed '.wav' filenames, propagating I/O or split errors as 'WikiError'. [crates/gwiki/src/ai/chunk.rs:61-90] |
| `transcribe_audio_request` | function | Delegates a 'TranscriptionRequest' to 'transcribe_audio_request_with_chunker' using the provided 'TranscriptionClient', 'ChunkTranscriptionMode', and the 'MediaAudioChunker', returning a 'Result<TranscriptionOutput, WikiError>'. [crates/gwiki/src/ai/chunk.rs:93-99] |
| `transcribe_audio_request_with_chunker` | function | Routes a transcription request through single-pass transcription when the audio does not require chunking, otherwise splits it into overlapping chunks via the provided 'AudioChunker', transcribes the chunks, and returns the aggregated 'TranscriptionOutput'. [crates/gwiki/src/ai/chunk.rs:101-113] |
| `requires_chunking` | function | Returns 'true' when 'byte_len' exceeds 'MAX_AUDIO_UPLOAD_BYTES', indicating the audio must be split into chunks. [crates/gwiki/src/ai/chunk.rs:115-117] |
| `fixed_codec_bytes_for_duration` | function | Returns the total WAV byte size for a fixed-PCM stream of the given 'Duration' by computing 'ceil(duration * sample_rate * channels * bytes_per_sample / 1e9) + header_bytes', using saturating arithmetic and clamping overflow to 'u64::MAX'. [crates/gwiki/src/ai/chunk.rs:120-131] |
| `transcribe_chunks` | function | 'transcribe_chunks' sorts audio chunks by start time, transcribes each chunk independently via the provided client and mode, merges and offsets the resulting segments into an aggregate transcription while tracking completed and missing time ranges, returns the first error if every chunk fails, and optionally post-processes the assembled segments for translation mode. [crates/gwiki/src/ai/chunk.rs:133-197] |
| `transcribe_single_request` | function | Dispatches a single 'TranscriptionRequest' to either 'client.transcribe' or 'translate::translate_audio' with the appropriate target language and optional language hint based on the provided 'ChunkTranscriptionMode', returning the resulting 'TranscriptionOutput' or 'WikiError'. [crates/gwiki/src/ai/chunk.rs:199-214] |
| `transcribe_chunk_request` | function | Dispatches a transcription request to either 'client.transcribe(request)' for transcribe or segment-translation modes, or to 'translate::translate_audio(request, client, Some("en"), language_hint)' when translating audio to English, returning the resulting 'TranscriptionOutput' or 'WikiError'. [crates/gwiki/src/ai/chunk.rs:216-229] |
| `empty_output` | function | Constructs and returns a default 'TranscriptionOutput' with all optional metadata fields set to 'None', all boolean flags set to 'false', and all segment/range collections initialized empty. [crates/gwiki/src/ai/chunk.rs:231-245] |
| `merge_metadata` | function | 'merge_metadata' fills any missing optional metadata fields in 'aggregate' from 'output' and OR-accumulates the 'translated' and 'translation_degraded' boolean flags. [crates/gwiki/src/ai/chunk.rs:247-265] |
| `offset_segments` | function | Adds 'chunk_start_ms' to each transcript segment’s 'start_ms' and 'end_ms' in place, using saturating addition to avoid overflow. [crates/gwiki/src/ai/chunk.rs:267-272] |
| `append_deduped` | function | Appends each 'incoming' 'TranscriptSegment' to 'segments' unless it is deemed an overlap duplicate of the current last segment, in which case it is skipped. [crates/gwiki/src/ai/chunk.rs:274-281] |
| `is_overlap_duplicate` | function | Returns 'true' when a prior transcript segment exists, both segments have equal trimmed text, and the current segment starts no later than 'previous.end_ms + CHUNK_OVERLAP' milliseconds, using saturating addition to avoid overflow. [crates/gwiki/src/ai/chunk.rs:283-289] |
| `duration_ms` | function | Converts a 'Duration' to milliseconds as 'u64', saturating at 'u64::MAX' if 'as_millis()' does not fit in 'u64'. [crates/gwiki/src/ai/chunk.rs:291-293] |
| `TestChunkGuard::drop` | method | 'drop' clears the thread-local 'TEST_CHUNKS' state by borrowing it mutably and calling 'take()' on the stored value, effectively resetting it to 'None'/empty. [crates/gwiki/src/ai/chunk.rs:305-309] |
| `FakeChunker` | class | 'FakeChunker' is a test double that tracks the number of times it is called via 'calls: Cell<usize>' and stores a prebuilt sequence of 'AudioChunk' values in 'chunks: Vec<AudioChunk>'. [crates/gwiki/src/ai/chunk.rs:489-492] |
| `FakeChunker::new` | method | Constructs a new instance initialized with 'calls' set to '0' in a 'Cell' and stores the provided 'chunks' vector. [crates/gwiki/src/ai/chunk.rs:495-500] |
| `FakeChunker::split` | method | 'split' increments the internal 'calls' counter and returns a cloned 'Vec<AudioChunk>' from 'self.chunks', ignoring the transcription request, window, and overlap arguments. [crates/gwiki/src/ai/chunk.rs:504-512] |
| `ScriptedClient` | class | 'ScriptedClient' is a test double that holds a mutable queue of scripted 'TranscriptionOutput' results or 'WikiError' failures in a 'RefCell<Vec<...>>' for deterministic client behavior. [crates/gwiki/src/ai/chunk.rs:515-517] |

_9 more symbol(s) not shown — run `gcode outline crates/gwiki/src/ai/chunk.rs` for the full list._

_Verified by 9 in-file unit tests._

