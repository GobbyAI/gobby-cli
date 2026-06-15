---
title: crates/gsqz/src/config.rs
type: code_file
provenance:
- file: crates/gsqz/src/config.rs
  ranges:
  - 26-35
  - 38-47
  - 49-58
  - 60-62
  - 64-66
  - 69-76
  - 79-87
  - 91-166
  - 169-172
  - 175-177
  - 180-189
  - 191-193
  - 195-197
  - '200'
  - 203-205
  - 208-211
  - 214-216
  - 219-224
  - 227-230
  - 232-234
  - 237-240
  - 242-248
  - 250-257
  - 259-326
  - 333-338
  - 341-345
  - 348-353
  - 356-359
  - 362-368
  - 371-374
  - 377-381
  - 384-388
  - 391-398
  - 401-408
  - 411-423
  - 426-436
  - 439-443
  - 446-457
  - 460-473
  - 476-480
  - 483-490
  - 493-503
  - 506-513
  - 516-526
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/config.rs

Module: [[code/modules/crates/gsqz/src|crates/gsqz/src]]

## Purpose

Defines the gsqz configuration schema and its serde behavior. The file ties together top-level `Config`, `Settings`, `Pipeline`, and `Step` types, supplies defaults for output sizing and fallback truncation, and implements custom step deserialization from single-key YAML maps into the appropriate operation-specific argument structs.
[crates/gsqz/src/config.rs:26-35]
[crates/gsqz/src/config.rs:38-47]
[crates/gsqz/src/config.rs:49-58]
[crates/gsqz/src/config.rs:50-57]
[crates/gsqz/src/config.rs:60-62]

## API Symbols

- `Config` (class) component `Config [class]` (`97e782d0-91b2-5fc2-b9e5-b17b655dd84d`) lines 26-35 [crates/gsqz/src/config.rs:26-35]
  - Signature: `pub struct Config {`
  - Purpose: `Config` is a serde-deserializable struct that aggregates application settings, a sorted map of named pipelines, fallback behavior configuration, and a list of excluded commands. [crates/gsqz/src/config.rs:26-35]
- `Settings` (class) component `Settings [class]` (`c99f5df8-5e38-5b4f-909b-63b22890e986`) lines 38-47 [crates/gsqz/src/config.rs:38-47]
  - Signature: `pub struct Settings {`
  - Purpose: Settings is a serde-deserializable configuration struct that defines output compression constraints via minimum/maximum length thresholds and optional daemon endpoint and empty-state handler fields. [crates/gsqz/src/config.rs:38-47]
- `Settings` (class) component `Settings [class]` (`f40bc0b3-9141-515d-99a6-24b2a8e5f706`) lines 49-58 [crates/gsqz/src/config.rs:49-58]
  - Signature: `impl Default for Settings {`
  - Purpose: This is a `Default` trait implementation for `Settings` that initializes configuration fields with default values: two derived from helper functions (`min_output_length` and `max_compressed_lines`) and two as `None` options (`daemon_url` and `on_empty`). [crates/gsqz/src/config.rs:49-58]
- `Settings.default` (method) component `Settings.default [method]` (`61e2caff-30a4-5d81-a921-9ffb808d6a6d`) lines 50-57 [crates/gsqz/src/config.rs:50-57]
  - Signature: `fn default() -> Self {`
  - Purpose: Constructs a default instance of the struct by initializing numeric configuration parameters via helper functions and setting optional fields to `None`. [crates/gsqz/src/config.rs:50-57]
- `default_min_output_length` (function) component `default_min_output_length [function]` (`d49a5c68-e3dc-538a-a368-f5567051b11a`) lines 60-62 [crates/gsqz/src/config.rs:60-62]
  - Signature: `fn default_min_output_length() -> usize {`
  - Purpose: This function returns a `usize` constant of 1000 as the default minimum output length. [crates/gsqz/src/config.rs:60-62]
