---
title: crates/gsqz/src/config.rs
type: code_file
provenance:
- file: crates/gsqz/src/config.rs
  ranges:
  - 26-35
  - 38-47
  - 49-58
  - 50-57
  - 60-62
  - 64-66
  - 69-76
  - 79-87
  - 91-166
  - 92-165
  - '96'
  - 98-162
  - '99'
  - 101-105
  - 107-161
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
  - 243-247
  - 250-257
  - 259-361
  - 262-264
  - 268-290
  - 294-304
  - 307-322
  - 325-360
  - 368-373
  - 376-380
  - 383-388
  - 391-394
  - 397-403
  - 406-409
  - 412-416
  - 419-423
  - 426-433
  - 436-443
  - 446-458
  - 461-471
  - 474-478
  - 481-492
  - 495-508
  - 511-515
  - 518-525
  - 528-538
  - 541-548
  - 551-561
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/config.rs

Module: [[code/modules/crates/gsqz/src|crates/gsqz/src]]

## Purpose

`crates/gsqz/src/config.rs` exposes 57 indexed API symbols.
[crates/gsqz/src/config.rs:26-35]
[crates/gsqz/src/config.rs:38-47]
[crates/gsqz/src/config.rs:49-58]
[crates/gsqz/src/config.rs:50-57]
[crates/gsqz/src/config.rs:60-62]
[crates/gsqz/src/config.rs:64-66]
[crates/gsqz/src/config.rs:69-76]
[crates/gsqz/src/config.rs:79-87]
[crates/gsqz/src/config.rs:91-166]
[crates/gsqz/src/config.rs:92-165]
[crates/gsqz/src/config.rs:96]
[crates/gsqz/src/config.rs:98-162]
[crates/gsqz/src/config.rs:99]
[crates/gsqz/src/config.rs:101-105]
[crates/gsqz/src/config.rs:107-161]
[crates/gsqz/src/config.rs:169-172]
[crates/gsqz/src/config.rs:175-177]
[crates/gsqz/src/config.rs:180-189]
[crates/gsqz/src/config.rs:191-193]
[crates/gsqz/src/config.rs:195-197]
[crates/gsqz/src/config.rs:200]
[crates/gsqz/src/config.rs:203-205]
[crates/gsqz/src/config.rs:208-211]
[crates/gsqz/src/config.rs:214-216]
[crates/gsqz/src/config.rs:219-224]
[crates/gsqz/src/config.rs:227-230]
[crates/gsqz/src/config.rs:232-234]
[crates/gsqz/src/config.rs:237-240]
[crates/gsqz/src/config.rs:242-248]
[crates/gsqz/src/config.rs:243-247]
[crates/gsqz/src/config.rs:250-257]
[crates/gsqz/src/config.rs:259-361]
[crates/gsqz/src/config.rs:262-264]
[crates/gsqz/src/config.rs:268-290]
[crates/gsqz/src/config.rs:294-304]
[crates/gsqz/src/config.rs:307-322]
[crates/gsqz/src/config.rs:325-360]
[crates/gsqz/src/config.rs:368-373]
[crates/gsqz/src/config.rs:376-380]
[crates/gsqz/src/config.rs:383-388]
[crates/gsqz/src/config.rs:391-394]
[crates/gsqz/src/config.rs:397-403]
[crates/gsqz/src/config.rs:406-409]
[crates/gsqz/src/config.rs:412-416]
[crates/gsqz/src/config.rs:419-423]
[crates/gsqz/src/config.rs:426-433]
[crates/gsqz/src/config.rs:436-443]
[crates/gsqz/src/config.rs:446-458]
[crates/gsqz/src/config.rs:461-471]
[crates/gsqz/src/config.rs:474-478]
[crates/gsqz/src/config.rs:481-492]
[crates/gsqz/src/config.rs:495-508]
[crates/gsqz/src/config.rs:511-515]
[crates/gsqz/src/config.rs:518-525]
[crates/gsqz/src/config.rs:528-538]
[crates/gsqz/src/config.rs:541-548]
[crates/gsqz/src/config.rs:551-561]

