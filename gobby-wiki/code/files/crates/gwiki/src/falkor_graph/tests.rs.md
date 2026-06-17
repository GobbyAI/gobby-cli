---
title: crates/gwiki/src/falkor_graph/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/tests.rs
  ranges:
  - 27-30
  - 33-76
  - 79-90
  - 93-95
  - 98-104
  - 107-112
  - 115-126
  - 129-147
  - 150-159
  - 162-181
  - 184-196
  - 199-251
  - 253-255
  - 257-274
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/falkor_graph/tests.rs:27-30](crates/gwiki/src/falkor_graph/tests.rs#L27-L30), [crates/gwiki/src/falkor_graph/tests.rs:33-76](crates/gwiki/src/falkor_graph/tests.rs#L33-L76), [crates/gwiki/src/falkor_graph/tests.rs:79-90](crates/gwiki/src/falkor_graph/tests.rs#L79-L90), [crates/gwiki/src/falkor_graph/tests.rs:93-95](crates/gwiki/src/falkor_graph/tests.rs#L93-L95), [crates/gwiki/src/falkor_graph/tests.rs:98-104](crates/gwiki/src/falkor_graph/tests.rs#L98-L104), [crates/gwiki/src/falkor_graph/tests.rs:107-112](crates/gwiki/src/falkor_graph/tests.rs#L107-L112), [crates/gwiki/src/falkor_graph/tests.rs:115-126](crates/gwiki/src/falkor_graph/tests.rs#L115-L126), [crates/gwiki/src/falkor_graph/tests.rs:129-147](crates/gwiki/src/falkor_graph/tests.rs#L129-L147), [crates/gwiki/src/falkor_graph/tests.rs:150-159](crates/gwiki/src/falkor_graph/tests.rs#L150-L159), [crates/gwiki/src/falkor_graph/tests.rs:162-181](crates/gwiki/src/falkor_graph/tests.rs#L162-L181), [crates/gwiki/src/falkor_graph/tests.rs:184-196](crates/gwiki/src/falkor_graph/tests.rs#L184-L196), [crates/gwiki/src/falkor_graph/tests.rs:199-251](crates/gwiki/src/falkor_graph/tests.rs#L199-L251), [crates/gwiki/src/falkor_graph/tests.rs:253-255](crates/gwiki/src/falkor_graph/tests.rs#L253-L255), [crates/gwiki/src/falkor_graph/tests.rs:257-274](crates/gwiki/src/falkor_graph/tests.rs#L257-L274)

</details>

# crates/gwiki/src/falkor_graph/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file is a test module for the Falkor graph layer in `gwiki`. It verifies the graph name is wiki-owned, target resolution keeps missing links unresolved while skipping external URLs, scope parameters are emitted as Cypher string literals and omit global filters, code-doc source paths map back to code files, string escaping matches Cypher requirements, and graph truncation/edge-limit logic handles sentinel rows, zero limits, and remaining-cap calculations. It also checks that graph write statements use the wiki labels and relationships expected by the graph schema, with small helper tests covering Cypher literal formatting and string-content escaping.
[crates/gwiki/src/falkor_graph/tests.rs:27-30]
[crates/gwiki/src/falkor_graph/tests.rs:33-76]
[crates/gwiki/src/falkor_graph/tests.rs:79-90]
[crates/gwiki/src/falkor_graph/tests.rs:93-95]
[crates/gwiki/src/falkor_graph/tests.rs:98-104]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `falkordb_graph_name_is_wiki_owned` | function | `fn falkordb_graph_name_is_wiki_owned() {` | `falkordb_graph_name_is_wiki_owned [function]` | `dda75dcf-bed7-502e-8fa9-95594f0457ac` | 27-30 [crates/gwiki/src/falkor_graph/tests.rs:27-30] | Indexed function `falkordb_graph_name_is_wiki_owned` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:27-30] |
| `graph_resolution_keeps_unresolved_targets_and_skips_external` | function | `fn graph_resolution_keeps_unresolved_targets_and_skips_external() {` | `graph_resolution_keeps_unresolved_targets_and_skips_external [function]` | `8af826ff-4be3-5ac3-b322-1136a96c7fd5` | 33-76 [crates/gwiki/src/falkor_graph/tests.rs:33-76] | Indexed function `graph_resolution_keeps_unresolved_targets_and_skips_external` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:33-76] |
| `graph_scope_params_are_cypher_string_literals` | function | `fn graph_scope_params_are_cypher_string_literals() {` | `graph_scope_params_are_cypher_string_literals [function]` | `a482585a-9872-5fc7-a17f-798c33cac30b` | 79-90 [crates/gwiki/src/falkor_graph/tests.rs:79-90] | Indexed function `graph_scope_params_are_cypher_string_literals` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:79-90] |
| `graph_scope_params_omit_global_scope_filters` | function | `fn graph_scope_params_omit_global_scope_filters() {` | `graph_scope_params_omit_global_scope_filters [function]` | `69cefdd7-1f80-51a8-b82a-4ae177569bc6` | 93-95 [crates/gwiki/src/falkor_graph/tests.rs:93-95] | Indexed function `graph_scope_params_omit_global_scope_filters` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:93-95] |
| `ask_unified_graph_code_doc_source_path_maps_to_code_file` | function | `fn ask_unified_graph_code_doc_source_path_maps_to_code_file() {` | `ask_unified_graph_code_doc_source_path_maps_to_code_file [function]` | `698360e3-f57f-5e20-9552-fe589bbbdbcd` | 98-104 [crates/gwiki/src/falkor_graph/tests.rs:98-104] | Indexed function `ask_unified_graph_code_doc_source_path_maps_to_code_file` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:98-104] |
| `cypher_string_literal_escapes_like_gcode` | function | `fn cypher_string_literal_escapes_like_gcode() {` | `cypher_string_literal_escapes_like_gcode [function]` | `932a5137-6dbb-5ce7-98bf-9801e22b85c2` | 107-112 [crates/gwiki/src/falkor_graph/tests.rs:107-112] | Indexed function `cypher_string_literal_escapes_like_gcode` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:107-112] |
| `partial_graph_degradation_reports_capped_components` | function | `fn partial_graph_degradation_reports_capped_components() {` | `partial_graph_degradation_reports_capped_components [function]` | `f34434ae-e2dd-586b-b128-b7a2c6845f5f` | 115-126 [crates/gwiki/src/falkor_graph/tests.rs:115-126] | Indexed function `partial_graph_degradation_reports_capped_components` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:115-126] |
| `code_edge_query_params_use_sentinel_limit_and_parameterized_queries` | function | `fn code_edge_query_params_use_sentinel_limit_and_parameterized_queries() {` | `code_edge_query_params_use_sentinel_limit_and_parameterized_queries [function]` | `d7a19ea1-0976-5338-9677-46448e5dbc23` | 129-147 [crates/gwiki/src/falkor_graph/tests.rs:129-147] | Indexed function `code_edge_query_params_use_sentinel_limit_and_parameterized_queries` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:129-147] |
| `truncation_components_name_capped_call_and_import_queries` | function | `fn truncation_components_name_capped_call_and_import_queries() {` | `truncation_components_name_capped_call_and_import_queries [function]` | `18c8c2e2-3e75-580b-8fc2-72ed731fa47b` | 150-159 [crates/gwiki/src/falkor_graph/tests.rs:150-159] | Indexed function `truncation_components_name_capped_call_and_import_queries` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:150-159] |
| `code_edge_query_limit_respects_total_remaining_cap` | function | `fn code_edge_query_limit_respects_total_remaining_cap() {` | `code_edge_query_limit_respects_total_remaining_cap [function]` | `c3d9b04b-5171-5876-b9a9-64a14adcf741` | 162-181 [crates/gwiki/src/falkor_graph/tests.rs:162-181] | Indexed function `code_edge_query_limit_respects_total_remaining_cap` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:162-181] |
| `truncate_to_limit_handles_sentinel_rows_and_zero_limit` | function | `fn truncate_to_limit_handles_sentinel_rows_and_zero_limit() {` | `truncate_to_limit_handles_sentinel_rows_and_zero_limit [function]` | `a6ee0af9-71f4-5331-87f2-0166dc3bb591` | 184-196 [crates/gwiki/src/falkor_graph/tests.rs:184-196] | Indexed function `truncate_to_limit_handles_sentinel_rows_and_zero_limit` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:184-196] |
| `graph_write_uses_wiki_labels_and_relationships` | function | `fn graph_write_uses_wiki_labels_and_relationships() {` | `graph_write_uses_wiki_labels_and_relationships [function]` | `4c9c1f92-82e3-5e96-b008-d96e90d2b5f8` | 199-251 [crates/gwiki/src/falkor_graph/tests.rs:199-251] | Indexed function `graph_write_uses_wiki_labels_and_relationships` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:199-251] |
| `cypher_string_literal` | function | `fn cypher_string_literal(value: &str) -> String {` | `cypher_string_literal [function]` | `9dc9ad72-462d-51ff-b7e0-e90e29907994` | 253-255 [crates/gwiki/src/falkor_graph/tests.rs:253-255] | Indexed function `cypher_string_literal` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:253-255] |
| `escape_string_contents` | function | `fn escape_string_contents(value: &str) -> String {` | `escape_string_contents [function]` | `d13bd21c-ea6b-5d61-a349-13aae32a30a2` | 257-274 [crates/gwiki/src/falkor_graph/tests.rs:257-274] | Indexed function `escape_string_contents` in `crates/gwiki/src/falkor_graph/tests.rs`. [crates/gwiki/src/falkor_graph/tests.rs:257-274] |
