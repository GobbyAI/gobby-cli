---
title: crates/gwiki/src/ai/clients.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/clients.rs
  ranges:
  - 20-23
  - 25-27
  - 30-32
  - 36-70
  - 72-107
  - 109-152
  - 156-178
  - 180-198
  - 201-219
  - 221-254
  - 256-270
  - 272-274
  - 277-279
  - 283-301
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ai/clients.rs:20-23](crates/gwiki/src/ai/clients.rs#L20-L23), [crates/gwiki/src/ai/clients.rs:25-27](crates/gwiki/src/ai/clients.rs#L25-L27), [crates/gwiki/src/ai/clients.rs:30-32](crates/gwiki/src/ai/clients.rs#L30-L32), [crates/gwiki/src/ai/clients.rs:36-70](crates/gwiki/src/ai/clients.rs#L36-L70), [crates/gwiki/src/ai/clients.rs:72-107](crates/gwiki/src/ai/clients.rs#L72-L107), [crates/gwiki/src/ai/clients.rs:109-152](crates/gwiki/src/ai/clients.rs#L109-L152), [crates/gwiki/src/ai/clients.rs:156-178](crates/gwiki/src/ai/clients.rs#L156-L178), [crates/gwiki/src/ai/clients.rs:180-198](crates/gwiki/src/ai/clients.rs#L180-L198), [crates/gwiki/src/ai/clients.rs:201-219](crates/gwiki/src/ai/clients.rs#L201-L219), [crates/gwiki/src/ai/clients.rs:221-254](crates/gwiki/src/ai/clients.rs#L221-L254), [crates/gwiki/src/ai/clients.rs:256-270](crates/gwiki/src/ai/clients.rs#L256-L270), [crates/gwiki/src/ai/clients.rs:272-274](crates/gwiki/src/ai/clients.rs#L272-L274), [crates/gwiki/src/ai/clients.rs:277-279](crates/gwiki/src/ai/clients.rs#L277-L279), [crates/gwiki/src/ai/clients.rs:283-301](crates/gwiki/src/ai/clients.rs#L283-L301), [crates/gwiki/src/ai/clients.rs:304-313](crates/gwiki/src/ai/clients.rs#L304-L313), [crates/gwiki/src/ai/clients.rs:315-322](crates/gwiki/src/ai/clients.rs#L315-L322), [crates/gwiki/src/ai/clients.rs:324-329](crates/gwiki/src/ai/clients.rs#L324-L329), [crates/gwiki/src/ai/clients.rs:331-357](crates/gwiki/src/ai/clients.rs#L331-L357), [crates/gwiki/src/ai/clients.rs:359-372](crates/gwiki/src/ai/clients.rs#L359-L372), [crates/gwiki/src/ai/clients.rs:384-439](crates/gwiki/src/ai/clients.rs#L384-L439), [crates/gwiki/src/ai/clients.rs:442-451](crates/gwiki/src/ai/clients.rs#L442-L451), [crates/gwiki/src/ai/clients.rs:453-469](crates/gwiki/src/ai/clients.rs#L453-L469), [crates/gwiki/src/ai/clients.rs:471-484](crates/gwiki/src/ai/clients.rs#L471-L484)

</details>

# crates/gwiki/src/ai/clients.rs

Module: [[code/modules/crates/gwiki/src/ai|crates/gwiki/src/ai]]

## Purpose

This file implements the production AI client layer for `gwiki`, wiring `AiContext`-based routing into transcription, translation, and vision extraction. `ProductionTranscriptionClient` chooses between daemon and direct backends for audio transcription and translation, builds the segment-translation prompt, parses indexed translation responses back into ordered transcript segments, and normalizes core AI errors into `WikiError`. `ProductionVisionClient` does the same for image extraction. The helper functions encapsulate route validation, route naming, response conversion, batch mismatch warnings, and test utilities/binding setup so the client methods stay focused on dispatching requests and adapting core AI results to wiki-specific types.
[crates/gwiki/src/ai/clients.rs:20-23]
[crates/gwiki/src/ai/clients.rs:25-27]
[crates/gwiki/src/ai/clients.rs:30-32]
[crates/gwiki/src/ai/clients.rs:36-70]
[crates/gwiki/src/ai/clients.rs:72-107]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IndexedTranslation` | class | `struct IndexedTranslation {` | `IndexedTranslation [class]` | `21d35c2b-e3d3-5381-bee4-1666c7bc2161` | 20-23 [crates/gwiki/src/ai/clients.rs:20-23] | Indexed class `IndexedTranslation` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:20-23] |
| `ProductionTranscriptionClient` | class | `pub(crate) struct ProductionTranscriptionClient {` | `ProductionTranscriptionClient [class]` | `c4c40339-e272-5fb1-842e-eea0d78f0717` | 25-27 [crates/gwiki/src/ai/clients.rs:25-27] | Indexed class `ProductionTranscriptionClient` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:25-27] |
| `ProductionTranscriptionClient::new` | method | `pub(crate) fn new(context: AiContext) -> Self {` | `ProductionTranscriptionClient::new [method]` | `ff895f26-4572-5021-b694-8cb6d08c96fe` | 30-32 [crates/gwiki/src/ai/clients.rs:30-32] | Indexed method `ProductionTranscriptionClient::new` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:30-32] |
| `ProductionTranscriptionClient::transcribe` | method | `fn transcribe(` | `ProductionTranscriptionClient::transcribe [method]` | `99559d87-8b50-569a-bcc4-0074b439210d` | 36-70 [crates/gwiki/src/ai/clients.rs:36-70] | Indexed method `ProductionTranscriptionClient::transcribe` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:36-70] |
| `ProductionTranscriptionClient::translate_to_english` | method | `fn translate_to_english(` | `ProductionTranscriptionClient::translate_to_english [method]` | `f8b71bec-bcc1-5005-8a33-6d4894e5c967` | 72-107 [crates/gwiki/src/ai/clients.rs:72-107] | Indexed method `ProductionTranscriptionClient::translate_to_english` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:72-107] |
| `ProductionTranscriptionClient::translate_segments` | method | `fn translate_segments(` | `ProductionTranscriptionClient::translate_segments [method]` | `4c3b7195-017f-5a7b-8a15-2415bb2f7364` | 109-152 [crates/gwiki/src/ai/clients.rs:109-152] | Indexed method `ProductionTranscriptionClient::translate_segments` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:109-152] |
| `ProductionTranscriptionClient::translate_segment_chunks` | method | `fn translate_segment_chunks(` | `ProductionTranscriptionClient::translate_segment_chunks [method]` | `e43c7bcc-0371-5eb1-ba23-8acb6c486a7b` | 156-178 [crates/gwiki/src/ai/clients.rs:156-178] | Indexed method `ProductionTranscriptionClient::translate_segment_chunks` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:156-178] |
| `ProductionTranscriptionClient::translate_segment_batch` | method | `fn translate_segment_batch(` | `ProductionTranscriptionClient::translate_segment_batch [method]` | `ea9da3c6-4aec-5866-9a09-861604d4a92e` | 180-198 [crates/gwiki/src/ai/clients.rs:180-198] | Indexed method `ProductionTranscriptionClient::translate_segment_batch` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:180-198] |
| `segment_translation_prompt` | function | `fn segment_translation_prompt(` | `segment_translation_prompt [function]` | `f5da7098-faa8-58c2-ad54-3fd066398797` | 201-219 [crates/gwiki/src/ai/clients.rs:201-219] | Indexed function `segment_translation_prompt` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:201-219] |
| `parse_indexed_translation` | function | `fn parse_indexed_translation(text: &str, expected_len: usize) -> Result<Vec<String>, WikiError> {` | `parse_indexed_translation [function]` | `a1d3249f-d12a-50b3-975a-1463e5255128` | 221-254 [crates/gwiki/src/ai/clients.rs:221-254] | Indexed function `parse_indexed_translation` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:221-254] |
| `warn_translation_batch_mismatch` | function | `fn warn_translation_batch_mismatch(` | `warn_translation_batch_mismatch [function]` | `a87056a0-f300-52dd-840a-5252bd7026a9` | 256-270 [crates/gwiki/src/ai/clients.rs:256-270] | Indexed function `warn_translation_batch_mismatch` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:256-270] |
| `ProductionVisionClient` | class | `pub(crate) struct ProductionVisionClient {` | `ProductionVisionClient [class]` | `fa5ccca1-84be-582f-97ac-63261d366f2c` | 272-274 [crates/gwiki/src/ai/clients.rs:272-274] | Indexed class `ProductionVisionClient` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:272-274] |
| `ProductionVisionClient::new` | method | `pub(crate) fn new(context: AiContext) -> Self {` | `ProductionVisionClient::new [method]` | `511e9fdb-0fcb-5a5c-969a-a151532e83f4` | 277-279 [crates/gwiki/src/ai/clients.rs:277-279] | Indexed method `ProductionVisionClient::new` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:277-279] |
| `ProductionVisionClient::extract` | method | `fn extract(&self, request: &VisionRequest<'_>) -> Result<VisionExtraction, WikiError> {` | `ProductionVisionClient::extract [method]` | `4a316e9f-ba1f-5356-a604-cf9faae75936` | 283-301 [crates/gwiki/src/ai/clients.rs:283-301] | Indexed method `ProductionVisionClient::extract` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:283-301] |
| `route_unavailable` | function | `fn route_unavailable(capability: AiCapability, route: AiRouting) -> AiError {` | `route_unavailable [function]` | `fe53aed4-9119-555f-8930-5636f799bd8a` | 304-313 [crates/gwiki/src/ai/clients.rs:304-313] | Indexed function `route_unavailable` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:304-313] |
| `route_name` | function | `fn route_name(route: AiRouting) -> &'static str {` | `route_name [function]` | `7eb7621e-6e4f-5964-9d77-eaaa0191baec` | 315-322 [crates/gwiki/src/ai/clients.rs:315-322] | Indexed function `route_name` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:315-322] |
| `ai_error_to_wiki_error` | function | `fn ai_error_to_wiki_error(error: AiError) -> WikiError {` | `ai_error_to_wiki_error [function]` | `366340b0-5b92-53b0-ae6c-a7defe4ac2b8` | 324-329 [crates/gwiki/src/ai/clients.rs:324-329] | Indexed function `ai_error_to_wiki_error` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:324-329] |
| `transcription_output_from_core` | function | `fn transcription_output_from_core(result: CoreTranscriptionResult) -> TranscriptionOutput {` | `transcription_output_from_core [function]` | `d94e9112-3e98-5e4b-b1b8-ef53ea3ac1b1` | 331-357 [crates/gwiki/src/ai/clients.rs:331-357] | Indexed function `transcription_output_from_core` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:331-357] |
| `vision_extraction_from_core` | function | `fn vision_extraction_from_core(result: VisionResult) -> VisionExtraction {` | `vision_extraction_from_core [function]` | `04ed7217-5fc7-5f41-8824-978fa7b36b47` | 359-372 [crates/gwiki/src/ai/clients.rs:359-372] | Indexed function `vision_extraction_from_core` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:359-372] |
| `clients_consume_effective_off_and_direct_routes` | function | `fn clients_consume_effective_off_and_direct_routes() {` | `clients_consume_effective_off_and_direct_routes [function]` | `6c19c5e3-c505-5d59-ab6b-10a4137dc35e` | 384-439 [crates/gwiki/src/ai/clients.rs:384-439] | Indexed function `clients_consume_effective_off_and_direct_routes` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:384-439] |
| `indexed_translation_errors_name_bad_index_shape` | function | `fn indexed_translation_errors_name_bad_index_shape() {` | `indexed_translation_errors_name_bad_index_shape [function]` | `081a4819-1d9c-5e1e-bb89-832c80ec26c7` | 442-451 [crates/gwiki/src/ai/clients.rs:442-451] | Indexed function `indexed_translation_errors_name_bad_index_shape` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:442-451] |
| `test_context` | function | `fn test_context(binding: CapabilityBinding) -> AiContext {` | `test_context [function]` | `ddb4a9f1-ba30-59f9-a2aa-543760c7f3b9` | 453-469 [crates/gwiki/src/ai/clients.rs:453-469] | Indexed function `test_context` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:453-469] |
| `binding` | function | `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {` | `binding [function]` | `bb21c0d9-ac1e-568c-8bcb-726a905316ca` | 471-484 [crates/gwiki/src/ai/clients.rs:471-484] | Indexed function `binding` in `crates/gwiki/src/ai/clients.rs`. [crates/gwiki/src/ai/clients.rs:471-484] |
