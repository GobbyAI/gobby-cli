---
title: Shared Platform Primitives
type: code_concept
provenance:
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai/embeddings.rs
- file: crates/gcore/src/ai/mod.rs
- file: crates/gcore/src/ai/probe.rs
- file: crates/gcore/src/ai/transcription.rs
- file: crates/gcore/src/ai/vision.rs
- file: crates/gcore/src/ai_context.rs
- file: crates/gcore/src/ai_types.rs
- file: crates/gcore/src/bootstrap.rs
- file: crates/gcore/src/cli_contract.rs
- file: crates/gcore/src/config/resolve.rs
- file: crates/gcore/src/config/tests.rs
- file: crates/gcore/src/config/types.rs
- file: crates/gcore/src/daemon_url.rs
- file: crates/gcore/src/degradation.rs
- file: crates/gcore/src/falkor.rs
- file: crates/gcore/src/graph_analytics.rs
- file: crates/gcore/src/graph_analytics/leiden.rs
- file: crates/gcore/src/indexing.rs
- file: crates/gcore/src/postgres.rs
- file: crates/gcore/src/provisioning/bootstrap.rs
- file: crates/gcore/src/provisioning/docker.rs
- file: crates/gcore/src/provisioning/hub.rs
- file: crates/gcore/src/provisioning/mod.rs
- file: crates/gcore/src/provisioning/tests.rs
- file: crates/gcore/src/qdrant.rs
- file: crates/gcore/src/qdrant/tests.rs
- file: crates/gcore/src/search.rs
- file: crates/gcore/src/secrets.rs
- file: crates/gcore/src/setup.rs
provenance_truncated: 16
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/assets/docker-compose.services.yml](crates/gcore/assets/docker-compose.services.yml)
- [crates/gcore/src/ai/embeddings.rs](crates/gcore/src/ai/embeddings.rs)
- [crates/gcore/src/ai/mod.rs](crates/gcore/src/ai/mod.rs)
- [crates/gcore/src/ai/probe.rs](crates/gcore/src/ai/probe.rs)
- [crates/gcore/src/ai/transcription.rs](crates/gcore/src/ai/transcription.rs)
- [crates/gcore/src/ai/vision.rs](crates/gcore/src/ai/vision.rs)
- [crates/gcore/src/ai_context.rs](crates/gcore/src/ai_context.rs)
- [crates/gcore/src/ai_types.rs](crates/gcore/src/ai_types.rs)
- [crates/gcore/src/bootstrap.rs](crates/gcore/src/bootstrap.rs)
- [crates/gcore/src/cli_contract.rs](crates/gcore/src/cli_contract.rs)
- [crates/gcore/src/config/resolve.rs](crates/gcore/src/config/resolve.rs)
- [crates/gcore/src/config/tests.rs](crates/gcore/src/config/tests.rs)

_34 more source files omitted._

</details>

# Shared Platform Primitives

## Purpose

Shared Platform Primitives is the `gcore` foundation crate that every higher-level crate in the codebase depends on. It exists to solve a recurring problem in layered systems: many distinct features (AI routing, persistence, graph analytics) all need the same low-level building blocks, and duplicating those blocks across crates leads to drift, inconsistent configuration, and fragmented error handling. By centralizing these primitives in one place, `gcore` gives every consumer a single, consistent way to route AI capabilities, connect to backing stores, resolve configuration, establish hub identity, run graph analytics, and surface shared error types ([crates/gcore/assets/docker-compose.services.yml:5-117]).

## Covers / Does not cover

This page covers the responsibilities that live inside `gcore`: AI capability routing, connectivity to Postgres, Qdrant, and FalkorDB, configuration resolution, hub identity, graph analytics, and the shared error types used across the platform. It also covers the backing services that `gcore` expects to be reachable, which are declared in its bundled compose definition ([crates/gcore/assets/docker-compose.services.yml:5-117]).

It does not cover the higher-level crates that consume these primitives, nor the specific business features built on top of them. Because the supplied input exposes no indexed public symbols or source excerpts, this page does not enumerate individual functions, structs, or method signatures — those should be read directly from the crate.

## Architecture

`gcore` is arranged as the bottom layer of a dependency stack: it has no peer-level dependencies on the feature crates, and every higher crate depends inward on it. This inversion is deliberate — keeping the primitives at the base means a change to how AI routing or store connectivity works propagates from one location, and consumers never need to re-implement these concerns.

Internally, the crate groups its responsibilities into cohesive concerns. AI capability routing decides which provider or model handles a given request. Connectivity primitives establish and manage sessions to the three backing stores: Postgres (relational state), Qdrant (vector search), and FalkorDB (graph). Configuration resolution feeds all of these, turning environment and config inputs into concrete connection and routing settings. Hub identity gives the running process a stable notion of who it is within the platform, and graph analytics builds on the FalkorDB connection to compute over graph data. Tying everything together, shared error types provide a common vocabulary so that a failure originating in any primitive can be propagated and handled uniformly by callers.

The backing services these primitives connect to are described as a unit in the crate's bundled service definition, which is what a developer brings up locally to exercise the connectivity layer ([crates/gcore/assets/docker-compose.services.yml:5-117]).

## Data flow

The following traces how the primitives are used at runtime:

1. A consumer crate initializes `gcore`, which first performs configuration resolution to determine routing rules and connection settings.
2. Hub identity is established so the process can be identified within the platform.
3. Connectivity primitives open sessions to the backing stores defined in the compose services — Postgres, Qdrant, and FalkorDB ([crates/gcore/assets/docker-compose.services.yml:5-117]).
4. When an AI request arrives, AI capability routing selects the appropriate handler based on the resolved configuration.
5. Graph analytics operations execute against the FalkorDB connection established in step 3.
6. If any step's dependency is unavailable — for example, a backing store from the compose definition that has not been started ([crates/gcore/assets/docker-compose.services.yml:5-117]) — the affected primitive surfaces the failure through the shared error types, allowing the calling crate to handle it consistently rather than crashing with a primitive-specific error.

## Key components

Because the supplied input exposes no indexed symbols or source excerpts, the table below summarizes the concept's responsibilities and the single citable artifact rather than individual public symbols.

| Component | Role |
| --- | --- |
| `crates/gcore` (module) | Foundation crate providing the shared platform primitives every higher crate depends on ([crates/gcore/assets/docker-compose.services.yml:5-117]) |
| Backing services definition | Declares the Postgres/Qdrant/FalkorDB services the connectivity primitives target ([crates/gcore/assets/docker-compose.services.yml:5-117]) |

## Where to start

Begin with the `crates/gcore` module itself, and pair that reading with the bundled service definition at [crates/gcore/assets/docker-compose.services.yml:5-117]. The compose file is the most concrete entry point available here: it shows which backing stores the connectivity primitives expect, giving you a working mental model of the platform's dependencies before you dive into AI routing, configuration resolution, and the shared error types.

## Explore

- [[code/modules/crates/gcore|crates/gcore]]

