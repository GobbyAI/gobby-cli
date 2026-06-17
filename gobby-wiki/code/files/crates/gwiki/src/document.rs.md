---
title: crates/gwiki/src/document.rs
type: code_file
provenance:
- file: crates/gwiki/src/document.rs
  ranges:
  - 4-16
  - 19-33
  - 37-40
  - 43-48
  - 50-55
  - 57-62
  - 64-66
  - 68-70
  - 74-78
  - 81-91
  - 93-95
  - '98'
  - 101-116
  - 118-125
  - 133-217
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/document.rs:4-16](crates/gwiki/src/document.rs#L4-L16), [crates/gwiki/src/document.rs:19-33](crates/gwiki/src/document.rs#L19-L33), [crates/gwiki/src/document.rs:37-40](crates/gwiki/src/document.rs#L37-L40), [crates/gwiki/src/document.rs:43-48](crates/gwiki/src/document.rs#L43-L48), [crates/gwiki/src/document.rs:50-55](crates/gwiki/src/document.rs#L50-L55), [crates/gwiki/src/document.rs:57-62](crates/gwiki/src/document.rs#L57-L62), [crates/gwiki/src/document.rs:64-66](crates/gwiki/src/document.rs#L64-L66), [crates/gwiki/src/document.rs:68-70](crates/gwiki/src/document.rs#L68-L70), [crates/gwiki/src/document.rs:74-78](crates/gwiki/src/document.rs#L74-L78), [crates/gwiki/src/document.rs:81-91](crates/gwiki/src/document.rs#L81-L91), [crates/gwiki/src/document.rs:93-95](crates/gwiki/src/document.rs#L93-L95), [crates/gwiki/src/document.rs:98](crates/gwiki/src/document.rs#L98), [crates/gwiki/src/document.rs:101-116](crates/gwiki/src/document.rs#L101-L116), [crates/gwiki/src/document.rs:118-125](crates/gwiki/src/document.rs#L118-L125), [crates/gwiki/src/document.rs:133-217](crates/gwiki/src/document.rs#L133-L217)

</details>

# crates/gwiki/src/document.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the document degradation model and formatting helpers used to describe and report extraction failures. `DocumentFailureMode` provides a fixed set of machine-readable failure reasons, `DocumentUnitCount` tags counts by document unit type (`page_count`, `sheet_count`, `slide_count`), and `DocumentDegradation` combines a failure mode with the affected unit count and fallback text. `DocumentDegradationMatrix` and `document_degradation_matrix` then turn those values into structured metadata and markdown sections for a degradation matrix output.
[crates/gwiki/src/document.rs:4-16]
[crates/gwiki/src/document.rs:19-33]
[crates/gwiki/src/document.rs:37-40]
[crates/gwiki/src/document.rs:43-48]
[crates/gwiki/src/document.rs:50-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DocumentFailureMode` | type | `pub enum DocumentFailureMode {` | `DocumentFailureMode [type]` | `637da746-dd23-52bf-a6ba-1dd755c1805d` | 4-16 [crates/gwiki/src/document.rs:4-16] | Indexed type `DocumentFailureMode` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:4-16] |
| `DocumentFailureMode::as_str` | method | `pub fn as_str(self) -> &'static str {` | `DocumentFailureMode::as_str [method]` | `80335ee5-2689-5027-b945-d4db97b5ae59` | 19-33 [crates/gwiki/src/document.rs:19-33] | Indexed method `DocumentFailureMode::as_str` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:19-33] |
| `DocumentUnitCount` | class | `pub struct DocumentUnitCount {` | `DocumentUnitCount [class]` | `65f6074c-ab55-591a-b637-2c51891a382a` | 37-40 [crates/gwiki/src/document.rs:37-40] | Indexed class `DocumentUnitCount` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:37-40] |
| `DocumentUnitCount::pages` | method | `pub fn pages(count: usize) -> Self {` | `DocumentUnitCount::pages [method]` | `d6526ac2-f00a-5032-822c-3740d6a785f5` | 43-48 [crates/gwiki/src/document.rs:43-48] | Indexed method `DocumentUnitCount::pages` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:43-48] |
| `DocumentUnitCount::sheets` | method | `pub fn sheets(count: usize) -> Self {` | `DocumentUnitCount::sheets [method]` | `35cd1a20-47a2-5958-8862-f1a6968bf067` | 50-55 [crates/gwiki/src/document.rs:50-55] | Indexed method `DocumentUnitCount::sheets` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:50-55] |
| `DocumentUnitCount::slides` | method | `pub fn slides(count: usize) -> Self {` | `DocumentUnitCount::slides [method]` | `24bb6f62-4949-55f2-bb92-7d4dde65f248` | 57-62 [crates/gwiki/src/document.rs:57-62] | Indexed method `DocumentUnitCount::slides` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:57-62] |
| `DocumentUnitCount::key` | method | `pub fn key(self) -> &'static str {` | `DocumentUnitCount::key [method]` | `a293c971-39c6-5c3b-aa6f-5efe1f6ed402` | 64-66 [crates/gwiki/src/document.rs:64-66] | Indexed method `DocumentUnitCount::key` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:64-66] |
| `DocumentUnitCount::count` | method | `pub fn count(self) -> usize {` | `DocumentUnitCount::count [method]` | `aeea1f97-8d6e-52c4-ad34-fdb365641909` | 68-70 [crates/gwiki/src/document.rs:68-70] | Indexed method `DocumentUnitCount::count` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:68-70] |
| `DocumentDegradation` | class | `pub struct DocumentDegradation {` | `DocumentDegradation [class]` | `774a272f-ec20-597c-913f-5b9b7c9b41bc` | 74-78 [crates/gwiki/src/document.rs:74-78] | Indexed class `DocumentDegradation` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:74-78] |
| `DocumentDegradation::new` | method | `pub fn new(` | `DocumentDegradation::new [method]` | `8d203c3e-ed93-59dd-a59a-2c5b82d59faf` | 81-91 [crates/gwiki/src/document.rs:81-91] | Indexed method `DocumentDegradation::new` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:81-91] |
| `DocumentDegradation::reason` | method | `pub fn reason(&self) -> &'static str {` | `DocumentDegradation::reason [method]` | `fef08e82-178f-5b7f-9aa3-0f3083753e86` | 93-95 [crates/gwiki/src/document.rs:93-95] | Indexed method `DocumentDegradation::reason` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:93-95] |
| `DocumentDegradationMatrix` | class | `pub struct DocumentDegradationMatrix;` | `DocumentDegradationMatrix [class]` | `b582a6bf-e3e9-5d58-9c7b-09475b92914b` | 98-98 [crates/gwiki/src/document.rs:98] | Indexed class `DocumentDegradationMatrix` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:98] |
| `DocumentDegradationMatrix::metadata` | method | `pub fn metadata(` | `DocumentDegradationMatrix::metadata [method]` | `4a6f6f41-50b0-5263-a78b-0b162edf35b1` | 101-116 [crates/gwiki/src/document.rs:101-116] | Indexed method `DocumentDegradationMatrix::metadata` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:101-116] |
| `DocumentDegradationMatrix::markdown_section` | method | `pub fn markdown_section(degradation: &DocumentDegradation) -> String {` | `DocumentDegradationMatrix::markdown_section [method]` | `97e3dbc3-d4e0-5238-85cb-59a91d9415fa` | 118-125 [crates/gwiki/src/document.rs:118-125] | Indexed method `DocumentDegradationMatrix::markdown_section` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:118-125] |
| `document_degradation_matrix` | function | `fn document_degradation_matrix() {` | `document_degradation_matrix [function]` | `6188003d-adf7-5ac2-913b-ba1be9b1c190` | 133-217 [crates/gwiki/src/document.rs:133-217] | Indexed function `document_degradation_matrix` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:133-217] |
