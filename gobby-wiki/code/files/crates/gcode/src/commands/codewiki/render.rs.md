---
title: crates/gcode/src/commands/codewiki/render.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The file `crates/gcode/src/commands/codewiki/render.rs` is a module entry point that coordinates the rendering of a codebase wiki. It defines several submodules on lines 1-5, including `common`, `diagrams`, `overview`, `pages`, and `repo`.

It exposes functions to render structured overview documents such as onboarding guides, hotspots analysis, and architecture overviews on line 15. Additionally, it handles rendering documentation for specific files and modules as shown on line 16, and orchestrates building the overall repository documentation on line 17.

The file also manages the generation of visual architecture maps. On lines 9-14, it re-exports functions that collect subsystem dependencies and render Mermaid diagrams for module calls, module dependencies, subsystem dependencies, and the broader architectural structure.

## How it fits

This file acts as a central facade for the rendering engine of the `codewiki` command within the `gcode` crate. By re-exporting internal submodule functions as `pub(crate)` on lines 7-17, it provides a clean, unified API for other components of the `gcode` tool to generate wiki documentation without needing to interact with individual rendering submodules directly. [crates/gcode/src/commands/codewiki/render.rs:1-18]

## Key components

No indexed symbols.
