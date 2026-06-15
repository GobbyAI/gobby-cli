---
title: crates/gsqz/src/compressor.rs
type: code_file
provenance:
- file: crates/gsqz/src/compressor.rs
  ranges:
  - 7-12
  - 14-34
  - 36-40
  - 42-52
  - 54-60
  - 62-67
  - 69-76
  - 78-233
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

Implements the `gsqz` text compressor: it decides when command output should be passed through, excluded, or compressed, then applies a regex-selected pipeline or fallback steps to shorten verbose output while tracking the original and compressed sizes. The file also includes helpers for parsing command tokens and shell-style basenames, plus the step executor that performs filtering, grouping, truncation, deduplication, replacement, and prose compression, with tests covering pipeline selection, exclusions, savings calculations, and empty-output fallback behavior.
[crates/gsqz/src/compressor.rs:7-12]
[crates/gsqz/src/compressor.rs:14-34]
[crates/gsqz/src/compressor.rs:15-20]
[crates/gsqz/src/compressor.rs:29-33]
[crates/gsqz/src/compressor.rs:36-40]

## API Symbols

- `CompressionResult` (class) component `CompressionResult [class]` (`72df8651-a364-5c4e-acc5-8c9cd21e9524`) lines 7-12 [crates/gsqz/src/compressor.rs:7-12]
  - Signature: `pub struct CompressionResult {`
  - Purpose: 'CompressionResult' is a Rust struct that records the compressed text output along with the original and compressed character counts and the name of the compression strategy used. [crates/gsqz/src/compressor.rs:7-12]
- `CompressionResult` (class) component `CompressionResult [class]` (`9854a28c-9b93-5d2b-9480-de05469fd68f`) lines 14-34 [crates/gsqz/src/compressor.rs:14-34]
  - Signature: `impl CompressionResult {`
  - Purpose: 'CompressionResult' encapsulates compression outcome metrics and strategy metadata, exposing a 'savings_pct()' calculation from original vs. compressed character counts and an 'is_passthrough()' predicate that identifies cases where no useful compression was applied ('passthrough', 'excluded', or '*/no-op'). [crates/gsqz/src/compressor.rs:14-34]
- `CompressionResult.savings_pct` (method) component `CompressionResult.savings_pct [method]` (`c33f4294-b3d8-5ddf-b3f1-1afff71934fe`) lines 15-20 [crates/gsqz/src/compressor.rs:15-20]
  - Signature: `pub fn savings_pct(&self) -> f64 {`
  - Purpose: Returns the percentage reduction from 'original_chars' to 'compressed_chars', yielding '0.0' when 'original_chars' is zero and clamping the computed percentage to a minimum of '0.0'. [crates/gsqz/src/compressor.rs:15-20]
- `CompressionResult.is_passthrough` (method) component `CompressionResult.is_passthrough [method]` (`3ac3f184-4da9-5e04-819c-f645ee0cfcad`) lines 29-33 [crates/gsqz/src/compressor.rs:29-33]
  - Signature: `pub fn is_passthrough(&self) -> bool {`
  - Purpose: Returns 'true' when 'self.strategy_name' is exactly '"passthrough"' or '"excluded"', or when it ends with '"/no-op"'. [crates/gsqz/src/compressor.rs:29-33]
- `first_command_token` (function) component `first_command_token [function]` (`d236570a-4711-5192-a192-5741d959fa0f`) lines 36-40 [crates/gsqz/src/compressor.rs:36-40]
  - Signature: `fn first_command_token(segment: &str) -> Option<&str> {`
  - Purpose: Returns the first non-environment-assignment whitespace-delimited token from 'segment', or 'None' if no such token exists. [crates/gsqz/src/compressor.rs:36-40]
- `is_env_assignment_token` (function) component `is_env_assignment_token [function]` (`78816fa0-49b2-543c-845a-38a3286dd358`) lines 42-52 [crates/gsqz/src/compressor.rs:42-52]
  - Signature: `fn is_env_assignment_token(token: &str) -> bool {`
  - Purpose: Returns 'true' only if 'token' contains exactly one '='-separated name/value pair whose name is nonempty and is a valid shell-style identifier: the first character is ASCII alphabetic or '_', and all remaining characters are ASCII alphanumeric or '_'. [crates/gsqz/src/compressor.rs:42-52]
