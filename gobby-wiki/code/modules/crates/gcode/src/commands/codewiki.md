---
title: crates/gcode/src/commands/codewiki
type: code_module
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
- file: crates/gcode/src/commands/codewiki/prompts/builders.rs
- file: crates/gcode/src/commands/codewiki/prompts/tests.rs
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
- file: crates/gcode/src/commands/codewiki/text/verify.rs
- file: crates/gcode/src/commands/codewiki/types.rs
provenance_truncated: 32
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki

Parent: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/codewiki` contains 24 direct files and 5 child modules.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-24]
[crates/gcode/src/commands/codewiki/architecture_diagrams.rs:40-81]
[crates/gcode/src/commands/codewiki/build.rs:1-39]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170]
[crates/gcode/src/commands/codewiki/build_parts/audit.rs:28-34]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/commands/codewiki/build_parts\|crates/gcode/src/commands/codewiki/build_parts]] | `crates/gcode/src/commands/codewiki/build_parts` contains 12 direct files and 1 child module. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170] [crates/gcode/src/commands/codewiki/build_parts/audit.rs:28-34] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85] [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38] |
| [[code/modules/crates/gcode/src/commands/codewiki/ownership\|crates/gcode/src/commands/codewiki/ownership]] | `crates/gcode/src/commands/codewiki/ownership` contains 4 direct files and 0 child modules. [crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21] [crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7] [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34] [crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35] [crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87] |
| [[code/modules/crates/gcode/src/commands/codewiki/prompts\|crates/gcode/src/commands/codewiki/prompts]] | `crates/gcode/src/commands/codewiki/prompts` contains 6 direct files and 0 child modules. [crates/gcode/src/commands/codewiki/prompts/builders.rs:24-39] [crates/gcode/src/commands/codewiki/prompts/excerpts.rs:5-7] [crates/gcode/src/commands/codewiki/prompts/systems.rs:1-25] [crates/gcode/src/commands/codewiki/prompts/tables.rs:6-18] [crates/gcode/src/commands/codewiki/prompts/tests.rs:5-9] |
| [[code/modules/crates/gcode/src/commands/codewiki/render\|crates/gcode/src/commands/codewiki/render]] | `crates/gcode/src/commands/codewiki/render` contains 8 direct files and 0 child modules. [crates/gcode/src/commands/codewiki/render/audit.rs:8-57] [crates/gcode/src/commands/codewiki/render/common.rs:1-7] [crates/gcode/src/commands/codewiki/render/diagrams.rs:7-34] [crates/gcode/src/commands/codewiki/render/features.rs:11-73] [crates/gcode/src/commands/codewiki/render/infrastructure.rs:10-43] |
| [[code/modules/crates/gcode/src/commands/codewiki/text\|crates/gcode/src/commands/codewiki/text]] | `crates/gcode/src/commands/codewiki/text` contains 6 direct files and 0 child modules. [crates/gcode/src/commands/codewiki/text/citations.rs:26-34] [crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-23] [crates/gcode/src/commands/codewiki/text/generation.rs:28-39] [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10] [crates/gcode/src/commands/codewiki/text/structural.rs:7-22] |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/architecture_diagrams.rs\|crates/gcode/src/commands/codewiki/architecture_diagrams.rs]] | `crates/gcode/src/commands/codewiki/architecture_diagrams.rs` exposes 40 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build.rs\|crates/gcode/src/commands/codewiki/build.rs]] | `crates/gcode/src/commands/codewiki/build.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/cluster.rs\|crates/gcode/src/commands/codewiki/cluster.rs]] | `crates/gcode/src/commands/codewiki/cluster.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/generation.rs\|crates/gcode/src/commands/codewiki/generation.rs]] | `crates/gcode/src/commands/codewiki/generation.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/graph.rs\|crates/gcode/src/commands/codewiki/graph.rs]] | `crates/gcode/src/commands/codewiki/graph.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/io.rs\|crates/gcode/src/commands/codewiki/io.rs]] | `crates/gcode/src/commands/codewiki/io.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/mod.rs\|crates/gcode/src/commands/codewiki/mod.rs]] | `crates/gcode/src/commands/codewiki/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership.rs\|crates/gcode/src/commands/codewiki/ownership.rs]] | `crates/gcode/src/commands/codewiki/ownership.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/analysis.rs\|crates/gcode/src/commands/codewiki/ownership/analysis.rs]] | `crates/gcode/src/commands/codewiki/ownership/analysis.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/codeowners.rs\|crates/gcode/src/commands/codewiki/ownership/codeowners.rs]] | `crates/gcode/src/commands/codewiki/ownership/codeowners.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/render.rs\|crates/gcode/src/commands/codewiki/ownership/render.rs]] | `crates/gcode/src/commands/codewiki/ownership/render.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/paths.rs\|crates/gcode/src/commands/codewiki/paths.rs]] | `crates/gcode/src/commands/codewiki/paths.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/progress.rs\|crates/gcode/src/commands/codewiki/progress.rs]] | `crates/gcode/src/commands/codewiki/progress.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/prompts.rs\|crates/gcode/src/commands/codewiki/prompts.rs]] | `crates/gcode/src/commands/codewiki/prompts.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/relationship_facts.rs\|crates/gcode/src/commands/codewiki/relationship_facts.rs]] | `crates/gcode/src/commands/codewiki/relationship_facts.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/render.rs\|crates/gcode/src/commands/codewiki/render.rs]] | `crates/gcode/src/commands/codewiki/render.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/repair.rs\|crates/gcode/src/commands/codewiki/repair.rs]] | `crates/gcode/src/commands/codewiki/repair.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/reuse.rs\|crates/gcode/src/commands/codewiki/reuse.rs]] | `crates/gcode/src/commands/codewiki/reuse.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/run.rs\|crates/gcode/src/commands/codewiki/run.rs]] | `crates/gcode/src/commands/codewiki/run.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/system_model.rs\|crates/gcode/src/commands/codewiki/system_model.rs]] | `crates/gcode/src/commands/codewiki/system_model.rs` exposes 29 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/tests.rs\|crates/gcode/src/commands/codewiki/tests.rs]] | `crates/gcode/src/commands/codewiki/tests.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcode/src/commands/codewiki/text.rs\|crates/gcode/src/commands/codewiki/text.rs]] | `crates/gcode/src/commands/codewiki/text.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/truth_digest.rs\|crates/gcode/src/commands/codewiki/truth_digest.rs]] | `crates/gcode/src/commands/codewiki/truth_digest.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/types.rs\|crates/gcode/src/commands/codewiki/types.rs]] | `crates/gcode/src/commands/codewiki/types.rs` exposes 66 indexed API symbols. |