- `default_max_compressed_lines` (function) component `default_max_compressed_lines [function]` (`8a691623-f9d1-5a58-bb36-73790de7f69c`) lines 64-66 [crates/gsqz/src/config.rs:64-66]
  - Signature: `fn default_max_compressed_lines() -> usize {`
  - Purpose: This function returns the hardcoded default maximum line count (100) for compressed content. [crates/gsqz/src/config.rs:64-66]
- `Pipeline` (class) component `Pipeline [class]` (`1efb3c74-edf7-5ebc-a0b5-88669eac2e96`) lines 69-76 [crates/gsqz/src/config.rs:69-76]
  - Signature: `pub struct Pipeline {`
  - Purpose: `Pipeline` is a serializable struct that matches a pattern and executes a sequence of `Step` items with optional fallback behavior when the steps are empty. [crates/gsqz/src/config.rs:69-76]
- `Step` (type) component `Step [type]` (`8bbf9a80-b14b-52bb-b973-f157dadfbc28`) lines 79-87 [crates/gsqz/src/config.rs:79-87]
  - Signature: `pub enum Step {`
  - Purpose: Indexed type `Step` in `crates/gsqz/src/config.rs`. [crates/gsqz/src/config.rs:79-87]
- `Step` (class) component `Step [class]` (`21c00c1b-e191-54b0-87c0-043b12afe344`) lines 91-166 [crates/gsqz/src/config.rs:91-166]
  - Signature: `impl<'de> Deserialize<'de> for Step {`
  - Purpose: A custom `Deserialize` implementation for the `Step` enum that uses a visitor pattern to parse a single-key map, routing the key name to the corresponding enum variant while deserializing type-specific arguments for each operation. [crates/gsqz/src/config.rs:91-166]
- `Step.deserialize` (method) component `Step.deserialize [method]` (`56149edc-ee35-5f1b-8ace-271999a70383`) lines 92-165 [crates/gsqz/src/config.rs:92-165]
  - Signature: `fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>`
  - Purpose: This method deserializes a single-keyed map into a `Step` enum variant by matching the key against predefined operation names (filter_lines, group_lines, truncate, dedup, replace, match_output, compress_prose) and instantiating the corresponding arguments struct. [crates/gsqz/src/config.rs:92-165]
- `Step.StepVisitor` (class) component `Step.StepVisitor [class]` (`3615d100-7c7a-545a-a5ff-e3338c872984`) lines 96-96 [crates/gsqz/src/config.rs:96]
  - Signature: `struct StepVisitor;`
  - Purpose: `StepVisitor` is an empty unit struct, likely implementing the visitor pattern for traversing or processing step-related data structures. [crates/gsqz/src/config.rs:96]
- `Step.StepVisitor` (class) component `Step.StepVisitor [class]` (`7499f4da-79c2-5ca6-a3e6-0a46b6bcde5e`) lines 98-162 [crates/gsqz/src/config.rs:98-162]
  - Signature: `impl<'de> Visitor<'de> for StepVisitor {`
  - Purpose: A serde `Visitor` implementation that deserializes a single-key map into one of seven `Step` enum variants by dispatching on the key name (filter_lines, group_lines, truncate, dedup, replace, match_output, or compress_prose). [crates/gsqz/src/config.rs:98-162]
- `StepVisitor.Value` (type) component `StepVisitor.Value [type]` (`a66c7e8b-a774-5f5a-8864-bab0e1b98432`) lines 99-99 [crates/gsqz/src/config.rs:99]
  - Signature: `type Value = Step;`
  - Purpose: Indexed type `StepVisitor.Value` in `crates/gsqz/src/config.rs`. [crates/gsqz/src/config.rs:99]
- `StepVisitor.expecting` (method) component `StepVisitor.expecting [method]` (`a4fd98f4-1986-5a02-b40c-6fa089eb797b`) lines 101-105 [crates/gsqz/src/config.rs:101-105]
  - Signature: `fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {`
  - Purpose: This method implements the `Visitor` trait's `expecting` method to specify that deserialization expects a map containing a single key with one of seven allowed values: filter_lines, group_lines, truncate, dedup, replace, match_output, or compress_prose. [crates/gsqz/src/config.rs:101-105]