## API Symbols

- `Config` (class) component `Config [class]` (`97e782d0-91b2-5fc2-b9e5-b17b655dd84d`) lines 26-35 [crates/gsqz/src/config.rs:26-35]
  - Signature: `pub struct Config {`
  - Purpose: The `Config` struct is a serde-deserializable configuration container that aggregates application settings, an ordered map of named pipelines, fallback behavior, and a list of excluded commands, each with default initializers. [crates/gsqz/src/config.rs:26-35]
- `Settings` (class) component `Settings [class]` (`c99f5df8-5e38-5b4f-909b-63b22890e986`) lines 38-47 [crates/gsqz/src/config.rs:38-47]
  - Signature: `pub struct Settings {`
  - Purpose: A serde-serializable configuration struct that defines output length constraints, maximum compression limits, an optional daemon service URL, and empty-value handling behavior. [crates/gsqz/src/config.rs:38-47]
- `Settings` (class) component `Settings [class]` (`f40bc0b3-9141-515d-99a6-24b2a8e5f706`) lines 49-58 [crates/gsqz/src/config.rs:49-58]
  - Signature: `impl Default for Settings {`
  - Purpose: This `Default` trait implementation for `Settings` initializes a new instance with default output constraints via helper functions and sets optional daemon configuration fields to `None`. [crates/gsqz/src/config.rs:49-58]
- `Settings.default` (method) component `Settings.default [method]` (`61e2caff-30a4-5d81-a921-9ffb808d6a6d`) lines 50-57 [crates/gsqz/src/config.rs:50-57]
  - Signature: `fn default() -> Self {`
  - Purpose: This Default trait implementation constructs a struct instance by initializing min_output_length and max_compressed_lines with function-derived defaults, while setting daemon_url and on_empty to None. [crates/gsqz/src/config.rs:50-57]
- `default_min_output_length` (function) component `default_min_output_length [function]` (`d49a5c68-e3dc-538a-a368-f5567051b11a`) lines 60-62 [crates/gsqz/src/config.rs:60-62]
  - Signature: `fn default_min_output_length() -> usize {`
  - Purpose: This function returns the constant unsigned integer value 1000, representing the default minimum output length. [crates/gsqz/src/config.rs:60-62]
- `default_max_compressed_lines` (function) component `default_max_compressed_lines [function]` (`8a691623-f9d1-5a58-bb36-73790de7f69c`) lines 64-66 [crates/gsqz/src/config.rs:64-66]
  - Signature: `fn default_max_compressed_lines() -> usize {`
  - Purpose: This function returns a `usize` constant of 100, representing the default maximum number of compressed lines. [crates/gsqz/src/config.rs:64-66]
- `Pipeline` (class) component `Pipeline [class]` (`1efb3c74-edf7-5ebc-a0b5-88669eac2e96`) lines 69-76 [crates/gsqz/src/config.rs:69-76]
  - Signature: `pub struct Pipeline {`
  - Purpose: A serializable struct that defines a sequence of processing steps triggered by a pattern match, with an optional fallback action when the step collection is empty. [crates/gsqz/src/config.rs:69-76]
- `Step` (type) component `Step [type]` (`8bbf9a80-b14b-52bb-b973-f157dadfbc28`) lines 79-87 [crates/gsqz/src/config.rs:79-87]
  - Signature: `pub enum Step {`
  - Purpose: Indexed type `Step` in `crates/gsqz/src/config.rs`. [crates/gsqz/src/config.rs:79-87]
- `Step` (class) component `Step [class]` (`21c00c1b-e191-54b0-87c0-043b12afe344`) lines 91-166 [crates/gsqz/src/config.rs:91-166]
  - Signature: `impl<'de> Deserialize<'de> for Step {`
  - Purpose: **A custom Deserialize implementation for the Step enum that parses a single-keyed map to select and instantiate the appropriate enum variant with its corresponding type-specific arguments.** [crates/gsqz/src/config.rs:91-166]
