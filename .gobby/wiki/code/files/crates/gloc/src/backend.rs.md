---
title: crates/gloc/src/backend.rs
type: code_file
provenance:
- file: crates/gloc/src/backend.rs
  ranges:
  - 7-12
  - 14-23
  - 15-22
  - 28-62
  - 67-108
  - 111-129
  - 132-149
  - 153-162
  - 168-175
  - 178-181
  - 184-189
  - 192-201
  - 204-207
  - 210-213
  - 216-219
  - 222-225
  - 228-231
  - 234-243
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gloc/src/backend.rs

Module: [[code/modules/crates/gloc/src|crates/gloc/src]]

## Purpose

`crates/gloc/src/backend.rs` exposes 18 indexed API symbols.
[crates/gloc/src/backend.rs:7-12]
[crates/gloc/src/backend.rs:14-23]
[crates/gloc/src/backend.rs:15-22]
[crates/gloc/src/backend.rs:28-62]
[crates/gloc/src/backend.rs:67-108]
[crates/gloc/src/backend.rs:111-129]
[crates/gloc/src/backend.rs:132-149]
[crates/gloc/src/backend.rs:153-162]
[crates/gloc/src/backend.rs:168-175]
[crates/gloc/src/backend.rs:178-181]
[crates/gloc/src/backend.rs:184-189]
[crates/gloc/src/backend.rs:192-201]
[crates/gloc/src/backend.rs:204-207]
[crates/gloc/src/backend.rs:210-213]
[crates/gloc/src/backend.rs:216-219]
[crates/gloc/src/backend.rs:222-225]
[crates/gloc/src/backend.rs:228-231]
[crates/gloc/src/backend.rs:234-243]

## API Symbols

- `ModelError` (type) component `ModelError [type]` (`17e77151-ca44-58bc-9469-7f26e21f4719`) lines 7-12 [crates/gloc/src/backend.rs:7-12]
  - Signature: `pub enum ModelError {`
  - Purpose: Indexed type `ModelError` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:7-12]
- `ModelError` (class) component `ModelError [class]` (`959f4302-6ec9-5693-892c-448fab92ce23`) lines 14-23 [crates/gloc/src/backend.rs:14-23]
  - Signature: `impl fmt::Display for ModelError {`
  - Purpose: Indexed class `ModelError` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:14-23]
- `ModelError.fmt` (method) component `ModelError.fmt [method]` (`7e263d52-5ed8-5422-a547-87a81d3649ac`) lines 15-22 [crates/gloc/src/backend.rs:15-22]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Indexed method `ModelError.fmt` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:15-22]
- `ensure_model_ready` (function) component `ensure_model_ready [function]` (`1550bb68-f95d-5cf7-9a78-634164f14e23`) lines 28-62 [crates/gloc/src/backend.rs:28-62]
  - Signature: `pub fn ensure_model_ready(`
  - Purpose: Indexed function `ensure_model_ready` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:28-62]
- `ollama_check_model` (function) component `ollama_check_model [function]` (`c3153167-82c9-5ef3-a9f2-0b33df034b8c`) lines 67-108 [crates/gloc/src/backend.rs:67-108]
  - Signature: `fn ollama_check_model(backend: &Backend, model: &str, timeout_ms: u64) -> Result<bool, ModelError> {`
  - Purpose: Indexed function `ollama_check_model` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:67-108]
- `ollama_pull_model` (function) component `ollama_pull_model [function]` (`2e3be105-cdbe-547f-90a6-bbe2885de96b`) lines 111-129 [crates/gloc/src/backend.rs:111-129]
  - Signature: `fn ollama_pull_model(backend: &Backend, model: &str) -> Result<(), ModelError> {`
  - Purpose: Indexed function `ollama_pull_model` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:111-129]
- `ollama_warmup_model` (function) component `ollama_warmup_model [function]` (`cd57587b-8493-53ba-bd7d-73e123d81762`) lines 132-149 [crates/gloc/src/backend.rs:132-149]
  - Signature: `fn ollama_warmup_model(backend: &Backend, model: &str) -> Result<(), ModelError> {`
  - Purpose: Indexed function `ollama_warmup_model` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:132-149]
