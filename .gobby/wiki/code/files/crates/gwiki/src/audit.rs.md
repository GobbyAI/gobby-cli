---
title: crates/gwiki/src/audit.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit.rs
  ranges:
  - 36-38
  - 40-76
  - 78-87
  - 90-96
  - 99-106
  - 109-114
  - 117-119
  - 121-144
  - 146-158
  - 160-167
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/audit.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the wiki audit pipeline: it defines `AuditOptions` for building a case-insensitive ignored-section set from defaults, environment, or extra inputs, and data types for the resulting `AuditReport`, `UnsupportedClaim`, and `AuditSourceContext`. The top-level `run`/`run_with_options` flow collects scoped pages, loads source context and provenance, computes unsupported claims using the audit options, and returns a consolidated report; `source_context` and `load_provenance` provide the supporting metadata sources.
[crates/gwiki/src/audit.rs:36-38]
[crates/gwiki/src/audit.rs:40-76]
[crates/gwiki/src/audit.rs:41-47]
[crates/gwiki/src/audit.rs:50-57]
[crates/gwiki/src/audit.rs:59-62]

## API Symbols

- `AuditOptions` (class) component `AuditOptions [class]` (`7a00edb9-9f8d-5551-843e-2d4802cbd8ad`) lines 36-38 [crates/gwiki/src/audit.rs:36-38]
  - Signature: `pub struct AuditOptions {`
  - Purpose: Indexed class `AuditOptions` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:36-38]
- `AuditOptions` (class) component `AuditOptions [class]` (`f73b01b2-de57-5b3b-967a-b445e16e1fb9`) lines 40-76 [crates/gwiki/src/audit.rs:40-76]
  - Signature: `impl AuditOptions {`
  - Purpose: 'AuditOptions' is a configuration object that builds its state from defaults plus a comma-separated environment variable, normalizes ignored section names by trimming and lowercasing them, and provides helpers to extend and test case-insensitive section-ignore membership. [crates/gwiki/src/audit.rs:40-76]
- `AuditOptions.from_env` (method) component `AuditOptions.from_env [method]` (`371ed3e0-ab16-5a4a-96a9-6a176f597d03`) lines 41-47 [crates/gwiki/src/audit.rs:41-47]
  - Signature: `pub fn from_env() -> Self {`
  - Purpose: Constructs a default 'Self' value and, if the 'IGNORED_SECTIONS_ENV' environment variable is set, extends its ignored sections with the comma-separated entries from that variable. [crates/gwiki/src/audit.rs:41-47]
- `AuditOptions.with_additional_ignored_sections` (method) component `AuditOptions.with_additional_ignored_sections [method]` (`88810d0b-1b77-5926-943f-99ad7c1220d7`) lines 50-57 [crates/gwiki/src/audit.rs:50-57]
  - Signature: `pub fn with_additional_ignored_sections<I, S>(mut self, sections: I) -> Self`
  - Purpose: Consumes and returns 'self' after extending its ignored-section set with every string-like section provided by the given iterator. [crates/gwiki/src/audit.rs:50-57]
- `AuditOptions.ignores_section` (method) component `AuditOptions.ignores_section [method]` (`8e563f04-b752-5466-ad68-0d84fe8338ab`) lines 59-62 [crates/gwiki/src/audit.rs:59-62]
  - Signature: `fn ignores_section(&self, heading: &str) -> bool {`
  - Purpose: Returns 'true' if the provided heading, after trimming and converting to ASCII lowercase, is present in 'self.ignored_sections'; otherwise returns 'false'. [crates/gwiki/src/audit.rs:59-62]
- `AuditOptions.extend_ignored_sections` (method) component `AuditOptions.extend_ignored_sections [method]` (`cf416c70-9547-5894-ade2-0c2ad1b6a299`) lines 64-75 [crates/gwiki/src/audit.rs:64-75]
  - Signature: `fn extend_ignored_sections<I, S>(&mut self, sections: I)`
  - Purpose: Extends 'self.ignored_sections' by iterating over the provided items, trimming each string, converting it to ASCII lowercase, and inserting only non-empty results. [crates/gwiki/src/audit.rs:64-75]
