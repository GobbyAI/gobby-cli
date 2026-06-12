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
  - 149-187
  - 189-223
  - 225-233
  - 235-237
  - 239-245
  - 247-263
  - 265-267
  - 269-271
  - 273-293
  - 295-304
  - 306-331
  - 333-350
  - 352-356
  - 358-360
  - 362-364
  - 366-402
  - 404-423
  - 437-488
  - 491-510
  - 513-530
  - 533-555
  - 558-579
  - 582-605
  - 608-638
  - 641-656
  - 659-694
  - 697-750
  - 753-770
  - 772-781
  - 783-786
  - 788-795
  - 797-799
  - 801-803
  - 805-814
  - 816-833
  - 835-848
  - 850-856
  - 858-881
  - 883-902
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/daemon.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Purpose

`crates/gcore/src/ai/daemon.rs` exposes 47 indexed API symbols.
[crates/gcore/src/ai/daemon.rs:19-24]
[crates/gcore/src/ai/daemon.rs:27-31]
[crates/gcore/src/ai/daemon.rs:34-41]
[crates/gcore/src/ai/daemon.rs:44-96]
[crates/gcore/src/ai/daemon.rs:98-136]

## API Symbols

- `DaemonTranscriptionOptions` (class) component `DaemonTranscriptionOptions [class]` (`fe2b6abe-325a-5b65-987c-5494d8de2245`) lines 19-24 [crates/gcore/src/ai/daemon.rs:19-24]
  - Signature: `pub struct DaemonTranscriptionOptions<'a> {`
  - Purpose: Indexed class `DaemonTranscriptionOptions` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:19-24]
- `DaemonEmbeddingResult` (class) component `DaemonEmbeddingResult [class]` (`37bfcc0e-6619-5f90-91f9-c3910c81e82d`) lines 27-31 [crates/gcore/src/ai/daemon.rs:27-31]
  - Signature: `pub struct DaemonEmbeddingResult {`
  - Purpose: Indexed class `DaemonEmbeddingResult` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:27-31]
- `default` (function) component `default [function]` (`9e9d7634-b2f2-5ee0-8608-cf9c74922d62`) lines 34-41 [crates/gcore/src/ai/daemon.rs:34-41]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed function `default` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:34-41]
- `transcribe_via_daemon` (function) component `transcribe_via_daemon [function]` (`e9f2ba09-f1c6-5a87-8884-c48c0e955a54`) lines 44-96 [crates/gcore/src/ai/daemon.rs:44-96]
  - Signature: `pub fn transcribe_via_daemon(`
  - Purpose: Indexed function `transcribe_via_daemon` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:44-96]
- `describe_image_via_daemon` (function) component `describe_image_via_daemon [function]` (`48017a1b-075c-5dbe-9269-323340b49c6d`) lines 98-136 [crates/gcore/src/ai/daemon.rs:98-136]
  - Signature: `pub fn describe_image_via_daemon(`
  - Purpose: Indexed function `describe_image_via_daemon` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:98-136]
- `generate_via_daemon` (function) component `generate_via_daemon [function]` (`3575e0cd-f05d-5d20-90d2-8e3d02cc9a40`) lines 138-144 [crates/gcore/src/ai/daemon.rs:138-144]
  - Signature: `pub fn generate_via_daemon(`
  - Purpose: Indexed function `generate_via_daemon` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:138-144]
- `generate_via_daemon_with_max_tokens` (function) component `generate_via_daemon_with_max_tokens [function]` (`fc924f08-7212-584c-994d-5ec9121f6793`) lines 149-187 [crates/gcore/src/ai/daemon.rs:149-187]
  - Signature: `pub fn generate_via_daemon_with_max_tokens(`
  - Purpose: Indexed function `generate_via_daemon_with_max_tokens` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:149-187]
- `embed_via_daemon` (function) component `embed_via_daemon [function]` (`603a96e1-c01d-512b-9e6c-ddfbfd10c60f`) lines 189-223 [crates/gcore/src/ai/daemon.rs:189-223]
  - Signature: `pub fn embed_via_daemon(`
  - Purpose: Indexed function `embed_via_daemon` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:189-223]
- `audio_capability` (function) component `audio_capability [function]` (`d51d0c9e-6a27-5522-a654-14444ab1c0e4`) lines 225-233 [crates/gcore/src/ai/daemon.rs:225-233]
  - Signature: `fn audio_capability(capability: AiCapability) -> Result<AiCapability, AiError> {`
  - Purpose: Indexed function `audio_capability` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:225-233]
- `daemon_client` (function) component `daemon_client [function]` (`1ac4b829-b376-5132-971e-b80c34d0b1a3`) lines 235-237 [crates/gcore/src/ai/daemon.rs:235-237]
  - Signature: `fn daemon_client() -> Result<Client, AiError> {`
  - Purpose: Indexed function `daemon_client` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:235-237]