- `StepVisitor.visit_map` (method) component `StepVisitor.visit_map [method]` (`fd3332ad-f1cf-55a7-8c3f-129c25d667ea`) lines 107-161 [crates/gsqz/src/config.rs:107-161]
  - Signature: `fn visit_map<A>(self, mut map: A) -> Result<Step, A::Error>`
  - Purpose: # Summary

This method implements custom serde deserialization for a `Step` enum by extracting a string key from a map, pattern-matching it to a step variant name (e.g., "filter_lines", "truncate", "dedup"), and deserializing the associated argument value into the corresponding `Step` variant. [crates/gsqz/src/config.rs:107-161]
- `FilterLinesArgs` (class) component `FilterLinesArgs [class]` (`262c8a3c-1bc2-59f1-88cd-0025b942738d`) lines 169-172 [crates/gsqz/src/config.rs:169-172]
  - Signature: `pub struct FilterLinesArgs {`
  - Purpose: FilterLinesArgs is a serializable struct containing a vector of string patterns that defaults to an empty vector during deserialization. [crates/gsqz/src/config.rs:169-172]
- `GroupLinesArgs` (class) component `GroupLinesArgs [class]` (`70ff970c-0832-5f0b-a491-8780f58cd92b`) lines 175-177 [crates/gsqz/src/config.rs:175-177]
  - Signature: `pub struct GroupLinesArgs {`
  - Purpose: GroupLinesArgs is a struct containing a single public `mode` field of type `String` that specifies the grouping mode for line operations. [crates/gsqz/src/config.rs:175-177]
- `TruncateArgs` (class) component `TruncateArgs [class]` (`4497fb46-154d-5e52-8fb2-13dedea16bf5`) lines 180-189 [crates/gsqz/src/config.rs:180-189]
  - Signature: `pub struct TruncateArgs {`
  - Purpose: `TruncateArgs` is a serializable configuration struct that specifies parameters for truncating file content by retaining a maximum number of lines from the head and tail of each file, with optional per-file line limits and file boundary markers. [crates/gsqz/src/config.rs:180-189]
- `default_head` (function) component `default_head [function]` (`03348671-9439-5797-9091-294049237f7a`) lines 191-193 [crates/gsqz/src/config.rs:191-193]
  - Signature: `fn default_head() -> usize {`
  - Purpose: Returns a constant `usize` value of 20 as the default head size. [crates/gsqz/src/config.rs:191-193]
- `default_tail` (function) component `default_tail [function]` (`444f8690-64bf-57e2-ac6b-1fd0c0e92204`) lines 195-197 [crates/gsqz/src/config.rs:195-197]
  - Signature: `fn default_tail() -> usize {`
  - Purpose: This function returns the constant unsigned integer value `10` as the default tail size. [crates/gsqz/src/config.rs:195-197]
- `DedupArgs` (class) component `DedupArgs [class]` (`fa007958-7166-57a5-88ac-ba9d5880289b`) lines 200-200 [crates/gsqz/src/config.rs:200]
  - Signature: `pub struct DedupArgs {}`
  - Purpose: `DedupArgs` is an empty public struct that serves as a zero-sized marker or placeholder type for deduplication operation arguments. [crates/gsqz/src/config.rs:200]
- `ReplaceArgs` (class) component `ReplaceArgs [class]` (`0d26e39a-9792-5ae2-82ac-76b2e3d971d3`) lines 203-205 [crates/gsqz/src/config.rs:203-205]
  - Signature: `pub struct ReplaceArgs {`
  - Purpose: ReplaceArgs is a struct that encapsulates a vector of ReplaceRule objects to specify multiple replacement transformations. [crates/gsqz/src/config.rs:203-205]
