---
title: crates/gcode/src/commands/codewiki/build.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/build.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

By consolidating these modules, the file re-exports specialized functions designed to build specific documentation segments, as shown in `crates/gcode/src/commands/codewiki/build.rs:21-30`. These builder functions facilitate the generation of structured content such as onboarding guides, module documentation, hotspots, and architecture overviews.

## How it fits

Additionally, the file defines structural modularity by mapping the submodules to distinct physical files using path attributes, as declared in `crates/gcode/src/commands/codewiki/build.rs:1-19`. This separation of concerns allows developers to manage individual document builders in isolated files while maintaining a single, clean API boundary in this module for the broader `codewiki` command operations. [crates/gcode/src/commands/codewiki/build.rs:1-30]

## Key components

No indexed symbols.
