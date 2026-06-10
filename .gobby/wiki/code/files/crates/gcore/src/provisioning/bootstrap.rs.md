---
title: crates/gcore/src/provisioning/bootstrap.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/bootstrap.rs
  ranges:
  - 8-15
  - 17-39
  - 18-27
  - 29-38
  - 41-71
  - 73-79
  - 81-134
  - 136-157
  - 159-161
  - 167-172
  - 175-179
  - 182-186
  - 189-194
  - 197-207
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/bootstrap.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Purpose

`crates/gcore/src/provisioning/bootstrap.rs` exposes 14 indexed API symbols.
[crates/gcore/src/provisioning/bootstrap.rs:8-15]
[crates/gcore/src/provisioning/bootstrap.rs:17-39]
[crates/gcore/src/provisioning/bootstrap.rs:18-27]
[crates/gcore/src/provisioning/bootstrap.rs:29-38]
[crates/gcore/src/provisioning/bootstrap.rs:41-71]
[crates/gcore/src/provisioning/bootstrap.rs:73-79]
[crates/gcore/src/provisioning/bootstrap.rs:81-134]
[crates/gcore/src/provisioning/bootstrap.rs:136-157]
[crates/gcore/src/provisioning/bootstrap.rs:159-161]
[crates/gcore/src/provisioning/bootstrap.rs:167-172]
[crates/gcore/src/provisioning/bootstrap.rs:175-179]
[crates/gcore/src/provisioning/bootstrap.rs:182-186]
[crates/gcore/src/provisioning/bootstrap.rs:189-194]
[crates/gcore/src/provisioning/bootstrap.rs:197-207]

## API Symbols

- `EmbeddingBootstrap` (class) component `EmbeddingBootstrap [class]` (`ce7a2576-2387-5908-bd7e-91e53a45cee2`) lines 8-15 [crates/gcore/src/provisioning/bootstrap.rs:8-15]
  - Signature: `pub struct EmbeddingBootstrap {`
  - Purpose: Indexed class `EmbeddingBootstrap` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:8-15]
- `EmbeddingBootstrap` (class) component `EmbeddingBootstrap [class]` (`133e5dd4-9e1c-508d-a82f-729df9762ad2`) lines 17-39 [crates/gcore/src/provisioning/bootstrap.rs:17-39]
  - Signature: `impl EmbeddingBootstrap {`
  - Purpose: Indexed class `EmbeddingBootstrap` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:17-39]
- `EmbeddingBootstrap.lm_studio` (method) component `EmbeddingBootstrap.lm_studio [method]` (`d1bb0d95-437a-5706-bf65-662048c0daad`) lines 18-27 [crates/gcore/src/provisioning/bootstrap.rs:18-27]
  - Signature: `pub fn lm_studio() -> Self {`
  - Purpose: Indexed method `EmbeddingBootstrap.lm_studio` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:18-27]
- `EmbeddingBootstrap.ollama` (method) component `EmbeddingBootstrap.ollama [method]` (`aee67858-80b9-56dc-ba8d-328a24fdeedd`) lines 29-38 [crates/gcore/src/provisioning/bootstrap.rs:29-38]
  - Signature: `pub fn ollama() -> Self {`
  - Purpose: Indexed method `EmbeddingBootstrap.ollama` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:29-38]
- `write_standalone_bootstrap` (function) component `write_standalone_bootstrap [function]` (`ebfc045b-4665-5ba1-91e4-778295c338e2`) lines 41-71 [crates/gcore/src/provisioning/bootstrap.rs:41-71]
  - Signature: `pub fn write_standalone_bootstrap(`
  - Purpose: Indexed function `write_standalone_bootstrap` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:41-71]
- `flatten_yaml_value` (function) component `flatten_yaml_value [function]` (`1ccefbb2-ca3c-5ca6-833d-c98a19282c95`) lines 73-79 [crates/gcore/src/provisioning/bootstrap.rs:73-79]
  - Signature: `pub(crate) fn flatten_yaml_value(`
  - Purpose: Indexed function `flatten_yaml_value` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:73-79]
- `flatten_yaml_value_at_depth` (function) component `flatten_yaml_value_at_depth [function]` (`a1348283-dc8a-59cf-9288-0522b82186be`) lines 81-134 [crates/gcore/src/provisioning/bootstrap.rs:81-134]
  - Signature: `fn flatten_yaml_value_at_depth(`
  - Purpose: Indexed function `flatten_yaml_value_at_depth` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:81-134]
- `scalar_to_string` (function) component `scalar_to_string [function]` (`44bb07b6-d8c5-5ede-9be5-5e625897bfc0`) lines 136-157 [crates/gcore/src/provisioning/bootstrap.rs:136-157]
  - Signature: `fn scalar_to_string(path: &str, value: &serde_yaml::Value) -> anyhow::Result<Option<String>> {`
  - Purpose: Indexed function `scalar_to_string` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:136-157]
- `yaml_path` (function) component `yaml_path [function]` (`24805972-4d28-5219-9f55-874ee066e02d`) lines 159-161 [crates/gcore/src/provisioning/bootstrap.rs:159-161]
  - Signature: `fn yaml_path(prefix: Option<&str>) -> &str {`
  - Purpose: Indexed function `yaml_path` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:159-161]
- `flatten` (function) component `flatten [function]` (`3ccfc221-2f8d-5fc2-91a7-9cdcf8d11205`) lines 167-172 [crates/gcore/src/provisioning/bootstrap.rs:167-172]
  - Signature: `fn flatten(contents: &str) -> anyhow::Result<BTreeMap<String, String>> {`
  - Purpose: Indexed function `flatten` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:167-172]
- `flatten_yaml_errors_include_root_path` (function) component `flatten_yaml_errors_include_root_path [function]` (`2ae59e9c-e6ed-5cc1-9ce8-a68a1f32b04d`) lines 175-179 [crates/gcore/src/provisioning/bootstrap.rs:175-179]
  - Signature: `fn flatten_yaml_errors_include_root_path() {`
  - Purpose: Indexed function `flatten_yaml_errors_include_root_path` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:175-179]
- `flatten_yaml_errors_include_mapping_path_for_non_string_keys` (function) component `flatten_yaml_errors_include_mapping_path_for_non_string_keys [function]` (`8432da91-dbad-578c-a4fc-57321bab0941`) lines 182-186 [crates/gcore/src/provisioning/bootstrap.rs:182-186]
  - Signature: `fn flatten_yaml_errors_include_mapping_path_for_non_string_keys() {`
  - Purpose: Indexed function `flatten_yaml_errors_include_mapping_path_for_non_string_keys` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:182-186]
- `flatten_yaml_errors_include_scalar_path` (function) component `flatten_yaml_errors_include_scalar_path [function]` (`7b896b56-2854-5931-abec-22ddb683f82f`) lines 189-194 [crates/gcore/src/provisioning/bootstrap.rs:189-194]
  - Signature: `fn flatten_yaml_errors_include_scalar_path() {`
  - Purpose: Indexed function `flatten_yaml_errors_include_scalar_path` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:189-194]
- `flatten_yaml_depth_errors_include_current_path` (function) component `flatten_yaml_depth_errors_include_current_path [function]` (`169802bc-2973-56aa-bed5-90b6c77c4103`) lines 197-207 [crates/gcore/src/provisioning/bootstrap.rs:197-207]
  - Signature: `fn flatten_yaml_depth_errors_include_current_path() {`
  - Purpose: Indexed function `flatten_yaml_depth_errors_include_current_path` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:197-207]

