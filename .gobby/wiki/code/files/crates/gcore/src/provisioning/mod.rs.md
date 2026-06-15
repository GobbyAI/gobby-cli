---
title: crates/gcore/src/provisioning/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/mod.rs
  ranges:
  - 53-55
  - 57-115
  - 117-128
  - 130-132
  - 134-136
  - 138-140
  - 142-151
  - 153-166
  - 168-203
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/mod.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Purpose

This module defines the standalone provisioning layer for GCore: it packages bootstrap and Docker service config defaults, filesystem path helpers, and nested YAML key insertion so runtime callers can mirror the daemon’s service layout and persist bootstrap state in `gcore.yaml`.

Its main type, `StandaloneConfig`, is a thin `BTreeMap<String, String>` wrapper that can load and save YAML, expose simple key accessors, and satisfy `ConfigSource` by returning stored values and resolving environment patterns while rejecting `$secret:` references because secret lookup requires the daemon-backed store.
[crates/gcore/src/provisioning/mod.rs:53-55]
[crates/gcore/src/provisioning/mod.rs:57-115]
[crates/gcore/src/provisioning/mod.rs:58-60]
[crates/gcore/src/provisioning/mod.rs:62-64]
[crates/gcore/src/provisioning/mod.rs:66-75]

## API Symbols

- `StandaloneConfig` (class) component `StandaloneConfig [class]` (`802640ac-0e89-5daa-a220-3a04d2f0db1b`) lines 53-55 [crates/gcore/src/provisioning/mod.rs:53-55]
  - Signature: `pub struct StandaloneConfig {`
  - Purpose: 'StandaloneConfig' is a simple configuration container that stores string key-value pairs in a 'BTreeMap<String, String>'. [crates/gcore/src/provisioning/mod.rs:53-55]
- `StandaloneConfig` (class) component `StandaloneConfig [class]` (`89374ad3-9649-53cd-8fcb-fd84a891d058`) lines 57-115 [crates/gcore/src/provisioning/mod.rs:57-115]
  - Signature: `impl StandaloneConfig {`
  - Purpose: 'StandaloneConfig' is a thin YAML-backed configuration wrapper around a 'BTreeMap<String, String>' that supports empty/default construction, path-based load/save, flattened nested key serialization/deserialization, and basic key get/set/remove accessors. [crates/gcore/src/provisioning/mod.rs:57-115]
- `StandaloneConfig.new` (method) component `StandaloneConfig.new [method]` (`30681f49-c1c0-561e-a4dd-1b17ca4a8c53`) lines 58-60 [crates/gcore/src/provisioning/mod.rs:58-60]
  - Signature: `pub fn new(values: BTreeMap<String, String>) -> Self {`
  - Purpose: Constructs a new instance by moving the provided 'BTreeMap<String, String>' into the 'values' field. [crates/gcore/src/provisioning/mod.rs:58-60]
- `StandaloneConfig.empty` (method) component `StandaloneConfig.empty [method]` (`1e3dd01d-7223-5091-a7c1-76ef5be762e1`) lines 62-64 [crates/gcore/src/provisioning/mod.rs:62-64]
  - Signature: `pub fn empty() -> Self {`
  - Purpose: Returns a new 'Self' by delegating to 'Self::default()', producing the type’s default empty value. [crates/gcore/src/provisioning/mod.rs:62-64]
- `StandaloneConfig.read_at` (method) component `StandaloneConfig.read_at [method]` (`7f881cf6-e384-552c-abd8-6cd0cc741b9a`) lines 66-75 [crates/gcore/src/provisioning/mod.rs:66-75]
  - Signature: `pub fn read_at(path: &Path) -> anyhow::Result<Option<Self>> {`
  - Purpose: Returns 'Ok(None)' if the path does not exist, otherwise reads the file as UTF-8 text and parses it from YAML into 'Self', wrapping any I/O or parse failure with the path in an 'anyhow' error. [crates/gcore/src/provisioning/mod.rs:66-75]
