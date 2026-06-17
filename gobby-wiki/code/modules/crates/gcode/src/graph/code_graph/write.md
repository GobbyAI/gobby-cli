---
title: crates/gcode/src/graph/code_graph/write
type: code_module
provenance:
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
  ranges:
  - 8-66
  - 68-113
  - 115-127
  - 129-145
  - 147-161
  - 163-171
  - 173-189
  - 191-200
  - 202-211
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
  ranges:
  - 89-96
  - 99-102
  - 105-112
  - 115-119
  - 121-128
  - 130-145
  - 147-152
  - 154-182
  - 184-197
  - 199-207
  - 209-227
  - 229-259
  - 261-295
  - 297-301
  - 304-321
  - 323-327
  - 329-334
  - 337-343
  - 345-364
  - 366-377
  - 379-390
  - 392-403
  - 411-435
  - 438-450
- file: crates/gcode/src/graph/code_graph/write/support.rs
  ranges:
  - 6-13
  - 15-21
  - 23-27
  - 29-31
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
  ranges:
  - 30-81
  - 89-110
  - 113-156
  - 159-177
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66](crates/gcode/src/graph/code_graph/write/deletion.rs#L8-L66), [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113](crates/gcode/src/graph/code_graph/write/deletion.rs#L68-L113), [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127](crates/gcode/src/graph/code_graph/write/deletion.rs#L115-L127), [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145](crates/gcode/src/graph/code_graph/write/deletion.rs#L129-L145), [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161](crates/gcode/src/graph/code_graph/write/deletion.rs#L147-L161), [crates/gcode/src/graph/code_graph/write/deletion.rs:163-171](crates/gcode/src/graph/code_graph/write/deletion.rs#L163-L171), [crates/gcode/src/graph/code_graph/write/deletion.rs:173-189](crates/gcode/src/graph/code_graph/write/deletion.rs#L173-L189), [crates/gcode/src/graph/code_graph/write/deletion.rs:191-200](crates/gcode/src/graph/code_graph/write/deletion.rs#L191-L200), [crates/gcode/src/graph/code_graph/write/deletion.rs:202-211](crates/gcode/src/graph/code_graph/write/deletion.rs#L202-L211)
- [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96](crates/gcode/src/graph/code_graph/write/mutation.rs#L89-L96), [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102](crates/gcode/src/graph/code_graph/write/mutation.rs#L99-L102), [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112](crates/gcode/src/graph/code_graph/write/mutation.rs#L105-L112), [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119](crates/gcode/src/graph/code_graph/write/mutation.rs#L115-L119), [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128](crates/gcode/src/graph/code_graph/write/mutation.rs#L121-L128), [crates/gcode/src/graph/code_graph/write/mutation.rs:130-145](crates/gcode/src/graph/code_graph/write/mutation.rs#L130-L145), [crates/gcode/src/graph/code_graph/write/mutation.rs:147-152](crates/gcode/src/graph/code_graph/write/mutation.rs#L147-L152), [crates/gcode/src/graph/code_graph/write/mutation.rs:154-182](crates/gcode/src/graph/code_graph/write/mutation.rs#L154-L182), [crates/gcode/src/graph/code_graph/write/mutation.rs:184-197](crates/gcode/src/graph/code_graph/write/mutation.rs#L184-L197), [crates/gcode/src/graph/code_graph/write/mutation.rs:199-207](crates/gcode/src/graph/code_graph/write/mutation.rs#L199-L207), [crates/gcode/src/graph/code_graph/write/mutation.rs:209-227](crates/gcode/src/graph/code_graph/write/mutation.rs#L209-L227), [crates/gcode/src/graph/code_graph/write/mutation.rs:229-259](crates/gcode/src/graph/code_graph/write/mutation.rs#L229-L259), [crates/gcode/src/graph/code_graph/write/mutation.rs:261-295](crates/gcode/src/graph/code_graph/write/mutation.rs#L261-L295), [crates/gcode/src/graph/code_graph/write/mutation.rs:297-301](crates/gcode/src/graph/code_graph/write/mutation.rs#L297-L301), [crates/gcode/src/graph/code_graph/write/mutation.rs:304-321](crates/gcode/src/graph/code_graph/write/mutation.rs#L304-L321), [crates/gcode/src/graph/code_graph/write/mutation.rs:323-327](crates/gcode/src/graph/code_graph/write/mutation.rs#L323-L327), [crates/gcode/src/graph/code_graph/write/mutation.rs:329-334](crates/gcode/src/graph/code_graph/write/mutation.rs#L329-L334), [crates/gcode/src/graph/code_graph/write/mutation.rs:337-343](crates/gcode/src/graph/code_graph/write/mutation.rs#L337-L343), [crates/gcode/src/graph/code_graph/write/mutation.rs:345-364](crates/gcode/src/graph/code_graph/write/mutation.rs#L345-L364), [crates/gcode/src/graph/code_graph/write/mutation.rs:366-377](crates/gcode/src/graph/code_graph/write/mutation.rs#L366-L377), [crates/gcode/src/graph/code_graph/write/mutation.rs:379-390](crates/gcode/src/graph/code_graph/write/mutation.rs#L379-L390), [crates/gcode/src/graph/code_graph/write/mutation.rs:392-403](crates/gcode/src/graph/code_graph/write/mutation.rs#L392-L403), [crates/gcode/src/graph/code_graph/write/mutation.rs:411-435](crates/gcode/src/graph/code_graph/write/mutation.rs#L411-L435), [crates/gcode/src/graph/code_graph/write/mutation.rs:438-450](crates/gcode/src/graph/code_graph/write/mutation.rs#L438-L450)
- [crates/gcode/src/graph/code_graph/write/support.rs:6-13](crates/gcode/src/graph/code_graph/write/support.rs#L6-L13), [crates/gcode/src/graph/code_graph/write/support.rs:15-21](crates/gcode/src/graph/code_graph/write/support.rs#L15-L21), [crates/gcode/src/graph/code_graph/write/support.rs:23-27](crates/gcode/src/graph/code_graph/write/support.rs#L23-L27), [crates/gcode/src/graph/code_graph/write/support.rs:29-31](crates/gcode/src/graph/code_graph/write/support.rs#L29-L31)
- [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L30-L81), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L89-L110), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L113-L156), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L159-L177)