- `Step.deserialize` (method) component `Step.deserialize [method]` (`56149edc-ee35-5f1b-8ace-271999a70383`) lines 92-165 [crates/gsqz/src/config.rs:92-165]
  - Signature: `fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>`
  - Purpose: This method implements custom deserialization for the `Step` enum by using a `Visitor` that extracts a single discriminant key from a map and constructs the corresponding `Step` variant by deserializing its associated value into the appropriate typed arguments structure. [crates/gsqz/src/config.rs:92-165]
- `Step.StepVisitor` (class) component `Step.StepVisitor [class]` (`3615d100-7c7a-545a-a5ff-e3338c872984`) lines 96-96 [crates/gsqz/src/config.rs:96]
  - Signature: `struct StepVisitor;`
  - Purpose: `StepVisitor` is an empty struct type with no visible fields or implementation, likely serving as a marker or visitor pattern type for traversing or processing step-related data structures. [crates/gsqz/src/config.rs:96]
- `Step.StepVisitor` (class) component `Step.StepVisitor [class]` (`7499f4da-79c2-5ca6-a3e6-0a46b6bcde5e`) lines 98-162 [crates/gsqz/src/config.rs:98-162]
  - Signature: `impl<'de> Visitor<'de> for StepVisitor {`
  - Purpose: **StepVisitor is a serde deserialization visitor that converts a single-key map into a Step enum variant by dispatching on the key name to one of seven step operations (filter_lines, group_lines, truncate, dedup, replace, match_output, compress_prose) and deserializing their associated typed arguments.** [crates/gsqz/src/config.rs:98-162]
- `StepVisitor.Value` (type) component `StepVisitor.Value [type]` (`a66c7e8b-a774-5f5a-8864-bab0e1b98432`) lines 99-99 [crates/gsqz/src/config.rs:99]
  - Signature: `type Value = Step;`
  - Purpose: Indexed type `StepVisitor.Value` in `crates/gsqz/src/config.rs`. [crates/gsqz/src/config.rs:99]
- `StepVisitor.expecting` (method) component `StepVisitor.expecting [method]` (`a4fd98f4-1986-5a02-b40c-6fa089eb797b`) lines 101-105 [crates/gsqz/src/config.rs:101-105]
  - Signature: `fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {`
  - Purpose: This visitor method writes a description of expected input format to the formatter for serde deserialization error messages, specifying that a map with a single key from the set {filter_lines, group_lines, truncate, dedup, replace, match_output, compress_prose} is required. [crates/gsqz/src/config.rs:101-105]
- `StepVisitor.visit_map` (method) component `StepVisitor.visit_map [method]` (`fd3332ad-f1cf-55a7-8c3f-129c25d667ea`) lines 107-161 [crates/gsqz/src/config.rs:107-161]
  - Signature: `fn visit_map<A>(self, mut map: A) -> Result<Step, A::Error>`
  - Purpose: This method deserializes a `Step` enum variant by reading a key from the map access, matching it against known variant names ("filter_lines", "group_lines", etc.), deserializing the corresponding argument type into that variant, and returning the constructed `Step` result. [crates/gsqz/src/config.rs:107-161]
- `FilterLinesArgs` (class) component `FilterLinesArgs [class]` (`262c8a3c-1bc2-59f1-88cd-0025b942738d`) lines 169-172 [crates/gsqz/src/config.rs:169-172]
  - Signature: `pub struct FilterLinesArgs {`
  - Purpose: `FilterLinesArgs` is a Rust struct that encapsulates a vector of string patterns with serde-derived default deserialization for use as command-line filter arguments. [crates/gsqz/src/config.rs:169-172]
- `GroupLinesArgs` (class) component `GroupLinesArgs [class]` (`70ff970c-0832-5f0b-a491-8780f58cd92b`) lines 175-177 [crates/gsqz/src/config.rs:175-177]
  - Signature: `pub struct GroupLinesArgs {`
  - Purpose: `GroupLinesArgs` is a public struct that encapsulates a single `String` field named `mode` to specify the grouping strategy or configuration for a line-grouping operation. [crates/gsqz/src/config.rs:175-177]
