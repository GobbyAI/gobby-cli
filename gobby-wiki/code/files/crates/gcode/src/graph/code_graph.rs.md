---
title: crates/gcode/src/graph/code_graph.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/graph/code_graph.rs

Module: [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]

## Overview

This file serves as the central module definition and public API gateway for the code graph functionality in the `gcode` crate. It declares internal submodules for connection, lifecycle, payload, read, write, and testing behaviors, establishing a clean interface for graph interactions.
Supporting source: crates/gcode/src/graph/code_graph.rs:1-7

The module exposes structured data types representing the graph elements and metadata. These include payload elements such as nodes, links, and blast radius targets.
Supporting source: crates/gcode/src/graph/code_graph.rs:15-18

It also exports comprehensive read capabilities to query relationships in the codebase, such as counting callers, tracking usages, finding callees, and computing symbol paths.
Supporting source: crates/gcode/src/graph/code_graph.rs:19-25

Additionally, it provides write capabilities to manage and mutate the code graph. These include synchronization of file graphs, clearing indexes, and cleaning up orphan nodes.
Supporting source: crates/gcode/src/graph/code_graph.rs:26-31

## How it fits

This file integrates the underlying submodules to expose unified code graph management to the broader project. It exposes lifecycle demands, error types, and daemon configurations required to connect and interact with code graph backends.
Supporting source: crates/gcode/src/graph/code_graph.rs:9-14

By defining the external read functions, the module enables features like finding imports, calculating blast radiuses, and retrieving project overview graphs to be called by other system components.
Supporting source: crates/gcode/src/graph/code_graph.rs:19-25 [crates/gcode/src/graph/code_graph.rs:1-51]

## Key components

No indexed symbols.
