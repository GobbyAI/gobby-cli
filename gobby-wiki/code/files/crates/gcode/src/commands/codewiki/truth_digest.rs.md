---
title: crates/gcode/src/commands/codewiki/truth_digest.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/truth_digest.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/truth_digest.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/truth_digest.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/truth_digest.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_truth_digest` | function | # Summary Constructs a 'CodewikiTruthDigest' by extracting infrastructure service boundaries from a 'SystemModel' into bounded metadata entries, sorting them by service name, computing key path mappings and stack authority status, and combining them with project metadata and repository statistics. [crates/gcode/src/commands/codewiki/truth_digest.rs:22-74] |
| `write_truth_digest` | function | Writes a CodewikiTruthDigest as JSON-serialized content to a metadata file in the output directory, but only if the document scope is unscoped. [crates/gcode/src/commands/codewiki/truth_digest.rs:76-86] |
| `bounded` | function | This function returns a trimmed string either unchanged (if ≤ 'max_chars' characters) or truncated to 'max_chars - 3' characters with "..." appended. [crates/gcode/src/commands/codewiki/truth_digest.rs:88-97] |