- `TruncateArgs` (class) component `TruncateArgs [class]` (`4497fb46-154d-5e52-8fb2-13dedea16bf5`) lines 180-189 [crates/gsqz/src/config.rs:180-189]
  - Signature: `pub struct TruncateArgs {`
  - Purpose: `TruncateArgs` is a serializable configuration struct that specifies truncation parameters with default-valued fields for head/tail line counts, per-file line limits, and a file marker delimiter. [crates/gsqz/src/config.rs:180-189]
- `default_head` (function) component `default_head [function]` (`03348671-9439-5797-9091-294049237f7a`) lines 191-193 [crates/gsqz/src/config.rs:191-193]
  - Signature: `fn default_head() -> usize {`
  - Purpose: The `default_head()` function is a parameterless Rust function that returns a constant `usize` value of 20. [crates/gsqz/src/config.rs:191-193]
- `default_tail` (function) component `default_tail [function]` (`444f8690-64bf-57e2-ac6b-1fd0c0e92204`) lines 195-197 [crates/gsqz/src/config.rs:195-197]
  - Signature: `fn default_tail() -> usize {`
  - Purpose: The `default_tail` function is a parameterless Rust function that returns the unsigned integer constant `10` of type `usize`. [crates/gsqz/src/config.rs:195-197]
- `DedupArgs` (class) component `DedupArgs [class]` (`fa007958-7166-57a5-88ac-ba9d5880289b`) lines 200-200 [crates/gsqz/src/config.rs:200]
  - Signature: `pub struct DedupArgs {}`
  - Purpose: `DedupArgs` is a zero-sized public Rust struct with no fields, typically used as a marker type for configuration or parameter passing in deduplication-related operations. [crates/gsqz/src/config.rs:200]
- `ReplaceArgs` (class) component `ReplaceArgs [class]` (`0d26e39a-9792-5ae2-82ac-76b2e3d971d3`) lines 203-205 [crates/gsqz/src/config.rs:203-205]
  - Signature: `pub struct ReplaceArgs {`
  - Purpose: ReplaceArgs is a struct that encapsulates a vector of ReplaceRule objects for defining multiple replacement operations. [crates/gsqz/src/config.rs:203-205]
- `ReplaceRule` (class) component `ReplaceRule [class]` (`9a4e43d3-8796-56f0-945a-3d642416b95c`) lines 208-211 [crates/gsqz/src/config.rs:208-211]
  - Signature: `pub struct ReplaceRule {`
  - Purpose: ReplaceRule is a public struct that encapsulates a text substitution rule, pairing a pattern String to match with a replacement String. [crates/gsqz/src/config.rs:208-211]
- `MatchOutputArgs` (class) component `MatchOutputArgs [class]` (`f82d75c2-99d3-5e8d-85e2-1cb8bc5e0ef9`) lines 214-216 [crates/gsqz/src/config.rs:214-216]
  - Signature: `pub struct MatchOutputArgs {`
  - Purpose: `MatchOutputArgs` is a public struct that encapsulates a vector of `MatchOutputRule` objects for specifying output matching rules. [crates/gsqz/src/config.rs:214-216]
- `MatchOutputRule` (class) component `MatchOutputRule [class]` (`6b0c3e07-cb4f-536a-98be-edf0805b978c`) lines 219-224 [crates/gsqz/src/config.rs:219-224]
  - Signature: `pub struct MatchOutputRule {`
  - Purpose: `MatchOutputRule` is a public struct that encapsulates a pattern string, an optional negation condition (`unless`), and a message for pattern-based rule evaluation with conditional output. [crates/gsqz/src/config.rs:219-224]