- `command_basename` (function) component `command_basename [function]` (`0cb8da5a-eea9-5dd4-921c-19f79ee3dd87`) lines 54-60 [crates/gsqz/src/compressor.rs:54-60]
  - Signature: `fn command_basename(token: &str) -> &str {`
  - Purpose: Returns the last path component of 'token' after trimming leading and trailing single or double quotes, splitting on '/' or '\', and falling back to the original string if no separator is present. [crates/gsqz/src/compressor.rs:54-60]
- `CompiledPipeline` (class) component `CompiledPipeline [class]` (`436c60a6-c1e8-5f2e-b449-55a94e08f6e4`) lines 62-67 [crates/gsqz/src/compressor.rs:62-67]
  - Signature: `struct CompiledPipeline {`
  - Purpose: 'CompiledPipeline' is a compiled pipeline definition that stores a pipeline name, a precompiled 'Regex' selector, an ordered list of 'Step' executions, and an optional 'on_empty' handler string for the empty-match case. [crates/gsqz/src/compressor.rs:62-67]
- `Compressor` (class) component `Compressor [class]` (`880dadac-40a2-5d27-88d4-05b3cf9df5ed`) lines 69-76 [crates/gsqz/src/compressor.rs:69-76]
  - Signature: `pub struct Compressor {`
  - Purpose: 'Compressor' is a configuration holder for text compression that stores compiled pipelines, fallback steps, exclusion regexes, and size thresholds, plus an optional global empty-output fallback string. [crates/gsqz/src/compressor.rs:69-76]
- `Compressor` (class) component `Compressor [class]` (`aff9cb40-2d59-5dc4-b5fd-fdc80889ab74`) lines 78-233 [crates/gsqz/src/compressor.rs:78-233]
  - Signature: `impl Compressor {`
  - Purpose: 'Compressor' builds regex-matched compression pipelines and exclusion rules from config, then decides whether a command/output pair should be compressed and applies the configured pipeline or fallback behavior with length, line, and empty-output limits. [crates/gsqz/src/compressor.rs:78-233]
- `Compressor.new` (method) component `Compressor.new [method]` (`a2c1c64c-462d-5f42-9dc8-5b35344a04b5`) lines 79-109 [crates/gsqz/src/compressor.rs:79-109]
  - Signature: `pub fn new(config: &Config) -> Self {`
  - Purpose: Constructs a 'Self' by compiling valid pipeline match patterns and excluded-command regexes from 'Config', cloning pipeline/fallback fields, and copying output-length, line-limit, and global 'on_empty' settings into the new instance. [crates/gsqz/src/compressor.rs:79-109]
- `Compressor.command_is_excluded` (method) component `Compressor.command_is_excluded [method]` (`8efa0e8a-6b21-511c-a07f-6423de18fddc`) lines 118-125 [crates/gsqz/src/compressor.rs:118-125]
  - Signature: `pub fn command_is_excluded(&self, command: &str) -> bool {`
  - Purpose: Returns 'true' if any compound-command segment resolves to a basename in 'BUILTIN_EXCLUDED_COMMANDS' or if the full command matches any regex in 'self.excluded', otherwise 'false'. [crates/gsqz/src/compressor.rs:118-125]
- `Compressor.compress` (method) component `Compressor.compress [method]` (`788d8c50-5ed2-5301-a6df-1d0d5958e804`) lines 127-232 [crates/gsqz/src/compressor.rs:127-232]
  - Signature: `pub fn compress(&self, command: &str, output: &str) -> CompressionResult {`
  - Purpose: 'compress' returns a 'CompressionResult' that either passes the output through unchanged for excluded or too-short commands, or applies the first matching pipeline from the command’s reversed compound segments (otherwise a fallback pipeline), tracking original/compressed character counts and strategy name. [crates/gsqz/src/compressor.rs:127-232]
- `apply_steps` (function) component `apply_steps [function]` (`b9f4a498-1b46-5866-8057-03d7fd3db7a2`) lines 235-266 [crates/gsqz/src/compressor.rs:235-266]
  - Signature: `fn apply_steps(mut lines: Vec<String>, steps: &[Step]) -> Vec<String> {`
  - Purpose: Applies an ordered sequence of transformation steps to a vector of lines, mutating it through filtering/grouping/truncation/deduplication/replacement/prose compression and returning immediately with a single formatted message if 'MatchOutput' succeeds. [crates/gsqz/src/compressor.rs:235-266]
