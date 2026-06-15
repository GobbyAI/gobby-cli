---
title: crates/gcore/src/config/types.rs
type: code_file
provenance:
- file: crates/gcore/src/config/types.rs
  ranges:
  - 5-9
  - 15-18
  - 22-28
  - 32-34
  - 36-42
  - 46-52
  - 54-68
  - 71-73
  - 75-79
  - '81'
  - 85-91
  - 93-173
  - 175-190
  - 193-195
  - 197-201
  - '203'
  - 207-220
  - 224-227
  - 338-340
  - 344-347
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config/types.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Purpose

This file defines the core configuration and parsing types used by `gcore` for service connections, indexing behavior, and AI feature routing. It groups plain config structs for FalkorDB, Qdrant, embeddings, indexing, capability bindings, tuning, and embedding resolution, then adds the `AiRouting` and `AiCapability` enums plus their `FromStr`, displayable error types, and string/registry key accessors so config values can be parsed from text and mapped consistently to the daemon’s expected identifiers.
[crates/gcore/src/config/types.rs:5-9]
[crates/gcore/src/config/types.rs:15-18]
[crates/gcore/src/config/types.rs:22-28]
[crates/gcore/src/config/types.rs:32-34]
[crates/gcore/src/config/types.rs:36-42]

## API Symbols

- `FalkorConfig` (class) component `FalkorConfig [class]` (`736ce4a7-4629-5373-bc2b-b2c36becd71b`) lines 5-9 [crates/gcore/src/config/types.rs:5-9]
  - Signature: `pub struct FalkorConfig {`
  - Purpose: 'FalkorConfig' is a Rust configuration struct that stores the Falkor service host as a 'String', the TCP port as a 'u16', and an optional 'String' password for authentication. [crates/gcore/src/config/types.rs:5-9]
- `QdrantConfig` (class) component `QdrantConfig [class]` (`fc7a5920-d5d5-58ac-a945-c323e994251f`) lines 15-18 [crates/gcore/src/config/types.rs:15-18]
  - Signature: `pub struct QdrantConfig {`
  - Purpose: 'QdrantConfig' is a configuration struct that optionally stores the Qdrant service URL and API key for authenticating and connecting to a Qdrant instance. [crates/gcore/src/config/types.rs:15-18]
- `EmbeddingConfig` (class) component `EmbeddingConfig [class]` (`f374024a-0997-5ef7-810d-8916ebd8d208`) lines 22-28 [crates/gcore/src/config/types.rs:22-28]
  - Signature: `pub struct EmbeddingConfig {`
  - Purpose: 'EmbeddingConfig' stores the embedding service connection and request parameters: API base URL, model name, optional API key, optional query prefix, and a timeout in seconds. [crates/gcore/src/config/types.rs:22-28]
- `IndexingConfig` (class) component `IndexingConfig [class]` (`16c45d21-a0dd-5fb7-87a7-b17c1834e03c`) lines 32-34 [crates/gcore/src/config/types.rs:32-34]
  - Signature: `pub struct IndexingConfig {`
  - Purpose: 'IndexingConfig' is a configuration struct that controls indexing behavior via a single 'respect_gitignore' flag, indicating whether '.gitignore' rules should be honored during indexing. [crates/gcore/src/config/types.rs:32-34]
- `IndexingConfig` (class) component `IndexingConfig [class]` (`3509b2e1-9de9-5823-a6d3-cbb5696b1b44`) lines 36-42 [crates/gcore/src/config/types.rs:36-42]
  - Signature: `impl Default for IndexingConfig {`
  - Purpose: 'IndexingConfig' is a defaultable configuration type whose 'default()' constructor initializes 'respect_gitignore' to 'true'. [crates/gcore/src/config/types.rs:36-42]
- `IndexingConfig.default` (method) component `IndexingConfig.default [method]` (`4eb5e272-cfb6-56b0-bf09-ceb356573f71`) lines 37-41 [crates/gcore/src/config/types.rs:37-41]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a 'Self' instance with 'respect_gitignore' set to 'true'. [crates/gcore/src/config/types.rs:37-41]
- `AiRouting` (type) component `AiRouting [type]` (`b4f8f770-1392-531d-8bc3-49a4ee59902a`) lines 46-52 [crates/gcore/src/config/types.rs:46-52]
  - Signature: `pub enum AiRouting {`
  - Purpose: Indexed type `AiRouting` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:46-52]
- `AiRouting` (class) component `AiRouting [class]` (`f2f8b33e-f912-5db4-b466-97d2f13d26eb`) lines 54-68 [crates/gcore/src/config/types.rs:54-68]
  - Signature: `impl std::str::FromStr for AiRouting {`
  - Purpose: 'AiRouting' implements 'FromStr' to parse a trimmed string into one of four routing modes ('auto', 'daemon', 'direct', 'off'), returning 'ParseAiRoutingError' with the original value for any other input. [crates/gcore/src/config/types.rs:54-68]
