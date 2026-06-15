---
title: crates/gcore/src/graph_analytics/leiden.rs
type: code_file
provenance:
- file: crates/gcore/src/graph_analytics/leiden.rs
  ranges:
  - 32-40
  - 42-73
  - 76-79
  - 81-88
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

# crates/gcore/src/graph_analytics/leiden.rs

Module: [[code/modules/crates/gcore/src/graph_analytics|crates/gcore/src/graph_analytics]]

## Purpose

Implements a std-only, deterministic weighted Leiden community detection kernel over dense integer node IDs. It defines `LeidenGraph` to normalize an edge list into sorted weighted adjacency lists while tracking vertex strength and total weight, then uses `Partition` plus `local_moving`, `refine_partition`, `aggregate_graph`, and `renumber_dense` to run the multilevel Leiden loop in `detect_communities` and project the final communities back to original nodes. The rest of the file provides helpers for relabeling, invariant and connectivity checks, small graph generators and modularity calculation, a `detect` wrapper, and a broad test suite validating correctness, determinism, and behavior on common graph shapes.
[crates/gcore/src/graph_analytics/leiden.rs:32-40]
[crates/gcore/src/graph_analytics/leiden.rs:42-73]
[crates/gcore/src/graph_analytics/leiden.rs:45-72]
[crates/gcore/src/graph_analytics/leiden.rs:76-79]
[crates/gcore/src/graph_analytics/leiden.rs:81-88]

## API Symbols

- `LeidenGraph` (class) component `LeidenGraph [class]` (`10643e1f-8b4d-56c2-aaea-dc0eaa6d8e5e`) lines 32-40 [crates/gcore/src/graph_analytics/leiden.rs:32-40]
  - Signature: `pub(super) struct LeidenGraph {`
  - Purpose: 'LeidenGraph' is an internal graph representation storing the vertex count, per-vertex sorted weighted adjacency lists with self-loops represented once, per-vertex weighted strength with self-loops counted twice, and the total edge weight 'm' with self-loops counted once. [crates/gcore/src/graph_analytics/leiden.rs:32-40]
- `LeidenGraph` (class) component `LeidenGraph [class]` (`a7a73fcf-600a-5987-b123-0f897b163552`) lines 42-73 [crates/gcore/src/graph_analytics/leiden.rs:42-73]
  - Signature: `impl LeidenGraph {`
  - Purpose: 'LeidenGraph' constructs a weighted graph from an edge list by aggregating duplicate edges into deterministic, sorted adjacency lists while computing per-node strength and total edge weight, including double-counting self-loop contribution in node strength. [crates/gcore/src/graph_analytics/leiden.rs:42-73]
- `LeidenGraph.new` (method) component `LeidenGraph.new [method]` (`410fc44c-6256-5066-80df-c92a0c639154`) lines 45-72 [crates/gcore/src/graph_analytics/leiden.rs:45-72]
  - Signature: `pub(super) fn new(n: usize, edges: &[(usize, usize, f64)]) -> Self {`
  - Purpose: Constructs a weighted undirected graph from an edge list by accumulating duplicate edges into per-vertex sorted adjacency lists, computing each vertex’s weighted strength with self-loops counted twice, and summing the total edge weight. [crates/gcore/src/graph_analytics/leiden.rs:45-72]
- `Partition` (class) component `Partition [class]` (`506327f8-24b0-5bc9-879a-9d1f4cca002e`) lines 76-79 [crates/gcore/src/graph_analytics/leiden.rs:76-79]
  - Signature: `struct Partition {`
  - Purpose: 'Partition' is a data structure that stores a community assignment for each item in 'community_of' and the corresponding per-community total weights or degrees in 'sigma_tot'. [crates/gcore/src/graph_analytics/leiden.rs:76-79]
- `Partition` (class) component `Partition [class]` (`98e0e768-8420-5bb1-8a65-535eef2facdd`) lines 81-88 [crates/gcore/src/graph_analytics/leiden.rs:81-88]
  - Signature: `impl Partition {`
  - Purpose: 'Partition::singletons' constructs a partition in which every vertex starts in its own community by setting 'community_of[i] = i' for all nodes and initializing 'sigma_tot' as a clone of the graph’s 'strength' vector. [crates/gcore/src/graph_analytics/leiden.rs:81-88]
