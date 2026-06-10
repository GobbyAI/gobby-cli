---
title: crates/gwiki/src/ai/clients.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/clients.rs
  ranges:
  - 20-23
  - 25-27
  - 29-33
  - 30-32
  - 35-153
  - 36-70
  - 72-107
  - 109-152
  - 155-199
  - 156-178
  - 180-198
  - 201-219
  - 221-254
  - 256-270
  - 272-274
  - 276-280
  - 277-279
  - 282-302
  - 283-301
  - 304-313
  - 315-322
  - 324-329
  - 331-357
  - 359-372
  - 384-439
  - 442-451
  - 453-469
  - 471-483
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai/clients.rs

Module: [[code/modules/crates/gwiki/src/ai|crates/gwiki/src/ai]]

## Purpose

`crates/gwiki/src/ai/clients.rs` exposes 28 indexed API symbols.
[crates/gwiki/src/ai/clients.rs:20-23]
[crates/gwiki/src/ai/clients.rs:25-27]
[crates/gwiki/src/ai/clients.rs:29-33]
[crates/gwiki/src/ai/clients.rs:30-32]
[crates/gwiki/src/ai/clients.rs:35-153]
[crates/gwiki/src/ai/clients.rs:36-70]
[crates/gwiki/src/ai/clients.rs:72-107]
[crates/gwiki/src/ai/clients.rs:109-152]
[crates/gwiki/src/ai/clients.rs:155-199]
[crates/gwiki/src/ai/clients.rs:156-178]
[crates/gwiki/src/ai/clients.rs:180-198]
[crates/gwiki/src/ai/clients.rs:201-219]
[crates/gwiki/src/ai/clients.rs:221-254]
[crates/gwiki/src/ai/clients.rs:256-270]
[crates/gwiki/src/ai/clients.rs:272-274]
[crates/gwiki/src/ai/clients.rs:276-280]
[crates/gwiki/src/ai/clients.rs:277-279]
[crates/gwiki/src/ai/clients.rs:282-302]
[crates/gwiki/src/ai/clients.rs:283-301]
[crates/gwiki/src/ai/clients.rs:304-313]
[crates/gwiki/src/ai/clients.rs:315-322]
[crates/gwiki/src/ai/clients.rs:324-329]
[crates/gwiki/src/ai/clients.rs:331-357]
[crates/gwiki/src/ai/clients.rs:359-372]
[crates/gwiki/src/ai/clients.rs:384-439]
[crates/gwiki/src/ai/clients.rs:442-451]
[crates/gwiki/src/ai/clients.rs:453-469]
[crates/gwiki/src/ai/clients.rs:471-483]

## API Symbols

- `IndexedTranslation` (class) component `IndexedTranslation [class]` (`21d35c2b-e3d3-5381-bee4-1666c7bc2161`) lines 20-23 [crates/gwiki/src/ai/clients.rs:20-23]
  - Signature: `struct IndexedTranslation {`
  - Purpose: `IndexedTranslation` is a struct that pairs a `usize` index with a `String` to represent an indexed translation entry. [crates/gwiki/src/ai/clients.rs:20-23]
- `ProductionTranscriptionClient` (class) component `ProductionTranscriptionClient [class]` (`c4c40339-e272-5fb1-842e-eea0d78f0717`) lines 25-27 [crates/gwiki/src/ai/clients.rs:25-27]
  - Signature: `pub(crate) struct ProductionTranscriptionClient {`
  - Purpose: A crate-scoped struct that encapsulates an `AiContext` to provide transcription client functionality. [crates/gwiki/src/ai/clients.rs:25-27]
- `ProductionTranscriptionClient` (class) component `ProductionTranscriptionClient [class]` (`30c6a7ef-365b-57df-9517-6b1fee82f27f`) lines 29-33 [crates/gwiki/src/ai/clients.rs:29-33]
  - Signature: `impl ProductionTranscriptionClient {`
  - Purpose: Defines a crate-private constructor for `ProductionTranscriptionClient` that accepts and stores an `AiContext`. [crates/gwiki/src/ai/clients.rs:29-33]
- `ProductionTranscriptionClient.new` (method) component `ProductionTranscriptionClient.new [method]` (`ff895f26-4572-5021-b694-8cb6d08c96fe`) lines 30-32 [crates/gwiki/src/ai/clients.rs:30-32]
  - Signature: `pub(crate) fn new(context: AiContext) -> Self {`
  - Purpose: A constructor that initializes a new instance with the provided `AiContext` parameter. [crates/gwiki/src/ai/clients.rs:30-32]
