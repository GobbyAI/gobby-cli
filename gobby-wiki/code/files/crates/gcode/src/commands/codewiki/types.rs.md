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

`crates/gcode/src/commands/codewiki/types.rs` exposes 46 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/types.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodewikiInput` | class | 'CodewikiInput' is a struct that packages file paths, graph structure and availability metadata, discovered symbols, and a per-file leading-content map used to seed code-index-driven aggregate prompts with real source context. [crates/gcode/src/commands/codewiki/types.rs:11-21] |
| `LeadingChunk` | class | 'LeadingChunk' is a struct that stores a text 'content' string together with the inclusive line-range metadata 'line_start' and 'line_end' for the leading chunk of some input. [crates/gcode/src/commands/codewiki/types.rs:26-30] |
| `source_excerpt_for_file` | function | Returns 'Some(prompts::SourceExcerpt)' for the given file by looking up its 'LeadingChunk' in 'leading_chunks' and copying the chunk’s path, line range, and content, or 'None' if the file is absent. [crates/gcode/src/commands/codewiki/types.rs:33-45] |
| `ranked_source_excerpts` | function | Collects candidate 'FileDoc's into a vector, sorts them by descending symbol count then ascending path, maps each to a source excerpt using 'leading_chunks', and returns up to 'limit' excerpts. [crates/gcode/src/commands/codewiki/types.rs:50-62] |
| `CodewikiGraphEdge` | class | 'CodewikiGraphEdge' is a struct that represents a directed edge in a codewiki graph by storing the source component ID, target component ID, and the edge kind. [crates/gcode/src/commands/codewiki/types.rs:65-69] |
| `CodewikiGraphEdge::call` | method | Constructs and returns a 'CodewikiGraphEdge' with the provided source and target component IDs and sets its kind to 'CodewikiGraphEdgeKind::Call'. [crates/gcode/src/commands/codewiki/types.rs:72-81] |
| `CodewikiGraphEdge::import` | method | Constructs a 'CodewikiGraphEdge' of kind 'Import' by converting the provided source and target component identifiers into owned 'String' fields. [crates/gcode/src/commands/codewiki/types.rs:83-92] |
| `CodewikiGraphEdgeKind` | type | Indexed type `CodewikiGraphEdgeKind` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:96-99] |
| `CodewikiGraph` | class | 'CodewikiGraph' is an internal graph container that stores a vector of 'CodewikiGraphEdge' values and a 'CodewikiGraphAvailability' state. [crates/gcode/src/commands/codewiki/types.rs:102-105] |
| `CodewikiGraph::available` | method | Constructs a 'Self' instance from the provided 'edges' vector and sets 'availability' to 'CodewikiGraphAvailability::Available'. [crates/gcode/src/commands/codewiki/types.rs:108-113] |
| `CodewikiGraph::truncated` | method | Constructs a 'Self' value by storing the provided 'edges' and setting 'availability' to 'CodewikiGraphAvailability::Truncated'. [crates/gcode/src/commands/codewiki/types.rs:115-120] |
| `CodewikiGraph::unavailable` | method | Constructs and returns a 'Self' instance with 'edges' initialized to an empty 'Vec' and 'availability' set to 'CodewikiGraphAvailability::Unavailable'. [crates/gcode/src/commands/codewiki/types.rs:122-127] |
| `CodewikiGraphAvailability` | type | Indexed type `CodewikiGraphAvailability` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:131-135] |
| `FileDoc` | class | 'FileDoc' is a crate-visible record that models a documented source file, including its path, module, summary and rendered body text, provenance spans, symbol and component references, and flags for degraded generation or verbatim page reuse. [crates/gcode/src/commands/codewiki/types.rs:138-156] |
| `SymbolDoc` | class | 'SymbolDoc' is an internal data container that associates a 'Symbol' with its purpose, component identifier and label, and the source span where it is defined or documented. [crates/gcode/src/commands/codewiki/types.rs:159-165] |
| `ModuleDoc` | class | 'ModuleDoc' is a crate-visible record of a module’s generated documentation metadata, including its name, summary, source spans, linked files and child modules, optional dependency/call diagrams, graph availability, and flags for degraded generation or reused on-disk content. [crates/gcode/src/commands/codewiki/types.rs:168-182] |
| `ArchitectureDoc` | class | 'ArchitectureDoc' is an internal data structure that aggregates source span references, parsed subsystems, an optional narrative and dependency diagram, and a list of degraded source identifiers for an architecture document. [crates/gcode/src/commands/codewiki/types.rs:185-191] |
| `ArchitectureSubsystem` | class | 'ArchitectureSubsystem' is an internal data struct that represents a subsystem by name, its stated responsibility, the names of its child modules, and the source spans where it is defined or referenced. [crates/gcode/src/commands/codewiki/types.rs:194-199] |
| `OnboardingDoc` | class | 'OnboardingDoc' is an internal document model that aggregates source spans, onboarding entry points, a prescribed reading order of steps, and a list of degraded source identifiers. [crates/gcode/src/commands/codewiki/types.rs:202-207] |
| `OnboardingEntryPoint` | class | 'OnboardingEntryPoint' is a crate-visible data record that identifies an onboarding entry point via a link, a description, and its originating 'SourceSpan'. [crates/gcode/src/commands/codewiki/types.rs:210-214] |
| `OnboardingStep` | class | 'OnboardingStep' is an internal Rust record type that stores a module identifier, a textual summary, and two ranking metrics: an integer 'degree' and a floating-point 'score'. [crates/gcode/src/commands/codewiki/types.rs:217-222] |
| `HotspotsDoc` | class | 'HotspotsDoc' is a crate-private aggregation record that groups source spans, hotspot findings, god-node findings, bridge findings, and a list of degraded source identifiers. [crates/gcode/src/commands/codewiki/types.rs:225-231] |
| `HotspotFinding` | class | 'HotspotFinding' is an internal record that pairs a 'HotspotNode' with optional quantitative metrics ('degree', 'score', 'frequency', and 'weight') describing the finding. [crates/gcode/src/commands/codewiki/types.rs:234-240] |
| `HotspotNode` | class | 'HotspotNode' is an internal data record identifying a hotspot by 'id', 'kind', 'label', and 'wikilink', with optional 'file_wikilink' and optional 'source_span' metadata. [crates/gcode/src/commands/codewiki/types.rs:243-250] |
| `FileLink` | class | 'FileLink' is a crate-visible struct that stores a file 'path', a 'summary' string, and a collection of 'SourceSpan' values identifying the source locations associated with that link. [crates/gcode/src/commands/codewiki/types.rs:253-257] |
| `ModuleLink` | class | 'ModuleLink' is a crate-visible struct that associates a module identifier with a textual summary and the source locations ('SourceSpan' values) from which that link was derived. [crates/gcode/src/commands/codewiki/types.rs:260-264] |
| `SourceSpan` | class | 'SourceSpan' is an internal source-location record that identifies a file and a contiguous line range via 'line_start' and 'line_end'. [crates/gcode/src/commands/codewiki/types.rs:267-271] |
| `CodewikiRunSummary` | class | 'CodewikiRunSummary' is a run-report struct that captures the executed command, project identifiers and paths, generation counts and file/module/symbol totals, changed and skipped outputs, and whether AI assistance was enabled. [crates/gcode/src/commands/codewiki/types.rs:274-286] |
| `CodewikiMeta` | class | 'CodewikiMeta' is a crate-visible metadata container that tracks document metadata in a 'BTreeMap', a list of generated document IDs, an optional serialized index snapshot, and an 'ai_mode' string. [crates/gcode/src/commands/codewiki/types.rs:289-296] |
| `CodewikiDocMeta` | class | 'CodewikiDocMeta' is crate-visible persisted metadata for a generated document, tracking its 'source_hashes', 'degraded' fallback status, optional cached 'summary', generation 'ai_mode', and deterministic 'render_version'. [crates/gcode/src/commands/codewiki/types.rs:299-319] |
| `BuiltDoc` | class | 'BuiltDoc' is a crate-visible document record containing the output path, rendered content, a 'degraded' status flag, and an optional persisted grounded summary for reuse in later prompt generation. [crates/gcode/src/commands/codewiki/types.rs:324-331] |
| `BuiltDoc::healthy` | method | Constructs a 'Self' value with 'path' set from the given 'Into<String>', 'content' set to the provided string, 'degraded' set to 'false', and 'summary' initialized to 'None'. [crates/gcode/src/commands/codewiki/types.rs:334-341] |
| `CodewikiIndexSnapshot` | class | 'CodewikiIndexSnapshot' is a serialized snapshot of a codewiki index containing per-file and per-symbol state, an optional map of graph neighborhood data, and a list of degraded source identifiers. [crates/gcode/src/commands/codewiki/types.rs:345-352] |
| `CodewikiFileSnapshot` | class | 'CodewikiFileSnapshot' is an internal struct that records a file’s 'content_hash' and its 'symbol_count' for snapshotting or change detection purposes. [crates/gcode/src/commands/codewiki/types.rs:355-358] |
| `CodewikiSymbolSnapshot` | class | 'CodewikiSymbolSnapshot' is a crate-visible data snapshot of a code symbol, storing its source file path, simple and qualified names, kind, and starting line number. [crates/gcode/src/commands/codewiki/types.rs:361-367] |
| `TextGenerator` | type | Indexed type `TextGenerator` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:369] |
| `TextVerifier` | type | Indexed type `TextVerifier` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:377] |
| `PromptTier` | type | Indexed type `PromptTier` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:384-388] |
| `AiDepth` | type | Indexed type `AiDepth` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:393-401] |
| `AiDepth::includes_files` | method | Returns 'true' if 'self' is greater than or equal to 'AiDepth::Files', indicating that file inclusion is enabled at this depth. [crates/gcode/src/commands/codewiki/types.rs:404-406] |
| `AiDepth::includes_symbols` | method | Returns 'true' when 'self' is at least 'AiDepth::Symbols', indicating that symbols are included at this depth or any deeper level. [crates/gcode/src/commands/codewiki/types.rs:408-410] |
| `AiDepth::mode_label` | method | Returns a static string slice identifying the 'AiDepth' variant as '"sections"', '"files"', or '"symbols"'. [crates/gcode/src/commands/codewiki/types.rs:412-418] |
| `CodewikiAiOptions` | class | 'CodewikiAiOptions' configures AI generation and verification behavior for Codewiki, including optional routing, required depth, an optional aggregate-docs profile, and optional verify-time profile/model/API-key overrides with documented fallback precedence. [crates/gcode/src/commands/codewiki/types.rs:422-436] |
| `SourceSpan::from_symbol` | method | Constructs a new 'Self' by cloning 'symbol.file_path' into 'file' and copying 'line_start' and 'line_end' from the given 'Symbol'. [crates/gcode/src/commands/codewiki/types.rs:439-445] |
| `SourceSpan::citation` | method | Returns a formatted citation string for the file and line span, using '[file:start]' when 'line_start == line_end' and '[file:start-end]' otherwise. [crates/gcode/src/commands/codewiki/types.rs:447-453] |
| `SourceSpan::contains` | method | Returns 'true' when the given 'file' matches 'self.file' and the interval '[line_start, line_end]' is fully contained within 'self.line_start..=self.line_end'. [crates/gcode/src/commands/codewiki/types.rs:455-457] |

