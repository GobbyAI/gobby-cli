---
title: crates/gsqz/src/compressor.rs
type: code_file
provenance:
- file: crates/gsqz/src/compressor.rs
  ranges:
  - 7-12
  - 14-34
  - 15-20
  - 29-33
  - 36-40
  - 42-52
  - 54-60
  - 62-67
  - 69-76
  - 78-233
  - 79-109
  - 118-125
  - 127-232
  - 235-266
  - 272-274
  - 277-282
  - 285-293
  - 296-304
  - 307-315
  - 318-327
  - 330-345
  - 348-358
  - 361-377
  - 380-402
  - 405-410
  - 413-424
  - 427-431
  - 434-455
  - 458-468
  - 471-481
  - 484-493
  - 496-507
  - 510-523
  - 526-548
  - 551-571
  - 574-583
  - 586-618
  - 621-646
  - 649-666
  - 669-678
  - 681-691
  - 694-702
  - 705-715
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/compressor.rs

Module: [[code/modules/crates/gsqz/src|crates/gsqz/src]]

## Purpose

`crates/gsqz/src/compressor.rs` exposes 43 indexed API symbols.
[crates/gsqz/src/compressor.rs:7-12]
[crates/gsqz/src/compressor.rs:14-34]
[crates/gsqz/src/compressor.rs:15-20]
[crates/gsqz/src/compressor.rs:29-33]
[crates/gsqz/src/compressor.rs:36-40]
[crates/gsqz/src/compressor.rs:42-52]
[crates/gsqz/src/compressor.rs:54-60]
[crates/gsqz/src/compressor.rs:62-67]
[crates/gsqz/src/compressor.rs:69-76]
[crates/gsqz/src/compressor.rs:78-233]
[crates/gsqz/src/compressor.rs:79-109]
[crates/gsqz/src/compressor.rs:118-125]
[crates/gsqz/src/compressor.rs:127-232]
[crates/gsqz/src/compressor.rs:235-266]
[crates/gsqz/src/compressor.rs:272-274]
[crates/gsqz/src/compressor.rs:277-282]
[crates/gsqz/src/compressor.rs:285-293]
[crates/gsqz/src/compressor.rs:296-304]
[crates/gsqz/src/compressor.rs:307-315]
[crates/gsqz/src/compressor.rs:318-327]
[crates/gsqz/src/compressor.rs:330-345]
[crates/gsqz/src/compressor.rs:348-358]
[crates/gsqz/src/compressor.rs:361-377]
[crates/gsqz/src/compressor.rs:380-402]
[crates/gsqz/src/compressor.rs:405-410]
[crates/gsqz/src/compressor.rs:413-424]
[crates/gsqz/src/compressor.rs:427-431]
[crates/gsqz/src/compressor.rs:434-455]
[crates/gsqz/src/compressor.rs:458-468]
[crates/gsqz/src/compressor.rs:471-481]
[crates/gsqz/src/compressor.rs:484-493]
[crates/gsqz/src/compressor.rs:496-507]
[crates/gsqz/src/compressor.rs:510-523]
[crates/gsqz/src/compressor.rs:526-548]
[crates/gsqz/src/compressor.rs:551-571]
[crates/gsqz/src/compressor.rs:574-583]
[crates/gsqz/src/compressor.rs:586-618]
[crates/gsqz/src/compressor.rs:621-646]
[crates/gsqz/src/compressor.rs:649-666]
[crates/gsqz/src/compressor.rs:669-678]
[crates/gsqz/src/compressor.rs:681-691]
[crates/gsqz/src/compressor.rs:694-702]
[crates/gsqz/src/compressor.rs:705-715]

## API Symbols

- `CompressionResult` (class) component `CompressionResult [class]` (`72df8651-a364-5c4e-acc5-8c9cd21e9524`) lines 7-12 [crates/gsqz/src/compressor.rs:7-12]
  - Signature: `pub struct CompressionResult {`
  - Purpose: Indexed class `CompressionResult` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:7-12]
- `CompressionResult` (class) component `CompressionResult [class]` (`9854a28c-9b93-5d2b-9480-de05469fd68f`) lines 14-34 [crates/gsqz/src/compressor.rs:14-34]
  - Signature: `impl CompressionResult {`
  - Purpose: Indexed class `CompressionResult` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:14-34]
