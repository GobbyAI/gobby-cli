---
title: crates/gwiki/src/ingest/pdf/text.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/pdf/text.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/pdf/text.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/pdf/text.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/pdf/text.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `normalize_page_text` | function | This function normalizes input text by joining consecutive non-empty lines—processed via 'single_line'—with a single space into paragraph blocks, and then concatenates these paragraphs using double newlines. [crates/gwiki/src/ingest/pdf/text.rs:4-25] |

_Verified by 8 in-file unit tests._