- `StandaloneConfig.from_yaml_str` (method) component `StandaloneConfig.from_yaml_str [method]` (`cd9bf7e3-f931-5f61-9904-6ced0a386b4a`) lines 77-85 [crates/gcore/src/provisioning/mod.rs:77-85]
  - Signature: `pub fn from_yaml_str(contents: &str) -> anyhow::Result<Self> {`
  - Purpose: Parses a YAML string into a flattened 'BTreeMap'-backed 'Self', returning 'Self::default()' for empty or whitespace-only input and propagating parse/flattening errors via 'anyhow::Result'. [crates/gcore/src/provisioning/mod.rs:77-85]
- `StandaloneConfig.write_at` (method) component `StandaloneConfig.write_at [method]` (`7fa37a8d-eb13-5be2-81be-baf81efa9f27`) lines 87-98 [crates/gcore/src/provisioning/mod.rs:87-98]
  - Signature: `pub fn write_at(&self, path: &Path) -> anyhow::Result<()> {`
  - Purpose: Creates any missing parent directories, serializes 'self.values' into a nested 'serde_yaml::Mapping', writes the resulting YAML string to 'path', and returns 'Ok(())' or any I/O/serialization error. [crates/gcore/src/provisioning/mod.rs:87-98]
- `StandaloneConfig.get` (method) component `StandaloneConfig.get [method]` (`119bed32-45c6-5a8b-8310-640afcd38d33`) lines 100-102 [crates/gcore/src/provisioning/mod.rs:100-102]
  - Signature: `pub fn get(&self, key: &str) -> Option<&str> {`
  - Purpose: Returns the stored value for 'key' as an 'Option<&str>' by looking up the 'String' in 'self.values' and mapping it to a string slice with 'String::as_str'. [crates/gcore/src/provisioning/mod.rs:100-102]
- `StandaloneConfig.set` (method) component `StandaloneConfig.set [method]` (`f21affb5-8aab-5672-8df6-e980c928b8c1`) lines 104-106 [crates/gcore/src/provisioning/mod.rs:104-106]
  - Signature: `pub fn set(&mut self, key: impl Into<String>, value: impl Into<String>) {`
  - Purpose: Inserts or updates the given key-value pair in 'self.values' by converting both arguments into 'String' and storing them via 'insert'. [crates/gcore/src/provisioning/mod.rs:104-106]
- `StandaloneConfig.remove` (method) component `StandaloneConfig.remove [method]` (`ea8d9cb4-617c-5d11-ae78-7d5a62f81a55`) lines 108-110 [crates/gcore/src/provisioning/mod.rs:108-110]
  - Signature: `pub fn remove(&mut self, key: &str) {`
  - Purpose: Removes the entry associated with 'key' from 'self.values' by delegating to the underlying map’s 'remove' operation. [crates/gcore/src/provisioning/mod.rs:108-110]
- `StandaloneConfig.values` (method) component `StandaloneConfig.values [method]` (`45520a0c-b9fb-5383-b9e5-d76b1fec7ede`) lines 112-114 [crates/gcore/src/provisioning/mod.rs:112-114]
  - Signature: `pub fn values(&self) -> &BTreeMap<String, String> {`
  - Purpose: Returns an immutable reference to the struct’s internal 'BTreeMap<String, String>' field named 'values'. [crates/gcore/src/provisioning/mod.rs:112-114]
- `StandaloneConfig` (class) component `StandaloneConfig [class]` (`19b7cefa-43a1-5a5a-b137-40f6193495a3`) lines 117-128 [crates/gcore/src/provisioning/mod.rs:117-128]
  - Signature: `impl ConfigSource for StandaloneConfig {`
  - Purpose: 'StandaloneConfig' is a 'ConfigSource' implementation that returns cloned values from an internal map for 'config_value' and resolves environment patterns in 'resolve_value', but explicitly rejects any '$secret:' references with an error because secret lookup requires a daemon-backed config store. [crates/gcore/src/provisioning/mod.rs:117-128]