- `Partition.singletons` (method) component `Partition.singletons [method]` (`fb6d3f00-1b33-5485-abb9-094d865bd8cb`) lines 82-87 [crates/gcore/src/graph_analytics/leiden.rs:82-87]
  - Signature: `fn singletons(g: &LeidenGraph) -> Self {`
  - Purpose: Initializes a Leiden community state by assigning each vertex to its own community and setting 'sigma_tot' to a clone of the graph’s node-strength vector. [crates/gcore/src/graph_analytics/leiden.rs:82-87]
- `local_moving` (function) component `local_moving [function]` (`b50cc58d-7bde-5717-80c2-9bf5f38f4909`) lines 94-184 [crates/gcore/src/graph_analytics/leiden.rs:94-184]
  - Signature: `fn local_moving(g: &LeidenGraph, partition: &mut Partition, gamma: f64) -> bool {`
  - Purpose: Performs one local-moving pass over all vertices, temporarily removing each node from its current community and reassigning it to the neighboring community, or a fresh isolated community if best, that maximizes the modularity-style gain 'k_u,in - gamma * k_u * sigma_tot / (2m)', returning 'true' if any node changes community. [crates/gcore/src/graph_analytics/leiden.rs:94-184]
- `refine_partition` (function) component `refine_partition [function]` (`12d86f44-35c2-51ae-b36b-c9c1a5ae1d2a`) lines 195-277 [crates/gcore/src/graph_analytics/leiden.rs:195-277]
  - Signature: `fn refine_partition(g: &LeidenGraph, partition: &Partition, gamma: f64) -> Partition {`
  - Purpose: It iterates over singleton nodes within each parent community and greedily merges each into the eligible neighboring refined subcommunity that gives the highest positive modularity-style gain under the 'gamma'-well-connectedness criterion, returning the resulting refined partition and updated community strength totals. [crates/gcore/src/graph_analytics/leiden.rs:195-277]
- `aggregate_graph` (function) component `aggregate_graph [function]` (`6f44fe09-f769-585a-b174-5415aed620d6`) lines 282-336 [crates/gcore/src/graph_analytics/leiden.rs:282-336]
  - Signature: `fn aggregate_graph(`
  - Purpose: 'aggregate_graph' contracts a 'LeidenGraph' by mapping nodes to dense super-nodes using 'refined.community_of', aggregates undirected edge weights into a new supergraph with self-loops for intra-community edges, initializes the supergraph partition from each super-node’s representative node in 'partition', renumbers that partition densely, and returns the contracted graph, partition, and original-to-super-node mapping. [crates/gcore/src/graph_analytics/leiden.rs:282-336]
- `renumber_dense` (function) component `renumber_dense [function]` (`d398ad74-115f-5304-be52-3e8f0809aeff`) lines 339-359 [crates/gcore/src/graph_analytics/leiden.rs:339-359]
  - Signature: `fn renumber_dense(partition: &mut Partition, g: &LeidenGraph) {`
  - Purpose: Renumbers the partition’s community IDs into a dense 0-based range in first-seen order and recomputes 'sigma_tot' as the total vertex strength per new community from 'g'. [crates/gcore/src/graph_analytics/leiden.rs:339-359]
- `detect_communities` (function) component `detect_communities [function]` (`4535eb12-f6b7-5d2e-8d63-d063cd6e4584`) lines 366-407 [crates/gcore/src/graph_analytics/leiden.rs:366-407]
  - Signature: `pub(super) fn detect_communities(g: &LeidenGraph, gamma: f64) -> Vec<usize> {`
  - Purpose: Runs a multilevel Leiden-style community detection loop that repeatedly performs local moving and refinement, aggregates the graph until no further coarsening is possible or 'MAX_LEVELS' is reached, then projects the final partition back to the original nodes and densely relabels the community IDs. [crates/gcore/src/graph_analytics/leiden.rs:366-407]
