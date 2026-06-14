---
title: crates/gsqz/src/primitives/group.rs
type: code_file
provenance:
- file: crates/gsqz/src/primitives/group.rs
  ranges:
  - 8-21
  - 28-79
  - 99-183
  - 187-243
  - 247-296
  - 304-344
  - 348-387
  - 391-428
  - 434-475
  - 482-525
  - 532-543
  - 546-556
  - 559-567
  - 570-574
  - 577-581
  - 584-587
  - 590-595
  - 598-606
  - 609-623
  - 626-634
  - 637-650
  - 653-665
  - 668-681
  - 684-709
  - 712-716
  - 719-734
  - 737-750
  - 753-770
  - 773-781
  - 784-793
  - 796-805
  - 808-812
  - 815-822
  - 825-834
  - 837-840
  - 843-849
  - 852-861
  - 864-868
  - 871-880
  - 883-887
  - 890-901
  - 904-908
  - 911-921
  - 924-929
  - 932-940
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/primitives/group.rs

Module: [[code/modules/crates/gsqz/src/primitives|crates/gsqz/src/primitives]]

## Purpose

Provides a small output-normalization layer for grouping and summarizing line-oriented command results. `group_lines` dispatches to mode-specific helpers, and those helpers reshape common noisy outputs into compact, human-readable sections: git status and diff summaries, pytest and test failure extraction, lint grouping by rule, and file/path grouping by extension, directory, or filename, plus generic error/warning aggregation. The file also includes unit tests that verify the dispatcher behavior, grouping classification, truncation limits, and passthrough cases.
[crates/gsqz/src/primitives/group.rs:8-21]
[crates/gsqz/src/primitives/group.rs:28-79]
[crates/gsqz/src/primitives/group.rs:99-183]
[crates/gsqz/src/primitives/group.rs:187-243]
[crates/gsqz/src/primitives/group.rs:247-296]

## API Symbols

- `group_lines` (function) component `group_lines [function]` (`95102c90-3c76-5929-9b47-25cda49173c9`) lines 8-21 [crates/gsqz/src/primitives/group.rs:8-21]
  - Signature: `pub fn group_lines(lines: Vec<String>, mode: &str) -> Vec<String> {`
  - Purpose: Routes a vector of strings to one of nine mode-specific grouping functions via pattern matching, returning the unmodified input if the mode is unrecognized. [crates/gsqz/src/primitives/group.rs:8-21]
