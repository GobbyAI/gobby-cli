---
title: crates/gwiki/src/falkor_graph/boost.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/boost.rs
  ranges:
  - 11-35
  - 37-67
  - 69-104
  - 106-109
  - 111-138
  - 140-151
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/falkor_graph/boost.rs:11-35](crates/gwiki/src/falkor_graph/boost.rs#L11-L35), [crates/gwiki/src/falkor_graph/boost.rs:37-67](crates/gwiki/src/falkor_graph/boost.rs#L37-L67), [crates/gwiki/src/falkor_graph/boost.rs:69-104](crates/gwiki/src/falkor_graph/boost.rs#L69-L104), [crates/gwiki/src/falkor_graph/boost.rs:106-109](crates/gwiki/src/falkor_graph/boost.rs#L106-L109), [crates/gwiki/src/falkor_graph/boost.rs:111-138](crates/gwiki/src/falkor_graph/boost.rs#L111-L138), [crates/gwiki/src/falkor_graph/boost.rs:140-151](crates/gwiki/src/falkor_graph/boost.rs#L140-L151)

</details>

# crates/gwiki/src/falkor_graph/boost.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file builds FalkorDB-backed graph boost data for search. `load_graph_boost_data` orchestrates the flow by querying documents and links with caller-provided limits, collecting any truncation into a degradation report, and returning a `GraphBoostData` bundle. `query_documents` and `query_links` choose scope-aware Cypher queries, run them through the shared `query_limited` helper, and map rows into graph-boost document/link records. `LimitedQuery` carries the result items plus a capped flag, while `partial_graph_degradation` turns any limit overruns into a degradation value and warning.
[crates/gwiki/src/falkor_graph/boost.rs:11-35]
[crates/gwiki/src/falkor_graph/boost.rs:37-67]
[crates/gwiki/src/falkor_graph/boost.rs:69-104]
[crates/gwiki/src/falkor_graph/boost.rs:106-109]
[crates/gwiki/src/falkor_graph/boost.rs:111-138]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `load_graph_boost_data` | function | `pub(crate) fn load_graph_boost_data(` | `load_graph_boost_data [function]` | `2432f054-ea66-5f38-8d6f-5043dbb8d5a0` | 11-35 [crates/gwiki/src/falkor_graph/boost.rs:11-35] | Indexed function `load_graph_boost_data` in `crates/gwiki/src/falkor_graph/boost.rs`. [crates/gwiki/src/falkor_graph/boost.rs:11-35] |
| `query_documents` | function | `fn query_documents(` | `query_documents [function]` | `c464cc10-9b4b-5176-9f42-1704c006adcd` | 37-67 [crates/gwiki/src/falkor_graph/boost.rs:37-67] | Indexed function `query_documents` in `crates/gwiki/src/falkor_graph/boost.rs`. [crates/gwiki/src/falkor_graph/boost.rs:37-67] |
| `query_links` | function | `fn query_links(` | `query_links [function]` | `de740b87-92a9-5100-a3b7-083e6647e1ea` | 69-104 [crates/gwiki/src/falkor_graph/boost.rs:69-104] | Indexed function `query_links` in `crates/gwiki/src/falkor_graph/boost.rs`. [crates/gwiki/src/falkor_graph/boost.rs:69-104] |
| `LimitedQuery` | class | `struct LimitedQuery<T> {` | `LimitedQuery [class]` | `257581d4-45e1-5496-83d6-f17d4fb2407f` | 106-109 [crates/gwiki/src/falkor_graph/boost.rs:106-109] | Indexed class `LimitedQuery` in `crates/gwiki/src/falkor_graph/boost.rs`. [crates/gwiki/src/falkor_graph/boost.rs:106-109] |
| `query_limited` | function | `fn query_limited(` | `query_limited [function]` | `20090afd-3d58-54f5-819e-7b5211a470e9` | 111-138 [crates/gwiki/src/falkor_graph/boost.rs:111-138] | Indexed function `query_limited` in `crates/gwiki/src/falkor_graph/boost.rs`. [crates/gwiki/src/falkor_graph/boost.rs:111-138] |
| `partial_graph_degradation` | function | `pub(super) fn partial_graph_degradation(capped: &[String]) -> Option<DegradationKind> {` | `partial_graph_degradation [function]` | `4ef2cfae-3fc1-53fe-a1b1-526ee7a8bf0d` | 140-151 [crates/gwiki/src/falkor_graph/boost.rs:140-151] | Indexed function `partial_graph_degradation` in `crates/gwiki/src/falkor_graph/boost.rs`. [crates/gwiki/src/falkor_graph/boost.rs:140-151] |
