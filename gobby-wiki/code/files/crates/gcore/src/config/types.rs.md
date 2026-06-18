---
title: crates/gcore/src/config/types.rs
type: code_file
provenance:
- file: crates/gcore/src/config/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config/types.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Overview

`crates/gcore/src/config/types.rs` exposes 27 indexed API symbols.

## How it fits

`crates/gcore/src/config/types.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FalkorConfig` | class | Indexed class `FalkorConfig` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:5-9] |
| `QdrantConfig` | class | Indexed class `QdrantConfig` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:15-18] |
| `EmbeddingConfig` | class | Indexed class `EmbeddingConfig` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:22-28] |
| `IndexingConfig` | class | Indexed class `IndexingConfig` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:32-34] |
| `IndexingConfig::default` | method | Indexed method `IndexingConfig::default` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:37-41] |
| `AiRouting` | type | Indexed type `AiRouting` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:46-52] |
| `AiRouting::Err` | type | Indexed type `AiRouting::Err` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:55] |
| `AiRouting::from_str` | method | Parses a trimmed '&str' into an 'AiRouting' variant by accepting '"auto"', '"daemon"', '"direct"', or '"off"', and otherwise returns 'ParseAiRoutingError' containing the unrecognized value. [crates/gcore/src/config/types.rs:57-67] |
| `ParseAiRoutingError` | class | 'ParseAiRoutingError' is a struct wrapping a 'String' 'value' that represents the unparsed input associated with an AI routing parse failure. [crates/gcore/src/config/types.rs:71-73] |
| `ParseAiRoutingError::fmt` | method | Formats the value as 'invalid AI routing '<value>'' by writing the contained 'self.value' into the provided formatter and returning the resulting 'std::fmt::Result'. [crates/gcore/src/config/types.rs:76-78] |
| `AiCapability` | type | Indexed type `AiCapability` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:85-91] |
| `AiCapability::as_str` | method | Returns the static string identifier for the enum variant, mapping 'Embed', 'AudioTranscribe', 'AudioTranslate', 'VisionExtract', and 'TextGenerate' to '"embed"', '"audio_transcribe"', '"audio_translate"', '"vision_extract"', and '"text_generate"' respectively. [crates/gcore/src/config/types.rs:94-102] |
| `AiCapability::namespace` | method | Indexed method `AiCapability::namespace` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:104-112] |
| `AiCapability::routing_key` | method | Indexed method `AiCapability::routing_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:114-122] |
| `AiCapability::transport_key` | method | Indexed method `AiCapability::transport_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:124-132] |
| `AiCapability::api_base_key` | method | Indexed method `AiCapability::api_base_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:134-142] |
| `AiCapability::api_key_key` | method | Returns the '&'static str' constant for the current enum variant by matching 'self' to the corresponding API key identifier in 'ai_keys'. [crates/gcore/src/config/types.rs:144-152] |
| `AiCapability::model_key` | method | Indexed method `AiCapability::model_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:154-162] |
| `AiCapability::provider_key` | method | Indexed method `AiCapability::provider_key` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:164-172] |
| `AiCapability::Err` | type | Indexed type `AiCapability::Err` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:176] |
| `AiCapability::from_str` | method | Indexed method `AiCapability::from_str` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:178-189] |
| `ParseAiCapabilityError` | class | Indexed class `ParseAiCapabilityError` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:193-195] |
| `ParseAiCapabilityError::fmt` | method | Indexed method `ParseAiCapabilityError::fmt` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:198-200] |
| `CapabilityBinding` | class | 'CapabilityBinding' is a configuration record that binds AI routing and optional direct/inherited transport, API, provider, model, task, and language parameters, including separate profile/model/API-key overrides for the verification pass in 'text_generate' flows. [crates/gcore/src/config/types.rs:207-230] |
| `AiTuning` | class | 'AiTuning' is a configuration struct that sets an AI client’s maximum concurrent operations via 'max_concurrency' and optionally specifies a keep-alive duration or policy string via 'keep_alive'. [crates/gcore/src/config/types.rs:234-237] |
| `all` | function | Indexed function `all` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:354-356] |
| `EmbeddingConfigResolution` | class | Indexed class `EmbeddingConfigResolution` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:360-363] |

