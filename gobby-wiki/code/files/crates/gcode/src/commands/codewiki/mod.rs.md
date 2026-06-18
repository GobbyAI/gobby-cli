---
title: crates/gcode/src/commands/codewiki/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/mod.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

This file serves as the module entry point for the codewiki command inside the gcode crate. It defines default paths, constraints, cache versions, and daemon feature profiles used to generate and verify codewiki documentation pages.

The module sets the default output directory to "codewiki" crates/gcode/src/commands/codewiki/mod.rs:8. It designates specific paths for metadata, tracking main metadata at "_meta/codewiki.json" crates/gcode/src/commands/codewiki/mod.rs:9 and file ownership data at "_meta/ownership.json" crates/gcode/src/commands/codewiki/mod.rs:10.

Diagram generation is constrained by specific thresholds. Mermaid diagram hops are capped at a maximum of 2 crates/gcode/src/commands/codewiki/mod.rs:11, with diagram edges limited to 20 crates/gcode/src/commands/codewiki/mod.rs:12, and an overall limit of 100,000 edges crates/gcode/src/commands/codewiki/mod.rs:13.

The file maintains cache validation through the `CODEWIKI_RENDER_VERSION` epoch, set to 6 crates/gcode/src/commands/codewiki/mod.rs:19. This version bump prevents the reuse of outdated disk page shapes, ensuring that file and module pages render with verified narrative bodies and human-readable key components tables.

For AI-assisted content generation, the file defines specific daemon feature profiles. The `DEFAULT_AGGREGATE_PROFILE` uses "feature_mid" crates/gcode/src/commands/codewiki/mod.rs:24 to synthesize massive 10k+-token grounded prompts for high-level module, repository, and architectural prose. In contrast, checking source claims uses the cheaper `DEFAULT_VERIFY_PROFILE` set to "feature_low" crates/gcode/src/commands/codewiki/mod.rs:29.

## How it fits

It exposes high-level document builders from the `build` submodule, making them accessible to other components of gcode. These include builders for file, architecture, onboarding, hotspots, index snapshot, and curated navigation documentation crates/gcode/src/commands/codewiki/mod.rs:49-54.

It also integrates clustering algorithms and import-target resolution by exporting helper functions from the `cluster` submodule crates/gcode/src/commands/codewiki/mod.rs:56-61. These helpers help group symbols by file component and locate source roots. [crates/gcode/src/commands/codewiki/mod.rs:1-100]

## Key components

No indexed symbols.
