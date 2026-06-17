---
title: crates/gcore/src/provisioning/bootstrap.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/bootstrap.rs
  ranges:
  - 8-15
  - 18-22
  - 25-34
  - 36-45
  - 49-55
  - 57-68
  - 71-85
  - 87-97
  - 99-133
  - 135-141
  - 143-196
  - 198-219
  - 221-223
  - 229-234
  - 237-241
  - 244-248
  - 251-256
  - 259-269
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/provisioning/bootstrap.rs:8-15](crates/gcore/src/provisioning/bootstrap.rs#L8-L15), [crates/gcore/src/provisioning/bootstrap.rs:18-22](crates/gcore/src/provisioning/bootstrap.rs#L18-L22), [crates/gcore/src/provisioning/bootstrap.rs:25-34](crates/gcore/src/provisioning/bootstrap.rs#L25-L34), [crates/gcore/src/provisioning/bootstrap.rs:36-45](crates/gcore/src/provisioning/bootstrap.rs#L36-L45), [crates/gcore/src/provisioning/bootstrap.rs:49-55](crates/gcore/src/provisioning/bootstrap.rs#L49-L55), [crates/gcore/src/provisioning/bootstrap.rs:57-68](crates/gcore/src/provisioning/bootstrap.rs#L57-L68), [crates/gcore/src/provisioning/bootstrap.rs:71-85](crates/gcore/src/provisioning/bootstrap.rs#L71-L85), [crates/gcore/src/provisioning/bootstrap.rs:87-97](crates/gcore/src/provisioning/bootstrap.rs#L87-L97), [crates/gcore/src/provisioning/bootstrap.rs:99-133](crates/gcore/src/provisioning/bootstrap.rs#L99-L133), [crates/gcore/src/provisioning/bootstrap.rs:135-141](crates/gcore/src/provisioning/bootstrap.rs#L135-L141), [crates/gcore/src/provisioning/bootstrap.rs:143-196](crates/gcore/src/provisioning/bootstrap.rs#L143-L196), [crates/gcore/src/provisioning/bootstrap.rs:198-219](crates/gcore/src/provisioning/bootstrap.rs#L198-L219), [crates/gcore/src/provisioning/bootstrap.rs:221-223](crates/gcore/src/provisioning/bootstrap.rs#L221-L223), [crates/gcore/src/provisioning/bootstrap.rs:229-234](crates/gcore/src/provisioning/bootstrap.rs#L229-L234), [crates/gcore/src/provisioning/bootstrap.rs:237-241](crates/gcore/src/provisioning/bootstrap.rs#L237-L241), [crates/gcore/src/provisioning/bootstrap.rs:244-248](crates/gcore/src/provisioning/bootstrap.rs#L244-L248), [crates/gcore/src/provisioning/bootstrap.rs:251-256](crates/gcore/src/provisioning/bootstrap.rs#L251-L256), [crates/gcore/src/provisioning/bootstrap.rs:259-269](crates/gcore/src/provisioning/bootstrap.rs#L259-L269)

</details>

# crates/gcore/src/provisioning/bootstrap.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Purpose

Defines bootstrap data and helpers for provisioning AI configuration. `EmbeddingBootstrap` supplies preset embedding setups for LM Studio and Ollama, `TextGenerationBootstrap` derives text-generation settings from an embedding or arbitrary endpoint, `apply_text_generation_bootstrap` writes those settings into a `StandaloneConfig`, and `write_standalone_bootstrap` plus the YAML-flattening helpers convert nested bootstrap YAML into flat config entries while preserving useful path information in validation errors.
[crates/gcore/src/provisioning/bootstrap.rs:8-15]
[crates/gcore/src/provisioning/bootstrap.rs:18-22]
[crates/gcore/src/provisioning/bootstrap.rs:25-34]
[crates/gcore/src/provisioning/bootstrap.rs:36-45]
[crates/gcore/src/provisioning/bootstrap.rs:49-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `EmbeddingBootstrap` | class | `pub struct EmbeddingBootstrap {` | `EmbeddingBootstrap [class]` | `ce7a2576-2387-5908-bd7e-91e53a45cee2` | 8-15 [crates/gcore/src/provisioning/bootstrap.rs:8-15] | Indexed class `EmbeddingBootstrap` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:8-15] |
| `TextGenerationBootstrap` | class | `pub struct TextGenerationBootstrap {` | `TextGenerationBootstrap [class]` | `d060d72b-38e6-5bc8-88b0-4f87949e5511` | 18-22 [crates/gcore/src/provisioning/bootstrap.rs:18-22] | Indexed class `TextGenerationBootstrap` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:18-22] |
| `EmbeddingBootstrap::lm_studio` | method | `pub fn lm_studio() -> Self {` | `EmbeddingBootstrap::lm_studio [method]` | `3b2b4cfa-bc8d-5435-8b72-423d832d93ed` | 25-34 [crates/gcore/src/provisioning/bootstrap.rs:25-34] | Indexed method `EmbeddingBootstrap::lm_studio` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:25-34] |
| `EmbeddingBootstrap::ollama` | method | `pub fn ollama() -> Self {` | `EmbeddingBootstrap::ollama [method]` | `33e026e7-623e-5de6-bfe1-6ac60cd55ffc` | 36-45 [crates/gcore/src/provisioning/bootstrap.rs:36-45] | Indexed method `EmbeddingBootstrap::ollama` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:36-45] |
| `TextGenerationBootstrap::from_embedding` | method | `pub fn from_embedding(embedding: &EmbeddingBootstrap) -> Self {` | `TextGenerationBootstrap::from_embedding [method]` | `8b53e6bd-0059-5964-a443-b4459e0373d6` | 49-55 [crates/gcore/src/provisioning/bootstrap.rs:49-55] | Indexed method `TextGenerationBootstrap::from_embedding` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:49-55] |
| `TextGenerationBootstrap::from_endpoint` | method | `pub fn from_endpoint(` | `TextGenerationBootstrap::from_endpoint [method]` | `2798215e-e3b3-5124-8c36-1966f62bb077` | 57-68 [crates/gcore/src/provisioning/bootstrap.rs:57-68] | Indexed method `TextGenerationBootstrap::from_endpoint` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:57-68] |
| `apply_text_generation_bootstrap` | function | `pub fn apply_text_generation_bootstrap(` | `apply_text_generation_bootstrap [function]` | `c78d15b5-3bb6-5168-9f2f-868608470093` | 71-85 [crates/gcore/src/provisioning/bootstrap.rs:71-85] | Indexed function `apply_text_generation_bootstrap` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:71-85] |
| `default_text_model` | function | `fn default_text_model(provider: Option<&str>, api_base: &str) -> &'static str {` | `default_text_model [function]` | `5faa0702-011f-5c72-87b2-d0a210ee6cb9` | 87-97 [crates/gcore/src/provisioning/bootstrap.rs:87-97] | Indexed function `default_text_model` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:87-97] |
| `write_standalone_bootstrap` | function | `pub fn write_standalone_bootstrap(` | `write_standalone_bootstrap [function]` | `eae0e93a-5077-5b83-8a37-0b67881a3c4d` | 99-133 [crates/gcore/src/provisioning/bootstrap.rs:99-133] | Indexed function `write_standalone_bootstrap` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:99-133] |
| `flatten_yaml_value` | function | `pub(crate) fn flatten_yaml_value(` | `flatten_yaml_value [function]` | `cab97bb3-e9f9-5bd2-a4fe-164ff31d2782` | 135-141 [crates/gcore/src/provisioning/bootstrap.rs:135-141] | Indexed function `flatten_yaml_value` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:135-141] |
| `flatten_yaml_value_at_depth` | function | `fn flatten_yaml_value_at_depth(` | `flatten_yaml_value_at_depth [function]` | `51b1cf3d-a694-5c92-adae-d92c66f97315` | 143-196 [crates/gcore/src/provisioning/bootstrap.rs:143-196] | Indexed function `flatten_yaml_value_at_depth` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:143-196] |
| `scalar_to_string` | function | `fn scalar_to_string(path: &str, value: &serde_yaml::Value) -> anyhow::Result<Option<String>> {` | `scalar_to_string [function]` | `b936ccd1-f7ce-50d4-b28b-cdcb8910ec59` | 198-219 [crates/gcore/src/provisioning/bootstrap.rs:198-219] | Indexed function `scalar_to_string` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:198-219] |
| `yaml_path` | function | `fn yaml_path(prefix: Option<&str>) -> &str {` | `yaml_path [function]` | `04cb477e-cdae-557e-b65b-cadfa7a2f53a` | 221-223 [crates/gcore/src/provisioning/bootstrap.rs:221-223] | Indexed function `yaml_path` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:221-223] |
| `flatten` | function | `fn flatten(contents: &str) -> anyhow::Result<BTreeMap<String, String>> {` | `flatten [function]` | `4d4f4739-aa84-5448-9878-be168c14f0ff` | 229-234 [crates/gcore/src/provisioning/bootstrap.rs:229-234] | Indexed function `flatten` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:229-234] |
| `flatten_yaml_errors_include_root_path` | function | `fn flatten_yaml_errors_include_root_path() {` | `flatten_yaml_errors_include_root_path [function]` | `94b311d8-e3e8-590e-b869-7cd5379544a5` | 237-241 [crates/gcore/src/provisioning/bootstrap.rs:237-241] | Indexed function `flatten_yaml_errors_include_root_path` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:237-241] |
| `flatten_yaml_errors_include_mapping_path_for_non_string_keys` | function | `fn flatten_yaml_errors_include_mapping_path_for_non_string_keys() {` | `flatten_yaml_errors_include_mapping_path_for_non_string_keys [function]` | `ac64bc11-a2ac-5cd8-beff-1b96cc3c13f1` | 244-248 [crates/gcore/src/provisioning/bootstrap.rs:244-248] | Indexed function `flatten_yaml_errors_include_mapping_path_for_non_string_keys` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:244-248] |
| `flatten_yaml_errors_include_scalar_path` | function | `fn flatten_yaml_errors_include_scalar_path() {` | `flatten_yaml_errors_include_scalar_path [function]` | `abe6ce4c-0db9-56bd-b59b-7c4a26ca84b8` | 251-256 [crates/gcore/src/provisioning/bootstrap.rs:251-256] | Indexed function `flatten_yaml_errors_include_scalar_path` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:251-256] |
| `flatten_yaml_depth_errors_include_current_path` | function | `fn flatten_yaml_depth_errors_include_current_path() {` | `flatten_yaml_depth_errors_include_current_path [function]` | `f420cd1f-9833-5523-b9de-8bf095519973` | 259-269 [crates/gcore/src/provisioning/bootstrap.rs:259-269] | Indexed function `flatten_yaml_depth_errors_include_current_path` in `crates/gcore/src/provisioning/bootstrap.rs`. [crates/gcore/src/provisioning/bootstrap.rs:259-269] |
