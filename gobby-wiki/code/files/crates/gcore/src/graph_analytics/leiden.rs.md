---
title: crates/gcore/src/graph_analytics/leiden.rs
type: code_file
provenance:
- file: crates/gcore/src/graph_analytics/leiden.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/graph_analytics/leiden.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/graph_analytics/leiden.rs` exposes 36 indexed API symbols.

## How it fits

`crates/gcore/src/graph_analytics/leiden.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LeidenGraph` | class | Indexed class `LeidenGraph` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:32-40] |
| `LeidenGraph::new` | method | Indexed method `LeidenGraph::new` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:45-72] |
| `Partition` | class | Indexed class `Partition` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:76-79] |
| `Partition::singletons` | method | Indexed method `Partition::singletons` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:82-87] |
| `local_moving` | function | Indexed function `local_moving` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:94-184] |
| `refine_partition` | function | Indexed function `refine_partition` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:195-277] |
| `aggregate_graph` | function | Indexed function `aggregate_graph` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:282-336] |
| `renumber_dense` | function | Indexed function `renumber_dense` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:339-359] |
| `detect_communities` | function | Indexed function `detect_communities` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:366-407] |
| `dense_relabel` | function | Indexed function `dense_relabel` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:410-425] |
| `assert_strength_invariant` | function | Indexed function `assert_strength_invariant` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:433-440] |
| `assert_communities_connected` | function | Indexed function `assert_communities_connected` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:443-477] |
| `detect` | function | Indexed function `detect` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:479-482] |
| `community_count` | function | Indexed function `community_count` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:484-486] |
| `triangle` | function | Indexed function `triangle` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:488-494] |
| `clique` | function | Indexed function `clique` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:496-504] |
| `modularity` | function | Indexed function `modularity` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:511-531] |
| `karate_club` | function | Indexed function `karate_club` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:536-570] |
| `assert_no_improving_single_move` | function | Indexed function `assert_no_improving_single_move` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:577-595] |
| `two_triangles_with_bridge_split` | function | Indexed function `two_triangles_with_bridge_split` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:598-610] |
| `two_cliques_recover_planted_partition` | function | Indexed function `two_cliques_recover_planted_partition` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:613-628] |
| `no_edge_multi_node_graph_is_all_singletons` | function | Indexed function `no_edge_multi_node_graph_is_all_singletons` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:631-634] |
| `empty_graph_returns_empty` | function | Indexed function `empty_graph_returns_empty` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:637-639] |
| `single_node_returns_one_community` | function | Indexed function `single_node_returns_one_community` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:642-644] |
| `triangle_with_isolated_node_yields_two_communities` | function | Indexed function `triangle_with_isolated_node_yields_two_communities` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:647-654] |
| `four_node_path_is_not_all_singletons` | function | Indexed function `four_node_path_is_not_all_singletons` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:657-666] |
| `duplicate_and_reciprocal_edges_fold_by_summation` | function | Indexed function `duplicate_and_reciprocal_edges_fold_by_summation` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:669-676] |
| `self_loop_contributes_double_strength_single_weight` | function | Indexed function `self_loop_contributes_double_strength_single_weight` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:679-687] |
| `aggregation_preserves_strength_invariant_and_total_weight` | function | Indexed function `aggregation_preserves_strength_invariant_and_total_weight` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:690-704] |
| `multi_level_back_projection_maps_original_nodes` | function | Indexed function `multi_level_back_projection_maps_original_nodes` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:707-726] |
| `output_is_deterministic_across_repeats` | function | Indexed function `output_is_deterministic_across_repeats` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:729-737] |
| `output_is_invariant_to_edge_list_order` | function | Indexed function `output_is_invariant_to_edge_list_order` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:740-752] |
| `weighting_pulls_a_node_toward_the_heavier_community` | function | Indexed function `weighting_pulls_a_node_toward_the_heavier_community` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:755-764] |
| `local_moving_isolates_over_merged_self_loop_cluster` | function | Indexed function `local_moving_isolates_over_merged_self_loop_cluster` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:767-784] |
| `zachary_karate_club_finds_modular_structure` | function | Indexed function `zachary_karate_club_finds_modular_structure` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:787-806] |
| `local_moving_partition_has_no_improving_single_node_move` | function | Indexed function `local_moving_partition_has_no_improving_single_node_move` in `crates/gcore/src/graph_analytics/leiden.rs`. [crates/gcore/src/graph_analytics/leiden.rs:809-845] |