- `test_config` (function) component `test_config [function]` (`4d96cd0c-6125-510e-8a0c-be9ca181554f`) lines 272-274 [crates/gsqz/src/compressor.rs:272-274]
  - Signature: `fn test_config() -> Config {`
  - Purpose: Returns the builtin 'Config' by calling 'Config::builtin()'. [crates/gsqz/src/compressor.rs:272-274]
- `test_passthrough_short_output` (function) component `test_passthrough_short_output [function]` (`82da9c95-f727-591e-9942-21c643550913`) lines 277-282 [crates/gsqz/src/compressor.rs:277-282]
  - Signature: `fn test_passthrough_short_output() {`
  - Purpose: Verifies that 'Compressor::compress' selects the 'passthrough' strategy for a short input and returns the original output unchanged ('"ok"'). [crates/gsqz/src/compressor.rs:277-282]
- `test_pipeline_match` (function) component `test_pipeline_match [function]` (`5d783255-271c-5a75-8deb-3ec862819af3`) lines 285-293 [crates/gsqz/src/compressor.rs:285-293]
  - Signature: `fn test_pipeline_match() {`
  - Purpose: Verifies that 'Compressor::compress' recognizes a 'uv run pytest tests/' command as the 'pytest' strategy and reduces the size of a large passing-test output string. [crates/gsqz/src/compressor.rs:285-293]
- `test_savings_pct_zero_original` (function) component `test_savings_pct_zero_original [function]` (`cfbb0621-7d91-5119-b162-b30dc3cd3e56`) lines 296-304 [crates/gsqz/src/compressor.rs:296-304]
  - Signature: `fn test_savings_pct_zero_original() {`
  - Purpose: Verifies that 'CompressionResult::savings_pct()' returns '0.0' when both 'original_chars' and 'compressed_chars' are zero. [crates/gsqz/src/compressor.rs:296-304]
- `test_savings_pct_calculation` (function) component `test_savings_pct_calculation [function]` (`b8c1c8fa-0070-5933-9d6e-245777fa2bc3`) lines 307-315 [crates/gsqz/src/compressor.rs:307-315]
  - Signature: `fn test_savings_pct_calculation() {`
  - Purpose: Verifies that 'CompressionResult::savings_pct()' computes a 75.0% savings for a result with 1000 original characters and 250 compressed characters, allowing a 0.01 floating-point tolerance. [crates/gsqz/src/compressor.rs:307-315]
- `test_fallback_used_when_no_pipeline_matches` (function) component `test_fallback_used_when_no_pipeline_matches [function]` (`266e5f64-482b-55c8-b7b5-9d67b90ef67a`) lines 318-327 [crates/gsqz/src/compressor.rs:318-327]
  - Signature: `fn test_fallback_used_when_no_pipeline_matches() {`
  - Purpose: Verifies that when 'Compressor::compress' receives a command that matches no configured pipeline, it selects the 'fallback' strategy and returns passthrough-compressed output prefixed with '[gsqz:passthrough]\n'. [crates/gsqz/src/compressor.rs:318-327]
- `test_max_lines_cap_applied` (function) component `test_max_lines_cap_applied [function]` (`f53ea6fe-88b5-545b-a75d-043b12fb3f0a`) lines 330-345 [crates/gsqz/src/compressor.rs:330-345]
  - Signature: `fn test_max_lines_cap_applied() {`
  - Purpose: Verifies that 'Compressor::compress' truncates oversized output so the resulting compressed text contains no more than 'max_compressed_lines' plus a single omission marker line. [crates/gsqz/src/compressor.rs:330-345]
- `test_low_savings_fallback_keeps_passthrough_marker` (function) component `test_low_savings_fallback_keeps_passthrough_marker [function]` (`32305f32-7ea1-5474-9381-c4024de06ea4`) lines 348-358 [crates/gsqz/src/compressor.rs:348-358]
  - Signature: `fn test_low_savings_fallback_keeps_passthrough_marker() {`
  - Purpose: Verifies that when compressing 25 unique long lines yields insufficient savings, the compressor selects the 'fallback' strategy and preserves the '[gsqz:passthrough]' marker at the start of the output. [crates/gsqz/src/compressor.rs:348-358]
