---
title: crates/gwiki/src/audit.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/audit.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/audit.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gwiki/src/audit.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AuditOptions` | class | 'AuditOptions' is a Rust configuration struct that stores a 'BTreeSet<String>' of 'ignored_sections' to indicate which audit sections should be skipped. [crates/gwiki/src/audit.rs:36-38] |
| `AuditOptions::from_env` | method | Creates a default options value and, if the 'IGNORED_SECTIONS_ENV' environment variable is set, extends its ignored sections with the variable’s comma-separated values. [crates/gwiki/src/audit.rs:41-47] |
| `AuditOptions::with_additional_ignored_sections` | method | Consumes 'self', appends the provided iterable of section names to the ignored-sections set via 'extend_ignored_sections', and returns the updated value. [crates/gwiki/src/audit.rs:50-57] |
| `AuditOptions::ignores_section` | method | Returns 'true' if the trimmed, ASCII-lowercased 'heading' is present in 'self.ignored_sections', otherwise 'false'. [crates/gwiki/src/audit.rs:59-62] |
| `AuditOptions::extend_ignored_sections` | method | Extends 'self.ignored_sections' by inserting each input section as a trimmed, ASCII-lowercased string and discarding any entries that become empty. [crates/gwiki/src/audit.rs:64-75] |
| `AuditOptions::default` | method | Constructs 'Self' with 'ignored_sections' initialized as a 'Vec<String>' collected by cloning each entry from 'DEFAULT_IGNORED_SECTIONS'. [crates/gwiki/src/audit.rs:79-86] |
| `AuditReport` | class | 'AuditReport' is a Rust report struct that records the audited command, the target scope identity, the root path, a list of unsupported claims, and shared source context data for the audit. [crates/gwiki/src/audit.rs:90-96] |
| `UnsupportedClaim` | class | 'UnsupportedClaim' is a Rust struct that records an unsupported assertion with its source location ('path', 'line', optional 'heading'), the claim text, an explanatory 'reason', and associated audit source context. [crates/gwiki/src/audit.rs:99-106] |
| `AuditSourceContext` | class | 'AuditSourceContext' is a data container that identifies an audit source by required 'source_id' and optional 'path', 'citation', and 'location' metadata. [crates/gwiki/src/audit.rs:109-114] |
| `run` | function | Invokes 'run_with_options' using 'AuditOptions::from_env()' to produce an 'AuditReport' for the given 'vault_root' and 'scope'. [crates/gwiki/src/audit.rs:117-119] |
| `run_with_options` | function | 'run_with_options' collects pages under 'vault_root' that match 'scope', builds shared source context and provenance, computes unsupported claims for those pages using the provided 'options', and returns an 'AuditReport' with the audit command, scope, vault root, and aggregated unsupported claims. [crates/gwiki/src/audit.rs:121-144] |
| `source_context` | function | Reads a 'SourceManifest' from 'vault_root' and transforms each manifest entry into an 'AuditSourceContext' with 'path' set to 'raw/{id}.md', preserving 'source_id', 'citation', and 'location', returning the collected list. [crates/gwiki/src/audit.rs:146-158] |
| `load_provenance` | function | Returns 'ProvenanceGraph::load_from_vault(vault_root)' when 'meta/provenance.json' exists under the vault root, otherwise returns 'Ok(ProvenanceGraph::default())'. [crates/gwiki/src/audit.rs:160-167] |

