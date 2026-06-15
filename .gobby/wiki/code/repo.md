---
title: Repository Overview
type: code_repo
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai_context.rs
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/gsqz/config.yaml
- file: crates/gsqz/src/config.rs
- file: crates/gwiki/contract/gwiki.contract.json
- file: crates/gwiki/src/benchmark.rs
- file: crates/gwiki/src/graph/mod.rs
- file: crates/gwiki/src/health.rs
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/search/semantic.rs
- file: crates/gwiki/src/vector.rs
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json
- file: docs/evidence/wiki-parity-2026-06/wp3-search-sources.json
provenance_truncated: 427
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# Repository Overview

## Overview

Gobby is a Rust workspace organized around command-line tools and shared local-first infrastructure. The `crates` tree is the main implementation area: it contains user-facing CLIs for code indexing, hook delivery, local LLM launching, LLM-oriented output compression, and wiki workflows, alongside shared runtime primitives in `gcore`. The shared crate centralizes bootstrap, daemon, project, config, AI, setup, degradation, datastore, search, and indexing capabilities, with heavier integrations gated behind features for lighter consumers (crates/gcore/src/lib.rs:27-34).

The major pieces fit together as separate packages with clear contracts: `gcode` and `gwiki` define public command shapes through contract JSON files, while `gcore` provides the reusable substrate used by tools that need common project, indexing, search, or integration behavior. Documentation is lighter-weight in the current snapshot: `docs` is mostly a container, and its active evidence area stores generated bundles such as the 2026-06 wiki-parity workstream for the wp3 scope [7913].

A reader should start in `crates`, especially `gcore` to understand the shared capabilities and then the individual CLI crates to see how those capabilities are exposed. For current documentation context, inspect the generated evidence bundle under `docs/evidence/wiki-parity-2026-06`, since the docs tree itself does not yet appear to hold direct implementation-bearing files.

## Modules

- [[code/modules/crates|crates]] - The crates module is the Rust workspace container for Gobby’s command-line tools and shared libraries. Its children cover code indexing (`gcode`), shared runtime and integration primitives (`gcore`), host CLI hook delivery (`ghook`), local LLM launcher behavior (`gloc`), output compression for LLM consumption (`gsqz`), and the local-first wiki CLI (`gwiki`). Each package owns either a user-facing CLI contract or a reusable layer: `gcode` and `gwiki` pin public command shapes in contract JSON files  , while `gcore` exposes common bootstrap, daemon, project, config, AI, setup, degradation, datastore, search, and indexing capabilities with heavier integrations feature-gated for lighter consumers (crates/gcore/src/lib.rs:27-34).

The main flows split along tool boundaries. `gcode` parses global flags and subcommands, then routes from its binary entry point into dispatch while supporting runtime config, daemon schemas, output formatting, and progress reporting [2315]  [1268] [1393]. `ghook` parses host CLI hook invocations, classifies diagnostics/version/owned-execution paths, and returns usage-style exit code 2 for validation failures  [3902]. `gloc` uses layered configuration to probe local backends such as LM Studio and Ollama until a responding backend wins [4064], while `gsqz` matches command-output pipelines in order and applies compression steps under configurable thresholds.

These crates collaborate by sharing conventions and infrastructure while keeping product-specific behavior isolated. `gcore` supplies the cross-cutting foundations that let CLIs depend on common project identity, daemon access, AI routing, setup, degradation, and optional service integrations without duplicating service logic (crates/gcore/src/lib.rs:27-34). The CLI packages then layer their own contracts and orchestration on top: `gcode` focuses on code-indexing workflows and daemon-facing schemas [30] [1393], `gwiki` defines wiki capture/search/upkeep/synthesis semantics and shared scope flags [4567] [4568], and the supporting tools (`ghook`, `gloc`, `gsqz`) feed runtime context, local AI execution, and compacted command output into those broader workflows.
- [[code/modules/docs|docs]] - The docs module is currently a container rather than an implementation-bearing package: it has no direct files, and its documented responsibility is expressed through child documentation artifacts. Its active child path, docs/evidence, is likewise a parent for generated evidence bundles, with the current docs/evidence/wiki-parity-2026-06 bundle preserving the 2026-06 wiki-parity workstream for the wp3 scope [7913].

The key flow captured under this module is audit evidence collection across wiki-parity operations. The evidence bundle records outputs from gwiki and ghook flows spanning compilation, ingestion, search, and ask behavior, so the docs tree functions as a traceable documentation and verification surface rather than runtime code [7913] [9331] [8066].

The collaboration model is simple: docs delegates all current responsibility to docs/evidence, and docs/evidence organizes timestamped or workstream-specific bundles beneath it. Those bundles carry structured records with shared fields such as command, status, source paths, search results, synthesis, citation checks, and warnings, allowing compile, search, and ask outputs to be inspected together as an auditable chain for the wiki-parity scope [7913] [9331] [8066].

## References

- [30] [crates/gcode/contract/gcode.contract.json:4]
- [1268] [crates/gcode/src/config.rs:1-25]
- [1393] [crates/gcode/src/contract.rs:5-288]
- [2315] [crates/gcode/src/main.rs:4-6]
- [3902] [crates/ghook/src/args.rs:9-33]
- [4064] [crates/gloc/config.yaml:18-30]
- [4567] [crates/gwiki/contract/gwiki.contract.json:4]
- [4568] [crates/gwiki/contract/gwiki.contract.json:5-25]
- [7913] [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
- [8066] [docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10]
- [9331] [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]

