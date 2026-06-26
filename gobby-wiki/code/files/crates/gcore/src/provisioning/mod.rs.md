---
title: crates/gcore/src/provisioning/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/mod.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Overview

`crates/gcore/src/provisioning/mod.rs` exposes 19 indexed API symbols.

## How it fits

`crates/gcore/src/provisioning/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `StandaloneConfig` | class | StandaloneConfig is a public struct that wraps a BTreeMap<String, String> to store configuration key-value pairs with lexicographic ordering. [crates/gcore/src/provisioning/mod.rs:55-57] |
| `StandaloneConfig::new` | method | Creates a new instance initialized with a 'BTreeMap<String, String>' for the values field. [crates/gcore/src/provisioning/mod.rs:60-62] |
| `StandaloneConfig::empty` | method | This method constructs and returns a new instance of Self by delegating to its Default trait implementation. [crates/gcore/src/provisioning/mod.rs:64-66] |
| `StandaloneConfig::read_at` | method | Reads a file from the specified path and deserializes its YAML content into 'Self', returning 'Ok(None)' if the file doesn't exist, 'Ok(Some(Self))' on successful parse, or an error on I/O or parse failure. [crates/gcore/src/provisioning/mod.rs:68-77] |
| `StandaloneConfig::from_yaml_str` | method | Deserializes a YAML string into a flattened configuration object by parsing the YAML into a key-value map, applying text generation defaults from embeddings, and returning a default instance if the input is empty. [crates/gcore/src/provisioning/mod.rs:79-89] |
| `StandaloneConfig::write_at` | method | Writes the instance's key-value pairs as a nested YAML mapping to the specified file path, creating parent directories as needed. [crates/gcore/src/provisioning/mod.rs:91-102] |
| `StandaloneConfig::get` | method | Returns an optional string slice reference to the value associated with the given key by looking up the key in the internal values collection and converting the String reference to a '&str'. [crates/gcore/src/provisioning/mod.rs:104-106] |
| `StandaloneConfig::set` | method | Inserts a key-value pair into the 'values' map, converting both parameters to 'String' using the 'Into' trait. [crates/gcore/src/provisioning/mod.rs:108-110] |
| `StandaloneConfig::remove` | method | Removes the entry with the specified string key from the underlying 'values' collection. [crates/gcore/src/provisioning/mod.rs:112-114] |
| `StandaloneConfig::values` | method | Returns an immutable reference to the internal 'BTreeMap<String, String>' containing key-value pairs. [crates/gcore/src/provisioning/mod.rs:116-118] |
| `StandaloneConfig::apply_text_generation_defaults_from_embeddings` | method | Populates text generation configuration from embedding API credentials using LM Studio's default API base if no text generation settings are already defined. [crates/gcore/src/provisioning/mod.rs:120-133] |
| `StandaloneConfig::config_value` | method | This method retrieves and returns a cloned copy of a 'String' value from the internal configuration map for the given key, or 'None' if the key does not exist. [crates/gcore/src/provisioning/mod.rs:137-139] |
| `StandaloneConfig::resolve_value` | method | This method resolves environment variable patterns in the input string via 'resolve_env_pattern', explicitly rejecting '$secret:' directives and returning an error for unresolved patterns. [crates/gcore/src/provisioning/mod.rs:141-146] |
| `gcore_config_path` | function | Returns a 'PathBuf' by joining the provided 'gobby_home' directory path with the 'GCORE_CONFIG_FILENAME' constant. [crates/gcore/src/provisioning/mod.rs:149-151] |
| `services_dir` | function | This function constructs and returns a 'PathBuf' representing the services directory by joining the provided 'gobby_home' path with the 'SERVICES_DIRNAME' constant. [crates/gcore/src/provisioning/mod.rs:153-155] |
| `compose_file_path` | function | Constructs a PathBuf for the compose file by joining the COMPOSE_FILENAME constant to the services directory within the given gobby_home path. [crates/gcore/src/provisioning/mod.rs:157-159] |
| `default_database_url` | function | Constructs and returns a PostgreSQL connection URL string by formatting default authentication credentials (user, password, host, database) with a supplied port parameter. [crates/gcore/src/provisioning/mod.rs:161-170] |
| `insert_nested_yaml_value` | function | Inserts a string value into a nested YAML mapping at a key path specified by dot-separated components. [crates/gcore/src/provisioning/mod.rs:172-185] |
| `insert_nested_yaml_parts` | function | Recursively inserts a string value into a YAML mapping by traversing a dot-separated key path, creating intermediate nested mappings as needed while ensuring no key is used as both a scalar value and a nested mapping. [crates/gcore/src/provisioning/mod.rs:187-222] |