- `daemon_url` (function) component `daemon_url [function]` (`8d162ca0-183b-5e09-b857-519683114dc3`) lines 239-245 [crates/gcore/src/ai/daemon.rs:239-245]
  - Signature: `fn daemon_url(path: &str) -> String {`
  - Purpose: Indexed function `daemon_url` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:239-245]
- `read_local_cli_token` (function) component `read_local_cli_token [function]` (`9097eb66-0a1d-5ddc-ba26-d478094936ea`) lines 247-263 [crates/gcore/src/ai/daemon.rs:247-263]
  - Signature: `fn read_local_cli_token() -> Result<String, AiError> {`
  - Purpose: Indexed function `read_local_cli_token` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:247-263]
- `gobby_home` (function) component `gobby_home [function]` (`11e2a651-32d0-5ad9-93ec-3405ccf9ff7b`) lines 265-267 [crates/gcore/src/ai/daemon.rs:265-267]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, AiError> {`
  - Purpose: Indexed function `gobby_home` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:265-267]
- `with_local_token` (function) component `with_local_token [function]` (`4071c551-a34b-594d-b9e9-85864097d0ea`) lines 269-271 [crates/gcore/src/ai/daemon.rs:269-271]
  - Signature: `fn with_local_token(request: RequestBuilder, token: &str) -> RequestBuilder {`
  - Purpose: Indexed function `with_local_token` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:269-271]
- `multipart_form_with_file` (function) component `multipart_form_with_file [function]` (`e76b63fb-1a4f-5e8b-aaf4-a35137efebde`) lines 273-293 [crates/gcore/src/ai/daemon.rs:273-293]
  - Signature: `fn multipart_form_with_file(`
  - Purpose: Indexed function `multipart_form_with_file` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:273-293]
- `add_optional_text` (function) component `add_optional_text [function]` (`140a3d79-8513-56bb-801d-abc6d2c3f055`) lines 295-304 [crates/gcore/src/ai/daemon.rs:295-304]
  - Signature: `fn add_optional_text(`
  - Purpose: Indexed function `add_optional_text` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:295-304]
- `text_request_body` (function) component `text_request_body [function]` (`562b2429-576a-52b5-bbe1-885d9457d3e7`) lines 306-331 [crates/gcore/src/ai/daemon.rs:306-331]
  - Signature: `fn text_request_body(`
  - Purpose: Indexed function `text_request_body` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:306-331]
- `embeddings_request_body` (function) component `embeddings_request_body [function]` (`5e23fec2-f487-5fd5-b3cd-66bf41d79dcd`) lines 333-350 [crates/gcore/src/ai/daemon.rs:333-350]
  - Signature: `fn embeddings_request_body(`
  - Purpose: Indexed function `embeddings_request_body` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:333-350]
- `insert_optional` (function) component `insert_optional [function]` (`d9ac39f5-a35a-5c32-9d43-18a2d6019fe5`) lines 352-356 [crates/gcore/src/ai/daemon.rs:352-356]
  - Signature: `fn insert_optional(body: &mut Map<String, Value>, name: &str, value: Option<&str>) {`
  - Purpose: Indexed function `insert_optional` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:352-356]
- `non_empty` (function) component `non_empty [function]` (`0c92d3d6-d4b8-5aba-bc76-1828a1193b9c`) lines 358-360 [crates/gcore/src/ai/daemon.rs:358-360]
  - Signature: `fn non_empty(value: Option<&str>) -> Option<&str> {`
  - Purpose: Indexed function `non_empty` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:358-360]
- `parse_daemon_transcription` (function) component `parse_daemon_transcription [function]` (`05808d65-c919-5b8c-9350-18f7947c00a3`) lines 362-364 [crates/gcore/src/ai/daemon.rs:362-364]
  - Signature: `fn parse_daemon_transcription(value: Value) -> Result<TranscriptionResult, AiError> {`
  - Purpose: Indexed function `parse_daemon_transcription` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:362-364]
- `parse_daemon_embeddings` (function) component `parse_daemon_embeddings [function]` (`1046d96e-a58d-5957-928b-7fa50a164102`) lines 366-402 [crates/gcore/src/ai/daemon.rs:366-402]
  - Signature: `fn parse_daemon_embeddings(`
  - Purpose: Indexed function `parse_daemon_embeddings` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:366-402]
- `parse_daemon_embedding` (function) component `parse_daemon_embedding [function]` (`d05d6301-bbec-50aa-94b7-4887e115e98d`) lines 404-423 [crates/gcore/src/ai/daemon.rs:404-423]
  - Signature: `fn parse_daemon_embedding(value: &Value, dim: usize) -> Result<Vec<f32>, AiError> {`
  - Purpose: Indexed function `parse_daemon_embedding` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:404-423]
- `forwards_provider_model_and_optional_project_id` (function) component `forwards_provider_model_and_optional_project_id [function]` (`3973bc4e-c301-53b9-a1d3-e94ea03e6732`) lines 437-488 [crates/gcore/src/ai/daemon.rs:437-488]
  - Signature: `fn forwards_provider_model_and_optional_project_id() {`
  - Purpose: Indexed function `forwards_provider_model_and_optional_project_id` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:437-488]
- `text_generation_defaults_to_feature_low_without_provider_model` (function) component `text_generation_defaults_to_feature_low_without_provider_model [function]` (`3b0bce9b-06c9-585d-8879-938b9f41c8ca`) lines 491-510 [crates/gcore/src/ai/daemon.rs:491-510]
  - Signature: `fn text_generation_defaults_to_feature_low_without_provider_model() {`
  - Purpose: Indexed function `text_generation_defaults_to_feature_low_without_provider_model` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:491-510]
- `configured_binding_profile_replaces_feature_low_default` (function) component `configured_binding_profile_replaces_feature_low_default [function]` (`3ff1eade-8add-5bd6-a401-5550c7d0001d`) lines 513-530 [crates/gcore/src/ai/daemon.rs:513-530]
  - Signature: `fn configured_binding_profile_replaces_feature_low_default() {`
  - Purpose: Indexed function `configured_binding_profile_replaces_feature_low_default` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:513-530]
- `per_call_profile_overrides_configured_binding_profile` (function) component `per_call_profile_overrides_configured_binding_profile [function]` (`45e9aa3d-6fa9-5867-94d0-978b1012fd9a`) lines 533-555 [crates/gcore/src/ai/daemon.rs:533-555]
  - Signature: `fn per_call_profile_overrides_configured_binding_profile() {`
  - Purpose: Indexed function `per_call_profile_overrides_configured_binding_profile` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:533-555]
- `explicit_provider_model_suppresses_profile_override` (function) component `explicit_provider_model_suppresses_profile_override [function]` (`09f6bb39-7d40-5fc9-b75c-86642c544ea9`) lines 558-579 [crates/gcore/src/ai/daemon.rs:558-579]
  - Signature: `fn explicit_provider_model_suppresses_profile_override() {`
  - Purpose: Indexed function `explicit_provider_model_suppresses_profile_override` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:558-579]
- `embeddings_post_preserves_batch_and_local_token` (function) component `embeddings_post_preserves_batch_and_local_token [function]` (`d803c299-8c52-5095-9b32-ffb9a6d68e03`) lines 582-605 [crates/gcore/src/ai/daemon.rs:582-605]
  - Signature: `fn embeddings_post_preserves_batch_and_local_token() {`
  - Purpose: Indexed function `embeddings_post_preserves_batch_and_local_token` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:582-605]
- `embedding_response_validates_count_and_dimension` (function) component `embedding_response_validates_count_and_dimension [function]` (`5f3be6a0-edf9-5794-86b9-b0c7af28ac0f`) lines 608-638 [crates/gcore/src/ai/daemon.rs:608-638]
  - Signature: `fn embedding_response_validates_count_and_dimension() {`
  - Purpose: Indexed function `embedding_response_validates_count_and_dimension` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:608-638]
- `empty_embedding_batch_parses_daemon_model_and_dim` (function) component `empty_embedding_batch_parses_daemon_model_and_dim [function]` (`105fdbc7-4236-5718-a78a-9c5d67ff92d1`) lines 641-656 [crates/gcore/src/ai/daemon.rs:641-656]
  - Signature: `fn empty_embedding_batch_parses_daemon_model_and_dim() {`
  - Purpose: Indexed function `empty_embedding_batch_parses_daemon_model_and_dim` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:641-656]
- `sends_local_token_and_multipart` (function) component `sends_local_token_and_multipart [function]` (`6298e2ca-d1a8-5124-89f1-1f8e6e800843`) lines 659-694 [crates/gcore/src/ai/daemon.rs:659-694]
  - Signature: `fn sends_local_token_and_multipart() {`
  - Purpose: Indexed function `sends_local_token_and_multipart` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:659-694]
- `voice_multipart_carries_capability_fields` (function) component `voice_multipart_carries_capability_fields [function]` (`77571a21-d63c-5ae2-90ce-73834889e1b7`) lines 697-750 [crates/gcore/src/ai/daemon.rs:697-750]
  - Signature: `fn voice_multipart_carries_capability_fields() {`
  - Purpose: Indexed function `voice_multipart_carries_capability_fields` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:697-750]
- `probe_and_transport_resolve_same_custom_port_url_under_gobby_home` (function) component `probe_and_transport_resolve_same_custom_port_url_under_gobby_home [function]` (`842bfa7f-9938-5650-8f08-119c1c05cc4f`) lines 753-770 [crates/gcore/src/ai/daemon.rs:753-770]
  - Signature: `fn probe_and_transport_resolve_same_custom_port_url_under_gobby_home() {`
  - Purpose: Indexed function `probe_and_transport_resolve_same_custom_port_url_under_gobby_home` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:753-770]
- `spawn_server` (function) component `spawn_server [function]` (`2c4f50e8-a084-5f3a-96da-34b5e3586b3c`) lines 772-781 [crates/gcore/src/ai/daemon.rs:772-781]
  - Signature: `fn spawn_server(response: &'static str) -> (u16, RequestHandle) {`
  - Purpose: Indexed function `spawn_server` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:772-781]
- `request_body_json` (function) component `request_body_json [function]` (`4dd15874-95ea-5090-a1af-a5a7feee5644`) lines 783-786 [crates/gcore/src/ai/daemon.rs:783-786]
  - Signature: `fn request_body_json(request: &str) -> serde_json::Value {`
  - Purpose: Indexed function `request_body_json` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:783-786]
- `has_header` (function) component `has_header [function]` (`4b4f4ddc-1587-5a42-8a56-671bcb939a7b`) lines 788-795 [crates/gcore/src/ai/daemon.rs:788-795]
  - Signature: `fn has_header(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Indexed function `has_header` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:788-795]
- `multipart_has_field` (function) component `multipart_has_field [function]` (`2d67bef1-b486-53e0-9cf0-18b28208f637`) lines 797-799 [crates/gcore/src/ai/daemon.rs:797-799]
  - Signature: `fn multipart_has_field(request: &str, name: &str, value: &str) -> bool {`
  - Purpose: Indexed function `multipart_has_field` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:797-799]
- `temp_home` (function) component `temp_home [function]` (`f475c60b-885a-5c8f-b098-6857aacba69b`) lines 801-803 [crates/gcore/src/ai/daemon.rs:801-803]
  - Signature: `fn temp_home() -> tempfile::TempDir {`
  - Purpose: Indexed function `temp_home` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:801-803]
- `write_daemon_files` (function) component `write_daemon_files [function]` (`639814da-47a4-528f-9763-5d60e7bbfae9`) lines 805-814 [crates/gcore/src/ai/daemon.rs:805-814]
  - Signature: `fn write_daemon_files(home: &Path, port: u16, token: &str) {`
  - Purpose: Indexed function `write_daemon_files` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:805-814]
- `test_context` (function) component `test_context [function]` (`51653529-1ebf-5764-8485-705de7077402`) lines 816-833 [crates/gcore/src/ai/daemon.rs:816-833]
  - Signature: `fn test_context(project_id: Option<&str>) -> AiContext {`
  - Purpose: Indexed function `test_context` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:816-833]
- `binding` (function) component `binding [function]` (`913108dd-e5d5-52de-abcf-11b802236def`) lines 835-848 [crates/gcore/src/ai/daemon.rs:835-848]
  - Signature: `fn binding() -> CapabilityBinding {`
  - Purpose: Indexed function `binding` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:835-848]
- `EnvGuard` (class) component `EnvGuard [class]` (`c1f000a1-bfe4-5002-b75d-142552507f1c`) lines 850-856 [crates/gcore/src/ai/daemon.rs:850-856]
  - Signature: `struct EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:850-856]
- `EnvGuard` (class) component `EnvGuard [class]` (`aa6cfc87-ccd4-5874-b010-b5c4a3839636`) lines 858-881 [crates/gcore/src/ai/daemon.rs:858-881]
  - Signature: `impl EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:858-881]
- `EnvGuard.set_home` (method) component `EnvGuard.set_home [method]` (`65d08b11-ecae-52d9-8f65-b0f7664735fb`) lines 859-880 [crates/gcore/src/ai/daemon.rs:859-880]
  - Signature: `fn set_home(home: &Path) -> Self {`
  - Purpose: Indexed method `EnvGuard.set_home` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:859-880]
- `EnvGuard` (class) component `EnvGuard [class]` (`3c19b4cf-1b6a-5027-b81d-0a9ff40b575c`) lines 883-902 [crates/gcore/src/ai/daemon.rs:883-902]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: Indexed class `EnvGuard` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:883-902]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`59aa653c-0579-5480-a8cc-3c30fed9b3d2`) lines 884-901 [crates/gcore/src/ai/daemon.rs:884-901]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `EnvGuard.drop` in `crates/gcore/src/ai/daemon.rs`. [crates/gcore/src/ai/daemon.rs:884-901]

