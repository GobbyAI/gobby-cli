---
title: Infrastructure Stack
type: code_infrastructure
provenance: []
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# Infrastructure Stack

This page is derived deterministically from the workspace's Cargo manifests and service boundaries — no LLM. Each section names a service the workspace can reach, what pulls it in, the adapter module that talks to it, and how the workspace behaves when it is unavailable.

## Document toolchain (PDF/Office)

The document toolchain (PDF text/page extraction plus spreadsheet parsing) lets `gwiki` ingest documents into the Markdown vault. It is gated behind the `documents` Cargo feature.

**Pulled in by:** gobby-wiki (feature: documents)

**Code path:** `crates/gwiki/src/ingest/pdf/ingest.rs:23`

**When unavailable:** When the `documents` feature is off or extraction fails, the ingest path falls back to a skeleton/derived Markdown document carrying an explicit degradation marker.

## Embedding API

An OpenAI-compatible embedding API turns text into vectors for semantic search and ingest. The `ai` adapter feature calls it directly (standalone routing) using the resolved runtime config.

**Pulled in by:** gobby-code (feature: ai), gobby-wiki (feature: ai)

**Code path:** `crates/gcore/src/ai/embeddings.rs:19`

**When unavailable:** When the embedding API is routed off or unreachable, semantic search returns `[]` and embedding-dependent ingest degrades to derived output with explicit degradation markers.

## FalkorDB graph

FalkorDB holds the code/relationship graph projection. The `falkor` adapter feature opens a read-only graph client used for graph queries and the search graph-relevance boost.

**Pulled in by:** gobby-code (feature: falkor), gobby-wiki (feature: falkor)

**Code path:** `crates/gcore/src/falkor.rs:28`

**When unavailable:** When FalkorDB is down, graph commands return `[]` and the graph boost is simply omitted from search ranking; BM25 and semantic results are unaffected.

## Gobby daemon

The Gobby daemon is the optional routing target for AI work (generation, embedding, transcription, vision). The `ai` adapter routes requests through it when daemon routing is selected; the daemon URL is resolved by always-compiled `gobby_core::daemon_url`.

**Pulled in by:** gobby-code (feature: ai), gobby-wiki (feature: ai), workspace (gobby_core::daemon_url, always)

**Code path:** `crates/gcore/src/ai/daemon.rs:10`

**When unavailable:** When the daemon is unreachable, AI capabilities fall back to direct transport or are reported off, and ingest/generation degrade to skeleton/derived output with explicit degradation markers.

## Media toolchain (ffmpeg)

The media toolchain shells out to ffmpeg (a system binary on `PATH`) to probe duration and extract audio/frames so `gwiki` can transcribe and analyze audio/video sources.

**Pulled in by:** gobby-wiki (src/media.rs, ffmpeg via PATH)

**Code path:** `crates/gwiki/src/media.rs:13`

**When unavailable:** When ffmpeg is not on `PATH`, media ingest degrades (detected via `error.rs::is_ffmpeg_unavailable`) to derived output with explicit degradation markers instead of failing the run.

## PostgreSQL hub

The Gobby PostgreSQL hub stores indexed symbols, content chunks, and config. The CLIs connect read-only or read-write through the `postgres` adapter feature and run pg_search BM25 queries against the hub.

**Pulled in by:** gobby-code (feature: postgres), gobby-wiki (feature: postgres)

**Code path:** `crates/gcore/src/postgres.rs:16`

**When unavailable:** BM25 search works whenever the PostgreSQL hub is configured and indexed; with no hub configured the index-backed commands have nothing to read.

## Qdrant vectors

Qdrant stores per-project vector collections (e.g. `code_symbols_{project_id}`). The `qdrant` adapter feature upserts and searches those vectors to power semantic retrieval.

**Pulled in by:** gobby-code (feature: qdrant), gobby-wiki (feature: qdrant)

**Code path:** `crates/gcore/src/qdrant.rs:20`

**When unavailable:** When Qdrant (or the embedding API) is unavailable, semantic search returns `[]` and results fall back to BM25 plus any available graph boost.

## ghook inbox

`ghook` always enqueues each hook envelope to `~/.gobby/hooks/inbox/` before attempting a best-effort daemon POST, so hooks are durable even when the daemon is down (enqueue-first transport).

**Pulled in by:** gobby-hooks (always)

**Code path:** `crates/ghook/src/transport.rs:31`

**When unavailable:** When the daemon POST fails, the enqueued envelope still lands in the inbox for later delivery; the observable per-CLI hook contract (stdout/stderr/exit code) is preserved.

## tree-sitter grammars

tree-sitter grammars drive AST-aware symbol extraction during indexing. The `gcode` indexer maps file extensions to grammars and walks each parse tree to extract symbols.

**Pulled in by:** gobby-code (deps: tree-sitter + 21 grammars)

**Code path:** `crates/gcode/src/index/languages.rs:9`

**When unavailable:** A file in a language with no registered grammar is indexed as content-only repo text (BM25/semantic) rather than producing AST symbols; indexing never fails on an unknown language.