- `dense_relabel` (function) component `dense_relabel [function]` (`cf630d00-8c2b-5921-ba5d-2ae128308e55`) lines 410-425 [crates/gcore/src/graph_analytics/leiden.rs:410-425]
  - Signature: `fn dense_relabel(membership: &mut [usize]) {`
  - Purpose: Rewrites 'membership' in place so each distinct label is assigned the next available dense index in order of first appearance, using a 'BTreeMap' to preserve a deterministic remapping of old labels to '0..n-1'. [crates/gcore/src/graph_analytics/leiden.rs:410-425]
- `assert_strength_invariant` (function) component `assert_strength_invariant [function]` (`e28ea454-4ce0-5805-8a3e-b3bcc8d103a4`) lines 433-440 [crates/gcore/src/graph_analytics/leiden.rs:433-440]
  - Signature: `fn assert_strength_invariant(g: &LeidenGraph) {`
  - Purpose: Checks that the sum of all vertex strengths in 'g' equals '2 * g.total_weight' within '1e-9', panicking with a diagnostic message if the invariant is violated. [crates/gcore/src/graph_analytics/leiden.rs:433-440]
- `assert_communities_connected` (function) component `assert_communities_connected [function]` (`2821e810-6c51-51b4-8e72-c3feb213af96`) lines 443-477 [crates/gcore/src/graph_analytics/leiden.rs:443-477]
  - Signature: `fn assert_communities_connected(n: usize, edges: &[(usize, usize, f64)], membership: &[usize]) {`
  - Purpose: Per community label present in 'membership', this function builds the induced undirected subgraph from non-self-loop edges whose endpoints share that label, then depth-first searches each nontrivial community and asserts that all of its members are reachable from an arbitrary member, panicking if any community is internally disconnected. [crates/gcore/src/graph_analytics/leiden.rs:443-477]
- `detect` (function) component `detect [function]` (`7905ccbd-d341-593c-a127-451a77d48598`) lines 479-482 [crates/gcore/src/graph_analytics/leiden.rs:479-482]
  - Signature: `fn detect(n: usize, edges: &[(usize, usize, f64)]) -> Vec<usize> {`
  - Purpose: Constructs a 'LeidenGraph' from 'n' nodes and the weighted edge list, then returns the community assignments produced by 'detect_communities' using 'DEFAULT_GAMMA'. [crates/gcore/src/graph_analytics/leiden.rs:479-482]
- `community_count` (function) component `community_count [function]` (`3c96c976-85dc-5748-89cf-bcbd5ac3c002`) lines 484-486 [crates/gcore/src/graph_analytics/leiden.rs:484-486]
  - Signature: `fn community_count(membership: &[usize]) -> usize {`
  - Purpose: Returns the number of communities implied by the 'membership' slice by taking the maximum community ID present and adding 1, or '0' if the slice is empty. [crates/gcore/src/graph_analytics/leiden.rs:484-486]
- `triangle` (function) component `triangle [function]` (`934c4817-4219-5e6a-8b98-de861315c1c7`) lines 488-494 [crates/gcore/src/graph_analytics/leiden.rs:488-494]
  - Signature: `fn triangle(base: usize) -> Vec<(usize, usize, f64)> {`
  - Purpose: Returns a three-edge triangle as a 'Vec' of '(usize, usize, f64)' tuples connecting 'base -> base + 1 -> base + 2 -> base', each with weight '1.0'. [crates/gcore/src/graph_analytics/leiden.rs:488-494]
- `clique` (function) component `clique [function]` (`a6bce990-bca1-5c57-834b-1d34fa579e66`) lines 496-504 [crates/gcore/src/graph_analytics/leiden.rs:496-504]
  - Signature: `fn clique(base: usize, size: usize, weight: f64) -> Vec<(usize, usize, f64)> {`
  - Purpose: Returns a vector of weighted undirected edges forming a complete graph on 'size' vertices labeled 'base..base+size-1', with each pair '(i, j)' for 'i < j' assigned the given 'weight'. [crates/gcore/src/graph_analytics/leiden.rs:496-504]