- `CompressProseArgs` (class) component `CompressProseArgs [class]` (`d03e6ca4-e5b8-5c55-87a2-40828e2078c8`) lines 227-230 [crates/gsqz/src/config.rs:227-230]
  - Signature: `pub struct CompressProseArgs {`
  - Purpose: `CompressProseArgs` is a public struct that encapsulates a compression level parameter as a String field, with a serde-controlled default value provided by the `default_prose_level` function during deserialization. [crates/gsqz/src/config.rs:227-230]
- `default_prose_level` (function) component `default_prose_level [function]` (`0e60e410-df3d-5449-a753-ebb02a9ee4c9`) lines 232-234 [crates/gsqz/src/config.rs:232-234]
  - Signature: `fn default_prose_level() -> String {`
  - Purpose: This function returns a `String` containing the literal value "standard", serving as a default prose level configuration. [crates/gsqz/src/config.rs:232-234]
- `Fallback` (class) component `Fallback [class]` (`4585eab8-fb22-5aeb-82e6-cac370b74d93`) lines 237-240 [crates/gsqz/src/config.rs:237-240]
  - Signature: `pub struct Fallback {`
  - Purpose: `Fallback` is a public struct that contains a vector of `Step` items with serde deserialization support, defaulting to the output of `default_fallback_steps` when the field is absent during deserialization. [crates/gsqz/src/config.rs:237-240]
- `Fallback` (class) component `Fallback [class]` (`4265aaa4-a9f1-5b88-8a17-0d925919e3a5`) lines 242-248 [crates/gsqz/src/config.rs:242-248]
  - Signature: `impl Default for Fallback {`
  - Purpose: The `Default` implementation for `Fallback` constructs an instance with its `steps` field initialized to the result of calling `default_fallback_steps()`. [crates/gsqz/src/config.rs:242-248]
- `Fallback.default` (method) component `Fallback.default [method]` (`814ddd9d-5afe-597d-87d8-99d41110c04b`) lines 243-247 [crates/gsqz/src/config.rs:243-247]
  - Signature: `fn default() -> Self {`
  - Purpose: The `default` method returns a new instance of the struct with the `steps` field initialized to the result of calling `default_fallback_steps()`. [crates/gsqz/src/config.rs:243-247]
- `default_fallback_steps` (function) component `default_fallback_steps [function]` (`fd118047-5041-5ca5-b03b-7431dc1ff002`) lines 250-257 [crates/gsqz/src/config.rs:250-257]
  - Signature: `fn default_fallback_steps() -> Vec<Step> {`
  - Purpose: Returns a `Vec<Step>` containing a single `Step::Truncate` variant configured to preserve the first and last 20 lines of content with zero per-file line limit and an empty file marker. [crates/gsqz/src/config.rs:250-257]
- `Config` (class) component `Config [class]` (`8e92b8ec-67bd-5ae4-9ce9-3c993f1d5dfc`) lines 259-361 [crates/gsqz/src/config.rs:259-361]
  - Signature: `impl Config {`
  - Purpose: **Config implements a priority-based YAML configuration loader that cascades through four sources in order—explicit CLI override, project-local .gobby/gsqz.yaml, user-global ~/.gobby/gsqz.yaml, and compiled-in default—returning the first successfully parsed configuration found.** [crates/gsqz/src/config.rs:259-361]
- `Config.builtin` (method) component `Config.builtin [method]` (`cf1061f8-a6c2-5d2f-9d5c-a8d6735f413e`) lines 262-264 [crates/gsqz/src/config.rs:262-264]
  - Signature: `pub fn builtin() -> Self {`
  - Purpose: This method constructs and returns a Self instance by deserializing a built-in YAML configuration string (`DEFAULT_CONFIG`) using `serde_yaml::from_str`, panicking if deserialization fails. [crates/gsqz/src/config.rs:262-264]
- `Config.load` (method) component `Config.load [method]` (`2153d116-cbf9-593e-83fc-d3be9d884a83`) lines 268-290 [crates/gsqz/src/config.rs:268-290]
  - Signature: `pub fn load(config_override: Option<&Path>) -> Self {`
  - Purpose: Loads and returns a `Self` instance by attempting to read configuration from an optional CLI-provided path, with cascading fallbacks to project-level (`.gobby/gsqz.yaml`), global (`~/.gobby/gsqz.yaml`), and compiled-in default configurations in priority order. [crates/gsqz/src/config.rs:268-290]
