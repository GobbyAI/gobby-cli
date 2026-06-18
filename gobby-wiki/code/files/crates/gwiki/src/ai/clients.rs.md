---
title: crates/gwiki/src/ai/clients.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/clients.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai/clients.rs

Module: [[code/modules/crates/gwiki/src/ai|crates/gwiki/src/ai]]

## Overview

`crates/gwiki/src/ai/clients.rs` exposes 23 indexed API symbols.

## How it fits

`crates/gwiki/src/ai/clients.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexedTranslation` | class | 'IndexedTranslation' is a struct that pairs a 'usize' index 'i' with a 'String' field 'text', representing a translation associated with a specific position or ordinal. [crates/gwiki/src/ai/clients.rs:20-23] |
| `ProductionTranscriptionClient` | class | 'ProductionTranscriptionClient' is an internal Rust struct that encapsulates an 'AiContext' for use by the production transcription client implementation. [crates/gwiki/src/ai/clients.rs:25-27] |
| `ProductionTranscriptionClient::new` | method | Constructs a new instance by moving the provided 'AiContext' into the 'context' field and returning 'Self { context }'. [crates/gwiki/src/ai/clients.rs:30-32] |
| `ProductionTranscriptionClient::transcribe` | method | Routes an audio transcription request by selecting the effective AI route, defaulting the MIME type, invoking either the daemon or direct transcription backend with 'AudioTranscribe' capability, and converting the core result or error into 'TranscriptionOutput' or 'WikiError'. [crates/gwiki/src/ai/clients.rs:36-70] |
| `ProductionTranscriptionClient::translate_to_english` | method | Routes an audio transcription request through the configured AI backend to translate the input into English, using a daemon path with 'target_lang: Some("en")' or a direct 'TranscriptionTask::Translate' call, and converts the core result or error into 'TranscriptionOutput' or 'WikiError'. [crates/gwiki/src/ai/clients.rs:72-107] |
| `ProductionTranscriptionClient::translate_segments` | method | 'translate_segments' tries to translate all transcript segments in one batch, falls back to progressively smaller chunked translations if the batch result length mismatches, and finally translates each segment individually, returning the first successful 'Vec<String>' or a 'WikiError' if any single-segment translation fails or returns no text. [crates/gwiki/src/ai/clients.rs:109-152] |
| `ProductionTranscriptionClient::translate_segment_chunks` | method | Translates transcript segments in fixed-size chunks via 'translate_segment_batch', validates that each batch returns exactly one translated string per input segment, and concatenates all translated texts into a single 'Vec<String>', otherwise returning a 'WikiError::Config'. [crates/gwiki/src/ai/clients.rs:156-178] |
| `ProductionTranscriptionClient::translate_segment_batch` | method | Translates a batch of 'TranscriptSegment's from 'source_lang' to 'target_lang' by building a translation prompt, routing text generation through the configured AI backend, enforcing a JSON-only system constraint, converting routing/API failures into 'WikiError', and parsing an indexed string array of the expected segment length. [crates/gwiki/src/ai/clients.rs:180-198] |
| `segment_translation_prompt` | function | Builds a translation prompt string by JSON-serializing the input transcript segments with their original indexes and formatting instructions to translate each segment from 'source_lang' to 'target_lang' and return only a JSON array of '{ "i": number, "text": string }' objects in the same order, propagating JSON serialization errors as 'WikiError::Json'. [crates/gwiki/src/ai/clients.rs:201-219] |
| `parse_indexed_translation` | function | Parses a trimmed JSON array of indexed translation objects, validates that each index is within bounds and unique for 'expected_len', and returns the translations ordered by index or a 'WikiError' if the JSON is invalid, indices are out of range/duplicated, or any segment is missing. [crates/gwiki/src/ai/clients.rs:221-254] |
| `warn_translation_batch_mismatch` | function | Logs a warning indicating that a translation batch either returned a different number of texts than expected or failed with a 'WikiError', and notes that the caller will retry using smaller batches. [crates/gwiki/src/ai/clients.rs:256-270] |
| `ProductionVisionClient` | class | 'ProductionVisionClient' is a crate-private struct that encapsulates an 'AiContext' for use as a production vision client. [crates/gwiki/src/ai/clients.rs:272-274] |
| `ProductionVisionClient::new` | method | Constructs a new instance by moving the provided 'AiContext' into the 'context' field and returning 'Self { context }'. [crates/gwiki/src/ai/clients.rs:277-279] |
| `ProductionVisionClient::extract` | method | Routes a vision-extraction request to either the daemon or direct image-description backend based on the effective routing policy, defaults the MIME type to 'application/octet-stream', converts the core response into 'VisionExtraction', and maps any AI errors into 'WikiError'. [crates/gwiki/src/ai/clients.rs:283-301] |
| `route_unavailable` | function | Constructs an 'AiError' indicating that the given 'AiCapability' is unavailable after shared effective routing resolves to the specified 'AiRouting', using the capability’s string name in both the error code and formatted message. [crates/gwiki/src/ai/clients.rs:304-313] |
| `route_name` | function | Returns the static string identifier for an 'AiRouting' variant by matching 'Auto', 'Daemon', 'Direct', and 'Off' to '"auto"', '"daemon"', '"direct"', and '"off"' respectively. [crates/gwiki/src/ai/clients.rs:315-322] |
| `ai_error_to_wiki_error` | function | Converts an 'AiError' into a 'WikiError::Daemon' with the fixed endpoint 'gcore::ai' and the error’s stringified message. [crates/gwiki/src/ai/clients.rs:324-329] |
| `transcription_output_from_core` | function | Converts a 'CoreTranscriptionResult' into a 'TranscriptionOutput' by mapping core segments to transcript segments, choosing 'language' from 'result.language' or falling back to 'source_language', and populating the remaining metadata while initializing partial/completion fields to empty or false. [crates/gwiki/src/ai/clients.rs:331-357] |
| `vision_extraction_from_core` | function | Converts a 'VisionResult' into a 'VisionExtraction' by collecting its metadata into a 'Vec', inserting '("model", result.model)' if present and not already in metadata, and then transferring 'description', 'ocr_text', and the normalized metadata into the output. [crates/gwiki/src/ai/clients.rs:359-372] |
| `clients_consume_effective_off_and_direct_routes` | function | Verifies that transcription and vision clients consume the shared effective AI routing state, treating 'Off' as unavailable and forcing 'Direct' requests onto the direct transport path with the expected 'api_base' configuration requirement. [crates/gwiki/src/ai/clients.rs:384-439] |
| `indexed_translation_errors_name_bad_index_shape` | function | Verifies that 'parse_indexed_translation' rejects malformed indexed translations by returning errors for duplicate indices and for indices that are out of range. [crates/gwiki/src/ai/clients.rs:442-451] |
| `test_context` | function | Constructs an 'AiContext' with all capability bindings ('embed', 'audio_transcribe', 'audio_translate', 'vision_extract', 'text_generate') set from the provided 'CapabilityBinding', concurrency limited to 1, no keep-alive, a new limiter of 1, and 'project_id' set to 'Some("project-123")'. [crates/gwiki/src/ai/clients.rs:453-469] |
| `binding` | function | Constructs and returns a 'CapabilityBinding' initialized with the provided 'routing', an optional 'api_base' cloned into an owned 'String', fixed test 'model' and 'provider' values, and all other fields set to 'None'. [crates/gwiki/src/ai/clients.rs:471-487] |

