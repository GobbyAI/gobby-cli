---
title: crates/gwiki/src/compile/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/render.rs
  ranges:
  - 11-47
  - 49-63
  - 65-105
  - 107-144
  - 146-182
  - 184-186
  - 188-190
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/compile/render.rs:11-47](crates/gwiki/src/compile/render.rs#L11-L47), [crates/gwiki/src/compile/render.rs:49-63](crates/gwiki/src/compile/render.rs#L49-L63), [crates/gwiki/src/compile/render.rs:65-105](crates/gwiki/src/compile/render.rs#L65-L105), [crates/gwiki/src/compile/render.rs:107-144](crates/gwiki/src/compile/render.rs#L107-L144), [crates/gwiki/src/compile/render.rs:146-182](crates/gwiki/src/compile/render.rs#L146-L182), [crates/gwiki/src/compile/render.rs:184-186](crates/gwiki/src/compile/render.rs#L184-L186), [crates/gwiki/src/compile/render.rs:188-190](crates/gwiki/src/compile/render.rs#L188-L190)

</details>

# crates/gwiki/src/compile/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds a rendered compile-bundle page and safely writes it to disk inside the wiki vault. `render_bundle` formats the bundle into Markdown sections for the topic outline, accepted sources, citations, conflicting claims, and missing evidence, while `render_list_section` handles the repeated “list or none recorded” section layout. `write_target_page` creates parent directories, validates the target path stays within the vault, and writes the rendered content, with `normalize_target_page`, `slugify`, and `unix_timestamp_ms` providing path normalization and naming/timestamp helpers used by the compile output flow.
[crates/gwiki/src/compile/render.rs:11-47]
[crates/gwiki/src/compile/render.rs:49-63]
[crates/gwiki/src/compile/render.rs:65-105]
[crates/gwiki/src/compile/render.rs:107-144]
[crates/gwiki/src/compile/render.rs:146-182]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_bundle` | function | `pub(crate) fn render_bundle(bundle: &CompileBundle) -> String {` | `render_bundle [function]` | `56943c0d-cfe8-5f14-b11b-ef9f9ecc2475` | 11-47 [crates/gwiki/src/compile/render.rs:11-47] | Indexed function `render_bundle` in `crates/gwiki/src/compile/render.rs`. [crates/gwiki/src/compile/render.rs:11-47] |
| `render_list_section` | function | `fn render_list_section(rendered: &mut String, title: &str, values: &[String]) {` | `render_list_section [function]` | `dd6472a3-a905-5843-99bf-6c5edb0de4c9` | 49-63 [crates/gwiki/src/compile/render.rs:49-63] | Indexed function `render_list_section` in `crates/gwiki/src/compile/render.rs`. [crates/gwiki/src/compile/render.rs:49-63] |
| `write_target_page` | function | `pub(crate) fn write_target_page(` | `write_target_page [function]` | `be4b6643-5374-525e-8c59-cb225be17d24` | 65-105 [crates/gwiki/src/compile/render.rs:65-105] | Indexed function `write_target_page` in `crates/gwiki/src/compile/render.rs`. [crates/gwiki/src/compile/render.rs:65-105] |
| `ensure_compile_target_parent_inside_vault` | function | `fn ensure_compile_target_parent_inside_vault(` | `ensure_compile_target_parent_inside_vault [function]` | `e08cbe81-33d5-5e97-a81b-d4655ca63529` | 107-144 [crates/gwiki/src/compile/render.rs:107-144] | Indexed function `ensure_compile_target_parent_inside_vault` in `crates/gwiki/src/compile/render.rs`. [crates/gwiki/src/compile/render.rs:107-144] |
| `normalize_target_page` | function | `pub(crate) fn normalize_target_page(` | `normalize_target_page [function]` | `ce3526ab-ec8a-5db7-ba9f-feebabfe95eb` | 146-182 [crates/gwiki/src/compile/render.rs:146-182] | Indexed function `normalize_target_page` in `crates/gwiki/src/compile/render.rs`. [crates/gwiki/src/compile/render.rs:146-182] |
| `slugify` | function | `pub(crate) fn slugify(topic: &str) -> String {` | `slugify [function]` | `3ec66435-b542-5a7c-8216-4e8d22ef9b5f` | 184-186 [crates/gwiki/src/compile/render.rs:184-186] | Indexed function `slugify` in `crates/gwiki/src/compile/render.rs`. [crates/gwiki/src/compile/render.rs:184-186] |
| `unix_timestamp_ms` | function | `pub(crate) fn unix_timestamp_ms() -> Result<u64, WikiError> {` | `unix_timestamp_ms [function]` | `abdea677-0cb5-5f29-8d6d-1d72dc6f098f` | 188-190 [crates/gwiki/src/compile/render.rs:188-190] | Indexed function `unix_timestamp_ms` in `crates/gwiki/src/compile/render.rs`. [crates/gwiki/src/compile/render.rs:188-190] |
