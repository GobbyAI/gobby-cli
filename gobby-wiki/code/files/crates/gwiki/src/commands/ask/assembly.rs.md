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

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Overview

`crates/gwiki/src/commands/ask/assembly.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/ask/assembly.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ask_output_from_retrieval` | function | Constructs an 'AskOutput' from a 'SearchOutput' and 'EvidencePlan' by extracting unique sources, organizing evidence and degradations, setting retrieval status based on result availability, and marking truncation when hits were dropped. [crates/gwiki/src/commands/ask/assembly.rs:6-40] |
| `unique_sources` | function | Extracts all unique source file paths and source identifiers from search results and returns them as a sorted vector of strings. [crates/gwiki/src/commands/ask/assembly.rs:42-51] |
| `ordered_unique_strings` | function | This function deduplicates a string vector while preserving the original order of first occurrences by filtering with a BTreeSet that tracks seen values. [crates/gwiki/src/commands/ask/assembly.rs:53-59] |

_Verified by 1 in-file unit test._