- `AiRouting.Err` (type) component `AiRouting.Err [type]` (`fe3adb64-e209-5a8f-b4aa-ded7b01b0c08`) lines 55-55 [crates/gcore/src/config/types.rs:55]
  - Signature: `type Err = ParseAiRoutingError;`
  - Purpose: Indexed type `AiRouting.Err` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:55]
- `AiRouting.from_str` (method) component `AiRouting.from_str [method]` (`2fad0433-78ee-59fe-9daa-f2d966723554`) lines 57-67 [crates/gcore/src/config/types.rs:57-67]
  - Signature: `fn from_str(value: &str) -> Result<Self, Self::Err> {`
  - Purpose: Parses a trimmed string into 'AiRouting' by accepting exactly '"auto"', '"daemon"', '"direct"', or '"off"', and returns 'ParseAiRoutingError' containing the original trimmed value for any other input. [crates/gcore/src/config/types.rs:57-67]
- `ParseAiRoutingError` (class) component `ParseAiRoutingError [class]` (`90aa6511-4a89-56c4-945c-1208e5d7cb67`) lines 71-73 [crates/gcore/src/config/types.rs:71-73]
  - Signature: `pub struct ParseAiRoutingError {`
  - Purpose: 'ParseAiRoutingError' is a Rust error struct that encapsulates the offending routing input as a private 'String' value when parsing AI routing data fails. [crates/gcore/src/config/types.rs:71-73]
- `ParseAiRoutingError` (class) component `ParseAiRoutingError [class]` (`e4a1042b-6543-513d-a4be-6cae210cf50e`) lines 75-79 [crates/gcore/src/config/types.rs:75-79]
  - Signature: `impl std::fmt::Display for ParseAiRoutingError {`
  - Purpose: 'ParseAiRoutingError' implements 'Display' to render the error as 'invalid AI routing '<value>'', where '<value>' is the offending routing string. [crates/gcore/src/config/types.rs:75-79]
- `ParseAiRoutingError.fmt` (method) component `ParseAiRoutingError.fmt [method]` (`82c103f5-dd4f-5e8e-bc16-3440aa58178a`) lines 76-78 [crates/gcore/src/config/types.rs:76-78]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Implements 'Display'-style formatting by writing 'invalid AI routing '<value>'' into the provided formatter and returning the result of that write operation. [crates/gcore/src/config/types.rs:76-78]
- `ParseAiRoutingError` (class) component `ParseAiRoutingError [class]` (`365633d0-03de-5cf7-b986-4712654447a4`) lines 81-81 [crates/gcore/src/config/types.rs:81]
  - Signature: `impl std::error::Error for ParseAiRoutingError {}`
  - Purpose: 'ParseAiRoutingError' is a Rust error type that implements 'std::error::Error' as a marker for failures encountered while parsing AI routing data. [crates/gcore/src/config/types.rs:81]
- `AiCapability` (type) component `AiCapability [type]` (`8907d6e7-70ee-5b09-a19f-6d4e0a7e181a`) lines 85-91 [crates/gcore/src/config/types.rs:85-91]
  - Signature: `pub enum AiCapability {`
  - Purpose: Indexed type `AiCapability` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:85-91]
- `AiCapability` (class) component `AiCapability [class]` (`3d8cbb54-ca64-5431-bb90-5387a2c692cd`) lines 93-173 [crates/gcore/src/config/types.rs:93-173]
  - Signature: `impl AiCapability {`
  - Purpose: 'AiCapability' is an enum-backed capability descriptor that provides stable string, namespace, routing, transport, and API-base key mappings for each AI feature variant ('Embed', 'AudioTranscribe', 'AudioTranslate', 'VisionExtract', and 'TextGenerate'). [crates/gcore/src/config/types.rs:93-173]
- `AiCapability.as_str` (method) component `AiCapability.as_str [method]` (`f282c058-038c-5c02-b323-fccc5a777bce`) lines 94-102 [crates/gcore/src/config/types.rs:94-102]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Returns the canonical '&'static str' identifier for the enum variant, mapping 'Embed', 'AudioTranscribe', 'AudioTranslate', 'VisionExtract', and 'TextGenerate' to '"embed"', '"audio_transcribe"', '"audio_translate"', '"vision_extract"', and '"text_generate"' respectively. [crates/gcore/src/config/types.rs:94-102]
- `AiCapability.namespace` (method) component `AiCapability.namespace [method]` (`f007f2ff-02e3-534e-9cd2-09f92e645d9f`) lines 104-112 [crates/gcore/src/config/types.rs:104-112]
  - Signature: `pub fn namespace(self) -> &'static str {`
  - Purpose: Returns the static namespace string constant associated with the enum variant, mapping each variant to its corresponding 'ai_keys::*_NAMESPACE' value. [crates/gcore/src/config/types.rs:104-112]
