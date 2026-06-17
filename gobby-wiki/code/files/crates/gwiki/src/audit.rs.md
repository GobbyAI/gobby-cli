---
title: crates/gwiki/src/audit.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit.rs
  ranges:
  - 36-38
  - 41-47
  - 50-57
  - 59-62
  - 64-75
  - 79-86
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/audit.rs:36-38](crates/gwiki/src/audit.rs#L36-L38), [crates/gwiki/src/audit.rs:41-47](crates/gwiki/src/audit.rs#L41-L47), [crates/gwiki/src/audit.rs:50-57](crates/gwiki/src/audit.rs#L50-L57), [crates/gwiki/src/audit.rs:59-62](crates/gwiki/src/audit.rs#L59-L62), [crates/gwiki/src/audit.rs:64-75](crates/gwiki/src/audit.rs#L64-L75), [crates/gwiki/src/audit.rs:79-86](crates/gwiki/src/audit.rs#L79-L86), [crates/gwiki/src/audit.rs:90-96](crates/gwiki/src/audit.rs#L90-L96), [crates/gwiki/src/audit.rs:99-106](crates/gwiki/src/audit.rs#L99-L106), [crates/gwiki/src/audit.rs:109-114](crates/gwiki/src/audit.rs#L109-L114), [crates/gwiki/src/audit.rs:117-119](crates/gwiki/src/audit.rs#L117-L119), [crates/gwiki/src/audit.rs:121-144](crates/gwiki/src/audit.rs#L121-L144), [crates/gwiki/src/audit.rs:146-158](crates/gwiki/src/audit.rs#L146-L158), [crates/gwiki/src/audit.rs:160-167](crates/gwiki/src/audit.rs#L160-L167)

</details>

# crates/gwiki/src/audit.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the wiki audit pipeline and its data model. `AuditOptions` builds the set of ignored section headings from defaults, environment, or extra caller-supplied sections, and its lookup helpers normalize headings before checking them. `run` and `run_with_options` drive the audit over a scoped wiki root by collecting pages, loading provenance, deriving source context, and producing an `AuditReport` that includes any `UnsupportedClaim` entries. `source_context` and `load_provenance` provide the supporting data used to connect page content back to provenance and source manifests, while `render_text` exposes the text renderer for audit output.
[crates/gwiki/src/audit.rs:36-38]
[crates/gwiki/src/audit.rs:41-47]
[crates/gwiki/src/audit.rs:50-57]
[crates/gwiki/src/audit.rs:59-62]
[crates/gwiki/src/audit.rs:64-75]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `AuditOptions` | class | `pub struct AuditOptions {` | `AuditOptions [class]` | `7a00edb9-9f8d-5551-843e-2d4802cbd8ad` | 36-38 [crates/gwiki/src/audit.rs:36-38] | Indexed class `AuditOptions` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:36-38] |
| `AuditOptions::from_env` | method | `pub fn from_env() -> Self {` | `AuditOptions::from_env [method]` | `371ed3e0-ab16-5a4a-96a9-6a176f597d03` | 41-47 [crates/gwiki/src/audit.rs:41-47] | Indexed method `AuditOptions::from_env` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:41-47] |
| `AuditOptions::with_additional_ignored_sections` | method | `pub fn with_additional_ignored_sections<I, S>(mut self, sections: I) -> Self` | `AuditOptions::with_additional_ignored_sections [method]` | `88810d0b-1b77-5926-943f-99ad7c1220d7` | 50-57 [crates/gwiki/src/audit.rs:50-57] | Indexed method `AuditOptions::with_additional_ignored_sections` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:50-57] |
| `AuditOptions::ignores_section` | method | `fn ignores_section(&self, heading: &str) -> bool {` | `AuditOptions::ignores_section [method]` | `8e563f04-b752-5466-ad68-0d84fe8338ab` | 59-62 [crates/gwiki/src/audit.rs:59-62] | Indexed method `AuditOptions::ignores_section` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:59-62] |
| `AuditOptions::extend_ignored_sections` | method | `fn extend_ignored_sections<I, S>(&mut self, sections: I)` | `AuditOptions::extend_ignored_sections [method]` | `cf416c70-9547-5894-ade2-0c2ad1b6a299` | 64-75 [crates/gwiki/src/audit.rs:64-75] | Indexed method `AuditOptions::extend_ignored_sections` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:64-75] |
| `AuditOptions::default` | method | `fn default() -> Self {` | `AuditOptions::default [method]` | `8e9122ed-c1e5-56ea-a4b1-b8adca9e4e0d` | 79-86 [crates/gwiki/src/audit.rs:79-86] | Indexed method `AuditOptions::default` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:79-86] |
| `AuditReport` | class | `pub struct AuditReport {` | `AuditReport [class]` | `b61e26c0-467b-54f4-8d69-3f8e249e87d8` | 90-96 [crates/gwiki/src/audit.rs:90-96] | Indexed class `AuditReport` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:90-96] |
| `UnsupportedClaim` | class | `pub struct UnsupportedClaim {` | `UnsupportedClaim [class]` | `9c60ef97-0ca7-500c-bb42-9bc21b3800ca` | 99-106 [crates/gwiki/src/audit.rs:99-106] | Indexed class `UnsupportedClaim` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:99-106] |
| `AuditSourceContext` | class | `pub struct AuditSourceContext {` | `AuditSourceContext [class]` | `c952655e-97b5-55fb-9bca-a0affd123eb6` | 109-114 [crates/gwiki/src/audit.rs:109-114] | Indexed class `AuditSourceContext` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:109-114] |
| `run` | function | `pub fn run(vault_root: &Path, scope: ScopeIdentity) -> Result<AuditReport, WikiError> {` | `run [function]` | `3cc18e77-0373-5498-b0df-cf4a483e6b23` | 117-119 [crates/gwiki/src/audit.rs:117-119] | Indexed function `run` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:117-119] |
| `run_with_options` | function | `pub fn run_with_options(` | `run_with_options [function]` | `ba746a57-9125-54df-be6d-695d4bb6024d` | 121-144 [crates/gwiki/src/audit.rs:121-144] | Indexed function `run_with_options` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:121-144] |
| `source_context` | function | `fn source_context(vault_root: &Path) -> Result<Vec<AuditSourceContext>, WikiError> {` | `source_context [function]` | `db356499-0beb-5310-bffa-13a9fcb90ab0` | 146-158 [crates/gwiki/src/audit.rs:146-158] | Indexed function `source_context` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:146-158] |
| `load_provenance` | function | `fn load_provenance(vault_root: &Path) -> Result<ProvenanceGraph, WikiError> {` | `load_provenance [function]` | `b2b4bcd1-ab2e-5461-8c36-d6eacdffbac3` | 160-167 [crates/gwiki/src/audit.rs:160-167] | Indexed function `load_provenance` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:160-167] |