</details>

# crates/gcode/src/graph/code_graph/write

Parent: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Overview

The `crates/gcode/src/graph/code_graph/write` module is responsible for orchestrating write-side mutations and deletions within the codebase's FalkorDB-backed dependency and symbol graph. It structures, batches, and standardizes how code files, imports, symbol definitions, and caller relationships are upserted or removed. To prevent execution timeouts on exceptionally large or pathological source files, the module leverages bounded batching to split graph-sync mutations into small, idempotent Cypher query chunks . Standard write execution helper functions wrap parameter types and interact directly with the graph client, establishing uniform query formatting and transaction flows .

Key operational flows within this module start with write planning, where a `SyncFileMutation` is split into chunks capped at `GRAPH_SYNC_BATCH_SIZE` [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]. This produces a sequence of queries beginning with an initial code file header upsert followed by parallelizable batches for importing modules, symbol definitions, and call targets [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]. Correspondingly, deletion flows maintain graph integrity during file or project modifications by generating targeted batches of delete and cleanup queries [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]. These cleanup operations systematically prune outdated file imports, symbol definition paths, and call edges, and sweep orphaned graph nodes to keep the entire code index consistent and minimal [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66].

### Constants
| Constant | Type | Description | Supporting Span |
| --- | --- | --- | --- |
| GRAPH_SYNC_BATCH_SIZE | usize | Maximum number of rows per batched graph-sync query (set to 500) | [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81] |
| EXTRACTED_PROVENANCE | &str | Identifies extracted metadata provenance (set to "EXTRACTED") |  |
| SOURCE_SYSTEM_GCODE | &str | Global identifier for the source system |  |
| PROJECT_NODE_PREDICATE | &str | Cypher label filter matching all project code node types |  |