- `ReplaceRule` (class) component `ReplaceRule [class]` (`9a4e43d3-8796-56f0-945a-3d642416b95c`) lines 208-211 [crates/gsqz/src/config.rs:208-211]
  - Signature: `pub struct ReplaceRule {`
  - Purpose: ReplaceRule is a public struct that encapsulates a pattern string and its corresponding replacement string for performing text substitutions. [crates/gsqz/src/config.rs:208-211]
- `MatchOutputArgs` (class) component `MatchOutputArgs [class]` (`f82d75c2-99d3-5e8d-85e2-1cb8bc5e0ef9`) lines 214-216 [crates/gsqz/src/config.rs:214-216]
  - Signature: `pub struct MatchOutputArgs {`
  - Purpose: `MatchOutputArgs` is a public struct that encapsulates a vector of `MatchOutputRule` objects for specifying output matching configurations. [crates/gsqz/src/config.rs:214-216]
- `MatchOutputRule` (class) component `MatchOutputRule [class]` (`6b0c3e07-cb4f-536a-98be-edf0805b978c`) lines 219-224 [crates/gsqz/src/config.rs:219-224]
  - Signature: `pub struct MatchOutputRule {`
  - Purpose: `MatchOutputRule` is a struct that encapsulates a pattern-matching rule with an optional negation condition and an associated message. [crates/gsqz/src/config.rs:219-224]
- `CompressProseArgs` (class) component `CompressProseArgs [class]` (`d03e6ca4-e5b8-5c55-87a2-40828e2078c8`) lines 227-230 [crates/gsqz/src/config.rs:227-230]
  - Signature: `pub struct CompressProseArgs {`
  - Purpose: CompressProseArgs is a serde-serializable struct containing a single String field that specifies the compression level for prose, with a serde-derived default value. [crates/gsqz/src/config.rs:227-230]
- `default_prose_level` (function) component `default_prose_level [function]` (`0e60e410-df3d-5449-a753-ebb02a9ee4c9`) lines 232-234 [crates/gsqz/src/config.rs:232-234]
  - Signature: `fn default_prose_level() -> String {`
  - Purpose: This function returns a `String` containing the default prose level value `"standard"`. [crates/gsqz/src/config.rs:232-234]
- `Fallback` (class) component `Fallback [class]` (`4585eab8-fb22-5aeb-82e6-cac370b74d93`) lines 237-240 [crates/gsqz/src/config.rs:237-240]
  - Signature: `pub struct Fallback {`
  - Purpose: `Fallback` is a struct wrapping a `Vec<Step>` with a custom serde default function (`default_fallback_steps`) for deserialization. [crates/gsqz/src/config.rs:237-240]
- `Fallback` (class) component `Fallback [class]` (`4265aaa4-a9f1-5b88-8a17-0d925919e3a5`) lines 242-248 [crates/gsqz/src/config.rs:242-248]
  - Signature: `impl Default for Fallback {`
  - Purpose: The `Default` trait implementation for `Fallback` initializes a new instance by populating the `steps` field with the result of `default_fallback_steps()`. [crates/gsqz/src/config.rs:242-248]
- `Fallback.default` (method) component `Fallback.default [method]` (`814ddd9d-5afe-597d-87d8-99d41110c04b`) lines 243-247 [crates/gsqz/src/config.rs:243-247]
  - Signature: `fn default() -> Self {`
  - Purpose: Constructs a new instance of `Self` by initializing the `steps` field with the result of `default_fallback_steps()`. [crates/gsqz/src/config.rs:243-247]
- `default_fallback_steps` (function) component `default_fallback_steps [function]` (`fd118047-5041-5ca5-b03b-7431dc1ff002`) lines 250-257 [crates/gsqz/src/config.rs:250-257]
  - Signature: `fn default_fallback_steps() -> Vec<Step> {`
  - Purpose: Returns a vector containing a single `Truncate` step that retains the first and last 20 lines of content as a fallback truncation strategy. [crates/gsqz/src/config.rs:250-257]
