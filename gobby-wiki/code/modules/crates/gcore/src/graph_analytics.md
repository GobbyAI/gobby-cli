---
title: crates/gcore/src/graph_analytics
type: code_module
provenance:
- file: crates/gcore/src/graph_analytics/leiden.rs
  ranges:
  - 32-40
  - 45-72
  - 76-79
  - 82-87
  - 94-184
  - 195-277
  - 282-336
  - 339-359
  - 366-407
  - 410-425
  - 433-440
  - 443-477
  - 479-482
  - 484-486
  - 488-494
  - 496-504
  - 511-531
  - 536-570
  - 577-595
  - 598-610
  - 613-628
  - 631-634
  - 637-639
  - 642-644
  - 647-654
  - 657-666
  - 669-676
  - 679-687
  - 690-704
  - 707-726
  - 729-737
  - 740-752
  - 755-764
  - 767-784
  - 787-806
  - 809-845
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/graph_analytics/leiden.rs:32-40](crates/gcore/src/graph_analytics/leiden.rs#L32-L40), [crates/gcore/src/graph_analytics/leiden.rs:45-72](crates/gcore/src/graph_analytics/leiden.rs#L45-L72), [crates/gcore/src/graph_analytics/leiden.rs:76-79](crates/gcore/src/graph_analytics/leiden.rs#L76-L79), [crates/gcore/src/graph_analytics/leiden.rs:82-87](crates/gcore/src/graph_analytics/leiden.rs#L82-L87), [crates/gcore/src/graph_analytics/leiden.rs:94-184](crates/gcore/src/graph_analytics/leiden.rs#L94-L184), [crates/gcore/src/graph_analytics/leiden.rs:195-277](crates/gcore/src/graph_analytics/leiden.rs#L195-L277), [crates/gcore/src/graph_analytics/leiden.rs:282-336](crates/gcore/src/graph_analytics/leiden.rs#L282-L336), [crates/gcore/src/graph_analytics/leiden.rs:339-359](crates/gcore/src/graph_analytics/leiden.rs#L339-L359), [crates/gcore/src/graph_analytics/leiden.rs:366-407](crates/gcore/src/graph_analytics/leiden.rs#L366-L407), [crates/gcore/src/graph_analytics/leiden.rs:410-425](crates/gcore/src/graph_analytics/leiden.rs#L410-L425), [crates/gcore/src/graph_analytics/leiden.rs:433-440](crates/gcore/src/graph_analytics/leiden.rs#L433-L440), [crates/gcore/src/graph_analytics/leiden.rs:443-477](crates/gcore/src/graph_analytics/leiden.rs#L443-L477), [crates/gcore/src/graph_analytics/leiden.rs:479-482](crates/gcore/src/graph_analytics/leiden.rs#L479-L482), [crates/gcore/src/graph_analytics/leiden.rs:484-486](crates/gcore/src/graph_analytics/leiden.rs#L484-L486), [crates/gcore/src/graph_analytics/leiden.rs:488-494](crates/gcore/src/graph_analytics/leiden.rs#L488-L494), [crates/gcore/src/graph_analytics/leiden.rs:496-504](crates/gcore/src/graph_analytics/leiden.rs#L496-L504), [crates/gcore/src/graph_analytics/leiden.rs:511-531](crates/gcore/src/graph_analytics/leiden.rs#L511-L531), [crates/gcore/src/graph_analytics/leiden.rs:536-570](crates/gcore/src/graph_analytics/leiden.rs#L536-L570), [crates/gcore/src/graph_analytics/leiden.rs:577-595](crates/gcore/src/graph_analytics/leiden.rs#L577-L595), [crates/gcore/src/graph_analytics/leiden.rs:598-610](crates/gcore/src/graph_analytics/leiden.rs#L598-L610), [crates/gcore/src/graph_analytics/leiden.rs:613-628](crates/gcore/src/graph_analytics/leiden.rs#L613-L628), [crates/gcore/src/graph_analytics/leiden.rs:631-634](crates/gcore/src/graph_analytics/leiden.rs#L631-L634), [crates/gcore/src/graph_analytics/leiden.rs:637-639](crates/gcore/src/graph_analytics/leiden.rs#L637-L639), [crates/gcore/src/graph_analytics/leiden.rs:642-644](crates/gcore/src/graph_analytics/leiden.rs#L642-L644), [crates/gcore/src/graph_analytics/leiden.rs:647-654](crates/gcore/src/graph_analytics/leiden.rs#L647-L654), [crates/gcore/src/graph_analytics/leiden.rs:657-666](crates/gcore/src/graph_analytics/leiden.rs#L657-L666), [crates/gcore/src/graph_analytics/leiden.rs:669-676](crates/gcore/src/graph_analytics/leiden.rs#L669-L676), [crates/gcore/src/graph_analytics/leiden.rs:679-687](crates/gcore/src/graph_analytics/leiden.rs#L679-L687), [crates/gcore/src/graph_analytics/leiden.rs:690-704](crates/gcore/src/graph_analytics/leiden.rs#L690-L704), [crates/gcore/src/graph_analytics/leiden.rs:707-726](crates/gcore/src/graph_analytics/leiden.rs#L707-L726), [crates/gcore/src/graph_analytics/leiden.rs:729-737](crates/gcore/src/graph_analytics/leiden.rs#L729-L737), [crates/gcore/src/graph_analytics/leiden.rs:740-752](crates/gcore/src/graph_analytics/leiden.rs#L740-L752), [crates/gcore/src/graph_analytics/leiden.rs:755-764](crates/gcore/src/graph_analytics/leiden.rs#L755-L764), [crates/gcore/src/graph_analytics/leiden.rs:767-784](crates/gcore/src/graph_analytics/leiden.rs#L767-L784), [crates/gcore/src/graph_analytics/leiden.rs:787-806](crates/gcore/src/graph_analytics/leiden.rs#L787-L806), [crates/gcore/src/graph_analytics/leiden.rs:809-845](crates/gcore/src/graph_analytics/leiden.rs#L809-L845)

</details>

# crates/gcore/src/graph_analytics

Parent: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

The `graph_analytics` module is responsible for executing deterministic, std-only weighted Leiden community detection (Traag, Waltman & van Eck, 2019) over dense integer-index graphs crates/gcore/src/graph_analytics/leiden.rs:1-10. This core kernel is decoupled from public types like `AnalyticsGraph` and `Community` to permit isolated unit testing, relying on an adapter facade in `graph_analytics.rs` to map node IDs and memberships back and forth crates/gcore/src/graph_analytics/leiden.rs:3-6.

Key execution flows run through three iterative Leiden phases: local moving, refinement (which ensures internally-connected communities), and level-to-level coarsening/aggregation, continuing until the graph no longer coarsens or hits a recursion depth limit of 64 levels crates/gcore/src/graph_analytics/leiden.rs:7-10,20. The algorithm runs deterministically without using an RNG, relying on strict-improvement greedy steps where every choice is a strict ascending change crates/gcore/src/graph_analytics/leiden.rs:9-10. During creation and aggregation, the `LeidenGraph` maintains sorted adjacency lists, folds duplicate edges, and guarantees the invariant that the sum of node strengths equals twice the total edge weight crates/gcore/src/graph_analytics/leiden.rs:22-26,45-48.

| Symbol / Constant | Type | Description | Citation |
| --- | --- | --- | --- |
| `DEFAULT_GAMMA` | `const f64` | Default resolution parameter $\gamma$ (standard modularity) set to `1.0`. | crates/gcore/src/graph_analytics/leiden.rs:14 |
| `EPS` | `const f64` | Strict-improvement threshold of `1e-12` required for moves. | crates/gcore/src/graph_analytics/leiden.rs:17 |
| `MAX_LEVELS` | `const usize` | Hard cap on aggregation depth (runaway-recursion backstop) set to `64`. | crates/gcore/src/graph_analytics/leiden.rs:20 |
| `LeidenGraph` | `struct` | Weighted undirected graph over dense integer node indices. | crates/gcore/src/graph_analytics/leiden.rs:22-30 |
| `LeidenGraph::new` | `fn` | Builds graph from edge list, folding duplicate pairs and sorting adjacencies. | crates/gcore/src/graph_analytics/leiden.rs:45-51 |
| `Partition` | `struct` | Represents the partition state across Leiden phases. | crates/gcore/src/graph_analytics/leiden.rs:32-40 |
| `local_moving` | `fn` | Executes the local moving step of the Leiden algorithm. | crates/gcore/src/graph_analytics/leiden.rs:32-40 |
| `refine_partition` | `fn` | Performs partition refinement to guarantee internally-connected communities. | crates/gcore/src/graph_analytics/leiden.rs:32-40 |
| `aggregate_graph` | `fn` | Aggregates community structures for the next hierarchical level. | crates/gcore/src/graph_analytics/leiden.rs:32-40 |
| `renumber_dense` | `fn` | Helper for renumbering node IDs to maintain dense integer sequences. | crates/gcore/src/graph_analytics/leiden.rs:32-40 |
| `dense_relabel` | `fn` | Relabels nodes sequentially during graph coarsening. | crates/gcore/src/graph_analytics/leiden.rs:32-40 |
[crates/gcore/src/graph_analytics/leiden.rs:32-40]
[crates/gcore/src/graph_analytics/leiden.rs:45-72]
[crates/gcore/src/graph_analytics/leiden.rs:76-79]
[crates/gcore/src/graph_analytics/leiden.rs:82-87]
[crates/gcore/src/graph_analytics/leiden.rs:94-184]

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/graph_analytics/leiden.rs\|crates/gcore/src/graph_analytics/leiden.rs]] | Implements a deterministic, std-only weighted Leiden community-detection kernel over dense integer-index graphs, with a façade-friendly internal representation that keeps adjacency lists sorted, folds duplicate edges, and maintains the `Σ strength == 2·total_weight` invariant. `LeidenGraph` and `Partition` provide the core graph/partition state, while `local_moving`, `refine_partition`, `aggregate_graph`, `renumber_dense`, and `dense_relabel` drive the three Leiden phases and level-to-level coarsening. The remaining helpers expose detection, modularity, connectivity and invariant checks, plus a suite of test cases that validate correctness, determinism, edge folding, aggregation, and back-projection behavior. [crates/gcore/src/graph_analytics/leiden.rs:32-40] [crates/gcore/src/graph_analytics/leiden.rs:45-72] [crates/gcore/src/graph_analytics/leiden.rs:76-79] [crates/gcore/src/graph_analytics/leiden.rs:82-87] [crates/gcore/src/graph_analytics/leiden.rs:94-184] |

