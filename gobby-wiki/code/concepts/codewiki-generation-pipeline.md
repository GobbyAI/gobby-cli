---
title: CodeWiki Generation Pipeline
type: code_concept
provenance:
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
- file: crates/gcode/src/commands/codewiki/build_parts/features.rs
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
- file: crates/gcode/src/commands/codewiki/cluster.rs
- file: crates/gcode/src/commands/codewiki/generation.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/ownership.rs
- file: crates/gcode/src/commands/codewiki/ownership/analysis.rs
- file: crates/gcode/src/commands/codewiki/ownership/render.rs
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
- file: crates/gcode/src/commands/codewiki/paths.rs
- file: crates/gcode/src/commands/codewiki/progress.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/relationship_facts.rs
- file: crates/gcode/src/commands/codewiki/repair.rs
- file: crates/gcode/src/commands/codewiki/reuse.rs
- file: crates/gcode/src/commands/codewiki/run.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text.rs
- file: crates/gcode/src/commands/codewiki/text/citations.rs
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
- file: crates/gcode/src/commands/codewiki/text/generation.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/text/structural.rs
- file: crates/gcode/src/commands/codewiki/text/verify.rs
- file: crates/gcode/src/commands/codewiki/types.rs
provenance_truncated: 25
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: Invents a pipeline name; the excerpt only shows types and helpers.
- id: 3
  reason: Claims compact tables for prompts; the excerpt only shows evidence-only and citation requirements.
- id: 5
  reason: Cites types.rs 479-533, but those fields are not in the supplied excerpts.
- id: 6
  reason: References build_parts families that are not shown in the supplied evidence.
- id: 9
  reason: CodewikiGraph and the caller/import relationship claims are not shown in the excerpts.
- id: 10
  reason: CodewikiAiOptions fields at types.rs 693-712 are not shown in the excerpts.
- id: 11
  reason: BuiltDoc and CodewikiDocMeta details are not present in the supplied excerpts.
- id: 16
  reason: ArchitectureDoc and audit-page behavior are not shown in the excerpts.
- id: 17
  reason: Overgeneralizes prompt behavior; the symbol prompt is one sentence, not Markdown.
- id: 21
  reason: BuiltDoc and CodewikiDocMeta fields at those line ranges are not shown in the excerpts.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/architecture_diagrams.rs](crates/gcode/src/commands/codewiki/architecture_diagrams.rs)
- [crates/gcode/src/commands/codewiki/build_parts/audit.rs](crates/gcode/src/commands/codewiki/build_parts/audit.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs)
- [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs](crates/gcode/src/commands/codewiki/build_parts/curated_content.rs)
- [crates/gcode/src/commands/codewiki/build_parts/features.rs](crates/gcode/src/commands/codewiki/build_parts/features.rs)
- [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs)
- [crates/gcode/src/commands/codewiki/cluster.rs](crates/gcode/src/commands/codewiki/cluster.rs)
- [crates/gcode/src/commands/codewiki/generation.rs](crates/gcode/src/commands/codewiki/generation.rs)
- [crates/gcode/src/commands/codewiki/io.rs](crates/gcode/src/commands/codewiki/io.rs)
- [crates/gcode/src/commands/codewiki/ownership.rs](crates/gcode/src/commands/codewiki/ownership.rs)
- [crates/gcode/src/commands/codewiki/ownership/analysis.rs](crates/gcode/src/commands/codewiki/ownership/analysis.rs)

_43 more source files omitted._

</details>

# CodeWiki Generation Pipeline

## Purpose

CodeWiki Generation Pipeline is the documentation-generation subsystem that turns indexed repository facts into grounded wiki pages. It solves the problem of keeping generated documentation tied to source evidence: files, symbols, graph relationships, leading source chunks, prompts, verifier notes, rendered Markdown, and regeneration metadata all flow through explicit data structures instead of free-form prose alone .

The pipeline is designed to generate useful narrative pages while preserving boundaries: prompts require supplied evidence only, citation anchors, cross-file relationships when available, and compact tables for enumerable facts . Verification is optional but grounded: when it runs, it records unsupported-block findings as notes rather than rewriting the generated prose .

## Covers / Does not cover

This page covers the runtime path from indexed repository data to CodeWiki page models, AI-assisted or deterministic text, verification metadata, rendering, and persistence-oriented document metadata. It includes the main input model, graph facts, leading source excerpts, generation options, rendered document output, and invalidation metadata .

It does not cover every page builder in `build_parts`, every renderer, or every indexed symbol. The supplied evidence shows that `build_parts` includes many document-generation families such as architecture, audits, changes, curated concepts, feature catalogs, file/module pages, hotspots, infrastructure, onboarding, and snapshots, but this explainer focuses on the shared generation pipeline rather than each page type [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170].

## Architecture

The pipeline is arranged around a narrow input core and several specialized stages. `CodewikiInput` collects the files selected for documentation, graph edges, graph availability, symbols, and leading chunks from the index [crates/gcode/src/commands/codewiki/types.rs:11-21]. Leading chunks are important because they provide real source text and line provenance for prompts; when they are missing, aggregate prompts degrade to summary-only input rather than inventing source context .

Graph data is modeled separately from files and symbols. `CodewikiGraph` carries both edges and availability status, while each `CodewikiGraphEdge` records a directed relationship from one component ID to another with a specific edge kind [crates/gcode/src/commands/codewiki/types.rs:65-69], [crates/gcode/src/commands/codewiki/types.rs:102-105]. This lets generated pages describe callers, callees, imports, and other relationships when those facts are present, without making prose generation responsible for discovering relationships itself .