- `Config.try_load` (method) component `Config.try_load [method]` (`b8703b73-7623-5d7b-93bf-cb0126aa836e`) lines 294-304 [crates/gsqz/src/config.rs:294-304]
  - Signature: `fn try_load(path: &Path) -> Option<Self> {`
  - Purpose: Reads and deserializes a YAML configuration file from the provided path, returning the parsed config wrapped in `Some` on success or exiting the process with an error message if file reading or YAML deserialization fails. [crates/gsqz/src/config.rs:294-304]
- `Config.load_or_exit` (method) component `Config.load_or_exit [method]` (`468aec69-4992-5013-9c83-670485634131`) lines 307-322 [crates/gsqz/src/config.rs:307-322]
  - Signature: `fn load_or_exit(path: &Path) -> Self {`
  - Purpose: Constructs Self by reading and deserializing YAML from the specified file path, terminating the process with a diagnostic message on I/O or deserialization failure. [crates/gsqz/src/config.rs:307-322]
- `Config.dump` (method) component `Config.dump [method]` (`ce4f5f7f-188c-506c-ab6f-271b31b96735`) lines 325-360 [crates/gsqz/src/config.rs:325-360]
  - Signature: `pub fn dump(&self) -> String {`
  - Purpose: This method returns a manually-formatted string representation of the configuration state, including settings, pipeline definitions with their match patterns and step counts, and excluded commands, circumventing serde_yaml to avoid enum serialization quirks. [crates/gsqz/src/config.rs:325-360]
- `test_load_default_config` (function) component `test_load_default_config [function]` (`3566454c-0dd2-50b3-903d-90d766fa0542`) lines 368-373 [crates/gsqz/src/config.rs:368-373]
  - Signature: `fn test_load_default_config() {`
  - Purpose: This test function validates that `Config::builtin()` returns a default configuration with `min_output_length` of 1000, `max_compressed_lines` of 100, and at least one pipeline defined. [crates/gsqz/src/config.rs:368-373]
- `test_default_config_has_expected_pipelines` (function) component `test_default_config_has_expected_pipelines [function]` (`6026791f-3f1a-5536-b9b5-571b4c51fac1`) lines 376-380 [crates/gsqz/src/config.rs:376-380]
  - Signature: `fn test_default_config_has_expected_pipelines() {`
  - Purpose: This test function asserts that the builtin `Config` instance contains pipeline entries for both "pytest" and "cargo-test" keys. [crates/gsqz/src/config.rs:376-380]
- `test_pipeline_has_match_and_steps` (function) component `test_pipeline_has_match_and_steps [function]` (`75924ca7-53cf-50a2-9608-f0e7f879217e`) lines 383-388 [crates/gsqz/src/config.rs:383-388]
  - Signature: `fn test_pipeline_has_match_and_steps() {`
  - Purpose: This unit test validates that the builtin "pytest" pipeline configuration contains both a non-empty match pattern and a non-empty steps collection. [crates/gsqz/src/config.rs:383-388]
- `test_fallback_has_steps` (function) component `test_fallback_has_steps [function]` (`b0dfd4d4-8fa9-5baa-8e2e-7c4c90fba8b8`) lines 391-394 [crates/gsqz/src/config.rs:391-394]
  - Signature: `fn test_fallback_has_steps() {`
  - Purpose: This function tests that the built-in `Config` instance contains at least one step in its `fallback.steps` collection. [crates/gsqz/src/config.rs:391-394]
- `test_settings_default_values` (function) component `test_settings_default_values [function]` (`008d9a5c-713d-55a9-bd5c-4b09f8713ce6`) lines 397-403 [crates/gsqz/src/config.rs:397-403]
  - Signature: `fn test_settings_default_values() {`
  - Purpose: This unit test validates that `Settings::default()` initializes `min_output_length` to 1000, `max_compressed_lines` to 100, and both `daemon_url` and `on_empty` fields to `None`. [crates/gsqz/src/config.rs:397-403]
