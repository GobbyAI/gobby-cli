---
title: crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `InfraDescriptor` | class | The 'InfraDescriptor' struct is a metadata container representing an infrastructure service by storing a plain-text summary of the service, a validated workspace-relative path and line citation for its adapter module, and its documented graceful-degradation behavior when unavailable. [crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs:8-20] |
| `infra_descriptor` | function | The 'infra_descriptor' function maps a specified 'ServiceKind' to an optional 'InfraDescriptor' containing technical metadata, the adapter module path, and degradation behavior for the corresponding infrastructure service. [crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs:27-113] |
| `build_infrastructure_doc` | function | This function maps services from an optional 'SystemModel' into lexicographically sorted 'InfraSection' structures based on their respective infrastructure descriptors, returning an 'InfrastructureDoc' containing these sections and an empty list of degraded sources. [crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs:121-148] |

