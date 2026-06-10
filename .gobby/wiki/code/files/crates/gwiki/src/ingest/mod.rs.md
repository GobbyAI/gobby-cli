---
title: crates/gwiki/src/ingest/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/mod.rs
  ranges:
  - 25-29
  - 31-36
  - 38-46
  - 48-57
  - 59-73
  - 75-85
  - 87-107
  - 109-117
  - 119-134
  - 136-142
  - 145-148
  - 150-158
  - 151-153
  - 155-157
  - 160-170
  - 172-177
  - 179-185
  - 187-194
  - 196-203
  - 205-225
  - 227-229
  - 231-234
  - 236-243
  - 245-247
  - 249-251
  - 253-255
  - 257-259
  - 261-263
  - 265-304
  - 306-356
  - 358-373
  - 375-390
  - 392-409
  - 411-419
  - 421-448
  - 452-457
  - 459-473
  - 475-481
  - 507-516
  - 518-524
  - 526-541
  - 544-555
  - 558-584
  - 587-597
  - 600-617
  - 620-669
  - 672-718
  - 721-726
  - 728-745
  - 729-736
  - 738-744
  - 747-796
  - 748-752
  - 754-757
  - 759-766
  - 768-771
  - 773-776
  - 778-781
  - 783-790
  - 792-795
  - 799-832
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/mod.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

`crates/gwiki/src/ingest/mod.rs` exposes 61 indexed API symbols.
[crates/gwiki/src/ingest/mod.rs:25-29]
[crates/gwiki/src/ingest/mod.rs:31-36]
[crates/gwiki/src/ingest/mod.rs:38-46]
[crates/gwiki/src/ingest/mod.rs:48-57]
[crates/gwiki/src/ingest/mod.rs:59-73]
[crates/gwiki/src/ingest/mod.rs:75-85]
[crates/gwiki/src/ingest/mod.rs:87-107]
[crates/gwiki/src/ingest/mod.rs:109-117]
[crates/gwiki/src/ingest/mod.rs:119-134]
[crates/gwiki/src/ingest/mod.rs:136-142]
[crates/gwiki/src/ingest/mod.rs:145-148]
[crates/gwiki/src/ingest/mod.rs:150-158]
[crates/gwiki/src/ingest/mod.rs:151-153]
[crates/gwiki/src/ingest/mod.rs:155-157]
[crates/gwiki/src/ingest/mod.rs:160-170]
[crates/gwiki/src/ingest/mod.rs:172-177]
[crates/gwiki/src/ingest/mod.rs:179-185]
[crates/gwiki/src/ingest/mod.rs:187-194]
[crates/gwiki/src/ingest/mod.rs:196-203]
[crates/gwiki/src/ingest/mod.rs:205-225]
[crates/gwiki/src/ingest/mod.rs:227-229]
[crates/gwiki/src/ingest/mod.rs:231-234]
[crates/gwiki/src/ingest/mod.rs:236-243]
[crates/gwiki/src/ingest/mod.rs:245-247]
[crates/gwiki/src/ingest/mod.rs:249-251]
[crates/gwiki/src/ingest/mod.rs:253-255]
[crates/gwiki/src/ingest/mod.rs:257-259]
[crates/gwiki/src/ingest/mod.rs:261-263]
[crates/gwiki/src/ingest/mod.rs:265-304]
[crates/gwiki/src/ingest/mod.rs:306-356]
[crates/gwiki/src/ingest/mod.rs:358-373]
[crates/gwiki/src/ingest/mod.rs:375-390]
[crates/gwiki/src/ingest/mod.rs:392-409]
[crates/gwiki/src/ingest/mod.rs:411-419]
[crates/gwiki/src/ingest/mod.rs:421-448]
[crates/gwiki/src/ingest/mod.rs:452-457]
[crates/gwiki/src/ingest/mod.rs:459-473]
[crates/gwiki/src/ingest/mod.rs:475-481]
[crates/gwiki/src/ingest/mod.rs:507-516]
[crates/gwiki/src/ingest/mod.rs:518-524]
[crates/gwiki/src/ingest/mod.rs:526-541]
[crates/gwiki/src/ingest/mod.rs:544-555]
[crates/gwiki/src/ingest/mod.rs:558-584]
[crates/gwiki/src/ingest/mod.rs:587-597]
[crates/gwiki/src/ingest/mod.rs:600-617]
[crates/gwiki/src/ingest/mod.rs:620-669]
[crates/gwiki/src/ingest/mod.rs:672-718]
[crates/gwiki/src/ingest/mod.rs:721-726]
[crates/gwiki/src/ingest/mod.rs:728-745]
[crates/gwiki/src/ingest/mod.rs:729-736]
[crates/gwiki/src/ingest/mod.rs:738-744]
[crates/gwiki/src/ingest/mod.rs:747-796]
[crates/gwiki/src/ingest/mod.rs:748-752]
[crates/gwiki/src/ingest/mod.rs:754-757]
[crates/gwiki/src/ingest/mod.rs:759-766]
[crates/gwiki/src/ingest/mod.rs:768-771]
[crates/gwiki/src/ingest/mod.rs:773-776]
[crates/gwiki/src/ingest/mod.rs:778-781]
[crates/gwiki/src/ingest/mod.rs:783-790]
[crates/gwiki/src/ingest/mod.rs:792-795]
[crates/gwiki/src/ingest/mod.rs:799-832]

