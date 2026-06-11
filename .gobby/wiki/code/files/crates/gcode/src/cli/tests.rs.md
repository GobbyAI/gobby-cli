---
title: crates/gcode/src/cli/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/cli/tests.rs
  ranges:
  - 5-213
  - 216-234
  - 237-252
  - 255-270
  - 273-288
  - 291-298
  - 301-312
  - 315-348
  - 351-359
  - 362-372
  - 375-394
  - 397-415
  - 418-440
  - 443-461
  - 464-478
  - 481-488
  - 491-503
  - 506-511
  - 514-528
  - 531-559
  - 562-614
  - 617-636
  - 639-646
  - 649-658
  - 661-693
  - 696-726
  - 729-784
  - 787-796
  - 799-808
  - 811-821
  - 824-835
  - 838-850
  - 853-876
  - 879-887
  - 890-899
  - 902-913
  - 916-924
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/cli/tests.rs

Module: [[code/modules/crates/gcode/src/cli|crates/gcode/src/cli]]

## Purpose

`crates/gcode/src/cli/tests.rs` exposes 37 indexed API symbols.
[crates/gcode/src/cli/tests.rs:5-213]
[crates/gcode/src/cli/tests.rs:216-234]
[crates/gcode/src/cli/tests.rs:237-252]
[crates/gcode/src/cli/tests.rs:255-270]
[crates/gcode/src/cli/tests.rs:273-288]

## API Symbols

- `parse_projection_lifecycle_commands` (function) component `parse_projection_lifecycle_commands [function]` (`9c741412-7933-5ef9-828a-c7cbed61eb6c`) lines 5-213 [crates/gcode/src/cli/tests.rs:5-213]
  - Signature: `fn parse_projection_lifecycle_commands() {`
  - Purpose: Unit test that validates parsing of projection lifecycle subcommands (`sync-file`, `clear`, `rebuild`) for `graph` and `vector` commands with various optional flags and arguments. [crates/gcode/src/cli/tests.rs:5-213]
- `parse_graph_report_global_format` (function) component `parse_graph_report_global_format [function]` (`d7c125ef-0fcc-56ab-bfce-52398aec3be3`) lines 216-234 [crates/gcode/src/cli/tests.rs:216-234]
  - Signature: `fn parse_graph_report_global_format() {`
  - Purpose: Tests CLI argument parsing for the graph report command, validating that `--top-n` and `--format` arguments are correctly parsed while unknown arguments like `--limit` are rejected. [crates/gcode/src/cli/tests.rs:216-234]
- `test_parse_index_require_cpp_semantics` (function) component `test_parse_index_require_cpp_semantics [function]` (`fc8a3ded-0516-5e00-9fe7-a613b72cc2bf`) lines 237-252 [crates/gcode/src/cli/tests.rs:237-252]
  - Signature: `fn test_parse_index_require_cpp_semantics() {`
  - Purpose: Test that verifies parsing `gcode index --require-cpp-semantics` produces an Index command variant with `require_cpp_semantics=true` and `sync_projections=false`. [crates/gcode/src/cli/tests.rs:237-252]
- `test_parse_callers_remains_top_level` (function) component `test_parse_callers_remains_top_level [function]` (`1d0d67ea-99c9-5868-b106-04cdbb46b7fc`) lines 255-270 [crates/gcode/src/cli/tests.rs:255-270]
  - Signature: `fn test_parse_callers_remains_top_level() {`
  - Purpose: This test verifies that the CLI parser correctly parses the top-level `callers` subcommand with a symbol name argument and applies default values of 10 for limit and 0 for offset. [crates/gcode/src/cli/tests.rs:255-270]
- `test_parse_usages_remains_top_level` (function) component `test_parse_usages_remains_top_level [function]` (`f08b3ddb-160c-5181-abe3-ceb46260ceec`) lines 273-288 [crates/gcode/src/cli/tests.rs:273-288]
  - Signature: `fn test_parse_usages_remains_top_level() {`
  - Purpose: This test verifies that the CLI parser correctly parses a top-level `usages` subcommand with a symbol name argument and applies default values for limit (10) and offset (0). [crates/gcode/src/cli/tests.rs:273-288]