- `AiCapability.routing_key` (method) component `AiCapability.routing_key [method]` (`f9713eca-251c-5621-b6d1-6cdd7bb97ea2`) lines 114-122 [crates/gcore/src/config/types.rs:114-122]
  - Signature: `pub(crate) fn routing_key(self) -> &'static str {`
  - Purpose: Returns the static routing key string constant corresponding to the enum variant, mapping 'Embed', 'AudioTranscribe', 'AudioTranslate', 'VisionExtract', and 'TextGenerate' to their respective 'ai_keys::*_ROUTING' values. [crates/gcore/src/config/types.rs:114-122]
- `AiCapability.transport_key` (method) component `AiCapability.transport_key [method]` (`9331c5a8-4e36-5ec4-a247-b5c07c35386c`) lines 124-132 [crates/gcore/src/config/types.rs:124-132]
  - Signature: `pub(crate) fn transport_key(self) -> &'static str {`
  - Purpose: Returns the static transport key constant associated with the enum variant, mapping each self variant to its corresponding 'ai_keys::*_TRANSPORT' string. [crates/gcore/src/config/types.rs:124-132]
- `AiCapability.api_base_key` (method) component `AiCapability.api_base_key [method]` (`7f6ea463-d7f3-5f8d-9dc0-8345e27d34be`) lines 134-142 [crates/gcore/src/config/types.rs:134-142]
  - Signature: `pub(crate) fn api_base_key(self) -> &'static str {`
  - Purpose: Returns the static API base key string constant associated with the enum variant, mapping 'Embed', 'AudioTranscribe', 'AudioTranslate', 'VisionExtract', and 'TextGenerate' to their respective 'ai_keys::*_API_BASE' values. [crates/gcore/src/config/types.rs:134-142]
- `AiCapability.api_key_key` (method) component `AiCapability.api_key_key [method]` (`37af91b0-3bcf-5d14-bc69-c53123301de2`) lines 144-152 [crates/gcore/src/config/types.rs:144-152]
  - Signature: `pub(crate) fn api_key_key(self) -> &'static str {`
  - Purpose: Returns the static API key identifier string associated with the enum variant by matching 'self' to the corresponding 'ai_keys::*_API_KEY' constant. [crates/gcore/src/config/types.rs:144-152]
- `AiCapability.model_key` (method) component `AiCapability.model_key [method]` (`d6e1d6cb-a5b2-582e-a796-cecf6422d39e`) lines 154-162 [crates/gcore/src/config/types.rs:154-162]
  - Signature: `pub(crate) fn model_key(self) -> &'static str {`
  - Purpose: Returns the static model-key string constant associated with the enum variant, mapping each 'Self' case to the corresponding 'ai_keys::*_MODEL' value. [crates/gcore/src/config/types.rs:154-162]
- `AiCapability.provider_key` (method) component `AiCapability.provider_key [method]` (`c053b35d-09db-52dc-9c64-0204193469e8`) lines 164-172 [crates/gcore/src/config/types.rs:164-172]
  - Signature: `pub(crate) fn provider_key(self) -> &'static str {`
  - Purpose: Returns the static provider identifier string for the enum variant by matching 'self' to the corresponding 'ai_keys' constant for embeddings, audio transcription, audio translation, vision extraction, or text generation. [crates/gcore/src/config/types.rs:164-172]
- `AiCapability` (class) component `AiCapability [class]` (`61be36a5-74b0-5809-8482-9dff4ac4d5da`) lines 175-190 [crates/gcore/src/config/types.rs:175-190]
  - Signature: `impl std::str::FromStr for AiCapability {`
  - Purpose: 'AiCapability' implements 'FromStr' by trimming the input and mapping '"embed"'/'"embeddings"' to 'Embed', '"audio_transcribe"' to 'AudioTranscribe', '"audio_translate"' to 'AudioTranslate', '"vision_extract"' to 'VisionExtract', and '"text_generate"' to 'TextGenerate', otherwise returning 'ParseAiCapabilityError' containing the unrecognized value. [crates/gcore/src/config/types.rs:175-190]
- `AiCapability.Err` (type) component `AiCapability.Err [type]` (`97b86455-4c15-5557-afe7-963929758678`) lines 176-176 [crates/gcore/src/config/types.rs:176]
  - Signature: `type Err = ParseAiCapabilityError;`
  - Purpose: Indexed type `AiCapability.Err` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:176]