## API Symbols

- `IngestResult` (class) component `IngestResult [class]` (`4fef1039-56f8-52d8-9824-d9ae3d69d4d2`) lines 25-29 [crates/gwiki/src/ingest/mod.rs:25-29]
  - Signature: `pub struct IngestResult {`
  - Purpose: Indexed class `IngestResult` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:25-29]
- `lowercase_extension` (function) component `lowercase_extension [function]` (`54fcfcf1-8ef3-56c7-8480-d078aaaf97cd`) lines 31-36 [crates/gwiki/src/ingest/mod.rs:31-36]
  - Signature: `pub(crate) fn lowercase_extension(path: impl AsRef<Path>) -> Option<String> {`
  - Purpose: Indexed function `lowercase_extension` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:31-36]
- `write_raw_markdown` (function) component `write_raw_markdown [function]` (`c2d25784-c4d5-5929-8821-7de09490a327`) lines 38-46 [crates/gwiki/src/ingest/mod.rs:38-46]
  - Signature: `pub(crate) fn write_raw_markdown(`
  - Purpose: Indexed function `write_raw_markdown` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:38-46]
- `write_asset` (function) component `write_asset [function]` (`a57054cd-8dca-5f03-8ba8-290fd63e55b4`) lines 48-57 [crates/gwiki/src/ingest/mod.rs:48-57]
  - Signature: `pub(crate) fn write_asset(`
  - Purpose: Indexed function `write_asset` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:48-57]
- `write_asset_with_suffix` (function) component `write_asset_with_suffix [function]` (`596673d6-4dca-566c-8d9f-d6d7ac047925`) lines 59-73 [crates/gwiki/src/ingest/mod.rs:59-73]
  - Signature: `pub(crate) fn write_asset_with_suffix(`
  - Purpose: Indexed function `write_asset_with_suffix` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:59-73]
- `write_asset_from_path` (function) component `write_asset_from_path [function]` (`5eef7bd8-030b-5de2-8adf-1543fd4a5ac4`) lines 75-85 [crates/gwiki/src/ingest/mod.rs:75-85]
  - Signature: `pub(crate) fn write_asset_from_path(`
  - Purpose: Indexed function `write_asset_from_path` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:75-85]
- `sanitize_asset_suffix` (function) component `sanitize_asset_suffix [function]` (`0df6c0b0-0855-576d-b2f7-d34fcb9e3eab`) lines 87-107 [crates/gwiki/src/ingest/mod.rs:87-107]
  - Signature: `fn sanitize_asset_suffix(value: &str) -> String {`
  - Purpose: Indexed function `sanitize_asset_suffix` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:87-107]
- `index_after_ingest` (function) component `index_after_ingest [function]` (`4a9a51b9-9de1-56a5-bf47-605349732406`) lines 109-117 [crates/gwiki/src/ingest/mod.rs:109-117]
  - Signature: `pub(crate) fn index_after_ingest(`
  - Purpose: Indexed function `index_after_ingest` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:109-117]
