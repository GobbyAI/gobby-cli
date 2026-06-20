---
title: Workspace Map
type: code_concept
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
verify_notes:
- id: 2
  reason: Claims crate split and boundary without any source evidence.
- id: 3
  reason: Asserts shared-core responsibilities and GCode contract details not shown.
- id: 5
  reason: Lists covered topics and contract fields not supported by evidence.
- id: 6
  reason: Describes out-of-scope areas and broader workspace responsibilities without evidence.
- id: 8
  reason: States an architectural separation not shown in the supplied sources.
- id: 9
  reason: Attributes specific services, primitives, and daemon-managed assets to gcore without evidence.
- id: 10
  reason: Describes gcode contract contents and application-layer responsibilities not shown.
- id: 11
  reason: Claims the split’s effects on evolution and duplication without supporting evidence.
- id: 13
  reason: States installation and management behavior for the service stack without evidence.
- id: 14
  reason: Summarizes contract fields not shown in any source excerpt.
- id: 15
  reason: Claims command-layer orchestration and workflows not supported by evidence.
- id: 16
  reason: Attributes shared-core capabilities beyond what is evidenced.
- id: 17
  reason: Infers fallback handling and availability behavior not shown in sources.
- id: 18
  reason: Claims results return through the contract surface without evidence.
- id: 20
  reason: Names the main reference points without supporting source evidence.
- id: 21
  reason: Table entries assert roles and relationships not evidenced.
- id: 23
  reason: Recommends the contract as the starting point and summarizes its contents without evidence.
- id: 24
  reason: Claims GCore AI/context files explain infra ownership and centralization not shown.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/contract/gcode.contract.json](crates/gcode/contract/gcode.contract.json)
- [crates/gcode/src/commands/codewiki/prompts.rs](crates/gcode/src/commands/codewiki/prompts.rs)
- [crates/gcode/src/commands/codewiki/types.rs](crates/gcode/src/commands/codewiki/types.rs)
- [crates/gcode/src/commands/graph/reads.rs](crates/gcode/src/commands/graph/reads.rs)
- [crates/gcode/src/commands/grep.rs](crates/gcode/src/commands/grep.rs)
- [crates/gcode/src/commands/search.rs](crates/gcode/src/commands/search.rs)
- [crates/gcode/src/commands/symbol_at.rs](crates/gcode/src/commands/symbol_at.rs)
- [crates/gcode/src/config/services.rs](crates/gcode/src/config/services.rs)
- [crates/gcode/src/db/resolution.rs](crates/gcode/src/db/resolution.rs)
- [crates/gcode/src/index/semantic.rs](crates/gcode/src/index/semantic.rs)
- [crates/gcode/src/models.rs](crates/gcode/src/models.rs)
- [crates/gcore/assets/docker-compose.services.yml](crates/gcore/assets/docker-compose.services.yml)

_460 more source files omitted._

</details>

# Workspace Map

## Purpose

Workspace Map is the top-level orientation for how this codebase splits Gobby responsibilities across crates. The important boundary is that shared infrastructure lives in `crates/gcore`, while code-indexing and CLI behavior live in `crates/gcode`. The workspace-level `crates` area is the umbrella that groups these responsibilities ([crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]).

This solves the problem of keeping domain-facing tools from directly owning transport, storage, setup, and AI-service details. `crates/gcore` centralizes shared AI routing, context, configuration, service provisioning, graph/vector/search primitives, setup validation, and degradation contracts (, ). `crates/gcode` then builds the fast code-index CLI and its contract on top of that shared foundation ().

## Covers / Does not cover

This page covers the workspace map only at the level supported by the supplied files: the crate split, the shared core layer, the GCode CLI layer, and the runtime services/assets boundary. It also includes the documented GCode contract surface: invocation schema, global flags, scope resolution, command metadata, JSON output keys, and error-code metadata ().

