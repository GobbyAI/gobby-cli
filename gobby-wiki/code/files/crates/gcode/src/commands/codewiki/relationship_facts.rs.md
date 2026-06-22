---
title: crates/gcode/src/commands/codewiki/relationship_facts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/relationship_facts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/relationship_facts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/relationship_facts.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/relationship_facts.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SymbolRelation` | class | 'SymbolRelation' is a crate-visible record describing a symbol graph edge by storing the remote endpoint’s qualified name and kind, the optional local symbol name for call edges, and a citable 'SourceSpan' for the remote endpoint. [crates/gcode/src/commands/codewiki/relationship_facts.rs:29-41] |
| `SymbolRelation::citation` | method | Returns the citation string for 'self' by delegating directly to 'self.span.citation()'. [crates/gcode/src/commands/codewiki/relationship_facts.rs:46-48] |
| `RelationshipFacts` | class | 'RelationshipFacts' is an internal struct that aggregates symbol-relationship metadata for a file, tracking inbound calls from external symbols, outbound calls to external symbols, and imported files as 'SymbolRelation' lists. [crates/gcode/src/commands/codewiki/relationship_facts.rs:53-60] |
| `RelationshipFacts::is_empty` | method | Returns 'true' only when all three collections, 'inbound_calls', 'outbound_calls', and 'imports', are empty. [crates/gcode/src/commands/codewiki/relationship_facts.rs:63-65] |
| `RelationshipFacts::endpoint_spans` | method | Returns a 'Vec<SourceSpan>' containing the cloned 'span' of every relation in 'inbound_calls', 'outbound_calls', and 'imports', in that iteration order. [crates/gcode/src/commands/codewiki/relationship_facts.rs:72-79] |
| `RelationshipFacts::neighbor_files` | method | The 'neighbor_files' method retrieves the unique file paths associated with the instance's endpoint spans, excluding the specified 'own_file', and returns them as a sorted 'BTreeSet<String>'. [crates/gcode/src/commands/codewiki/relationship_facts.rs:86-92] |
| `relationship_facts_for_file` | function | The function processes a slice of graph edges to construct and return a 'RelationshipFacts' struct containing inbound calls, outbound calls, and file-level imports for a specific file by determining if the source or target symbol IDs of each edge belong to that file's set of local symbol IDs. [crates/gcode/src/commands/codewiki/relationship_facts.rs:100-154] |
| `call_relation` | function | The 'call_relation' function resolves and returns a cross-file 'SymbolRelation' between an optional local symbol and a target symbol retrieved by their IDs, returning 'None' if the target symbol is missing or located within the specified file. [crates/gcode/src/commands/codewiki/relationship_facts.rs:160-179] |
| `import_relation` | function | The 'import_relation' function retrieves a target symbol by its identifier from a hash map and returns a 'SymbolRelation' of kind 'import' containing the target's file path and source span if the symbol exists and is located in a different file than the one specified, returning 'None' otherwise. [crates/gcode/src/commands/codewiki/relationship_facts.rs:183-198] |
| `bound_relations` | function | This function sorts a vector of 'SymbolRelation' structures by their span, other name, and local name, removes duplicate elements, and truncates the vector to a maximum length of 'MAX_RELATIONS_PER_DIRECTION'. [crates/gcode/src/commands/codewiki/relationship_facts.rs:203-215] |
| `symbol` | function | The 'symbol' function constructs and returns a 'Symbol' struct by mapping the provided string slice and size parameters to their corresponding fields while initializing other fields to hardcoded defaults or empty values. [crates/gcode/src/commands/codewiki/relationship_facts.rs:221-249] |
| `id_set` | function | The 'id_set' function takes a slice of string slices with lifetime ''a' and collects them into a 'HashSet' of string slices with the same lifetime by copying the references. [crates/gcode/src/commands/codewiki/relationship_facts.rs:251-253] |
| `by_id` | function | The 'by_id' function borrows a slice of 'Symbol' structs and collects them into a 'HashMap' mapping each symbol's string slice identifier to its corresponding reference. [crates/gcode/src/commands/codewiki/relationship_facts.rs:255-257] |

_Verified by 4 in-file unit tests._