- `write_raw_then_index` (function) component `write_raw_then_index [function]` (`b64c3593-91a1-5a63-ba90-7d9003da2bd1`) lines 119-134 [crates/gwiki/src/ingest/mod.rs:119-134]
  - Signature: `pub(crate) fn write_raw_then_index(`
  - Purpose: Indexed function `write_raw_then_index` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:119-134]
- `markdown_metadata` (function) component `markdown_metadata [function]` (`0e7b802b-83c3-59e9-8444-f5279a51b5fd`) lines 136-142 [crates/gwiki/src/ingest/mod.rs:136-142]
  - Signature: `pub(crate) fn markdown_metadata(fields: &[(&str, String)]) -> String {`
  - Purpose: Indexed function `markdown_metadata` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:136-142]
- `MetadataValue` (type) component `MetadataValue [type]` (`8e2735e9-ebb1-5d33-a425-8b5baa283830`) lines 145-148 [crates/gwiki/src/ingest/mod.rs:145-148]
  - Signature: `pub(crate) enum MetadataValue {`
  - Purpose: Indexed type `MetadataValue` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:145-148]
- `MetadataValue` (class) component `MetadataValue [class]` (`cfdac1e3-d948-5631-a924-3d46bbd591d3`) lines 150-158 [crates/gwiki/src/ingest/mod.rs:150-158]
  - Signature: `impl MetadataValue {`
  - Purpose: Indexed class `MetadataValue` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:150-158]
- `MetadataValue.string` (method) component `MetadataValue.string [method]` (`17cb867d-c7a7-54e8-81bd-706b53ebb08d`) lines 151-153 [crates/gwiki/src/ingest/mod.rs:151-153]
  - Signature: `pub(crate) fn string(value: impl Into<String>) -> Self {`
  - Purpose: Indexed method `MetadataValue.string` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:151-153]
- `MetadataValue.number` (method) component `MetadataValue.number [method]` (`18ad1e58-88d4-5a0c-9c20-924133037f4e`) lines 155-157 [crates/gwiki/src/ingest/mod.rs:155-157]
  - Signature: `pub(crate) fn number(value: impl ToString) -> Self {`
  - Purpose: Indexed method `MetadataValue.number` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:155-157]
- `markdown_metadata_values` (function) component `markdown_metadata_values [function]` (`24b9c06b-46da-5df3-b04a-035d61aff2f0`) lines 160-170 [crates/gwiki/src/ingest/mod.rs:160-170]
  - Signature: `pub(crate) fn markdown_metadata_values(fields: &[(&str, MetadataValue)]) -> String {`
  - Purpose: Indexed function `markdown_metadata_values` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:160-170]
- `yaml_metadata_value` (function) component `yaml_metadata_value [function]` (`50cad92e-7696-5755-b87d-d8e8d351ce8c`) lines 172-177 [crates/gwiki/src/ingest/mod.rs:172-177]
  - Signature: `fn yaml_metadata_value(key: &str, value: &MetadataValue) -> String {`
  - Purpose: Indexed function `yaml_metadata_value` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:172-177]
- `yaml_metadata_scalar` (function) component `yaml_metadata_scalar [function]` (`8c42929b-048c-5dae-8a20-2fb844424646`) lines 179-185 [crates/gwiki/src/ingest/mod.rs:179-185]
  - Signature: `fn yaml_metadata_scalar(key: &str, value: &str) -> String {`
  - Purpose: Indexed function `yaml_metadata_scalar` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:179-185]
- `yaml_safe_single_line_scalar` (function) component `yaml_safe_single_line_scalar [function]` (`8c273e9e-83db-5498-a843-1cdb34366c7d`) lines 187-194 [crates/gwiki/src/ingest/mod.rs:187-194]
  - Signature: `fn yaml_safe_single_line_scalar(value: &str) -> String {`
  - Purpose: Indexed function `yaml_safe_single_line_scalar` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:187-194]
- `yaml_numeric_scalar` (function) component `yaml_numeric_scalar [function]` (`1709bc2d-2cbd-5935-bdd6-36df6f599943`) lines 196-203 [crates/gwiki/src/ingest/mod.rs:196-203]
  - Signature: `fn yaml_numeric_scalar(value: &str) -> String {`
  - Purpose: Indexed function `yaml_numeric_scalar` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:196-203]