- `test_builtin_config_has_global_on_empty` (function) component `test_builtin_config_has_global_on_empty [function]` (`8d79bc4f-475e-5a1f-ad20-36d4dc184d09`) lines 406-409 [crates/gsqz/src/config.rs:406-409]
  - Signature: `fn test_builtin_config_has_global_on_empty() {`
  - Purpose: This test function asserts that the built-in `Config` instance contains a `Some` value for the `settings.on_empty` field (i.e., the setting is defined, not `None`). [crates/gsqz/src/config.rs:406-409]
- `test_pipeline_on_empty_deserialization` (function) component `test_pipeline_on_empty_deserialization [function]` (`2e682f33-4643-5d30-9451-cfd1cfbe2b49`) lines 412-416 [crates/gsqz/src/config.rs:412-416]
  - Signature: `fn test_pipeline_on_empty_deserialization() {`
  - Purpose: This unit test verifies that a `Pipeline` struct correctly deserializes the `on_empty` optional field from a YAML string representation using `serde_yaml`. [crates/gsqz/src/config.rs:412-416]
- `test_pipeline_on_empty_defaults_to_none` (function) component `test_pipeline_on_empty_defaults_to_none [function]` (`d82728b6-636c-5230-92e2-bc0403befe1d`) lines 419-423 [crates/gsqz/src/config.rs:419-423]
  - Signature: `fn test_pipeline_on_empty_defaults_to_none() {`
  - Purpose: This test verifies that deserializing a YAML pipeline configuration without an explicitly specified `on_empty` field defaults that field to `None`. [crates/gsqz/src/config.rs:419-423]
- `test_step_deserialization_filter` (function) component `test_step_deserialization_filter [function]` (`bad4fb02-9c79-5473-9fd3-8f014dee9f9d`) lines 426-433 [crates/gsqz/src/config.rs:426-433]
  - Signature: `fn test_step_deserialization_filter() {`
  - Purpose: This unit test verifies that a YAML-formatted `FilterLines` step configuration with two regex patterns correctly deserializes into a `Step` enum variant containing exactly two pattern elements. [crates/gsqz/src/config.rs:426-433]
- `test_step_deserialization_group` (function) component `test_step_deserialization_group [function]` (`3a98f9d8-e673-5974-a0c6-00b6fa0163e8`) lines 436-443 [crates/gsqz/src/config.rs:436-443]
  - Signature: `fn test_step_deserialization_group() {`
  - Purpose: Tests deserialization of a YAML configuration into a `Step::GroupLines` enum variant and asserts the `mode` field equals `"git_status"`. [crates/gsqz/src/config.rs:436-443]
- `test_step_deserialization_truncate` (function) component `test_step_deserialization_truncate [function]` (`6c0664f7-cdd1-5456-855f-26b49490726a`) lines 446-458 [crates/gsqz/src/config.rs:446-458]
  - Signature: `fn test_step_deserialization_truncate() {`
  - Purpose: This test verifies the correct deserialization of a YAML truncate configuration into a Step::Truncate enum variant with specified and default field values. [crates/gsqz/src/config.rs:446-458]
- `test_step_deserialization_truncate_defaults` (function) component `test_step_deserialization_truncate_defaults [function]` (`ae84b4ff-8dad-5991-ba9b-a2c8eff5b6ba`) lines 461-471 [crates/gsqz/src/config.rs:461-471]
  - Signature: `fn test_step_deserialization_truncate_defaults() {`
  - Purpose: Verifies that deserializing an empty `truncate: {}` YAML object into a `Step` enum produces a `Step::Truncate` variant with default parameters `head=20` and `tail=10`. [crates/gsqz/src/config.rs:461-471]
