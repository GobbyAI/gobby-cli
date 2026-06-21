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

## Module: `crates`

The `crates` directory is the Rust workspace root that organises the system's first-party binaries and libraries into four distinct crates. Each crate owns a vertical slice of functionality — code intelligence, shared platform primitives, AI-agent hook integration, and knowledge-wiki management — while sharing a common configuration, identity, and AI-routing layer defined in `crates/gcore`. The workspace boundary enforces that no crate may reach across sibling boundaries except through explicit Cargo dependency declarations, keeping domain concerns cleanly separated.

| Child crate | Primary responsibility |
|---|---|
| `crates/gcode` | Code-graph indexing, AST parsing, symbol resolution, graph read/write, CLI surface for code intelligence |
| `crates/gcore` | Shared platform primitives: project identity, service config, PostgreSQL/FalkorDB/Qdrant connectivity, AI context, embedding backend, Gobby-core integration |
| `crates/ghook` | AI-agent hook dispatcher; intercepts session-start/tool-use events from Claude, Codex, Grok, Droid, Gemini, Qwen and routes envelopes to the daemon |
| `crates/gwiki` | Knowledge-wiki engine: ingest, search, compile, audit, health, vector sync, graph analytics, Obsidian vault management |

The component table exposed by the workspace spans the full public symbol surface of all four crates. Shared CLI primitives — `global_flags`, `scope`, `flags`, `positionals`, `json_output_keys`, `daemon_consumed`, and `error_codes` — appear in nearly every command, reflecting a contract-driven CLI design enforced by `BinaryContract`, `CliContract`, `CommandContract`, and `FlagContract` types. Argument-parsing adaptors such as `AiRouteArg`, `AiDepthArg`, `AiProseDepthArg`, and `AiRegisterArg` sit at the boundary between the raw CLI layer and the `AiContext`/`AiBindings` resolution pipeline that lives in `gcore`.

Key runtime flows cross crate boundaries in predictable ways. A `gcode` command (e.g., `graph sync-file`) resolves its `Context` and `ProjectIdentity` through `gcore`, opens a `CodeGraph` via a FalkorDB `GraphClient`, and writes `GraphNode`/`GraphLink` projections before notifying the daemon. A `gwiki` command (e.g., `search` or `ask`) resolves a `WikiScope` and `ResolvedScope` from `gcore`'s config stack, dispatches to BM25 (`Bm25SearchBackend`), vector (`SemanticSearchBackend`, `GobbyQdrantBackend`), and graph-boost (`FalkorGraphBoostBackend`) backends, then fuses results through `rrf_merge`. Hook events processed by `ghook` call into a lightweight daemon HTTP client (`DaemonEndpoint`, `post_and_cleanup`) and write envelopes to a scoped inbox directory; they share no Rust types with `gcode` or `gwiki` at runtime, communicating only through the file-system inbox and the daemon REST API. Embedding generation threads through `gcore`'s `EmbeddingBackend`, which multiplexes between a direct OpenAI-compatible HTTP route and a daemon-proxied route depending on `AiRouting` and `CapabilityStatusRoute` probe results.

The component table also exposes a large set of dependency library properties (`ecto`, `phoenix`, `plug`, `oban`, `broadway`, `httpoison`, `jason`, `req`, `finch`, `rspec`, `faraday`, `nokogiri`, etc.) that represent the Elixir/Ruby service layer and test tooling referenced by the wider system outside the Rust workspace. Within the workspace itself the collaboration points are: `gcore` is consumed by both `gcode` and `gwiki` as a library; `ghook` is a standalone binary with minimal shared code; and `gwiki` re-exports `gcore` connectivity primitives (`PostgresWikiStore`, `GwikiStandaloneSetup`, `WikiVectorChunk`) rather than duplicating them.
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
[crates/gcode/src/graph/code_graph/read.rs:1-25]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode\|crates/gcode]] | ## crates/gcode |
| [[code/modules/crates/gcore\|crates/gcore]] | ## Module: crates/gcore |
| [[code/modules/crates/ghook\|crates/ghook]] | ## crates/ghook |
| [[code/modules/crates/gwiki\|crates/gwiki]] | ## Module: `crates/gwiki` |