## Components

| Component ID |
| --- |
| `10643e1f-8b4d-56c2-aaea-dc0eaa6d8e5e` |
| `410fc44c-6256-5066-80df-c92a0c639154` |
| `506327f8-24b0-5bc9-879a-9d1f4cca002e` |
| `fb6d3f00-1b33-5485-abb9-094d865bd8cb` |
| `b50cc58d-7bde-5717-80c2-9bf5f38f4909` |
| `12d86f44-35c2-51ae-b36b-c9c1a5ae1d2a` |
| `6f44fe09-f769-585a-b174-5415aed620d6` |
| `d398ad74-115f-5304-be52-3e8f0809aeff` |
| `4535eb12-f6b7-5d2e-8d63-d063cd6e4584` |
| `cf630d00-8c2b-5921-ba5d-2ae128308e55` |
| `e28ea454-4ce0-5805-8a3e-b3bcc8d103a4` |
| `2821e810-6c51-51b4-8e72-c3feb213af96` |
| `7905ccbd-d341-593c-a127-451a77d48598` |
| `3c96c976-85dc-5748-89cf-bcbd5ac3c002` |
| `934c4817-4219-5e6a-8b98-de861315c1c7` |
| `a6bce990-bca1-5c57-834b-1d34fa579e66` |
| `b27da28d-3b74-59d6-8b19-af94d7f78a34` |
| `2fab2cc4-53d1-5076-b9f7-288dc29122a7` |
| `ac0269bb-7340-5c54-9781-a4cc7753027e` |
| `d816f36f-3c38-58cd-9f06-8d267c842951` |
| `200af774-19be-56fd-8aa9-3a17f1b3f1bb` |
| `d7228d7e-0019-53b4-99dd-028f7fe3da64` |
| `0616e115-9e4a-5b18-8a41-c7f7b55ee2d3` |
| `a6114e85-5b9f-597f-b0d4-5d3ef34b0533` |
| `785d4f2f-645d-51c9-8d70-450b92137e53` |
| `54b8068d-72a1-512f-af6d-8e19373284aa` |
| `658a288a-b7aa-5c96-aa07-de491b140bd7` |
| `ddffa4a5-5ab0-55d0-993d-ea15e3378265` |
| `7f48bedc-dd6c-5654-9099-9998037e18f9` |
| `f7164a8a-c560-54fc-aaed-e554d7b38fe2` |
| `a0cb0d70-b7a5-5d0d-93c8-0580a8ee1673` |
| `95235403-b02d-5a67-a3a2-cad45699f713` |
| `61001f47-e176-536a-a16e-7ea1abdd711f` |
| `3b7c21d5-e08d-520f-b749-9d3ae3b27d0b` |
| `61113965-d0f0-5af3-8a18-56325eef6861` |
| `ce1a46e9-bec0-5a2b-8fd9-22ff4c3ce0cf` |
