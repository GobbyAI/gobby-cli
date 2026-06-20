---
title: Repository Insight Pages
type: code_concept
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
- file: crates/gcode/src/commands/codewiki/build_parts/features.rs
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
- file: crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
- file: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
- file: crates/gcode/src/commands/codewiki/ownership/analysis.rs
- file: crates/gcode/src/commands/codewiki/ownership/codeowners.rs
- file: crates/gcode/src/commands/codewiki/ownership/render.rs
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
- file: crates/gcode/src/commands/codewiki/render/audit.rs
- file: crates/gcode/src/commands/codewiki/render/common.rs
- file: crates/gcode/src/commands/codewiki/render/diagrams.rs
- file: crates/gcode/src/commands/codewiki/render/features.rs
- file: crates/gcode/src/commands/codewiki/render/infrastructure.rs
- file: crates/gcode/src/commands/codewiki/render/overview.rs
- file: crates/gcode/src/commands/codewiki/render/pages.rs
- file: crates/gcode/src/commands/codewiki/render/repo.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: Lists page families and build_parts contents not shown in the supplied excerpts.
- id: 3
  reason: Claims about architecture views, entry-point summaries, and render/audit behavior are not shown.
- id: 5
  reason: Includes architecture/infrastructure and Git-blame metadata claims not supported by the excerpts.
- id: 6
  reason: Curated-concepts planning/rendering and fallback behavior are not shown.
- id: 8
  reason: Render/audit markdown details are not shown in the supplied evidence.
- id: 9
  reason: Claims about render.rs page conversion and aggregation helpers are not supported by the excerpt.
- id: 12
  reason: Mentions a module map for ownership, which is not shown in the evidence.
- id: 19
  reason: Claims about render/audit module and architecture page structure are not shown.
- id: 24
  reason: The claim that build_parts shows which page families exist is not supported by the excerpts.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/architecture.rs](crates/gcode/src/commands/codewiki/build_parts/architecture.rs)
- [crates/gcode/src/commands/codewiki/build_parts/audit.rs](crates/gcode/src/commands/codewiki/build_parts/audit.rs)
- [crates/gcode/src/commands/codewiki/build_parts/changes.rs](crates/gcode/src/commands/codewiki/build_parts/changes.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts.rs](crates/gcode/src/commands/codewiki/build_parts/concepts.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs)
- [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs](crates/gcode/src/commands/codewiki/build_parts/curated_content.rs)
- [crates/gcode/src/commands/codewiki/build_parts/features.rs](crates/gcode/src/commands/codewiki/build_parts/features.rs)
- [crates/gcode/src/commands/codewiki/build_parts/file.rs](crates/gcode/src/commands/codewiki/build_parts/file.rs)

_17 more source files omitted._

</details>

# Repository Insight Pages

## Purpose

Repository Insight Pages round out CodeWiki with higher-level documentation views built from indexed facts and repository metadata. They explain ownership, audits, feature catalogs, onboarding paths, architecture, hotspots, and infrastructure without requiring each page to be hand-authored. The `build_parts` module is the generation toolkit behind these page types, including architecture, audits, curated concepts, feature catalogs, file/module pages, hotspots, infrastructure, onboarding, and snapshots [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170].

The problem they solve is discoverability: a new engineer can move from raw files and symbols to purpose-built reference pages that summarize who owns code, what entry points matter, which CLI features exist, where deprecated or dead-code candidates appear, and how repository pieces connect. Rendering is handled separately so generated data models become navigable Markdown pages with frontmatter, verification/degradation metadata, and wiki links rather than raw provenance dumps [crates/gcode/src/commands/codewiki/render/audit.rs:8-57].

## Covers / Does not cover

This concept covers the repository-level documentation surface produced by CodeWiki: ownership pages, deterministic audit pages, feature catalogs, onboarding pages, architecture and infrastructure views, and related generated reference pages [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170]. It includes both indexed inputs, such as symbols and call graph edges, and repository metadata, such as CODEOWNERS files, Git blame summaries, pinned CLI contract JSON, and module/file summaries  [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7] [crates/gcode/src/commands/codewiki/build_parts/features.rs:16-19].

It does not cover changing the index parser or hub schema for audits; the audit path explicitly keeps those untouched and performs bounded source scans at generation time . It also does not make every page depend on LLM generation: audit pages are deterministic and LLM-free . Curated concepts are different: they use a planning step and a rendering step, with fallback behavior when generation is unavailable or degraded [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170].

## Architecture

The design separates page construction from Markdown rendering. `build_parts` gathers and shapes domain-specific documentation models: audits from code index facts and bounded source scans, feature catalogs from pinned contracts, onboarding from files/modules/graph edges, and ownership from CODEOWNERS plus Git blame metadata  [crates/gcode/src/commands/codewiki/build_parts/features.rs:39-46] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-43]. The `render` module then turns those models into human-readable Markdown with frontmatter, navigable links, subsystem tables, module rows, and degradation metadata [crates/gcode/src/commands/codewiki/render/audit.rs:8-57].

Ownership is a good example of the arrangement. `codeowners.rs` reads the first available CODEOWNERS file from known locations, parses ordered ownership rules, and resolves declared owners by applying the last matching rule to each file [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7]. `analysis.rs` derives contributors from Git blame, caching by content hash and marking partial status on timeouts or file caps [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]. `render.rs` converts the resulting status and file ownership into a Code Ownership page, including `type: code_ownership`, degradation sources, and aggregation helpers for primary owners and contributors [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34] [crates/gcode/src/commands/codewiki/ownership/render.rs:116-126] [crates/gcode/src/commands/codewiki/ownership/render.rs:128-172].

