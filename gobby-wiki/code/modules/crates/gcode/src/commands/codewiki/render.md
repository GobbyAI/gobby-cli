---
title: crates/gcode/src/commands/codewiki/render
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/render/common.rs
  ranges:
  - 1-7
- file: crates/gcode/src/commands/codewiki/render/diagrams.rs
  ranges:
  - 5-67
  - 72-92
  - 97-127
  - 131-166
  - 170-197
  - 199-222
  - 224-231
  - 233-330
  - 332-349
  - 351-380
  - 382-432
  - 434-447
  - 449-459
  - 461-476
- file: crates/gcode/src/commands/codewiki/render/overview.rs
  ranges:
  - 5-48
  - 50-87
  - 89-133
  - 135-137
  - 139-198
- file: crates/gcode/src/commands/codewiki/render/pages.rs
  ranges:
  - 6-72
  - 74-133
- file: crates/gcode/src/commands/codewiki/render/repo.rs
  ranges:
  - 5-91
  - 96-116
  - 118-172
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/render/common.rs:1-7](crates/gcode/src/commands/codewiki/render/common.rs#L1-L7)
- [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67](crates/gcode/src/commands/codewiki/render/diagrams.rs#L5-L67), [crates/gcode/src/commands/codewiki/render/diagrams.rs:72-92](crates/gcode/src/commands/codewiki/render/diagrams.rs#L72-L92), [crates/gcode/src/commands/codewiki/render/diagrams.rs:97-127](crates/gcode/src/commands/codewiki/render/diagrams.rs#L97-L127), [crates/gcode/src/commands/codewiki/render/diagrams.rs:131-166](crates/gcode/src/commands/codewiki/render/diagrams.rs#L131-L166), [crates/gcode/src/commands/codewiki/render/diagrams.rs:170-197](crates/gcode/src/commands/codewiki/render/diagrams.rs#L170-L197), [crates/gcode/src/commands/codewiki/render/diagrams.rs:199-222](crates/gcode/src/commands/codewiki/render/diagrams.rs#L199-L222), [crates/gcode/src/commands/codewiki/render/diagrams.rs:224-231](crates/gcode/src/commands/codewiki/render/diagrams.rs#L224-L231), [crates/gcode/src/commands/codewiki/render/diagrams.rs:233-330](crates/gcode/src/commands/codewiki/render/diagrams.rs#L233-L330), [crates/gcode/src/commands/codewiki/render/diagrams.rs:332-349](crates/gcode/src/commands/codewiki/render/diagrams.rs#L332-L349), [crates/gcode/src/commands/codewiki/render/diagrams.rs:351-380](crates/gcode/src/commands/codewiki/render/diagrams.rs#L351-L380), [crates/gcode/src/commands/codewiki/render/diagrams.rs:382-432](crates/gcode/src/commands/codewiki/render/diagrams.rs#L382-L432), [crates/gcode/src/commands/codewiki/render/diagrams.rs:434-447](crates/gcode/src/commands/codewiki/render/diagrams.rs#L434-L447), [crates/gcode/src/commands/codewiki/render/diagrams.rs:449-459](crates/gcode/src/commands/codewiki/render/diagrams.rs#L449-L459), [crates/gcode/src/commands/codewiki/render/diagrams.rs:461-476](crates/gcode/src/commands/codewiki/render/diagrams.rs#L461-L476)
- [crates/gcode/src/commands/codewiki/render/overview.rs:5-48](crates/gcode/src/commands/codewiki/render/overview.rs#L5-L48), [crates/gcode/src/commands/codewiki/render/overview.rs:50-87](crates/gcode/src/commands/codewiki/render/overview.rs#L50-L87), [crates/gcode/src/commands/codewiki/render/overview.rs:89-133](crates/gcode/src/commands/codewiki/render/overview.rs#L89-L133), [crates/gcode/src/commands/codewiki/render/overview.rs:135-137](crates/gcode/src/commands/codewiki/render/overview.rs#L135-L137), [crates/gcode/src/commands/codewiki/render/overview.rs:139-198](crates/gcode/src/commands/codewiki/render/overview.rs#L139-L198)
- [crates/gcode/src/commands/codewiki/render/pages.rs:6-72](crates/gcode/src/commands/codewiki/render/pages.rs#L6-L72), [crates/gcode/src/commands/codewiki/render/pages.rs:74-133](crates/gcode/src/commands/codewiki/render/pages.rs#L74-L133)
- [crates/gcode/src/commands/codewiki/render/repo.rs:5-91](crates/gcode/src/commands/codewiki/render/repo.rs#L5-L91), [crates/gcode/src/commands/codewiki/render/repo.rs:96-116](crates/gcode/src/commands/codewiki/render/repo.rs#L96-L116), [crates/gcode/src/commands/codewiki/render/repo.rs:118-172](crates/gcode/src/commands/codewiki/render/repo.rs#L118-L172)

</details>

# crates/gcode/src/commands/codewiki/render

Parent: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The `crates/gcode/src/commands/codewiki/render` module is responsible for generating consistent, structured Markdown documentation pages and interactive visualizations for a codebase's CodeWiki. It orchestrates the rendering of diverse page archetypes, including high-level repository overviews [crates/gcode/src/commands/codewiki/render/repo.rs:5-91], "Start Here" onboarding guides, subsystem architecture overviews [crates/gcode/src/commands/codewiki/render/overview.rs:5-48, 50-87], hotspot maps [crates/gcode/src/commands/codewiki/render/overview.rs:89-133], and individual module or file reference guides [crates/gcode/src/commands/codewiki/render/pages.rs:6-72, 74-133]. During generation, it aggregates, filters, and bounds dependency and call edges to produce legible, localized Mermaid diagrams tailored to the active file or module scope [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67].

The primary flow transforms extracted codebase metadata—such as module definitions, graph edges, and source spans—into polished markdown content integrated with frontmatter metadata, navigation controls, and degradation status tags [crates/gcode/src/commands/codewiki/render/common.rs:1-7][crates/gcode/src/commands/codewiki/render/pages.rs:6-72]. The module collaborates with text-generation models to synthesize global repository summaries from source excerpts when cached page content cannot be reused [crates/gcode/src/commands/codewiki/render/repo.rs:5-91, 118-172]. It ensures schematic readability by automatically truncating complex import trees and inserting fallback diagrams representing internal relations of nested sub-modules [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67].

### Key Render Symbols

| Symbol | Type | Description | Source Citation |
| --- | --- | --- | --- |
| `model_degraded_sources` | Function | Resolves model degradation flags into a list of tags. | [crates/gcode/src/commands/codewiki/render/common.rs:1-7] |
| `render_module_dependency_mermaid` | Function | Renders hop-bounded module import dependency trees as Mermaid diagrams. | [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67] |
| `render_architecture_doc` | Function | Emits the structural "Architecture Overview" document page. | [crates/gcode/src/commands/codewiki/render/overview.rs:5-48] |
| `render_onboarding_doc` | Function | Produces the "Start Here" onboarding documentation page. | [crates/gcode/src/commands/codewiki/render/overview.rs:50-87] |
| `render_hotspots_doc` | Function | Formats hotspot metadata and cross-references into an overview page. | [crates/gcode/src/commands/codewiki/render/overview.rs:89-133] |
| `render_module_doc` | Function | Assembles Markdown reference pages with parent navigation for modules. | [crates/gcode/src/commands/codewiki/render/pages.rs:6-72] |
| `render_file_doc` | Function | Builds documentation pages for individual files using source context. | [crates/gcode/src/commands/codewiki/render/pages.rs:74-133] |
| `build_repo_doc` | Function | Collects structures and initiates AI generation for repository-level overviews. | [crates/gcode/src/commands/codewiki/render/repo.rs:5-91] |
| `render_repo_doc` | Function | Formats global repository metadata into final rendered overview text. | [crates/gcode/src/commands/codewiki/render/repo.rs:118-172] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/render/common.rs\|crates/gcode/src/commands/codewiki/render/common.rs]] | Provides a small helper for render code that turns a degraded-model flag into the list of source tags to report: it returns `["model-unavailable"]` when degraded is true, and an empty vector otherwise. [crates/gcode/src/commands/codewiki/render/common.rs:1-7] |
| [[code/files/crates/gcode/src/commands/codewiki/render/diagrams.rs\|crates/gcode/src/commands/codewiki/render/diagrams.rs]] | Builds Mermaid diagrams for the codewiki’s dependency views. It collects import and dependency edges from `FileDoc` and `CodewikiGraphEdge` data, aggregates endpoints relative to the current page/module, and then renders bounded module, subsystem, architecture, and call graphs with truncation notes and partial-graph comments when edges are omitted. Helper functions handle edge collection, neighborhood filtering, module aggregation, and Mermaid-safe node IDs and labels so the diagrams stay readable and scoped to the page being rendered. [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67] [crates/gcode/src/commands/codewiki/render/diagrams.rs:72-92] [crates/gcode/src/commands/codewiki/render/diagrams.rs:97-127] [crates/gcode/src/commands/codewiki/render/diagrams.rs:131-166] [crates/gcode/src/commands/codewiki/render/diagrams.rs:170-197] |
| [[code/files/crates/gcode/src/commands/codewiki/render/overview.rs\|crates/gcode/src/commands/codewiki/render/overview.rs]] | Builds overview-style CodeWiki pages from structured docs data. `render_architecture_doc` emits an “Architecture Overview” page with frontmatter, relevant source-file references, an optional narrative section, an optional subsystem map diagram, and a subsystem table. `render_onboarding_doc` produces a “Start Here” page with frontmatter, source references, entry points, and a reading-order section or fallback content. `render_hotspots_doc` generates a hotspot-focused overview, while `write_hotspot_section` and `write_hotspot_section_with_cross_refs` handle section formatting, with the latter adding cross-referenced links when available. Together these functions turn architecture, onboarding, and hotspot metadata into consistent markdown documentation. [crates/gcode/src/commands/codewiki/render/overview.rs:5-48] [crates/gcode/src/commands/codewiki/render/overview.rs:50-87] [crates/gcode/src/commands/codewiki/render/overview.rs:89-133] [crates/gcode/src/commands/codewiki/render/overview.rs:135-137] [crates/gcode/src/commands/codewiki/render/overview.rs:139-198] |
| [[code/files/crates/gcode/src/commands/codewiki/render/pages.rs\|crates/gcode/src/commands/codewiki/render/pages.rs]] | Builds CodeWiki page text for module and file documentation. `render_module_doc` assembles a module page with frontmatter, linked source files, headings, parent navigation, summary, dependency and call diagrams, and tables for child modules and direct files, while `render_file_doc` does the same for a single file by combining its metadata, source context, summary, and related links into the final markdown output. [crates/gcode/src/commands/codewiki/render/pages.rs:6-72] [crates/gcode/src/commands/codewiki/render/pages.rs:74-133] |
| [[code/files/crates/gcode/src/commands/codewiki/render/repo.rs\|crates/gcode/src/commands/codewiki/render/repo.rs]] | Builds and renders the repository-level Codewiki overview. `build_repo_doc` collects top-level modules and root files, assembles summaries and source spans, reuses a cached page when the repo’s provenance is unchanged, otherwise generates the overview from a repo prompt and source excerpts. `repo_source_excerpts` gathers the source snippets fed into that prompt, and `render_repo_doc` turns the resulting document into the final rendered repo page. [crates/gcode/src/commands/codewiki/render/repo.rs:5-91] [crates/gcode/src/commands/codewiki/render/repo.rs:96-116] [crates/gcode/src/commands/codewiki/render/repo.rs:118-172] |

## Components

| Component ID |
| --- |
| `6fa7713c-5f00-5792-ac68-bd5c6ce05b1c` |
| `549d1ee2-6881-510c-889e-6f62e3a56159` |
| `e0e523a6-4d26-5dd5-87e5-fb3099346e6b` |
| `7abed7bd-189b-5b96-a2c2-d12fb67d97ce` |
| `ab0d093d-2922-55dd-b759-cc630c6013f5` |
| `0d99cf3d-e3ee-5f9d-b6d3-56325251a67d` |
| `9a025a96-c200-5993-8bae-aee3ac714b8f` |
| `f70327f9-ec20-58fb-87f3-4babd83c46db` |
| `e96d176e-b4fb-52d6-9228-80a5570e698e` |
| `abbe7d47-fea3-59d6-893d-dc337f545c9e` |
| `b9fc8168-3f2d-50bc-b90f-ea84514c8aca` |
| `7724626b-c47f-590b-a684-0282aea1d92d` |
| `dcd7f0d2-4e32-5ef4-a773-f0ad9d774f7d` |
| `942443b2-6fa9-5c4b-a7ee-d605313eeadb` |
| `c908a55b-f241-5d1e-9501-64d550859042` |
| `54e86679-7d53-58cb-8430-d15cfb472c97` |
| `9055f41d-9291-589f-81e2-67eb4dd8c5c0` |
| `d22c8fd8-bb60-5958-863e-2d063d3647aa` |
| `cc1bb07f-5aba-5f10-a929-6c336ad5df56` |
| `f0d9401d-3375-57b8-9edd-fb7a0f363193` |
| `1b8187f4-6e9a-5ef2-8abf-135f44de6a76` |
| `4054dafa-79aa-5928-8d06-3cb6d27221a4` |
| `4e5c8df9-7942-5e59-a2f5-1aac2dc17fad` |
| `d7299570-8cf6-5084-8a99-8973bda5f280` |
| `5bac84e0-5092-5474-ac4d-91d656324116` |