- `AiCapability.from_str` (method) component `AiCapability.from_str [method]` (`4009ca21-e70b-5d60-a9a4-768c7b1be355`) lines 178-189 [crates/gcore/src/config/types.rs:178-189]
  - Signature: `fn from_str(value: &str) -> Result<Self, Self::Err> {`
  - Purpose: Parses a trimmed input string into an 'AiCapability' variant by matching '"embed"'/'"embeddings"', '"audio_transcribe"', '"audio_translate"', '"vision_extract"', or '"text_generate"', and otherwise returns 'ParseAiCapabilityError' containing the unrecognized value. [crates/gcore/src/config/types.rs:178-189]
- `ParseAiCapabilityError` (class) component `ParseAiCapabilityError [class]` (`b3237e2d-25d4-5d18-be6d-7d7fec522ea1`) lines 193-195 [crates/gcore/src/config/types.rs:193-195]
  - Signature: `pub struct ParseAiCapabilityError {`
  - Purpose: 'ParseAiCapabilityError' is a Rust error type that owns the original input 'String' in its 'value' field for reporting or diagnostics when AI capability parsing fails. [crates/gcore/src/config/types.rs:193-195]
- `ParseAiCapabilityError` (class) component `ParseAiCapabilityError [class]` (`3168049f-315f-5cff-801d-791e64be55f9`) lines 197-201 [crates/gcore/src/config/types.rs:197-201]
  - Signature: `impl std::fmt::Display for ParseAiCapabilityError {`
  - Purpose: Formats a 'ParseAiCapabilityError' as the message 'invalid AI capability '<value>'', interpolating the stored 'value' into the error string. [crates/gcore/src/config/types.rs:197-201]
- `ParseAiCapabilityError.fmt` (method) component `ParseAiCapabilityError.fmt [method]` (`f11d1a81-7818-55d1-bdff-af482ee4c29c`) lines 198-200 [crates/gcore/src/config/types.rs:198-200]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Implements 'Display' formatting by writing the string 'invalid AI capability '<value>'' to the formatter using 'self.value'. [crates/gcore/src/config/types.rs:198-200]
- `ParseAiCapabilityError` (class) component `ParseAiCapabilityError [class]` (`f00d9a1e-0c98-5942-a4d6-0efdd2365944`) lines 203-203 [crates/gcore/src/config/types.rs:203]
  - Signature: `impl std::error::Error for ParseAiCapabilityError {}`
  - Purpose: 'ParseAiCapabilityError' is a Rust error type that implements the standard 'std::error::Error' trait, marking it as a recoverable parse failure for AI capability parsing. [crates/gcore/src/config/types.rs:203]
- `CapabilityBinding` (class) component `CapabilityBinding [class]` (`fb194676-f6c9-5a57-8e6a-1a97918a9f1e`) lines 207-220 [crates/gcore/src/config/types.rs:207-220]
  - Signature: `pub struct CapabilityBinding {`
  - Purpose: 'CapabilityBinding' is a configuration struct that binds an 'AiRouting' policy to optional transport, API, model, provider, task, and language parameters, plus an optional daemon feature 'profile' used only for 'text_generate' when no explicit provider/model route is specified. [crates/gcore/src/config/types.rs:207-220]
- `AiTuning` (class) component `AiTuning [class]` (`70929152-450c-5c61-8d30-840f62da781c`) lines 224-227 [crates/gcore/src/config/types.rs:224-227]
  - Signature: `pub struct AiTuning {`
  - Purpose: 'AiTuning' is a configuration struct that sets the maximum concurrency as an 8-bit unsigned integer and optionally specifies a keep-alive value as a string. [crates/gcore/src/config/types.rs:224-227]
- `all` (function) component `all [function]` (`b1442cb5-c8ef-5a26-ac20-09358ef34b57`) lines 338-340 [crates/gcore/src/config/types.rs:338-340]
  - Signature: `pub fn all() -> &'static [&'static str] {`
  - Purpose: Returns the 'ALL_KEYS' constant as a ''static' slice of ''static' string slices. [crates/gcore/src/config/types.rs:338-340]
- `EmbeddingConfigResolution` (class) component `EmbeddingConfigResolution [class]` (`3697426f-39d3-5a7a-9354-fd78aa859aa2`) lines 344-347 [crates/gcore/src/config/types.rs:344-347]
  - Signature: `pub struct EmbeddingConfigResolution {`
  - Purpose: 'EmbeddingConfigResolution' is a Rust struct that bundles an 'EmbeddingConfig' with the resolved static namespace string ('&'static str') used to identify it. [crates/gcore/src/config/types.rs:344-347]