It does not cover individual indexed symbols, because no indexed symbols were supplied. It also does not detail hook intake or wiki tooling internals; those are part of the broader workspace responsibility map, but no member modules or source excerpts for those areas were provided. The available evidence supports describing them only as out-of-scope workspace responsibilities, not as concrete architecture.

## Architecture

The architecture is arranged around a separation between shared capability and domain-facing tooling.

`crates/gcore` is the shared core layer. It owns cross-cutting services and primitives: AI context/routing, local and layered configuration, service provisioning, setup validation, graph/vector/search primitives, and degradation contracts (, ). Its local assets package also provides the service stack used by installed deployments; the Docker Compose services are installed by `gobby install` and managed by daemon start/stop profiles (, [crates/gcore/assets/docker-compose.services.yml:5-117]).

`crates/gcode` is the GCode CLI crate and its surrounding contract/assets bundle. Its contract describes a “Fast code index CLI for Gobby” at version 2, including how the CLI is invoked, which global flags exist, how scope is resolved, what commands expose, what JSON output keys are used, and how errors are represented (). Its application layer handles CLI orchestration, configuration/context resolution, PostgreSQL index access, graph/vector projection lifecycle, search/grep, setup, freshness, visibility, and shared output/model contracts (, ).

This split lets GCode focus on code-index user workflows while relying on GCore for shared infrastructure. The result is a workspace where indexing, search, and CLI contract behavior can evolve without duplicating service management, AI context handling, or setup/degradation logic.

## Data flow

1. A Gobby installation establishes the shared service layer through `crates/gcore` assets. The Docker Compose stack is installed by `gobby install` and managed by daemon start/stop profiles (, [crates/gcore/assets/docker-compose.services.yml:5-117]).

2. A user or caller invokes the GCode CLI according to the versioned contract. That contract defines the invocation schema, global flags, scope resolution, command metadata, JSON output keys, and error-code metadata for the fast code-index CLI ().

3. `crates/gcode` resolves CLI orchestration and configuration/context before reaching into the index-backed workflows. The supplied command modules show that search and grep live in this command layer (, ).

4. The command layer uses shared core capabilities rather than owning all infrastructure itself. `crates/gcore` supplies AI routing/context, configuration, service provisioning, graph/vector/search primitives, setup validation, and degradation contracts (, ).

5. If required service dependencies are unavailable, the evidence shows that availability is handled at the shared core/service-management boundary: `crates/gcore` owns setup validation and degradation contracts, and its service stack is managed through daemon start/stop profiles (, ). The supplied input does not expose the exact fallback behavior or user-facing error text.

6. Results return through the GCode contract surface, which defines the JSON output keys and error-code metadata that callers can rely on ().

## Key components

The main reference points are the workspace umbrella, the shared core crate, and the code-index CLI crate.

| Component | Role |
| --- | --- |
| `crates` | Workspace-level grouping for Gobby crate responsibilities ([crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]). |
| `crates/gcore` | Shared core layer for AI context/routing, configuration, services, setup validation, graph/vector/search primitives, and degradation contracts (, ). |
| `crates/gcore/assets/docker-compose.services.yml` | Installed service stack used by Gobby deployments and managed by daemon profiles (, [crates/gcore/assets/docker-compose.services.yml:5-117]). |
| `crates/gcode` | Fast code-index CLI crate and contract/assets bundle for search, grep, indexing context, output, and error metadata (, ). |

## Where to start

Start with the GCode contract if you want the external shape of the workspace-facing code-index tool: invocation, flags, scope, commands, JSON output, and errors are summarized there ().

Then read the GCore AI/context files to understand why GCode does not own all infrastructure directly: shared AI context, routing, configuration, setup validation, and degradation behavior are centralized in `crates/gcore` (, ).

## Explore

- [[code/modules/crates|crates]]
- [[code/modules/crates/gcore|crates/gcore]]
- [[code/modules/crates/gcode|crates/gcode]]

