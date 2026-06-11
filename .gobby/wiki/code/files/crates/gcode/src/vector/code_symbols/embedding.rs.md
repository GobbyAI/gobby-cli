---
title: crates/gcode/src/vector/code_symbols/embedding.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/embedding.rs
  ranges:
  - 21-23
  - 26-29
  - 31-35
  - 32-34
  - 37-41
  - 38-40
  - 44-47
  - 49-121
  - 50-64
  - 66-72
  - 74-101
  - 103-120
  - 123-126
  - 128-140
  - 142-145
  - 147-179
  - 181-203
  - 205-223
  - 225-228
  - 230-281
  - 283-306
  - 308-338
  - 340-361
  - 363-378
  - 380-411
  - 422-424
  - 426-432
  - 427-431
  - 434-445
  - 435-437
  - 439-444
  - 448-482
  - 485-507
  - 510-533
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/embedding.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

`crates/gcode/src/vector/code_symbols/embedding.rs` exposes 34 indexed API symbols.
[crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
[crates/gcode/src/vector/code_symbols/embedding.rs:26-29]
[crates/gcode/src/vector/code_symbols/embedding.rs:31-35]
[crates/gcode/src/vector/code_symbols/embedding.rs:32-34]
[crates/gcode/src/vector/code_symbols/embedding.rs:37-41]

## API Symbols

- `dimension_probe_text` (function) component `dimension_probe_text [function]` (`589ac3d5-8bb7-5601-b39d-acce0a0e012c`) lines 21-23 [crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
  - Signature: `pub(super) fn dimension_probe_text() -> &'static str {`
  - Purpose: Indexed function `dimension_probe_text` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:21-23]
- `EmbeddingSource` (type) component `EmbeddingSource [type]` (`8bc363cb-2547-5104-9236-3db4ab472ad8`) lines 26-29 [crates/gcode/src/vector/code_symbols/embedding.rs:26-29]
  - Signature: `pub enum EmbeddingSource {`
  - Purpose: Indexed type `EmbeddingSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:26-29]
- `EmbeddingSource` (class) component `EmbeddingSource [class]` (`3f69da9d-b9f6-5e38-9e7f-ced9cb1cda88`) lines 31-35 [crates/gcode/src/vector/code_symbols/embedding.rs:31-35]
  - Signature: `impl From<EmbeddingConfig> for EmbeddingSource {`
  - Purpose: Indexed class `EmbeddingSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:31-35]
- `EmbeddingSource.from` (method) component `EmbeddingSource.from [method]` (`5dd53c6b-6052-5f4f-82f7-01142071d334`) lines 32-34 [crates/gcode/src/vector/code_symbols/embedding.rs:32-34]
  - Signature: `fn from(config: EmbeddingConfig) -> Self {`
  - Purpose: Indexed method `EmbeddingSource.from` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:32-34]