- `StandaloneConfig.config_value` (method) component `StandaloneConfig.config_value [method]` (`02012a38-ee0b-5a25-841d-e860c20b1997`) lines 118-120 [crates/gcore/src/provisioning/mod.rs:118-120]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Returns a cloned 'String' value from 'self.values' for the given 'key', or 'None' if the key is absent. [crates/gcore/src/provisioning/mod.rs:118-120]
- `StandaloneConfig.resolve_value` (method) component `StandaloneConfig.resolve_value [method]` (`a2d4a263-83ad-56e5-9fd6-5bcd5d14faa0`) lines 122-127 [crates/gcore/src/provisioning/mod.rs:122-127]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Returns the input string with environment-variable patterns resolved via 'resolve_env_pattern', but immediately errors if it contains '$secret:' and otherwise fails if any pattern remains unresolved. [crates/gcore/src/provisioning/mod.rs:122-127]
- `gcore_config_path` (function) component `gcore_config_path [function]` (`d4e2f27a-7a74-5f36-a68e-05f7aac1312e`) lines 130-132 [crates/gcore/src/provisioning/mod.rs:130-132]
  - Signature: `pub fn gcore_config_path(gobby_home: &Path) -> PathBuf {`
  - Purpose: Returns the path to the GCore configuration file by appending 'GCORE_CONFIG_FILENAME' to the provided 'gobby_home' directory. [crates/gcore/src/provisioning/mod.rs:130-132]
- `services_dir` (function) component `services_dir [function]` (`f92f258e-5bed-5927-aaca-0ee3c0ce93bd`) lines 134-136 [crates/gcore/src/provisioning/mod.rs:134-136]
  - Signature: `pub fn services_dir(gobby_home: &Path) -> PathBuf {`
  - Purpose: Returns 'gobby_home' joined with 'SERVICES_DIRNAME' as a 'PathBuf', yielding the services directory path. [crates/gcore/src/provisioning/mod.rs:134-136]
- `compose_file_path` (function) component `compose_file_path [function]` (`1964c870-6a37-573f-9583-1560dcc57bc9`) lines 138-140 [crates/gcore/src/provisioning/mod.rs:138-140]
  - Signature: `pub fn compose_file_path(gobby_home: &Path) -> PathBuf {`
  - Purpose: Returns the compose file path by joining 'COMPOSE_FILENAME' onto the directory path produced by 'services_dir(gobby_home)'. [crates/gcore/src/provisioning/mod.rs:138-140]
- `default_database_url` (function) component `default_database_url [function]` (`100785e8-61c1-56f0-9381-f3a833e8ba46`) lines 142-151 [crates/gcore/src/provisioning/mod.rs:142-151]
  - Signature: `pub fn default_database_url(port: u16) -> String {`
  - Purpose: Returns a PostgreSQL connection URL string for the given 'port', using the default username, password, host, and database constants. [crates/gcore/src/provisioning/mod.rs:142-151]
- `insert_nested_yaml_value` (function) component `insert_nested_yaml_value [function]` (`cce66a54-a2c1-5378-a4e3-f1aef76ddca9`) lines 153-166 [crates/gcore/src/provisioning/mod.rs:153-166]
  - Signature: `fn insert_nested_yaml_value(`
  - Purpose: Parses a dot-delimited 'key' into non-empty path segments and, if any exist, delegates to 'insert_nested_yaml_parts' to insert the string 'value' into the provided mutable YAML mapping, returning any error from that insertion. [crates/gcore/src/provisioning/mod.rs:153-166]
- `insert_nested_yaml_parts` (function) component `insert_nested_yaml_parts [function]` (`f41e7ea1-921f-52b4-a0dc-5013570db309`) lines 168-203 [crates/gcore/src/provisioning/mod.rs:168-203]
  - Signature: `fn insert_nested_yaml_parts(`
  - Purpose: Recursively inserts a dot-delimited key path into a 'serde_yaml::Mapping' as nested YAML mappings ending in a string scalar, while rejecting collisions where the path conflicts with an existing scalar or mapping. [crates/gcore/src/provisioning/mod.rs:168-203]