- `test_git_status_is_excluded` (function) component `test_git_status_is_excluded [function]` (`3d78adca-c8bc-599e-b8b2-3f9e690b7473`) lines 361-377 [crates/gsqz/src/compressor.rs:361-377]
  - Signature: `fn test_git_status_is_excluded() {`
  - Purpose: Verifies that 'Compressor::compress' treats a large 'git status' output as excluded, returning a passthrough result with unchanged content, equal character counts, and no compression marker. [crates/gsqz/src/compressor.rs:361-377]
- `test_builtin_excluded_commands_are_raw_passthrough` (function) component `test_builtin_excluded_commands_are_raw_passthrough [function]` (`c33da4f0-c953-5367-bae6-c676a18cee85`) lines 380-402 [crates/gsqz/src/compressor.rs:380-402]
  - Signature: `fn test_builtin_excluded_commands_are_raw_passthrough() {`
  - Purpose: Verifies that a 'Compressor' leaves output unchanged for a set of excluded built-in commands by selecting the 'excluded' strategy, preserving character counts, and reporting passthrough. [crates/gsqz/src/compressor.rs:380-402]
- `test_builtin_exclusion_runs_before_min_length` (function) component `test_builtin_exclusion_runs_before_min_length [function]` (`8d608421-dcf6-54b8-a137-75be748af06e`) lines 405-410 [crates/gsqz/src/compressor.rs:405-410]
  - Signature: `fn test_builtin_exclusion_runs_before_min_length() {`
  - Purpose: Verifies that built-in exclusion logic takes precedence over minimum-length compression by returning the '"excluded"' strategy and leaving the input unchanged for '"ok"'. [crates/gsqz/src/compressor.rs:405-410]
- `test_builtin_exclusion_matches_compound_segments` (function) component `test_builtin_exclusion_matches_compound_segments [function]` (`cf4732b9-64d1-5821-a2a4-3705327673a7`) lines 413-424 [crates/gsqz/src/compressor.rs:413-424]
  - Signature: `fn test_builtin_exclusion_matches_compound_segments() {`
  - Purpose: Verifies that the compressor excludes output for compound commands containing built-in exclusion segments like 'cargo test && git status', while not excluding a simple command such as 'grep git README.md'. [crates/gsqz/src/compressor.rs:413-424]
- `test_builtin_exclusion_matches_binary_paths` (function) component `test_builtin_exclusion_matches_binary_paths [function]` (`5731515f-0018-5229-abf5-d0843ad24b68`) lines 427-431 [crates/gsqz/src/compressor.rs:427-431]
  - Signature: `fn test_builtin_exclusion_matches_binary_paths() {`
  - Purpose: Verifies that 'Compressor::compress' classifies a command path under '/Users/josh/.gobby/bin/' as 'excluded' by asserting the resulting 'strategy_name' is '"excluded"'. [crates/gsqz/src/compressor.rs:427-431]
- `test_shell_inspection_commands_are_builtin_exclusions` (function) component `test_shell_inspection_commands_are_builtin_exclusions [function]` (`ee1f11f1-1d57-5a22-9afb-43f1ae8f1962`) lines 434-455 [crates/gsqz/src/compressor.rs:434-455]
  - Signature: `fn test_shell_inspection_commands_are_builtin_exclusions() {`
  - Purpose: Verifies that 'Compressor::compress' treats shell inspection commands like 'gh', 'rg', and 'sed' as excluded passthrough cases, leaving the output unchanged and marking the strategy as '"excluded"'. [crates/gsqz/src/compressor.rs:434-455]
- `test_first_command_token_skips_env_assignments` (function) component `test_first_command_token_skips_env_assignments [function]` (`59d025ad-0262-587a-9492-2dd770574b58`) lines 458-468 [crates/gsqz/src/compressor.rs:458-468]
  - Signature: `fn test_first_command_token_skips_env_assignments() {`
  - Purpose: Verifies that 'first_command_token' ignores leading environment assignments, returns the first executable path or command token ('cargo', '/usr/bin/git'), and returns 'None' when the input contains only assignments. [crates/gsqz/src/compressor.rs:458-468]
