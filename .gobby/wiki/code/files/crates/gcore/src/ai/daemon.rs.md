---
title: crates/gcore/src/ai/daemon.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/daemon.rs
  ranges:
  - 19-24
  - 27-31
  - 34-41
  - 44-96
  - 98-136
  - 138-144
  - 146-182
  - 184-218
  - 220-228
  - 230-232
  - 234-241
  - 243-259
  - 261-263
  - 265-267
  - 269-289
  - 291-300
  - 302-328
  - 330-347
  - 349-353
  - 355-357
  - 359-361
  - 363-399
  - 401-420
  - 434-476
  - 479-498
  - 501-524
  - 527-557
  - 560-575
  - 578-613
  - 616-669
  - 671-680
  - 682-685
  - 687-694
  - 696-698
  - 700-702
  - 704-713
  - 715-732
  - 734-746
  - 748-752
  - 754-772
  - 755-771
  - 774-790
  - 775-789
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

`crates/gcore/src/ai/daemon.rs` exposes 43 indexed API symbols.
[crates/gcore/src/ai/daemon.rs:19-24]
[crates/gcore/src/ai/daemon.rs:27-31]
[crates/gcore/src/ai/daemon.rs:34-41]
[crates/gcore/src/ai/daemon.rs:44-96]
[crates/gcore/src/ai/daemon.rs:98-136]
[crates/gcore/src/ai/daemon.rs:138-144]
[crates/gcore/src/ai/daemon.rs:146-182]
[crates/gcore/src/ai/daemon.rs:184-218]
[crates/gcore/src/ai/daemon.rs:220-228]
[crates/gcore/src/ai/daemon.rs:230-232]
[crates/gcore/src/ai/daemon.rs:234-241]
[crates/gcore/src/ai/daemon.rs:243-259]
[crates/gcore/src/ai/daemon.rs:261-263]
[crates/gcore/src/ai/daemon.rs:265-267]
[crates/gcore/src/ai/daemon.rs:269-289]
[crates/gcore/src/ai/daemon.rs:291-300]
[crates/gcore/src/ai/daemon.rs:302-328]
[crates/gcore/src/ai/daemon.rs:330-347]
[crates/gcore/src/ai/daemon.rs:349-353]
[crates/gcore/src/ai/daemon.rs:355-357]
[crates/gcore/src/ai/daemon.rs:359-361]
[crates/gcore/src/ai/daemon.rs:363-399]
[crates/gcore/src/ai/daemon.rs:401-420]
[crates/gcore/src/ai/daemon.rs:434-476]
[crates/gcore/src/ai/daemon.rs:479-498]
[crates/gcore/src/ai/daemon.rs:501-524]
[crates/gcore/src/ai/daemon.rs:527-557]
[crates/gcore/src/ai/daemon.rs:560-575]
[crates/gcore/src/ai/daemon.rs:578-613]
[crates/gcore/src/ai/daemon.rs:616-669]
[crates/gcore/src/ai/daemon.rs:671-680]
[crates/gcore/src/ai/daemon.rs:682-685]
[crates/gcore/src/ai/daemon.rs:687-694]
[crates/gcore/src/ai/daemon.rs:696-698]
[crates/gcore/src/ai/daemon.rs:700-702]
[crates/gcore/src/ai/daemon.rs:704-713]
[crates/gcore/src/ai/daemon.rs:715-732]
[crates/gcore/src/ai/daemon.rs:734-746]
[crates/gcore/src/ai/daemon.rs:748-752]
[crates/gcore/src/ai/daemon.rs:754-772]
[crates/gcore/src/ai/daemon.rs:755-771]
[crates/gcore/src/ai/daemon.rs:774-790]
[crates/gcore/src/ai/daemon.rs:775-789]

## API Symbols

- `DaemonTranscriptionOptions` (class) component `DaemonTranscriptionOptions [class]` (`fe2b6abe-325a-5b65-987c-5494d8de2245`) lines 19-24 [crates/gcore/src/ai/daemon.rs:19-24]
  - Signature: `pub struct DaemonTranscriptionOptions<'a> {`
  - Purpose: A generic configuration struct that encapsulates a required `AiCapability` and optional borrowed string parameters for language, target language, and prompt configuration in daemon transcription operations. [crates/gcore/src/ai/daemon.rs:19-24]