- `modularity` (function) component `modularity [function]` (`b27da28d-3b74-59d6-8b19-af94d7f78a34`) lines 511-531 [crates/gcore/src/graph_analytics/leiden.rs:511-531]
  - Signature: `fn modularity(g: &LeidenGraph, membership: &[usize], gamma: f64) -> f64 {`
  - Purpose: Computes the modularity score of a community partition as the normalized fraction of intra-community edge weights minus a resolution-scaled null model term based on node strength distributions. [crates/gcore/src/graph_analytics/leiden.rs:511-531]
- `karate_club` (function) component `karate_club [function]` (`2fab2cc4-53d1-5076-b9f7-288dc29122a7`) lines 536-570 [crates/gcore/src/graph_analytics/leiden.rs:536-570]
  - Signature: `fn karate_club() -> Vec<(usize, usize, f64)> {`
  - Purpose: Returns the canonical Karate Club social network graph as a vector of undirected edges represented as tuples of (source node, destination node, uniform weight 1.0). [crates/gcore/src/graph_analytics/leiden.rs:536-570]
- `assert_no_improving_single_move` (function) component `assert_no_improving_single_move [function]` (`ac0269bb-7340-5c54-9781-a4cc7753027e`) lines 577-595 [crates/gcore/src/graph_analytics/leiden.rs:577-595]
  - Signature: `fn assert_no_improving_single_move(g: &LeidenGraph, membership: &[usize], gamma: f64) {`
  - Purpose: Validates that the community membership assignment is a local optimum of modularity by asserting that moving any single node to any alternative existing or new community does not increase modularity beyond a numerical tolerance threshold (1e-9). [crates/gcore/src/graph_analytics/leiden.rs:577-595]
- `two_triangles_with_bridge_split` (function) component `two_triangles_with_bridge_split [function]` (`d816f36f-3c38-58cd-9f06-8d267c842951`) lines 598-610 [crates/gcore/src/graph_analytics/leiden.rs:598-610]
  - Signature: `fn two_triangles_with_bridge_split() {`
  - Purpose: This function validates that a community detection algorithm correctly partitions a graph of two complete triangles connected by a single bridge edge into exactly two distinct communities with correct node membership assignments. [crates/gcore/src/graph_analytics/leiden.rs:598-610]
- `two_cliques_recover_planted_partition` (function) component `two_cliques_recover_planted_partition [function]` (`200af774-19be-56fd-8aa9-3a17f1b3f1bb`) lines 613-628 [crates/gcore/src/graph_analytics/leiden.rs:613-628]
  - Signature: `fn two_cliques_recover_planted_partition() {`
  - Purpose: **Validates that a community detection algorithm correctly recovers a two-clique planted partition model with 10 nodes partitioned into two complete subgraphs connected by two inter-clique edges.** [crates/gcore/src/graph_analytics/leiden.rs:613-628]
- `no_edge_multi_node_graph_is_all_singletons` (function) component `no_edge_multi_node_graph_is_all_singletons [function]` (`d7228d7e-0019-53b4-99dd-028f7fe3da64`) lines 631-634 [crates/gcore/src/graph_analytics/leiden.rs:631-634]
  - Signature: `fn no_edge_multi_node_graph_is_all_singletons() {`
  - Purpose: **This test verifies that a graph connectivity detection algorithm assigns 3 isolated nodes to 3 distinct singleton components with component identifiers [0, 1, 2].** [crates/gcore/src/graph_analytics/leiden.rs:631-634]
- `empty_graph_returns_empty` (function) component `empty_graph_returns_empty [function]` (`0616e115-9e4a-5b18-8a41-c7f7b55ee2d3`) lines 637-639 [crates/gcore/src/graph_analytics/leiden.rs:637-639]
  - Signature: `fn empty_graph_returns_empty() {`
  - Purpose: This test asserts that the 'detect' function returns an empty 'Vec<usize>' when invoked with a parameter of '0' and an empty graph (empty slice). [crates/gcore/src/graph_analytics/leiden.rs:637-639]