- `CompressionResult.savings_pct` (method) component `CompressionResult.savings_pct [method]` (`c33f4294-b3d8-5ddf-b3f1-1afff71934fe`) lines 15-20 [crates/gsqz/src/compressor.rs:15-20]
  - Signature: `pub fn savings_pct(&self) -> f64 {`
  - Purpose: Indexed method `CompressionResult.savings_pct` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:15-20]
- `CompressionResult.is_passthrough` (method) component `CompressionResult.is_passthrough [method]` (`3ac3f184-4da9-5e04-819c-f645ee0cfcad`) lines 29-33 [crates/gsqz/src/compressor.rs:29-33]
  - Signature: `pub fn is_passthrough(&self) -> bool {`
  - Purpose: Indexed method `CompressionResult.is_passthrough` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:29-33]
- `first_command_token` (function) component `first_command_token [function]` (`d236570a-4711-5192-a192-5741d959fa0f`) lines 36-40 [crates/gsqz/src/compressor.rs:36-40]
  - Signature: `fn first_command_token(segment: &str) -> Option<&str> {`
  - Purpose: Indexed function `first_command_token` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:36-40]
- `is_env_assignment_token` (function) component `is_env_assignment_token [function]` (`78816fa0-49b2-543c-845a-38a3286dd358`) lines 42-52 [crates/gsqz/src/compressor.rs:42-52]
  - Signature: `fn is_env_assignment_token(token: &str) -> bool {`
  - Purpose: Indexed function `is_env_assignment_token` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:42-52]
- `command_basename` (function) component `command_basename [function]` (`0cb8da5a-eea9-5dd4-921c-19f79ee3dd87`) lines 54-60 [crates/gsqz/src/compressor.rs:54-60]
  - Signature: `fn command_basename(token: &str) -> &str {`
  - Purpose: Indexed function `command_basename` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:54-60]
- `CompiledPipeline` (class) component `CompiledPipeline [class]` (`436c60a6-c1e8-5f2e-b449-55a94e08f6e4`) lines 62-67 [crates/gsqz/src/compressor.rs:62-67]
  - Signature: `struct CompiledPipeline {`
  - Purpose: Indexed class `CompiledPipeline` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:62-67]
- `Compressor` (class) component `Compressor [class]` (`880dadac-40a2-5d27-88d4-05b3cf9df5ed`) lines 69-76 [crates/gsqz/src/compressor.rs:69-76]
  - Signature: `pub struct Compressor {`
  - Purpose: Indexed class `Compressor` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:69-76]
- `Compressor` (class) component `Compressor [class]` (`aff9cb40-2d59-5dc4-b5fd-fdc80889ab74`) lines 78-233 [crates/gsqz/src/compressor.rs:78-233]
  - Signature: `impl Compressor {`
  - Purpose: Indexed class `Compressor` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:78-233]
- `Compressor.new` (method) component `Compressor.new [method]` (`a2c1c64c-462d-5f42-9dc8-5b35344a04b5`) lines 79-109 [crates/gsqz/src/compressor.rs:79-109]
  - Signature: `pub fn new(config: &Config) -> Self {`
  - Purpose: Indexed method `Compressor.new` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:79-109]
- `Compressor.command_is_excluded` (method) component `Compressor.command_is_excluded [method]` (`8efa0e8a-6b21-511c-a07f-6423de18fddc`) lines 118-125 [crates/gsqz/src/compressor.rs:118-125]
  - Signature: `pub fn command_is_excluded(&self, command: &str) -> bool {`
  - Purpose: Indexed method `Compressor.command_is_excluded` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:118-125]
- `Compressor.compress` (method) component `Compressor.compress [method]` (`788d8c50-5ed2-5301-a6df-1d0d5958e804`) lines 127-232 [crates/gsqz/src/compressor.rs:127-232]
  - Signature: `pub fn compress(&self, command: &str, output: &str) -> CompressionResult {`
  - Purpose: Indexed method `Compressor.compress` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:127-232]