- `yaml_plain_scalar_is_safe` (function) component `yaml_plain_scalar_is_safe [function]` (`6734882e-cdf8-5540-98c9-80a8bd3a83ce`) lines 205-225 [crates/gwiki/src/ingest/mod.rs:205-225]
  - Signature: `fn yaml_plain_scalar_is_safe(value: &str) -> bool {`
  - Purpose: Indexed function `yaml_plain_scalar_is_safe` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:205-225]
- `yaml_numeric_scalar_is_safe` (function) component `yaml_numeric_scalar_is_safe [function]` (`88831747-f466-537a-96a1-2d504f02303a`) lines 227-229 [crates/gwiki/src/ingest/mod.rs:227-229]
  - Signature: `fn yaml_numeric_scalar_is_safe(value: &str) -> bool {`
  - Purpose: Indexed function `yaml_numeric_scalar_is_safe` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:227-229]
- `yaml_plain_scalar_is_timestamp` (function) component `yaml_plain_scalar_is_timestamp [function]` (`fcee03a4-97c7-55ad-86a2-e2b180d2760b`) lines 231-234 [crates/gwiki/src/ingest/mod.rs:231-234]
  - Signature: `fn yaml_plain_scalar_is_timestamp(value: &str) -> bool {`
  - Purpose: Indexed function `yaml_plain_scalar_is_timestamp` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:231-234]
- `has_yaml_date_prefix` (function) component `has_yaml_date_prefix [function]` (`a171e0ef-93c5-5b5f-a3c9-ae15e7507e91`) lines 236-243 [crates/gwiki/src/ingest/mod.rs:236-243]
  - Signature: `fn has_yaml_date_prefix(bytes: &[u8]) -> bool {`
  - Purpose: Indexed function `has_yaml_date_prefix` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:236-243]
- `quote_yaml_string` (function) component `quote_yaml_string [function]` (`7f6a7509-641c-590b-8a0c-9e461cea329f`) lines 245-247 [crates/gwiki/src/ingest/mod.rs:245-247]
  - Signature: `fn quote_yaml_string(value: &str) -> String {`
  - Purpose: Indexed function `quote_yaml_string` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:245-247]
- `single_line` (function) component `single_line [function]` (`b5c27967-c9db-5892-8981-fa98b98d05c8`) lines 249-251 [crates/gwiki/src/ingest/mod.rs:249-251]
  - Signature: `pub(crate) fn single_line(value: &str) -> String {`
  - Purpose: Indexed function `single_line` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:249-251]
- `markdown_title` (function) component `markdown_title [function]` (`5a9a8289-dc41-5503-a6ca-e31ae1225603`) lines 253-255 [crates/gwiki/src/ingest/mod.rs:253-255]
  - Signature: `pub(crate) fn markdown_title(value: &str) -> String {`
  - Purpose: Indexed function `markdown_title` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:253-255]
- `text_from_utf8_lossy` (function) component `text_from_utf8_lossy [function]` (`a78ea851-f148-5a4c-aec7-a6294b98671d`) lines 257-259 [crates/gwiki/src/ingest/mod.rs:257-259]
  - Signature: `pub(crate) fn text_from_utf8_lossy(bytes: &[u8]) -> String {`
  - Purpose: Indexed function `text_from_utf8_lossy` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:257-259]
- `path_to_string` (function) component `path_to_string [function]` (`5d183b43-3943-59e8-8817-0e762b2b12f5`) lines 261-263 [crates/gwiki/src/ingest/mod.rs:261-263]
  - Signature: `pub(crate) fn path_to_string(path: &Path) -> String {`
  - Purpose: Indexed function `path_to_string` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:261-263]