- `single_node_returns_one_community` (function) component `single_node_returns_one_community [function]` (`a6114e85-5b9f-597f-b0d4-5d3ef34b0533`) lines 642-644 [crates/gcore/src/graph_analytics/leiden.rs:642-644]
  - Signature: `fn single_node_returns_one_community() {`
  - Purpose: Test asserting that the 'detect' function returns a single-element vector '[0]' when invoked with 1 node and an empty edge set. [crates/gcore/src/graph_analytics/leiden.rs:642-644]
- `triangle_with_isolated_node_yields_two_communities` (function) component `triangle_with_isolated_node_yields_two_communities [function]` (`785d4f2f-645d-51c9-8d70-450b92137e53`) lines 647-654 [crates/gcore/src/graph_analytics/leiden.rs:647-654]
  - Signature: `fn triangle_with_isolated_node_yields_two_communities() {`
  - Purpose: Validates that a community detection algorithm partitions a 4-node graph containing a complete triangle subgraph and an isolated vertex into exactly two distinct communities. [crates/gcore/src/graph_analytics/leiden.rs:647-654]
- `four_node_path_is_not_all_singletons` (function) component `four_node_path_is_not_all_singletons [function]` (`54b8068d-72a1-512f-af6d-8e19373284aa`) lines 657-666 [crates/gcore/src/graph_analytics/leiden.rs:657-666]
  - Signature: `fn four_node_path_is_not_all_singletons() {`
  - Purpose: This test function verifies that a community detection algorithm on a 4-node linear path graph produces fewer than 4 communities (i.e., merges at least some nodes) while maintaining connectivity among the detected communities. [crates/gcore/src/graph_analytics/leiden.rs:657-666]
- `duplicate_and_reciprocal_edges_fold_by_summation` (function) component `duplicate_and_reciprocal_edges_fold_by_summation [function]` (`658a288a-b7aa-5c96-aa07-de491b140bd7`) lines 669-676 [crates/gcore/src/graph_analytics/leiden.rs:669-676]
  - Signature: `fn duplicate_and_reciprocal_edges_fold_by_summation() {`
  - Purpose: This function verifies that a 'LeidenGraph' correctly folds reciprocal directed edges (0→1 and 1→0) into undirected edges by summing their weights and maintains consistent adjacency, strength, and total weight values. [crates/gcore/src/graph_analytics/leiden.rs:669-676]
- `self_loop_contributes_double_strength_single_weight` (function) component `self_loop_contributes_double_strength_single_weight [function]` (`ddffa4a5-5ab0-55d0-993d-ea15e3378265`) lines 679-687 [crates/gcore/src/graph_analytics/leiden.rs:679-687]
  - Signature: `fn self_loop_contributes_double_strength_single_weight() {`
  - Purpose: This test function verifies that in LeidenGraph, self-loop edges contribute twice their weight to node strength but only once their weight to total graph weight. [crates/gcore/src/graph_analytics/leiden.rs:679-687]
- `aggregation_preserves_strength_invariant_and_total_weight` (function) component `aggregation_preserves_strength_invariant_and_total_weight [function]` (`7f48bedc-dd6c-5654-9099-9998037e18f9`) lines 690-704 [crates/gcore/src/graph_analytics/leiden.rs:690-704]
  - Signature: `fn aggregation_preserves_strength_invariant_and_total_weight() {`
  - Purpose: # Summary This function verifies that aggregating a graph following community detection (via partition refinement) preserves the strength invariant and conserves total edge weight. [crates/gcore/src/graph_analytics/leiden.rs:690-704]
- `multi_level_back_projection_maps_original_nodes` (function) component `multi_level_back_projection_maps_original_nodes [function]` (`f7164a8a-c560-54fc-aaed-e554d7b38fe2`) lines 707-726 [crates/gcore/src/graph_analytics/leiden.rs:707-726]
  - Signature: `fn multi_level_back_projection_maps_original_nodes() {`
  - Purpose: This function validates that a multilevel community detection algorithm with hierarchical back-projection correctly identifies four distinct communities when applied to a graph of weakly-chained triangular clusters. [crates/gcore/src/graph_analytics/leiden.rs:707-726]