- `Config` (class) component `Config [class]` (`8e92b8ec-67bd-5ae4-9ce9-3c993f1d5dfc`) lines 259-326 [crates/gsqz/src/config.rs:259-326]
  - Signature: `impl Config {`
  - Purpose: Config implements layered YAML configuration loading with first-match-wins priority resolution across CLI override, project-local (`.gobby/gsqz.yaml`), home, and compiled-in defaults, plus YAML serialization via `dump()`. [crates/gsqz/src/config.rs:259-326]
- `Config.builtin` (method) component `Config.builtin [method]` (`cf1061f8-a6c2-5d2f-9d5c-a8d6735f413e`) lines 262-264 [crates/gsqz/src/config.rs:262-264]
  - Signature: `pub fn builtin() -> Self {`
  - Purpose: This method constructs and returns a `Self` instance by deserializing a built-in YAML configuration string (`DEFAULT_CONFIG`), panicking if deserialization fails. [crates/gsqz/src/config.rs:262-264]
- `Config.load` (method) component `Config.load [method]` (`ab027411-5918-534c-be77-b27a5e5fe441`) lines 270-287 [crates/gsqz/src/config.rs:270-287]
  - Signature: `pub fn load(config_override: Option<&Path>) -> Self {`
  - Purpose: Loads a configuration object from layered YAML using the "gsqz" namespace with optional override, falling back to a built-in default config string, and exiting with an error message if parsing fails. [crates/gsqz/src/config.rs:270-287]
- `Config.dump` (method) component `Config.dump [method]` (`42cf8946-29e2-573e-ac38-cb688653f8fc`) lines 290-325 [crates/gsqz/src/config.rs:290-325]
  - Signature: `pub fn dump(&self) -> String {`
  - Purpose: Serializes the configuration's settings, pipelines, and excluded commands into a manually-formatted YAML-style string to circumvent serde_yaml's enum serialization quirks. [crates/gsqz/src/config.rs:290-325]
- `test_load_default_config` (function) component `test_load_default_config [function]` (`29e16829-6ac5-59aa-bd0c-e78f4f32e243`) lines 333-338 [crates/gsqz/src/config.rs:333-338]
  - Signature: `fn test_load_default_config() {`
  - Purpose: Verifies that `Config::builtin()` initializes with expected default settings: `min_output_length` of 1000, `max_compressed_lines` of 100, and a non-empty `pipelines` collection. [crates/gsqz/src/config.rs:333-338]
- `test_default_config_has_expected_pipelines` (function) component `test_default_config_has_expected_pipelines [function]` (`14dee87e-39f8-575e-9d2f-b627c24ec474`) lines 341-345 [crates/gsqz/src/config.rs:341-345]
  - Signature: `fn test_default_config_has_expected_pipelines() {`
  - Purpose: This test verifies that the builtin `Config` instance contains pipeline definitions for both "pytest" and "cargo-test". [crates/gsqz/src/config.rs:341-345]
- `test_pipeline_has_match_and_steps` (function) component `test_pipeline_has_match_and_steps [function]` (`39f1fd34-f615-5c57-af0e-da171c85c69e`) lines 348-353 [crates/gsqz/src/config.rs:348-353]
  - Signature: `fn test_pipeline_has_match_and_steps() {`
  - Purpose: Asserts that the builtin configuration's "pytest" pipeline contains non-empty `match_pattern` and `steps` fields. [crates/gsqz/src/config.rs:348-353]
- `test_fallback_has_steps` (function) component `test_fallback_has_steps [function]` (`3cf867f3-5f25-56af-a385-bdad6b74e27b`) lines 356-359 [crates/gsqz/src/config.rs:356-359]
  - Signature: `fn test_fallback_has_steps() {`
  - Purpose: This test asserts that the builtin `Config` instance contains a non-empty `steps` collection in its `fallback` field. [crates/gsqz/src/config.rs:356-359]
