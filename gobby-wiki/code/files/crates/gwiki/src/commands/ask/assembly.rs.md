---
title: crates/gwiki/src/commands/ask/assembly.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/assembly.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/assembly.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/ask/assembly.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/ask/assembly.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ask_output_from_retrieval` | function | Constructs an 'AskOutput' from retrieval 'SearchOutput' and an 'EvidencePlan' by deduplicating sources and degradations, setting retrieval status/truncation flags, copying hits/code citations/evidence, and initializing prompt-budget and AI/synthesis fields to defaults. [crates/gwiki/src/commands/ask/assembly.rs:6-39] |
| `unique_sources` | function | Returns a sorted 'Vec<String>' of all distinct source identifiers from 'search.results', deduplicating both each hit’s 'source_path' and every string in 'hit.sources' via a 'BTreeSet'. [crates/gwiki/src/commands/ask/assembly.rs:41-50] |
| `ordered_unique_strings` | function | Returns the input 'Vec<String>' with duplicates removed while preserving the first occurrence order, using a 'BTreeSet' to track previously seen strings. [crates/gwiki/src/commands/ask/assembly.rs:52-58] |

_Verified by 1 in-file unit test._

