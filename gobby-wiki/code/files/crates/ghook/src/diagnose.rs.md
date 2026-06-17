---
title: crates/ghook/src/diagnose.rs
type: code_file
provenance:
- file: crates/ghook/src/diagnose.rs
  ranges:
  - 15-32
  - 42-45
  - 51-60
  - 62-70
  - 72-120
  - 128-134
  - 137-143
  - 146-152
  - 155-161
  - 164-170
  - 173-179
  - 181-188
  - 190-195
  - 198-210
  - 213-225
  - 228-231
  - 234-239
  - 242-264
  - 267-274
  - 277-284
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/diagnose.rs:15-32](crates/ghook/src/diagnose.rs#L15-L32), [crates/ghook/src/diagnose.rs:42-45](crates/ghook/src/diagnose.rs#L42-L45), [crates/ghook/src/diagnose.rs:51-60](crates/ghook/src/diagnose.rs#L51-L60), [crates/ghook/src/diagnose.rs:62-70](crates/ghook/src/diagnose.rs#L62-L70), [crates/ghook/src/diagnose.rs:72-120](crates/ghook/src/diagnose.rs#L72-L120), [crates/ghook/src/diagnose.rs:128-134](crates/ghook/src/diagnose.rs#L128-L134), [crates/ghook/src/diagnose.rs:137-143](crates/ghook/src/diagnose.rs#L137-L143), [crates/ghook/src/diagnose.rs:146-152](crates/ghook/src/diagnose.rs#L146-L152), [crates/ghook/src/diagnose.rs:155-161](crates/ghook/src/diagnose.rs#L155-L161), [crates/ghook/src/diagnose.rs:164-170](crates/ghook/src/diagnose.rs#L164-L170), [crates/ghook/src/diagnose.rs:173-179](crates/ghook/src/diagnose.rs#L173-L179), [crates/ghook/src/diagnose.rs:181-188](crates/ghook/src/diagnose.rs#L181-L188), [crates/ghook/src/diagnose.rs:190-195](crates/ghook/src/diagnose.rs#L190-L195), [crates/ghook/src/diagnose.rs:198-210](crates/ghook/src/diagnose.rs#L198-L210), [crates/ghook/src/diagnose.rs:213-225](crates/ghook/src/diagnose.rs#L213-L225), [crates/ghook/src/diagnose.rs:228-231](crates/ghook/src/diagnose.rs#L228-L231), [crates/ghook/src/diagnose.rs:234-239](crates/ghook/src/diagnose.rs#L234-L239), [crates/ghook/src/diagnose.rs:242-264](crates/ghook/src/diagnose.rs#L242-L264), [crates/ghook/src/diagnose.rs:267-274](crates/ghook/src/diagnose.rs#L267-L274), [crates/ghook/src/diagnose.rs:277-284](crates/ghook/src/diagnose.rs#L277-L284)

</details>

# crates/ghook/src/diagnose.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Implements `ghook --diagnose`, a pure introspection path that assembles a `DiagnoseOutput` JSON payload for a given CLI/hook configuration and validates it against the v2 diagnose-output schema. It carries core metadata such as schema/version, daemon and project info, CLI recognition, criticality, terminal-context state, and install provenance, with `read_install_provenance` and `install_provenance_for_running_binary` supplying best-effort sidecar metadata from `.ghook-install.json`. The remaining functions are targeted tests/helpers that verify hook classification, schema versioning, provenance parsing, and that the emitted diagnose output validates correctly.
[crates/ghook/src/diagnose.rs:15-32]
[crates/ghook/src/diagnose.rs:42-45]
[crates/ghook/src/diagnose.rs:51-60]
[crates/ghook/src/diagnose.rs:62-70]
[crates/ghook/src/diagnose.rs:72-120]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DiagnoseOutput` | class | `pub struct DiagnoseOutput {` | `DiagnoseOutput [class]` | `ea8d006f-58de-5e56-9585-3e3626837766` | 15-32 [crates/ghook/src/diagnose.rs:15-32] | Indexed class `DiagnoseOutput` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:15-32] |
| `InstallSidecar` | class | `struct InstallSidecar {` | `InstallSidecar [class]` | `066e347c-e0f8-580e-859e-f0d06f843f57` | 42-45 [crates/ghook/src/diagnose.rs:42-45] | Indexed class `InstallSidecar` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:42-45] |
| `read_install_provenance` | function | `pub fn read_install_provenance(dir: &Path) -> (Option<String>, Option<String>) {` | `read_install_provenance [function]` | `8ad675ee-8102-5b17-9be0-596b651dfb2d` | 51-60 [crates/ghook/src/diagnose.rs:51-60] | Indexed function `read_install_provenance` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:51-60] |
| `install_provenance_for_running_binary` | function | `fn install_provenance_for_running_binary() -> (Option<String>, Option<String>) {` | `install_provenance_for_running_binary [function]` | `fc376df5-19c5-581d-b3d2-f09e12350b71` | 62-70 [crates/ghook/src/diagnose.rs:62-70] | Indexed function `install_provenance_for_running_binary` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:62-70] |
| `diagnose` | function | `pub fn diagnose(cli: &str, hook_type: &str) -> DiagnoseOutput {` | `diagnose [function]` | `a992c00e-a5b1-52d1-95fe-4a2da82f0ca7` | 72-120 [crates/ghook/src/diagnose.rs:72-120] | Indexed function `diagnose` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:72-120] |
| `unknown_cli_marked_not_recognized` | function | `fn unknown_cli_marked_not_recognized() {` | `unknown_cli_marked_not_recognized [function]` | `03ff381b-511e-56de-96af-0cb6557a25d5` | 128-134 [crates/ghook/src/diagnose.rs:128-134] | Indexed function `unknown_cli_marked_not_recognized` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:128-134] |
| `claude_session_start_is_critical_with_terminal_context` | function | `fn claude_session_start_is_critical_with_terminal_context() {` | `claude_session_start_is_critical_with_terminal_context [function]` | `eccb2c13-3f5c-5c7c-a63e-4c670079d299` | 137-143 [crates/ghook/src/diagnose.rs:137-143] | Indexed function `claude_session_start_is_critical_with_terminal_context` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:137-143] |
| `codex_pre_tool_use_noncritical_without_terminal_context` | function | `fn codex_pre_tool_use_noncritical_without_terminal_context() {` | `codex_pre_tool_use_noncritical_without_terminal_context [function]` | `2ab1c8cb-1a26-526b-97e2-c3ced80e7439` | 146-152 [crates/ghook/src/diagnose.rs:146-152] | Indexed function `codex_pre_tool_use_noncritical_without_terminal_context` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:146-152] |
| `droid_session_start_is_recognized_noncritical_with_terminal_context_enabled` | function | `fn droid_session_start_is_recognized_noncritical_with_terminal_context_enabled() {` | `droid_session_start_is_recognized_noncritical_with_terminal_context_enabled [function]` | `14ae6661-fb9d-5b9e-95dd-ffd3a5d7a474` | 155-161 [crates/ghook/src/diagnose.rs:155-161] | Indexed function `droid_session_start_is_recognized_noncritical_with_terminal_context_enabled` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:155-161] |
| `grok_session_start_is_recognized_critical_with_terminal_context_enabled` | function | `fn grok_session_start_is_recognized_critical_with_terminal_context_enabled() {` | `grok_session_start_is_recognized_critical_with_terminal_context_enabled [function]` | `795a05af-c04d-5a73-ab94-9146d823e049` | 164-170 [crates/ghook/src/diagnose.rs:164-170] | Indexed function `grok_session_start_is_recognized_critical_with_terminal_context_enabled` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:164-170] |
| `grok_pre_tool_use_is_recognized_noncritical_without_terminal_context` | function | `fn grok_pre_tool_use_is_recognized_noncritical_without_terminal_context() {` | `grok_pre_tool_use_is_recognized_noncritical_without_terminal_context [function]` | `30bd626e-bc29-517c-bff3-1c4f93eac013` | 173-179 [crates/ghook/src/diagnose.rs:173-179] | Indexed function `grok_pre_tool_use_is_recognized_noncritical_without_terminal_context` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:173-179] |
| `compile_v2_schema` | function | `fn compile_v2_schema() -> jsonschema::JSONSchema {` | `compile_v2_schema [function]` | `5a382d07-9c7a-58a3-b3cd-b01b40a17632` | 181-188 [crates/ghook/src/diagnose.rs:181-188] | Indexed function `compile_v2_schema` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:181-188] |
| `assert_validates` | function | `fn assert_validates(schema: &jsonschema::JSONSchema, value: &serde_json::Value) {` | `assert_validates [function]` | `fe1b35b5-73e0-5aca-b6b5-d7f0a9925073` | 190-195 [crates/ghook/src/diagnose.rs:190-195] | Indexed function `assert_validates` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:190-195] |
| `diagnose_output_validates_against_v2_schema` | function | `fn diagnose_output_validates_against_v2_schema() {` | `diagnose_output_validates_against_v2_schema [function]` | `762d2a8d-cd34-51be-a027-3d4682d99336` | 198-210 [crates/ghook/src/diagnose.rs:198-210] | Indexed function `diagnose_output_validates_against_v2_schema` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:198-210] |
| `diagnose_output_for_unknown_cli_validates` | function | `fn diagnose_output_for_unknown_cli_validates() {` | `diagnose_output_for_unknown_cli_validates [function]` | `ae4c4cd0-16ce-55d0-9bc0-62c515937052` | 213-225 [crates/ghook/src/diagnose.rs:213-225] | Indexed function `diagnose_output_for_unknown_cli_validates` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:213-225] |
| `schema_version_is_two` | function | `fn schema_version_is_two() {` | `schema_version_is_two [function]` | `9db4fd22-c432-5442-999c-8c22131b75ae` | 228-231 [crates/ghook/src/diagnose.rs:228-231] | Indexed function `schema_version_is_two` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:228-231] |
| `install_provenance_absent_when_no_sidecar` | function | `fn install_provenance_absent_when_no_sidecar() {` | `install_provenance_absent_when_no_sidecar [function]` | `7b80b2bf-ff43-530a-9b7b-c6d492f8da75` | 234-239 [crates/ghook/src/diagnose.rs:234-239] | Indexed function `install_provenance_absent_when_no_sidecar` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:234-239] |
| `install_provenance_read_from_sidecar` | function | `fn install_provenance_read_from_sidecar() {` | `install_provenance_read_from_sidecar [function]` | `f133e890-2d7f-50e6-9f8a-b3a5c9a3865d` | 242-264 [crates/ghook/src/diagnose.rs:242-264] | Indexed function `install_provenance_read_from_sidecar` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:242-264] |
| `install_provenance_partial_sidecar_returns_present_fields` | function | `fn install_provenance_partial_sidecar_returns_present_fields() {` | `install_provenance_partial_sidecar_returns_present_fields [function]` | `ef10527d-4b79-5e46-9ab9-25aa755fd0a1` | 267-274 [crates/ghook/src/diagnose.rs:267-274] | Indexed function `install_provenance_partial_sidecar_returns_present_fields` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:267-274] |
| `install_provenance_malformed_json_collapses_to_none` | function | `fn install_provenance_malformed_json_collapses_to_none() {` | `install_provenance_malformed_json_collapses_to_none [function]` | `344fc7a0-6867-598f-b4c1-a52a530fada0` | 277-284 [crates/ghook/src/diagnose.rs:277-284] | Indexed function `install_provenance_malformed_json_collapses_to_none` in `crates/ghook/src/diagnose.rs`. [crates/ghook/src/diagnose.rs:277-284] |
