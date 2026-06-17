---
title: crates/gcode/src/commands/search.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/search.rs
  ranges:
  - 13-22
  - 28-211
  - 213-303
  - 305-310
  - 312-416
  - 418-496
  - 499-522
  - 524-604
  - 606-616
  - 618-624
  - 626-628
  - 630-642
  - 644-654
  - 656-658
  - 660-665
  - 667-670
  - 672-674
  - 676-678
  - 680-690
  - 692-696
  - 698-709
  - 711-713
  - 715-723
  - 725-727
  - 729-735
  - 737-752
  - 754-769
  - 771-773
  - 775-786
  - 788-797
  - 803-824
  - 827-838
  - 841-855
  - 858-867
  - 870-879
  - 882-904
  - 907-918
  - 921-923
  - 926-931
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/search.rs:13-22](crates/gcode/src/commands/search.rs#L13-L22), [crates/gcode/src/commands/search.rs:28-211](crates/gcode/src/commands/search.rs#L28-L211), [crates/gcode/src/commands/search.rs:213-303](crates/gcode/src/commands/search.rs#L213-L303), [crates/gcode/src/commands/search.rs:305-310](crates/gcode/src/commands/search.rs#L305-L310), [crates/gcode/src/commands/search.rs:312-416](crates/gcode/src/commands/search.rs#L312-L416), [crates/gcode/src/commands/search.rs:418-496](crates/gcode/src/commands/search.rs#L418-L496), [crates/gcode/src/commands/search.rs:499-522](crates/gcode/src/commands/search.rs#L499-L522), [crates/gcode/src/commands/search.rs:524-604](crates/gcode/src/commands/search.rs#L524-L604), [crates/gcode/src/commands/search.rs:606-616](crates/gcode/src/commands/search.rs#L606-L616), [crates/gcode/src/commands/search.rs:618-624](crates/gcode/src/commands/search.rs#L618-L624), [crates/gcode/src/commands/search.rs:626-628](crates/gcode/src/commands/search.rs#L626-L628), [crates/gcode/src/commands/search.rs:630-642](crates/gcode/src/commands/search.rs#L630-L642), [crates/gcode/src/commands/search.rs:644-654](crates/gcode/src/commands/search.rs#L644-L654), [crates/gcode/src/commands/search.rs:656-658](crates/gcode/src/commands/search.rs#L656-L658), [crates/gcode/src/commands/search.rs:660-665](crates/gcode/src/commands/search.rs#L660-L665), [crates/gcode/src/commands/search.rs:667-670](crates/gcode/src/commands/search.rs#L667-L670), [crates/gcode/src/commands/search.rs:672-674](crates/gcode/src/commands/search.rs#L672-L674), [crates/gcode/src/commands/search.rs:676-678](crates/gcode/src/commands/search.rs#L676-L678), [crates/gcode/src/commands/search.rs:680-690](crates/gcode/src/commands/search.rs#L680-L690), [crates/gcode/src/commands/search.rs:692-696](crates/gcode/src/commands/search.rs#L692-L696), [crates/gcode/src/commands/search.rs:698-709](crates/gcode/src/commands/search.rs#L698-L709), [crates/gcode/src/commands/search.rs:711-713](crates/gcode/src/commands/search.rs#L711-L713), [crates/gcode/src/commands/search.rs:715-723](crates/gcode/src/commands/search.rs#L715-L723), [crates/gcode/src/commands/search.rs:725-727](crates/gcode/src/commands/search.rs#L725-L727), [crates/gcode/src/commands/search.rs:729-735](crates/gcode/src/commands/search.rs#L729-L735), [crates/gcode/src/commands/search.rs:737-752](crates/gcode/src/commands/search.rs#L737-L752), [crates/gcode/src/commands/search.rs:754-769](crates/gcode/src/commands/search.rs#L754-L769), [crates/gcode/src/commands/search.rs:771-773](crates/gcode/src/commands/search.rs#L771-L773), [crates/gcode/src/commands/search.rs:775-786](crates/gcode/src/commands/search.rs#L775-L786), [crates/gcode/src/commands/search.rs:788-797](crates/gcode/src/commands/search.rs#L788-L797), [crates/gcode/src/commands/search.rs:803-824](crates/gcode/src/commands/search.rs#L803-L824), [crates/gcode/src/commands/search.rs:827-838](crates/gcode/src/commands/search.rs#L827-L838), [crates/gcode/src/commands/search.rs:841-855](crates/gcode/src/commands/search.rs#L841-L855), [crates/gcode/src/commands/search.rs:858-867](crates/gcode/src/commands/search.rs#L858-L867), [crates/gcode/src/commands/search.rs:870-879](crates/gcode/src/commands/search.rs#L870-L879), [crates/gcode/src/commands/search.rs:882-904](crates/gcode/src/commands/search.rs#L882-L904), [crates/gcode/src/commands/search.rs:907-918](crates/gcode/src/commands/search.rs#L907-L918), [crates/gcode/src/commands/search.rs:921-923](crates/gcode/src/commands/search.rs#L921-L923), [crates/gcode/src/commands/search.rs:926-931](crates/gcode/src/commands/search.rs#L926-L931)

</details>

# crates/gcode/src/commands/search.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Implements the `gcode search` command and related search subcommands, wiring together exact symbol lookup, full-text search, graph/vector boosting, and text/content search into a single ranked, paginated result flow. `SearchOptions` carries the user’s filters and output settings, while `search`, `search_symbol`, `search_symbol_with_graph`, `search_text`, and `search_content` route queries through the appropriate backend and visibility checks.

The rest of the file is support code: scoring and tiering helpers decide how matches are ranked, filter predicates narrow results by language/kind/path, and formatting/diagnostic helpers render result lines, warnings, pagination hints, and empty-state messages. Additional utility functions detect literal-like queries, extract seed IDs, and compact snippets so search output stays relevant and concise.
[crates/gcode/src/commands/search.rs:13-22]
[crates/gcode/src/commands/search.rs:28-211]
[crates/gcode/src/commands/search.rs:213-303]
[crates/gcode/src/commands/search.rs:305-310]
[crates/gcode/src/commands/search.rs:312-416]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SearchOptions` | class | `pub struct SearchOptions<'a> {` | `SearchOptions [class]` | `7723d2c9-8026-58aa-8ea7-4e652e628061` | 13-22 [crates/gcode/src/commands/search.rs:13-22] | Indexed class `SearchOptions` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:13-22] |
| `search` | function | `pub fn search(ctx: &Context, query: &str, options: SearchOptions<'_>) -> anyhow::Result<()> {` | `search [function]` | `c630fc4a-21a9-55cb-9d53-a4bde30a958b` | 28-211 [crates/gcode/src/commands/search.rs:28-211] | Indexed function `search` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:28-211] |
| `search_symbol` | function | `pub fn search_symbol(ctx: &Context, query: &str, options: SearchOptions<'_>) -> anyhow::Result<()> {` | `search_symbol [function]` | `8996c5f5-2f56-584f-a31d-703e6e1a4980` | 213-303 [crates/gcode/src/commands/search.rs:213-303] | Indexed function `search_symbol` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:213-303] |
| `SymbolGraphSearchContext` | class | `struct SymbolGraphSearchContext<'a> {` | `SymbolGraphSearchContext [class]` | `b2d3b511-9ed6-537b-868f-6afb24ec1d92` | 305-310 [crates/gcode/src/commands/search.rs:305-310] | Indexed class `SymbolGraphSearchContext` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:305-310] |
| `search_symbol_with_graph` | function | `fn search_symbol_with_graph(` | `search_symbol_with_graph [function]` | `893e57da-6689-530e-a523-6f3073c53b15` | 312-416 [crates/gcode/src/commands/search.rs:312-416] | Indexed function `search_symbol_with_graph` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:312-416] |
| `search_text` | function | `pub fn search_text(` | `search_text [function]` | `c840d393-82dd-53e5-9aac-420458b4f7c2` | 418-496 [crates/gcode/src/commands/search.rs:418-496] | Indexed function `search_text` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:418-496] |
| `extract_seed_ids` | function | `fn extract_seed_ids(` | `extract_seed_ids [function]` | `c6042b2d-d2d1-5602-a647-a8b062c017a1` | 499-522 [crates/gcode/src/commands/search.rs:499-522] | Indexed function `extract_seed_ids` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:499-522] |
| `search_content` | function | `pub fn search_content(` | `search_content [function]` | `105d1123-4c91-5e1d-bc95-3f8509d91a7f` | 524-604 [crates/gcode/src/commands/search.rs:524-604] | Indexed function `search_content` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:524-604] |
| `exact_tier` | function | `fn exact_tier(query: &str, symbol: &Symbol) -> u8 {` | `exact_tier [function]` | `b7a56852-cf1f-56da-87ab-b10383b17219` | 606-616 [crates/gcode/src/commands/search.rs:606-616] | Indexed function `exact_tier` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:606-616] |
| `exact_tier_score` | function | `fn exact_tier_score(query: &str, symbol: &Symbol) -> f64 {` | `exact_tier_score [function]` | `78148884-f794-5983-b1ff-db17c86449fe` | 618-624 [crates/gcode/src/commands/search.rs:618-624] | Indexed function `exact_tier_score` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:618-624] |
| `final_rank_score` | function | `fn final_rank_score(query: &str, symbol: &Symbol, rrf_score: f64) -> f64 {` | `final_rank_score [function]` | `419a5559-65cf-596a-b9ef-3582a9bb72c3` | 626-628 [crates/gcode/src/commands/search.rs:626-628] | Indexed function `final_rank_score` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:626-628] |
| `symbol_matches_filters` | function | `fn symbol_matches_filters(` | `symbol_matches_filters [function]` | `8a7e4d02-98b8-5eea-9463-153f5bd259f3` | 630-642 [crates/gcode/src/commands/search.rs:630-642] | Indexed function `symbol_matches_filters` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:630-642] |
| `search_result_matches_filters` | function | `fn search_result_matches_filters(` | `search_result_matches_filters [function]` | `7e2a5e13-b745-5b3f-a204-88c6b5d138ce` | 644-654 [crates/gcode/src/commands/search.rs:644-654] | Indexed function `search_result_matches_filters` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:644-654] |
| `path_matches_filters` | function | `fn path_matches_filters(path_patterns: &[glob::Pattern], file_path: &str) -> bool {` | `path_matches_filters [function]` | `da276627-f46f-5ccc-8c9c-ac6e18c3fcbe` | 656-658 [crates/gcode/src/commands/search.rs:656-658] | Indexed function `path_matches_filters` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:656-658] |
| `filtered_fetch_cap_hint` | function | `fn filtered_fetch_cap_hint() -> String {` | `filtered_fetch_cap_hint [function]` | `7ba5f8c1-af15-5cc5-a5d0-372ab364ea8d` | 660-665 [crates/gcode/src/commands/search.rs:660-665] | Indexed function `filtered_fetch_cap_hint` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:660-665] |
| `path_filter_post_filter_hint` | function | `fn path_filter_post_filter_hint() -> String {` | `path_filter_post_filter_hint [function]` | `91883a09-e43a-5dae-9c2e-b9a156dcf044` | 667-670 [crates/gcode/src/commands/search.rs:667-670] | Indexed function `path_filter_post_filter_hint` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:667-670] |
| `visible_search_degraded_hint` | function | `fn visible_search_degraded_hint() -> String {` | `visible_search_degraded_hint [function]` | `5b36aa42-323f-53d0-9963-788b51e8736c` | 672-674 [crates/gcode/src/commands/search.rs:672-674] | Indexed function `visible_search_degraded_hint` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:672-674] |
| `literal_query_hint` | function | `fn literal_query_hint(query: &str) -> Option<String> {` | `literal_query_hint [function]` | `4198a446-02c6-5e82-a09c-fc472610b91e` | 676-678 [crates/gcode/src/commands/search.rs:676-678] | Indexed function `literal_query_hint` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:676-678] |
| `literal_like_query` | function | `fn literal_like_query(query: &str) -> bool {` | `literal_like_query [function]` | `28d8ed41-ed5f-55d2-8c93-ffdbbd159be1` | 680-690 [crates/gcode/src/commands/search.rs:680-690] | Indexed function `literal_like_query` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:680-690] |
| `contains_quoted_literal` | function | `fn contains_quoted_literal(query: &str) -> bool {` | `contains_quoted_literal [function]` | `c8667061-4f0b-5a08-91c4-0156fc309238` | 692-696 [crates/gcode/src/commands/search.rs:692-696] | Indexed function `contains_quoted_literal` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:692-696] |
| `contains_call_site_syntax` | function | `fn contains_call_site_syntax(query: &str) -> bool {` | `contains_call_site_syntax [function]` | `30841f5b-777e-5499-8a6a-aaf47e0eb106` | 698-709 [crates/gcode/src/commands/search.rs:698-709] | Indexed function `contains_call_site_syntax` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:698-709] |
| `contains_path_separator` | function | `fn contains_path_separator(query: &str) -> bool {` | `contains_path_separator [function]` | `d324dd47-2b01-54bf-a218-9db84ce4a05c` | 711-713 [crates/gcode/src/commands/search.rs:711-713] | Indexed function `contains_path_separator` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:711-713] |
| `is_dotted_literal` | function | `fn is_dotted_literal(query: &str) -> bool {` | `is_dotted_literal [function]` | `f3ef215b-0e3a-5924-953f-089c53c752f2` | 715-723 [crates/gcode/src/commands/search.rs:715-723] | Indexed function `is_dotted_literal` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:715-723] |
| `is_dotted_literal_char` | function | `fn is_dotted_literal_char(ch: char) -> bool {` | `is_dotted_literal_char [function]` | `e910fc5a-37f1-5e24-937f-e15d5c4314af` | 725-727 [crates/gcode/src/commands/search.rs:725-727] | Indexed function `is_dotted_literal_char` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:725-727] |
| `print_search_warning` | function | `fn print_search_warning(ctx: &Context, hint: Option<&str>) {` | `print_search_warning [function]` | `d3b7f524-81b3-52c7-8fc1-50b34c5bc175` | 729-735 [crates/gcode/src/commands/search.rs:729-735] | Indexed function `print_search_warning` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:729-735] |
| `format_search_result_line` | function | `fn format_search_result_line(result: &SearchResult) -> String {` | `format_search_result_line [function]` | `fb2dd7bb-aeeb-53a3-b99b-548f50e4642e` | 737-752 [crates/gcode/src/commands/search.rs:737-752] | Indexed function `format_search_result_line` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:737-752] |
| `format_symbol_lookup_text` | function | `fn format_symbol_lookup_text(symbol: &Symbol) -> String {` | `format_symbol_lookup_text [function]` | `3843f7d0-29e7-57b1-8365-7628505d593f` | 754-769 [crates/gcode/src/commands/search.rs:754-769] | Indexed function `format_symbol_lookup_text` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:754-769] |
| `compact_snippet` | function | `fn compact_snippet(snippet: &str) -> String {` | `compact_snippet [function]` | `4eae7a2e-e537-5c3c-b4ba-ed4425a2b983` | 771-773 [crates/gcode/src/commands/search.rs:771-773] | Indexed function `compact_snippet` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:771-773] |
| `print_empty_diagnostic` | function | `fn print_empty_diagnostic(ctx: &Context, is_empty: bool, offset: usize, total: usize) {` | `print_empty_diagnostic [function]` | `5592c030-a9b7-5d65-ad76-45ccd63e6107` | 775-786 [crates/gcode/src/commands/search.rs:775-786] | Indexed function `print_empty_diagnostic` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:775-786] |
| `print_pagination_hint` | function | `fn print_pagination_hint(total: usize, offset: usize, result_count: usize) {` | `print_pagination_hint [function]` | `af2275b0-4792-518f-9f07-cfaea03bc2bb` | 788-797 [crates/gcode/src/commands/search.rs:788-797] | Indexed function `print_pagination_hint` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:788-797] |
| `symbol` | function | `fn symbol(file_path: &str, kind: &str, language: &str) -> Symbol {` | `symbol [function]` | `126cf970-9105-5baa-8500-ee7b4df71a14` | 803-824 [crates/gcode/src/commands/search.rs:803-824] | Indexed function `symbol` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:803-824] |
| `symbol_filter_rejects_language_kind_path_and_missing_disk_file` | function | `fn symbol_filter_rejects_language_kind_path_and_missing_disk_file() {` | `symbol_filter_rejects_language_kind_path_and_missing_disk_file [function]` | `bc4beb93-d3fb-5196-876f-dbada6030afc` | 827-838 [crates/gcode/src/commands/search.rs:827-838] | Indexed function `symbol_filter_rejects_language_kind_path_and_missing_disk_file` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:827-838] |
| `exact_tier_prefers_case_sensitive_match` | function | `fn exact_tier_prefers_case_sensitive_match() {` | `exact_tier_prefers_case_sensitive_match [function]` | `c96c4ec4-3b44-56d4-b480-540539c4e6fb` | 841-855 [crates/gcode/src/commands/search.rs:841-855] | Indexed function `exact_tier_prefers_case_sensitive_match` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:841-855] |
| `final_score_preserves_display_tier_before_rrf_score` | function | `fn final_score_preserves_display_tier_before_rrf_score() {` | `final_score_preserves_display_tier_before_rrf_score [function]` | `2fa6d143-bdf1-5a49-8fdd-8e3e8b6bf782` | 858-867 [crates/gcode/src/commands/search.rs:858-867] | Indexed function `final_score_preserves_display_tier_before_rrf_score` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:858-867] |
| `combines_fetch_cap_and_path_post_filter_hints` | function | `fn combines_fetch_cap_and_path_post_filter_hints() {` | `combines_fetch_cap_and_path_post_filter_hints [function]` | `c4339597-4968-5616-aa46-d8f786588af8` | 870-879 [crates/gcode/src/commands/search.rs:870-879] | Indexed function `combines_fetch_cap_and_path_post_filter_hints` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:870-879] |
| `search_result_token_budget_uses_text_row_estimate` | function | `fn search_result_token_budget_uses_text_row_estimate() {` | `search_result_token_budget_uses_text_row_estimate [function]` | `0f09d1fa-c365-5127-9032-9c1bbe356fa0` | 882-904 [crates/gcode/src/commands/search.rs:882-904] | Indexed function `search_result_token_budget_uses_text_row_estimate` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:882-904] |
| `literal_query_hint_detects_literal_like_queries` | function | `fn literal_query_hint_detects_literal_like_queries() {` | `literal_query_hint_detects_literal_like_queries [function]` | `b06a319b-b14c-55a8-af8e-35f74bfc653d` | 907-918 [crates/gcode/src/commands/search.rs:907-918] | Indexed function `literal_query_hint_detects_literal_like_queries` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:907-918] |
| `literal_query_hint_skips_natural_language_queries` | function | `fn literal_query_hint_skips_natural_language_queries() {` | `literal_query_hint_skips_natural_language_queries [function]` | `5491fcc6-5d45-51f5-826e-05b482b48729` | 921-923 [crates/gcode/src/commands/search.rs:921-923] | Indexed function `literal_query_hint_skips_natural_language_queries` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:921-923] |
| `content_snippet_compaction_collapses_whitespace` | function | `fn content_snippet_compaction_collapses_whitespace() {` | `content_snippet_compaction_collapses_whitespace [function]` | `b6aef9c4-57a9-5abd-890a-a049bfc85146` | 926-931 [crates/gcode/src/commands/search.rs:926-931] | Indexed function `content_snippet_compaction_collapses_whitespace` in `crates/gcode/src/commands/search.rs`. [crates/gcode/src/commands/search.rs:926-931] |