- `apply_steps` (function) component `apply_steps [function]` (`b9f4a498-1b46-5866-8057-03d7fd3db7a2`) lines 235-266 [crates/gsqz/src/compressor.rs:235-266]
  - Signature: `fn apply_steps(mut lines: Vec<String>, steps: &[Step]) -> Vec<String> {`
  - Purpose: Indexed function `apply_steps` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:235-266]
- `test_config` (function) component `test_config [function]` (`4d96cd0c-6125-510e-8a0c-be9ca181554f`) lines 272-274 [crates/gsqz/src/compressor.rs:272-274]
  - Signature: `fn test_config() -> Config {`
  - Purpose: Indexed function `test_config` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:272-274]
- `test_passthrough_short_output` (function) component `test_passthrough_short_output [function]` (`82da9c95-f727-591e-9942-21c643550913`) lines 277-282 [crates/gsqz/src/compressor.rs:277-282]
  - Signature: `fn test_passthrough_short_output() {`
  - Purpose: Indexed function `test_passthrough_short_output` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:277-282]
- `test_pipeline_match` (function) component `test_pipeline_match [function]` (`5d783255-271c-5a75-8deb-3ec862819af3`) lines 285-293 [crates/gsqz/src/compressor.rs:285-293]
  - Signature: `fn test_pipeline_match() {`
  - Purpose: Indexed function `test_pipeline_match` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:285-293]
- `test_savings_pct_zero_original` (function) component `test_savings_pct_zero_original [function]` (`cfbb0621-7d91-5119-b162-b30dc3cd3e56`) lines 296-304 [crates/gsqz/src/compressor.rs:296-304]
  - Signature: `fn test_savings_pct_zero_original() {`
  - Purpose: Indexed function `test_savings_pct_zero_original` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:296-304]
- `test_savings_pct_calculation` (function) component `test_savings_pct_calculation [function]` (`b8c1c8fa-0070-5933-9d6e-245777fa2bc3`) lines 307-315 [crates/gsqz/src/compressor.rs:307-315]
  - Signature: `fn test_savings_pct_calculation() {`
  - Purpose: Indexed function `test_savings_pct_calculation` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:307-315]
- `test_fallback_used_when_no_pipeline_matches` (function) component `test_fallback_used_when_no_pipeline_matches [function]` (`266e5f64-482b-55c8-b7b5-9d67b90ef67a`) lines 318-327 [crates/gsqz/src/compressor.rs:318-327]
  - Signature: `fn test_fallback_used_when_no_pipeline_matches() {`
  - Purpose: Indexed function `test_fallback_used_when_no_pipeline_matches` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:318-327]
- `test_max_lines_cap_applied` (function) component `test_max_lines_cap_applied [function]` (`f53ea6fe-88b5-545b-a75d-043b12fb3f0a`) lines 330-345 [crates/gsqz/src/compressor.rs:330-345]
  - Signature: `fn test_max_lines_cap_applied() {`
  - Purpose: Indexed function `test_max_lines_cap_applied` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:330-345]
- `test_low_savings_fallback_keeps_passthrough_marker` (function) component `test_low_savings_fallback_keeps_passthrough_marker [function]` (`32305f32-7ea1-5474-9381-c4024de06ea4`) lines 348-358 [crates/gsqz/src/compressor.rs:348-358]
  - Signature: `fn test_low_savings_fallback_keeps_passthrough_marker() {`
  - Purpose: Indexed function `test_low_savings_fallback_keeps_passthrough_marker` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:348-358]
- `test_git_status_is_excluded` (function) component `test_git_status_is_excluded [function]` (`3d78adca-c8bc-599e-b8b2-3f9e690b7473`) lines 361-377 [crates/gsqz/src/compressor.rs:361-377]
  - Signature: `fn test_git_status_is_excluded() {`
  - Purpose: Indexed function `test_git_status_is_excluded` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:361-377]
- `test_builtin_excluded_commands_are_raw_passthrough` (function) component `test_builtin_excluded_commands_are_raw_passthrough [function]` (`c33da4f0-c953-5367-bae6-c676a18cee85`) lines 380-402 [crates/gsqz/src/compressor.rs:380-402]
  - Signature: `fn test_builtin_excluded_commands_are_raw_passthrough() {`
  - Purpose: Indexed function `test_builtin_excluded_commands_are_raw_passthrough` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:380-402]
