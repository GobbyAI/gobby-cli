---
title: crates/gcode/src/commands/codewiki/render/overview.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/overview.rs
  ranges:
  - 5-48
  - 50-87
  - 89-133
  - 135-137
  - 139-198
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/render/overview.rs:5-48](crates/gcode/src/commands/codewiki/render/overview.rs#L5-L48), [crates/gcode/src/commands/codewiki/render/overview.rs:50-87](crates/gcode/src/commands/codewiki/render/overview.rs#L50-L87), [crates/gcode/src/commands/codewiki/render/overview.rs:89-133](crates/gcode/src/commands/codewiki/render/overview.rs#L89-L133), [crates/gcode/src/commands/codewiki/render/overview.rs:135-137](crates/gcode/src/commands/codewiki/render/overview.rs#L135-L137), [crates/gcode/src/commands/codewiki/render/overview.rs:139-198](crates/gcode/src/commands/codewiki/render/overview.rs#L139-L198)

</details>

# crates/gcode/src/commands/codewiki/render/overview.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Purpose

Builds overview-style CodeWiki pages from structured docs data. `render_architecture_doc` emits an “Architecture Overview” page with frontmatter, relevant source-file references, an optional narrative section, an optional subsystem map diagram, and a subsystem table. `render_onboarding_doc` produces a “Start Here” page with frontmatter, source references, entry points, and a reading-order section or fallback content. `render_hotspots_doc` generates a hotspot-focused overview, while `write_hotspot_section` and `write_hotspot_section_with_cross_refs` handle section formatting, with the latter adding cross-referenced links when available. Together these functions turn architecture, onboarding, and hotspot metadata into consistent markdown documentation.
[crates/gcode/src/commands/codewiki/render/overview.rs:5-48]
[crates/gcode/src/commands/codewiki/render/overview.rs:50-87]
[crates/gcode/src/commands/codewiki/render/overview.rs:89-133]
[crates/gcode/src/commands/codewiki/render/overview.rs:135-137]
[crates/gcode/src/commands/codewiki/render/overview.rs:139-198]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_architecture_doc` | function | `pub(crate) fn render_architecture_doc(architecture: &ArchitectureDoc) -> String {` | `render_architecture_doc [function]` | `54e86679-7d53-58cb-8430-d15cfb472c97` | 5-48 [crates/gcode/src/commands/codewiki/render/overview.rs:5-48] | Indexed function `render_architecture_doc` in `crates/gcode/src/commands/codewiki/render/overview.rs`. [crates/gcode/src/commands/codewiki/render/overview.rs:5-48] |
| `render_onboarding_doc` | function | `pub(crate) fn render_onboarding_doc(onboarding: &OnboardingDoc) -> String {` | `render_onboarding_doc [function]` | `9055f41d-9291-589f-81e2-67eb4dd8c5c0` | 50-87 [crates/gcode/src/commands/codewiki/render/overview.rs:50-87] | Indexed function `render_onboarding_doc` in `crates/gcode/src/commands/codewiki/render/overview.rs`. [crates/gcode/src/commands/codewiki/render/overview.rs:50-87] |
| `render_hotspots_doc` | function | `pub(crate) fn render_hotspots_doc(hotspots: &HotspotsDoc) -> String {` | `render_hotspots_doc [function]` | `d22c8fd8-bb60-5958-863e-2d063d3647aa` | 89-133 [crates/gcode/src/commands/codewiki/render/overview.rs:89-133] | Indexed function `render_hotspots_doc` in `crates/gcode/src/commands/codewiki/render/overview.rs`. [crates/gcode/src/commands/codewiki/render/overview.rs:89-133] |
| `write_hotspot_section` | function | `fn write_hotspot_section(doc: &mut String, title: &str, findings: &[HotspotFinding]) {` | `write_hotspot_section [function]` | `cc1bb07f-5aba-5f10-a929-6c336ad5df56` | 135-137 [crates/gcode/src/commands/codewiki/render/overview.rs:135-137] | Indexed function `write_hotspot_section` in `crates/gcode/src/commands/codewiki/render/overview.rs`. [crates/gcode/src/commands/codewiki/render/overview.rs:135-137] |
| `write_hotspot_section_with_cross_refs` | function | `fn write_hotspot_section_with_cross_refs(` | `write_hotspot_section_with_cross_refs [function]` | `f0d9401d-3375-57b8-9edd-fb7a0f363193` | 139-198 [crates/gcode/src/commands/codewiki/render/overview.rs:139-198] | Indexed function `write_hotspot_section_with_cross_refs` in `crates/gcode/src/commands/codewiki/render/overview.rs`. [crates/gcode/src/commands/codewiki/render/overview.rs:139-198] |
