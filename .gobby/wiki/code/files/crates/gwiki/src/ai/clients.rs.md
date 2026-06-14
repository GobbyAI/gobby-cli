---
title: crates/gwiki/src/ai/clients.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/clients.rs
  ranges:
  - 20-23
  - 25-27
  - 29-33
  - 35-153
  - 155-199
  - 201-219
  - 221-254
  - 256-270
  - 272-274
  - 276-280
  - 282-302
  - 304-313
  - 315-322
  - 324-329
  - 331-357
  - 359-372
  - 384-439
  - 442-451
  - 453-469
  - 471-484
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai/clients.rs

Module: [[code/modules/crates/gwiki/src/ai|crates/gwiki/src/ai]]

## Purpose

This file defines the production AI clients for the `gwiki` crate, wrapping a shared `AiContext` and exposing transcription and vision services through the crate’s `TranscriptionClient` and `VisionClient` traits. The transcription client routes work between daemon-backed and direct AI paths based on the effective capability routing, supports raw transcription and translation to English, and includes a segment-translation pipeline that batches transcript segments, retries with smaller chunks when needed, and validates JSON-indexed translation output. The vision client follows the same routing model to extract image information and converts core AI errors and results into crate-level `WikiError`, `TranscriptionOutput`, and `VisionExtraction` types.

Supporting helpers build the translation prompt, parse indexed translation responses, warn on batch mismatches, map routing and errors into local representations, and convert core transcription/vision results into the crate’s output types. The tests at the end verify routing behavior for off/direct modes, validate indexed-translation parsing failures, and provide shared test context and capability binding fixtures.
[crates/gwiki/src/ai/clients.rs:20-23]
[crates/gwiki/src/ai/clients.rs:25-27]
[crates/gwiki/src/ai/clients.rs:29-33]
[crates/gwiki/src/ai/clients.rs:30-32]
[crates/gwiki/src/ai/clients.rs:35-153]

## API Symbols

- `IndexedTranslation` (class) component `IndexedTranslation [class]` (`21d35c2b-e3d3-5381-bee4-1666c7bc2161`) lines 20-23 [crates/gwiki/src/ai/clients.rs:20-23]
  - Signature: `struct IndexedTranslation {`
  - Purpose: `IndexedTranslation` is a struct that pairs a `String` with a `usize` index for storing indexed text data. [crates/gwiki/src/ai/clients.rs:20-23]
- `ProductionTranscriptionClient` (class) component `ProductionTranscriptionClient [class]` (`c4c40339-e272-5fb1-842e-eea0d78f0717`) lines 25-27 [crates/gwiki/src/ai/clients.rs:25-27]
  - Signature: `pub(crate) struct ProductionTranscriptionClient {`
  - Purpose: `ProductionTranscriptionClient` is a crate-scoped struct that encapsulates an `AiContext` instance to serve as a production transcription client. [crates/gwiki/src/ai/clients.rs:25-27]
- `ProductionTranscriptionClient` (class) component `ProductionTranscriptionClient [class]` (`30c6a7ef-365b-57df-9517-6b1fee82f27f`) lines 29-33 [crates/gwiki/src/ai/clients.rs:29-33]
  - Signature: `impl ProductionTranscriptionClient {`
  - Purpose: ProductionTranscriptionClient is a struct providing a crate-scoped constructor that initializes itself by storing an AiContext instance. [crates/gwiki/src/ai/clients.rs:29-33]
- `ProductionTranscriptionClient.new` (method) component `ProductionTranscriptionClient.new [method]` (`ff895f26-4572-5021-b694-8cb6d08c96fe`) lines 30-32 [crates/gwiki/src/ai/clients.rs:30-32]
  - Signature: `pub(crate) fn new(context: AiContext) -> Self {`
  - Purpose: A crate-visible constructor that initializes a new instance by wrapping the provided `AiContext`. [crates/gwiki/src/ai/clients.rs:30-32]
