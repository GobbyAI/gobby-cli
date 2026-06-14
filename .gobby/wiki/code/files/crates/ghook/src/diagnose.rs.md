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
  - 163-170
  - 172-177
  - 180-192
  - 195-207
  - 210-213
  - 216-221
  - 224-246
  - 249-256
  - 259-266
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/diagnose.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Builds the `ghook --diagnose` introspection output: it assembles a schema-versioned JSON report describing the current CLI/hook invocation, daemon connection details, project context, terminal-context state, CLI recognition, and install provenance for the running binary. The helper functions read optional `.ghook-install.json` sidecar metadata and locate it beside the executable, while the tests verify CLI-specific criticality/source behavior and that the output and provenance parsing conform to the v2 schema and failure-tolerant sidecar rules.
[crates/ghook/src/diagnose.rs:15-32]
[crates/ghook/src/diagnose.rs:42-45]
[crates/ghook/src/diagnose.rs:51-60]
[crates/ghook/src/diagnose.rs:62-70]
[crates/ghook/src/diagnose.rs:72-120]

## API Symbols

- `DiagnoseOutput` (class) component `DiagnoseOutput [class]` (`ea8d006f-58de-5e56-9585-3e3626837766`) lines 15-32 [crates/ghook/src/diagnose.rs:15-32]
  - Signature: `pub struct DiagnoseOutput {`
  - Purpose: `DiagnoseOutput` is a diagnostic struct that aggregates metadata about a Git hook installation, including version information, hook configuration, daemon connectivity parameters, project context, and installation details. [crates/ghook/src/diagnose.rs:15-32]
- `InstallSidecar` (class) component `InstallSidecar [class]` (`066e347c-e0f8-580e-859e-f0d06f843f57`) lines 42-45 [crates/ghook/src/diagnose.rs:42-45]
  - Signature: `struct InstallSidecar {`
  - Purpose: `InstallSidecar` is a struct that encapsulates optional configuration parameters for sidecar installation, comprising an installation method and source URL. [crates/ghook/src/diagnose.rs:42-45]
- `read_install_provenance` (function) component `read_install_provenance [function]` (`8ad675ee-8102-5b17-9be0-596b651dfb2d`) lines 51-60 [crates/ghook/src/diagnose.rs:51-60]
  - Signature: `pub fn read_install_provenance(dir: &Path) -> (Option<String>, Option<String>) {`
  - Purpose: Deserializes a JSON install sidecar file from the specified directory and returns the install method and source URL as an optional tuple, or `(None, None)` if the file cannot be read or parsed. [crates/ghook/src/diagnose.rs:51-60]
- `install_provenance_for_running_binary` (function) component `install_provenance_for_running_binary [function]` (`fc376df5-19c5-581d-b3d2-f09e12350b71`) lines 62-70 [crates/ghook/src/diagnose.rs:62-70]
  - Signature: `fn install_provenance_for_running_binary() -> (Option<String>, Option<String>) {`
  - Purpose: This function retrieves installation provenance metadata from the parent directory of the currently executing binary, returning a tuple of two optional strings or (None, None) if the executable path cannot be determined. [crates/ghook/src/diagnose.rs:62-70]
- `diagnose` (function) component `diagnose [function]` (`a992c00e-a5b1-52d1-95fe-4a2da82f0ca7`) lines 72-120 [crates/ghook/src/diagnose.rs:72-120]
  - Signature: `pub fn diagnose(cli: &str, hook_type: &str) -> DiagnoseOutput {`
  - Purpose: Collects and returns diagnostic metadata about a git hook's execution context, including CLI configuration, daemon connectivity, project identification, hook criticality, and binary installation provenance. [crates/ghook/src/diagnose.rs:72-120]
- `unknown_cli_marked_not_recognized` (function) component `unknown_cli_marked_not_recognized [function]` (`03ff381b-511e-56de-96af-0cb6557a25d5`) lines 128-134 [crates/ghook/src/diagnose.rs:128-134]
  - Signature: `fn unknown_cli_marked_not_recognized() {`
  - Purpose: This test asserts that diagnosing an unknown "cursor" CLI at "session-start" produces a diagnosis with unrecognized status, no source, non-critical severity, and disabled terminal context. [crates/ghook/src/diagnose.rs:128-134]
- `claude_session_start_is_critical_with_terminal_context` (function) component `claude_session_start_is_critical_with_terminal_context [function]` (`eccb2c13-3f5c-5c7c-a63e-4c670079d299`) lines 137-143 [crates/ghook/src/diagnose.rs:137-143]
  - Signature: `fn claude_session_start_is_critical_with_terminal_context() {`
  - Purpose: This function asserts that diagnosing a "claude" session-start event produces a critical diagnostic result with CLI recognition, "claude" source identification, and terminal context enabled. [crates/ghook/src/diagnose.rs:137-143]
- `codex_pre_tool_use_noncritical_without_terminal_context` (function) component `codex_pre_tool_use_noncritical_without_terminal_context [function]` (`2ab1c8cb-1a26-526b-97e2-c3ced80e7439`) lines 146-152 [crates/ghook/src/diagnose.rs:146-152]
  - Signature: `fn codex_pre_tool_use_noncritical_without_terminal_context() {`
  - Purpose: This function verifies that a "codex" PreToolUse diagnostic instance is CLI-recognized, non-critical, and has terminal context disabled with no preview data. [crates/ghook/src/diagnose.rs:146-152]
