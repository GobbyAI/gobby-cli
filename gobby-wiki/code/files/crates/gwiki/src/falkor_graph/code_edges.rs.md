---
title: crates/gwiki/src/falkor_graph/code_edges.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/code_edges.rs
  ranges:
  - 18-21
  - 23-114
  - 116-157
  - 159-167
  - 169-205
  - 207-213
  - 215-231
  - 233-237
  - 239-245
  - 247-252
  - 254-266
  - 268-270
  - 272-277
  - 279-285
  - 287-289
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/falkor_graph/code_edges.rs:18-21](crates/gwiki/src/falkor_graph/code_edges.rs#L18-L21), [crates/gwiki/src/falkor_graph/code_edges.rs:23-114](crates/gwiki/src/falkor_graph/code_edges.rs#L23-L114), [crates/gwiki/src/falkor_graph/code_edges.rs:116-157](crates/gwiki/src/falkor_graph/code_edges.rs#L116-L157), [crates/gwiki/src/falkor_graph/code_edges.rs:159-167](crates/gwiki/src/falkor_graph/code_edges.rs#L159-L167), [crates/gwiki/src/falkor_graph/code_edges.rs:169-205](crates/gwiki/src/falkor_graph/code_edges.rs#L169-L205), [crates/gwiki/src/falkor_graph/code_edges.rs:207-213](crates/gwiki/src/falkor_graph/code_edges.rs#L207-L213), [crates/gwiki/src/falkor_graph/code_edges.rs:215-231](crates/gwiki/src/falkor_graph/code_edges.rs#L215-L231), [crates/gwiki/src/falkor_graph/code_edges.rs:233-237](crates/gwiki/src/falkor_graph/code_edges.rs#L233-L237), [crates/gwiki/src/falkor_graph/code_edges.rs:239-245](crates/gwiki/src/falkor_graph/code_edges.rs#L239-L245), [crates/gwiki/src/falkor_graph/code_edges.rs:247-252](crates/gwiki/src/falkor_graph/code_edges.rs#L247-L252), [crates/gwiki/src/falkor_graph/code_edges.rs:254-266](crates/gwiki/src/falkor_graph/code_edges.rs#L254-L266), [crates/gwiki/src/falkor_graph/code_edges.rs:268-270](crates/gwiki/src/falkor_graph/code_edges.rs#L268-L270), [crates/gwiki/src/falkor_graph/code_edges.rs:272-277](crates/gwiki/src/falkor_graph/code_edges.rs#L272-L277), [crates/gwiki/src/falkor_graph/code_edges.rs:279-285](crates/gwiki/src/falkor_graph/code_edges.rs#L279-L285), [crates/gwiki/src/falkor_graph/code_edges.rs:287-289](crates/gwiki/src/falkor_graph/code_edges.rs#L287-L289)

</details>

# crates/gwiki/src/falkor_graph/code_edges.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds and limits the code-edge data loaded from Falkor for a set of documents. `load_code_graph_edges` filters documents to code sources, fetches call and import edges through `GraphClient`, accumulates them up to `MAX_TOTAL_CODE_EDGES`, and records which truncation components were hit; the helper functions split out query construction, per-edge limit handling, truncation bookkeeping, source-path normalization, and endpoint/path formatting, while `LimitedCodeGraphEdges` carries the fetched edge list plus a truncation flag.
[crates/gwiki/src/falkor_graph/code_edges.rs:18-21]
[crates/gwiki/src/falkor_graph/code_edges.rs:23-114]
[crates/gwiki/src/falkor_graph/code_edges.rs:116-157]
[crates/gwiki/src/falkor_graph/code_edges.rs:159-167]
[crates/gwiki/src/falkor_graph/code_edges.rs:169-205]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `LimitedCodeGraphEdges` | class | `struct LimitedCodeGraphEdges {` | `LimitedCodeGraphEdges [class]` | `32f4b0e4-d704-5a95-a9b3-254e2bffa0f9` | 18-21 [crates/gwiki/src/falkor_graph/code_edges.rs:18-21] | Indexed class `LimitedCodeGraphEdges` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:18-21] |
| `load_code_graph_edges` | function | `pub(crate) fn load_code_graph_edges(` | `load_code_graph_edges [function]` | `0775c1dd-d659-5a29-90e5-e97c7e504a3a` | 23-114 [crates/gwiki/src/falkor_graph/code_edges.rs:23-114] | Indexed function `load_code_graph_edges` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:23-114] |
| `code_call_edges` | function | `fn code_call_edges(` | `code_call_edges [function]` | `fb62f197-8f94-5f03-9473-580d85ce25d3` | 116-157 [crates/gwiki/src/falkor_graph/code_edges.rs:116-157] | Indexed function `code_call_edges` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:116-157] |
| `code_call_edges_query` | function | `pub(super) fn code_call_edges_query() -> &'static str {` | `code_call_edges_query [function]` | `af1379bb-6fbc-5be2-b869-42db0a5f1569` | 159-167 [crates/gwiki/src/falkor_graph/code_edges.rs:159-167] | Indexed function `code_call_edges_query` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:159-167] |
| `code_import_edges` | function | `fn code_import_edges(` | `code_import_edges [function]` | `417d8bea-062d-5470-a99f-c23cdb2dd730` | 169-205 [crates/gwiki/src/falkor_graph/code_edges.rs:169-205] | Indexed function `code_import_edges` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:169-205] |
| `code_import_edges_query` | function | `pub(super) fn code_import_edges_query() -> &'static str {` | `code_import_edges_query [function]` | `7767ef79-f4a2-5855-b756-46de4172a8d9` | 207-213 [crates/gwiki/src/falkor_graph/code_edges.rs:207-213] | Indexed function `code_import_edges_query` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:207-213] |
| `code_edge_query_params` | function | `pub(super) fn code_edge_query_params(` | `code_edge_query_params [function]` | `9da3f5ac-e05b-5052-8e0e-be8d1ad1362b` | 215-231 [crates/gwiki/src/falkor_graph/code_edges.rs:215-231] | Indexed function `code_edge_query_params` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:215-231] |
| `sentinel_limit` | function | `fn sentinel_limit(limit: usize) -> anyhow::Result<usize> {` | `sentinel_limit [function]` | `d5d73cb3-82f3-5d7b-bc10-66bfce067773` | 233-237 [crates/gwiki/src/falkor_graph/code_edges.rs:233-237] | Indexed function `sentinel_limit` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:233-237] |
| `truncate_to_limit` | function | `pub(super) fn truncate_to_limit<T>(rows: &mut Vec<T>, limit: usize) -> bool {` | `truncate_to_limit [function]` | `2a422e76-1369-55f6-981d-3c337d9e0ea9` | 239-245 [crates/gwiki/src/falkor_graph/code_edges.rs:239-245] | Indexed function `truncate_to_limit` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:239-245] |
| `remaining_code_edge_limit` | function | `pub(super) fn remaining_code_edge_limit(` | `remaining_code_edge_limit [function]` | `c6bc2497-2af6-5490-9620-23ac5d92b0c7` | 247-252 [crates/gwiki/src/falkor_graph/code_edges.rs:247-252] | Indexed function `remaining_code_edge_limit` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:247-252] |
| `record_code_edge_truncation` | function | `pub(super) fn record_code_edge_truncation(` | `record_code_edge_truncation [function]` | `e8c3e0ef-4465-58d5-841a-5cd8343d05c0` | 254-266 [crates/gwiki/src/falkor_graph/code_edges.rs:254-266] | Indexed function `record_code_edge_truncation` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:254-266] |
| `truncation_component` | function | `pub(super) fn truncation_component(component: &str, limit: usize) -> String {` | `truncation_component [function]` | `c9480e0d-41f7-59cb-9cb1-7b0e6d3928d6` | 268-270 [crates/gwiki/src/falkor_graph/code_edges.rs:268-270] | Indexed function `truncation_component` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:268-270] |
| `code_doc_source_path` | function | `pub(super) fn code_doc_source_path(path: &Path) -> Option<String> {` | `code_doc_source_path [function]` | `bf490a72-e183-5fd3-9932-411dfaaecca9` | 272-277 [crates/gwiki/src/falkor_graph/code_edges.rs:272-277] | Indexed function `code_doc_source_path` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:272-277] |
| `code_endpoint` | function | `fn code_endpoint(file_path: &str, symbol: &str) -> String {` | `code_endpoint [function]` | `ca4d8e56-ae15-57b4-821d-33a58460bb4b` | 279-285 [crates/gwiki/src/falkor_graph/code_edges.rs:279-285] | Indexed function `code_endpoint` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:279-285] |
| `normalize_graph_path` | function | `fn normalize_graph_path(path: &Path) -> String {` | `normalize_graph_path [function]` | `3066fff2-6ead-566f-a56b-e95deef1c12e` | 287-289 [crates/gwiki/src/falkor_graph/code_edges.rs:287-289] | Indexed function `normalize_graph_path` in `crates/gwiki/src/falkor_graph/code_edges.rs`. [crates/gwiki/src/falkor_graph/code_edges.rs:287-289] |
