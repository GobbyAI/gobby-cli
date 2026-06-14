---
title: Repository Overview
type: code_repo
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/ownership.rs
- file: crates/gcode/src/commands/codewiki/text.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/index/walker.rs
- file: crates/gcode/src/models.rs
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai_context.rs
- file: crates/gcore/src/config/tests.rs
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/gsqz/config.yaml
- file: crates/gsqz/src/config.rs
- file: crates/gwiki/contract/gwiki.contract.json
- file: crates/gwiki/src/ai/chunk.rs
- file: crates/gwiki/src/audit.rs
- file: crates/gwiki/src/benchmark.rs
- file: crates/gwiki/src/falkor_graph.rs
- file: crates/gwiki/src/graph/mod.rs
- file: crates/gwiki/src/health.rs
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/ingest/url.rs
- file: crates/gwiki/src/search/semantic.rs
- file: crates/gwiki/src/store.rs
- file: crates/gwiki/src/vector.rs
- file: docs/evidence/wiki-parity-2026-06/wp3-search-sources.json
provenance_truncated: 342
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# Repository Overview

## Overview

Gobby is organized as a Rust workspace whose top-level `crates` directory groups the command-line tooling and shared foundation rather than owning direct source files itself. The main CLI-facing pieces are split between `gcode`, which provides a code-indexing command-line tool plus reusable library APIs, and `gcore`, which supplies shared infrastructure such as bootstrap, daemon URL discovery, project lookup, layered configuration, CLI contracts, setup/provisioning, degradation terminology, and optional storage/indexing integrations [2336] [491] [2330] [3527].

The major pieces fit together around a clean separation between CLI concerns, daemon-facing contracts, and reusable indexing foundations. `gcode` keeps command parsing, process dispatch, contract publication, and core indexing APIs separated, with tests protecting the public library from depending on CLI-specific code [1370] [2330]. `gcore` sits underneath as the common layer used to discover projects and daemon endpoints, manage configuration, describe command contracts, and package the Docker Compose service stack installed by `gobby install` [3527].

A reader should start in `crates/gcore/src/lib.rs` to understand the shared vocabulary and services that support the workspace, then move to `crates/gcode/src/lib.rs` for the reusable indexing API surface and `crates/gcode/src/cli.rs` or `crates/gcode/src/main.rs` for how that functionality is exposed as a command-line program [3527] [2330] [491] [2336]. The `docs` tree is presently just a documentation namespace, with `docs/evidence` serving as a container for proof artifacts rather than executable code or authored documentation.

## Modules

- [[code/modules/crates|crates]] - The crates module is a container directory with no direct files of its own; it groups the Rust workspace's tooling crates and shared foundation that together make up the Gobby command-line surface. Its responsibilities are split across six child crates: gcode packages a code-indexing CLI and reusable library whose source root keeps command parsing, process dispatch, daemon-facing contract publication, and core indexing APIs separated, with tests guarding that the public library stays independent of CLI-specific code [2336] [491] [1370] [2330]; and gcore provides the shared foundation—bootstrap, daemon URL discovery, project lookup, layered configuration, CLI contracts, setup/provisioning, degradation vocabulary, and feature-gated storage/indexing integrations—alongside assets that package the Docker Compose service stack installed by `gobby install` [3527].

The remaining crates layer specific tools on top of that foundation. ghook is a hook-dispatcher crate plus strict draft-07 JSON schemas for diagnostic output and queued inbox envelopes, using `additionalProperties: false` so external surfaces reject unknown fields [3843] [3893]. gloc is a launcher that auto-detects a local LLM backend and hands control to a supported AI CLI, with a built-in YAML defining configuration precedence and runtime defaults such as a 500 ms probe timeout and automatic model loading [crates/gloc/config.yaml:11-14]. gsqz compresses command output for LLM consumption, defining ordered first-match-wins pipeline matching in YAML and routing stdin or stripped-ANSI command output through the compressor with optional stats and daemon savings reporting [4487] [4489] [4491]. gwiki is the local-first wiki system, pairing a contract layer that declares tool identity, version, command shape, output flags, and scope selectors with a library/CLI layer covering scope resolution, vault initialization, ingestion, indexing, manifest and registry persistence, search, provenance audits, and formatted output [4618] [4621] [6828].

These crates collaborate through a consistent pattern established in gcode and gcore: each tool publishes a JSON CLI contract describing its tool identity, version, summary, global flags, project detection, and identity keys [28] [31], while depending on gcore for cross-cutting concerns like configuration layering, daemon discovery, and the provisioned service stack. The tool crates (gcode, gsqz, gloc, ghook, gwiki) thus remain focused on their domain logic and contract surfaces, deferring shared bootstrap, storage, and degradation handling to gcore so that the Gobby CLI ecosystem stays uniform in how it detects projects, reads configuration, and reports degraded behavior.
- [[code/modules/docs|docs]] - The docs module is currently a documentation namespace with no direct files of its own. Its responsibilities are expressed through child modules, especially docs/evidence, which acts as a container for proof artifacts rather than executable source or authored documentation.

The visible flow is evidence-driven: docs/evidence/wiki-parity-2026-06 records artifacts for a gwiki parity workflow that resolves a project scope, searches within that scope, selects relevant sources, and uses those sources to compile a grounded explainer. The stable component IDs show the shape of those artifacts, including search inputs and results, selected source paths, prompts, synthesis metadata, citation handling, page writes, and generated article/index paths.

Because the docs module has no direct files or source excerpts in the supplied input, collaboration is organized by containment rather than code calls: docs owns the top-level documentation area, docs/evidence groups evidence sets, and the wiki parity child set carries the concrete workflow records and metadata. No file:line spans were supplied for citation.
[7917]
[7949]
[7981]
[7918]
[7919]

## References

- [28] [crates/gcode/contract/gcode.contract.json:2]
- [31] [crates/gcode/contract/gcode.contract.json:5-49]
- [491] [crates/gcode/src/cli.rs:21-44]
- [1370] [crates/gcode/src/contract.rs:5-259]
- [2330] [crates/gcode/src/lib.rs:34-42]
- [2336] [crates/gcode/src/main.rs:4-6]
- [3527] [crates/gcore/src/lib.rs:27-34]
- [3843] [crates/ghook/schemas/diagnose-output.v2.schema.json:19]
- [3893] [crates/ghook/schemas/inbox-envelope.v1.schema.json:16]
- [4487] [crates/gsqz/src/main.rs:25-48]
- [4489] [crates/gsqz/src/main.rs:67-139]
- [4491] [crates/gsqz/src/main.rs:186-276]
- [4618] [crates/gwiki/contract/gwiki.contract.json:2]
- [4621] [crates/gwiki/contract/gwiki.contract.json:5-25]
- [6828] [crates/gwiki/src/lib.rs:1-60]
- [7917] [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
- [7918] [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:4]
- [7919] [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:5]
- [7949] [docs/evidence/wiki-parity-2026-06/wp3-compile-explainer.json:3-12]
- [7981] [docs/evidence/wiki-parity-2026-06/wp3-search-sources.json:3-16]

