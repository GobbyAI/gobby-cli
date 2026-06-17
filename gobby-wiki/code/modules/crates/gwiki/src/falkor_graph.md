---
title: crates/gwiki/src/falkor_graph
type: code_module
provenance:
- file: crates/gwiki/src/falkor_graph/boost.rs
  ranges:
  - 11-35
  - 37-67
  - 69-104
  - 106-109
  - 111-138
  - 140-151
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
- file: crates/gwiki/src/falkor_graph/query.rs
  ranges:
  - 8-23
  - 25-28
  - 30-34
  - 36-40
- file: crates/gwiki/src/falkor_graph/sync.rs
  ranges:
  - 13-29
  - 31-44
  - 46-49
  - 51-55
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
- file: crates/gwiki/src/falkor_graph/wiki_facts.rs
  ranges:
  - 13-98
  - 100-132
  - 134-142
  - 144-157
  - 159-161
  - 163-176
  - 178-186
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/falkor_graph/boost.rs:11-35](crates/gwiki/src/falkor_graph/boost.rs#L11-L35), [crates/gwiki/src/falkor_graph/boost.rs:37-67](crates/gwiki/src/falkor_graph/boost.rs#L37-L67), [crates/gwiki/src/falkor_graph/boost.rs:69-104](crates/gwiki/src/falkor_graph/boost.rs#L69-L104), [crates/gwiki/src/falkor_graph/boost.rs:106-109](crates/gwiki/src/falkor_graph/boost.rs#L106-L109), [crates/gwiki/src/falkor_graph/boost.rs:111-138](crates/gwiki/src/falkor_graph/boost.rs#L111-L138), [crates/gwiki/src/falkor_graph/boost.rs:140-151](crates/gwiki/src/falkor_graph/boost.rs#L140-L151)
- [crates/gwiki/src/falkor_graph/code_edges.rs:18-21](crates/gwiki/src/falkor_graph/code_edges.rs#L18-L21), [crates/gwiki/src/falkor_graph/code_edges.rs:23-114](crates/gwiki/src/falkor_graph/code_edges.rs#L23-L114), [crates/gwiki/src/falkor_graph/code_edges.rs:116-157](crates/gwiki/src/falkor_graph/code_edges.rs#L116-L157), [crates/gwiki/src/falkor_graph/code_edges.rs:159-167](crates/gwiki/src/falkor_graph/code_edges.rs#L159-L167), [crates/gwiki/src/falkor_graph/code_edges.rs:169-205](crates/gwiki/src/falkor_graph/code_edges.rs#L169-L205), [crates/gwiki/src/falkor_graph/code_edges.rs:207-213](crates/gwiki/src/falkor_graph/code_edges.rs#L207-L213), [crates/gwiki/src/falkor_graph/code_edges.rs:215-231](crates/gwiki/src/falkor_graph/code_edges.rs#L215-L231), [crates/gwiki/src/falkor_graph/code_edges.rs:233-237](crates/gwiki/src/falkor_graph/code_edges.rs#L233-L237), [crates/gwiki/src/falkor_graph/code_edges.rs:239-245](crates/gwiki/src/falkor_graph/code_edges.rs#L239-L245), [crates/gwiki/src/falkor_graph/code_edges.rs:247-252](crates/gwiki/src/falkor_graph/code_edges.rs#L247-L252), [crates/gwiki/src/falkor_graph/code_edges.rs:254-266](crates/gwiki/src/falkor_graph/code_edges.rs#L254-L266), [crates/gwiki/src/falkor_graph/code_edges.rs:268-270](crates/gwiki/src/falkor_graph/code_edges.rs#L268-L270), [crates/gwiki/src/falkor_graph/code_edges.rs:272-277](crates/gwiki/src/falkor_graph/code_edges.rs#L272-L277), [crates/gwiki/src/falkor_graph/code_edges.rs:279-285](crates/gwiki/src/falkor_graph/code_edges.rs#L279-L285), [crates/gwiki/src/falkor_graph/code_edges.rs:287-289](crates/gwiki/src/falkor_graph/code_edges.rs#L287-L289)
- [crates/gwiki/src/falkor_graph/query.rs:8-23](crates/gwiki/src/falkor_graph/query.rs#L8-L23), [crates/gwiki/src/falkor_graph/query.rs:25-28](crates/gwiki/src/falkor_graph/query.rs#L25-L28), [crates/gwiki/src/falkor_graph/query.rs:30-34](crates/gwiki/src/falkor_graph/query.rs#L30-L34), [crates/gwiki/src/falkor_graph/query.rs:36-40](crates/gwiki/src/falkor_graph/query.rs#L36-L40)
- [crates/gwiki/src/falkor_graph/sync.rs:13-29](crates/gwiki/src/falkor_graph/sync.rs#L13-L29), [crates/gwiki/src/falkor_graph/sync.rs:31-44](crates/gwiki/src/falkor_graph/sync.rs#L31-L44), [crates/gwiki/src/falkor_graph/sync.rs:46-49](crates/gwiki/src/falkor_graph/sync.rs#L46-L49), [crates/gwiki/src/falkor_graph/sync.rs:51-55](crates/gwiki/src/falkor_graph/sync.rs#L51-L55)
- [crates/gwiki/src/falkor_graph/tests.rs:27-30](crates/gwiki/src/falkor_graph/tests.rs#L27-L30), [crates/gwiki/src/falkor_graph/tests.rs:33-76](crates/gwiki/src/falkor_graph/tests.rs#L33-L76), [crates/gwiki/src/falkor_graph/tests.rs:79-90](crates/gwiki/src/falkor_graph/tests.rs#L79-L90), [crates/gwiki/src/falkor_graph/tests.rs:93-95](crates/gwiki/src/falkor_graph/tests.rs#L93-L95), [crates/gwiki/src/falkor_graph/tests.rs:98-104](crates/gwiki/src/falkor_graph/tests.rs#L98-L104), [crates/gwiki/src/falkor_graph/tests.rs:107-112](crates/gwiki/src/falkor_graph/tests.rs#L107-L112), [crates/gwiki/src/falkor_graph/tests.rs:115-126](crates/gwiki/src/falkor_graph/tests.rs#L115-L126), [crates/gwiki/src/falkor_graph/tests.rs:129-147](crates/gwiki/src/falkor_graph/tests.rs#L129-L147), [crates/gwiki/src/falkor_graph/tests.rs:150-159](crates/gwiki/src/falkor_graph/tests.rs#L150-L159), [crates/gwiki/src/falkor_graph/tests.rs:162-181](crates/gwiki/src/falkor_graph/tests.rs#L162-L181), [crates/gwiki/src/falkor_graph/tests.rs:184-196](crates/gwiki/src/falkor_graph/tests.rs#L184-L196), [crates/gwiki/src/falkor_graph/tests.rs:199-251](crates/gwiki/src/falkor_graph/tests.rs#L199-L251), [crates/gwiki/src/falkor_graph/tests.rs:253-255](crates/gwiki/src/falkor_graph/tests.rs#L253-L255), [crates/gwiki/src/falkor_graph/tests.rs:257-274](crates/gwiki/src/falkor_graph/tests.rs#L257-L274)
- [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98](crates/gwiki/src/falkor_graph/wiki_facts.rs#L13-L98), [crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132](crates/gwiki/src/falkor_graph/wiki_facts.rs#L100-L132), [crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142](crates/gwiki/src/falkor_graph/wiki_facts.rs#L134-L142), [crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157](crates/gwiki/src/falkor_graph/wiki_facts.rs#L144-L157), [crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161](crates/gwiki/src/falkor_graph/wiki_facts.rs#L159-L161), [crates/gwiki/src/falkor_graph/wiki_facts.rs:163-176](crates/gwiki/src/falkor_graph/wiki_facts.rs#L163-L176), [crates/gwiki/src/falkor_graph/wiki_facts.rs:178-186](crates/gwiki/src/falkor_graph/wiki_facts.rs#L178-L186)

</details>

# crates/gwiki/src/falkor_graph

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

The `falkor_graph` module manages FalkorDB-backed graph projection and synchronization for search operations within the wiki system. Its core flow orchestrates the projection of Postgres graph facts into FalkorDB via `sync_scope_from_postgres`, which safely deletes stale scoped wiki nodes before populating newly resolved relationships [crates/gwiki/src/falkor_graph/sync.rs:13-29]. In-memory graph facts are built using `load_wiki_graph_facts`, which retrieves raw Postgres links and resolves them into normalized graph targets (direct paths, relative paths, slug matches, or unresolved/external paths) [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98].

For queries, the module coordinates with FalkorDB to supply search boost weights and source code edges through safe query utilities [crates/gwiki/src/falkor_graph/query.rs:8-23]. Specifically, `load_graph_boost_data` retrieves documents and links while generating degradation reports if data exceeds caller limits [crates/gwiki/src/falkor_graph/boost.rs:11-35], whereas `load_code_graph_edges` fetches call and import references up to predefined caps to prevent processing overruns [crates/gwiki/src/falkor_graph/code_edges.rs:23-114]. Safe row parser helpers translate Cypher output back into domain-specific Rust structures [crates/gwiki/src/falkor_graph/query.rs:36-40].

| Public API Symbol | Signature / Description | Source Reference |
| --- | --- | --- |
| `load_graph_boost_data` | Queries document and link paths from FalkorDB for search boost weighting under specified limits. | [crates/gwiki/src/falkor_graph/boost.rs:11-35] |
| `load_code_graph_edges` | Accumulates and limits code-edge (calls/imports) data for specified documents. | [crates/gwiki/src/falkor_graph/code_edges.rs:23-114] |
| `sync_scope_from_postgres` | Orchestrates clearing a graph projection scope in FalkorDB and syncing new nodes and links from Postgres. | [crates/gwiki/src/falkor_graph/sync.rs:13-29] |
| `load_wiki_graph_facts` | Loads documents and links from Postgres and resolves targets to normalized graph destinations. | [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98] |
| `scope_params` | Converts an optional `SearchScope` into escaped parameters suitable for safe interpolation into Cypher queries. | [crates/gwiki/src/falkor_graph/query.rs:8-23] |
| `row_string` | Extracts a required string field from a FalkorDB `Row` and maps errors to search backend diagnostics. | [crates/gwiki/src/falkor_graph/query.rs:36-40] |

| Constant / Config Fact | Value / Purpose | Source Reference |
| --- | --- | --- |
| `FALKORDB_GRAPH_NAME` | `"gobby_wiki"` – Identifies the primary wiki graph name in FalkorDB. | [crates/gwiki/src/falkor_graph/tests.rs:27-30] |
| `CODE_GRAPH_NAME` | Identifies the graph name used for loading code graph connections. |  |
| `MAX_TOTAL_CODE_EDGES` | Cap limit for accumulated call and import edges when loading code connections. |  |
| `WIKI_DOC_LABEL` | Node label (`WikiDoc`) applied to document entities in FalkorDB. |  |
| `WIKI_SOURCE_LABEL` | Node label (`WikiSource`) representing source nodes in the graph schema. |  |
| `WIKI_TARGET_LABEL` | Node label (`WikiTarget`) representing resolved target nodes in the graph schema. |  |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/falkor_graph/boost.rs\|crates/gwiki/src/falkor_graph/boost.rs]] | This file builds FalkorDB-backed graph boost data for search. `load_graph_boost_data` orchestrates the flow by querying documents and links with caller-provided limits, collecting any truncation into a degradation report, and returning a `GraphBoostData` bundle. `query_documents` and `query_links` choose scope-aware Cypher queries, run them through the shared `query_limited` helper, and map rows into graph-boost document/link records. `LimitedQuery` carries the result items plus a capped flag, while `partial_graph_degradation` turns any limit overruns into a degradation value and warning. [crates/gwiki/src/falkor_graph/boost.rs:11-35] [crates/gwiki/src/falkor_graph/boost.rs:37-67] [crates/gwiki/src/falkor_graph/boost.rs:69-104] [crates/gwiki/src/falkor_graph/boost.rs:106-109] [crates/gwiki/src/falkor_graph/boost.rs:111-138] |
| [[code/files/crates/gwiki/src/falkor_graph/code_edges.rs\|crates/gwiki/src/falkor_graph/code_edges.rs]] | Builds and limits the code-edge data loaded from Falkor for a set of documents. `load_code_graph_edges` filters documents to code sources, fetches call and import edges through `GraphClient`, accumulates them up to `MAX_TOTAL_CODE_EDGES`, and records which truncation components were hit; the helper functions split out query construction, per-edge limit handling, truncation bookkeeping, source-path normalization, and endpoint/path formatting, while `LimitedCodeGraphEdges` carries the fetched edge list plus a truncation flag. [crates/gwiki/src/falkor_graph/code_edges.rs:18-21] [crates/gwiki/src/falkor_graph/code_edges.rs:23-114] [crates/gwiki/src/falkor_graph/code_edges.rs:116-157] [crates/gwiki/src/falkor_graph/code_edges.rs:159-167] [crates/gwiki/src/falkor_graph/code_edges.rs:169-205] |
| [[code/files/crates/gwiki/src/falkor_graph/query.rs\|crates/gwiki/src/falkor_graph/query.rs]] | Builds and reads FalkorDB graph query data for the wiki search backend. `scope_params` turns an optional `SearchScope` filter into escaped `scope_kind` and `scope_id` query parameters for interpolated Cypher text, while `optional_row_string` and `optional_row_usize` extract typed values from a `Row` safely. `row_string` wraps the string extractor with a backend error when a required field is missing, so callers can treat query results as validated row data. [crates/gwiki/src/falkor_graph/query.rs:8-23] [crates/gwiki/src/falkor_graph/query.rs:25-28] [crates/gwiki/src/falkor_graph/query.rs:30-34] [crates/gwiki/src/falkor_graph/query.rs:36-40] |
| [[code/files/crates/gwiki/src/falkor_graph/sync.rs\|crates/gwiki/src/falkor_graph/sync.rs]] | This file syncs a wiki graph projection from Postgres into FalkorDB. `sync_scope_from_postgres` loads graph facts for a `SearchScope`, opens a FalkorDB `GraphClient` from config, clears any existing nodes for that scope, then writes the new graph statements one by one. `clear_scope` deletes existing `WikiDoc`, `WikiSource`, and `WikiTarget` nodes for a scoped projection, but refuses to clear the global scope because it cannot be represented as a scoped delete. `execute_statement` is a small helper that runs each generated Cypher statement. `graph_sync_error` maps FalkorDB failures into `WikiError::Config` with a sync-specific message. [crates/gwiki/src/falkor_graph/sync.rs:13-29] [crates/gwiki/src/falkor_graph/sync.rs:31-44] [crates/gwiki/src/falkor_graph/sync.rs:46-49] [crates/gwiki/src/falkor_graph/sync.rs:51-55] |
| [[code/files/crates/gwiki/src/falkor_graph/tests.rs\|crates/gwiki/src/falkor_graph/tests.rs]] | This file is a test module for the Falkor graph layer in `gwiki`. It verifies the graph name is wiki-owned, target resolution keeps missing links unresolved while skipping external URLs, scope parameters are emitted as Cypher string literals and omit global filters, code-doc source paths map back to code files, string escaping matches Cypher requirements, and graph truncation/edge-limit logic handles sentinel rows, zero limits, and remaining-cap calculations. It also checks that graph write statements use the wiki labels and relationships expected by the graph schema, with small helper tests covering Cypher literal formatting and string-content escaping. [crates/gwiki/src/falkor_graph/tests.rs:27-30] [crates/gwiki/src/falkor_graph/tests.rs:33-76] [crates/gwiki/src/falkor_graph/tests.rs:79-90] [crates/gwiki/src/falkor_graph/tests.rs:93-95] [crates/gwiki/src/falkor_graph/tests.rs:98-104] |
| [[code/files/crates/gwiki/src/falkor_graph/wiki_facts.rs\|crates/gwiki/src/falkor_graph/wiki_facts.rs]] | Builds `WikiGraphFacts` for a search scope by reading wiki documents and links from Postgres, then resolving each link target into a normalized graph target. `load_wiki_graph_facts` gathers documents, derives the set of known document paths, builds a slug-to-target map for title-based references, and loads links and sources into the graph facts result. The helper functions work together to interpret targets: `resolve_graph_target` chooses between direct paths, relative paths, slug matches, and external URLs; `resolve_relative_graph_path` and `normalize_path` clean up path-like targets; `slug_target_map` indexes documents by slug; `is_path_like_target` and `is_external_target` classify raw link targets before resolution. [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98] [crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132] [crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142] [crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157] [crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161] |

## Components

| Component ID |
| --- |
| `2432f054-ea66-5f38-8d6f-5043dbb8d5a0` |
| `c464cc10-9b4b-5176-9f42-1704c006adcd` |
| `de740b87-92a9-5100-a3b7-083e6647e1ea` |
| `257581d4-45e1-5496-83d6-f17d4fb2407f` |
| `20090afd-3d58-54f5-819e-7b5211a470e9` |
| `4ef2cfae-3fc1-53fe-a1b1-526ee7a8bf0d` |
| `32f4b0e4-d704-5a95-a9b3-254e2bffa0f9` |
| `0775c1dd-d659-5a29-90e5-e97c7e504a3a` |
| `fb62f197-8f94-5f03-9473-580d85ce25d3` |
| `af1379bb-6fbc-5be2-b869-42db0a5f1569` |
| `417d8bea-062d-5470-a99f-c23cdb2dd730` |
| `7767ef79-f4a2-5855-b756-46de4172a8d9` |
| `9da3f5ac-e05b-5052-8e0e-be8d1ad1362b` |
| `d5d73cb3-82f3-5d7b-bc10-66bfce067773` |
| `2a422e76-1369-55f6-981d-3c337d9e0ea9` |
| `c6bc2497-2af6-5490-9620-23ac5d92b0c7` |
| `e8c3e0ef-4465-58d5-841a-5cd8343d05c0` |
| `c9480e0d-41f7-59cb-9cb1-7b0e6d3928d6` |
| `bf490a72-e183-5fd3-9932-411dfaaecca9` |
| `ca4d8e56-ae15-57b4-821d-33a58460bb4b` |
| `3066fff2-6ead-566f-a56b-e95deef1c12e` |
| `ab081406-4af2-588d-bb69-ce33342eefcd` |
| `d9d3982e-ff9d-5a7b-8e09-7101173d7770` |
| `cd2b16d3-36c1-51d6-a305-49c704bb7253` |
| `8354d785-37a3-5443-94aa-d343bb5881fa` |
| `770ff3b5-3bd6-545f-805c-ed9f07a88298` |
| `988a1ff8-f62d-573d-ac49-fa72e1241701` |
| `e353979f-80a6-56cd-993f-957f8701d872` |
| `16c528c1-6f71-5f96-8d12-86160d9397e8` |
| `dda75dcf-bed7-502e-8fa9-95594f0457ac` |
| `8af826ff-4be3-5ac3-b322-1136a96c7fd5` |
| `a482585a-9872-5fc7-a17f-798c33cac30b` |
| `69cefdd7-1f80-51a8-b82a-4ae177569bc6` |
| `698360e3-f57f-5e20-9552-fe589bbbdbcd` |
| `932a5137-6dbb-5ce7-98bf-9801e22b85c2` |
| `f34434ae-e2dd-586b-b128-b7a2c6845f5f` |
| `d7a19ea1-0976-5338-9677-46448e5dbc23` |
| `18c8c2e2-3e75-580b-8fc2-72ed731fa47b` |
| `c3d9b04b-5171-5876-b9a9-64a14adcf741` |
| `a6ee0af9-71f4-5331-87f2-0166dc3bb591` |
| `4c9c1f92-82e3-5e96-b008-d96e90d2b5f8` |
| `9dc9ad72-462d-51ff-b7e0-e90e29907994` |
| `d13bd21c-ea6b-5d61-a349-13aae32a30a2` |
| `4d60aa47-5986-548d-9cae-f94257e97305` |
| `0f96a6b2-3f9f-54e1-8a93-55d3dacff49b` |
| `0db8eae8-81ba-5f42-a87b-1811ef91f66e` |
| `d6ff3e27-e967-5741-bce2-edc03a5634ae` |
| `663ec667-9918-525d-a4dc-74935a3d965b` |
| `b07ea7cf-e4ea-5736-a222-440a89520e01` |
| `a0c822d1-8b52-5757-8738-840ac6a1b723` |