- `ProductionTranscriptionClient` (class) component `ProductionTranscriptionClient [class]` (`c5ded5cb-2b3e-595c-b019-616651e285aa`) lines 35-153 [crates/gwiki/src/ai/clients.rs:35-153]
  - Signature: `impl TranscriptionClient for ProductionTranscriptionClient {`
  - Purpose: Implements `TranscriptionClient` to transcribe and translate audio via configurable routing between daemon and direct transcription services. [crates/gwiki/src/ai/clients.rs:35-153]
- `ProductionTranscriptionClient.transcribe` (method) component `ProductionTranscriptionClient.transcribe [method]` (`99559d87-8b50-569a-bcc4-0074b439210d`) lines 36-70 [crates/gwiki/src/ai/clients.rs:36-70]
  - Signature: `fn transcribe(`
  - Purpose: Routes a transcription request through daemon or direct AI services based on effective routing configuration, converting the result to `TranscriptionOutput` or mapping errors to `WikiError`. [crates/gwiki/src/ai/clients.rs:36-70]
- `ProductionTranscriptionClient.translate_to_english` (method) component `ProductionTranscriptionClient.translate_to_english [method]` (`f8b71bec-bcc1-5005-8a33-6d4894e5c967`) lines 72-107 [crates/gwiki/src/ai/clients.rs:72-107]
  - Signature: `fn translate_to_english(`
  - Purpose: Translates audio to English by routing through either a daemon or direct transcription service based on configured AI capability routing, then maps the result to `TranscriptionOutput` or `WikiError`. [crates/gwiki/src/ai/clients.rs:72-107]
- `ProductionTranscriptionClient.translate_segments` (method) component `ProductionTranscriptionClient.translate_segments [method]` (`4c3b7195-017f-5a7b-8a15-2415bb2f7364`) lines 109-152 [crates/gwiki/src/ai/clients.rs:109-152]
  - Signature: `fn translate_segments(`
  - Purpose: Translates transcript segments from source to target language using a cascading retry strategy that progressively reduces batch size from full batch through halved chunks to individual segments. [crates/gwiki/src/ai/clients.rs:109-152]
- `ProductionTranscriptionClient` (class) component `ProductionTranscriptionClient [class]` (`5c1bafbf-ce3e-563a-b590-b4959177e2b9`) lines 155-199 [crates/gwiki/src/ai/clients.rs:155-199]
  - Signature: `impl ProductionTranscriptionClient {`
  - Purpose: Implements chunked and batched translation of transcript segments through routed AI text generation with JSON result validation. [crates/gwiki/src/ai/clients.rs:155-199]
- `ProductionTranscriptionClient.translate_segment_chunks` (method) component `ProductionTranscriptionClient.translate_segment_chunks [method]` (`e43c7bcc-0371-5eb1-ba23-8acb6c486a7b`) lines 156-178 [crates/gwiki/src/ai/clients.rs:156-178]
  - Signature: `fn translate_segment_chunks(`
  - Purpose: Partitions transcript segments into fixed-size chunks, translates each chunk via batch translation, and validates that the output count matches the input count for each chunk. [crates/gwiki/src/ai/clients.rs:156-178]
- `ProductionTranscriptionClient.translate_segment_batch` (method) component `ProductionTranscriptionClient.translate_segment_batch [method]` (`ea9da3c6-4aec-5866-9a09-861604d4a92e`) lines 180-198 [crates/gwiki/src/ai/clients.rs:180-198]
  - Signature: `fn translate_segment_batch(`
  - Purpose: Translates a batch of transcript segments from source to target language by routing a structured prompt through an AI text generation service (via Daemon or Direct) and parsing the resulting indexed JSON translations. [crates/gwiki/src/ai/clients.rs:180-198]
- `segment_translation_prompt` (function) component `segment_translation_prompt [function]` (`f5da7098-faa8-58c2-ad54-3fd066398797`) lines 201-219 [crates/gwiki/src/ai/clients.rs:201-219]
  - Signature: `fn segment_translation_prompt(`
  - Purpose: Constructs a translation instruction prompt containing transcript segments serialized as indexed JSON objects, directing conversion from source to target language while preserving segment order and indices. [crates/gwiki/src/ai/clients.rs:201-219]