- `test_builtin_exclusion_runs_before_min_length` (function) component `test_builtin_exclusion_runs_before_min_length [function]` (`8d608421-dcf6-54b8-a137-75be748af06e`) lines 405-410 [crates/gsqz/src/compressor.rs:405-410]
  - Signature: `fn test_builtin_exclusion_runs_before_min_length() {`
  - Purpose: Indexed function `test_builtin_exclusion_runs_before_min_length` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:405-410]
- `test_builtin_exclusion_matches_compound_segments` (function) component `test_builtin_exclusion_matches_compound_segments [function]` (`cf4732b9-64d1-5821-a2a4-3705327673a7`) lines 413-424 [crates/gsqz/src/compressor.rs:413-424]
  - Signature: `fn test_builtin_exclusion_matches_compound_segments() {`
  - Purpose: Indexed function `test_builtin_exclusion_matches_compound_segments` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:413-424]
- `test_builtin_exclusion_matches_binary_paths` (function) component `test_builtin_exclusion_matches_binary_paths [function]` (`5731515f-0018-5229-abf5-d0843ad24b68`) lines 427-431 [crates/gsqz/src/compressor.rs:427-431]
  - Signature: `fn test_builtin_exclusion_matches_binary_paths() {`
  - Purpose: Indexed function `test_builtin_exclusion_matches_binary_paths` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:427-431]
- `test_shell_inspection_commands_are_builtin_exclusions` (function) component `test_shell_inspection_commands_are_builtin_exclusions [function]` (`ee1f11f1-1d57-5a22-9afb-43f1ae8f1962`) lines 434-455 [crates/gsqz/src/compressor.rs:434-455]
  - Signature: `fn test_shell_inspection_commands_are_builtin_exclusions() {`
  - Purpose: Indexed function `test_shell_inspection_commands_are_builtin_exclusions` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:434-455]
- `test_first_command_token_skips_env_assignments` (function) component `test_first_command_token_skips_env_assignments [function]` (`59d025ad-0262-587a-9492-2dd770574b58`) lines 458-468 [crates/gsqz/src/compressor.rs:458-468]
  - Signature: `fn test_first_command_token_skips_env_assignments() {`
  - Purpose: Indexed function `test_first_command_token_skips_env_assignments` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:458-468]
- `test_first_command_token_keeps_non_env_equals_tokens` (function) component `test_first_command_token_keeps_non_env_equals_tokens [function]` (`cb63f364-22c4-592c-9f81-e08b5588698d`) lines 471-481 [crates/gsqz/src/compressor.rs:471-481]
  - Signature: `fn test_first_command_token_keeps_non_env_equals_tokens() {`
  - Purpose: Indexed function `test_first_command_token_keeps_non_env_equals_tokens` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:471-481]
- `test_cargo_test_pipeline` (function) component `test_cargo_test_pipeline [function]` (`7c0e68a6-4150-5ff2-8eb2-77621155aeaf`) lines 484-493 [crates/gsqz/src/compressor.rs:484-493]
  - Signature: `fn test_cargo_test_pipeline() {`
  - Purpose: Indexed function `test_cargo_test_pipeline` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:484-493]
- `test_match_output_short_circuits` (function) component `test_match_output_short_circuits [function]` (`eef9e1ad-e0fa-5e69-9a86-87d8e9d0bb86`) lines 496-507 [crates/gsqz/src/compressor.rs:496-507]
  - Signature: `fn test_match_output_short_circuits() {`
  - Purpose: Indexed function `test_match_output_short_circuits` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:496-507]
- `test_match_output_unless_prevents_short_circuit` (function) component `test_match_output_unless_prevents_short_circuit [function]` (`80fb0fdb-a33d-5192-ae12-c2017805790b`) lines 510-523 [crates/gsqz/src/compressor.rs:510-523]
  - Signature: `fn test_match_output_unless_prevents_short_circuit() {`
  - Purpose: Indexed function `test_match_output_unless_prevents_short_circuit` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:510-523]