- `test_parse_imports_remains_top_level` (function) component `test_parse_imports_remains_top_level [function]` (`b37dcc5d-3d2e-5eb1-826e-71b807a59f48`) lines 291-298 [crates/gcode/src/cli/tests.rs:291-298]
  - Signature: `fn test_parse_imports_remains_top_level() {`
  - Purpose: This test verifies that the CLI parser correctly parses the top-level `imports` subcommand and captures the file argument into the `Command::Imports` variant. [crates/gcode/src/cli/tests.rs:291-298]
- `test_parse_blast_radius_remains_top_level` (function) component `test_parse_blast_radius_remains_top_level [function]` (`3692d049-bcce-5629-9ab8-51d4ce433c50`) lines 301-312 [crates/gcode/src/cli/tests.rs:301-312]
  - Signature: `fn test_parse_blast_radius_remains_top_level() {`
  - Purpose: Tests that the blast-radius subcommand correctly parses 'handleAuth' as its target argument with a default depth value of 3 at the top level of the CLI command hierarchy. [crates/gcode/src/cli/tests.rs:301-312]
- `test_parse_search_symbol_filters` (function) component `test_parse_search_symbol_filters [function]` (`96d50dd6-56ec-5bca-9797-25ffb2a24856`) lines 315-348 [crates/gcode/src/cli/tests.rs:315-348]
  - Signature: `fn test_parse_search_symbol_filters() {`
  - Purpose: This test verifies that `Cli::try_parse_from` correctly parses and assigns the `search-symbol` subcommand's positional/optional arguments and their default values (limit=10, offset=0, with_graph=false). [crates/gcode/src/cli/tests.rs:315-348]
- `test_parse_search_symbol_with_graph` (function) component `test_parse_search_symbol_with_graph [function]` (`c51f13d4-9b81-550e-8457-3adf2d176229`) lines 351-359 [crates/gcode/src/cli/tests.rs:351-359]
  - Signature: `fn test_parse_search_symbol_with_graph() {`
  - Purpose: # Summary

Tests that the CLI parser correctly sets the `with_graph` boolean flag to `true` when parsing the `search-symbol` command with the `--with-graph` argument. [crates/gcode/src/cli/tests.rs:351-359]
- `test_parse_search_language_filters` (function) component `test_parse_search_language_filters [function]` (`b0718bf1-d30c-5c3b-9da3-050d32f7d716`) lines 362-372 [crates/gcode/src/cli/tests.rs:362-372]
  - Signature: `fn test_parse_search_language_filters() {`
  - Purpose: This test asserts that the CLI argument parser correctly deserializes the `--language rust` flag into the `language` field of a `Search` command variant. [crates/gcode/src/cli/tests.rs:362-372]
- `test_parse_search_positional_paths` (function) component `test_parse_search_positional_paths [function]` (`00dbdfe0-4b8f-5f24-9a29-ce8966da102d`) lines 375-394 [crates/gcode/src/cli/tests.rs:375-394]
  - Signature: `fn test_parse_search_positional_paths() {`
  - Purpose: This test verifies that the CLI argument parser correctly extracts positional path arguments and the `--limit` flag value from a search command invocation. [crates/gcode/src/cli/tests.rs:375-394]
- `test_parse_search_text_positional_path_after_option` (function) component `test_parse_search_text_positional_path_after_option [function]` (`57311634-100e-5bb4-81f5-39e6837bc818`) lines 397-415 [crates/gcode/src/cli/tests.rs:397-415]
  - Signature: `fn test_parse_search_text_positional_path_after_option() {`
  - Purpose: Verifies that the search-text subcommand parser correctly captures a positional path argument positioned after an option-value pair. [crates/gcode/src/cli/tests.rs:397-415]
- `test_parse_search_content_positional_paths_and_format` (function) component `test_parse_search_content_positional_paths_and_format [function]` (`d11ba557-7d75-5d1f-872b-d5a2d849e310`) lines 418-440 [crates/gcode/src/cli/tests.rs:418-440]
  - Signature: `fn test_parse_search_content_positional_paths_and_format() {`
  - Purpose: Tests that the CLI parser correctly parses the `search-content` subcommand with a query argument, multiple positional file paths, and named `--limit` and `--format` options. [crates/gcode/src/cli/tests.rs:418-440]