- `parse_indexed_translation` (function) component `parse_indexed_translation [function]` (`a1d3249f-d12a-50b3-975a-1463e5255128`) lines 221-254 [crates/gwiki/src/ai/clients.rs:221-254]
  - Signature: `fn parse_indexed_translation(text: &str, expected_len: usize) -> Result<Vec<String>, WikiError> {`
  - Purpose: # Summary

Parses a JSON-encoded array of indexed translations, validates completeness and absence of duplicates or out-of-bounds indices, and reconstructs them into a contiguous vector of strings matching the expected length. [crates/gwiki/src/ai/clients.rs:221-254]
- `warn_translation_batch_mismatch` (function) component `warn_translation_batch_mismatch [function]` (`a87056a0-f300-52dd-840a-5252bd7026a9`) lines 256-270 [crates/gwiki/src/ai/clients.rs:256-270]
  - Signature: `fn warn_translation_batch_mismatch(`
  - Purpose: Logs a warning when a translation batch operation fails or returns a result count mismatched with the expected segment count, indicating retry with smaller batches. [crates/gwiki/src/ai/clients.rs:256-270]
- `ProductionVisionClient` (class) component `ProductionVisionClient [class]` (`fa5ccca1-84be-582f-97ac-63261d366f2c`) lines 272-274 [crates/gwiki/src/ai/clients.rs:272-274]
  - Signature: `pub(crate) struct ProductionVisionClient {`
  - Purpose: A crate-scoped struct that encapsulates an `AiContext` to provide production-grade vision AI client capabilities. [crates/gwiki/src/ai/clients.rs:272-274]
- `ProductionVisionClient` (class) component `ProductionVisionClient [class]` (`4843e211-6a3a-55bc-bd49-0a8c01afd9e4`) lines 276-280 [crates/gwiki/src/ai/clients.rs:276-280]
  - Signature: `impl ProductionVisionClient {`
  - Purpose: ProductionVisionClient implements a crate-private constructor that wraps an AiContext dependency for initialization. [crates/gwiki/src/ai/clients.rs:276-280]
- `ProductionVisionClient.new` (method) component `ProductionVisionClient.new [method]` (`511e9fdb-0fcb-5a5c-969a-a151532e83f4`) lines 277-279 [crates/gwiki/src/ai/clients.rs:277-279]
  - Signature: `pub(crate) fn new(context: AiContext) -> Self {`
  - Purpose: A crate-public constructor that instantiates `Self` with the provided `AiContext` parameter. [crates/gwiki/src/ai/clients.rs:277-279]
- `ProductionVisionClient` (class) component `ProductionVisionClient [class]` (`9211b020-21a1-5887-99a6-6813a14cb918`) lines 282-302 [crates/gwiki/src/ai/clients.rs:282-302]
  - Signature: `impl VisionClient for ProductionVisionClient {`
  - Purpose: `ProductionVisionClient` implements the `VisionClient` trait to extract image features via capability-aware routing that dispatches vision requests to either daemon-based or direct AI processing pipelines, with error translation to `WikiError`. [crates/gwiki/src/ai/clients.rs:282-302]
