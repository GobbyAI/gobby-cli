---
title: crates/gcore/src/provisioning/bootstrap.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/bootstrap.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/bootstrap.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Overview

`crates/gcore/src/provisioning/bootstrap.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcore/src/provisioning/bootstrap.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `EmbeddingBootstrap` | class | 'EmbeddingBootstrap' is a configuration struct for initializing an embedding service, specifying the provider, API base URL, model name, vector dimensionality, an optional query prefix, and an optional API key. [crates/gcore/src/provisioning/bootstrap.rs:8-15] |
| `TextGenerationBootstrap` | class | 'TextGenerationBootstrap' is a configuration struct containing the text generation API base URL, target model identifier, and an optional API key for authentication. [crates/gcore/src/provisioning/bootstrap.rs:18-22] |
| `EmbeddingBootstrap::lm_studio` | method | Constructs and returns a 'Self' configured for the 'lmstudio' provider with the default LM Studio API base, default model, default embedding vector dimension, and 'query_prefix' and 'api_key' set to 'None'. [crates/gcore/src/provisioning/bootstrap.rs:25-34] |
| `EmbeddingBootstrap::ollama` | method | Constructs and returns a default 'Self' configured for the 'ollama' provider, using the default Ollama API base, default model, default embedding vector dimension, and 'None' for both 'query_prefix' and 'api_key'. [crates/gcore/src/provisioning/bootstrap.rs:36-45] |
| `TextGenerationBootstrap::from_embedding` | method | Constructs 'Self' by delegating to 'from_endpoint', passing the embedding’s provider as 'Some(&embedding.provider)' along with cloned 'api_base' and 'api_key' values. [crates/gcore/src/provisioning/bootstrap.rs:49-55] |
| `TextGenerationBootstrap::from_endpoint` | method | Constructs a new instance by converting 'api_base' into a 'String', deriving 'model' via 'default_text_model(provider, &api_base).to_string()', and storing the provided 'api_key' unchanged. [crates/gcore/src/provisioning/bootstrap.rs:57-68] |
| `apply_text_generation_bootstrap` | function | Sets a 'StandaloneConfig' for direct text-generation bootstrap by writing the routing, API base, and model, clearing transport/provider/profile and stale verify overrides, and conditionally setting or removing the API key based on 'TextGenerationBootstrap::api_key'. [crates/gcore/src/provisioning/bootstrap.rs:71-91] |
| `default_text_model` | function | Returns 'DEFAULT_OLLAMA_TEXT_MODEL' when the provider is '"ollama"' after trimming/lowercasing or the trimmed 'api_base' equals the default Ollama API base, otherwise returns 'DEFAULT_LM_STUDIO_TEXT_MODEL'. [crates/gcore/src/provisioning/bootstrap.rs:93-103] |
| `write_standalone_bootstrap` | function | Creates a 'StandaloneConfig' seeded with Postgres, FalkorDB, and Qdrant connection settings plus optional embedding and compose-file settings, writes it to 'path', and returns the resulting config. [crates/gcore/src/provisioning/bootstrap.rs:105-139] |
| `flatten_yaml_value` | function | Forwards the provided optional key prefix, YAML value, and mutable output map to 'flatten_yaml_value_at_depth' with an initial recursion depth of '0', returning its 'anyhow::Result<()>'. [crates/gcore/src/provisioning/bootstrap.rs:141-147] |
| `flatten_yaml_value_at_depth` | function | Recursively flattens a 'serde_yaml::Value' into a 'BTreeMap<String, String>' using dotted key paths, skipping nulls, converting scalar leaf values to strings, and returning an error for non-string keys, non-mapping roots, or excessive nesting depth. [crates/gcore/src/provisioning/bootstrap.rs:149-202] |
| `scalar_to_string` | function | Converts a 'serde_yaml::Value' at a given YAML path into an 'Option<String>' by returning 'None' for 'Null', cloning scalar strings, stringifying booleans and numbers, rejecting sequences and mappings with a path-specific error, and serializing any other tagged value with 'serde_yaml::to_string' then trimming whitespace. [crates/gcore/src/provisioning/bootstrap.rs:204-225] |
| `yaml_path` | function | Returns 'prefix' when it is 'Some(non-empty string)' and otherwise returns the fallback '"<root>"'. [crates/gcore/src/provisioning/bootstrap.rs:227-229] |
| `flatten` | function | Parses the input YAML string into a 'serde_yaml::Value', recursively flattens it into a 'BTreeMap<String, String>' via 'flatten_yaml_value', and returns the result or any parsing/flattening error. [crates/gcore/src/provisioning/bootstrap.rs:235-240] |

_Verified by 4 in-file unit tests._

