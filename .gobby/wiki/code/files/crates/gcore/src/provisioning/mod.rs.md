---
title: crates/gcore/src/provisioning/mod.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/mod.rs
  ranges:
  - 53-55
  - 57-115
  - 58-60
  - 62-64
  - 66-75
  - 77-85
  - 87-98
  - 100-102
  - 104-106
  - 108-110
  - 112-114
  - 117-128
  - 118-120
  - 122-127
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

`crates/gcore/src/provisioning/mod.rs` exposes 20 indexed API symbols.
[crates/gcore/src/provisioning/mod.rs:53-55]
[crates/gcore/src/provisioning/mod.rs:57-115]
[crates/gcore/src/provisioning/mod.rs:58-60]
[crates/gcore/src/provisioning/mod.rs:62-64]
[crates/gcore/src/provisioning/mod.rs:66-75]

## API Symbols

- `StandaloneConfig` (class) component `StandaloneConfig [class]` (`802640ac-0e89-5daa-a220-3a04d2f0db1b`) lines 53-55 [crates/gcore/src/provisioning/mod.rs:53-55]
  - Signature: `pub struct StandaloneConfig {`
  - Purpose: Indexed class `StandaloneConfig` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:53-55]
- `StandaloneConfig` (class) component `StandaloneConfig [class]` (`89374ad3-9649-53cd-8fcb-fd84a891d058`) lines 57-115 [crates/gcore/src/provisioning/mod.rs:57-115]
  - Signature: `impl StandaloneConfig {`
  - Purpose: Indexed class `StandaloneConfig` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:57-115]
- `StandaloneConfig.new` (method) component `StandaloneConfig.new [method]` (`30681f49-c1c0-561e-a4dd-1b17ca4a8c53`) lines 58-60 [crates/gcore/src/provisioning/mod.rs:58-60]
  - Signature: `pub fn new(values: BTreeMap<String, String>) -> Self {`
  - Purpose: Indexed method `StandaloneConfig.new` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:58-60]
- `StandaloneConfig.empty` (method) component `StandaloneConfig.empty [method]` (`1e3dd01d-7223-5091-a7c1-76ef5be762e1`) lines 62-64 [crates/gcore/src/provisioning/mod.rs:62-64]
  - Signature: `pub fn empty() -> Self {`
  - Purpose: Indexed method `StandaloneConfig.empty` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:62-64]
- `StandaloneConfig.read_at` (method) component `StandaloneConfig.read_at [method]` (`7f881cf6-e384-552c-abd8-6cd0cc741b9a`) lines 66-75 [crates/gcore/src/provisioning/mod.rs:66-75]
  - Signature: `pub fn read_at(path: &Path) -> anyhow::Result<Option<Self>> {`
  - Purpose: Indexed method `StandaloneConfig.read_at` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:66-75]
- `StandaloneConfig.from_yaml_str` (method) component `StandaloneConfig.from_yaml_str [method]` (`cd9bf7e3-f931-5f61-9904-6ced0a386b4a`) lines 77-85 [crates/gcore/src/provisioning/mod.rs:77-85]
  - Signature: `pub fn from_yaml_str(contents: &str) -> anyhow::Result<Self> {`
  - Purpose: Indexed method `StandaloneConfig.from_yaml_str` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:77-85]
- `StandaloneConfig.write_at` (method) component `StandaloneConfig.write_at [method]` (`7fa37a8d-eb13-5be2-81be-baf81efa9f27`) lines 87-98 [crates/gcore/src/provisioning/mod.rs:87-98]
  - Signature: `pub fn write_at(&self, path: &Path) -> anyhow::Result<()> {`
  - Purpose: Indexed method `StandaloneConfig.write_at` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:87-98]
- `StandaloneConfig.get` (method) component `StandaloneConfig.get [method]` (`119bed32-45c6-5a8b-8310-640afcd38d33`) lines 100-102 [crates/gcore/src/provisioning/mod.rs:100-102]
  - Signature: `pub fn get(&self, key: &str) -> Option<&str> {`
  - Purpose: Indexed method `StandaloneConfig.get` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:100-102]
- `StandaloneConfig.set` (method) component `StandaloneConfig.set [method]` (`f21affb5-8aab-5672-8df6-e980c928b8c1`) lines 104-106 [crates/gcore/src/provisioning/mod.rs:104-106]
  - Signature: `pub fn set(&mut self, key: impl Into<String>, value: impl Into<String>) {`
  - Purpose: Indexed method `StandaloneConfig.set` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:104-106]