- `test_on_empty_global_fallback` (function) component `test_on_empty_global_fallback [function]` (`d748924c-2414-5716-9e6e-7a635ba939dd`) lines 526-548 [crates/gsqz/src/compressor.rs:526-548]
  - Signature: `fn test_on_empty_global_fallback() {`
  - Purpose: Indexed function `test_on_empty_global_fallback` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:526-548]
- `test_on_empty_pipeline_overrides_global` (function) component `test_on_empty_pipeline_overrides_global [function]` (`00260bd3-7b94-5050-87e1-8f9d438367cd`) lines 551-571 [crates/gsqz/src/compressor.rs:551-571]
  - Signature: `fn test_on_empty_pipeline_overrides_global() {`
  - Purpose: Indexed function `test_on_empty_pipeline_overrides_global` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:551-571]
- `test_on_empty_not_used_when_output_nonempty` (function) component `test_on_empty_not_used_when_output_nonempty [function]` (`b197eca9-c3e2-5f6a-871d-972b88480059`) lines 574-583 [crates/gsqz/src/compressor.rs:574-583]
  - Signature: `fn test_on_empty_not_used_when_output_nonempty() {`
  - Purpose: Indexed function `test_on_empty_not_used_when_output_nonempty` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:574-583]
- `test_low_savings_pipeline_gets_marker` (function) component `test_low_savings_pipeline_gets_marker [function]` (`42e7086f-b4c2-5a60-93c6-30c01c7dd3df`) lines 586-618 [crates/gsqz/src/compressor.rs:586-618]
  - Signature: `fn test_low_savings_pipeline_gets_marker() {`
  - Purpose: Indexed function `test_low_savings_pipeline_gets_marker` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:586-618]
- `test_low_savings_suppressed_when_marker_would_grow_output` (function) component `test_low_savings_suppressed_when_marker_would_grow_output [function]` (`52ce9ccd-bfb7-54df-ad64-53574fb8f51d`) lines 621-646 [crates/gsqz/src/compressor.rs:621-646]
  - Signature: `fn test_low_savings_suppressed_when_marker_would_grow_output() {`
  - Purpose: Indexed function `test_low_savings_suppressed_when_marker_would_grow_output` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:621-646]
- `test_is_passthrough_classification` (function) component `test_is_passthrough_classification [function]` (`244f4e2e-f09d-5630-be63-93e3c2b43aca`) lines 649-666 [crates/gsqz/src/compressor.rs:649-666]
  - Signature: `fn test_is_passthrough_classification() {`
  - Purpose: Indexed function `test_is_passthrough_classification` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:649-666]
- `test_good_compression_has_no_marker` (function) component `test_good_compression_has_no_marker [function]` (`10e4d22b-0b39-5ef2-a0a7-d255fa00f24e`) lines 669-678 [crates/gsqz/src/compressor.rs:669-678]
  - Signature: `fn test_good_compression_has_no_marker() {`
  - Purpose: Indexed function `test_good_compression_has_no_marker` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:669-678]
- `test_compound_command_matches_last_segment` (function) component `test_compound_command_matches_last_segment [function]` (`575ed30f-5095-58fa-812e-162379f98752`) lines 681-691 [crates/gsqz/src/compressor.rs:681-691]
  - Signature: `fn test_compound_command_matches_last_segment() {`
  - Purpose: Indexed function `test_compound_command_matches_last_segment` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:681-691]
- `test_compound_single_command_unchanged` (function) component `test_compound_single_command_unchanged [function]` (`72a1f9c8-eee3-5eef-bc85-65940de1b80c`) lines 694-702 [crates/gsqz/src/compressor.rs:694-702]
  - Signature: `fn test_compound_single_command_unchanged() {`
  - Purpose: Indexed function `test_compound_single_command_unchanged` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:694-702]
- `test_compound_falls_back_to_earlier_segment` (function) component `test_compound_falls_back_to_earlier_segment [function]` (`25be7ab4-68f7-58ee-b58b-f9777d5d464c`) lines 705-715 [crates/gsqz/src/compressor.rs:705-715]
  - Signature: `fn test_compound_falls_back_to_earlier_segment() {`
  - Purpose: Indexed function `test_compound_falls_back_to_earlier_segment` in `crates/gsqz/src/compressor.rs`. [crates/gsqz/src/compressor.rs:705-715]