- `test_first_command_token_keeps_non_env_equals_tokens` (function) component `test_first_command_token_keeps_non_env_equals_tokens [function]` (`cb63f364-22c4-592c-9f81-e08b5588698d`) lines 471-481 [crates/gsqz/src/compressor.rs:471-481]
  - Signature: `fn test_first_command_token_keeps_non_env_equals_tokens() {`
  - Purpose: Verifies that 'first_command_token' returns the leading token as the command, treating tokens with '=' as ordinary arguments when they are not valid environment assignments, while still stopping before later 'foo=bar' tokens. [crates/gsqz/src/compressor.rs:471-481]
- `test_cargo_test_pipeline` (function) component `test_cargo_test_pipeline [function]` (`7c0e68a6-4150-5ff2-8eb2-77621155aeaf`) lines 484-493 [crates/gsqz/src/compressor.rs:484-493]
  - Signature: `fn test_cargo_test_pipeline() {`
  - Purpose: Verifies that 'Compressor::compress' selects the 'cargo-test' strategy when given 'cargo test' output containing many passing test lines and a final 'test result: ok' summary. [crates/gsqz/src/compressor.rs:484-493]
- `test_match_output_short_circuits` (function) component `test_match_output_short_circuits [function]` (`eef9e1ad-e0fa-5e69-9a86-87d8e9d0bb86`) lines 496-507 [crates/gsqz/src/compressor.rs:496-507]
  - Signature: `fn test_match_output_short_circuits() {`
  - Purpose: Verifies that the compressor’s 'cargo-test' strategy detects the '"test result: ok."' marker in long 'cargo test' output, short-circuits accordingly, and replaces the verbose log with the '"All tests passed."' summary. [crates/gsqz/src/compressor.rs:496-507]
- `test_match_output_unless_prevents_short_circuit` (function) component `test_match_output_unless_prevents_short_circuit [function]` (`80fb0fdb-a33d-5192-ae12-c2017805790b`) lines 510-523 [crates/gsqz/src/compressor.rs:510-523]
  - Signature: `fn test_match_output_unless_prevents_short_circuit() {`
  - Purpose: Verifies that 'Compressor::compress' uses the 'unless' guard to avoid the 'cargo-test' short-circuit when the test output contains 'FAILED', so the compressed result does not incorrectly report 'All tests passed.' [crates/gsqz/src/compressor.rs:510-523]
- `test_on_empty_global_fallback` (function) component `test_on_empty_global_fallback [function]` (`d748924c-2414-5716-9e6e-7a635ba939dd`) lines 526-548 [crates/gsqz/src/compressor.rs:526-548]
  - Signature: `fn test_on_empty_global_fallback() {`
  - Purpose: Verifies that when a pipeline filters all input to empty output, the compressor falls back to the global 'on_empty' message and reports an 'on_empty' strategy. [crates/gsqz/src/compressor.rs:526-548]
- `test_on_empty_pipeline_overrides_global` (function) component `test_on_empty_pipeline_overrides_global [function]` (`00260bd3-7b94-5050-87e1-8f9d438367cd`) lines 551-571 [crates/gsqz/src/compressor.rs:551-571]
  - Signature: `fn test_on_empty_pipeline_overrides_global() {`
  - Purpose: Verifies that when a pipeline-specific 'on_empty' message is configured, 'Compressor::compress' returns that pipeline override instead of the global 'settings.on_empty' after all lines are filtered out. [crates/gsqz/src/compressor.rs:551-571]
- `test_on_empty_not_used_when_output_nonempty` (function) component `test_on_empty_not_used_when_output_nonempty [function]` (`b197eca9-c3e2-5f6a-871d-972b88480059`) lines 574-583 [crates/gsqz/src/compressor.rs:574-583]
  - Signature: `fn test_on_empty_not_used_when_output_nonempty() {`
  - Purpose: Verifies that 'Compressor::compress' does not apply the 'on_empty' fallback text when the input output is nonempty, by asserting the compressed result omits '"Should not appear."'. [crates/gsqz/src/compressor.rs:574-583]
