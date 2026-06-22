---
title: crates/gwiki/src/graph/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/graph/mod.rs` exposes 59 indexed API symbols.

## How it fits

`crates/gwiki/src/graph/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiGraphDocument` | class | The 'WikiGraphDocument' struct represents a wiki graph document, containing its search scope, filesystem path, and an optional title. [crates/gwiki/src/graph/mod.rs:22-26] |
| `WikiGraphSource` | class | The 'WikiGraphSource' struct represents a data source configuration containing a search scope and filesystem paths for both the source directory and document output. [crates/gwiki/src/graph/mod.rs:29-33] |
| `WikiGraphLinkTarget` | type | Indexed type `WikiGraphLinkTarget` in `crates/gwiki/src/graph/mod.rs`. [crates/gwiki/src/graph/mod.rs:36-39] |
| `WikiGraphLink` | class | The 'WikiGraphLink' struct represents a link within a wiki graph, containing its associated search scope, source file path, raw target string, and resolved link target representation. [crates/gwiki/src/graph/mod.rs:42-47] |
| `WikiGraphCodeEdge` | class | 'WikiGraphCodeEdge' is a Rust structure representing a directed, typed connection between code elements within a wiki graph, capturing the relationship's source, target, and orientation alongside metadata for search scope, source file path, line number, and provenance. [crates/gwiki/src/graph/mod.rs:50-59] |
| `WikiGraphFacts` | class | The 'WikiGraphFacts' struct aggregates vectors of wiki documents, links, sources, and code edges, acting as a data container for the entities and relationships of a wiki-based graph. [crates/gwiki/src/graph/mod.rs:62-67] |
| `GraphExportOptions` | class | The 'GraphExportOptions' struct represents the configuration options for exporting a graph, specifically containing a vector of strings that identifies degraded data sources. [crates/gwiki/src/graph/mod.rs:70-72] |
| `GraphExportOptions::available` | method | The 'available' method is a public constructor that returns an instance of the implementing type by delegating to its 'Default' trait implementation. [crates/gwiki/src/graph/mod.rs:75-77] |
| `GraphExportOptions::degraded` | method | This method is a public constructor that instantiates and returns a new instance of the struct by initializing its 'degraded_sources' field with the provided vector of strings. [crates/gwiki/src/graph/mod.rs:79-81] |
| `GraphExport` | class | The 'GraphExport' struct represents an exported representation of a graph, encapsulating its nodes and edges, analytical metrics, the generating command, and its degradation state along with any degraded sources. [crates/gwiki/src/graph/mod.rs:85-92] |
| `GraphExportNode` | class | 'GraphExportNode' is a Rust struct designed to represent a graph node for serialization and export, containing fields for its unique identifier, static and scope-specific kinds, scope identifier, path, and an optional, conditionally serialized title. [crates/gwiki/src/graph/mod.rs:95-103] |
| `GraphExportEdges` | class | The 'GraphExportEdges' struct aggregates various categories of exportable graph connections—specifically links, imports, calls, callers, trust, and audit relationships—each represented as a vector of 'GraphExportEdge' objects. [crates/gwiki/src/graph/mod.rs:106-113] |
| `GraphExportEdge` | class | The 'GraphExportEdge' struct represents a serializable graph edge, containing 'String' fields for its 'source' and 'target' node identifiers, a static string slice defining its 'kind', and an optional, conditionally serialized 'raw_target' identifier. [crates/gwiki/src/graph/mod.rs:116-122] |
| `GraphStatement` | class | 'GraphStatement' is a public Rust structure that encapsulates a graph database query represented as a Cypher query string. [crates/gwiki/src/graph/mod.rs:125-127] |
| `WikiBacklink` | class | The 'WikiBacklink' struct represents a link reference from a source wiki page to a target destination, encapsulating its search scope, source and target file paths, and the original raw target string. [crates/gwiki/src/graph/mod.rs:130-135] |
| `LinkSuggestion` | class | The 'LinkSuggestion' struct represents a proposed link target within a specific search scope, containing the target identifier, a count of its mentions, and the file paths of the sources referencing it. [crates/gwiki/src/graph/mod.rs:138-143] |
| `RelatedPathOptions` | class | The 'RelatedPathOptions' public struct is a configuration options container that defines the weight of backward links in path calculations using a 64-bit floating-point value. [crates/gwiki/src/graph/mod.rs:146-148] |
| `RelatedPathOptions::default` | method | The 'default' method instantiates the implementing type by initializing its 'backward_link_weight' field with the value of the 'BACKWARD_LINK_WEIGHT' constant. [crates/gwiki/src/graph/mod.rs:151-155] |
| `graph_write_statements` | function | This function converts wiki graph facts into a vector of Cypher-based graph statements that merge document nodes and create directed relationships between them based on resolved or unresolved link targets. [crates/gwiki/src/graph/mod.rs:158-239] |
| `MemoryWikiGraph` | class | The 'MemoryWikiGraph' struct represents a wiki graph that encapsulates factual data of type 'WikiGraphFacts'. [crates/gwiki/src/graph/mod.rs:242-244] |
| `MemoryWikiGraph::replace_facts` | method | The 'replace_facts' method mutably updates the struct's internal 'facts' field by replacing its current value with the provided 'WikiGraphFacts' instance. [crates/gwiki/src/graph/mod.rs:247-249] |
| `MemoryWikiGraph::backlinks` | method | The 'backlinks' method queries the internal links collection to retrieve and return a list of valid, resolved links within a specified search scope that point to the given target path, sorted lexicographically by their source document path. [crates/gwiki/src/graph/mod.rs:256-290] |
| `MemoryWikiGraph::link_suggestions` | method | The 'link_suggestions' method filters unresolved wiki-graph links by a specified search scope, aggregates their mention counts and unique source paths grouped by target, and returns a list of suggestions truncated to 'limit' and sorted descending by mention count and then lexicographically by target. [crates/gwiki/src/graph/mod.rs:292-334] |
| `MemoryWikiGraph::Accumulator` | class | The 'Accumulator' struct aggregates an integer count alongside an ordered, unique set of filesystem paths representing the sources of the accumulated data. [crates/gwiki/src/graph/mod.rs:298-301] |

_28 more symbol(s) not shown — run `gcode outline crates/gwiki/src/graph/mod.rs` for the full list._

_Verified by 7 in-file unit tests._

