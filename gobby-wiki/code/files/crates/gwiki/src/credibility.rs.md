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
  - 39-57
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/credibility.rs:7-13](crates/gwiki/src/credibility.rs#L7-L13), [crates/gwiki/src/credibility.rs:16-22](crates/gwiki/src/credibility.rs#L16-L22), [crates/gwiki/src/credibility.rs:25-30](crates/gwiki/src/credibility.rs#L25-L30), [crates/gwiki/src/credibility.rs:33-36](crates/gwiki/src/credibility.rs#L33-L36), [crates/gwiki/src/credibility.rs:39-57](crates/gwiki/src/credibility.rs#L39-L57), [crates/gwiki/src/credibility.rs:60-89](crates/gwiki/src/credibility.rs#L60-L89), [crates/gwiki/src/credibility.rs:91-118](crates/gwiki/src/credibility.rs#L91-L118), [crates/gwiki/src/credibility.rs:120-135](crates/gwiki/src/credibility.rs#L120-L135), [crates/gwiki/src/credibility.rs:137-152](crates/gwiki/src/credibility.rs#L137-L152), [crates/gwiki/src/credibility.rs:154-175](crates/gwiki/src/credibility.rs#L154-L175), [crates/gwiki/src/credibility.rs:177-189](crates/gwiki/src/credibility.rs#L177-L189), [crates/gwiki/src/credibility.rs:196-223](crates/gwiki/src/credibility.rs#L196-L223)

</details>

# crates/gwiki/src/credibility.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements explainable credibility scoring for raw wiki sources. It defines the input model (`CredibilitySourceType`, `CredibilityInput`) and the output model (`CredibilityScore`, `CredibilitySignal`), then computes a score by combining several weighted signals: source type, freshness, author, publisher, and corroborating sources. `CredibilityScore::evaluate` starts from a neutral baseline, gathers those per-factor signals through small helper functions, sums their weights, and clamps the final score to 0-100. The remaining helper functions encapsulate each signal’s logic, and `credibility_score_has_explanation` checks whether a score includes enough signal detail to be considered explained.
[crates/gwiki/src/credibility.rs:7-13]
[crates/gwiki/src/credibility.rs:16-22]
[crates/gwiki/src/credibility.rs:25-30]
[crates/gwiki/src/credibility.rs:33-36]
[crates/gwiki/src/credibility.rs:39-57]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CredibilitySourceType` | type | `pub enum CredibilitySourceType {` | `CredibilitySourceType [type]` | `114b1727-7880-57c7-a00c-dbc815575552` | 7-13 [crates/gwiki/src/credibility.rs:7-13] | Indexed type `CredibilitySourceType` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:7-13] |
| `CredibilityInput` | class | `pub struct CredibilityInput {` | `CredibilityInput [class]` | `22762a00-0ffa-5a24-aed3-5d5930132a5a` | 16-22 [crates/gwiki/src/credibility.rs:16-22] | Indexed class `CredibilityInput` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:16-22] |
| `CredibilitySignal` | class | `pub struct CredibilitySignal {` | `CredibilitySignal [class]` | `b3fd920b-fd0b-5e09-9bb0-957d9379ccab` | 25-30 [crates/gwiki/src/credibility.rs:25-30] | Indexed class `CredibilitySignal` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:25-30] |
| `CredibilityScore` | class | `pub struct CredibilityScore {` | `CredibilityScore [class]` | `44987ec2-d082-5e53-a1ac-35a277221549` | 33-36 [crates/gwiki/src/credibility.rs:33-36] | Indexed class `CredibilityScore` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:33-36] |
| `CredibilityScore::evaluate` | method | `pub fn evaluate(input: CredibilityInput) -> Self {` | `CredibilityScore::evaluate [method]` | `8e164fcb-cda4-5249-94be-fcfbcc286f52` | 39-57 [crates/gwiki/src/credibility.rs:39-57] | Indexed method `CredibilityScore::evaluate` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:39-57] |
| `source_type_signal` | function | `fn source_type_signal(source_type: CredibilitySourceType) -> CredibilitySignal {` | `source_type_signal [function]` | `d20beb4f-5f31-5edc-8afa-15b009971058` | 60-89 [crates/gwiki/src/credibility.rs:60-89] | Indexed function `source_type_signal` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:60-89] |
| `freshness_signal` | function | `fn freshness_signal(age_days: Option<u16>) -> CredibilitySignal {` | `freshness_signal [function]` | `0c8040eb-ee93-5970-8859-a0725bc10415` | 91-118 [crates/gwiki/src/credibility.rs:91-118] | Indexed function `freshness_signal` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:91-118] |
| `author_signal` | function | `fn author_signal(author: Option<&str>) -> CredibilitySignal {` | `author_signal [function]` | `9f00a5de-e202-5683-b143-f5af8e65a315` | 120-135 [crates/gwiki/src/credibility.rs:120-135] | Indexed function `author_signal` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:120-135] |
| `publisher_signal` | function | `fn publisher_signal(publisher: Option<&str>) -> CredibilitySignal {` | `publisher_signal [function]` | `76997bd3-3213-5d1a-b3d8-c2cb4070bcb0` | 137-152 [crates/gwiki/src/credibility.rs:137-152] | Indexed function `publisher_signal` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:137-152] |
| `corroboration_signal` | function | `fn corroboration_signal(count: usize) -> CredibilitySignal {` | `corroboration_signal [function]` | `4dc81dc3-31a8-540e-ba67-af1664b690e0` | 154-175 [crates/gwiki/src/credibility.rs:154-175] | Indexed function `corroboration_signal` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:154-175] |
| `signal` | function | `fn signal(` | `signal [function]` | `1fdcdede-bdfd-567e-b6e3-6e08838ab3ce` | 177-189 [crates/gwiki/src/credibility.rs:177-189] | Indexed function `signal` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:177-189] |
| `credibility_score_has_explanation` | function | `fn credibility_score_has_explanation() {` | `credibility_score_has_explanation [function]` | `1e752991-a5e9-53d8-8768-a4591b61980c` | 196-223 [crates/gwiki/src/credibility.rs:196-223] | Indexed function `credibility_score_has_explanation` in `crates/gwiki/src/credibility.rs`. [crates/gwiki/src/credibility.rs:196-223] |
