---
title: crates/gwiki/src/graph/context.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/context.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/graph/context.rs` exposes 35 indexed API symbols.

## How it fits

`crates/gwiki/src/graph/context.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphContextOptions` | class | 'GraphContextOptions' is a configuration struct that contains vectors of strings representing degraded sources and truncated components. [crates/gwiki/src/graph/context.rs:8-11] |
| `GraphContextOptions::available` | method | The 'available' method is a public constructor that instantiates and returns a default instance of the type by calling its 'Default' implementation. [crates/gwiki/src/graph/context.rs:14-16] |
| `GraphContextOptions::degraded` | method | Constructs an instance of the type by initializing the 'degraded_sources' field with the provided vector of strings and the 'truncated_components' field with an empty vector. [crates/gwiki/src/graph/context.rs:18-23] |
| `GraphContextOptions::with_truncated_components` | method | This builder-pattern method consumes 'self' by value, sets its 'truncated_components' field to the provided vector of strings, and returns the updated instance. [crates/gwiki/src/graph/context.rs:25-28] |
| `GraphContextPack` | class | 'GraphContextPack' is a Rust struct that aggregates graph query context data, packaging an execution command, scope and degradation details, and collections of warnings, localized neighborhood subgraphs, and generated recommendations. [crates/gwiki/src/graph/context.rs:32-39] |
| `GraphContextScope` | class | 'GraphContextScope' is a public Rust structure containing public 'kind' and 'id' string fields used to define and identify a specific context scope within a graph. [crates/gwiki/src/graph/context.rs:42-45] |
| `GraphContextDegradation` | class | 'GraphContextDegradation' is a status struct that records whether graph context has been degraded or truncated, along with the specific source and component identifiers affected in each case. [crates/gwiki/src/graph/context.rs:48-53] |
| `GraphContextWarning` | class | The 'GraphContextWarning' struct represents a warning within a graph context, containing a static string slice identifying the warning kind, a string message, and an optional string path that is omitted from serialization when it is 'None'. [crates/gwiki/src/graph/context.rs:56-61] |
| `GraphContextNeighborhood` | class | The 'GraphContextNeighborhood' struct represents the localized graph context of a file, encapsulating its path, optional title, adjacent nodes, documentation links, citations, and code dependency edges for function calls and module imports. [crates/gwiki/src/graph/context.rs:64-73] |
| `GraphContextNeighbor` | class | The 'GraphContextNeighbor' struct represents a neighboring vertex within a graph context, specifying its source file path, relationship direction, and raw target identifier. [crates/gwiki/src/graph/context.rs:76-80] |
| `GraphContextDocLink` | class | 'GraphContextDocLink' is a public Rust struct representing a document link in a graph context, containing string fields for the link's source, resolved target, and raw target, along with a static string slice indicating its status. [crates/gwiki/src/graph/context.rs:83-88] |
| `GraphContextCodeEdge` | class | The 'GraphContextCodeEdge' struct represents a directed relationship within a code context graph, containing fields for source and target node identifiers, relationship kind and direction, an optional line number, and provenance metadata. [crates/gwiki/src/graph/context.rs:91-99] |
| `GraphContextRecommendation` | class | The 'GraphContextRecommendation' struct represents a recommended file or node path within a graph context, paired with a textual justification explaining the reason for the recommendation. [crates/gwiki/src/graph/context.rs:102-105] |
| `build_context_pack` | function | The 'build_context_pack' function compiles a 'GraphContextPack' by analyzing 'WikiGraphFacts' and 'GraphContextOptions' to aggregate document scopes, degradation states, validation warnings, recommendations, and localized neighborhood graph data for each document. [crates/gwiki/src/graph/context.rs:107-153] |
| `context_scope` | function | The 'context_scope' function resolves and returns a 'GraphContextScope' by extracting the scope identifier and kind from the first available document, link, or source in the provided 'WikiGraphFacts', defaulting to an 'unknown' project scope if all lists are empty. [crates/gwiki/src/graph/context.rs:155-172] |
| `citations_by_document` | function | The 'citations_by_document' function aggregates sources from the provided 'WikiGraphFacts' into a 'BTreeMap' that maps each document's path to a sorted 'BTreeSet' of its associated formatted source paths. [crates/gwiki/src/graph/context.rs:174-183] |
| `degradation_warnings` | function | The 'degradation_warnings' function maps a slice of degraded source strings to a vector of 'GraphContextWarning' structs of kind "degradation", generating a specialized capped graph warning if the source represents a truncated shared code graph, or an unavailability message otherwise. [crates/gwiki/src/graph/context.rs:185-201] |
| `capped_graph_warning` | function | This function returns a warning message indicating that the shared code graph was capped, optionally appending a comma-separated list of the specified truncated components if any are provided. [crates/gwiki/src/graph/context.rs:203-212] |
| `stale_link_warnings` | function | The 'stale_link_warnings' function processes a set of wiki graph facts by filtering its links for unresolved targets and mapping each into a 'GraphContextWarning' struct of kind 'stale' containing the target's name and the source path. [crates/gwiki/src/graph/context.rs:214-227] |
| `audit_warnings` | function | The 'audit_warnings' function identifies document paths in 'document_titles' that are not present as keys in 'citations_by_doc' and returns a vector of 'GraphContextWarning' structs indicating that these documents lack source citations in the wiki index. [crates/gwiki/src/graph/context.rs:229-242] |
| `neighbors_for_path` | function | This function identifies all resolved incoming and outgoing neighbors for a specified graph path from the provided 'WikiGraphFacts', returning them as a vector of 'GraphContextNeighbor' structs sorted lexicographically by their path, direction, and raw target. [crates/gwiki/src/graph/context.rs:244-272] |
| `doc_links_for_path` | function | The 'doc_links_for_path' function retrieves, formats, and returns a sorted list of all outgoing and incoming document links associated with a specified path from the given wiki graph facts. [crates/gwiki/src/graph/context.rs:274-311] |
| `code_calls_for_path` | function | The function filters 'WikiGraphFacts' code edges to retrieve those matching the specified 'Path' with a type other than "imports", maps them via 'graph_context_code_edge', and returns the result as a collected vector of 'GraphContextCodeEdge'. [crates/gwiki/src/graph/context.rs:313-320] |
| `code_imports_for_path` | function | The 'code_imports_for_path' function filters code edges within a 'WikiGraphFacts' instance to locate import relationships associated with the specified file path, mapping and returning them as a vector of 'GraphContextCodeEdge' objects. [crates/gwiki/src/graph/context.rs:322-329] |

_8 more symbol(s) not shown — run `gcode outline crates/gwiki/src/graph/context.rs` for the full list._

_Verified by 3 in-file unit tests._

