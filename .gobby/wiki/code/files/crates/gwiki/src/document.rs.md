---
title: crates/gwiki/src/document.rs
type: code_file
provenance:
- file: crates/gwiki/src/document.rs
  ranges:
  - 4-16
  - 18-34
  - 19-33
  - 37-40
  - 42-71
  - 43-48
  - 50-55
  - 57-62
  - 64-66
  - 68-70
  - 74-78
  - 80-96
  - 81-91
  - 93-95
  - '98'
  - 100-126
  - 101-116
  - 118-125
  - 133-217
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/document.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/document.rs` exposes 19 indexed API symbols.
[crates/gwiki/src/document.rs:4-16]
[crates/gwiki/src/document.rs:18-34]
[crates/gwiki/src/document.rs:19-33]
[crates/gwiki/src/document.rs:37-40]
[crates/gwiki/src/document.rs:42-71]

## API Symbols

- `DocumentFailureMode` (type) component `DocumentFailureMode [type]` (`637da746-dd23-52bf-a6ba-1dd755c1805d`) lines 4-16 [crates/gwiki/src/document.rs:4-16]
  - Signature: `pub enum DocumentFailureMode {`
  - Purpose: Indexed type `DocumentFailureMode` in `crates/gwiki/src/document.rs`. [crates/gwiki/src/document.rs:4-16]
- `DocumentFailureMode` (class) component `DocumentFailureMode [class]` (`40c19c8b-4e51-5e9d-b516-971695bc0f30`) lines 18-34 [crates/gwiki/src/document.rs:18-34]
  - Signature: `impl DocumentFailureMode {`
  - Purpose: The `as_str` method converts `DocumentFailureMode` enum variants into their corresponding static string literal representations for document processing failures across Office, HTML, and PDF formats. [crates/gwiki/src/document.rs:18-34]
- `DocumentFailureMode.as_str` (method) component `DocumentFailureMode.as_str [method]` (`80335ee5-2689-5027-b945-d4db97b5ae59`) lines 19-33 [crates/gwiki/src/document.rs:19-33]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Returns a static string representation of each document processing error enum variant. [crates/gwiki/src/document.rs:19-33]
- `DocumentUnitCount` (class) component `DocumentUnitCount [class]` (`65f6074c-ab55-591a-b637-2c51891a382a`) lines 37-40 [crates/gwiki/src/document.rs:37-40]
  - Signature: `pub struct DocumentUnitCount {`
  - Purpose: DocumentUnitCount is a public struct that associates a static string key with a usize count value for tracking document unit metrics. [crates/gwiki/src/document.rs:37-40]
- `DocumentUnitCount` (class) component `DocumentUnitCount [class]` (`9c46e5c3-9e68-5657-ae7f-c75dea7c0549`) lines 42-71 [crates/gwiki/src/document.rs:42-71]
  - Signature: `impl DocumentUnitCount {`
  - Purpose: DocumentUnitCount provides type-specific factory constructors that create instances with document unit type keys (page_count, sheet_count, slide_count) and exposes accessor methods for retrieving the key and count fields. [crates/gwiki/src/document.rs:42-71]
- `DocumentUnitCount.pages` (method) component `DocumentUnitCount.pages [method]` (`d6526ac2-f00a-5032-822c-3740d6a785f5`) lines 43-48 [crates/gwiki/src/document.rs:43-48]
  - Signature: `pub fn pages(count: usize) -> Self {`
  - Purpose: Constructs a new instance of `Self` with the `key` field set to `"page_count"` and the `count` field initialized to the provided `usize` argument. [crates/gwiki/src/document.rs:43-48]
- `DocumentUnitCount.sheets` (method) component `DocumentUnitCount.sheets [method]` (`35cd1a20-47a2-5958-8862-f1a6968bf067`) lines 50-55 [crates/gwiki/src/document.rs:50-55]
  - Signature: `pub fn sheets(count: usize) -> Self {`
  - Purpose: Constructs an instance of `Self` with the `key` field set to the literal string `"sheet_count"` and the `count` field set to the provided `usize` parameter. [crates/gwiki/src/document.rs:50-55]
- `DocumentUnitCount.slides` (method) component `DocumentUnitCount.slides [method]` (`24bb6f62-4949-55f2-bb92-7d4dde65f248`) lines 57-62 [crates/gwiki/src/document.rs:57-62]
  - Signature: `pub fn slides(count: usize) -> Self {`
  - Purpose: Constructs a new instance with the literal key `"slide_count"` and the provided `count` value. [crates/gwiki/src/document.rs:57-62]
- `DocumentUnitCount.key` (method) component `DocumentUnitCount.key [method]` (`a293c971-39c6-5c3b-aa6f-5efe1f6ed402`) lines 64-66 [crates/gwiki/src/document.rs:64-66]
  - Signature: `pub fn key(self) -> &'static str {`
  - Purpose: This method consumes self and returns a static string reference to the key field. [crates/gwiki/src/document.rs:64-66]
- `DocumentUnitCount.count` (method) component `DocumentUnitCount.count [method]` (`aeea1f97-8d6e-52c4-ad34-fdb365641909`) lines 68-70 [crates/gwiki/src/document.rs:68-70]
  - Signature: `pub fn count(self) -> usize {`
  - Purpose: # count

Consumes `self` and returns its `count` field as a `usize`. [crates/gwiki/src/document.rs:68-70]
- `DocumentDegradation` (class) component `DocumentDegradation [class]` (`774a272f-ec20-597c-913f-5b9b7c9b41bc`) lines 74-78 [crates/gwiki/src/document.rs:74-78]
  - Signature: `pub struct DocumentDegradation {`
  - Purpose: `DocumentDegradation` is a struct that manages graceful document failure handling by encapsulating a failure mode, unit count, and fallback string. [crates/gwiki/src/document.rs:74-78]
- `DocumentDegradation` (class) component `DocumentDegradation [class]` (`14b6d536-02fa-57ef-9cf3-9381c9bfd6f9`) lines 80-96 [crates/gwiki/src/document.rs:80-96]
  - Signature: `impl DocumentDegradation {`
  - Purpose: Encapsulates document degradation state comprising a failure mode, unit count, and string fallback, with a method to retrieve the failure mode's static string representation. [crates/gwiki/src/document.rs:80-96]
- `DocumentDegradation.new` (method) component `DocumentDegradation.new [method]` (`8d203c3e-ed93-59dd-a59a-2c5b82d59faf`) lines 81-91 [crates/gwiki/src/document.rs:81-91]
  - Signature: `pub fn new(`
  - Purpose: This constructor initializes a new instance with a `DocumentFailureMode`, `DocumentUnitCount`, and a fallback value generically converted into a `String` via the `Into` trait. [crates/gwiki/src/document.rs:81-91]
- `DocumentDegradation.reason` (method) component `DocumentDegradation.reason [method]` (`fef08e82-178f-5b7f-9aa3-0f3083753e86`) lines 93-95 [crates/gwiki/src/document.rs:93-95]
  - Signature: `pub fn reason(&self) -> &'static str {`
  - Purpose: The `reason` method returns a static string reference by converting the instance's `mode` field via the `as_str()` method. [crates/gwiki/src/document.rs:93-95]
- `DocumentDegradationMatrix` (class) component `DocumentDegradationMatrix [class]` (`b582a6bf-e3e9-5d58-9c7b-09475b92914b`) lines 98-98 [crates/gwiki/src/document.rs:98]
  - Signature: `pub struct DocumentDegradationMatrix;`
  - Purpose: DocumentDegradationMatrix is a zero-sized unit struct that likely serves as a marker type or namespace for document degradation operations. [crates/gwiki/src/document.rs:98]
- `DocumentDegradationMatrix` (class) component `DocumentDegradationMatrix [class]` (`e13625cc-4411-5819-b3d8-edae453b9623`) lines 100-126 [crates/gwiki/src/document.rs:100-126]
  - Signature: `impl DocumentDegradationMatrix {`
  - Purpose: DocumentDegradationMatrix provides static methods to serialize DocumentDegradation metadata as key-value tuples and markdown-formatted sections describing document parsing failures. [crates/gwiki/src/document.rs:100-126]
- `DocumentDegradationMatrix.metadata` (method) component `DocumentDegradationMatrix.metadata [method]` (`4a6f6f41-50b0-5263-a78b-0b162edf35b1`) lines 101-116 [crates/gwiki/src/document.rs:101-116]
  - Signature: `pub fn metadata(`
  - Purpose: Constructs and returns a vector of string key-value pairs containing file size and DocumentDegradation metrics (unit count and degradation reason). [crates/gwiki/src/document.rs:101-116]
- `DocumentDegradationMatrix.markdown_section` (method) component `DocumentDegradationMatrix.markdown_section [method]` (`97e3dbc3-d4e0-5238-85cb-59a91d9415fa`) lines 118-125 [crates/gwiki/src/document.rs:118-125]
  - Signature: `pub fn markdown_section(degradation: &DocumentDegradation) -> String {`
  - Purpose: Generates a markdown level-2 heading section documenting document parse failure by formatting the single-line degradation reason and fallback value separated by a colon. [crates/gwiki/src/document.rs:118-125]
- `document_degradation_matrix` (function) component `document_degradation_matrix [function]` (`6188003d-adf7-5ac2-913b-ba1be9b1c190`) lines 133-217 [crates/gwiki/src/document.rs:133-217]
  - Signature: `fn document_degradation_matrix() {`
  - Purpose: Initializes a test matrix mapping document processing failure modes (across Office, HTML, and PDF formats) to their corresponding unit counts and metric identifiers for degradation scenario testing. [crates/gwiki/src/document.rs:133-217]