- `EmbeddingSource` (class) component `EmbeddingSource [class]` (`f65130d3-6ee2-531a-8aac-de2fcd9075c2`) lines 37-41 [crates/gcode/src/vector/code_symbols/embedding.rs:37-41]
  - Signature: `impl From<AiContext> for EmbeddingSource {`
  - Purpose: Indexed class `EmbeddingSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:37-41]
- `EmbeddingSource.from` (method) component `EmbeddingSource.from [method]` (`2f34c2e2-2428-5741-8827-efc049c61799`) lines 38-40 [crates/gcode/src/vector/code_symbols/embedding.rs:38-40]
  - Signature: `fn from(context: AiContext) -> Self {`
  - Purpose: Indexed method `EmbeddingSource.from` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:38-40]
- `EmbeddingBackend` (class) component `EmbeddingBackend [class]` (`f1753204-5a79-5557-a3d3-609c8c924acd`) lines 44-47 [crates/gcode/src/vector/code_symbols/embedding.rs:44-47]
  - Signature: `pub struct EmbeddingBackend {`
  - Purpose: Indexed class `EmbeddingBackend` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:44-47]
- `EmbeddingBackend` (class) component `EmbeddingBackend [class]` (`6bee5b5f-5a52-5685-84c3-07ed7409d707`) lines 49-121 [crates/gcode/src/vector/code_symbols/embedding.rs:49-121]
  - Signature: `impl EmbeddingBackend {`
  - Purpose: Indexed class `EmbeddingBackend` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:49-121]
- `EmbeddingBackend.new` (method) component `EmbeddingBackend.new [method]` (`62a029ed-1334-5022-a439-adf81275c81b`) lines 50-64 [crates/gcode/src/vector/code_symbols/embedding.rs:50-64]
  - Signature: `pub fn new(source: EmbeddingSource) -> Result<Self, VectorLifecycleError> {`
  - Purpose: Indexed method `EmbeddingBackend.new` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:50-64]
- `EmbeddingBackend.embed_text` (method) component `EmbeddingBackend.embed_text [method]` (`e15ff7dd-f742-55fd-b1d6-d6f50a88546c`) lines 66-72 [crates/gcode/src/vector/code_symbols/embedding.rs:66-72]
  - Signature: `pub fn embed_text(&self, text: &str) -> Result<Vec<f32>, VectorLifecycleError> {`
  - Purpose: Indexed method `EmbeddingBackend.embed_text` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:66-72]
- `EmbeddingBackend.embed_query` (method) component `EmbeddingBackend.embed_query [method]` (`d53327a1-d622-5108-b73f-0c32f2cb9941`) lines 74-101 [crates/gcode/src/vector/code_symbols/embedding.rs:74-101]
  - Signature: `pub fn embed_query(&self, text: &str) -> Result<Vec<f32>, VectorLifecycleError> {`
  - Purpose: Indexed method `EmbeddingBackend.embed_query` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:74-101]
- `EmbeddingBackend.embed_text_batch` (method) component `EmbeddingBackend.embed_text_batch [method]` (`eaa17429-a1aa-56db-af8f-4638b84af956`) lines 103-120 [crates/gcode/src/vector/code_symbols/embedding.rs:103-120]
  - Signature: `pub fn embed_text_batch(`
  - Purpose: Indexed method `EmbeddingBackend.embed_text_batch` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:103-120]
- `embedding_source_from_context` (function) component `embedding_source_from_context [function]` (`08460f1b-a2ce-5726-9d7f-5b7157cdfc72`) lines 123-126 [crates/gcode/src/vector/code_symbols/embedding.rs:123-126]
  - Signature: `pub fn embedding_source_from_context(ctx: &Context) -> Option<EmbeddingSource> {`
  - Purpose: Indexed function `embedding_source_from_context` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:123-126]
- `embedding_source_from_resolved_ai_context` (function) component `embedding_source_from_resolved_ai_context [function]` (`426955a5-2426-59da-8fa0-b434bd81198b`) lines 128-140 [crates/gcode/src/vector/code_symbols/embedding.rs:128-140]
  - Signature: `fn embedding_source_from_resolved_ai_context(`
  - Purpose: Indexed function `embedding_source_from_resolved_ai_context` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:128-140]
- `ResolvedEmbeddingAiContext` (class) component `ResolvedEmbeddingAiContext [class]` (`b3f25608-8bc8-55c3-b74a-fa7cedee6428`) lines 142-145 [crates/gcode/src/vector/code_symbols/embedding.rs:142-145]
  - Signature: `struct ResolvedEmbeddingAiContext {`
  - Purpose: Indexed class `ResolvedEmbeddingAiContext` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:142-145]
- `resolve_embedding_ai_context` (function) component `resolve_embedding_ai_context [function]` (`9e4605d9-be27-5b47-8a88-4057f0b3b8fb`) lines 147-179 [crates/gcode/src/vector/code_symbols/embedding.rs:147-179]
  - Signature: `fn resolve_embedding_ai_context(ctx: &Context) -> ResolvedEmbeddingAiContext {`
  - Purpose: Indexed function `resolve_embedding_ai_context` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:147-179]
- `embedding_client` (function) component `embedding_client [function]` (`933da43f-3b6d-50ce-bc47-2ad31809f62c`) lines 181-203 [crates/gcode/src/vector/code_symbols/embedding.rs:181-203]
  - Signature: `pub fn embedding_client(`
  - Purpose: Indexed function `embedding_client` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:181-203]
- `embed_text` (function) component `embed_text [function]` (`e796544f-4d6e-503d-95d0-126089233f63`) lines 205-223 [crates/gcode/src/vector/code_symbols/embedding.rs:205-223]
  - Signature: `pub fn embed_text(`
  - Purpose: Indexed function `embed_text` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:205-223]
- `probe_embedding_dim` (function) component `probe_embedding_dim [function]` (`ead5f733-966a-59fe-aa08-684aff4de558`) lines 225-228 [crates/gcode/src/vector/code_symbols/embedding.rs:225-228]
  - Signature: `pub fn probe_embedding_dim(config: &EmbeddingConfig) -> Result<usize, VectorLifecycleError> {`
  - Purpose: Indexed function `probe_embedding_dim` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:225-228]
- `embed_text_batch` (function) component `embed_text_batch [function]` (`c02b677a-9ae9-5446-b9d5-15e8da244552`) lines 230-281 [crates/gcode/src/vector/code_symbols/embedding.rs:230-281]
  - Signature: `pub fn embed_text_batch(`
  - Purpose: Indexed function `embed_text_batch` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:230-281]
- `send_embedding_request` (function) component `send_embedding_request [function]` (`9eb26cd4-da4f-5002-850b-3a8ca2daea62`) lines 283-306 [crates/gcode/src/vector/code_symbols/embedding.rs:283-306]
  - Signature: `fn send_embedding_request(`
  - Purpose: Indexed function `send_embedding_request` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:283-306]
- `parse_embedding` (function) component `parse_embedding [function]` (`25e19896-ecae-5e6a-8578-4e58ec56a0d1`) lines 308-338 [crates/gcode/src/vector/code_symbols/embedding.rs:308-338]
  - Signature: `fn parse_embedding(value: &Value) -> Result<Vec<f32>, VectorLifecycleError> {`
  - Purpose: Indexed function `parse_embedding` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:308-338]
- `embed_query` (function) component `embed_query [function]` (`621907c9-5e94-53ca-983e-168df458329a`) lines 340-361 [crates/gcode/src/vector/code_symbols/embedding.rs:340-361]
  - Signature: `pub fn embed_query(config: &EmbeddingConfig, text: &str) -> Option<Vec<f32>> {`
  - Purpose: Indexed function `embed_query` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:340-361]
- `embed_query_with_source` (function) component `embed_query_with_source [function]` (`e89f6329-c427-58df-b2af-9065e27bed12`) lines 363-378 [crates/gcode/src/vector/code_symbols/embedding.rs:363-378]
  - Signature: `pub fn embed_query_with_source(source: &EmbeddingSource, text: &str) -> Option<Vec<f32>> {`
  - Purpose: Indexed function `embed_query_with_source` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:363-378]
- `vector_text_for_symbol` (function) component `vector_text_for_symbol [function]` (`87c55fec-dbf9-56e6-b8a4-455a78e9e3e3`) lines 380-411 [crates/gcode/src/vector/code_symbols/embedding.rs:380-411]
  - Signature: `pub fn vector_text_for_symbol(symbol: &Symbol) -> String {`
  - Purpose: Indexed function `vector_text_for_symbol` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:380-411]
- `TestSource` (class) component `TestSource [class]` (`5e577ae5-d712-5f8f-b4b3-425bb8d2064c`) lines 422-424 [crates/gcode/src/vector/code_symbols/embedding.rs:422-424]
  - Signature: `struct TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:422-424]
- `TestSource` (class) component `TestSource [class]` (`7f07b8a1-5332-524a-8b52-f1f5a590d87f`) lines 426-432 [crates/gcode/src/vector/code_symbols/embedding.rs:426-432]
  - Signature: `impl TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:426-432]
- `TestSource.with_values` (method) component `TestSource.with_values [method]` (`5b65687f-95a7-5816-888f-06f8cf1eaa92`) lines 427-431 [crates/gcode/src/vector/code_symbols/embedding.rs:427-431]
  - Signature: `fn with_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {`
  - Purpose: Indexed method `TestSource.with_values` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:427-431]
- `TestSource` (class) component `TestSource [class]` (`e6b0251b-ddca-5c4b-be9b-d6892f6c1800`) lines 434-445 [crates/gcode/src/vector/code_symbols/embedding.rs:434-445]
  - Signature: `impl ConfigSource for TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:434-445]
- `TestSource.config_value` (method) component `TestSource.config_value [method]` (`b83771cb-16c1-5655-ab53-63e9c74752fa`) lines 435-437 [crates/gcode/src/vector/code_symbols/embedding.rs:435-437]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed method `TestSource.config_value` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:435-437]
- `TestSource.resolve_value` (method) component `TestSource.resolve_value [method]` (`413d22ab-b544-55e9-8772-4f7e56ef77b0`) lines 439-444 [crates/gcode/src/vector/code_symbols/embedding.rs:439-444]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `TestSource.resolve_value` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:439-444]
- `resolves_via_shared_routing` (function) component `resolves_via_shared_routing [function]` (`ed7c35dc-09a9-5c86-ac65-7ebe214fd635`) lines 448-482 [crates/gcode/src/vector/code_symbols/embedding.rs:448-482]
  - Signature: `fn resolves_via_shared_routing() {`
  - Purpose: Indexed function `resolves_via_shared_routing` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:448-482]
- `reads_endpoint_from_shared_binding` (function) component `reads_endpoint_from_shared_binding [function]` (`86e8fdfe-8ee9-53d5-91e9-1bb0fe1395c3`) lines 485-507 [crates/gcode/src/vector/code_symbols/embedding.rs:485-507]
  - Signature: `fn reads_endpoint_from_shared_binding() {`
  - Purpose: Indexed function `reads_endpoint_from_shared_binding` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:485-507]
- `direct_source_uses_resolved_embedding_config` (function) component `direct_source_uses_resolved_embedding_config [function]` (`3dd5e950-1424-592b-a552-3fb7a26a9319`) lines 510-533 [crates/gcode/src/vector/code_symbols/embedding.rs:510-533]
  - Signature: `fn direct_source_uses_resolved_embedding_config() {`
  - Purpose: Indexed function `direct_source_uses_resolved_embedding_config` in `crates/gcode/src/vector/code_symbols/embedding.rs`. [crates/gcode/src/vector/code_symbols/embedding.rs:510-533]