- `output_is_deterministic_across_repeats` (function) component `output_is_deterministic_across_repeats [function]` (`a0cb0d70-b7a5-5d0d-93c8-0580a8ee1673`) lines 729-737 [crates/gcore/src/graph_analytics/leiden.rs:729-737]
  - Signature: `fn output_is_deterministic_across_repeats() {`
  - Purpose: This function verifies that the 'detect' algorithm is deterministic by asserting that 10 repeated invocations with an identical graph input (two cliques connected by a bridge edge) produce outputs identical to the initial invocation. [crates/gcore/src/graph_analytics/leiden.rs:729-737]
- `output_is_invariant_to_edge_list_order` (function) component `output_is_invariant_to_edge_list_order [function]` (`95235403-b02d-5a67-a3a2-cad45699f713`) lines 740-752 [crates/gcore/src/graph_analytics/leiden.rs:740-752]
  - Signature: `fn output_is_invariant_to_edge_list_order() {`
  - Purpose: This test verifies that the graph community detection algorithm produces identical output regardless of input edge list ordering by asserting equivalence between detection results on original and reversed edge lists. [crates/gcore/src/graph_analytics/leiden.rs:740-752]
- `weighting_pulls_a_node_toward_the_heavier_community` (function) component `weighting_pulls_a_node_toward_the_heavier_community [function]` (`61001f47-e176-536a-a16e-7ea1abdd711f`) lines 755-764 [crates/gcore/src/graph_analytics/leiden.rs:755-764]
  - Signature: `fn weighting_pulls_a_node_toward_the_heavier_community() {`
  - Purpose: This test verifies that a community detection algorithm assigns a node to the community corresponding to its highest-weighted edge when the node bridges multiple communities. [crates/gcore/src/graph_analytics/leiden.rs:755-764]
- `local_moving_isolates_over_merged_self_loop_cluster` (function) component `local_moving_isolates_over_merged_self_loop_cluster [function]` (`3b7c21d5-e08d-520f-b749-9d3ae3b27d0b`) lines 767-784 [crates/gcore/src/graph_analytics/leiden.rs:767-784]
  - Signature: `fn local_moving_isolates_over_merged_self_loop_cluster() {`
  - Purpose: This test validates that the 'local_moving' greedy modularity optimization algorithm successfully isolates two nodes with strong self-loops from a single over-merged community by moving them to distinct communities when a fresh empty candidate community is available to enable modularity gains. [crates/gcore/src/graph_analytics/leiden.rs:767-784]
- `zachary_karate_club_finds_modular_structure` (function) component `zachary_karate_club_finds_modular_structure [function]` (`61113965-d0f0-5af3-8a18-56325eef6861`) lines 787-806 [crates/gcore/src/graph_analytics/leiden.rs:787-806]
  - Signature: `fn zachary_karate_club_finds_modular_structure() {`
  - Purpose: Validates that the Leiden community detection algorithm achieves modularity Q ∈ [0.40, 0.42+ε] on Zachary's karate club network (34 nodes), producing 2-5 connected communities with deterministic reproducibility. [crates/gcore/src/graph_analytics/leiden.rs:787-806]
- `local_moving_partition_has_no_improving_single_node_move` (function) component `local_moving_partition_has_no_improving_single_node_move [function]` (`ce1a46e9-bec0-5a2b-8fd9-22ff4c3ce0cf`) lines 809-845 [crates/gcore/src/graph_analytics/leiden.rs:809-845]
  - Signature: `fn local_moving_partition_has_no_improving_single_node_move() {`
  - Purpose: This test function verifies that the 'local_moving' algorithm converges to a strict single-node local optimum by asserting that no node in the resulting partition can improve modularity through relocation to a different community. [crates/gcore/src/graph_analytics/leiden.rs:809-845]