- `ProductionTranscriptionClient` (class) component `ProductionTranscriptionClient [class]` (`c5ded5cb-2b3e-595c-b019-616651e285aa`) lines 35-153 [crates/gwiki/src/ai/clients.rs:35-153]
  - Signature: `impl TranscriptionClient for ProductionTranscriptionClient {`
  - Purpose: ProductionTranscriptionClient implements the TranscriptionClient trait to route audio transcription and English translation requests through configurable daemon or direct AI processing backends, converting results to a standardized output format. [crates/gwiki/src/ai/clients.rs:35-153]
- `ProductionTranscriptionClient.transcribe` (method) component `ProductionTranscriptionClient.transcribe [method]` (`99559d87-8b50-569a-bcc4-0074b439210d`) lines 36-70 [crates/gwiki/src/ai/clients.rs:36-70]
  - Signature: `fn transcribe(`
  - Purpose: Routes an audio transcription request to either a daemon or direct processor based on the configured AI routing strategy, transforming the core result to `TranscriptionOutput` or mapping `AIError` to `WikiError`. [crates/gwiki/src/ai/clients.rs:36-70]
- `ProductionTranscriptionClient.translate_to_english` (method) component `ProductionTranscriptionClient.translate_to_english [method]` (`f8b71bec-bcc1-5005-8a33-6d4894e5c967`) lines 72-107 [crates/gwiki/src/ai/clients.rs:72-107]
  - Signature: `fn translate_to_english(`
  - Purpose: Routes audio transcription to English via daemon or direct transcription based on configured capability routing, converting results to TranscriptionOutput or WikiError. [crates/gwiki/src/ai/clients.rs:72-107]
- `ProductionTranscriptionClient.translate_segments` (method) component `ProductionTranscriptionClient.translate_segments [method]` (`4c3b7195-017f-5a7b-8a15-2415bb2f7364`) lines 109-152 [crates/gwiki/src/ai/clients.rs:109-152]
  - Signature: `fn translate_segments(`
  - Purpose: Translates transcript segments between languages with cascading fallback: attempts full-batch translation, then progressively halves chunk sizes, then translates individually if batches fail. [crates/gwiki/src/ai/clients.rs:109-152]
- `ProductionTranscriptionClient` (class) component `ProductionTranscriptionClient [class]` (`5c1bafbf-ce3e-563a-b590-b4959177e2b9`) lines 155-199 [crates/gwiki/src/ai/clients.rs:155-199]
  - Signature: `impl ProductionTranscriptionClient {`
  - Purpose: ProductionTranscriptionClient translates transcript segment chunks through routed AI text generation with cardinality validation and indexed JSON response parsing. [crates/gwiki/src/ai/clients.rs:155-199]
- `ProductionTranscriptionClient.translate_segment_chunks` (method) component `ProductionTranscriptionClient.translate_segment_chunks [method]` (`e43c7bcc-0371-5eb1-ba23-8acb6c486a7b`) lines 156-178 [crates/gwiki/src/ai/clients.rs:156-178]
  - Signature: `fn translate_segment_chunks(`
  - Purpose: Partitions transcript segments into fixed-size chunks and sequentially translates each chunk via batch processing, validating that output cardinality matches input before returning concatenated translations. [crates/gwiki/src/ai/clients.rs:156-178]
- `ProductionTranscriptionClient.translate_segment_batch` (method) component `ProductionTranscriptionClient.translate_segment_batch [method]` (`ea9da3c6-4aec-5866-9a09-861604d4a92e`) lines 180-198 [crates/gwiki/src/ai/clients.rs:180-198]
  - Signature: `fn translate_segment_batch(`
  - Purpose: Translates a batch of transcript segments between specified languages via daemon or direct AI routing, parsing the indexed JSON response into a vector of translated strings. [crates/gwiki/src/ai/clients.rs:180-198]
- `segment_translation_prompt` (function) component `segment_translation_prompt [function]` (`f5da7098-faa8-58c2-ad54-3fd066398797`) lines 201-219 [crates/gwiki/src/ai/clients.rs:201-219]
  - Signature: `fn segment_translation_prompt(`
  - Purpose: Constructs a translation prompt by serializing indexed transcript segments as JSON and instructing translation from source to target language while preserving segment order and indexes. [crates/gwiki/src/ai/clients.rs:201-219]