- `droid_session_start_is_recognized_noncritical_with_terminal_context_enabled` (function) component `droid_session_start_is_recognized_noncritical_with_terminal_context_enabled [function]` (`14ae6661-fb9d-5b9e-95dd-ffd3a5d7a474`) lines 155-161 [crates/ghook/src/diagnose.rs:155-161]
  - Signature: `fn droid_session_start_is_recognized_noncritical_with_terminal_context_enabled() {`
  - Purpose: This test verifies that the `diagnose()` function recognizes a 'droid' SessionStart event as a non-critical diagnostic result with terminal context enabled and correct source attribution. [crates/ghook/src/diagnose.rs:155-161]
- `compile_v2_schema` (function) component `compile_v2_schema [function]` (`00e9dfcb-4c8a-5ce3-9fb1-8c1101e1e67b`) lines 163-170 [crates/ghook/src/diagnose.rs:163-170]
  - Signature: `fn compile_v2_schema() -> jsonschema::JSONSchema {`
  - Purpose: Loads an embedded JSON file (`diagnose-output.v2.schema.json`), deserializes it, and returns a compiled JSONSchema validator using Draft 7 specification. [crates/ghook/src/diagnose.rs:163-170]
- `assert_validates` (function) component `assert_validates [function]` (`6162c40d-ddf8-5812-bd34-5902c76f6b62`) lines 172-177 [crates/ghook/src/diagnose.rs:172-177]
  - Signature: `fn assert_validates(schema: &jsonschema::JSONSchema, value: &serde_json::Value) {`
  - Purpose: This function asserts that a JSON value conforms to a JSON schema, panicking with a formatted list of all validation errors if validation fails. [crates/ghook/src/diagnose.rs:172-177]
- `diagnose_output_validates_against_v2_schema` (function) component `diagnose_output_validates_against_v2_schema [function]` (`a10ccd0d-dda9-53a5-b2a8-1c6acc8d7481`) lines 180-192 [crates/ghook/src/diagnose.rs:180-192]
  - Signature: `fn diagnose_output_validates_against_v2_schema() {`
  - Purpose: Validates that the diagnostic output for the Claude CLI's session-start hook conforms to a compiled v2 JSON schema and contains expected field values including schema version, CLI name, hook type, source, and boolean status flags. [crates/ghook/src/diagnose.rs:180-192]
- `diagnose_output_for_unknown_cli_validates` (function) component `diagnose_output_for_unknown_cli_validates [function]` (`23646fad-b5d5-5ed2-aa07-56333505a4a7`) lines 195-207 [crates/ghook/src/diagnose.rs:195-207]
  - Signature: `fn diagnose_output_for_unknown_cli_validates() {`
  - Purpose: This test function verifies that `diagnose` produces v2-schema-compliant JSON output for an unknown CLI type, with correct field values including a false `cli_recognized` flag. [crates/ghook/src/diagnose.rs:195-207]
- `schema_version_is_two` (function) component `schema_version_is_two [function]` (`b48a5f81-4b1e-50c4-a3c6-bd5a56e6adaf`) lines 210-213 [crates/ghook/src/diagnose.rs:210-213]
  - Signature: `fn schema_version_is_two() {`
  - Purpose: This test function asserts that the schema_version field returned by diagnosing "claude" at "session-start" equals 2. [crates/ghook/src/diagnose.rs:210-213]
- `install_provenance_absent_when_no_sidecar` (function) component `install_provenance_absent_when_no_sidecar [function]` (`1037de6b-5f5f-50b7-861d-9f1d9a9a8ffa`) lines 216-221 [crates/ghook/src/diagnose.rs:216-221]
  - Signature: `fn install_provenance_absent_when_no_sidecar() {`
  - Purpose: This test asserts that `read_install_provenance` returns `(None, None)` when invoked on an empty temporary directory lacking a sidecar file. [crates/ghook/src/diagnose.rs:216-221]
- `install_provenance_read_from_sidecar` (function) component `install_provenance_read_from_sidecar [function]` (`e7a32469-b625-5e77-a884-390c699de709`) lines 224-246 [crates/ghook/src/diagnose.rs:224-246]
  - Signature: `fn install_provenance_read_from_sidecar() {`
  - Purpose: Unit test that validates `read_install_provenance` correctly parses the `install_method` and `install_source_url` fields from a JSON sidecar metadata file. [crates/ghook/src/diagnose.rs:224-246]
- `install_provenance_partial_sidecar_returns_present_fields` (function) component `install_provenance_partial_sidecar_returns_present_fields [function]` (`68f07533-2835-53d4-ae83-6b840dffd509`) lines 249-256 [crates/ghook/src/diagnose.rs:249-256]
  - Signature: `fn install_provenance_partial_sidecar_returns_present_fields() {`
  - Purpose: This function tests that `read_install_provenance()` correctly parses a partial provenance sidecar file by returning the present "install_method" field and None for the missing "url" field. [crates/ghook/src/diagnose.rs:249-256]
- `install_provenance_malformed_json_collapses_to_none` (function) component `install_provenance_malformed_json_collapses_to_none [function]` (`99ed98ac-6741-5da6-b9d6-23c91e3b0c19`) lines 259-266 [crates/ghook/src/diagnose.rs:259-266]
  - Signature: `fn install_provenance_malformed_json_collapses_to_none() {`
  - Purpose: Tests that `read_install_provenance()` returns `(None, None)` when the install sidecar file contains malformed JSON. [crates/ghook/src/diagnose.rs:259-266]