### Public & Internal API Symbols
| Symbol | Type | Description | Supporting Span |
| --- | --- | --- | --- |
| SyncFileMutation | Struct | Bundles symbols, imports, and calls for a single file sync operation | [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96] |
| plan_sync_batches | Function | Plans bounded, sequential, and idempotent write batches for syncing a file | [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81] |
| delete_file_graph_queries | Function | Generates queries to remove graph relations and nodes associated with a file | [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66] |
| delete_stale_file_graph_queries | Function | Generates queries to delete file graph components not matching the active sync token | [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113] |
| ensure_file_node_query | Function | Generates a query to safely upsert a CodeFile node and its current sync token | [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96] |
| add_imports_query | Function | Generates a query to batch-insert import relationships for a file | [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96] |
| add_definitions_query | Function | Generates a query to batch-insert symbol definitions defined in a file | [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96] |
| execute_write_query | Function | Executes a typed Cypher query with parameters against a graph client | [crates/gcode/src/graph/code_graph/write/support.rs:6-13] |
| typed_query | Function | Helper that constructs a TypedQuery from a Cypher string and parameters | [crates/gcode/src/graph/code_graph/write/support.rs:15-21] |
| usize_value | Function | Safely converts a usize value into a FalkorDB-compatible integer value | [crates/gcode/src/graph/code_graph/write/support.rs:23-27] |
| sync_token_param | Function | Formats a sync token string into a query parameter key-value pair | [crates/gcode/src/graph/code_graph/write/support.rs:29-31] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/graph/code_graph/write/deletion.rs\|crates/gcode/src/graph/code_graph/write/deletion.rs]] | Builds typed Cypher delete/cleanup queries for maintaining the code graph when a file or project changes. The helpers generate query batches to remove file relationships, delete stale or missing symbol nodes, clean orphaned graph nodes and segments, and clear either one project’s index data or the entire code index. [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66] [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113] [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127] [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145] [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161] |
| [[code/files/crates/gcode/src/graph/code_graph/write/mutation.rs\|crates/gcode/src/graph/code_graph/write/mutation.rs]] | Builds Cypher mutations for syncing a code graph into the database. The file centralizes shared constants and helpers for provenance and sync-token generation, then assembles query fragments for imports, definitions, and call relationships. `SyncFileMutation` and `ensure_file_node_query` support file-level upserts, `add_imports_query` and `add_definitions_query` write import and symbol-definition edges, and the `GraphCallTarget`/`call_rows` helpers split calls into symbol, external, and unresolved targets so the three call mutation queries can write the right `CALLS` relationships. [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96] [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102] [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112] [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119] [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128] |
| [[code/files/crates/gcode/src/graph/code_graph/write/support.rs\|crates/gcode/src/graph/code_graph/write/support.rs]] | Provides small write-side helpers for the code graph layer. `execute_write_query` unwraps a `TypedQuery` and sends its Cypher plus parameters to `GraphClient`, returning a plain result. `typed_query` builds a `TypedQuery` from Cypher and an iterator of typed parameters. `usize_value` converts a `usize` into a FalkorDB-compatible integer value with a range check, and `sync_token_param` packages a sync token string as the standard `"sync_token"` query parameter. Together these functions standardize query construction and execution for graph writes. [crates/gcode/src/graph/code_graph/write/support.rs:6-13] [crates/gcode/src/graph/code_graph/write/support.rs:15-21] [crates/gcode/src/graph/code_graph/write/support.rs:23-27] [crates/gcode/src/graph/code_graph/write/support.rs:29-31] |
| [[code/files/crates/gcode/src/graph/code_graph/write/sync_plan.rs\|crates/gcode/src/graph/code_graph/write/sync_plan.rs]] | Implements bounded write planning for `sync_file`: it always emits a header query that upserts the `CodeFile` with the final symbol count and sync token, then splits imports, symbol definitions, and call data into fixed-size batches so each graph-sync mutation stays small and idempotent. The helper tests verify the batching behavior, including the normal case of one header plus one batch per chunk and the small-file case where everything still fits in a single definition batch. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81] [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110] [crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156] [crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177] |