Text generation and verification are also separated. `CodewikiAiOptions` configures generation and verification routing, depth, verbosity, audience register, profile, and model overrides [crates/gcode/src/commands/codewiki/types.rs:693-712]. The text generator resolves an AI context and route, then returns no generator when routing is `Off` or `Auto`; successful routes use bounded retry behavior and model-specific token limits [crates/gcode/src/commands/codewiki/text/generation.rs:23-79]. Verification is a second pass over already-generated prose, and its notes are kept as frontmatter-only audit information rather than mutating the page body .

Rendering is the final human-facing layer. Renderers turn page models into Markdown with frontmatter, degradation metadata, verification notes, wiki links, and structured sections instead of raw provenance dumps [crates/gcode/src/commands/codewiki/render/pages.rs:5-51]. Persistence and incremental regeneration are represented by `BuiltDoc`, which carries path, content, degradation status, persistent summary, cross-file dependencies, and an optional invalidation key, and by `CodewikiDocMeta`, which tracks source hashes, neighbor hashes, quality status, cached summaries, generation modes, and template versions [crates/gcode/src/commands/codewiki/types.rs:518-533], [crates/gcode/src/commands/codewiki/types.rs:479-513].

## Data flow

1. The CLI entry point validates the edge limit, initializes progress reporting, opens a readonly database connection, normalizes scope arguments, and loads visible files that should be documented [crates/gcode/src/commands/codewiki/run.rs:23-223].

2. It loads symbols for the selected files, fetches graph edges for those files and symbols, and loads leading content chunks from the index before assembling `CodewikiInput` [crates/gcode/src/commands/codewiki/run.rs:23-223], [crates/gcode/src/commands/codewiki/types.rs:11-21].

3. Leading chunks are converted into prompt source excerpts through `source_excerpt_for_file`; module-level context can use `ranked_source_excerpts`, which ranks candidate files by symbol count and path tie-break before taking the top excerpts . If a file has no leading chunk, the evidence says prompts degrade to summary-only input .

4. Build stages use the shared facts to create page models. Architecture documents carry source spans, subsystems, optional narrative, Mermaid diagrams, an optional service dependency matrix, and degraded sources [crates/gcode/src/commands/codewiki/types.rs:201-218]. Audit pages can be deterministic and LLM-free, using indexed symbols, call graph edges, and bounded scans [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170].

5. Prompt contracts constrain AI output. Symbol, file, content-file, and module prompts require concise Markdown, supplied evidence only, valid citation anchors, and relationship explanations when cross-file facts are supplied .

6. The text generator resolves AI configuration and routing. If AI context resolution fails, or if the effective route is `Off` or `Auto`, no generator is returned and generation-dependent paths must fall back or degrade according to their builder behavior [crates/gcode/src/commands/codewiki/text/generation.rs:23-79].

7. When verification is configured and runnable, the verifier splits prose into blocks, asks for unsupported-block findings, and returns either verified text with notes or verified text with an empty notes list. If there is no verifier, the verifier is unavailable, there is nothing to verify, or the verdict is malformed, verification is skipped [crates/gcode/src/commands/codewiki/text/verify.rs:19-30], .

8. Renderers convert the page models into Markdown. Module pages, for example, write range-free frontmatter, parent navigation, an overview, child-module rows, and direct-file rows, while attaching degradation and verification metadata [crates/gcode/src/commands/codewiki/render/pages.rs:5-51].

9. The resulting `BuiltDoc` carries the rendered path and content plus degradation state, persistent summary, cross-file dependencies, and invalidation key for downstream persistence and incremental invalidation [crates/gcode/src/commands/codewiki/types.rs:518-533]. `CodewikiDocMeta` stores hashes and generation metadata so later runs can decide what needs regeneration [crates/gcode/src/commands/codewiki/types.rs:479-513].

## Key components

The most important symbols are the ones that define the pipeline’s contract: input facts, graph relationships, AI behavior, verification/rendering output, and regeneration metadata.

| Symbol | Role |
| --- | --- |
| `CodewikiInput` | Collects selected files, graph edges, graph availability, symbols, and leading chunks for generation [crates/gcode/src/commands/codewiki/types.rs:11-21]. |
| `CodewikiGraph` / `CodewikiGraphEdge` | Represent available relationship facts and directed component relationships used by generated pages [crates/gcode/src/commands/codewiki/types.rs:102-105], [crates/gcode/src/commands/codewiki/types.rs:65-69]. |
| `CodewikiAiOptions` | Configures AI routing, depth, prose style, profiles, and verification-related options [crates/gcode/src/commands/codewiki/types.rs:693-712]. |
| `ArchitectureDoc` | Holds architecture-page source spans, subsystems, narrative, diagrams, service matrix, and degraded sources [crates/gcode/src/commands/codewiki/types.rs:201-218]. |
| `BuiltDoc` | Represents the rendered document plus persistence, degradation, dependency, and invalidation information [crates/gcode/src/commands/codewiki/types.rs:518-533]. |
| `CodewikiDocMeta` | Tracks hashes, quality status, summaries, generation modes, and template versions for incremental regeneration [crates/gcode/src/commands/codewiki/types.rs:479-513]. |

## Where to start

Start with `CodewikiInput` in `crates/gcode/src/commands/codewiki/types.rs`, because it defines the fact bundle that every later stage depends on: selected files, symbols, graph relationships, graph availability, and leading source chunks [crates/gcode/src/commands/codewiki/types.rs:11-21].

After that, read `run` to see how the CLI fills that input from the index and graph fetcher [crates/gcode/src/commands/codewiki/run.rs:23-223], then read the prompt contracts and verification path to understand how generated prose is constrained and audited , .

## Explore

- [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]
- [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]
- [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]
- [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

