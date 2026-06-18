---
title: crates/gwiki/src/search/graph_boost.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/graph_boost.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/graph_boost.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/search/graph_boost.rs` exposes 35 indexed API symbols.

## How it fits

`crates/gwiki/src/search/graph_boost.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphBoostConfig` | class | Indexed class `GraphBoostConfig` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:21-24] |
| `GraphBoostConfig::default` | method | Indexed method `GraphBoostConfig::default` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:27-32] |
| `GraphBoostRequest` | class | Indexed class `GraphBoostRequest` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:35-39] |
| `GraphBoostOutcome` | class | Indexed class `GraphBoostOutcome` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:41-44] |
| `GraphBoostBackend` | type | Indexed type `GraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:46-51] |
| `NoopGraphBoostBackend` | class | Indexed class `NoopGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:54] |
| `NoopGraphBoostBackend::search_graph_boost` | method | Indexed method `NoopGraphBoostBackend::search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:57-65] |
| `UnavailableGraphBoostBackend` | class | Indexed class `UnavailableGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:68-70] |
| `UnavailableGraphBoostBackend::unreachable` | method | Indexed method `UnavailableGraphBoostBackend::unreachable` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:73-77] |
| `UnavailableGraphBoostBackend::search_graph_boost` | method | Indexed method `UnavailableGraphBoostBackend::search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:81-89] |
| `search_graph_boost` | function | Indexed function `search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:93-98] |
| `MemoryGraphBoostBackend` | class | Indexed class `MemoryGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:101-103] |
| `MemoryGraphBoostBackend::new` | method | Indexed method `MemoryGraphBoostBackend::new` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:106-108] |
| `MemoryGraphBoostBackend::search_graph_boost` | method | Indexed method `MemoryGraphBoostBackend::search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:112-123] |
| `FalkorGraphBoostBackend` | class | Indexed class `FalkorGraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:126-129] |
| `FalkorGraphBoostBackend::new` | method | Indexed method `FalkorGraphBoostBackend::new` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:132-134] |
| `FalkorGraphBoostBackend::new_with_config` | method | Indexed method `FalkorGraphBoostBackend::new_with_config` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:136-145] |
| `FalkorGraphBoostBackend::search_graph_boost` | method | Indexed method `FalkorGraphBoostBackend::search_graph_boost` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:149-184] |
| `GraphBoostDocument` | class | Indexed class `GraphBoostDocument` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:188-191] |
| `GraphBoostLink` | class | Indexed class `GraphBoostLink` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:194-197] |
| `rank_link_neighborhood` | function | Indexed function `rank_link_neighborhood` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:199-264] |
| `graph_boost_hits` | function | Indexed function `graph_boost_hits` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:266-277] |
| `graph_result` | function | Indexed function `graph_result` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:279-301] |
| `graph_degradation` | function | Indexed function `graph_degradation` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:303-308] |
| `resolve_graph_target` | function | Indexed function `resolve_graph_target` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:310-347] |
| `normalize_path` | function | Indexed function `normalize_path` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:349-362] |
| `slug_target_map` | function | Indexed function `slug_target_map` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:364-384] |
| `is_external_target` | function | Indexed function `is_external_target` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:386-392] |
| `rank_link_neighborhood_boosts_outbound_and_backlinks` | function | Indexed function `rank_link_neighborhood_boosts_outbound_and_backlinks` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:399-427] |
| `rank_link_neighborhood_filters_non_searchable_before_truncating` | function | Indexed function `rank_link_neighborhood_filters_non_searchable_before_truncating` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:430-452] |
| `rank_link_neighborhood_resolves_targets_relative_to_source` | function | Indexed function `rank_link_neighborhood_resolves_targets_relative_to_source` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:455-473] |
| `graph_boost_hits_marks_graph_source` | function | Indexed function `graph_boost_hits_marks_graph_source` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:476-489] |
| `unavailable_graph_backend_reports_service_degradation` | function | Indexed function `unavailable_graph_backend_reports_service_degradation` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:492-512] |
| `document` | function | Indexed function `document` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:514-519] |
| `link` | function | Indexed function `link` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:521-526] |

