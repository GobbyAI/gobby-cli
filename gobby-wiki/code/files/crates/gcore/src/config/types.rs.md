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

`crates/gcore/src/config/types.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gcore/src/config/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FalkorConfig` | class | 'FalkorConfig' is a public Rust structure that defines connection configuration parameters, including a host address as a 'String', a port number as a 'u16', and an optional password as an 'Option<String>'. [crates/gcore/src/config/types.rs:7-11] |
| `QdrantConfig` | class | The 'QdrantConfig' struct is a public configuration container holding optional connection details for a Qdrant client, specifically containing an optional URL string and an optional API key string. [crates/gcore/src/config/types.rs:17-20] |
| `EmbeddingConfig` | class | 'EmbeddingConfig' is a Rust structure that defines the configuration parameters for connecting to and interacting with an embedding API, including the base URL, model name, optional authentication key, optional query prefix, and a request timeout in seconds. [crates/gcore/src/config/types.rs:24-30] |
| `IndexingConfig` | class | 'IndexingConfig' is a configuration structure containing a boolean flag that determines whether the indexing process should respect ignore patterns specified in '.gitignore' files. [crates/gcore/src/config/types.rs:34-36] |
| `IndexingConfig::default` | method | The 'default' method constructs and returns an instance of the implementing type with the 'respect_gitignore' field initialized to 'true'. [crates/gcore/src/config/types.rs:39-43] |
| `AiRouting` | type | Indexed type `AiRouting` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:48-54] |
| `AiRouting::Err` | type | Indexed type `AiRouting::Err` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:57] |
| `AiRouting::from_str` | method | The 'from_str' method parses a trimmed string slice into an enum representation, returning 'Ok' with the corresponding variant ('Auto', 'Daemon', 'Direct', or 'Off') if matched, or 'Err' containing a 'ParseAiRoutingError' if the input is unrecognized. [crates/gcore/src/config/types.rs:59-69] |
| `ParseAiRoutingError` | class | 'ParseAiRoutingError' is a public Rust struct representing an AI routing parsing error that encapsulates a single private 'String' field named 'value' to store the error detail. [crates/gcore/src/config/types.rs:73-75] |
| `ParseAiRoutingError::fmt` | method | This method formats the object for display by writing the string "invalid AI routing" followed by the single-quoted string representation of its 'value' field to the provided formatter. [crates/gcore/src/config/types.rs:78-80] |
| `AiCapability` | type | Indexed type `AiCapability` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:87-93] |
| `AiCapability::as_str` | method | The 'as_str' method consumes the enum variant to match and return its corresponding static string slice representation. [crates/gcore/src/config/types.rs:96-104] |
| `AiCapability::namespace` | method | The 'namespace' method matches the enum instance to return its corresponding static string namespace constant defined in the 'ai_keys' module. [crates/gcore/src/config/types.rs:106-114] |
| `AiCapability::routing_key` | method | This crate-visible method consumes the enum receiver and maps its variants to their corresponding static string slice routing key constants defined in the 'ai_keys' module. [crates/gcore/src/config/types.rs:116-124] |
| `AiCapability::transport_key` | method | This crate-visible method maps the enum instance to its corresponding static string slice constant representing the associated AI service transport key. [crates/gcore/src/config/types.rs:126-134] |
| `AiCapability::api_base_key` | method | This crate-visible method maps enum variants representing AI capabilities to their corresponding static string slice API base key constants defined in the 'ai_keys' module. [crates/gcore/src/config/types.rs:136-144] |
| `AiCapability::api_key_key` | method | The crate-visible 'api_key_key' method maps the enum instance to its corresponding static string slice reference representing the specific API key identifier defined in the 'ai_keys' module. [crates/gcore/src/config/types.rs:146-154] |
| `AiCapability::model_key` | method | The 'model_key' method maps the enum instance to its corresponding static string slice constant representing the associated AI model key. [crates/gcore/src/config/types.rs:156-164] |
| `AiCapability::provider_key` | method | The 'provider_key' method maps the enum instance to its corresponding static string slice representing the specific AI provider key constant. [crates/gcore/src/config/types.rs:166-174] |
| `AiCapability::Err` | type | Indexed type `AiCapability::Err` in `crates/gcore/src/config/types.rs`. [crates/gcore/src/config/types.rs:178] |
| `AiCapability::from_str` | method | This method parses a trimmed string slice into an enum variant representing an AI capability, returning a 'ParseAiCapabilityError' if the input does not match any predefined capability string. [crates/gcore/src/config/types.rs:180-191] |
| `ParseAiCapabilityError` | class | The 'ParseAiCapabilityError' struct represents an error encountered during the parsing of an AI capability, encapsulating the invalid string value that triggered the failure. [crates/gcore/src/config/types.rs:195-197] |
| `ParseAiCapabilityError::fmt` | method | This method implements standard string formatting to write an "invalid AI capability" error message containing the 'self.value' field to the provided formatter. [crates/gcore/src/config/types.rs:200-202] |
| `FeatureCandidate` | class | 'FeatureCandidate' is a serializable Rust struct containing a candidate identifier string and an optional reasoning effort configuration string. [crates/gcore/src/config/types.rs:209-213] |

_7 more symbol(s) not shown — run `gcode outline crates/gcore/src/config/types.rs` for the full list._

