---
title: crates/gcode/src/commands/codewiki/ownership/render.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/ownership/render.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The module handles diagnostic reporting of metadata degradation in degraded_sources (crates/gcode/src/commands/codewiki/ownership/render.rs:10-34), tracking issues such as missing CODEOWNERS or git blame files. It constructs the YAML frontmatter document block using ownership_frontmatter (crates/gcode/src/commands/codewiki/ownership/render.rs:36-68) with a Serde-serializable Frontmatter struct (crates/gcode/src/commands/codewiki/ownership/render.rs:38-52).

## How it fits

This file acts as the presentation layer for the code ownership analysis subsystem within the codewiki command. It imports structures like FileOwnership, OwnershipContributor, and OwnershipStatus from its parent module to translate analysis results into user-readable Markdown documents.

The rendering process begins with data ingestion. It takes an OwnershipStatus and a map of analyzed files to determine degradation levels and construct a standard frontmatter block. It utilizes helpers like is_false (crates/gcode/src/commands/codewiki/ownership/render.rs:70-72) to omit unnecessary boolean fields during YAML serialization.
[crates/gcode/src/commands/codewiki/ownership/render.rs:10-34]
[crates/gcode/src/commands/codewiki/ownership/render.rs:36-68]
[crates/gcode/src/commands/codewiki/ownership/render.rs:38-52]
[crates/gcode/src/commands/codewiki/ownership/render.rs:70-72]
[crates/gcode/src/commands/codewiki/ownership/render.rs:74-100]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `degraded_sources` | function | Returns a list of degradation reason strings for an 'OwnershipStatus' and file-ownership map, adding markers for unavailable CODEOWNERS or git blame data, blame errors or partial results, and 'ownership_unknown' when every file has neither declared nor derived ownership. [crates/gcode/src/commands/codewiki/ownership/render.rs:10-34] |
| `ownership_frontmatter` | function | Constructs and returns a YAML frontmatter block for a 'Code Ownership' document by serializing a 'Frontmatter' struct with generated provenance/trust metadata, optional 'degraded' and 'partial' fields derived from 'degraded_sources' and 'partial', stripping the serializer’s leading '---', and rewrapping it as a YAML document string. [crates/gcode/src/commands/codewiki/ownership/render.rs:36-68] |
| `Frontmatter` | class | 'Frontmatter<'a>' is a Serde-serializable metadata struct that records a document’s title, type, provenance, generator, trust and freshness labels, plus optional degradation flags and source lists, with conditional omission of empty or false fields during serialization. [crates/gcode/src/commands/codewiki/ownership/render.rs:38-52] |
| `is_false` | function | Returns the logical negation of the referenced boolean, yielding 'true' when 'value' is 'false' and 'false' when 'value' is 'true'. [crates/gcode/src/commands/codewiki/ownership/render.rs:70-72] |
| `write_modules` | function | Groups files by module, appends a '## Modules' section to 'doc', and for each module writes a heading plus aggregated primary-owner and contributor lines derived from the files in that module. [crates/gcode/src/commands/codewiki/ownership/render.rs:74-100] |
| `write_files` | function | Appends a '## Files' section to 'doc' that iterates over 'by_file', emits a wikilinked '###' heading for each file, writes “Unknown ownership.” when both declared and derived owners are empty, otherwise writes the declared owners and derived contributors lines followed by a blank line. [crates/gcode/src/commands/codewiki/ownership/render.rs:102-114] |
| `aggregate_primary` | function | Returns a sorted, deduplicated 'Vec<String>' of primary owner names by collecting all non-empty declared owners from the input files, otherwise falling back to the first derived owner name for files without declared owners. [crates/gcode/src/commands/codewiki/ownership/render.rs:116-126] |
| `aggregate_contributors` | function | Aggregates all 'derived' contributors across the input 'FileOwnership' values by contributor ID, deterministically merges identity fields while summing line counts, then returns the top five 'OwnershipContributor' records sorted by descending lines, ascending name, and ascending contributor ID. [crates/gcode/src/commands/codewiki/ownership/render.rs:128-172] |
| `write_owner_line` | function | Appends a 'label:' line to 'doc' ending with 'unknown' when 'owners' is empty, otherwise joining the owner strings with ', ' and writing them via 'writeln!'. [crates/gcode/src/commands/codewiki/ownership/render.rs:174-180] |
| `write_contributor_line` | function | Appends a 'Top contributors:' line to 'doc', rendering each contributor as 'name (N line[s])' joined by commas, or 'Top contributors: unknown' if the slice is empty. [crates/gcode/src/commands/codewiki/ownership/render.rs:182-204] |

