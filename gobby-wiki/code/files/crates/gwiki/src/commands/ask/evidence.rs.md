---
title: crates/gwiki/src/commands/ask/evidence.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/evidence.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/evidence.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Overview

`crates/gwiki/src/commands/ask/evidence.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/ask/evidence.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `estimate_tokens` | function | Returns the ceiling of 'chars / 4', estimating token count by rounding any nonzero remainder up to the next whole token. [crates/gwiki/src/commands/ask/evidence.rs:14-16] |
| `EvidencePlan` | class | 'EvidencePlan' is a package-private struct that aggregates evidence-candidate outputs, their textual excerpts, the generated prompt, an estimated prompt token count, and the number of dropped hits. [crates/gwiki/src/commands/ask/evidence.rs:20-26] |
| `plan_evidence` | function | Constructs an 'EvidencePlan' by formatting the query and ranked retrieval hits into a prompt with bounded excerpt windows, tracking included wiki/source items and estimated token usage, and stopping at the first hit that would exceed the prompt budget while recording how many lower-ranked hits were dropped. [crates/gwiki/src/commands/ask/evidence.rs:31-83] |
| `retrieval_with_bodies` | function | Constructs a 'SearchRetrieval' whose 'SearchOutput' contains one wiki 'SearchResultOutput' per input body with synthetic hit metadata, descending scores, and 'evidence' set to the original 'bodies' vector. [crates/gwiki/src/commands/ask/evidence.rs:95-121] |

_Verified by 3 in-file unit tests._