- `StandaloneConfig.remove` (method) component `StandaloneConfig.remove [method]` (`ea8d9cb4-617c-5d11-ae78-7d5a62f81a55`) lines 108-110 [crates/gcore/src/provisioning/mod.rs:108-110]
  - Signature: `pub fn remove(&mut self, key: &str) {`
  - Purpose: Indexed method `StandaloneConfig.remove` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:108-110]
- `StandaloneConfig.values` (method) component `StandaloneConfig.values [method]` (`45520a0c-b9fb-5383-b9e5-d76b1fec7ede`) lines 112-114 [crates/gcore/src/provisioning/mod.rs:112-114]
  - Signature: `pub fn values(&self) -> &BTreeMap<String, String> {`
  - Purpose: Indexed method `StandaloneConfig.values` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:112-114]
- `StandaloneConfig` (class) component `StandaloneConfig [class]` (`19b7cefa-43a1-5a5a-b137-40f6193495a3`) lines 117-128 [crates/gcore/src/provisioning/mod.rs:117-128]
  - Signature: `impl ConfigSource for StandaloneConfig {`
  - Purpose: Indexed class `StandaloneConfig` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:117-128]
- `StandaloneConfig.config_value` (method) component `StandaloneConfig.config_value [method]` (`02012a38-ee0b-5a25-841d-e860c20b1997`) lines 118-120 [crates/gcore/src/provisioning/mod.rs:118-120]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed method `StandaloneConfig.config_value` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:118-120]
- `StandaloneConfig.resolve_value` (method) component `StandaloneConfig.resolve_value [method]` (`a2d4a263-83ad-56e5-9fd6-5bcd5d14faa0`) lines 122-127 [crates/gcore/src/provisioning/mod.rs:122-127]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `StandaloneConfig.resolve_value` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:122-127]
- `gcore_config_path` (function) component `gcore_config_path [function]` (`d4e2f27a-7a74-5f36-a68e-05f7aac1312e`) lines 130-132 [crates/gcore/src/provisioning/mod.rs:130-132]
  - Signature: `pub fn gcore_config_path(gobby_home: &Path) -> PathBuf {`
  - Purpose: Indexed function `gcore_config_path` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:130-132]
- `services_dir` (function) component `services_dir [function]` (`f92f258e-5bed-5927-aaca-0ee3c0ce93bd`) lines 134-136 [crates/gcore/src/provisioning/mod.rs:134-136]
  - Signature: `pub fn services_dir(gobby_home: &Path) -> PathBuf {`
  - Purpose: Indexed function `services_dir` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:134-136]
- `compose_file_path` (function) component `compose_file_path [function]` (`1964c870-6a37-573f-9583-1560dcc57bc9`) lines 138-140 [crates/gcore/src/provisioning/mod.rs:138-140]
  - Signature: `pub fn compose_file_path(gobby_home: &Path) -> PathBuf {`
  - Purpose: Indexed function `compose_file_path` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:138-140]
- `default_database_url` (function) component `default_database_url [function]` (`100785e8-61c1-56f0-9381-f3a833e8ba46`) lines 142-151 [crates/gcore/src/provisioning/mod.rs:142-151]
  - Signature: `pub fn default_database_url(port: u16) -> String {`
  - Purpose: Indexed function `default_database_url` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:142-151]
- `insert_nested_yaml_value` (function) component `insert_nested_yaml_value [function]` (`cce66a54-a2c1-5378-a4e3-f1aef76ddca9`) lines 153-166 [crates/gcore/src/provisioning/mod.rs:153-166]
  - Signature: `fn insert_nested_yaml_value(`
  - Purpose: Indexed function `insert_nested_yaml_value` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:153-166]
- `insert_nested_yaml_parts` (function) component `insert_nested_yaml_parts [function]` (`f41e7ea1-921f-52b4-a0dc-5013570db309`) lines 168-203 [crates/gcore/src/provisioning/mod.rs:168-203]
  - Signature: `fn insert_nested_yaml_parts(`
  - Purpose: Indexed function `insert_nested_yaml_parts` in `crates/gcore/src/provisioning/mod.rs`. [crates/gcore/src/provisioning/mod.rs:168-203]

