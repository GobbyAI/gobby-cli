---
title: crates/gwiki/src/credibility.rs
type: code_file
provenance:
- file: crates/gwiki/src/credibility.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/credibility.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/credibility.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gwiki/src/credibility.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CredibilitySourceType` | type | Indexed type `CredibilitySourceType` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:7-13] |
| `CredibilityInput` | class | 'CredibilityInput' is a data container for evaluating source credibility, holding a required 'source_type', optional 'age_days', 'author', and 'publisher', and a list of 'corroborating_source_ids' used for cross-validation. [crates/gwiki/src/credibility.rs:16-22] |
| `CredibilitySignal` | class | 'CredibilitySignal' is a data container for a named credibility indicator, storing the signal name, the observed value, an explanatory rationale, and an associated signed 16-bit weight. [crates/gwiki/src/credibility.rs:25-30] |
| `CredibilityScore` | class | 'CredibilityScore' is a struct that stores a 'u8' credibility 'score' alongside a 'Vec<CredibilitySignal>' detailing the signals used to derive it. [crates/gwiki/src/credibility.rs:33-36] |
| `CredibilityScore::evaluate` | method | 'evaluate' computes a credibility 'score' by starting from a base of 50, adding the weighted contributions of source type, freshness, author, publisher, and corroboration signals derived from the input, then clamping the result to '[0, 100]' and returning 'Self { score, signals }'. [crates/gwiki/src/credibility.rs:39-57] |
| `source_type_signal` | function | Maps a 'CredibilitySourceType' to a 'CredibilitySignal' by assigning a fixed observed label, weight, and explanation for each source category, then constructing the signal via 'signal("source_type", ...)'. [crates/gwiki/src/credibility.rs:60-89] |
| `freshness_signal` | function | Returns a 'CredibilitySignal' encoding source freshness from 'age_days', awarding +15 for sources 30 days old or less, +5 for sources up to 365 days old, -10 for older sources, and -5 when freshness metadata is missing. [crates/gwiki/src/credibility.rs:91-118] |
| `author_signal` | function | 'author_signal' returns a 'CredibilitySignal' that scores a non-empty author name as a positive '"author"' signal with value '5' and rationale about accountability, or returns a negative '"author"' signal with value '-5' and '"missing"' when the optional author is absent or blank. [crates/gwiki/src/credibility.rs:120-135] |
| `publisher_signal` | function | Returns a 'CredibilitySignal' for the 'publisher' field, assigning a positive score and the trimmed publisher value when a non-empty publisher string is present, otherwise emitting a negative '"missing"' signal for absent or blank publisher metadata. [crates/gwiki/src/credibility.rs:137-152] |
| `corroboration_signal` | function | Returns a 'CredibilitySignal' for corroboration strength, mapping '0' sources to a low-confidence '-5' signal, '1' source to a modest '5' signal, and any higher count to a '10' signal labeled with the source count. [crates/gwiki/src/credibility.rs:154-175] |
| `signal` | function | Constructs and returns a 'CredibilitySignal' by converting 'name', 'observed', and 'explanation' into 'String' fields and storing the provided 'weight' unchanged. [crates/gwiki/src/credibility.rs:177-189] |

_Verified by 1 in-file unit test._