- `test_step_deserialization_dedup` (function) component `test_step_deserialization_dedup [function]` (`4436b800-152a-51b6-a218-b4e8b4e3ea57`) lines 474-478 [crates/gsqz/src/config.rs:474-478]
  - Signature: `fn test_step_deserialization_dedup() {`
  - Purpose: This unit test asserts that deserializing the YAML string `"dedup: {}"` via `serde_yaml::from_str()` produces a `Step::Dedup` enum variant. [crates/gsqz/src/config.rs:474-478]
- `test_step_deserialization_replace` (function) component `test_step_deserialization_replace [function]` (`6d7b689e-d1a7-54b5-b42b-f1631accea06`) lines 481-492 [crates/gsqz/src/config.rs:481-492]
  - Signature: `fn test_step_deserialization_replace() {`
  - Purpose: This function tests that a YAML string containing regex pattern-replacement rules is correctly deserialized into a `Step::Replace` enum variant with the expected field values. [crates/gsqz/src/config.rs:481-492]
- `test_step_deserialization_match_output` (function) component `test_step_deserialization_match_output [function]` (`02504c17-6ea3-581d-88a0-9d8b0a081e5f`) lines 495-508 [crates/gsqz/src/config.rs:495-508]
  - Signature: `fn test_step_deserialization_match_output() {`
  - Purpose: Verifies that a YAML string containing conditional pattern-matching rules with optional `unless` filters deserializes correctly into a `Step::MatchOutput` variant with the expected rule patterns, messages, and conditions. [crates/gsqz/src/config.rs:495-508]
- `test_step_deserialization_unknown_variant` (function) component `test_step_deserialization_unknown_variant [function]` (`d4d6aa7c-cd13-598e-8a71-61922875b1f5`) lines 511-515 [crates/gsqz/src/config.rs:511-515]
  - Signature: `fn test_step_deserialization_unknown_variant() {`
  - Purpose: This unit test verifies that attempting to deserialize an unknown variant from YAML into a `Step` enum results in a deserialization error. [crates/gsqz/src/config.rs:511-515]
- `test_config_dump_contains_settings` (function) component `test_config_dump_contains_settings [function]` (`6e598d07-c87b-531d-8cb1-326ad8d3292f`) lines 518-525 [crates/gsqz/src/config.rs:518-525]
  - Signature: `fn test_config_dump_contains_settings() {`
  - Purpose: This test verifies that dumping a builtin `Config` instance produces output containing the expected configuration fields (`min_output_length`, `max_compressed_lines`, `pipelines`, and `builtin_excluded_commands`). [crates/gsqz/src/config.rs:518-525]
- `test_fallback_default` (function) component `test_fallback_default [function]` (`ab4a4658-16b4-5b65-b174-65c879565a88`) lines 528-538 [crates/gsqz/src/config.rs:528-538]
  - Signature: `fn test_fallback_default() {`
  - Purpose: A unit test verifying that `Fallback::default()` instantiates a single `Step::Truncate` step with `head` and `tail` parameters both set to 20. [crates/gsqz/src/config.rs:528-538]
- `test_config_from_valid_override` (function) component `test_config_from_valid_override [function]` (`bf464094-76be-5529-805d-af756541dbb6`) lines 541-548 [crates/gsqz/src/config.rs:541-548]
  - Signature: `fn test_config_from_valid_override() {`
  - Purpose: This test function verifies that `Config::load()` successfully deserializes a valid YAML configuration file from an explicitly provided path, resulting in a `Config` object with a non-empty `pipelines` collection. [crates/gsqz/src/config.rs:541-548]
- `test_all_pipeline_regexes_compile` (function) component `test_all_pipeline_regexes_compile [function]` (`238824a7-8147-5cdd-89c6-68a914b22123`) lines 551-561 [crates/gsqz/src/config.rs:551-561]
  - Signature: `fn test_all_pipeline_regexes_compile() {`
  - Purpose: This unit test validates that every `match_pattern` regex string in the built-in pipelines configuration compiles successfully without errors. [crates/gsqz/src/config.rs:551-561]

