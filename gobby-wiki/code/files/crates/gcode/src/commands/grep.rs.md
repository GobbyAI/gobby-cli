---
title: crates/gcode/src/commands/grep.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/grep.rs
  ranges:
  - 21-33
  - 36-40
  - 43-46
  - 49-52
  - 55-58
  - 61-68
  - 71-84
  - 87-92
  - 94-125
  - 127-234
  - 236-254
  - 256-276
  - 279-285
  - 287-352
  - 354-375
  - 377-407
  - 409-414
  - 417-430
  - 432-438
  - 441-456
  - 458-467
  - 469-472
  - 475-481
  - 483-496
  - 499-515
  - 517-533
  - 535-582
  - 584-597
  - 603-609
  - 611-625
  - 628-633
  - 636-647
  - 650-664
  - 667-674
  - 677-685
  - 688-703
  - 706-738
  - 741-759
  - 762-776
  - 779-799
  - 802-817
  - 820-837
  - 840-868
  - 871-879
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/grep.rs:21-33](crates/gcode/src/commands/grep.rs#L21-L33), [crates/gcode/src/commands/grep.rs:36-40](crates/gcode/src/commands/grep.rs#L36-L40), [crates/gcode/src/commands/grep.rs:43-46](crates/gcode/src/commands/grep.rs#L43-L46), [crates/gcode/src/commands/grep.rs:49-52](crates/gcode/src/commands/grep.rs#L49-L52), [crates/gcode/src/commands/grep.rs:55-58](crates/gcode/src/commands/grep.rs#L55-L58), [crates/gcode/src/commands/grep.rs:61-68](crates/gcode/src/commands/grep.rs#L61-L68), [crates/gcode/src/commands/grep.rs:71-84](crates/gcode/src/commands/grep.rs#L71-L84), [crates/gcode/src/commands/grep.rs:87-92](crates/gcode/src/commands/grep.rs#L87-L92), [crates/gcode/src/commands/grep.rs:94-125](crates/gcode/src/commands/grep.rs#L94-L125), [crates/gcode/src/commands/grep.rs:127-234](crates/gcode/src/commands/grep.rs#L127-L234), [crates/gcode/src/commands/grep.rs:236-254](crates/gcode/src/commands/grep.rs#L236-L254), [crates/gcode/src/commands/grep.rs:256-276](crates/gcode/src/commands/grep.rs#L256-L276), [crates/gcode/src/commands/grep.rs:279-285](crates/gcode/src/commands/grep.rs#L279-L285), [crates/gcode/src/commands/grep.rs:287-352](crates/gcode/src/commands/grep.rs#L287-L352), [crates/gcode/src/commands/grep.rs:354-375](crates/gcode/src/commands/grep.rs#L354-L375), [crates/gcode/src/commands/grep.rs:377-407](crates/gcode/src/commands/grep.rs#L377-L407), [crates/gcode/src/commands/grep.rs:409-414](crates/gcode/src/commands/grep.rs#L409-L414), [crates/gcode/src/commands/grep.rs:417-430](crates/gcode/src/commands/grep.rs#L417-L430), [crates/gcode/src/commands/grep.rs:432-438](crates/gcode/src/commands/grep.rs#L432-L438), [crates/gcode/src/commands/grep.rs:441-456](crates/gcode/src/commands/grep.rs#L441-L456), [crates/gcode/src/commands/grep.rs:458-467](crates/gcode/src/commands/grep.rs#L458-L467), [crates/gcode/src/commands/grep.rs:469-472](crates/gcode/src/commands/grep.rs#L469-L472), [crates/gcode/src/commands/grep.rs:475-481](crates/gcode/src/commands/grep.rs#L475-L481), [crates/gcode/src/commands/grep.rs:483-496](crates/gcode/src/commands/grep.rs#L483-L496), [crates/gcode/src/commands/grep.rs:499-515](crates/gcode/src/commands/grep.rs#L499-L515), [crates/gcode/src/commands/grep.rs:517-533](crates/gcode/src/commands/grep.rs#L517-L533), [crates/gcode/src/commands/grep.rs:535-582](crates/gcode/src/commands/grep.rs#L535-L582), [crates/gcode/src/commands/grep.rs:584-597](crates/gcode/src/commands/grep.rs#L584-L597), [crates/gcode/src/commands/grep.rs:603-609](crates/gcode/src/commands/grep.rs#L603-L609), [crates/gcode/src/commands/grep.rs:611-625](crates/gcode/src/commands/grep.rs#L611-L625), [crates/gcode/src/commands/grep.rs:628-633](crates/gcode/src/commands/grep.rs#L628-L633), [crates/gcode/src/commands/grep.rs:636-647](crates/gcode/src/commands/grep.rs#L636-L647), [crates/gcode/src/commands/grep.rs:650-664](crates/gcode/src/commands/grep.rs#L650-L664), [crates/gcode/src/commands/grep.rs:667-674](crates/gcode/src/commands/grep.rs#L667-L674), [crates/gcode/src/commands/grep.rs:677-685](crates/gcode/src/commands/grep.rs#L677-L685), [crates/gcode/src/commands/grep.rs:688-703](crates/gcode/src/commands/grep.rs#L688-L703), [crates/gcode/src/commands/grep.rs:706-738](crates/gcode/src/commands/grep.rs#L706-L738), [crates/gcode/src/commands/grep.rs:741-759](crates/gcode/src/commands/grep.rs#L741-L759), [crates/gcode/src/commands/grep.rs:762-776](crates/gcode/src/commands/grep.rs#L762-L776), [crates/gcode/src/commands/grep.rs:779-799](crates/gcode/src/commands/grep.rs#L779-L799), [crates/gcode/src/commands/grep.rs:802-817](crates/gcode/src/commands/grep.rs#L802-L817), [crates/gcode/src/commands/grep.rs:820-837](crates/gcode/src/commands/grep.rs#L820-L837), [crates/gcode/src/commands/grep.rs:840-868](crates/gcode/src/commands/grep.rs#L840-L868), [crates/gcode/src/commands/grep.rs:871-879](crates/gcode/src/commands/grep.rs#L871-L879)

</details>

# crates/gcode/src/commands/grep.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Implements the `grep` command for indexed project content, turning a search pattern plus path/glob and matching options into either text or JSON output. `run` opens a read-only DB connection, builds `GrepFilters`, loads indexed chunks, searches them with `grep_chunks_with_filters`, and carries truncation and count metadata into a `GrepResponse`.

The supporting types model the pipeline: `IndexedContentChunk` and `LoadedIndexedChunks` represent fetched index data, `GrepMatch`/`GrepSpan`/`GrepContextLine` capture matched lines and surrounding context, and `GrepResult`/`GrepResponse` collect final stats and payload. Helper functions split responsibility between SQL prefiltering, glob/prefix filtering, case and fixed-string matching, context-line selection, grouping/formatting, and tests that verify behavior like ordering, deduplication, context limits, and JSON/text rendering.
[crates/gcode/src/commands/grep.rs:21-33]
[crates/gcode/src/commands/grep.rs:36-40]
[crates/gcode/src/commands/grep.rs:43-46]
[crates/gcode/src/commands/grep.rs:49-52]
[crates/gcode/src/commands/grep.rs:55-58]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GrepOptions` | class | `pub struct GrepOptions<'a> {` | `GrepOptions [class]` | `9f43ffb2-a0e2-584d-8dfe-82f0ce874a24` | 21-33 [crates/gcode/src/commands/grep.rs:21-33] | Indexed class `GrepOptions` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:21-33] |
| `IndexedContentChunk` | class | `struct IndexedContentChunk {` | `IndexedContentChunk [class]` | `a65c0559-e81e-5a17-9e34-ebeed224caec` | 36-40 [crates/gcode/src/commands/grep.rs:36-40] | Indexed class `IndexedContentChunk` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:36-40] |
| `LoadedIndexedChunks` | class | `struct LoadedIndexedChunks {` | `LoadedIndexedChunks [class]` | `6fc15fb0-bb89-5936-9db4-bcaa6d6f7df6` | 43-46 [crates/gcode/src/commands/grep.rs:43-46] | Indexed class `LoadedIndexedChunks` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:43-46] |
| `GrepSpan` | class | `pub(crate) struct GrepSpan {` | `GrepSpan [class]` | `a878e6c4-236b-53fc-a236-408cf43fdbd2` | 49-52 [crates/gcode/src/commands/grep.rs:49-52] | Indexed class `GrepSpan` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:49-52] |
| `GrepContextLine` | class | `pub(crate) struct GrepContextLine {` | `GrepContextLine [class]` | `b8e8d047-8f26-5940-971b-710d77152bf7` | 55-58 [crates/gcode/src/commands/grep.rs:55-58] | Indexed class `GrepContextLine` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:55-58] |
| `GrepMatch` | class | `pub(crate) struct GrepMatch {` | `GrepMatch [class]` | `86f41bac-4649-5bd6-97d6-9fd4f872ff30` | 61-68 [crates/gcode/src/commands/grep.rs:61-68] | Indexed class `GrepMatch` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:61-68] |
| `GrepResponse` | class | `struct GrepResponse {` | `GrepResponse [class]` | `58726474-5973-560c-9146-2faff91c89a3` | 71-84 [crates/gcode/src/commands/grep.rs:71-84] | Indexed class `GrepResponse` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:71-84] |
| `GrepResult` | class | `struct GrepResult {` | `GrepResult [class]` | `27c1f00b-2e90-5b76-809a-1b4bea5df859` | 87-92 [crates/gcode/src/commands/grep.rs:87-92] | Indexed class `GrepResult` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:87-92] |
| `run` | function | `pub fn run(ctx: &Context, options: GrepOptions<'_>) -> anyhow::Result<()> {` | `run [function]` | `e4ad18ed-bf49-5e30-9643-c4663ca79386` | 94-125 [crates/gcode/src/commands/grep.rs:94-125] | Indexed function `run` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:94-125] |
| `load_indexed_chunks` | function | `fn load_indexed_chunks(` | `load_indexed_chunks [function]` | `83404754-52be-5b49-a427-5ebe679917e5` | 127-234 [crates/gcode/src/commands/grep.rs:127-234] | Indexed function `load_indexed_chunks` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:127-234] |
| `push_grep_sql_prefilters` | function | `fn push_grep_sql_prefilters<'a>(` | `push_grep_sql_prefilters [function]` | `2ff26069-514a-56c1-a80e-1a6be42ecbce` | 236-254 [crates/gcode/src/commands/grep.rs:236-254] | Indexed function `push_grep_sql_prefilters` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:236-254] |
| `push_grep_sql_prefix_filter` | function | `fn push_grep_sql_prefix_filter<'a>(` | `push_grep_sql_prefix_filter [function]` | `7c0008e1-a6c7-54e5-a63b-b063ec39052f` | 256-276 [crates/gcode/src/commands/grep.rs:256-276] | Indexed function `push_grep_sql_prefix_filter` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:256-276] |
| `grep_chunks` | function | `fn grep_chunks(` | `grep_chunks [function]` | `954329a6-d4a3-5a62-817d-5bf3efe8d331` | 279-285 [crates/gcode/src/commands/grep.rs:279-285] | Indexed function `grep_chunks` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:279-285] |
| `grep_chunks_with_filters` | function | `fn grep_chunks_with_filters(` | `grep_chunks_with_filters [function]` | `8d76e759-dbab-5321-9fab-32689530c947` | 287-352 [crates/gcode/src/commands/grep.rs:287-352] | Indexed function `grep_chunks_with_filters` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:287-352] |
| `context_line_numbers` | function | `fn context_line_numbers(` | `context_line_numbers [function]` | `dcc025cd-e9eb-576c-b9df-4e1316cbda62` | 354-375 [crates/gcode/src/commands/grep.rs:354-375] | Indexed function `context_line_numbers` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:354-375] |
| `collect_context_lines` | function | `fn collect_context_lines(` | `collect_context_lines [function]` | `45706af7-f610-56ef-a836-ce2fc419b8c2` | 377-407 [crates/gcode/src/commands/grep.rs:377-407] | Indexed function `collect_context_lines` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:377-407] |
| `GrepFilters` | class | `struct GrepFilters {` | `GrepFilters [class]` | `bd62ccd2-646e-5409-a0db-1ad365e2cdf0` | 409-414 [crates/gcode/src/commands/grep.rs:409-414] | Indexed class `GrepFilters` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:409-414] |
| `GrepFilters::new` | method | `fn new(paths: &[String], globs: &[String]) -> anyhow::Result<Self> {` | `GrepFilters::new [method]` | `cf1f9046-be13-5808-831b-256769c7b1b8` | 417-430 [crates/gcode/src/commands/grep.rs:417-430] | Indexed method `GrepFilters::new` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:417-430] |
| `GrepFilters::matches` | method | `fn matches(&self, file_path: &str) -> bool {` | `GrepFilters::matches [method]` | `c641df2d-cacd-550c-ad50-e07cf000e199` | 432-438 [crates/gcode/src/commands/grep.rs:432-438] | Indexed method `GrepFilters::matches` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:432-438] |
| `sql_like_prefixes` | function | `fn sql_like_prefixes(patterns: &[String]) -> Option<Vec<String>> {` | `sql_like_prefixes [function]` | `644f2010-69d2-55f5-b0af-22fed8545f29` | 441-456 [crates/gcode/src/commands/grep.rs:441-456] | Indexed function `sql_like_prefixes` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:441-456] |
| `escape_like_prefix` | function | `fn escape_like_prefix(value: &str) -> String {` | `escape_like_prefix [function]` | `13033af0-a185-5280-a5f8-3afe00b8251b` | 458-467 [crates/gcode/src/commands/grep.rs:458-467] | Indexed function `escape_like_prefix` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:458-467] |
| `CompiledGlob` | class | `struct CompiledGlob {` | `CompiledGlob [class]` | `2799976f-1742-50e4-baed-e05e472703a0` | 469-472 [crates/gcode/src/commands/grep.rs:469-472] | Indexed class `CompiledGlob` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:469-472] |
| `CompiledGlob::new` | method | `fn new(raw: &str) -> anyhow::Result<Self> {` | `CompiledGlob::new [method]` | `074e9aa6-d4fa-5edd-87f1-8d351cf9b842` | 475-481 [crates/gcode/src/commands/grep.rs:475-481] | Indexed method `CompiledGlob::new` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:475-481] |
| `CompiledGlob::matches` | method | `fn matches(&self, file_path: &str) -> bool {` | `CompiledGlob::matches [method]` | `eb3daa05-3f26-5757-bee5-fce82627e4b0` | 483-496 [crates/gcode/src/commands/grep.rs:483-496] | Indexed method `CompiledGlob::matches` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:483-496] |
| `context_before` | function | `fn context_before(` | `context_before [function]` | `b52b9585-424c-50f4-8867-c41a7db63ba5` | 499-515 [crates/gcode/src/commands/grep.rs:499-515] | Indexed function `context_before` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:499-515] |
| `context_after` | function | `fn context_after(` | `context_after [function]` | `15cf79b4-25cf-5ac9-bbe7-b0b89c82c4e0` | 517-533 [crates/gcode/src/commands/grep.rs:517-533] | Indexed function `context_after` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:517-533] |
| `format_text_matches` | function | `fn format_text_matches(matches: &[GrepMatch]) -> String {` | `format_text_matches [function]` | `c02cd8cb-a29e-55f8-9b93-ccd228274be1` | 535-582 [crates/gcode/src/commands/grep.rs:535-582] | Indexed function `format_text_matches` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:535-582] |
| `push_grouped_grep_line` | function | `fn push_grouped_grep_line<'a>(` | `push_grouped_grep_line [function]` | `ec2e1060-afcb-5065-af30-f0cde31e01b5` | 584-597 [crates/gcode/src/commands/grep.rs:584-597] | Indexed function `push_grouped_grep_line` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:584-597] |
| `chunk` | function | `fn chunk(path: &str, line_start: usize, content: &str) -> IndexedContentChunk {` | `chunk [function]` | `ac573f3c-d5e8-5888-baa5-1b865c37f9bc` | 603-609 [crates/gcode/src/commands/grep.rs:603-609] | Indexed function `chunk` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:603-609] |
| `options` | function | `fn options(pattern: &str) -> GrepOptions<'_> {` | `options [function]` | `6f61f38a-5454-559a-974c-5071faabe799` | 611-625 [crates/gcode/src/commands/grep.rs:611-625] | Indexed function `options` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:611-625] |
| `text_renders_grouped_grep_shape` | function | `fn text_renders_grouped_grep_shape() {` | `text_renders_grouped_grep_shape [function]` | `e0017516-64f8-5a21-bf17-16be7dd0b3e9` | 628-633 [crates/gcode/src/commands/grep.rs:628-633] | Indexed function `text_renders_grouped_grep_shape` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:628-633] |
| `text_groups_multiple_files` | function | `fn text_groups_multiple_files() {` | `text_groups_multiple_files [function]` | `a3d33973-a772-5cf8-b823-8598a2371b51` | 636-647 [crates/gcode/src/commands/grep.rs:636-647] | Indexed function `text_groups_multiple_files` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:636-647] |
| `ordering_is_path_then_line` | function | `fn ordering_is_path_then_line() {` | `ordering_is_path_then_line [function]` | `2bdd7782-cac8-5f88-9a7e-c2cf791486a3` | 650-664 [crates/gcode/src/commands/grep.rs:650-664] | Indexed function `ordering_is_path_then_line` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:650-664] |
| `ignore_case_matches_case_insensitively` | function | `fn ignore_case_matches_case_insensitively() {` | `ignore_case_matches_case_insensitively [function]` | `7e756417-f504-5fc1-8c4f-ab0542086d9e` | 667-674 [crates/gcode/src/commands/grep.rs:667-674] | Indexed function `ignore_case_matches_case_insensitively` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:667-674] |
| `fixed_strings_treat_regex_metacharacters_literally` | function | `fn fixed_strings_treat_regex_metacharacters_literally() {` | `fixed_strings_treat_regex_metacharacters_literally [function]` | `3a304aaf-8f7d-5b7d-b921-37295bd0af53` | 677-685 [crates/gcode/src/commands/grep.rs:677-685] | Indexed function `fixed_strings_treat_regex_metacharacters_literally` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:677-685] |
| `sql_prefix_prefilter_requires_convertible_globs` | function | `fn sql_prefix_prefilter_requires_convertible_globs() {` | `sql_prefix_prefilter_requires_convertible_globs [function]` | `ecad04ae-9a94-54de-808f-2bee566c70bf` | 688-703 [crates/gcode/src/commands/grep.rs:688-703] | Indexed function `sql_prefix_prefilter_requires_convertible_globs` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:688-703] |
| `context_flags_include_bounded_neighbors` | function | `fn context_flags_include_bounded_neighbors() {` | `context_flags_include_bounded_neighbors [function]` | `e068ba8c-f043-5a69-8dea-f72530f8a667` | 706-738 [crates/gcode/src/commands/grep.rs:706-738] | Indexed function `context_flags_include_bounded_neighbors` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:706-738] |
| `text_output_trims_leading_whitespace_without_changing_matches` | function | `fn text_output_trims_leading_whitespace_without_changing_matches() {` | `text_output_trims_leading_whitespace_without_changing_matches [function]` | `2551b512-edc2-5703-960d-1965d2dacff3` | 741-759 [crates/gcode/src/commands/grep.rs:741-759] | Indexed function `text_output_trims_leading_whitespace_without_changing_matches` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:741-759] |
| `text_suppresses_duplicate_context_lines` | function | `fn text_suppresses_duplicate_context_lines() {` | `text_suppresses_duplicate_context_lines [function]` | `23478b36-66d4-5eb3-80ab-3ba256c877bb` | 762-776 [crates/gcode/src/commands/grep.rs:762-776] | Indexed function `text_suppresses_duplicate_context_lines` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:762-776] |
| `max_count_caps_retained_matches_not_total_matching_lines` | function | `fn max_count_caps_retained_matches_not_total_matching_lines() {` | `max_count_caps_retained_matches_not_total_matching_lines [function]` | `b735aac2-8f6b-5d7c-bf1b-bfca81a1ddfd` | 779-799 [crates/gcode/src/commands/grep.rs:779-799] | Indexed function `max_count_caps_retained_matches_not_total_matching_lines` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:779-799] |
| `json_match_contains_spans_and_context` | function | `fn json_match_contains_spans_and_context() {` | `json_match_contains_spans_and_context [function]` | `e0d0bcee-eada-5623-9706-6f81ef7be175` | 802-817 [crates/gcode/src/commands/grep.rs:802-817] | Indexed function `json_match_contains_spans_and_context` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:802-817] |
| `path_and_glob_filters_compose` | function | `fn path_and_glob_filters_compose() {` | `path_and_glob_filters_compose [function]` | `f92c30a6-8c83-59b4-a63b-d5d3a2a61c04` | 820-837 [crates/gcode/src/commands/grep.rs:820-837] | Indexed function `path_and_glob_filters_compose` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:820-837] |
| `bare_globs_match_basenames_but_slash_globs_match_paths` | function | `fn bare_globs_match_basenames_but_slash_globs_match_paths() {` | `bare_globs_match_basenames_but_slash_globs_match_paths [function]` | `c5305f9f-a236-51cf-89bb-3fa90015f6da` | 840-868 [crates/gcode/src/commands/grep.rs:840-868] | Indexed function `bare_globs_match_basenames_but_slash_globs_match_paths` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:840-868] |
| `overlapping_chunks_dedupe_by_file_and_line` | function | `fn overlapping_chunks_dedupe_by_file_and_line() {` | `overlapping_chunks_dedupe_by_file_and_line [function]` | `73f14613-cf9a-5d14-b7bc-eccbe524a8ad` | 871-879 [crates/gcode/src/commands/grep.rs:871-879] | Indexed function `overlapping_chunks_dedupe_by_file_and_line` in `crates/gcode/src/commands/grep.rs`. [crates/gcode/src/commands/grep.rs:871-879] |