- `parse_indexed_translation` (function) component `parse_indexed_translation [function]` (`a1d3249f-d12a-50b3-975a-1463e5255128`) lines 221-254 [crates/gwiki/src/ai/clients.rs:221-254]
  - Signature: `fn parse_indexed_translation(text: &str, expected_len: usize) -> Result<Vec<String>, WikiError> {`
  - Purpose: # Summary

Deserializes a JSON array of indexed translations into a complete vector, validating that all indices are within bounds, unique, and accounted for. [crates/gwiki/src/ai/clients.rs:221-254]
- `warn_translation_batch_mismatch` (function) component `warn_translation_batch_mismatch [function]` (`a87056a0-f300-52dd-840a-5252bd7026a9`) lines 256-270 [crates/gwiki/src/ai/clients.rs:256-270]
  - Signature: `fn warn_translation_batch_mismatch(`
  - Purpose: This function logs a warning when a translation batch operation either returns a result count mismatched to the expected segment count or encounters an error, signaling that the operation will be retried with smaller batches. [crates/gwiki/src/ai/clients.rs:256-270]
- `ProductionVisionClient` (class) component `ProductionVisionClient [class]` (`fa5ccca1-84be-582f-97ac-63261d366f2c`) lines 272-274 [crates/gwiki/src/ai/clients.rs:272-274]
  - Signature: `pub(crate) struct ProductionVisionClient {`
  - Purpose: `ProductionVisionClient` is a crate-private struct that wraps an `AiContext` to manage AI vision operations. [crates/gwiki/src/ai/clients.rs:272-274]
- `ProductionVisionClient` (class) component `ProductionVisionClient [class]` (`4843e211-6a3a-55bc-bd49-0a8c01afd9e4`) lines 276-280 [crates/gwiki/src/ai/clients.rs:276-280]
  - Signature: `impl ProductionVisionClient {`
  - Purpose: ProductionVisionClient provides a crate-private constructor method that instantiates a struct by wrapping an AiContext value. [crates/gwiki/src/ai/clients.rs:276-280]
- `ProductionVisionClient.new` (method) component `ProductionVisionClient.new [method]` (`511e9fdb-0fcb-5a5c-969a-a151532e83f4`) lines 277-279 [crates/gwiki/src/ai/clients.rs:277-279]
  - Signature: `pub(crate) fn new(context: AiContext) -> Self {`
  - Purpose: A crate-public constructor that creates and returns a struct instance initialized with the provided `AiContext` parameter. [crates/gwiki/src/ai/clients.rs:277-279]
- `ProductionVisionClient` (class) component `ProductionVisionClient [class]` (`9211b020-21a1-5887-99a6-6813a14cb918`) lines 282-302 [crates/gwiki/src/ai/clients.rs:282-302]
  - Signature: `impl VisionClient for ProductionVisionClient {`
  - Purpose: ProductionVisionClient implements VisionClient by routing image extraction requests to either a daemon or direct AI service based on configured AiRouting strategy, mapping results to VisionExtraction objects and errors to WikiError. [crates/gwiki/src/ai/clients.rs:282-302]
- `ProductionVisionClient.extract` (method) component `ProductionVisionClient.extract [method]` (`4a316e9f-ba1f-5356-a604-cf9faae75936`) lines 283-301 [crates/gwiki/src/ai/clients.rs:283-301]
  - Signature: `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {`
  - Purpose: Routes a `VisionRequest` through either daemon or direct AI image analysis based on configured routing strategy, returning extracted vision data as `VisionExtraction` or converting errors to `WikiError`. [crates/gwiki/src/ai/clients.rs:283-301]
- `route_unavailable` (function) component `route_unavailable [function]` (`fe53aed4-9119-555f-8930-5636f799bd8a`) lines 304-313 [crates/gwiki/src/ai/clients.rs:304-313]
  - Signature: `fn route_unavailable(capability: AiCapability, route: AiRouting) -> AiError {`
  - Purpose: Returns an `AiError::capability_unavailable` indicating that a specified AI capability is unavailable after shared effective routing has resolved a given route. [crates/gwiki/src/ai/clients.rs:304-313]