- `DaemonEmbeddingResult` (class) component `DaemonEmbeddingResult [class]` (`37bfcc0e-6619-5f90-91f9-c3910c81e82d`) lines 27-31 [crates/gcore/src/ai/daemon.rs:27-31]
  - Signature: `pub struct DaemonEmbeddingResult {`
  - Purpose: `DaemonEmbeddingResult` is a struct that encapsulates the output of an embedding operation, containing a collection of floating-point vectors, the model identifier used to generate them, and the vector dimensionality. [crates/gcore/src/ai/daemon.rs:27-31]
- `default` (function) component `default [function]` (`9e9d7634-b2f2-5ee0-8608-cf9c74922d62`) lines 34-41 [crates/gcore/src/ai/daemon.rs:34-41]
  - Signature: `fn default() -> Self {`
  - Purpose: Creates a default instance with `AudioTranscribe` capability and `None` for all optional fields (language, target_lang, prompt). [crates/gcore/src/ai/daemon.rs:34-41]
- `transcribe_via_daemon` (function) component `transcribe_via_daemon [function]` (`e9f2ba09-f1c6-5a87-8884-c48c0e955a54`) lines 44-96 [crates/gcore/src/ai/daemon.rs:44-96]
  - Signature: `pub fn transcribe_via_daemon(`
  - Purpose: # Summary

Sends audio bytes with optional transcription parameters to an authenticated daemon service via multipart HTTP POST request with exponential backoff retry, returning the parsed transcription result. [crates/gcore/src/ai/daemon.rs:44-96]
- `describe_image_via_daemon` (function) component `describe_image_via_daemon [function]` (`3994d8af-6946-5c94-9d15-b13a669b4205`) lines 98-136 [crates/gcore/src/ai/daemon.rs:98-136]
  - Signature: `pub fn describe_image_via_daemon(`
  - Purpose: # Function Summary

Submits image data to a remote daemon service via authenticated HTTP multipart POST with exponential backoff retry logic to extract vision-based image analysis. [crates/gcore/src/ai/daemon.rs:98-136]
- `generate_via_daemon` (function) component `generate_via_daemon [function]` (`79897c3c-a54c-5605-9155-ac311297092d`) lines 138-144 [crates/gcore/src/ai/daemon.rs:138-144]
  - Signature: `pub fn generate_via_daemon(`
  - Purpose: Invokes daemon-based text generation with the provided AI context, prompt, and optional system message, with no maximum token limit. [crates/gcore/src/ai/daemon.rs:138-144]
- `generate_via_daemon_with_max_tokens` (function) component `generate_via_daemon_with_max_tokens [function]` (`3f45b81c-0951-5f57-8d45-9e4a1276ddf2`) lines 146-182 [crates/gcore/src/ai/daemon.rs:146-182]
  - Signature: `pub fn generate_via_daemon_with_max_tokens(`
  - Purpose: Sends an authenticated text generation request to a local daemon endpoint with configurable max_tokens, implementing rate limiting and exponential backoff retry logic. [crates/gcore/src/ai/daemon.rs:146-182]
- `embed_via_daemon` (function) component `embed_via_daemon [function]` (`3526895d-859c-5328-b6ef-569fef946184`) lines 184-218 [crates/gcore/src/ai/daemon.rs:184-218]
  - Signature: `pub fn embed_via_daemon(`
  - Purpose: Makes a rate-limited, authenticated HTTP request to a local embedding daemon with exponential backoff retry logic to generate embeddings for the provided strings. [crates/gcore/src/ai/daemon.rs:184-218]
- `audio_capability` (function) component `audio_capability [function]` (`c3eba19e-42d0-5597-8d4c-644cb58cae9b`) lines 220-228 [crates/gcore/src/ai/daemon.rs:220-228]
  - Signature: `fn audio_capability(capability: AiCapability) -> Result<AiCapability, AiError> {`
  - Purpose: Validates that the provided `AiCapability` is either `AudioTranscribe` or `AudioTranslate`, returning it on success or an error indicating the capability is unavailable otherwise. [crates/gcore/src/ai/daemon.rs:220-228]
- `daemon_client` (function) component `daemon_client [function]` (`3a24eb1f-2505-5cff-ae38-1a88866babce`) lines 230-232 [crates/gcore/src/ai/daemon.rs:230-232]
  - Signature: `fn daemon_client() -> Result<Client, AiError> {`
  - Purpose: Constructs a `Client` using the builder pattern and converts any build errors to `AiError`. [crates/gcore/src/ai/daemon.rs:230-232]