Audits are deliberately deterministic. `AuditContext` carries the project root, deprecation index, test-gated symbol index, and contract-handler entry points so deprecation and dead-code pages can be generated once from repository facts without altering shared index schemas [crates/gcode/src/commands/codewiki/build_parts/audit.rs:38-51]. Feature catalog generation follows a separate contract-driven path: `BinaryContract` maps each binary display name to its workspace crate and contract file, while `Contract`, `ContractCommand`, and `ContractFlag` deserialize only the fields needed for a navigational catalog [crates/gcode/src/commands/codewiki/build_parts/features.rs:16-19] [crates/gcode/src/commands/codewiki/build_parts/features.rs:22-28] [crates/gcode/src/commands/codewiki/build_parts/features.rs:31-34] [crates/gcode/src/commands/codewiki/build_parts/features.rs:39-46].

## Data flow

1. CodeWiki starts with indexed repository inputs: file docs, module docs, symbols, graph edges, and repository metadata. Audit generation consumes symbols and call graph edges plus a bounded source scan, while ownership consumes a project root, file list, module map, mutable ownership metadata, and ownership options  [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21].

2. Ownership first tries to load CODEOWNERS from `CODEOWNERS`, `.github/CODEOWNERS`, or `docs/CODEOWNERS`. If no file is found, `read_codeowners` returns `None`; declared owner resolution then returns an empty map when no `Codeowners` value is available [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7].

3. Ownership then tries to derive contributors from Git blame. If repository discovery or `HEAD` lookup fails, the derived contributor map is empty. When blame is available, the status records that fact, cached summaries are reused by content hash, and timeouts or file caps mark the result partial [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21].

4. Ownership rendering records degraded sources based on what was unavailable or partial: missing CODEOWNERS, missing Git blame, blame errors, partial blame, or completely unknown ownership all become explicit degradation markers [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34]. The page frontmatter includes `type: code_ownership`, generated/trust/freshness labels, optional `degraded`, optional `degraded_sources`, and optional `partial` [crates/gcode/src/commands/codewiki/ownership/render.rs:38-52].

5. Audit generation builds deterministic deprecation and dead-code pages from existing code index facts and source scans. If there is nothing to report, or if the graph is unavailable, the pages still render; audit pages are described as never degrading .

6. Feature catalog generation parses pinned CLI contract JSON into contracts, commands, and flags, then maps binaries through `BinaryContract` metadata. The contract command set is treated as the authority, while handler mapping gaps remain visible instead of being silently hidden [crates/gcode/src/commands/codewiki/build_parts/features.rs:16-19] [crates/gcode/src/commands/codewiki/build_parts/features.rs:39-46].

7. Onboarding generation finds Rust entry files and, when graph data is available or truncated, computes a centrality-ranked reading order. If the graph is unavailable, the onboarding page keeps entry points, omits the reading order, and does not mark the page degraded [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-43].

8. Renderers convert the generated models into Markdown pages with navigation-oriented links and structured sections. Module pages include parent navigation, overviews, child-module rows, and direct-file rows; architecture pages combine narrative, validated diagram or service-matrix strings, and deterministic subsystem tables [crates/gcode/src/commands/codewiki/render/audit.rs:8-57].

## Key components

The most important symbols are the ones that define page inputs, degradation behavior, and compact repository metadata models.

| Symbol | Role |
| --- | --- |
| `AuditContext` | Bundles project root, deprecation index, test-gated symbols, and contract-handler entry points for deterministic audit generation [crates/gcode/src/commands/codewiki/build_parts/audit.rs:38-51]. |
| `Codeowners` / `CodeownersEntry` | Store ordered CODEOWNERS rules as path patterns with owner lists, used to resolve declared file ownership [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7] [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:10-13]. |
| `BlameContributorsOutcome` | Represents Git blame contributor collection as success, timeout, or error, which feeds ownership degradation and partial status [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]. |
| `Frontmatter` | Serializes ownership page metadata including document type, generator labels, degradation flags, and source lists [crates/gcode/src/commands/codewiki/ownership/render.rs:38-52]. |
| `Contract`, `ContractCommand`, `ContractFlag` | Deserialize the pinned CLI contract fields needed to build feature catalog rows [crates/gcode/src/commands/codewiki/build_parts/features.rs:16-19] [crates/gcode/src/commands/codewiki/build_parts/features.rs:22-28] [crates/gcode/src/commands/codewiki/build_parts/features.rs:31-34]. |
| `BinaryContract` | Maps a binary name to its workspace crate directory and contract file path for catalog enumeration [crates/gcode/src/commands/codewiki/build_parts/features.rs:39-46]. |

## Where to start

Start with `crates/gcode/src/commands/codewiki/build_parts`, because it defines the generation side of Repository Insight Pages and shows which page families exist [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170]. From there, read the ownership path next if you want the clearest end-to-end example: CODEOWNERS parsing, Git blame derivation, degradation tracking, and Markdown frontmatter are split across focused files [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7] [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21] [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34].

## Explore

- [[code/modules/crates/gcode/src/commands/codewiki/ownership|crates/gcode/src/commands/codewiki/ownership]]
- [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]
- [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