- `test_low_savings_pipeline_gets_marker` (function) component `test_low_savings_pipeline_gets_marker [function]` (`42e7086f-b4c2-5a60-93c6-30c01c7dd3df`) lines 586-618 [crates/gsqz/src/compressor.rs:586-618]
  - Signature: `fn test_low_savings_pipeline_gets_marker() {`
  - Purpose: Verifies that a named pipeline whose compression savings stay below the 5% threshold still receives the '[gsqz:low-savings]' marker when the marker overhead fits within the original size, and that the resulting compressed output is shorter than the input. [crates/gsqz/src/compressor.rs:586-618]
- `test_low_savings_suppressed_when_marker_would_grow_output` (function) component `test_low_savings_suppressed_when_marker_would_grow_output [function]` (`52ce9ccd-bfb7-54df-ad64-53574fb8f51d`) lines 621-646 [crates/gsqz/src/compressor.rs:621-646]
  - Signature: `fn test_low_savings_suppressed_when_marker_would_grow_output() {`
  - Purpose: Verifies that when a named pipeline yields zero compression savings, 'Compressor::compress' returns the original output unchanged with strategy name 'noop-pipeline/no-op', omits the '[gsqz:low-savings]' marker, preserves equal compressed and original character counts, and reports passthrough mode. [crates/gsqz/src/compressor.rs:621-646]
- `test_is_passthrough_classification` (function) component `test_is_passthrough_classification [function]` (`244f4e2e-f09d-5630-be63-93e3c2b43aca`) lines 649-666 [crates/gsqz/src/compressor.rs:649-666]
  - Signature: `fn test_is_passthrough_classification() {`
  - Purpose: This test verifies that 'CompressionResult::is_passthrough()' returns 'true' only for strategy names that represent verbatim output paths ('passthrough', 'excluded', 'pytest/no-op', 'cargo-test/no-op') and 'false' for strategies that perform or imply real compression ('pytest', 'cargo-test/low-savings', 'pytest/on_empty', 'fallback'). [crates/gsqz/src/compressor.rs:649-666]
- `test_good_compression_has_no_marker` (function) component `test_good_compression_has_no_marker [function]` (`10e4d22b-0b39-5ef2-a0a7-d255fa00f24e`) lines 669-678 [crates/gsqz/src/compressor.rs:669-678]
  - Signature: `fn test_good_compression_has_no_marker() {`
  - Purpose: Verifies that compressing successful 'cargo test' output with 'Compressor::compress' does not insert a '[gsqz:' marker into the compressed result. [crates/gsqz/src/compressor.rs:669-678]
- `test_compound_command_matches_last_segment` (function) component `test_compound_command_matches_last_segment [function]` (`575ed30f-5095-58fa-812e-162379f98752`) lines 681-691 [crates/gsqz/src/compressor.rs:681-691]
  - Signature: `fn test_compound_command_matches_last_segment() {`
  - Purpose: Verifies that 'Compressor::compress' selects the 'cargo-test' strategy for a compound command by matching the last command segment ('cargo test') in '"cargo build && cargo test"'. [crates/gsqz/src/compressor.rs:681-691]
- `test_compound_single_command_unchanged` (function) component `test_compound_single_command_unchanged [function]` (`72a1f9c8-eee3-5eef-bc85-65940de1b80c`) lines 694-702 [crates/gsqz/src/compressor.rs:694-702]
  - Signature: `fn test_compound_single_command_unchanged() {`
  - Purpose: Verifies that compressing output for an unrecognized single command uses the 'fallback' strategy and leaves behavior unchanged. [crates/gsqz/src/compressor.rs:694-702]
- `test_compound_falls_back_to_earlier_segment` (function) component `test_compound_falls_back_to_earlier_segment [function]` (`25be7ab4-68f7-58ee-b58b-f9777d5d464c`) lines 705-715 [crates/gsqz/src/compressor.rs:705-715]
  - Signature: `fn test_compound_falls_back_to_earlier_segment() {`
  - Purpose: Verifies that 'Compressor::compress' selects the earlier matching 'cargo-test' pipeline when the final command segment ('unknown-cmd') has no match, even if the output matches that earlier segment’s test log pattern. [crates/gsqz/src/compressor.rs:705-715]

