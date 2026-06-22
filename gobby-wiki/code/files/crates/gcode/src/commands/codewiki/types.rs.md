---
title: crates/gcode/src/commands/codewiki/types.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/types.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/types.rs` exposes 65 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodewikiInput` | class | The 'CodewikiInput' struct aggregates file paths, dependency graph edges, graph availability, extracted code symbols, and leading file content chunks to serve as the structured input payload for generating aggregate code-wiki prompts. [crates/gcode/src/commands/codewiki/types.rs:11-21] |
| `LeadingChunk` | class | The 'LeadingChunk' struct represents a segment of text content along with its starting and ending line boundaries. [crates/gcode/src/commands/codewiki/types.rs:26-30] |
| `source_excerpt_for_file` | function | This function retrieves a 'LeadingChunk' associated with a specified file path from a map and, if present, maps it to a 'prompts::SourceExcerpt' containing the file path, line boundaries, and cloned chunk content, returned as an 'Option'. [crates/gcode/src/commands/codewiki/types.rs:33-45] |
| `ranked_source_excerpts` | function | This function sorts candidate file documents in descending order of symbol count (with file paths as a tie-breaker), resolves them to source excerpts using a mapping of leading chunks, and returns up to a specified limit of the resolved excerpts. [crates/gcode/src/commands/codewiki/types.rs:50-62] |
| `CodewikiGraphEdge` | class | The 'CodewikiGraphEdge' struct represents a directed relationship of a specific 'CodewikiGraphEdgeKind' connecting a source component to a target component, both identified by their respective string IDs. [crates/gcode/src/commands/codewiki/types.rs:65-69] |
| `CodewikiGraphEdge::call` | method | This constructor instantiates and returns a new graph edge of type 'Self' representing a call relation, converting the provided source and target component identifiers into owned 'String' fields and setting the edge kind to 'CodewikiGraphEdgeKind::Call'. [crates/gcode/src/commands/codewiki/types.rs:72-81] |
| `CodewikiGraphEdge::import` | method | Constructs and returns an instance of the struct representing an import edge between a source component and a target component. [crates/gcode/src/commands/codewiki/types.rs:83-92] |
| `CodewikiGraphEdgeKind` | type | Indexed type `CodewikiGraphEdgeKind` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:96-99] |
| `CodewikiGraph` | class | The 'CodewikiGraph' crate-visible struct represents a graph structure composed of a vector of 'CodewikiGraphEdge' edges and its associated 'CodewikiGraphAvailability' status. [crates/gcode/src/commands/codewiki/types.rs:102-105] |
| `CodewikiGraph::available` | method | The 'available' constructor initializes and returns a new instance of the struct with the specified vector of 'CodewikiGraphEdge' instances and its 'availability' state set to 'CodewikiGraphAvailability::Available'. [crates/gcode/src/commands/codewiki/types.rs:108-113] |
| `CodewikiGraph::truncated` | method | Constructs a new instance of the containing struct with the provided vector of edges and initializes its 'availability' field to 'CodewikiGraphAvailability::Truncated'. [crates/gcode/src/commands/codewiki/types.rs:115-120] |
| `CodewikiGraph::unavailable` | method | The 'unavailable' constructor instantiates and returns a new 'Self' instance initialized with an empty 'edges' vector and its 'availability' set to 'CodewikiGraphAvailability::Unavailable'. [crates/gcode/src/commands/codewiki/types.rs:122-127] |
| `CodewikiGraphAvailability` | type | Indexed type `CodewikiGraphAvailability` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:131-135] |
| `FileDoc` | class | The 'FileDoc' struct represents the structured documentation and metadata for a source file, encapsulating its path, module affiliation, narrative body, associated symbol documentation, source spans, validation state, and optional raw disk content for lossless reuse. [crates/gcode/src/commands/codewiki/types.rs:138-158] |
| `SymbolDoc` | class | The crate-private 'SymbolDoc' struct encapsulates metadata for a codebase symbol, including its identifier, purpose, component associations, source location, optional deprecation details, and test-gated status. [crates/gcode/src/commands/codewiki/types.rs:161-182] |
| `ModuleDoc` | class | The 'ModuleDoc' struct stores metadata and structural relationships for a module's documentation, including its name, summary, source spans, associated files, child modules, verification notes, degradation status for failed AI generation, and optional cached on-disk content. [crates/gcode/src/commands/codewiki/types.rs:185-198] |
| `ArchitectureDoc` | class | The 'ArchitectureDoc' struct represents an architectural document, containing source spans, subsystems, an optional narrative description, pre-rendered Mermaid diagrams, an optional service dependency matrix, and a list of degraded sources. [crates/gcode/src/commands/codewiki/types.rs:201-218] |
| `ArchitectureSubsystem` | class | The 'ArchitectureSubsystem' struct represents a crate-private architectural subsystem, encapsulating its module name, defined responsibility, list of child modules, and associated source code spans. [crates/gcode/src/commands/codewiki/types.rs:221-226] |
| `InfraSection` | class | The 'InfraSection' struct is a package-private Rust data structure representing an infrastructure service, containing its identifier, a list of dependent entities that pulled it in, its associated adapter module, and textual summaries of its purpose and degradation impact. [crates/gcode/src/commands/codewiki/types.rs:234-240] |
| `InfrastructureDoc` | class | The 'InfrastructureDoc' struct represents an infrastructure document composed of a collection of infrastructure sections and a list of identifiers for degraded sources. [crates/gcode/src/commands/codewiki/types.rs:247-250] |
| `FeatureEntry` | class | The 'FeatureEntry' struct stores configuration and routing metadata for a CLI feature, mapping a command name and its associated flags to its implementation's handler file and entry symbol. [crates/gcode/src/commands/codewiki/types.rs:258-264] |
| `FeatureBinarySection` | class | The 'FeatureBinarySection' struct is a crate-visible ('pub(crate)') Rust data structure that associates a binary's name or path, represented as a 'String', with a vector of its corresponding 'FeatureEntry' instances. [crates/gcode/src/commands/codewiki/types.rs:269-272] |
| `FeatureCatalogDoc` | class | The 'FeatureCatalogDoc' struct represents a document containing a collection of binary feature sections and a list of degraded source identifiers. [crates/gcode/src/commands/codewiki/types.rs:279-282] |
| `DeprecationIndex` ⚠️ **deprecated** | type | ⚠️ **deprecated** — when nothing is deprecated; the scan never panics and never degrades. Indexed type `DeprecationIndex` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:289] |

_41 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/codewiki/types.rs` for the full list._