- `test_parse_search_content_positional_path_after_option` (function) component `test_parse_search_content_positional_path_after_option [function]` (`1bf6d286-1d88-537a-ab8e-27329f738e83`) lines 443-461 [crates/gcode/src/cli/tests.rs:443-461]
  - Signature: `fn test_parse_search_content_positional_path_after_option() {`
  - Purpose: This test verifies that the CLI parser correctly recognizes a positional path argument (`src/gobby`) when it appears after an option-value pair (`--limit 5`) in the `search-content` command. [crates/gcode/src/cli/tests.rs:443-461]
- `test_parse_search_path_flag_rejected` (function) component `test_parse_search_path_flag_rejected [function]` (`b0438a53-61e7-589f-b46b-7fd24a965d2d`) lines 464-478 [crates/gcode/src/cli/tests.rs:464-478]
  - Signature: `fn test_parse_search_path_flag_rejected() {`
  - Purpose: Validates that the `--path` flag produces an `UnknownArgument` error when parsed with all search command variants (search, search-symbol, search-text, search-content). [crates/gcode/src/cli/tests.rs:464-478]
- `top_level_help_includes_agent_task_examples` (function) component `top_level_help_includes_agent_task_examples [function]` (`b109dc9a-f0c3-5875-b206-237f2beacba6`) lines 481-488 [crates/gcode/src/cli/tests.rs:481-488]
  - Signature: `fn top_level_help_includes_agent_task_examples() {`
  - Purpose: This test function verifies that the CLI's top-level help output includes four example `gcode` commands demonstrating symbol search, code grep, and symbol lookup operations. [crates/gcode/src/cli/tests.rs:481-488]
- `search_help_routes_literal_and_ranked_content_queries` (function) component `search_help_routes_literal_and_ranked_content_queries [function]` (`4d4500ab-b067-5900-96d6-b99eeb6dce2b`) lines 491-503 [crates/gcode/src/cli/tests.rs:491-503]
  - Signature: `fn search_help_routes_literal_and_ranked_content_queries() {`
  - Purpose: Validates that the search subcommand's help text documents both literal query routes (grep patterns, exact matches, config keys) and ranked content query routes (hybrid/fuzzy concept search). [crates/gcode/src/cli/tests.rs:491-503]
- `test_parse_no_freshness_global_flag` (function) component `test_parse_no_freshness_global_flag [function]` (`3518e280-04a4-5b2c-999f-805a9c959939`) lines 506-511 [crates/gcode/src/cli/tests.rs:506-511]
  - Signature: `fn test_parse_no_freshness_global_flag() {`
  - Purpose: Tests that the CLI parser correctly recognizes the `--no-freshness` global flag and parses `tree` as the active subcommand. [crates/gcode/src/cli/tests.rs:506-511]
- `parse_codewiki_ai_flag` (function) component `parse_codewiki_ai_flag [function]` (`cc695152-b17b-5865-806e-8e13cf1ffd68`) lines 514-528 [crates/gcode/src/cli/tests.rs:514-528]
  - Signature: `fn parse_codewiki_ai_flag() {`
  - Purpose: This test function validates that the CLI parser correctly maps the four string values ('auto', 'daemon', 'direct', 'off') to their corresponding `AiRouteArg` enum variants when passed to the codewiki command's `--ai` flag. [crates/gcode/src/cli/tests.rs:514-528]
- `parse_codewiki_edge_limit_flag` (function) component `parse_codewiki_edge_limit_flag [function]` (`17dc8c95-d813-5784-9d05-be8c905c7fcd`) lines 531-559 [crates/gcode/src/cli/tests.rs:531-559]
  - Signature: `fn parse_codewiki_edge_limit_flag() {`
  - Purpose: Unit test that validates the CLI parser's handling of the `--edge-limit` flag in the `codewiki` subcommand, verifying default value assignment, custom value acceptance, and rejection of zero and oversized inputs with appropriate error messages. [crates/gcode/src/cli/tests.rs:531-559]
- `parse_setup_standalone` (function) component `parse_setup_standalone [function]` (`fb6c5404-cd34-5039-a4bd-cdd8ab0c0244`) lines 562-614 [crates/gcode/src/cli/tests.rs:562-614]
  - Signature: `fn parse_setup_standalone() {`
  - Purpose: This function validates that the CLI parser correctly extracts all configuration parameters from a standalone setup command invocation, including database URL, embedding provider type, query prefix, vector dimensionality, and credentials. [crates/gcode/src/cli/tests.rs:562-614]