- `model_name_matches` (function) component `model_name_matches [function]` (`636cea91-7278-5e0b-a985-9e719e252bd3`) lines 153-162 [crates/gloc/src/backend.rs:153-162]
  - Signature: `fn model_name_matches(entry: &serde_json::Value, model: &str) -> bool {`
  - Purpose: Indexed function `model_name_matches` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:153-162]
- `unreachable_backend` (function) component `unreachable_backend [function]` (`26bded03-836f-58c7-8409-c46953e9b282`) lines 168-175 [crates/gloc/src/backend.rs:168-175]
  - Signature: `fn unreachable_backend() -> Backend {`
  - Purpose: Indexed function `unreachable_backend` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:168-175]
- `test_detect_backend_none_running` (function) component `test_detect_backend_none_running [function]` (`bc20d012-5207-57d8-87bf-b209fabb7988`) lines 178-181 [crates/gloc/src/backend.rs:178-181]
  - Signature: `fn test_detect_backend_none_running() {`
  - Purpose: Indexed function `test_detect_backend_none_running` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:178-181]
- `test_validate_backend_unreachable` (function) component `test_validate_backend_unreachable [function]` (`a381ca63-91a0-50da-b4d4-f9274138f5dd`) lines 184-189 [crates/gloc/src/backend.rs:184-189]
  - Signature: `fn test_validate_backend_unreachable() {`
  - Purpose: Indexed function `test_validate_backend_unreachable` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:184-189]
- `test_ensure_model_ready_non_ollama_is_noop` (function) component `test_ensure_model_ready_non_ollama_is_noop [function]` (`fb12b714-be3f-5221-a8ad-21e12c2d1c5d`) lines 192-201 [crates/gloc/src/backend.rs:192-201]
  - Signature: `fn test_ensure_model_ready_non_ollama_is_noop() {`
  - Purpose: Indexed function `test_ensure_model_ready_non_ollama_is_noop` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:192-201]
- `test_model_name_matches_exact` (function) component `test_model_name_matches_exact [function]` (`fb28a04e-5a8f-559a-afb2-f6d530ca292d`) lines 204-207 [crates/gloc/src/backend.rs:204-207]
  - Signature: `fn test_model_name_matches_exact() {`
  - Purpose: Indexed function `test_model_name_matches_exact` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:204-207]
- `test_model_name_matches_with_latest` (function) component `test_model_name_matches_with_latest [function]` (`8eb03b46-e5a9-5a2c-ad9b-f452fbfd72d1`) lines 210-213 [crates/gloc/src/backend.rs:210-213]
  - Signature: `fn test_model_name_matches_with_latest() {`
  - Purpose: Indexed function `test_model_name_matches_with_latest` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:210-213]
- `test_model_name_matches_with_tag` (function) component `test_model_name_matches_with_tag [function]` (`001d13de-e5d1-5ff5-8031-35b5d08aee92`) lines 216-219 [crates/gloc/src/backend.rs:216-219]
  - Signature: `fn test_model_name_matches_with_tag() {`
  - Purpose: Indexed function `test_model_name_matches_with_tag` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:216-219]
- `test_model_name_no_match` (function) component `test_model_name_no_match [function]` (`28f1c2a8-fc17-51ae-b0aa-c942e21f9368`) lines 222-225 [crates/gloc/src/backend.rs:222-225]
  - Signature: `fn test_model_name_no_match() {`
  - Purpose: Indexed function `test_model_name_no_match` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:222-225]
- `test_model_name_matches_model_field` (function) component `test_model_name_matches_model_field [function]` (`5e9f0915-50ce-5cfd-8e21-a853a3059467`) lines 228-231 [crates/gloc/src/backend.rs:228-231]
  - Signature: `fn test_model_name_matches_model_field() {`
  - Purpose: Indexed function `test_model_name_matches_model_field` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:228-231]
- `test_model_error_display` (function) component `test_model_error_display [function]` (`0b24632d-b0de-563d-bfad-d9c7a9df0df0`) lines 234-243 [crates/gloc/src/backend.rs:234-243]
  - Signature: `fn test_model_error_display() {`
  - Purpose: Indexed function `test_model_error_display` in `crates/gloc/src/backend.rs`. [crates/gloc/src/backend.rs:234-243]

