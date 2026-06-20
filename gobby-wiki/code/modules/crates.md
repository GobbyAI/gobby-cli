---
title: crates
type: code_module
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai_context.rs
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
- file: crates/gwiki/contract/gwiki.contract.json
- file: crates/gwiki/src/ai/chunk.rs
- file: crates/gwiki/src/benchmark.rs
- file: crates/gwiki/src/collect.rs
- file: crates/gwiki/src/commands/citation_quality.rs
- file: crates/gwiki/src/commands/sources.rs
- file: crates/gwiki/src/graph/mod.rs
- file: crates/gwiki/src/health.rs
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/ingest/session.rs
- file: crates/gwiki/src/links.rs
- file: crates/gwiki/src/main.rs
- file: crates/gwiki/src/search/semantic.rs
- file: crates/gwiki/src/vector.rs
provenance_truncated: 442
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates

Parent: [[code/repo|Repository Overview]]

## Overview

# crates

The `crates` module is the Rust workspace root for Gobby. It owns no source files of its own; instead it aggregates four sibling crates that together provide code indexing, a shared service/AI core, host-agent hook integration, and a local-first wiki. The shared core (`gcore`) supplies the common substrate — configuration resolution, storage clients (FalkorDB, Qdrant, PostgreSQL), embeddings, indexing/search primitives, graph analytics, and setup/degradation contracts — while the three feature crates (`gcode`, `ghook`, `gwiki`) build user-facing surfaces on top of it (`crates/gcore/src/config/mod.rs:1-17`, `crates/gcore/src/config/types.rs:1-30`).

| Crate | Role | Key anchor |
| --- | --- | --- |
| `gcore` | Shared core: AI routing/result types, config resolution, storage clients, indexing/search/graph primitives, setup & degradation contracts, local service provisioning | `crates/gcore/src/config/mod.rs:1-17` |
| `gcode` | Fast code-index CLI for Gobby; Clap parsing, command dispatch, project/service context resolution, PostgreSQL hub access, search/graph/vector/setup/docs flows | `crates/gcode/src/commands/search.rs:1-13` |
| `gwiki` | Local-first wiki CLI for capture, search, upkeep, and synthesis | `crates/gwiki/contract/gwiki.contract.json:2-4` |
| `ghook` | Host-agent hook integration: builds and persists hook envelopes, attempts daemon delivery | `crates/ghook/src/transport.rs:1-18` |

The two CLI crates each pair a static, versioned invocation contract with an application crate that implements it. `gcode` exposes contract version 2 — a “Fast code index CLI for Gobby” — centralizing global flags, scope handling, command metadata, JSON output keys, and error-code metadata as a stable surface (`crates/gcode/contract/gcode.contract.json:1-4`, `crates/gcode/contract/gcode.contract.json:5-94`). `gwiki` follows the same pattern, declaring its identity, contract version, global flags, scope selection, commands, JSON output shapes, and error codes in its contract document (`crates/gwiki/contract/gwiki.contract.json:2-4`). These contracts let the runtime surfaces be validated against a published shape while keeping consumer-owned choices (such as graph and collection names) outside the shared config layer (`crates/gcore/src/config/types.rs:1-30`).

`ghook` is the hook-side integration layer that connects external host agents into the Gobby system. Its runtime child receives hook invocations, builds a durable inbox envelope, persists it locally, and then attempts daemon delivery, while its schema child defines the JSON contracts for both diagnostics output and inbox envelopes (`crates/ghook/src/transport.rs:1-18`, `crates/ghook/schemas/diagnose-output.v2.schema.json:1`, `crates/ghook/schemas/inbox-envelope.v1.schema.json:1`). Collaboration across the workspace flows through `gcore`: the feature crates resolve configuration and service bindings, reach PostgreSQL/FalkorDB/Qdrant, and apply setup and degradation contracts via the shared core, so that capability gaps degrade gracefully rather than fail outright (`crates/gcore/src/config/mod.rs:1-17`).

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode\|crates/gcode]] | `crates/gcode` is the code-indexing CLI module for Gobby. Its contract submodule defines the stable invocation surface as contract version 2, described as a “Fast code index CLI for Gobby,” and centralizes global flags, scope handling, command metadata, JSON output keys, and error-code metadata (crates/gcode/contract/gcode.contract.json:1-4, crates/gcode/contract/gcode.contract.json:5-94). The `src` submodule implements the binary/library surface: Clap parsing, command dispatch, project and service context resolution, PostgreSQL hub access, and shared model types for search, graph, vector,… |
| [[code/modules/crates/gcore\|crates/gcore]] | `crates/gcore` is Gobby’s shared core layer: it centralizes AI routing and result types, configuration resolution, storage clients, indexing/search primitives, graph analytics, setup/degradation contracts, and local service provisioning. Its `src` child keeps service configuration behind a lightweight shared surface, covering FalkorDB, Qdrant, embeddings, indexing, AI routing, capability bindings, tuning, and feature candidates, while leaving consumer-owned choices such as graph and collection names outside the shared config layer (`crates/gcore/src/config/mod.rs:1-17`,… |
| [[code/modules/crates/ghook\|crates/ghook]] | `crates/ghook` is Gobby’s hook-side integration layer. Its runtime child module receives host-agent hook invocations, builds a hook envelope, persists it locally, and then attempts daemon delivery; its schema child module defines the JSON contracts for both diagnostics and durable inbox envelopes (crates/ghook/src/transport.rs:1-18) (crates/ghook/schemas/diagnose-output.v2.schema.json:1) (crates/ghook/schemas/inbox-envelope.v1.schema.json:1). |
| [[code/modules/crates/gwiki\|crates/gwiki]] | `crates/gwiki` is the top-level gwiki module, combining a static CLI contract with the application crate that implements it. The contract defines gwiki’s identity as a local-first wiki CLI for capture, search, upkeep, and synthesis, along with contract version, global flags, scope selection, commands, JSON output shapes, and error codes (`crates/gwiki/contract/gwiki.contract.json:2-4`). |