- `parse_grep_basic` (function) component `parse_grep_basic [function]` (`30e3a1a0-c154-5df2-bf00-e5affbcfd97a`) lines 617-636 [crates/gcode/src/cli/tests.rs:617-636]
  - Signature: `fn parse_grep_basic() {`
  - Purpose: This function is a unit test that verifies the CLI parser correctly deserializes a grep command with pattern "needle", path "src", and all boolean flags (fixed_strings, ignore_case, word) defaulting to false. [crates/gcode/src/cli/tests.rs:617-636]
- `parse_grep_ignore_case` (function) component `parse_grep_ignore_case [function]` (`3d48f22c-5145-505c-9650-6d373361aaed`) lines 639-646 [crates/gcode/src/cli/tests.rs:639-646]
  - Signature: `fn parse_grep_ignore_case() {`
  - Purpose: This function tests that the CLI parser correctly parses the `--ignore-case` flag for the `grep` command and asserts the resulting `ignore_case` field is `true`. [crates/gcode/src/cli/tests.rs:639-646]
- `parse_grep_word` (function) component `parse_grep_word [function]` (`b94a2778-9e2b-540d-8ab8-03b369075a15`) lines 649-658 [crates/gcode/src/cli/tests.rs:649-658]
  - Signature: `fn parse_grep_word() {`
  - Purpose: Tests that the CLI parser correctly parses the `grep -w note_path` command, validating extraction of the pattern argument and confirmation of the word-match flag. [crates/gcode/src/cli/tests.rs:649-658]
- `parse_grep_word_long_with_fixed_json` (function) component `parse_grep_word_long_with_fixed_json [function]` (`ccbd1042-b3a8-5eba-95b6-e01ce9f02e3f`) lines 661-693 [crates/gcode/src/cli/tests.rs:661-693]
  - Signature: `fn parse_grep_word_long_with_fixed_json() {`
  - Purpose: This test function verifies that the CLI parser correctly parses a grep command with word-boundary matching (`--word`), fixed-string search (`-F`), a maximum of 50 results (`-m 50`), and JSON output format options. [crates/gcode/src/cli/tests.rs:661-693]
- `parse_grep_with_flags` (function) component `parse_grep_with_flags [function]` (`3f87276e-1133-5b86-af2b-2390ccda6c36`) lines 696-726 [crates/gcode/src/cli/tests.rs:696-726]
  - Signature: `fn parse_grep_with_flags() {`
  - Purpose: This function is a unit test that verifies the CLI argument parser correctly extracts the grep pattern, file paths, and command-line flags (-F for fixed strings, -C for context lines, -g for glob filtering) from parsed input. [crates/gcode/src/cli/tests.rs:696-726]
- `parse_grep_max_count` (function) component `parse_grep_max_count [function]` (`eed18059-ffa2-5a90-801a-fae98c5c167a`) lines 729-784 [crates/gcode/src/cli/tests.rs:729-784]
  - Signature: `fn parse_grep_max_count() {`
  - Purpose: This test function verifies that the grep CLI parser correctly handles the `-m`/`--max-count` option in multiple argument positions and rejects values exceeding the maximum threshold of 10000. [crates/gcode/src/cli/tests.rs:729-784]
- `parse_grep_rejects_limit` (function) component `parse_grep_rejects_limit [function]` (`29c79d7c-9cd9-5220-b2d2-fb1b8bab7339`) lines 787-796 [crates/gcode/src/cli/tests.rs:787-796]
  - Signature: `fn parse_grep_rejects_limit() {`
  - Purpose: Validates that Clap's argument parser rejects the `--limit` flag as an unexpected argument for the `gcode grep` subcommand. [crates/gcode/src/cli/tests.rs:787-796]
- `parse_grep_rejects_line_number_flag` (function) component `parse_grep_rejects_line_number_flag [function]` (`5eab7ad4-9146-51d8-aa70-0729e1e2e4d0`) lines 799-808 [crates/gcode/src/cli/tests.rs:799-808]
  - Signature: `fn parse_grep_rejects_line_number_flag() {`
  - Purpose: This function is a test that verifies the grep subcommand's argument parser correctly rejects the `-n` (line-number) flag and produces an "unexpected argument" error. [crates/gcode/src/cli/tests.rs:799-808]