- `daemon_url` (function) component `daemon_url [function]` (`bc0aa047-7c5d-5e9a-9938-acadbfa97052`) lines 234-241 [crates/gcore/src/ai/daemon.rs:234-241]
  - Signature: `fn daemon_url(path: &str) -> Result<String, AiError> {`
  - Purpose: Constructs a daemon URL by appending the provided path to the base daemon URL loaded from a bootstrap.yaml configuration file in the gobby home directory, with trailing slashes trimmed. [crates/gcore/src/ai/daemon.rs:234-241]
- `read_local_cli_token` (function) component `read_local_cli_token [function]` (`f6f0dbb6-a46b-5409-b0af-80fbc9103cec`) lines 243-259 [crates/gcore/src/ai/daemon.rs:243-259]
  - Signature: `fn read_local_cli_token() -> Result<String, AiError> {`
  - Purpose: Reads and validates a non-empty local CLI token from a file in the gobby home directory, returning it trimmed or an `AiError` if the file is missing or contains only whitespace. [crates/gcore/src/ai/daemon.rs:243-259]
- `gobby_home` (function) component `gobby_home [function]` (`328bc6eb-e69e-5474-9f95-7138431d1665`) lines 261-263 [crates/gcore/src/ai/daemon.rs:261-263]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, AiError> {`
  - Purpose: This function wraps the crate's `gobby_home()` function and converts any error into an `AiError::not_configured` variant, returning either a `PathBuf` or an AI configuration error. [crates/gcore/src/ai/daemon.rs:261-263]
- `with_local_token` (function) component `with_local_token [function]` (`6c29c9c5-2279-5fc1-8fb0-e2500c002df1`) lines 265-267 [crates/gcore/src/ai/daemon.rs:265-267]
  - Signature: `fn with_local_token(request: RequestBuilder, token: &str) -> RequestBuilder {`
  - Purpose: Adds a local token authentication header to an HTTP request builder and returns the modified builder. [crates/gcore/src/ai/daemon.rs:265-267]
- `multipart_form_with_file` (function) component `multipart_form_with_file [function]` (`6080a26b-883f-532b-9d65-b65b3be9d218`) lines 269-289 [crates/gcore/src/ai/daemon.rs:269-289]
  - Signature: `fn multipart_form_with_file(`
  - Purpose: Constructs a multipart form with a single file part from bytes, validating the payload size and MIME type. [crates/gcore/src/ai/daemon.rs:269-289]
- `add_optional_text` (function) component `add_optional_text [function]` (`780a20b2-6f5b-5337-b7bf-72c071631734`) lines 291-300 [crates/gcore/src/ai/daemon.rs:291-300]
  - Signature: `fn add_optional_text(`
  - Purpose: Conditionally appends a text field to a multipart form only if the optional value is non-empty, otherwise returns the form unmodified. [crates/gcore/src/ai/daemon.rs:291-300]
- `text_request_body` (function) component `text_request_body [function]` (`8a588c16-d832-57de-9691-5816e93fae72`) lines 302-328 [crates/gcore/src/ai/daemon.rs:302-328]
  - Signature: `fn text_request_body(`
  - Purpose: Constructs and returns a JSON request body for text generation by assembling a required prompt with optional system message, provider, model, project ID, and max tokens parameters, applying a default profile when both provider and model are absent. [crates/gcore/src/ai/daemon.rs:302-328]
- `embeddings_request_body` (function) component `embeddings_request_body [function]` (`b65bdf95-a9ed-5b6a-a33b-4d99f9e4278f`) lines 330-347 [crates/gcore/src/ai/daemon.rs:330-347]
  - Signature: `fn embeddings_request_body(`
  - Purpose: Constructs a JSON object Value containing the input strings array, is_query boolean flag, and optional project_id, provider, and model fields for an embeddings API request. [crates/gcore/src/ai/daemon.rs:330-347]
- `insert_optional` (function) component `insert_optional [function]` (`a19f020c-d220-54da-99f9-afeeb54c1342`) lines 349-353 [crates/gcore/src/ai/daemon.rs:349-353]
  - Signature: `fn insert_optional(body: &mut Map<String, Value>, name: &str, value: Option<&str>) {`
  - Purpose: Inserts a non-empty optional string as a JSON value into a map under the given key name, if the value is non-empty. [crates/gcore/src/ai/daemon.rs:349-353]
- `non_empty` (function) component `non_empty [function]` (`ad792195-1f0c-5559-9ebf-c769b243ae60`) lines 355-357 [crates/gcore/src/ai/daemon.rs:355-357]
  - Signature: `fn non_empty(value: Option<&str>) -> Option<&str> {`
  - Purpose: Trims whitespace from an optional string reference and returns `None` if the trimmed result is empty. [crates/gcore/src/ai/daemon.rs:355-357]
- `parse_daemon_transcription` (function) component `parse_daemon_transcription [function]` (`bafc93db-852a-587b-b31f-117952db8ccb`) lines 359-361 [crates/gcore/src/ai/daemon.rs:359-361]
  - Signature: `fn parse_daemon_transcription(value: Value) -> Result<TranscriptionResult, AiError> {`
  - Purpose: Indexed function `parse_daemon_transcription` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:359-361]
- `parse_daemon_embeddings` (function) component `parse_daemon_embeddings [function]` (`4aafb767-2df1-5255-b317-edad37548cfa`) lines 363-399 [crates/gcore/src/ai/daemon.rs:363-399]
  - Signature: `fn parse_daemon_embeddings(`
  - Purpose: Indexed function `parse_daemon_embeddings` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:363-399]
- `parse_daemon_embedding` (function) component `parse_daemon_embedding [function]` (`1362a5e4-16f5-5b00-a5a9-fd49ec6a33ad`) lines 401-420 [crates/gcore/src/ai/daemon.rs:401-420]
  - Signature: `fn parse_daemon_embedding(value: &Value, dim: usize) -> Result<Vec<f32>, AiError> {`
  - Purpose: Indexed function `parse_daemon_embedding` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:401-420]
- `forwards_provider_model_and_optional_project_id` (function) component `forwards_provider_model_and_optional_project_id [function]` (`515fde76-98f9-5ccc-8ded-8fc760dc28a7`) lines 434-476 [crates/gcore/src/ai/daemon.rs:434-476]
  - Signature: `fn forwards_provider_model_and_optional_project_id() {`
  - Purpose: Indexed function `forwards_provider_model_and_optional_project_id` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:434-476]
- `text_generation_defaults_to_feature_low_without_provider_model` (function) component `text_generation_defaults_to_feature_low_without_provider_model [function]` (`752be597-f39c-5187-9000-d58905b8999d`) lines 479-498 [crates/gcore/src/ai/daemon.rs:479-498]
  - Signature: `fn text_generation_defaults_to_feature_low_without_provider_model() {`
  - Purpose: Indexed function `text_generation_defaults_to_feature_low_without_provider_model` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:479-498]
- `embeddings_post_preserves_batch_and_local_token` (function) component `embeddings_post_preserves_batch_and_local_token [function]` (`82d933c1-771d-540c-bed3-6bcc72f65285`) lines 501-524 [crates/gcore/src/ai/daemon.rs:501-524]
  - Signature: `fn embeddings_post_preserves_batch_and_local_token() {`
  - Purpose: Indexed function `embeddings_post_preserves_batch_and_local_token` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:501-524]
- `embedding_response_validates_count_and_dimension` (function) component `embedding_response_validates_count_and_dimension [function]` (`4570471a-1365-545e-8338-f96d03f70cdb`) lines 527-557 [crates/gcore/src/ai/daemon.rs:527-557]
  - Signature: `fn embedding_response_validates_count_and_dimension() {`
  - Purpose: Indexed function `embedding_response_validates_count_and_dimension` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:527-557]
- `empty_embedding_batch_parses_daemon_model_and_dim` (function) component `empty_embedding_batch_parses_daemon_model_and_dim [function]` (`e845b126-23d0-5180-9f73-7582127824b8`) lines 560-575 [crates/gcore/src/ai/daemon.rs:560-575]
  - Signature: `fn empty_embedding_batch_parses_daemon_model_and_dim() {`
  - Purpose: Indexed function `empty_embedding_batch_parses_daemon_model_and_dim` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:560-575]
- `sends_local_token_and_multipart` (function) component `sends_local_token_and_multipart [function]` (`519ac86b-b526-51df-b44e-13aa7ffc3a00`) lines 578-613 [crates/gcore/src/ai/daemon.rs:578-613]
  - Signature: `fn sends_local_token_and_multipart() {`
  - Purpose: Indexed function `sends_local_token_and_multipart` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:578-613]
- `voice_multipart_carries_capability_fields` (function) component `voice_multipart_carries_capability_fields [function]` (`54747dea-6c1f-584c-9b75-989999d0464f`) lines 616-669 [crates/gcore/src/ai/daemon.rs:616-669]
  - Signature: `fn voice_multipart_carries_capability_fields() {`
  - Purpose: Indexed function `voice_multipart_carries_capability_fields` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:616-669]
- `spawn_server` (function) component `spawn_server [function]` (`991056ae-0645-5186-8531-889917f3822b`) lines 671-680 [crates/gcore/src/ai/daemon.rs:671-680]
  - Signature: `fn spawn_server(response: &'static str) -> (u16, RequestHandle) {`
  - Purpose: Indexed function `spawn_server` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:671-680]
- `request_body_json` (function) component `request_body_json [function]` (`8a44f93d-9168-534b-81ef-1b7e36a71c0e`) lines 682-685 [crates/gcore/src/ai/daemon.rs:682-685]
  - Signature: `fn request_body_json(request: &str) -> serde_json::Value {`
  - Purpose: Indexed function `request_body_json` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:682-685]
- `has_header` (function) component `has_header [function]` (`0951ee8f-98e4-54fa-8548-9cf1ac9d5618`) lines 687-694 [crates/gcore/src/ai/daemon.rs:687-694]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Indexed function `has_header` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:687-694]
- `multipart_has_field` (function) component `multipart_has_field [function]` (`809125d7-a003-5136-a8e7-202b8df30bc6`) lines 696-698 [crates/gcore/src/ai/daemon.rs:696-698]
  - Signature: `fn multipart_has_field(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Indexed function `multipart_has_field` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:696-698]
- `temp_home` (function) component `temp_home [function]` (`0930b312-5e74-5f6b-8222-0e1c06508a09`) lines 700-702 [crates/gcore/src/ai/daemon.rs:700-702]
  - Signature: `fn temp_home() -> tempfile::TempDir {`
  - Purpose: Indexed function `temp_home` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:700-702]
- `write_daemon_files` (function) component `write_daemon_files [function]` (`06b7e826-cd57-5666-b3b1-d0e1a4446c66`) lines 704-713 [crates/gcore/src/ai/daemon.rs:704-713]
  - Signature: `fn write_daemon_files(home: &Path, port: u16, token: &str) {`
  - Purpose: Indexed function `write_daemon_files` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:704-713]
- `test_context` (function) component `test_context [function]` (`a4682bde-8ea5-5d2a-992a-ac1e753ef63a`) lines 715-732 [crates/gcore/src/ai/daemon.rs:715-732]
  - Signature: `fn test_context(project_id: Option<&str>) -> AiContext {`
  - Purpose: Indexed function `test_context` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:715-732]
- `binding` (function) component `binding [function]` (`09f2f431-b6fb-5f13-937a-6c4bd6124f01`) lines 734-746 [crates/gcore/src/ai/daemon.rs:734-746]
  - Signature: `fn binding() -> CapabilityBinding {`
  - Purpose: Indexed function `binding` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:734-746]
- `EnvGuard` (class) component `EnvGuard [class]` (`ef133a3a-d68c-5aa0-a1e0-12fbd5e81ab2`) lines 748-752 [crates/gcore/src/ai/daemon.rs:748-752]
  - Signature: `struct EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:748-752]
- `EnvGuard` (class) component `EnvGuard [class]` (`a09ba8aa-052f-579a-8e41-720d9e7dfb84`) lines 754-772 [crates/gcore/src/ai/daemon.rs:754-772]
  - Signature: `impl EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:754-772]
- `EnvGuard.set_home` (method) component `EnvGuard.set_home [method]` (`2f2c7d00-f02d-54c9-81ee-055a895b99f8`) lines 755-771 [crates/gcore/src/ai/daemon.rs:755-771]
  - Signature: `fn set_home(home: &Path) -> Self {`
  - Purpose: Indexed method `EnvGuard.set_home` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:755-771]
- `EnvGuard` (class) component `EnvGuard [class]` (`43309968-dd25-5d9a-b0dc-c2513386d1a7`) lines 774-790 [crates/gcore/src/ai/daemon.rs:774-790]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:774-790]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`7201fe37-20de-54a7-b273-e5bb33b032c2`) lines 775-789 [crates/gcore/src/ai/daemon.rs:775-789]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `EnvGuard.drop` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:775-789]

