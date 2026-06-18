---
title: crates/gwiki/src/document.rs
type: code_file
provenance:
- file: crates/gwiki/src/document.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/document.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/document.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gwiki/src/document.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DocumentFailureMode` | type | Indexed type `DocumentFailureMode` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:4-16] |
| `DocumentFailureMode::as_str` | method | Returns a '&'static str' error-code label for the enum variant by matching each 'Self' case to its corresponding lowercase underscore-delimited string literal. [crates/gwiki/src/document.rs:19-33] |
| `DocumentUnitCount` | class | 'DocumentUnitCount' is a struct that stores an immutable static string key and an associated unit count as a 'usize'. [crates/gwiki/src/document.rs:37-40] |
| `DocumentUnitCount::pages` | method | Constructs a 'Self' value with 'key' set to '"page_count"' and 'count' initialized from the provided 'usize' argument. [crates/gwiki/src/document.rs:43-48] |
| `DocumentUnitCount::sheets` | method | Constructs and returns a 'Self' instance with 'key' set to '"sheet_count"' and 'count' initialized from the provided 'usize' argument. [crates/gwiki/src/document.rs:50-55] |
| `DocumentUnitCount::slides` | method | Creates and returns a 'Self' instance with 'key' set to '"slide_count"' and 'count' initialized from the provided 'count' argument. [crates/gwiki/src/document.rs:57-62] |
| `DocumentUnitCount::key` | method | Returns the 'key' field from 'self' as a '&'static str', consuming the value. [crates/gwiki/src/document.rs:64-66] |
| `DocumentUnitCount::count` | method | Consumes 'self' and returns the value of its 'count' field as a 'usize'. [crates/gwiki/src/document.rs:68-70] |
| `DocumentDegradation` | class | 'DocumentDegradation' is a struct that captures a document failure/degradation configuration via a failure 'mode', a public 'unit_count', and a public 'fallback' string used when degradation occurs. [crates/gwiki/src/document.rs:74-78] |
| `DocumentDegradation::new` | method | Creates and returns a new 'Self' by storing the provided 'mode' and 'unit_count' values and converting 'fallback' into a 'String' with 'Into<String>'. [crates/gwiki/src/document.rs:81-91] |
| `DocumentDegradation::reason` | method | Returns the static string slice representation of 'self.mode' by delegating to 'self.mode.as_str()'. [crates/gwiki/src/document.rs:93-95] |
| `DocumentDegradationMatrix` | class | 'DocumentDegradationMatrix' is a Rust unit struct with no fields, serving as a zero-sized type named to represent a document degradation matrix. [crates/gwiki/src/document.rs:98] |
| `DocumentDegradationMatrix::metadata` | method | Returns a three-element 'Vec<(String, String)>' containing the file size in bytes, the degradation unit count keyed by 'degradation.unit_count.key()', and the degradation reason under '"media_degradation"'. [crates/gwiki/src/document.rs:101-116] |
| `DocumentDegradationMatrix::markdown_section` | method | 'markdown_section' builds a Markdown string headed '## Document Parse Unavailable' and appends the degradation reason and fallback text, each normalized to a single line, followed by blank lines. [crates/gwiki/src/document.rs:118-125] |
| `document_degradation_matrix` | function | Constructs a static degradation matrix that maps each 'DocumentFailureMode' to a fallback 'DocumentUnitCount', a failure slug, and the relevant unit key ('sheet_count' or 'page_count') across Office, HTML, and PDF extraction paths. [crates/gwiki/src/document.rs:133-217] |