- `test_settings_default_values` (function) component `test_settings_default_values [function]` (`0e7e96ad-ab75-56a4-a08c-93e1be23f511`) lines 362-368 [crates/gsqz/src/config.rs:362-368]
  - Signature: `fn test_settings_default_values() {`
  - Purpose: Verifies that `Settings::default()` initializes `min_output_length` to 1000, `max_compressed_lines` to 100, and both `daemon_url` and `on_empty` as `None`. [crates/gsqz/src/config.rs:362-368]
- `test_builtin_config_has_global_on_empty` (function) component `test_builtin_config_has_global_on_empty [function]` (`a4163ae2-500f-5871-b147-b76d074c9d7b`) lines 371-374 [crates/gsqz/src/config.rs:371-374]
  - Signature: `fn test_builtin_config_has_global_on_empty() {`
  - Purpose: Asserts that `Config::builtin()` initializes the `on_empty` setting to a `Some` value. [crates/gsqz/src/config.rs:371-374]
- `test_pipeline_on_empty_deserialization` (function) component `test_pipeline_on_empty_deserialization [function]` (`de7c6b37-1d7f-5307-85e9-917b55d96198`) lines 377-381 [crates/gsqz/src/config.rs:377-381]
  - Signature: `fn test_pipeline_on_empty_deserialization() {`
  - Purpose: This test verifies that a `Pipeline` struct correctly deserializes the `on_empty` field from YAML as an `Option<String>` containing the expected value. [crates/gsqz/src/config.rs:377-381]
- `test_pipeline_on_empty_defaults_to_none` (function) component `test_pipeline_on_empty_defaults_to_none [function]` (`082b4df6-63d5-5909-ab55-b3915a57e462`) lines 384-388 [crates/gsqz/src/config.rs:384-388]
  - Signature: `fn test_pipeline_on_empty_defaults_to_none() {`
  - Purpose: Tests that a `Pipeline` struct deserialized from YAML without an explicit `on_empty` field defaults the `on_empty` field to `None`. [crates/gsqz/src/config.rs:384-388]
- `test_step_deserialization_filter` (function) component `test_step_deserialization_filter [function]` (`cd11cbdd-dd3c-56ca-b449-180a36c09340`) lines 391-398 [crates/gsqz/src/config.rs:391-398]
  - Signature: `fn test_step_deserialization_filter() {`
  - Purpose: Tests that a YAML string defining `filter_lines` with two regex patterns correctly deserializes into a `Step::FilterLines` enum variant. [crates/gsqz/src/config.rs:391-398]
- `test_step_deserialization_group` (function) component `test_step_deserialization_group [function]` (`e699ad43-e45a-5b97-8a03-720780448a89`) lines 401-408 [crates/gsqz/src/config.rs:401-408]
  - Signature: `fn test_step_deserialization_group() {`
  - Purpose: This test verifies that a YAML string deserializes correctly into a `Step::GroupLines` enum variant with the expected `mode` field value via `serde_yaml`. [crates/gsqz/src/config.rs:401-408]
- `test_step_deserialization_truncate` (function) component `test_step_deserialization_truncate [function]` (`1e44760b-ebd1-5eaf-8746-16bc00d75663`) lines 411-423 [crates/gsqz/src/config.rs:411-423]
  - Signature: `fn test_step_deserialization_truncate() {`
  - Purpose: Tests that a YAML truncate step configuration with `head` and `tail` parameters deserializes correctly into a `Step::Truncate` variant with expected field values and defaults. [crates/gsqz/src/config.rs:411-423]
- `test_step_deserialization_truncate_defaults` (function) component `test_step_deserialization_truncate_defaults [function]` (`188d95f6-a806-51e2-bbb9-4f7e2d2b8791`) lines 426-436 [crates/gsqz/src/config.rs:426-436]
  - Signature: `fn test_step_deserialization_truncate_defaults() {`
  - Purpose: Tests that deserializing a `Truncate` step from YAML with empty arguments applies default field values of 20 for `head` and 10 for `tail`. [crates/gsqz/src/config.rs:426-436]
