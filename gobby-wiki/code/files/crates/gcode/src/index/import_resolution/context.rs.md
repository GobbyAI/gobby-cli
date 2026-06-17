---
title: crates/gcode/src/index/import_resolution/context.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context.rs
  ranges:
  - 41-138
  - 144-146
  - 151-166
  - 170-187
  - 194-206
  - 212-214
  - 220-225
  - 231-236
  - 241-246
  - 248-253
  - 255-277
  - 279-284
  - 286-291
  - 297-302
  - 309-319
  - 321-326
  - 328-333
  - 335-340
  - 345-350
  - 353-363
  - 365-409
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context.rs:41-138](crates/gcode/src/index/import_resolution/context.rs#L41-L138), [crates/gcode/src/index/import_resolution/context.rs:144-146](crates/gcode/src/index/import_resolution/context.rs#L144-L146), [crates/gcode/src/index/import_resolution/context.rs:151-166](crates/gcode/src/index/import_resolution/context.rs#L151-L166), [crates/gcode/src/index/import_resolution/context.rs:170-187](crates/gcode/src/index/import_resolution/context.rs#L170-L187), [crates/gcode/src/index/import_resolution/context.rs:194-206](crates/gcode/src/index/import_resolution/context.rs#L194-L206), [crates/gcode/src/index/import_resolution/context.rs:212-214](crates/gcode/src/index/import_resolution/context.rs#L212-L214), [crates/gcode/src/index/import_resolution/context.rs:220-225](crates/gcode/src/index/import_resolution/context.rs#L220-L225), [crates/gcode/src/index/import_resolution/context.rs:231-236](crates/gcode/src/index/import_resolution/context.rs#L231-L236), [crates/gcode/src/index/import_resolution/context.rs:241-246](crates/gcode/src/index/import_resolution/context.rs#L241-L246), [crates/gcode/src/index/import_resolution/context.rs:248-253](crates/gcode/src/index/import_resolution/context.rs#L248-L253), [crates/gcode/src/index/import_resolution/context.rs:255-277](crates/gcode/src/index/import_resolution/context.rs#L255-L277), [crates/gcode/src/index/import_resolution/context.rs:279-284](crates/gcode/src/index/import_resolution/context.rs#L279-L284), [crates/gcode/src/index/import_resolution/context.rs:286-291](crates/gcode/src/index/import_resolution/context.rs#L286-L291), [crates/gcode/src/index/import_resolution/context.rs:297-302](crates/gcode/src/index/import_resolution/context.rs#L297-L302), [crates/gcode/src/index/import_resolution/context.rs:309-319](crates/gcode/src/index/import_resolution/context.rs#L309-L319), [crates/gcode/src/index/import_resolution/context.rs:321-326](crates/gcode/src/index/import_resolution/context.rs#L321-L326), [crates/gcode/src/index/import_resolution/context.rs:328-333](crates/gcode/src/index/import_resolution/context.rs#L328-L333), [crates/gcode/src/index/import_resolution/context.rs:335-340](crates/gcode/src/index/import_resolution/context.rs#L335-L340), [crates/gcode/src/index/import_resolution/context.rs:345-350](crates/gcode/src/index/import_resolution/context.rs#L345-L350), [crates/gcode/src/index/import_resolution/context.rs:353-363](crates/gcode/src/index/import_resolution/context.rs#L353-L363), [crates/gcode/src/index/import_resolution/context.rs:365-409](crates/gcode/src/index/import_resolution/context.rs#L365-L409)

</details>

# crates/gcode/src/index/import_resolution/context.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Defines `ImportResolutionContext`, a shared index of language-specific package, module, crate, class, and symbol mappings used to resolve imports and qualified references across the codebase. Its methods expose candidate files or declared targets for each supported ecosystem, while `build_import_resolution_context` and `build_import_resolution_context_with_overrides` assemble the context from discovered package metadata and local indexes, optionally applying caller-supplied overrides.
[crates/gcode/src/index/import_resolution/context.rs:41-138]
[crates/gcode/src/index/import_resolution/context.rs:144-146]
[crates/gcode/src/index/import_resolution/context.rs:151-166]
[crates/gcode/src/index/import_resolution/context.rs:170-187]
[crates/gcode/src/index/import_resolution/context.rs:194-206]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ImportResolutionContext` | class | `pub struct ImportResolutionContext {` | `ImportResolutionContext [class]` | `f65f153c-1b60-51f0-b675-548654e17587` | 41-138 [crates/gcode/src/index/import_resolution/context.rs:41-138] | Indexed class `ImportResolutionContext` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:41-138] |
| `ImportResolutionContext::js_candidate_files` | method | `pub(super) fn js_candidate_files(&self, rel_path: &str, specifier: &str) -> Vec<String> {` | `ImportResolutionContext::js_candidate_files [method]` | `da8e2247-b179-55c3-82d5-095967fcf9fe` | 144-146 [crates/gcode/src/index/import_resolution/context.rs:144-146] | Indexed method `ImportResolutionContext::js_candidate_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:144-146] |
| `ImportResolutionContext::rust_import_candidate` | method | `pub(super) fn rust_import_candidate(` | `ImportResolutionContext::rust_import_candidate [method]` | `1216800d-8c27-50d8-b37f-64887886404e` | 151-166 [crates/gcode/src/index/import_resolution/context.rs:151-166] | Indexed method `ImportResolutionContext::rust_import_candidate` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:151-166] |
| `ImportResolutionContext::rust_qualified_candidate` | method | `pub(super) fn rust_qualified_candidate(` | `ImportResolutionContext::rust_qualified_candidate [method]` | `f3ceb52b-49ce-5d5f-9e33-1124e525cbf5` | 170-187 [crates/gcode/src/index/import_resolution/context.rs:170-187] | Indexed method `ImportResolutionContext::rust_qualified_candidate` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:170-187] |
| `ImportResolutionContext::go_candidate_files` | method | `pub(super) fn go_candidate_files(&self, module: &str) -> Vec<String> {` | `ImportResolutionContext::go_candidate_files [method]` | `1d1d7443-c3db-58ed-8c26-f2b531cd6065` | 194-206 [crates/gcode/src/index/import_resolution/context.rs:194-206] | Indexed method `ImportResolutionContext::go_candidate_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:194-206] |
| `ImportResolutionContext::java_candidate_files` | method | `pub(super) fn java_candidate_files(&self, fqcn: &str) -> Vec<String> {` | `ImportResolutionContext::java_candidate_files [method]` | `6580a3ef-4d2d-5e87-8360-67d2a1d5bb9a` | 212-214 [crates/gcode/src/index/import_resolution/context.rs:212-214] | Indexed method `ImportResolutionContext::java_candidate_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:212-214] |
| `ImportResolutionContext::csharp_type_files` | method | `pub(super) fn csharp_type_files(&self, type_path: &str) -> Vec<String> {` | `ImportResolutionContext::csharp_type_files [method]` | `79e53299-330c-59f6-98cf-179facd661da` | 220-225 [crates/gcode/src/index/import_resolution/context.rs:220-225] | Indexed method `ImportResolutionContext::csharp_type_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:220-225] |
| `ImportResolutionContext::kotlin_package_files` | method | `pub(super) fn kotlin_package_files(&self, package: &str) -> Vec<String> {` | `ImportResolutionContext::kotlin_package_files [method]` | `9dcfa09c-cc6c-5c0c-8ad5-00f5fc7d679e` | 231-236 [crates/gcode/src/index/import_resolution/context.rs:231-236] | Indexed method `ImportResolutionContext::kotlin_package_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:231-236] |
| `ImportResolutionContext::scala_package_files` | method | `pub(super) fn scala_package_files(&self, package: &str) -> Vec<String> {` | `ImportResolutionContext::scala_package_files [method]` | `ff07a336-d6a6-52d7-bcc3-6fa8723b3416` | 241-246 [crates/gcode/src/index/import_resolution/context.rs:241-246] | Indexed method `ImportResolutionContext::scala_package_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:241-246] |
| `ImportResolutionContext::lua_module_files` | method | `pub(super) fn lua_module_files(&self, module: &str) -> Vec<String> {` | `ImportResolutionContext::lua_module_files [method]` | `74679e92-ae14-53aa-8dca-b8fbc709e993` | 248-253 [crates/gcode/src/index/import_resolution/context.rs:248-253] | Indexed method `ImportResolutionContext::lua_module_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:248-253] |
| `ImportResolutionContext::objc_import_candidate_files` | method | `pub(super) fn objc_import_candidate_files(` | `ImportResolutionContext::objc_import_candidate_files [method]` | `263ca027-5944-5993-8746-f36c8407578e` | 255-277 [crates/gcode/src/index/import_resolution/context.rs:255-277] | Indexed method `ImportResolutionContext::objc_import_candidate_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:255-277] |
| `ImportResolutionContext::objc_declared_types` | method | `pub(super) fn objc_declared_types(&self, rel_path: &str) -> Vec<String> {` | `ImportResolutionContext::objc_declared_types [method]` | `c24b988e-b2ac-5296-9b3e-ec22fec102c8` | 279-284 [crates/gcode/src/index/import_resolution/context.rs:279-284] | Indexed method `ImportResolutionContext::objc_declared_types` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:279-284] |
| `ImportResolutionContext::objc_declared_functions` | method | `pub(super) fn objc_declared_functions(&self, rel_path: &str) -> Vec<String> {` | `ImportResolutionContext::objc_declared_functions [method]` | `1c232509-3702-5056-92ea-0b37b5a5d8c5` | 286-291 [crates/gcode/src/index/import_resolution/context.rs:286-291] | Indexed method `ImportResolutionContext::objc_declared_functions` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:286-291] |
| `ImportResolutionContext::php_candidate_files` | method | `pub(super) fn php_candidate_files(&self, name: &str) -> Vec<String> {` | `ImportResolutionContext::php_candidate_files [method]` | `2888faba-e331-5360-a2f7-644ce486d59a` | 297-302 [crates/gcode/src/index/import_resolution/context.rs:297-302] | Indexed method `ImportResolutionContext::php_candidate_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:297-302] |
| `ImportResolutionContext::swift_module_candidate_files` | method | `pub(super) fn swift_module_candidate_files(&self, rel_path: &str) -> Vec<String> {` | `ImportResolutionContext::swift_module_candidate_files [method]` | `5789d02b-9abf-530f-98b2-af1896ab6442` | 309-319 [crates/gcode/src/index/import_resolution/context.rs:309-319] | Indexed method `ImportResolutionContext::swift_module_candidate_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:309-319] |
| `ImportResolutionContext::ruby_require_root` | method | `pub(super) fn ruby_require_root(&self, required: &str) -> Option<&str> {` | `ImportResolutionContext::ruby_require_root [method]` | `3842b8db-f242-5494-8874-f24dc7efa95f` | 321-326 [crates/gcode/src/index/import_resolution/context.rs:321-326] | Indexed method `ImportResolutionContext::ruby_require_root` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:321-326] |
| `ImportResolutionContext::ruby_constant_files` | method | `pub(super) fn ruby_constant_files(&self, root: &str) -> Vec<String> {` | `ImportResolutionContext::ruby_constant_files [method]` | `1e3eabf0-06ef-52cd-8cd4-677dc0f3af48` | 328-333 [crates/gcode/src/index/import_resolution/context.rs:328-333] | Indexed method `ImportResolutionContext::ruby_constant_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:328-333] |
| `ImportResolutionContext::elixir_external_root_module` | method | `pub(super) fn elixir_external_root_module(&self, root: &str) -> Option<&str> {` | `ImportResolutionContext::elixir_external_root_module [method]` | `7ef21e50-5fe1-58cf-ba23-d0ca2c71e9ba` | 335-340 [crates/gcode/src/index/import_resolution/context.rs:335-340] | Indexed method `ImportResolutionContext::elixir_external_root_module` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:335-340] |
| `ImportResolutionContext::elixir_module_files` | method | `pub(super) fn elixir_module_files(&self, module: &str) -> Vec<String> {` | `ImportResolutionContext::elixir_module_files [method]` | `3004176b-da64-5bc7-869a-61cc97466cab` | 345-350 [crates/gcode/src/index/import_resolution/context.rs:345-350] | Indexed method `ImportResolutionContext::elixir_module_files` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:345-350] |
| `build_import_resolution_context` | function | `pub fn build_import_resolution_context(` | `build_import_resolution_context [function]` | `2e0502cf-e815-550f-84b5-bd5eaeb7d013` | 353-363 [crates/gcode/src/index/import_resolution/context.rs:353-363] | Indexed function `build_import_resolution_context` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:353-363] |
| `build_import_resolution_context_with_overrides` | function | `pub fn build_import_resolution_context_with_overrides(` | `build_import_resolution_context_with_overrides [function]` | `25e5e0eb-7912-5924-8f9d-46eba8ad88e6` | 365-409 [crates/gcode/src/index/import_resolution/context.rs:365-409] | Indexed function `build_import_resolution_context_with_overrides` in `crates/gcode/src/index/import_resolution/context.rs`. [crates/gcode/src/index/import_resolution/context.rs:365-409] |
