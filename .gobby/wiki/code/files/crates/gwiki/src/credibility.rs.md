---
title: crates/gwiki/src/credibility.rs
type: code_file
provenance:
- file: crates/gwiki/src/credibility.rs
  ranges:
  - 7-13
  - 16-22
  - 25-30
  - 33-36
  - 38-58
  - 60-89
  - 91-118
  - 120-135
  - 137-152
  - 154-175
  - 177-189
  - 196-223
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/credibility.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines an explainable credibility scoring model for raw wiki sources. It introduces input and output types plus a `CredibilitySourceType` enum, then evaluates a `CredibilityInput` by combining weighted signals for source type, freshness, author, publisher, and corroboration into a normalized `CredibilityScore` with per-signal explanations. Helper functions build each signal consistently, and the test checks that the score stays high and all signal explanations are present.
[crates/gwiki/src/credibility.rs:7-13]
[crates/gwiki/src/credibility.rs:16-22]
[crates/gwiki/src/credibility.rs:25-30]
[crates/gwiki/src/credibility.rs:33-36]
[crates/gwiki/src/credibility.rs:38-58]

## API Symbols

- `CredibilitySourceType` (type) component `CredibilitySourceType [type]` (`114b1727-7880-57c7-a00c-dbc815575552`) lines 7-13 [crates/gwiki/src/credibility.rs:7-13]
  - Signature: `pub enum CredibilitySourceType {`
  - Purpose: Indexed type `CredibilitySourceType` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:7-13]
- `CredibilityInput` (class) component `CredibilityInput [class]` (`22762a00-0ffa-5a24-aed3-5d5930132a5a`) lines 16-22 [crates/gwiki/src/credibility.rs:16-22]
  - Signature: `pub struct CredibilityInput {`
  - Purpose: `CredibilityInput` is a struct that aggregates credibility assessment parameters for a source, including its type classification, age in days, optional authorship and publisher metadata, and a collection of corroborating source identifiers. [crates/gwiki/src/credibility.rs:16-22]
- `CredibilitySignal` (class) component `CredibilitySignal [class]` (`b3fd920b-fd0b-5e09-9bb0-957d9379ccab`) lines 25-30 [crates/gwiki/src/credibility.rs:25-30]
  - Signature: `pub struct CredibilitySignal {`
  - Purpose: `CredibilitySignal` is a public struct that encapsulates a weighted credibility indicator with String fields for name, observed evidence, and explanation, plus an i16 weight value for scoring. [crates/gwiki/src/credibility.rs:25-30]
- `CredibilityScore` (class) component `CredibilityScore [class]` (`44987ec2-d082-5e53-a1ac-35a277221549`) lines 33-36 [crates/gwiki/src/credibility.rs:33-36]
  - Signature: `pub struct CredibilityScore {`
  - Purpose: `CredibilityScore` is a struct that encapsulates a numeric credibility assessment (0-255) along with a vector of contributing credibility signals. [crates/gwiki/src/credibility.rs:33-36]
- `CredibilityScore` (class) component `CredibilityScore [class]` (`8e177e2d-b137-52f3-8b26-b37faf14776a`) lines 38-58 [crates/gwiki/src/credibility.rs:38-58]
  - Signature: `impl CredibilityScore {`
  - Purpose: The `evaluate` method computes a credibility score by aggregating weighted signals from source type, content freshness, authorship, publisher reputation, and corroboration count, clamping the result to 0-100. [crates/gwiki/src/credibility.rs:38-58]
- `CredibilityScore.evaluate` (method) component `CredibilityScore.evaluate [method]` (`8e164fcb-cda4-5249-94be-fcfbcc286f52`) lines 39-57 [crates/gwiki/src/credibility.rs:39-57]
  - Signature: `pub fn evaluate(input: CredibilityInput) -> Self {`
  - Purpose: Constructs a credibility assessment by aggregating weighted signals derived from source type, freshness, author, publisher, and corroboration factors, returning a normalized score clamped to 0-100. [crates/gwiki/src/credibility.rs:39-57]
- `source_type_signal` (function) component `source_type_signal [function]` (`d20beb4f-5f31-5edc-8afa-15b009971058`) lines 60-89 [crates/gwiki/src/credibility.rs:60-89]
  - Signature: `fn source_type_signal(source_type: CredibilitySourceType) -> CredibilitySignal {`
  - Purpose: Maps a source type to a weighted credibility signal (ranging from -10 to +25) with explanatory metadata for confidence evaluation. [crates/gwiki/src/credibility.rs:60-89]
- `freshness_signal` (function) component `freshness_signal [function]` (`0c8040eb-ee93-5970-8859-a0725bc10415`) lines 91-118 [crates/gwiki/src/credibility.rs:91-118]
  - Signature: `fn freshness_signal(age_days: Option<u16>) -> CredibilitySignal {`
  - Purpose: Returns a `CredibilitySignal` that assigns tiered confidence weights based on source age: +15 for ≤30 days, +5 for 31–365 days, -10 for >365 days, and -5 for unknown age. [crates/gwiki/src/credibility.rs:91-118]
- `author_signal` (function) component `author_signal [function]` (`9f00a5de-e202-5683-b143-f5af8e65a315`) lines 120-135 [crates/gwiki/src/credibility.rs:120-135]
  - Signature: `fn author_signal(author: Option<&str>) -> CredibilitySignal {`
  - Purpose: Returns a credibility signal that awards +5 points for a non-empty author or deducts 5 points for missing author metadata. [crates/gwiki/src/credibility.rs:120-135]
- `publisher_signal` (function) component `publisher_signal [function]` (`76997bd3-3213-5d1a-b3d8-c2cb4070bcb0`) lines 137-152 [crates/gwiki/src/credibility.rs:137-152]
  - Signature: `fn publisher_signal(publisher: Option<&str>) -> CredibilitySignal {`
  - Purpose: Generates a `CredibilitySignal` that assigns a +5 credibility score for a non-empty publisher string or -5 for missing/empty publisher metadata, evaluating source auditability. [crates/gwiki/src/credibility.rs:137-152]
- `corroboration_signal` (function) component `corroboration_signal [function]` (`4dc81dc3-31a8-540e-ba67-af1664b690e0`) lines 154-175 [crates/gwiki/src/credibility.rs:154-175]
  - Signature: `fn corroboration_signal(count: usize) -> CredibilitySignal {`
  - Purpose: Returns a `CredibilitySignal` that assigns confidence scores of -5 (uncorroborated), +5 (single source), or +10 (multiple sources) based on the corroboration count. [crates/gwiki/src/credibility.rs:154-175]
- `signal` (function) component `signal [function]` (`1fdcdede-bdfd-567e-b6e3-6e08838ab3ce`) lines 177-189 [crates/gwiki/src/credibility.rs:177-189]
  - Signature: `fn signal(`
  - Purpose: Constructs and returns a `CredibilitySignal` struct by converting three generic `Into<String>` parameters (name, observed, explanation) and storing an `i16` weight value. [crates/gwiki/src/credibility.rs:177-189]
- `credibility_score_has_explanation` (function) component `credibility_score_has_explanation [function]` (`1e752991-a5e9-53d8-8768-a4591b61980c`) lines 196-223 [crates/gwiki/src/credibility.rs:196-223]
  - Signature: `fn credibility_score_has_explanation() {`
  - Purpose: # Summary

This test function verifies that credibility score evaluation produces a score ≥80 and includes non-empty explanations for all five credibility signals: source_type, freshness, author, publisher, and corroboration. [crates/gwiki/src/credibility.rs:196-223]

