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
  - 37-41
  - 46-52
  - '55'
  - 57-67
  - 71-73
  - 76-78
  - 85-91
  - 94-102
  - 104-112
  - 114-122
  - 124-132
  - 134-142
  - 144-152
  - 154-162
  - 164-172
  - '176'
  - 178-189
  - 193-195
  - 198-200
  - 207-220
  - 224-227
  - 338-340
  - 344-347
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/config/types.rs:5-9](crates/gcore/src/config/types.rs#L5-L9), [crates/gcore/src/config/types.rs:15-18](crates/gcore/src/config/types.rs#L15-L18), [crates/gcore/src/config/types.rs:22-28](crates/gcore/src/config/types.rs#L22-L28), [crates/gcore/src/config/types.rs:32-34](crates/gcore/src/config/types.rs#L32-L34), [crates/gcore/src/config/types.rs:37-41](crates/gcore/src/config/types.rs#L37-L41), [crates/gcore/src/config/types.rs:46-52](crates/gcore/src/config/types.rs#L46-L52), [crates/gcore/src/config/types.rs:55](crates/gcore/src/config/types.rs#L55), [crates/gcore/src/config/types.rs:57-67](crates/gcore/src/config/types.rs#L57-L67), [crates/gcore/src/config/types.rs:71-73](crates/gcore/src/config/types.rs#L71-L73), [crates/gcore/src/config/types.rs:76-78](crates/gcore/src/config/types.rs#L76-L78), [crates/gcore/src/config/types.rs:85-91](crates/gcore/src/config/types.rs#L85-L91), [crates/gcore/src/config/types.rs:94-102](crates/gcore/src/config/types.rs#L94-L102), [crates/gcore/src/config/types.rs:104-112](crates/gcore/src/config/types.rs#L104-L112), [crates/gcore/src/config/types.rs:114-122](crates/gcore/src/config/types.rs#L114-L122), [crates/gcore/src/config/types.rs:124-132](crates/gcore/src/config/types.rs#L124-L132), [crates/gcore/src/config/types.rs:134-142](crates/gcore/src/config/types.rs#L134-L142), [crates/gcore/src/config/types.rs:144-152](crates/gcore/src/config/types.rs#L144-L152), [crates/gcore/src/config/types.rs:154-162](crates/gcore/src/config/types.rs#L154-L162), [crates/gcore/src/config/types.rs:164-172](crates/gcore/src/config/types.rs#L164-L172), [crates/gcore/src/config/types.rs:176](crates/gcore/src/config/types.rs#L176), [crates/gcore/src/config/types.rs:178-189](crates/gcore/src/config/types.rs#L178-L189), [crates/gcore/src/config/types.rs:193-195](crates/gcore/src/config/types.rs#L193-L195), [crates/gcore/src/config/types.rs:198-200](crates/gcore/src/config/types.rs#L198-L200), [crates/gcore/src/config/types.rs:207-220](crates/gcore/src/config/types.rs#L207-L220), [crates/gcore/src/config/types.rs:224-227](crates/gcore/src/config/types.rs#L224-L227), [crates/gcore/src/config/types.rs:338-340](crates/gcore/src/config/types.rs#L338-L340), [crates/gcore/src/config/types.rs:344-347](crates/gcore/src/config/types.rs#L344-L347)

</details>

# crates/gcore/src/config/types.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Purpose

Defines the core configuration types used by gcore for storage, embedding, and AI routing. It groups connection settings for FalkorDB and Qdrant, OpenAI-compatible embedding endpoint settings, and shared indexing defaults, then adds `AiRouting` and `AiCapability` enums with parsing and string/key helpers so the rest of the system can map capability names to routing, provider, model, transport, and API settings. It also includes binding and tuning types plus embedding-resolution helpers to tie those settings together for consumers.
[crates/gcore/src/config/types.rs:5-9]
[crates/gcore/src/config/types.rs:15-18]
[crates/gcore/src/config/types.rs:22-28]
[crates/gcore/src/config/types.rs:32-34]
[crates/gcore/src/config/types.rs:37-41]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `FalkorConfig` | class | `pub struct FalkorConfig {` | `FalkorConfig [class]` | `736ce4a7-4629-5373-bc2b-b2c36becd71b` | 5-9 [crates/gcore/src/config/types.rs:5-9] | Indexed class `FalkorConfig` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:5-9] |
| `QdrantConfig` | class | `pub struct QdrantConfig {` | `QdrantConfig [class]` | `fc7a5920-d5d5-58ac-a945-c323e994251f` | 15-18 [crates/gcore/src/config/types.rs:15-18] | Indexed class `QdrantConfig` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:15-18] |
| `EmbeddingConfig` | class | `pub struct EmbeddingConfig {` | `EmbeddingConfig [class]` | `f374024a-0997-5ef7-810d-8916ebd8d208` | 22-28 [crates/gcore/src/config/types.rs:22-28] | Indexed class `EmbeddingConfig` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:22-28] |
| `IndexingConfig` | class | `pub struct IndexingConfig {` | `IndexingConfig [class]` | `16c45d21-a0dd-5fb7-87a7-b17c1834e03c` | 32-34 [crates/gcore/src/config/types.rs:32-34] | Indexed class `IndexingConfig` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:32-34] |
| `IndexingConfig::default` | method | `fn default() -> Self {` | `IndexingConfig::default [method]` | `4eb5e272-cfb6-56b0-bf09-ceb356573f71` | 37-41 [crates/gcore/src/config/types.rs:37-41] | Indexed method `IndexingConfig::default` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:37-41] |
| `AiRouting` | type | `pub enum AiRouting {` | `AiRouting [type]` | `b4f8f770-1392-531d-8bc3-49a4ee59902a` | 46-52 [crates/gcore/src/config/types.rs:46-52] | Indexed type `AiRouting` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:46-52] |
| `AiRouting::Err` | type | `type Err = ParseAiRoutingError;` | `AiRouting::Err [type]` | `fe3adb64-e209-5a8f-b4aa-ded7b01b0c08` | 55-55 [crates/gcore/src/config/types.rs:55] | Indexed type `AiRouting::Err` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:55] |
| `AiRouting::from_str` | method | `fn from_str(value: &str) -> Result<Self, Self::Err> {` | `AiRouting::from_str [method]` | `2fad0433-78ee-59fe-9daa-f2d966723554` | 57-67 [crates/gcore/src/config/types.rs:57-67] | Indexed method `AiRouting::from_str` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:57-67] |
| `ParseAiRoutingError` | class | `pub struct ParseAiRoutingError {` | `ParseAiRoutingError [class]` | `90aa6511-4a89-56c4-945c-1208e5d7cb67` | 71-73 [crates/gcore/src/config/types.rs:71-73] | Indexed class `ParseAiRoutingError` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:71-73] |
| `ParseAiRoutingError::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `ParseAiRoutingError::fmt [method]` | `82c103f5-dd4f-5e8e-bc16-3440aa58178a` | 76-78 [crates/gcore/src/config/types.rs:76-78] | Indexed method `ParseAiRoutingError::fmt` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:76-78] |
| `AiCapability` | type | `pub enum AiCapability {` | `AiCapability [type]` | `8907d6e7-70ee-5b09-a19f-6d4e0a7e181a` | 85-91 [crates/gcore/src/config/types.rs:85-91] | Indexed type `AiCapability` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:85-91] |
| `AiCapability::as_str` | method | `pub fn as_str(self) -> &'static str {` | `AiCapability::as_str [method]` | `f282c058-038c-5c02-b323-fccc5a777bce` | 94-102 [crates/gcore/src/config/types.rs:94-102] | Indexed method `AiCapability::as_str` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:94-102] |
| `AiCapability::namespace` | method | `pub fn namespace(self) -> &'static str {` | `AiCapability::namespace [method]` | `f007f2ff-02e3-534e-9cd2-09f92e645d9f` | 104-112 [crates/gcore/src/config/types.rs:104-112] | Indexed method `AiCapability::namespace` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:104-112] |
| `AiCapability::routing_key` | method | `pub(crate) fn routing_key(self) -> &'static str {` | `AiCapability::routing_key [method]` | `f9713eca-251c-5621-b6d1-6cdd7bb97ea2` | 114-122 [crates/gcore/src/config/types.rs:114-122] | Indexed method `AiCapability::routing_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:114-122] |
| `AiCapability::transport_key` | method | `pub(crate) fn transport_key(self) -> &'static str {` | `AiCapability::transport_key [method]` | `9331c5a8-4e36-5ec4-a247-b5c07c35386c` | 124-132 [crates/gcore/src/config/types.rs:124-132] | Indexed method `AiCapability::transport_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:124-132] |
| `AiCapability::api_base_key` | method | `pub(crate) fn api_base_key(self) -> &'static str {` | `AiCapability::api_base_key [method]` | `7f6ea463-d7f3-5f8d-9dc0-8345e27d34be` | 134-142 [crates/gcore/src/config/types.rs:134-142] | Indexed method `AiCapability::api_base_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:134-142] |
| `AiCapability::api_key_key` | method | `pub(crate) fn api_key_key(self) -> &'static str {` | `AiCapability::api_key_key [method]` | `37af91b0-3bcf-5d14-bc69-c53123301de2` | 144-152 [crates/gcore/src/config/types.rs:144-152] | Indexed method `AiCapability::api_key_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:144-152] |
| `AiCapability::model_key` | method | `pub(crate) fn model_key(self) -> &'static str {` | `AiCapability::model_key [method]` | `d6e1d6cb-a5b2-582e-a796-cecf6422d39e` | 154-162 [crates/gcore/src/config/types.rs:154-162] | Indexed method `AiCapability::model_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:154-162] |
| `AiCapability::provider_key` | method | `pub(crate) fn provider_key(self) -> &'static str {` | `AiCapability::provider_key [method]` | `c053b35d-09db-52dc-9c64-0204193469e8` | 164-172 [crates/gcore/src/config/types.rs:164-172] | Indexed method `AiCapability::provider_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:164-172] |
| `AiCapability::Err` | type | `type Err = ParseAiCapabilityError;` | `AiCapability::Err [type]` | `97b86455-4c15-5557-afe7-963929758678` | 176-176 [crates/gcore/src/config/types.rs:176] | Indexed type `AiCapability::Err` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:176] |
| `AiCapability::from_str` | method | `fn from_str(value: &str) -> Result<Self, Self::Err> {` | `AiCapability::from_str [method]` | `4009ca21-e70b-5d60-a9a4-768c7b1be355` | 178-189 [crates/gcore/src/config/types.rs:178-189] | Indexed method `AiCapability::from_str` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:178-189] |
| `ParseAiCapabilityError` | class | `pub struct ParseAiCapabilityError {` | `ParseAiCapabilityError [class]` | `b3237e2d-25d4-5d18-be6d-7d7fec522ea1` | 193-195 [crates/gcore/src/config/types.rs:193-195] | Indexed class `ParseAiCapabilityError` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:193-195] |
| `ParseAiCapabilityError::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `ParseAiCapabilityError::fmt [method]` | `f11d1a81-7818-55d1-bdff-af482ee4c29c` | 198-200 [crates/gcore/src/config/types.rs:198-200] | Indexed method `ParseAiCapabilityError::fmt` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:198-200] |
| `CapabilityBinding` | class | `pub struct CapabilityBinding {` | `CapabilityBinding [class]` | `fb194676-f6c9-5a57-8e6a-1a97918a9f1e` | 207-220 [crates/gcore/src/config/types.rs:207-220] | Indexed class `CapabilityBinding` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:207-220] |
| `AiTuning` | class | `pub struct AiTuning {` | `AiTuning [class]` | `70929152-450c-5c61-8d30-840f62da781c` | 224-227 [crates/gcore/src/config/types.rs:224-227] | Indexed class `AiTuning` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:224-227] |
| `all` | function | `pub fn all() -> &'static [&'static str] {` | `all [function]` | `b1442cb5-c8ef-5a26-ac20-09358ef34b57` | 338-340 [crates/gcore/src/config/types.rs:338-340] | Indexed function `all` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:338-340] |
| `EmbeddingConfigResolution` | class | `pub struct EmbeddingConfigResolution {` | `EmbeddingConfigResolution [class]` | `3697426f-39d3-5a7a-9354-fd78aa859aa2` | 344-347 [crates/gcore/src/config/types.rs:344-347] | Indexed class `EmbeddingConfigResolution` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:344-347] |