## Components

| Component ID |
| --- |
| `6b7fce22-df5b-550f-b53a-72c5d45e6fe2` |
| `b4ecc305-d084-55c5-8058-c6f2b143a53d` |
| `c790d893-e066-5cef-810c-ef7a64d0f12a` |
| `bcb69555-7e78-5eeb-bea9-35eff3655ee2` |
| `133ee9df-3449-58f5-ba59-70c7dfc942fb` |
| `b3e61529-6088-569f-8f2a-410a2406e5e5` |
| `c562163b-a042-58a0-81c8-23d07ac78c60` |
| `5b08f08d-5c67-5c69-82e8-c701ee409a6d` |
| `f7b8b82a-1170-5017-a16b-e26c31f4381f` |
| `a8869846-a57f-5abe-b587-24741c8f8413` |
| `e3e21d69-34de-5bf8-ae87-3af3bb621bf4` |
| `8216b71e-91cc-5459-a595-ef65977a27c2` |
| `ad9a643c-cae1-5944-b160-e3c7e4145c8b` |
| `8b3d881e-e34f-545a-9757-873171c9dc1c` |
| `fe32193e-e656-514f-a57c-f045363d9b2b` |
| `eef347a6-d2c4-5db3-bbca-9ccdbd799044` |
| `40662a74-88c2-596a-82a7-59ee84497227` |
| `d728f3c4-1807-51af-b706-28a7394d375d` |
| `015f1eff-b334-5337-a893-bad0353001c2` |
| `d596eb39-fdeb-594f-9cc0-ec5a6e6a740f` |
| `49f95909-a463-50da-9751-9357d42e4a2f` |
| `9562a0f8-11b8-5d5e-b3bb-b654cbd0572f` |
| `a9c5b35c-0d08-53bc-a4a5-99529cc5ef5d` |
| `f301e8b4-d050-5e98-98c3-a2e160c9bdef` |
| `1dc09ea5-212b-5bf0-a7f1-5f2eef72080a` |
| `fb33098b-c1b2-5dc2-b9a4-3cbd8c6bc2ff` |
| `ce402677-421b-5686-b1eb-4949c37daeff` |
| `ad187869-a667-5a5e-9799-d546b2844cb5` |
| `4e2fbd55-4044-59e2-9786-dde50ef49b0c` |
| `725a13c0-675c-5b80-9cc9-dc1245885fa9` |
| `9d5c3fe6-de55-5101-a01d-48284fc003ee` |
| `6173c6c5-4bce-5e4c-bab7-cf7edac33923` |
| `01fb036d-0ff2-505b-8df6-18332cc72a82` |
| `9a139bb4-bbb8-5ff1-9d8c-f4fdb030fc1b` |
| `045f2ab8-46a9-5246-b469-16df5dd31fdd` |
| `82ffa7ef-b98b-5c9e-a1f5-5f413151f0ae` |
| `f2717d2f-b914-56b6-85a9-8502cf6a598f` |
| `6bd8d0a9-f677-5035-9a9b-4a79920c778b` |
| `8063daf0-5051-5564-8d4c-2b8a1fa5ff6a` |
| `284b67d6-d34b-5105-9685-d0b95fd6e276` |
| `319a1033-0bd7-575d-a7ba-7f6ebc24f235` |