- `ProductionVisionClient.extract` (method) component `ProductionVisionClient.extract [method]` (`4a316e9f-ba1f-5356-a604-cf9faae75936`) lines 283-301 [crates/gwiki/src/ai/clients.rs:283-301]
  - Signature: `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Routes a vision extraction request through either daemon-based or direct AI processing based on effective routing configuration, mapping the response to `VisionExtraction` or `WikiError`. [crates/gwiki/src/ai/clients.rs:283-301]
- `route_unavailable` (function) component `route_unavailable [function]` (`fe53aed4-9119-555f-8930-5636f799bd8a`) lines 304-313 [crates/gwiki/src/ai/clients.rs:304-313]
  - Signature: `fn route_unavailable(capability: AiCapability, route: AiRouting) -> AiError {`
  - Purpose: Returns an `AiError` indicating the specified capability is unavailable after shared effective routing resolves to the given route. [crates/gwiki/src/ai/clients.rs:304-313]
- `route_name` (function) component `route_name [function]` (`7eb7621e-6e4f-5964-9d77-eaaa0191baec`) lines 315-322 [crates/gwiki/src/ai/clients.rs:315-322]
  - Signature: `fn route_name(route: AiRouting) -> &'static str {`
  - Purpose: Maps an `AiRouting` enum variant to its corresponding static string representation. [crates/gwiki/src/ai/clients.rs:315-322]
- `ai_error_to_wiki_error` (function) component `ai_error_to_wiki_error [function]` (`366340b0-5b92-53b0-ae6c-a7defe4ac2b8`) lines 324-329 [crates/gwiki/src/ai/clients.rs:324-329]
  - Signature: `fn ai_error_to_wiki_error(error: AiError) -> WikiError {`
  - Purpose: Converts an `AiError` into a `WikiError::Daemon` variant with the hardcoded endpoint identifier `"gcore::ai"` and the error's string representation as the message. [crates/gwiki/src/ai/clients.rs:324-329]
- `transcription_output_from_core` (function) component `transcription_output_from_core [function]` (`d94e9112-3e98-5e4b-b1b8-ef53ea3ac1b1`) lines 331-357 [crates/gwiki/src/ai/clients.rs:331-357]
  - Signature: `fn transcription_output_from_core(result: CoreTranscriptionResult) -> TranscriptionOutput {`
  - Purpose: Converts a `CoreTranscriptionResult` into a `TranscriptionOutput` by remapping segments to `TranscriptSegment` structs and resolving the output language with source language fallback. [crates/gwiki/src/ai/clients.rs:331-357]
- `vision_extraction_from_core` (function) component `vision_extraction_from_core [function]` (`04ed7217-5fc7-5f41-8824-978fa7b36b47`) lines 359-372 [crates/gwiki/src/ai/clients.rs:359-372]
  - Signature: `fn vision_extraction_from_core(result: VisionResult) -> VisionExtraction {`
  - Purpose: Converts a `VisionResult` to a `VisionExtraction`, conditionally appending the model field to metadata if it exists and isn't already present. [crates/gwiki/src/ai/clients.rs:359-372]
- `clients_consume_effective_off_and_direct_routes` (function) component `clients_consume_effective_off_and_direct_routes [function]` (`6c19c5e3-c505-5d59-ab6b-10a4137dc35e`) lines 384-439 [crates/gwiki/src/ai/clients.rs:384-439]
  - Signature: `fn clients_consume_effective_off_and_direct_routes() {`
  - Purpose: Tests that ProductionTranscriptionClient and ProductionVisionClient properly enforce service unavailability when AiRouting is set to Off and require explicit API configuration when set to Direct. [crates/gwiki/src/ai/clients.rs:384-439]
- `indexed_translation_errors_name_bad_index_shape` (function) component `indexed_translation_errors_name_bad_index_shape [function]` (`081a4819-1d9c-5e1e-bb89-832c80ec26c7`) lines 442-451 [crates/gwiki/src/ai/clients.rs:442-451]
  - Signature: `fn indexed_translation_errors_name_bad_index_shape() {`
  - Purpose: Unit test that validates `parse_indexed_translation` correctly rejects both duplicate indices and indices exceeding the target array length. [crates/gwiki/src/ai/clients.rs:442-451]
- `test_context` (function) component `test_context [function]` (`ddb4a9f1-ba30-59f9-a2aa-543760c7f3b9`) lines 453-469 [crates/gwiki/src/ai/clients.rs:453-469]
  - Signature: `fn test_context(binding: CapabilityBinding) -> AiContext {`
  - Purpose: Constructs an `AiContext` test instance by replicating a single `CapabilityBinding` across all AI service types (embed, audio transcription/translation, vision, text generation) with serialized execution (max_concurrency=1), unit rate limiting, and project ID "project-123". [crates/gwiki/src/ai/clients.rs:453-469]
- `binding` (function) component `binding [function]` (`bb21c0d9-ac1e-568c-8bcb-726a905316ca`) lines 471-484 [crates/gwiki/src/ai/clients.rs:471-484]
  - Signature: `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {`
  - Purpose: Constructs a `CapabilityBinding` struct with the provided `routing` and `api_base` parameters, hard-coded test model and provider identifiers, and `None` for all remaining fields. [crates/gwiki/src/ai/clients.rs:471-484]