- `AuditOptions` (class) component `AuditOptions [class]` (`31191875-e3a0-556d-82e7-8fad03434b29`) lines 78-87 [crates/gwiki/src/audit.rs:78-87]
  - Signature: `impl Default for AuditOptions {`
  - Purpose: 'AuditOptions' implements 'Default' by constructing a value whose 'ignored_sections' field is populated with owned 'String's cloned from 'DEFAULT_IGNORED_SECTIONS'. [crates/gwiki/src/audit.rs:78-87]
- `AuditOptions.default` (method) component `AuditOptions.default [method]` (`8e9122ed-c1e5-56ea-a4b1-b8adca9e4e0d`) lines 79-86 [crates/gwiki/src/audit.rs:79-86]
  - Signature: `fn default() -> Self {`
  - Purpose: Constructs 'Self' by populating 'ignored_sections' with an owned collection of 'String's cloned from 'DEFAULT_IGNORED_SECTIONS'. [crates/gwiki/src/audit.rs:79-86]
- `AuditReport` (class) component `AuditReport [class]` (`b61e26c0-467b-54f4-8d69-3f8e249e87d8`) lines 90-96 [crates/gwiki/src/audit.rs:90-96]
  - Signature: `pub struct AuditReport {`
  - Purpose: 'AuditReport' is a data container for an audit result, holding the audited command, target scope identity, root path, a list of unsupported claims, and shared source context metadata. [crates/gwiki/src/audit.rs:90-96]
- `UnsupportedClaim` (class) component `UnsupportedClaim [class]` (`9c60ef97-0ca7-500c-bb42-9bc21b3800ca`) lines 99-106 [crates/gwiki/src/audit.rs:99-106]
  - Signature: `pub struct UnsupportedClaim {`
  - Purpose: Indexed class `UnsupportedClaim` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:99-106]
- `AuditSourceContext` (class) component `AuditSourceContext [class]` (`c952655e-97b5-55fb-9bca-a0affd123eb6`) lines 109-114 [crates/gwiki/src/audit.rs:109-114]
  - Signature: `pub struct AuditSourceContext {`
  - Purpose: 'AuditSourceContext' is a data-only struct that identifies an audit source by mandatory 'source_id' and optional 'path', 'citation', and 'location' metadata. [crates/gwiki/src/audit.rs:109-114]
- `run` (function) component `run [function]` (`3cc18e77-0373-5498-b0df-cf4a483e6b23`) lines 117-119 [crates/gwiki/src/audit.rs:117-119]
  - Signature: `pub fn run(vault_root: &Path, scope: ScopeIdentity) -> Result<AuditReport, WikiError> {`
  - Purpose: Invokes 'run_with_options' with 'AuditOptions::from_env()' to produce an 'AuditReport' for the given 'vault_root' and 'scope'. [crates/gwiki/src/audit.rs:117-119]
- `run_with_options` (function) component `run_with_options [function]` (`ba746a57-9125-54df-be6d-695d4bb6024d`) lines 121-144 [crates/gwiki/src/audit.rs:121-144]
  - Signature: `pub fn run_with_options(`
  - Purpose: Collects pages under 'vault_root' that match 'scope', builds shared source context and provenance, computes all unsupported claims for those pages using 'options', and returns an 'AuditReport' containing the audit command, scope, root path, source context, and aggregated unsupported claims. [crates/gwiki/src/audit.rs:121-144]
- `source_context` (function) component `source_context [function]` (`db356499-0beb-5310-bffa-13a9fcb90ab0`) lines 146-158 [crates/gwiki/src/audit.rs:146-158]
  - Signature: `fn source_context(vault_root: &Path) -> Result<Vec<AuditSourceContext>, WikiError> {`
  - Purpose: Reads the source manifest from 'vault_root' and converts each manifest entry into an 'AuditSourceContext' with a 'raw/{id}.md' path, preserving the entry’s 'id', 'citation', and 'location'. [crates/gwiki/src/audit.rs:146-158]
- `load_provenance` (function) component `load_provenance [function]` (`b2b4bcd1-ab2e-5461-8c36-d6eacdffbac3`) lines 160-167 [crates/gwiki/src/audit.rs:160-167]
  - Signature: `fn load_provenance(vault_root: &Path) -> Result<ProvenanceGraph, WikiError> {`
  - Purpose: Loads 'meta/provenance.json' from the given vault via 'ProvenanceGraph::load_from_vault(vault_root)' when the file exists, otherwise returns 'Ok(ProvenanceGraph::default())'. [crates/gwiki/src/audit.rs:160-167]