- `test_step_deserialization_dedup` (function) component `test_step_deserialization_dedup [function]` (`f7652769-b395-55f2-b4aa-c7a304d5d88e`) lines 439-443 [crates/gsqz/src/config.rs:439-443]
  - Signature: `fn test_step_deserialization_dedup() {`
  - Purpose: Verifies that a YAML dedup configuration deserializes into the `Step::Dedup` enum variant. [crates/gsqz/src/config.rs:439-443]
- `test_step_deserialization_replace` (function) component `test_step_deserialization_replace [function]` (`10c262d5-0c66-529d-aa6e-8f60fe2a5a59`) lines 446-457 [crates/gsqz/src/config.rs:446-457]
  - Signature: `fn test_step_deserialization_replace() {`
  - Purpose: Tests that a `Step::Replace` variant with a regex pattern matching rule and string replacement deserializes correctly from YAML via `serde_yaml`. [crates/gsqz/src/config.rs:446-457]
- `test_step_deserialization_match_output` (function) component `test_step_deserialization_match_output [function]` (`dc0b4691-58f7-5570-9fe4-ef1c636f142f`) lines 460-473 [crates/gsqz/src/config.rs:460-473]
  - Signature: `fn test_step_deserialization_match_output() {`
  - Purpose: Verifies deserialization of a YAML `match_output` step containing multiple conditional pattern-matching rules into the `Step::MatchOutput` enum variant. [crates/gsqz/src/config.rs:460-473]
- `test_step_deserialization_unknown_variant` (function) component `test_step_deserialization_unknown_variant [function]` (`a5218f73-542e-5e6d-bd46-c15b18026dcc`) lines 476-480 [crates/gsqz/src/config.rs:476-480]
  - Signature: `fn test_step_deserialization_unknown_variant() {`
  - Purpose: This unit test verifies that deserializing a YAML string containing an unknown `Step` enum variant via `serde_yaml` produces a deserialization error rather than succeeding. [crates/gsqz/src/config.rs:476-480]
- `test_config_dump_contains_settings` (function) component `test_config_dump_contains_settings [function]` (`3ae8fdd6-6bf5-5248-af3c-fdf72f39ac44`) lines 483-490 [crates/gsqz/src/config.rs:483-490]
  - Signature: `fn test_config_dump_contains_settings() {`
  - Purpose: Verifies that the dumped representation of a builtin `Config` object contains the expected configuration parameters: `min_output_length`, `max_compressed_lines`, `pipelines`, and `builtin_excluded_commands`. [crates/gsqz/src/config.rs:483-490]
- `test_fallback_default` (function) component `test_fallback_default [function]` (`0b5a4f49-60fd-5014-ad66-9344aabf2781`) lines 493-503 [crates/gsqz/src/config.rs:493-503]
  - Signature: `fn test_fallback_default() {`
  - Purpose: Tests that the default `Fallback` instance contains exactly one step of type `Truncate` with both `head` and `tail` parameters set to 20. [crates/gsqz/src/config.rs:493-503]
- `test_config_from_valid_override` (function) component `test_config_from_valid_override [function]` (`ab89657d-5853-5195-8839-91f7ab714268`) lines 506-513 [crates/gsqz/src/config.rs:506-513]
  - Signature: `fn test_config_from_valid_override() {`
  - Purpose: Tests that `Config::load()` successfully deserializes a valid YAML configuration file from a provided path and populates a non-empty pipelines collection. [crates/gsqz/src/config.rs:506-513]
- `test_all_pipeline_regexes_compile` (function) component `test_all_pipeline_regexes_compile [function]` (`7fe7bc16-fde3-5e8c-9a12-226f03161819`) lines 516-526 [crates/gsqz/src/config.rs:516-526]
  - Signature: `fn test_all_pipeline_regexes_compile() {`
  - Purpose: Tests that all `match_pattern` regular expressions across pipelines in the built-in configuration compile successfully without syntax errors. [crates/gsqz/src/config.rs:516-526]