- `parse_grep_rejects_empty_pattern` (function) component `parse_grep_rejects_empty_pattern [function]` (`d221cdf1-781a-5038-8ebf-d04746c6f202`) lines 811-821 [crates/gcode/src/cli/tests.rs:811-821]
  - Signature: `fn parse_grep_rejects_empty_pattern() {`
  - Purpose: Asserts that the CLI parser rejects empty patterns for the grep subcommand and validates the error message states "gcode grep pattern cannot be empty." [crates/gcode/src/cli/tests.rs:811-821]
- `parse_grep_unsupported_flag_fails_before_context_resolution` (function) component `parse_grep_unsupported_flag_fails_before_context_resolution [function]` (`99a75153-06d2-5af8-b960-20171a4bc9f8`) lines 824-835 [crates/gcode/src/cli/tests.rs:824-835]
  - Signature: `fn parse_grep_unsupported_flag_fails_before_context_resolution() {`
  - Purpose: This test verifies that the CLI parser rejects the unsupported `--files-with-matches` flag for the grep subcommand during argument parsing, producing an "unexpected argument" error before context resolution. [crates/gcode/src/cli/tests.rs:824-835]
- `parse_grep_unsupported_flag_after_path_fails_in_clap` (function) component `parse_grep_unsupported_flag_after_path_fails_in_clap [function]` (`41bdaeb5-7f96-5b24-8cf0-bae525456b4f`) lines 838-850 [crates/gcode/src/cli/tests.rs:838-850]
  - Signature: `fn parse_grep_unsupported_flag_after_path_fails_in_clap() {`
  - Purpose: Asserts that CLI argument parsing fails with an "unexpected argument" error when a flag (`--files-with-matches`) is positioned after a positional path argument in a grep subcommand. [crates/gcode/src/cli/tests.rs:838-850]
- `parse_graph_sync_file_with_flag` (function) component `parse_graph_sync_file_with_flag [function]` (`66252b91-b4fe-5a32-9402-5fa057f238ac`) lines 853-876 [crates/gcode/src/cli/tests.rs:853-876]
  - Signature: `fn parse_graph_sync_file_with_flag() {`
  - Purpose: Tests that the CLI parser correctly parses the `graph sync-file` subcommand with `--file src/lib.rs --allow-missing-indexed-file` into the `GraphCommand::SyncFile` variant with expected field values. [crates/gcode/src/cli/tests.rs:853-876]
- `parse_grep_with_global_format` (function) component `parse_grep_with_global_format [function]` (`0d69e5a4-0225-503b-a866-b975cb7f74ec`) lines 879-887 [crates/gcode/src/cli/tests.rs:879-887]
  - Signature: `fn parse_grep_with_global_format() {`
  - Purpose: This test function validates that the CLI parser correctly interprets a global `--format text` flag preceding a `grep` subcommand, asserting both the format output type and the grep pattern are properly parsed. [crates/gcode/src/cli/tests.rs:879-887]
- `effective_format_defaults_grep_to_text` (function) component `effective_format_defaults_grep_to_text [function]` (`c92485b7-171b-5bcc-b1fc-aeedec156d93`) lines 890-899 [crates/gcode/src/cli/tests.rs:890-899]
  - Signature: `fn effective_format_defaults_grep_to_text() {`
  - Purpose: This unit test verifies that `effective_format` defaults to `output::Format::Text` when no explicit format is specified for a grep command. [crates/gcode/src/cli/tests.rs:890-899]
- `effective_format_honors_explicit_grep_json` (function) component `effective_format_honors_explicit_grep_json [function]` (`0474b35f-05d2-59f9-9226-2fe181b44463`) lines 902-913 [crates/gcode/src/cli/tests.rs:902-913]
  - Signature: `fn effective_format_honors_explicit_grep_json() {`
  - Purpose: Tests that the `effective_format` function returns `output::Format::Json` when the CLI explicitly specifies `--format json` in a grep command. [crates/gcode/src/cli/tests.rs:902-913]
- `effective_format_keeps_other_commands_json_by_default` (function) component `effective_format_keeps_other_commands_json_by_default [function]` (`cd9492ef-bfe0-5848-82f1-913b7776cfbb`) lines 916-924 [crates/gcode/src/cli/tests.rs:916-924]
  - Signature: `fn effective_format_keeps_other_commands_json_by_default() {`
  - Purpose: Verifies that the `effective_format` function defaults to JSON output format when no explicit format is specified for the search-content command. [crates/gcode/src/cli/tests.rs:916-924]

