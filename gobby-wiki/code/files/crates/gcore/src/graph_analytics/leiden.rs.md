---
title: crates/gcore/src/graph_analytics/leiden.rs
type: code_file
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

# crates/gcore/src/graph_analytics/leiden.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Implements a deterministic, std-only weighted Leiden community-detection kernel over dense integer-index graphs, with a façade-friendly internal representation that keeps adjacency lists sorted, folds duplicate edges, and maintains the `Σ strength == 2·total_weight` invariant. `LeidenGraph` and `Partition` provide the core graph/partition state, while `local_moving`, `refine_partition`, `aggregate_graph`, `renumber_dense`, and `dense_relabel` drive the three Leiden phases and level-to-level coarsening. The remaining helpers expose detection, modularity, connectivity and invariant checks, plus a suite of test cases that validate correctness, determinism, edge folding, aggregation, and back-projection behavior.
[crates/gcore/src/graph_analytics/leiden.rs:32-40]
[crates/gcore/src/graph_analytics/leiden.rs:45-72]
[crates/gcore/src/graph_analytics/leiden.rs:76-79]
[crates/gcore/src/graph_analytics/leiden.rs:82-87]
[crates/gcore/src/graph_analytics/leiden.rs:94-184]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `LeidenGraph` | class | `pub(super) struct LeidenGraph {` | `LeidenGraph [class]` | `10643e1f-8b4d-56c2-aaea-dc0eaa6d8e5e` | 32-40 [crates/gcore/src/graph_analytics/leiden.rs:32-40] | Indexed class `LeidenGraph` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:32-40] |
| `LeidenGraph::new` | method | `pub(super) fn new(n: usize, edges: &[(usize, usize, f64)]) -> Self {` | `LeidenGraph::new [method]` | `410fc44c-6256-5066-80df-c92a0c639154` | 45-72 [crates/gcore/src/graph_analytics/leiden.rs:45-72] | Indexed method `LeidenGraph::new` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:45-72] |
| `Partition` | class | `struct Partition {` | `Partition [class]` | `506327f8-24b0-5bc9-879a-9d1f4cca002e` | 76-79 [crates/gcore/src/graph_analytics/leiden.rs:76-79] | Indexed class `Partition` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:76-79] |
| `Partition::singletons` | method | `fn singletons(g: &LeidenGraph) -> Self {` | `Partition::singletons [method]` | `fb6d3f00-1b33-5485-abb9-094d865bd8cb` | 82-87 [crates/gcore/src/graph_analytics/leiden.rs:82-87] | Indexed method `Partition::singletons` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:82-87] |
| `local_moving` | function | `fn local_moving(g: &LeidenGraph, partition: &mut Partition, gamma: f64) -> bool {` | `local_moving [function]` | `b50cc58d-7bde-5717-80c2-9bf5f38f4909` | 94-184 [crates/gcore/src/graph_analytics/leiden.rs:94-184] | Indexed function `local_moving` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:94-184] |
| `refine_partition` | function | `fn refine_partition(g: &LeidenGraph, partition: &Partition, gamma: f64) -> Partition {` | `refine_partition [function]` | `12d86f44-35c2-51ae-b36b-c9c1a5ae1d2a` | 195-277 [crates/gcore/src/graph_analytics/leiden.rs:195-277] | Indexed function `refine_partition` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:195-277] |
| `aggregate_graph` | function | `fn aggregate_graph(` | `aggregate_graph [function]` | `6f44fe09-f769-585a-b174-5415aed620d6` | 282-336 [crates/gcore/src/graph_analytics/leiden.rs:282-336] | Indexed function `aggregate_graph` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:282-336] |
| `renumber_dense` | function | `fn renumber_dense(partition: &mut Partition, g: &LeidenGraph) {` | `renumber_dense [function]` | `d398ad74-115f-5304-be52-3e8f0809aeff` | 339-359 [crates/gcore/src/graph_analytics/leiden.rs:339-359] | Indexed function `renumber_dense` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:339-359] |
| `detect_communities` | function | `pub(super) fn detect_communities(g: &LeidenGraph, gamma: f64) -> Vec<usize> {` | `detect_communities [function]` | `4535eb12-f6b7-5d2e-8d63-d063cd6e4584` | 366-407 [crates/gcore/src/graph_analytics/leiden.rs:366-407] | Indexed function `detect_communities` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:366-407] |
| `dense_relabel` | function | `fn dense_relabel(membership: &mut [usize]) {` | `dense_relabel [function]` | `cf630d00-8c2b-5921-ba5d-2ae128308e55` | 410-425 [crates/gcore/src/graph_analytics/leiden.rs:410-425] | Indexed function `dense_relabel` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:410-425] |
| `assert_strength_invariant` | function | `fn assert_strength_invariant(g: &LeidenGraph) {` | `assert_strength_invariant [function]` | `e28ea454-4ce0-5805-8a3e-b3bcc8d103a4` | 433-440 [crates/gcore/src/graph_analytics/leiden.rs:433-440] | Indexed function `assert_strength_invariant` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:433-440] |
| `assert_communities_connected` | function | `fn assert_communities_connected(n: usize, edges: &[(usize, usize, f64)], membership: &[usize]) {` | `assert_communities_connected [function]` | `2821e810-6c51-51b4-8e72-c3feb213af96` | 443-477 [crates/gcore/src/graph_analytics/leiden.rs:443-477] | Indexed function `assert_communities_connected` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:443-477] |
| `detect` | function | `fn detect(n: usize, edges: &[(usize, usize, f64)]) -> Vec<usize> {` | `detect [function]` | `7905ccbd-d341-593c-a127-451a77d48598` | 479-482 [crates/gcore/src/graph_analytics/leiden.rs:479-482] | Indexed function `detect` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:479-482] |
| `community_count` | function | `fn community_count(membership: &[usize]) -> usize {` | `community_count [function]` | `3c96c976-85dc-5748-89cf-bcbd5ac3c002` | 484-486 [crates/gcore/src/graph_analytics/leiden.rs:484-486] | Indexed function `community_count` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:484-486] |
| `triangle` | function | `fn triangle(base: usize) -> Vec<(usize, usize, f64)> {` | `triangle [function]` | `934c4817-4219-5e6a-8b98-de861315c1c7` | 488-494 [crates/gcore/src/graph_analytics/leiden.rs:488-494] | Indexed function `triangle` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:488-494] |
| `clique` | function | `fn clique(base: usize, size: usize, weight: f64) -> Vec<(usize, usize, f64)> {` | `clique [function]` | `a6bce990-bca1-5c57-834b-1d34fa579e66` | 496-504 [crates/gcore/src/graph_analytics/leiden.rs:496-504] | Indexed function `clique` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:496-504] |
| `modularity` | function | `fn modularity(g: &LeidenGraph, membership: &[usize], gamma: f64) -> f64 {` | `modularity [function]` | `b27da28d-3b74-59d6-8b19-af94d7f78a34` | 511-531 [crates/gcore/src/graph_analytics/leiden.rs:511-531] | Indexed function `modularity` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:511-531] |
| `karate_club` | function | `fn karate_club() -> Vec<(usize, usize, f64)> {` | `karate_club [function]` | `2fab2cc4-53d1-5076-b9f7-288dc29122a7` | 536-570 [crates/gcore/src/graph_analytics/leiden.rs:536-570] | Indexed function `karate_club` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:536-570] |
| `assert_no_improving_single_move` | function | `fn assert_no_improving_single_move(g: &LeidenGraph, membership: &[usize], gamma: f64) {` | `assert_no_improving_single_move [function]` | `ac0269bb-7340-5c54-9781-a4cc7753027e` | 577-595 [crates/gcore/src/graph_analytics/leiden.rs:577-595] | Indexed function `assert_no_improving_single_move` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:577-595] |
| `two_triangles_with_bridge_split` | function | `fn two_triangles_with_bridge_split() {` | `two_triangles_with_bridge_split [function]` | `d816f36f-3c38-58cd-9f06-8d267c842951` | 598-610 [crates/gcore/src/graph_analytics/leiden.rs:598-610] | Indexed function `two_triangles_with_bridge_split` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:598-610] |
| `two_cliques_recover_planted_partition` | function | `fn two_cliques_recover_planted_partition() {` | `two_cliques_recover_planted_partition [function]` | `200af774-19be-56fd-8aa9-3a17f1b3f1bb` | 613-628 [crates/gcore/src/graph_analytics/leiden.rs:613-628] | Indexed function `two_cliques_recover_planted_partition` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:613-628] |
| `no_edge_multi_node_graph_is_all_singletons` | function | `fn no_edge_multi_node_graph_is_all_singletons() {` | `no_edge_multi_node_graph_is_all_singletons [function]` | `d7228d7e-0019-53b4-99dd-028f7fe3da64` | 631-634 [crates/gcore/src/graph_analytics/leiden.rs:631-634] | Indexed function `no_edge_multi_node_graph_is_all_singletons` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:631-634] |
| `empty_graph_returns_empty` | function | `fn empty_graph_returns_empty() {` | `empty_graph_returns_empty [function]` | `0616e115-9e4a-5b18-8a41-c7f7b55ee2d3` | 637-639 [crates/gcore/src/graph_analytics/leiden.rs:637-639] | Indexed function `empty_graph_returns_empty` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:637-639] |
| `single_node_returns_one_community` | function | `fn single_node_returns_one_community() {` | `single_node_returns_one_community [function]` | `a6114e85-5b9f-597f-b0d4-5d3ef34b0533` | 642-644 [crates/gcore/src/graph_analytics/leiden.rs:642-644] | Indexed function `single_node_returns_one_community` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:642-644] |
| `triangle_with_isolated_node_yields_two_communities` | function | `fn triangle_with_isolated_node_yields_two_communities() {` | `triangle_with_isolated_node_yields_two_communities [function]` | `785d4f2f-645d-51c9-8d70-450b92137e53` | 647-654 [crates/gcore/src/graph_analytics/leiden.rs:647-654] | Indexed function `triangle_with_isolated_node_yields_two_communities` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:647-654] |
| `four_node_path_is_not_all_singletons` | function | `fn four_node_path_is_not_all_singletons() {` | `four_node_path_is_not_all_singletons [function]` | `54b8068d-72a1-512f-af6d-8e19373284aa` | 657-666 [crates/gcore/src/graph_analytics/leiden.rs:657-666] | Indexed function `four_node_path_is_not_all_singletons` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:657-666] |
| `duplicate_and_reciprocal_edges_fold_by_summation` | function | `fn duplicate_and_reciprocal_edges_fold_by_summation() {` | `duplicate_and_reciprocal_edges_fold_by_summation [function]` | `658a288a-b7aa-5c96-aa07-de491b140bd7` | 669-676 [crates/gcore/src/graph_analytics/leiden.rs:669-676] | Indexed function `duplicate_and_reciprocal_edges_fold_by_summation` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:669-676] |
| `self_loop_contributes_double_strength_single_weight` | function | `fn self_loop_contributes_double_strength_single_weight() {` | `self_loop_contributes_double_strength_single_weight [function]` | `ddffa4a5-5ab0-55d0-993d-ea15e3378265` | 679-687 [crates/gcore/src/graph_analytics/leiden.rs:679-687] | Indexed function `self_loop_contributes_double_strength_single_weight` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:679-687] |
| `aggregation_preserves_strength_invariant_and_total_weight` | function | `fn aggregation_preserves_strength_invariant_and_total_weight() {` | `aggregation_preserves_strength_invariant_and_total_weight [function]` | `7f48bedc-dd6c-5654-9099-9998037e18f9` | 690-704 [crates/gcore/src/graph_analytics/leiden.rs:690-704] | Indexed function `aggregation_preserves_strength_invariant_and_total_weight` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:690-704] |
| `multi_level_back_projection_maps_original_nodes` | function | `fn multi_level_back_projection_maps_original_nodes() {` | `multi_level_back_projection_maps_original_nodes [function]` | `f7164a8a-c560-54fc-aaed-e554d7b38fe2` | 707-726 [crates/gcore/src/graph_analytics/leiden.rs:707-726] | Indexed function `multi_level_back_projection_maps_original_nodes` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:707-726] |
| `output_is_deterministic_across_repeats` | function | `fn output_is_deterministic_across_repeats() {` | `output_is_deterministic_across_repeats [function]` | `a0cb0d70-b7a5-5d0d-93c8-0580a8ee1673` | 729-737 [crates/gcore/src/graph_analytics/leiden.rs:729-737] | Indexed function `output_is_deterministic_across_repeats` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:729-737] |
| `output_is_invariant_to_edge_list_order` | function | `fn output_is_invariant_to_edge_list_order() {` | `output_is_invariant_to_edge_list_order [function]` | `95235403-b02d-5a67-a3a2-cad45699f713` | 740-752 [crates/gcore/src/graph_analytics/leiden.rs:740-752] | Indexed function `output_is_invariant_to_edge_list_order` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:740-752] |
| `weighting_pulls_a_node_toward_the_heavier_community` | function | `fn weighting_pulls_a_node_toward_the_heavier_community() {` | `weighting_pulls_a_node_toward_the_heavier_community [function]` | `61001f47-e176-536a-a16e-7ea1abdd711f` | 755-764 [crates/gcore/src/graph_analytics/leiden.rs:755-764] | Indexed function `weighting_pulls_a_node_toward_the_heavier_community` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:755-764] |
| `local_moving_isolates_over_merged_self_loop_cluster` | function | `fn local_moving_isolates_over_merged_self_loop_cluster() {` | `local_moving_isolates_over_merged_self_loop_cluster [function]` | `3b7c21d5-e08d-520f-b749-9d3ae3b27d0b` | 767-784 [crates/gcore/src/graph_analytics/leiden.rs:767-784] | Indexed function `local_moving_isolates_over_merged_self_loop_cluster` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:767-784] |
| `zachary_karate_club_finds_modular_structure` | function | `fn zachary_karate_club_finds_modular_structure() {` | `zachary_karate_club_finds_modular_structure [function]` | `61113965-d0f0-5af3-8a18-56325eef6861` | 787-806 [crates/gcore/src/graph_analytics/leiden.rs:787-806] | Indexed function `zachary_karate_club_finds_modular_structure` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:787-806] |
| `local_moving_partition_has_no_improving_single_node_move` | function | `fn local_moving_partition_has_no_improving_single_node_move() {` | `local_moving_partition_has_no_improving_single_node_move [function]` | `ce1a46e9-bec0-5a2b-8fd9-22ff4c3ce0cf` | 809-845 [crates/gcore/src/graph_analytics/leiden.rs:809-845] | Indexed function `local_moving_partition_has_no_improving_single_node_move` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:809-845] |
