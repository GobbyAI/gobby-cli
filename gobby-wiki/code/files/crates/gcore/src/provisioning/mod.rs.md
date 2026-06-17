---
title: crates/gcore/src/provisioning/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/mod.rs
  ranges:
  - 55-57
  - 60-62
  - 64-66
  - 68-77
  - 79-89
  - 91-102
  - 104-106
  - 108-110
  - 112-114
  - 116-118
  - 120-133
  - 137-139
  - 141-146
  - 149-151
  - 153-155
  - 157-159
  - 161-170
  - 172-185
  - 187-222
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/provisioning/mod.rs:55-57](crates/gcore/src/provisioning/mod.rs#L55-L57), [crates/gcore/src/provisioning/mod.rs:60-62](crates/gcore/src/provisioning/mod.rs#L60-L62), [crates/gcore/src/provisioning/mod.rs:64-66](crates/gcore/src/provisioning/mod.rs#L64-L66), [crates/gcore/src/provisioning/mod.rs:68-77](crates/gcore/src/provisioning/mod.rs#L68-L77), [crates/gcore/src/provisioning/mod.rs:79-89](crates/gcore/src/provisioning/mod.rs#L79-L89), [crates/gcore/src/provisioning/mod.rs:91-102](crates/gcore/src/provisioning/mod.rs#L91-L102), [crates/gcore/src/provisioning/mod.rs:104-106](crates/gcore/src/provisioning/mod.rs#L104-L106), [crates/gcore/src/provisioning/mod.rs:108-110](crates/gcore/src/provisioning/mod.rs#L108-L110), [crates/gcore/src/provisioning/mod.rs:112-114](crates/gcore/src/provisioning/mod.rs#L112-L114), [crates/gcore/src/provisioning/mod.rs:116-118](crates/gcore/src/provisioning/mod.rs#L116-L118), [crates/gcore/src/provisioning/mod.rs:120-133](crates/gcore/src/provisioning/mod.rs#L120-L133), [crates/gcore/src/provisioning/mod.rs:137-139](crates/gcore/src/provisioning/mod.rs#L137-L139), [crates/gcore/src/provisioning/mod.rs:141-146](crates/gcore/src/provisioning/mod.rs#L141-L146), [crates/gcore/src/provisioning/mod.rs:149-151](crates/gcore/src/provisioning/mod.rs#L149-L151), [crates/gcore/src/provisioning/mod.rs:153-155](crates/gcore/src/provisioning/mod.rs#L153-L155), [crates/gcore/src/provisioning/mod.rs:157-159](crates/gcore/src/provisioning/mod.rs#L157-L159), [crates/gcore/src/provisioning/mod.rs:161-170](crates/gcore/src/provisioning/mod.rs#L161-L170), [crates/gcore/src/provisioning/mod.rs:172-185](crates/gcore/src/provisioning/mod.rs#L172-L185), [crates/gcore/src/provisioning/mod.rs:187-222](crates/gcore/src/provisioning/mod.rs#L187-L222)

</details>

# crates/gcore/src/provisioning/mod.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Provides standalone bootstrap and Docker service provisioning for `gcore`, centered on copying bundled service assets into `~/.gobby/services` and persisting daemon-style settings in `gcore.yaml`. `StandaloneConfig` wraps that config state with constructors, file read/write helpers, YAML parsing, key/value accessors, and a special update path that applies text-generation defaults from embedding settings. The free functions supply the standard config and service paths, build the default database URL, and insert nested YAML values so provisioning logic can assemble and update structured config data consistently.
[crates/gcore/src/provisioning/mod.rs:55-57]
[crates/gcore/src/provisioning/mod.rs:60-62]
[crates/gcore/src/provisioning/mod.rs:64-66]
[crates/gcore/src/provisioning/mod.rs:68-77]
[crates/gcore/src/provisioning/mod.rs:79-89]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `StandaloneConfig` | class | `pub struct StandaloneConfig {` | `StandaloneConfig [class]` | `a0607131-a365-5f06-ab8a-d138c5055b4b` | 55-57 [crates/gcore/src/provisioning/mod.rs:55-57] | Indexed class `StandaloneConfig` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:55-57] |
| `StandaloneConfig::new` | method | `pub fn new(values: BTreeMap<String, String>) -> Self {` | `StandaloneConfig::new [method]` | `65585fb5-9f10-5c87-91df-0a6f217dcad7` | 60-62 [crates/gcore/src/provisioning/mod.rs:60-62] | Indexed method `StandaloneConfig::new` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:60-62] |
| `StandaloneConfig::empty` | method | `pub fn empty() -> Self {` | `StandaloneConfig::empty [method]` | `ff543b6e-a0eb-55aa-9f38-7566951463d5` | 64-66 [crates/gcore/src/provisioning/mod.rs:64-66] | Indexed method `StandaloneConfig::empty` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:64-66] |
| `StandaloneConfig::read_at` | method | `pub fn read_at(path: &Path) -> anyhow::Result<Option<Self>> {` | `StandaloneConfig::read_at [method]` | `db4c24ce-5fd7-59be-8592-24476f6c0434` | 68-77 [crates/gcore/src/provisioning/mod.rs:68-77] | Indexed method `StandaloneConfig::read_at` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:68-77] |
| `StandaloneConfig::from_yaml_str` | method | `pub fn from_yaml_str(contents: &str) -> anyhow::Result<Self> {` | `StandaloneConfig::from_yaml_str [method]` | `11b08b3d-92ab-5b36-97fb-64a74e5df39b` | 79-89 [crates/gcore/src/provisioning/mod.rs:79-89] | Indexed method `StandaloneConfig::from_yaml_str` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:79-89] |
| `StandaloneConfig::write_at` | method | `pub fn write_at(&self, path: &Path) -> anyhow::Result<()> {` | `StandaloneConfig::write_at [method]` | `3ecb396d-3d64-5afa-9c40-9b8002853bd8` | 91-102 [crates/gcore/src/provisioning/mod.rs:91-102] | Indexed method `StandaloneConfig::write_at` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:91-102] |
| `StandaloneConfig::get` | method | `pub fn get(&self, key: &str) -> Option<&str> {` | `StandaloneConfig::get [method]` | `8fff3320-e477-5792-8957-f0af72db7790` | 104-106 [crates/gcore/src/provisioning/mod.rs:104-106] | Indexed method `StandaloneConfig::get` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:104-106] |
| `StandaloneConfig::set` | method | `pub fn set(&mut self, key: impl Into<String>, value: impl Into<String>) {` | `StandaloneConfig::set [method]` | `bb38d549-c751-590c-8444-f59da9a587ba` | 108-110 [crates/gcore/src/provisioning/mod.rs:108-110] | Indexed method `StandaloneConfig::set` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:108-110] |
| `StandaloneConfig::remove` | method | `pub fn remove(&mut self, key: &str) {` | `StandaloneConfig::remove [method]` | `89646a77-31bf-59a8-a77e-250dfd226d7b` | 112-114 [crates/gcore/src/provisioning/mod.rs:112-114] | Indexed method `StandaloneConfig::remove` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:112-114] |
| `StandaloneConfig::values` | method | `pub fn values(&self) -> &BTreeMap<String, String> {` | `StandaloneConfig::values [method]` | `a163a57b-86e9-57c7-90b1-165df0ac1dcf` | 116-118 [crates/gcore/src/provisioning/mod.rs:116-118] | Indexed method `StandaloneConfig::values` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:116-118] |
| `StandaloneConfig::apply_text_generation_defaults_from_embeddings` | method | `fn apply_text_generation_defaults_from_embeddings(&mut self) {` | `StandaloneConfig::apply_text_generation_defaults_from_embeddings [method]` | `ebc76215-63fe-5bac-8305-a54d67e2e04a` | 120-133 [crates/gcore/src/provisioning/mod.rs:120-133] | Indexed method `StandaloneConfig::apply_text_generation_defaults_from_embeddings` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:120-133] |
| `StandaloneConfig::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `StandaloneConfig::config_value [method]` | `e5131f1c-aa2a-5673-a766-750764ee714c` | 137-139 [crates/gcore/src/provisioning/mod.rs:137-139] | Indexed method `StandaloneConfig::config_value` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:137-139] |
| `StandaloneConfig::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `StandaloneConfig::resolve_value [method]` | `ea60950a-c336-5a6a-a12c-e0eee1d03341` | 141-146 [crates/gcore/src/provisioning/mod.rs:141-146] | Indexed method `StandaloneConfig::resolve_value` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:141-146] |
| `gcore_config_path` | function | `pub fn gcore_config_path(gobby_home: &Path) -> PathBuf {` | `gcore_config_path [function]` | `31cb9cc9-8f97-5c8d-84ce-1b14637e0a2f` | 149-151 [crates/gcore/src/provisioning/mod.rs:149-151] | Indexed function `gcore_config_path` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:149-151] |
| `services_dir` | function | `pub fn services_dir(gobby_home: &Path) -> PathBuf {` | `services_dir [function]` | `a6083a33-b44a-5cf9-a694-a7f4879379ba` | 153-155 [crates/gcore/src/provisioning/mod.rs:153-155] | Indexed function `services_dir` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:153-155] |
| `compose_file_path` | function | `pub fn compose_file_path(gobby_home: &Path) -> PathBuf {` | `compose_file_path [function]` | `9f5d1dd9-b76e-5af2-adbb-706b90d843f5` | 157-159 [crates/gcore/src/provisioning/mod.rs:157-159] | Indexed function `compose_file_path` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:157-159] |
| `default_database_url` | function | `pub fn default_database_url(port: u16) -> String {` | `default_database_url [function]` | `d8ccdfc9-92a8-51de-a022-0362fcd0d464` | 161-170 [crates/gcore/src/provisioning/mod.rs:161-170] | Indexed function `default_database_url` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:161-170] |
| `insert_nested_yaml_value` | function | `fn insert_nested_yaml_value(` | `insert_nested_yaml_value [function]` | `d9c570f9-dd8b-5168-af50-60327638cba4` | 172-185 [crates/gcore/src/provisioning/mod.rs:172-185] | Indexed function `insert_nested_yaml_value` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:172-185] |
| `insert_nested_yaml_parts` | function | `fn insert_nested_yaml_parts(` | `insert_nested_yaml_parts [function]` | `5d86c38b-6505-5d89-822d-8a6eb0eb8a49` | 187-222 [crates/gcore/src/provisioning/mod.rs:187-222] | Indexed function `insert_nested_yaml_parts` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:187-222] |