- `route_name` (function) component `route_name [function]` (`7eb7621e-6e4f-5964-9d77-eaaa0191baec`) lines 315-322 [crates/gwiki/src/ai/clients.rs:315-322]
  - Signature: `fn route_name(route: AiRouting) -> &'static str {`
  - Purpose: Returns the static string representation corresponding to the given `AiRouting` enum variant through exhaustive pattern matching. [crates/gwiki/src/ai/clients.rs:315-322]
- `ai_error_to_wiki_error` (function) component `ai_error_to_wiki_error [function]` (`366340b0-5b92-53b0-ae6c-a7defe4ac2b8`) lines 324-329 [crates/gwiki/src/ai/clients.rs:324-329]
  - Signature: `fn ai_error_to_wiki_error(error: AiError) -> WikiError {`
  - Purpose: This function converts an `AiError` into a `WikiError::Daemon` variant with the endpoint identifier "gcore::ai" and the error message stringified. [crates/gwiki/src/ai/clients.rs:324-329]
- `transcription_output_from_core` (function) component `transcription_output_from_core [function]` (`d94e9112-3e98-5e4b-b1b8-ef53ea3ac1b1`) lines 331-357 [crates/gwiki/src/ai/clients.rs:331-357]
  - Signature: `fn transcription_output_from_core(result: CoreTranscriptionResult) -> TranscriptionOutput {`
  - Purpose: Converts a `CoreTranscriptionResult` into a `TranscriptionOutput` by mapping segments to `TranscriptSegment` objects and resolving the output language via result language with source language as fallback. [crates/gwiki/src/ai/clients.rs:331-357]
- `vision_extraction_from_core` (function) component `vision_extraction_from_core [function]` (`04ed7217-5fc7-5f41-8824-978fa7b36b47`) lines 359-372 [crates/gwiki/src/ai/clients.rs:359-372]
  - Signature: `fn vision_extraction_from_core(result: VisionResult) -> VisionExtraction {`
  - Purpose: Converts a `VisionResult` into a `VisionExtraction` by extracting description and OCR text while conditionally inserting the model field into the metadata collection if not already present. [crates/gwiki/src/ai/clients.rs:359-372]
- `clients_consume_effective_off_and_direct_routes` (function) component `clients_consume_effective_off_and_direct_routes [function]` (`6c19c5e3-c505-5d59-ab6b-10a4137dc35e`) lines 384-439 [crates/gwiki/src/ai/clients.rs:384-439]
  - Signature: `fn clients_consume_effective_off_and_direct_routes() {`
  - Purpose: # Summary

Tests that `ProductionTranscriptionClient` and `ProductionVisionClient` correctly enforce AiRouting constraints by asserting expected failures when configured with `AiRouting::Off` (service unavailable) and `AiRouting::Direct` (missing api_base requirement). [crates/gwiki/src/ai/clients.rs:384-439]
- `indexed_translation_errors_name_bad_index_shape` (function) component `indexed_translation_errors_name_bad_index_shape [function]` (`081a4819-1d9c-5e1e-bb89-832c80ec26c7`) lines 442-451 [crates/gwiki/src/ai/clients.rs:442-451]
  - Signature: `fn indexed_translation_errors_name_bad_index_shape() {`
  - Purpose: Tests that `parse_indexed_translation` correctly rejects indexed translation arrays containing duplicate indices and out-of-range index values. [crates/gwiki/src/ai/clients.rs:442-451]
- `test_context` (function) component `test_context [function]` (`ddb4a9f1-ba30-59f9-a2aa-543760c7f3b9`) lines 453-469 [crates/gwiki/src/ai/clients.rs:453-469]
  - Signature: `fn test_context(binding: CapabilityBinding) -> AiContext {`
  - Purpose: Constructs an `AiContext` that replicates a single `CapabilityBinding` across all AI service bindings (embed, audio transcription/translation, vision extraction, and text generation) with a concurrency limit of 1 and a test project ID. [crates/gwiki/src/ai/clients.rs:453-469]
- `binding` (function) component `binding [function]` (`bb21c0d9-ac1e-568c-8bcb-726a905316ca`) lines 471-483 [crates/gwiki/src/ai/clients.rs:471-483]
  - Signature: `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {`
  - Purpose: This function instantiates a `CapabilityBinding` struct with provided routing and optional API base URL, while hardcoding test values for model and provider fields. [crates/gwiki/src/ai/clients.rs:471-483]