- `group_git_status` (function) component `group_git_status [function]` (`3870c8ea-daae-5054-97ec-c28cb949a695`) lines 28-79 [crates/gsqz/src/primitives/group.rs:28-79]
  - Signature: `fn group_git_status(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Parses git status lines using regex, groups files by their status code, and returns formatted output grouped by status type with human-readable labels, file counts, and truncation at 20 files per group. [crates/gsqz/src/primitives/group.rs:28-79]
- `group_git_diff` (function) component `group_git_diff [function]` (`46a62353-d5f2-5d00-9101-be5762be5a46`) lines 99-183 [crates/gsqz/src/primitives/group.rs:99-183]
  - Signature: `fn group_git_diff(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Partitions a git diff into file sections and returns a condensed summary with each file's addition/deletion counts and type classification (binary, lock file, or generated code). [crates/gsqz/src/primitives/group.rs:99-183]
- `group_pytest_failures` (function) component `group_pytest_failures [function]` (`66cb62e2-31a9-51ab-9093-71614885da97`) lines 187-243 [crates/gsqz/src/primitives/group.rs:187-243]
  - Signature: `fn group_pytest_failures(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Filters pytest output lines to extract and preserve failure, error, warning, and summary report sections using stateful regex pattern matching, with fallback to an alternative grouping function if no patterns match. [crates/gsqz/src/primitives/group.rs:187-243]
- `group_test_failures` (function) component `group_test_failures [function]` (`efd37613-da20-5fbf-9c5d-1ab33c9053a6`) lines 247-296 [crates/gsqz/src/primitives/group.rs:247-296]
  - Signature: `fn group_test_failures(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Extracts test failure content by collecting output lines from the first detected failure/error marker onward, with fallback to test result summary or default success message. [crates/gsqz/src/primitives/group.rs:247-296]
- `group_lint_by_rule` (function) component `group_lint_by_rule [function]` (`71101fc0-db55-51a8-91df-d07e93649273`) lines 304-344 [crates/gsqz/src/primitives/group.rs:304-344]
  - Signature: `fn group_lint_by_rule(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Groups lint output lines by extracted rule identifiers using regex matching and returns a formatted summary with occurrence counts and up to 5 sample lines per rule, maintaining order of first appearance. [crates/gsqz/src/primitives/group.rs:304-344]
- `group_by_extension` (function) component `group_by_extension [function]` (`d3c60b51-d1f1-58ff-9372-db73d73b6e9f`) lines 348-387 [crates/gsqz/src/primitives/group.rs:348-387]
  - Signature: `fn group_by_extension(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Groups input lines by file extension (extracted from the final whitespace-delimited token), sorts groups by descending cardinality, and returns formatted output with headers and up to 10 samples per extension. [crates/gsqz/src/primitives/group.rs:348-387]
- `group_by_directory` (function) component `group_by_directory [function]` (`1e2eeb86-7b54-58a8-9e75-9edb9e4f1d30`) lines 391-428 [crates/gsqz/src/primitives/group.rs:391-428]
  - Signature: `fn group_by_directory(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Groups file paths by their directory component, sorts directory groups by descending item count, and returns formatted output with directory headers and file listings truncated to 10 items per group. [crates/gsqz/src/primitives/group.rs:391-428]
- `group_by_file` (function) component `group_by_file [function]` (`460b6fc4-fcd9-5560-93c9-d110e3325708`) lines 434-475 [crates/gsqz/src/primitives/group.rs:434-475]
  - Signature: `fn group_by_file(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Formats grep-style output lines grouped by source filename with match counts, limiting display to five matches per file with overflow indicators while preserving non-matching lines. [crates/gsqz/src/primitives/group.rs:434-475]
- `group_errors_warnings` (function) component `group_errors_warnings [function]` (`8918cfc8-ed39-5d2d-9338-b2c301df4d96`) lines 482-525 [crates/gsqz/src/primitives/group.rs:482-525]
  - Signature: `fn group_errors_warnings(lines: Vec<String>) -> Vec<String> {`
  - Purpose: Partitions input lines by regex-matched errors and warnings, returning a reorganized vector with truncated groups (first 20 errors, first 10 warnings) and trailing summary lines, or the original vector if no errors/warnings are found. [crates/gsqz/src/primitives/group.rs:482-525]
- `test_git_status_grouping` (function) component `test_git_status_grouping [function]` (`dec6ba3c-7af8-5082-947e-835cc0bf95a8`) lines 532-543 [crates/gsqz/src/primitives/group.rs:532-543]
  - Signature: `fn test_git_status_grouping() {`
  - Purpose: Verifies that `group_git_status` correctly categorizes git status output lines by file state (Modified, Untracked, Deleted) and produces aggregated count summaries for each category. [crates/gsqz/src/primitives/group.rs:532-543]
- `test_errors_warnings_grouping` (function) component `test_errors_warnings_grouping [function]` (`32b44318-1705-5255-851a-70fd9d140cb5`) lines 546-556 [crates/gsqz/src/primitives/group.rs:546-556]
  - Signature: `fn test_errors_warnings_grouping() {`
  - Purpose: This unit test verifies that `group_errors_warnings` correctly groups and counts diagnostic messages by severity level, returning results indicating 2 errors and 1 warning from a mixed-severity log line set. [crates/gsqz/src/primitives/group.rs:546-556]
- `test_all_tests_passed` (function) component `test_all_tests_passed [function]` (`899f1756-faff-56c3-85b6-d79300f94cab`) lines 559-567 [crates/gsqz/src/primitives/group.rs:559-567]
  - Signature: `fn test_all_tests_passed() {`
  - Purpose: Unit test verifying that `group_test_failures()` returns a single-element vector containing `"All tests passed.\n"` when processing test output with no failures. [crates/gsqz/src/primitives/group.rs:559-567]
- `test_group_lines_dispatcher_unknown_mode` (function) component `test_group_lines_dispatcher_unknown_mode [function]` (`fbde926b-60ee-58cf-86c3-5bfc072d2693`) lines 570-574 [crates/gsqz/src/primitives/group.rs:570-574]
  - Signature: `fn test_group_lines_dispatcher_unknown_mode() {`
  - Purpose: This test verifies that `group_lines()` returns the input vector unmodified when called with a non-existent mode parameter. [crates/gsqz/src/primitives/group.rs:570-574]
- `test_group_lines_dispatcher_git_status` (function) component `test_group_lines_dispatcher_git_status [function]` (`a607594e-c9b4-5934-9af3-2c296bf5df18`) lines 577-581 [crates/gsqz/src/primitives/group.rs:577-581]
  - Signature: `fn test_group_lines_dispatcher_git_status() {`
  - Purpose: Tests that `group_lines` with the `git_status` dispatcher correctly parses a modified file indicator (` M foo.rs`) and produces output containing "Modified". [crates/gsqz/src/primitives/group.rs:577-581]
- `test_git_status_empty` (function) component `test_git_status_empty [function]` (`6932038a-07bd-5b03-8be6-22913ed0ec6a`) lines 584-587 [crates/gsqz/src/primitives/group.rs:584-587]
  - Signature: `fn test_git_status_empty() {`
  - Purpose: This unit test verifies that the `group_git_status` function returns an empty collection when passed an empty input vector. [crates/gsqz/src/primitives/group.rs:584-587]
- `test_git_status_non_status_lines` (function) component `test_git_status_non_status_lines [function]` (`9a7fbd39-5751-5310-af99-f3bdc7ba7b4f`) lines 590-595 [crates/gsqz/src/primitives/group.rs:590-595]
  - Signature: `fn test_git_status_non_status_lines() {`
  - Purpose: Unit test verifying that `group_git_status` classifies and returns non-matching git status output lines unchanged as the "other" grouping. [crates/gsqz/src/primitives/group.rs:590-595]
- `test_git_status_many_files_truncated` (function) component `test_git_status_many_files_truncated [function]` (`229484c2-5086-5772-b8fa-2bb9eee8dc2b`) lines 598-606 [crates/gsqz/src/primitives/group.rs:598-606]
  - Signature: `fn test_git_status_many_files_truncated() {`
  - Purpose: Verifies that `group_git_status` aggregates 30 modified files into a truncated summary displaying the total count ("Modified (30)") and a remainder indicator ("and 10 more"). [crates/gsqz/src/primitives/group.rs:598-606]
- `test_git_diff_lock_file_collapsed` (function) component `test_git_diff_lock_file_collapsed [function]` (`7ca0ed68-9605-579b-9e6d-408a3ba81d13`) lines 609-623 [crates/gsqz/src/primitives/group.rs:609-623]
  - Signature: `fn test_git_diff_lock_file_collapsed() {`
  - Purpose: Tests that `group_git_diff` collapses a Cargo.lock file diff into a single grouped entry with `[lock]` prefix and aggregated change statistics. [crates/gsqz/src/primitives/group.rs:609-623]
- `test_git_diff_binary_collapsed` (function) component `test_git_diff_binary_collapsed [function]` (`4213e21c-d950-5fba-9fb1-4b502a646071`) lines 626-634 [crates/gsqz/src/primitives/group.rs:626-634]
  - Signature: `fn test_git_diff_binary_collapsed() {`
  - Purpose: Tests that `group_git_diff()` correctly collapses a binary file diff into a single formatted entry prefixed with `[binary]`. [crates/gsqz/src/primitives/group.rs:626-634]
- `test_git_diff_generated_collapsed` (function) component `test_git_diff_generated_collapsed [function]` (`7350c4a9-5eea-598d-adcd-50b463f41f2b`) lines 637-650 [crates/gsqz/src/primitives/group.rs:637-650]
  - Signature: `fn test_git_diff_generated_collapsed() {`
  - Purpose: Tests that `group_git_diff` correctly groups a git diff of a generated minified JavaScript file into a single entry with the file path and change count metadata (+1, -1). [crates/gsqz/src/primitives/group.rs:637-650]
- `test_git_diff_normal_file_kept` (function) component `test_git_diff_normal_file_kept [function]` (`ff9d544e-c189-5753-9650-60b611d76675`) lines 653-665 [crates/gsqz/src/primitives/group.rs:653-665]
  - Signature: `fn test_git_diff_normal_file_kept() {`
  - Purpose: # Summary

Tests that `group_git_diff` returns the input lines unchanged when processing a standard git unified diff format. [crates/gsqz/src/primitives/group.rs:653-665]
- `test_git_diff_large_file_truncated` (function) component `test_git_diff_large_file_truncated [function]` (`83a6a86c-625c-58a7-945b-1bfbaf86de3f`) lines 668-681 [crates/gsqz/src/primitives/group.rs:668-681]
  - Signature: `fn test_git_diff_large_file_truncated() {`
  - Purpose: Tests that `group_git_diff` truncates large diffs by inserting an omission message and constraining output to fewer than 50 lines. [crates/gsqz/src/primitives/group.rs:668-681]
- `test_git_diff_mixed_files` (function) component `test_git_diff_mixed_files [function]` (`ff964456-3531-5a93-ae45-36e05512b4e3`) lines 684-709 [crates/gsqz/src/primitives/group.rs:684-709]
  - Signature: `fn test_git_diff_mixed_files() {`
  - Purpose: Verifies that `group_git_diff` preserves source file diffs while collapsing lock and binary file diffs into abbreviated summary format. [crates/gsqz/src/primitives/group.rs:684-709]
- `test_git_diff_no_diff_headers_passthrough` (function) component `test_git_diff_no_diff_headers_passthrough [function]` (`96c3be23-93fc-589f-b716-22b935973eb1`) lines 712-716 [crates/gsqz/src/primitives/group.rs:712-716]
  - Signature: `fn test_git_diff_no_diff_headers_passthrough() {`
  - Purpose: Verifies that `group_git_diff` returns non-diff input unmodified when no git diff headers are present. [crates/gsqz/src/primitives/group.rs:712-716]
- `test_pytest_failures_extracts_sections` (function) component `test_pytest_failures_extracts_sections [function]` (`64330604-ba12-5581-b56e-966e832fd592`) lines 719-734 [crates/gsqz/src/primitives/group.rs:719-734]
  - Signature: `fn test_pytest_failures_extracts_sections() {`
  - Purpose: Tests that `group_pytest_failures()` correctly extracts the FAILURES section, assertion details, and summary information from pytest output. [crates/gsqz/src/primitives/group.rs:719-734]
- `test_pytest_failures_preserves_warnings` (function) component `test_pytest_failures_preserves_warnings [function]` (`8f585076-379a-5d19-aa6e-8a306ba24da4`) lines 737-750 [crates/gsqz/src/primitives/group.rs:737-750]
  - Signature: `fn test_pytest_failures_preserves_warnings() {`
  - Purpose: This test verifies that `group_pytest_failures` preserves pytest warning summaries and metadata when processing test output containing passing tests. [crates/gsqz/src/primitives/group.rs:737-750]
- `test_pytest_failures_warnings_and_errors` (function) component `test_pytest_failures_warnings_and_errors [function]` (`f9ab04ea-1b43-551c-aa67-5374bf2b94cb`) lines 753-770 [crates/gsqz/src/primitives/group.rs:753-770]
  - Signature: `fn test_pytest_failures_warnings_and_errors() {`
  - Purpose: Tests that `group_pytest_failures` preserves failures, deprecation warnings, and summary sections when grouping pytest output lines. [crates/gsqz/src/primitives/group.rs:753-770]
- `test_pytest_failures_no_failures_delegates` (function) component `test_pytest_failures_no_failures_delegates [function]` (`4defbe90-0372-54ee-930d-e20f4b9bc88c`) lines 773-781 [crates/gsqz/src/primitives/group.rs:773-781]
  - Signature: `fn test_pytest_failures_no_failures_delegates() {`
  - Purpose: Tests that `group_pytest_failures` correctly delegates to `group_test_failures` when processing pytest output with no failures, preserving the summary line in the result. [crates/gsqz/src/primitives/group.rs:773-781]
- `test_test_failures_captures_fail_lines` (function) component `test_test_failures_captures_fail_lines [function]` (`08488e18-4735-5d3a-82ee-5bf7d5f46d2e`) lines 784-793 [crates/gsqz/src/primitives/group.rs:784-793]
  - Signature: `fn test_test_failures_captures_fail_lines() {`
  - Purpose: Tests that `group_test_failures` preserves FAIL-marked lines when grouping test execution output. [crates/gsqz/src/primitives/group.rs:784-793]
- `test_lint_by_rule_groups` (function) component `test_lint_by_rule_groups [function]` (`4414b78e-2214-5ab9-a3d7-f34c460e7d82`) lines 796-805 [crates/gsqz/src/primitives/group.rs:796-805]
  - Signature: `fn test_lint_by_rule_groups() {`
  - Purpose: This test verifies that `group_lint_by_rule` correctly aggregates lint error messages by rule code (E401, E302) and produces summarized output displaying the occurrence count for each rule violation. [crates/gsqz/src/primitives/group.rs:796-805]
- `test_lint_by_rule_no_rules` (function) component `test_lint_by_rule_no_rules [function]` (`3e5399e7-8362-507e-b212-3deb4fd101b3`) lines 808-812 [crates/gsqz/src/primitives/group.rs:808-812]
  - Signature: `fn test_lint_by_rule_no_rules() {`
  - Purpose: Tests that `group_lint_by_rule` returns the input vector unmodified when processing lines containing no lint errors. [crates/gsqz/src/primitives/group.rs:808-812]
- `test_lint_by_rule_many_occurrences_truncated` (function) component `test_lint_by_rule_many_occurrences_truncated [function]` (`a9c6cb9d-1155-5777-9160-27329badc744`) lines 815-822 [crates/gsqz/src/primitives/group.rs:815-822]
  - Signature: `fn test_lint_by_rule_many_occurrences_truncated() {`
  - Purpose: # Summary

Validates that `group_lint_by_rule()` correctly aggregates lint errors by rule code (E401), counts total occurrences, and truncates the display output with an "and N more" suffix when handling large result sets. [crates/gsqz/src/primitives/group.rs:815-822]
- `test_by_extension_groups` (function) component `test_by_extension_groups [function]` (`7360e1b1-073a-51de-aaf2-a2fa7975c08f`) lines 825-834 [crates/gsqz/src/primitives/group.rs:825-834]
  - Signature: `fn test_by_extension_groups() {`
  - Purpose: Verifies that `group_by_extension` correctly aggregates input file paths by extension and produces formatted output strings showing each extension with its file count. [crates/gsqz/src/primitives/group.rs:825-834]
- `test_by_extension_empty` (function) component `test_by_extension_empty [function]` (`5a215062-b14d-51e0-ba2a-234f936ca139`) lines 837-840 [crates/gsqz/src/primitives/group.rs:837-840]
  - Signature: `fn test_by_extension_empty() {`
  - Purpose: Tests that `group_by_extension` returns an empty collection when passed an empty vector as input. [crates/gsqz/src/primitives/group.rs:837-840]
- `test_by_extension_no_extension` (function) component `test_by_extension_no_extension [function]` (`5ecd8770-276f-5dc1-a5b0-605d48854279`) lines 843-849 [crates/gsqz/src/primitives/group.rs:843-849]
  - Signature: `fn test_by_extension_no_extension() {`
  - Purpose: Validates that `group_by_extension()` correctly assigns files lacking a dot delimiter to the "(no ext)" classification category. [crates/gsqz/src/primitives/group.rs:843-849]
- `test_by_directory_groups` (function) component `test_by_directory_groups [function]` (`93b1ca6a-64be-51dc-b99b-eafca72d4573`) lines 852-861 [crates/gsqz/src/primitives/group.rs:852-861]
  - Signature: `fn test_by_directory_groups() {`
  - Purpose: Tests that `group_by_directory` correctly groups file paths by parent directory and produces formatted output showing each directory name with its item count. [crates/gsqz/src/primitives/group.rs:852-861]
- `test_by_directory_no_slash` (function) component `test_by_directory_no_slash [function]` (`6e067005-787d-58f9-9839-beae65a43531`) lines 864-868 [crates/gsqz/src/primitives/group.rs:864-868]
  - Signature: `fn test_by_directory_no_slash() {`
  - Purpose: This test verifies that `group_by_directory()` prepends a `./` prefix to filenames that lack an explicit directory component. [crates/gsqz/src/primitives/group.rs:864-868]
- `test_by_file_grep_style` (function) component `test_by_file_grep_style [function]` (`56c442da-f3c8-5e2c-8598-f4d0a151fb2f`) lines 871-880 [crates/gsqz/src/primitives/group.rs:871-880]
  - Signature: `fn test_by_file_grep_style() {`
  - Purpose: This test verifies that `group_by_file` correctly aggregates grep-style colon-delimited output lines by filename and generates summary strings displaying each file path with its match count. [crates/gsqz/src/primitives/group.rs:871-880]
- `test_by_file_no_grep_format` (function) component `test_by_file_no_grep_format [function]` (`f8f38ab6-42d4-5618-aa98-5379dc6748a9`) lines 883-887 [crates/gsqz/src/primitives/group.rs:883-887]
  - Signature: `fn test_by_file_no_grep_format() {`
  - Purpose: Tests that `group_by_file` returns non-grep-formatted input unchanged. [crates/gsqz/src/primitives/group.rs:883-887]
- `test_by_file_many_matches_truncated` (function) component `test_by_file_many_matches_truncated [function]` (`9f0171d5-b442-5836-a689-79b0ce93e94a`) lines 890-901 [crates/gsqz/src/primitives/group.rs:890-901]
  - Signature: `fn test_by_file_many_matches_truncated() {`
  - Purpose: Verifies that `group_by_file` truncates match output for files with many matches, displaying a match count summary and an 'and N more' continuation indicator when matches exceed the display threshold. [crates/gsqz/src/primitives/group.rs:890-901]
- `test_errors_warnings_empty` (function) component `test_errors_warnings_empty [function]` (`e4a0a08c-e02e-5330-a736-38ed24a3d2f4`) lines 904-908 [crates/gsqz/src/primitives/group.rs:904-908]
  - Signature: `fn test_errors_warnings_empty() {`
  - Purpose: Unit test that verifies `group_errors_warnings()` returns the input vector unchanged when processing lines containing no error or warning messages. [crates/gsqz/src/primitives/group.rs:904-908]
- `test_errors_warnings_only_errors` (function) component `test_errors_warnings_only_errors [function]` (`1d237b01-a52b-586f-8553-230e2304698f`) lines 911-921 [crates/gsqz/src/primitives/group.rs:911-921]
  - Signature: `fn test_errors_warnings_only_errors() {`
  - Purpose: Tests that `group_errors_warnings` correctly labels a result group with "Errors (2)" and excludes a warnings section when processing only error messages. [crates/gsqz/src/primitives/group.rs:911-921]
- `test_errors_warnings_only_warnings` (function) component `test_errors_warnings_only_warnings [function]` (`d792296a-0110-5f9f-ad78-80c64330846f`) lines 924-929 [crates/gsqz/src/primitives/group.rs:924-929]
  - Signature: `fn test_errors_warnings_only_warnings() {`
  - Purpose: Tests that `group_errors_warnings()` produces a warnings count header and excludes an errors header when processing input containing only warnings and info lines. [crates/gsqz/src/primitives/group.rs:924-929]
- `test_errors_warnings_many_truncated` (function) component `test_errors_warnings_many_truncated [function]` (`b0293d67-8e6b-5527-b6ba-050851300fca`) lines 932-940 [crates/gsqz/src/primitives/group.rs:932-940]
  - Signature: `fn test_errors_warnings_many_truncated() {`
  - Purpose: Tests that `group_errors_warnings()` correctly truncates and categorizes 25 errors and 15 warnings, displaying aggregate counts and truncation indicators for suppressed items in each category. [crates/gsqz/src/primitives/group.rs:932-940]