- `write_immutable` (function) component `write_immutable [function]` (`afa41f90-7f04-5ffd-8dae-ed1400dd2301`) lines 265-304 [crates/gwiki/src/ingest/mod.rs:265-304]
  - Signature: `fn write_immutable(vault_root: &Path, relative: &Path, bytes: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Indexed function `write_immutable` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:265-304]
- `write_immutable_file` (function) component `write_immutable_file [function]` (`4655b5a4-7233-5278-b98e-18f9525b91ad`) lines 306-356 [crates/gwiki/src/ingest/mod.rs:306-356]
  - Signature: `fn write_immutable_file(`
  - Purpose: Indexed function `write_immutable_file` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:306-356]
- `validate_existing_raw_bytes` (function) component `validate_existing_raw_bytes [function]` (`43fb9154-d19d-52e0-9272-1498bb1afab0`) lines 358-373 [crates/gwiki/src/ingest/mod.rs:358-373]
  - Signature: `fn validate_existing_raw_bytes(`
  - Purpose: Indexed function `validate_existing_raw_bytes` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:358-373]
- `validate_existing_raw_file` (function) component `validate_existing_raw_file [function]` (`6f93f739-71ca-5c64-99f8-7f163a225767`) lines 375-390 [crates/gwiki/src/ingest/mod.rs:375-390]
  - Signature: `fn validate_existing_raw_file(`
  - Purpose: Indexed function `validate_existing_raw_file` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:375-390]
- `validate_source_file_hash` (function) component `validate_source_file_hash [function]` (`d1ec4fd4-22f0-5fdd-af9c-d6ebb00957b9`) lines 392-409 [crates/gwiki/src/ingest/mod.rs:392-409]
  - Signature: `fn validate_source_file_hash(source_path: &Path, content_hash: &str) -> Result<String, WikiError> {`
  - Purpose: Indexed function `validate_source_file_hash` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:392-409]
- `immutable_exists_error` (function) component `immutable_exists_error [function]` (`c6a490cc-bee7-5183-81c6-ce426221642e`) lines 411-419 [crates/gwiki/src/ingest/mod.rs:411-419]
  - Signature: `fn immutable_exists_error(relative: &Path) -> WikiError {`
  - Purpose: Indexed function `immutable_exists_error` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:411-419]
- `create_raw_temp_file` (function) component `create_raw_temp_file [function]` (`56f41b5f-b8e0-5c6e-af28-a91882a57b15`) lines 421-448 [crates/gwiki/src/ingest/mod.rs:421-448]
  - Signature: `fn create_raw_temp_file(path: &Path) -> Result<tempfile::NamedTempFile, WikiError> {`
  - Purpose: Indexed function `create_raw_temp_file` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:421-448]
- `asset_path` (function) component `asset_path [function]` (`6c9baea3-32b7-53f1-8745-726cd9637b36`) lines 452-457 [crates/gwiki/src/ingest/mod.rs:452-457]
  - Signature: `pub(crate) fn asset_path(record: &SourceRecord, file_name: &str) -> PathBuf {`
  - Purpose: Indexed function `asset_path` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:452-457]
- `sanitized_extension_for_file_name` (function) component `sanitized_extension_for_file_name [function]` (`8a40d2ac-e1ac-5910-b376-75fc129d3501`) lines 459-473 [crates/gwiki/src/ingest/mod.rs:459-473]
  - Signature: `fn sanitized_extension_for_file_name(file_name: &str) -> String {`
  - Purpose: Indexed function `sanitized_extension_for_file_name` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:459-473]
- `sanitize_extension` (function) component `sanitize_extension [function]` (`c39ea2c7-73b5-591a-b0ec-965e7c15a848`) lines 475-481 [crates/gwiki/src/ingest/mod.rs:475-481]
  - Signature: `fn sanitize_extension(extension: &str) -> String {`
  - Purpose: Indexed function `sanitize_extension` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:475-481]
- `no_ai_context` (function) component `no_ai_context [function]` (`2071c0f7-4fde-5e86-8128-9d235d08f29e`) lines 507-516 [crates/gwiki/src/ingest/mod.rs:507-516]
  - Signature: `fn no_ai_context() -> AiContext {`
  - Purpose: Indexed function `no_ai_context` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:507-516]
- `write_file` (function) component `write_file [function]` (`72314a55-1297-5ec6-b0a5-6e88e1c4b639`) lines 518-524 [crates/gwiki/src/ingest/mod.rs:518-524]
  - Signature: `fn write_file(root: &std::path::Path, relative: &str, contents: &str) {`
  - Purpose: Indexed function `write_file` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:518-524]
- `test_source_record` (function) component `test_source_record [function]` (`5a6b3478-994f-5774-a3ef-f7d68a295b41`) lines 526-541 [crates/gwiki/src/ingest/mod.rs:526-541]
  - Signature: `fn test_source_record() -> SourceRecord {`
  - Purpose: Indexed function `test_source_record` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:526-541]
- `asset_path_uses_basename_before_extension_extraction` (function) component `asset_path_uses_basename_before_extension_extraction [function]` (`982abc12-1b6c-5f02-9239-65342c44c686`) lines 544-555 [crates/gwiki/src/ingest/mod.rs:544-555]
  - Signature: `fn asset_path_uses_basename_before_extension_extraction() {`
  - Purpose: Indexed function `asset_path_uses_basename_before_extension_extraction` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:544-555]
- `markdown_metadata_quotes_yaml_sensitive_scalars` (function) component `markdown_metadata_quotes_yaml_sensitive_scalars [function]` (`60e11a07-7725-5b52-b965-a5b95e963875`) lines 558-584 [crates/gwiki/src/ingest/mod.rs:558-584]
  - Signature: `fn markdown_metadata_quotes_yaml_sensitive_scalars() {`
  - Purpose: Indexed function `markdown_metadata_quotes_yaml_sensitive_scalars` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:558-584]
- `markdown_metadata_allows_explicit_numeric_values` (function) component `markdown_metadata_allows_explicit_numeric_values [function]` (`258c03b2-151c-5142-a57d-24b89a4effbd`) lines 587-597 [crates/gwiki/src/ingest/mod.rs:587-597]
  - Signature: `fn markdown_metadata_allows_explicit_numeric_values() {`
  - Purpose: Indexed function `markdown_metadata_allows_explicit_numeric_values` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:587-597]
- `immutable_file_requires_declared_source_hash_before_copy` (function) component `immutable_file_requires_declared_source_hash_before_copy [function]` (`24b66dcc-045d-5bf4-8991-d727ee3f1ea3`) lines 600-617 [crates/gwiki/src/ingest/mod.rs:600-617]
  - Signature: `fn immutable_file_requires_declared_source_hash_before_copy() {`
  - Purpose: Indexed function `immutable_file_requires_declared_source_hash_before_copy` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:600-617]
- `immutable_file_existing_match_requires_declared_hash` (function) component `immutable_file_existing_match_requires_declared_hash [function]` (`2c92637e-7924-5459-ab64-b1a760902576`) lines 620-669 [crates/gwiki/src/ingest/mod.rs:620-669]
  - Signature: `fn immutable_file_existing_match_requires_declared_hash() {`
  - Purpose: Indexed function `immutable_file_existing_match_requires_declared_hash` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:620-669]
- `ingest_indexes_raw_without_wiki_rewrite` (function) component `ingest_indexes_raw_without_wiki_rewrite [function]` (`f86b00bc-1b60-553e-be64-0286af1d781b`) lines 672-718 [crates/gwiki/src/ingest/mod.rs:672-718]
  - Signature: `fn ingest_indexes_raw_without_wiki_rewrite() {`
  - Purpose: Indexed function `ingest_indexes_raw_without_wiki_rewrite` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:672-718]
- `RawFirstStore` (class) component `RawFirstStore [class]` (`1d1add87-0e38-5d14-8eff-59d9f28dd507`) lines 721-726 [crates/gwiki/src/ingest/mod.rs:721-726]
  - Signature: `struct RawFirstStore {`
  - Purpose: Indexed class `RawFirstStore` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:721-726]
- `RawFirstStore` (class) component `RawFirstStore [class]` (`9681443d-907d-5d93-93b8-cdcc3dcca48c`) lines 728-745 [crates/gwiki/src/ingest/mod.rs:728-745]
  - Signature: `impl RawFirstStore {`
  - Purpose: Indexed class `RawFirstStore` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:728-745]
- `RawFirstStore.new` (method) component `RawFirstStore.new [method]` (`84ad16e6-f5f7-5775-a33a-3193b377c8b9`) lines 729-736 [crates/gwiki/src/ingest/mod.rs:729-736]
  - Signature: `fn new(vault_root: &Path, expected_raw_path: impl Into<PathBuf>) -> Self {`
  - Purpose: Indexed method `RawFirstStore.new` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:729-736]
- `RawFirstStore.assert_raw_exists_before_index` (method) component `RawFirstStore.assert_raw_exists_before_index [method]` (`798a7b2e-c06f-5dc3-86c7-5d6f2a55df18`) lines 738-744 [crates/gwiki/src/ingest/mod.rs:738-744]
  - Signature: `fn assert_raw_exists_before_index(&mut self) {`
  - Purpose: Indexed method `RawFirstStore.assert_raw_exists_before_index` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:738-744]
- `RawFirstStore` (class) component `RawFirstStore [class]` (`08c74ff4-78cd-522e-a344-d0cd5736b7ae`) lines 747-796 [crates/gwiki/src/ingest/mod.rs:747-796]
  - Signature: `impl WikiIndexStore for RawFirstStore {`
  - Purpose: Indexed class `RawFirstStore` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:747-796]
- `RawFirstStore.indexed_hashes` (method) component `RawFirstStore.indexed_hashes [method]` (`345c7fbb-6396-5a7b-8c80-8427b76d05ee`) lines 748-752 [crates/gwiki/src/ingest/mod.rs:748-752]
  - Signature: `fn indexed_hashes(`
  - Purpose: Indexed method `RawFirstStore.indexed_hashes` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:748-752]
- `RawFirstStore.upsert_document` (method) component `RawFirstStore.upsert_document [method]` (`bdc0472f-032a-542b-b76d-6f3cee7a993d`) lines 754-757 [crates/gwiki/src/ingest/mod.rs:754-757]
  - Signature: `fn upsert_document(&mut self, document: WikiDocument) -> Result<(), StoreError> {`
  - Purpose: Indexed method `RawFirstStore.upsert_document` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:754-757]
- `RawFirstStore.replace_chunks` (method) component `RawFirstStore.replace_chunks [method]` (`e492d861-e315-55e7-ac60-9a7074a63229`) lines 759-766 [crates/gwiki/src/ingest/mod.rs:759-766]
  - Signature: `fn replace_chunks(`
  - Purpose: Indexed method `RawFirstStore.replace_chunks` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:759-766]
- `RawFirstStore.replace_links` (method) component `RawFirstStore.replace_links [method]` (`052a99d1-9f27-5219-ae8e-fd85302a9f73`) lines 768-771 [crates/gwiki/src/ingest/mod.rs:768-771]
  - Signature: `fn replace_links(&mut self, path: &Path, links: Vec<WikiLink>) -> Result<(), StoreError> {`
  - Purpose: Indexed method `RawFirstStore.replace_links` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:768-771]
- `RawFirstStore.upsert_source` (method) component `RawFirstStore.upsert_source [method]` (`978ee11e-01ad-5219-9957-e97eb9cd1647`) lines 773-776 [crates/gwiki/src/ingest/mod.rs:773-776]
  - Signature: `fn upsert_source(&mut self, source: WikiSource) -> Result<(), StoreError> {`
  - Purpose: Indexed method `RawFirstStore.upsert_source` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:773-776]
- `RawFirstStore.record_ingestion` (method) component `RawFirstStore.record_ingestion [method]` (`118327f1-6a8a-5549-bf16-13d6539d3154`) lines 778-781 [crates/gwiki/src/ingest/mod.rs:778-781]
  - Signature: `fn record_ingestion(&mut self, ingestion: WikiIngestion) -> Result<(), StoreError> {`
  - Purpose: Indexed method `RawFirstStore.record_ingestion` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:778-781]
- `RawFirstStore.record_file_hash` (method) component `RawFirstStore.record_file_hash [method]` (`7cfa5b7e-b3ac-510c-b0b4-c7ea9158fc33`) lines 783-790 [crates/gwiki/src/ingest/mod.rs:783-790]
  - Signature: `fn record_file_hash(`
  - Purpose: Indexed method `RawFirstStore.record_file_hash` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:783-790]
- `RawFirstStore.delete_derived_rows` (method) component `RawFirstStore.delete_derived_rows [method]` (`00803d20-d817-5876-bf1e-1921804e9836`) lines 792-795 [crates/gwiki/src/ingest/mod.rs:792-795]
  - Signature: `fn delete_derived_rows(&mut self, path: &Path) -> Result<(), StoreError> {`
  - Purpose: Indexed method `RawFirstStore.delete_derived_rows` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:792-795]
- `external_connectors_write_raw_first` (function) component `external_connectors_write_raw_first [function]` (`1349f575-04bb-54b7-99ae-00a8badcb409`) lines 799-832 [crates/gwiki/src/ingest/mod.rs:799-832]
  - Signature: `fn external_connectors_write_raw_first() {`
  - Purpose: Indexed function `external_connectors_write_raw_first` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:799-832]

