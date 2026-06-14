---
title: crates/gwiki/src/frontmatter.rs
type: code_file
provenance:
- file: crates/gwiki/src/frontmatter.rs
  ranges:
  - 10-13
  - 16-30
  - 32-116
  - 119-125
  - 128-130
  - 132-136
  - '138'
  - 140-170
  - 173-191
  - 193-199
  - 201-205
  - 207-221
  - 223-232
  - 234-264
  - 266-286
  - 289-303
  - 306-314
  - 316-329
  - 331-344
  - 346-394
  - 396-398
  - 400-406
  - 408-415
  - 419-434
  - 436-450
  - 457-524
  - 527-546
  - 549-578
  - 581-626
  - 629-659
  - 662-691
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/frontmatter.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the wiki frontmatter model and its parse/serialize pipeline. `FrontmatterFormat` selects YAML or TOML, `WikiFrontmatter` holds the canonical metadata fields plus an `unknown` map to preserve legacy or tool-specific keys, and `empty`/`as_json` provide a normalized default and JSON export. The parser side splits out frontmatter delimiters, parses metadata into typed fields, converts generic objects into `WikiFrontmatter`, and reports failures through `FrontmatterError`/`ParsedFrontmatter`. The helper serializers and tests cover round-tripping, stale-markdown marking, legacy unknown-field preservation, and migration of shared contract keys into the wiki metadata shape.
[crates/gwiki/src/frontmatter.rs:10-13]
[crates/gwiki/src/frontmatter.rs:16-30]
[crates/gwiki/src/frontmatter.rs:32-116]
[crates/gwiki/src/frontmatter.rs:33-48]
[crates/gwiki/src/frontmatter.rs:51-115]

## API Symbols

- `FrontmatterFormat` (type) component `FrontmatterFormat [type]` (`7d7d2878-4616-50b7-b364-5d25d085c2ff`) lines 10-13 [crates/gwiki/src/frontmatter.rs:10-13]
  - Signature: `pub enum FrontmatterFormat {`
  - Purpose: Indexed type `FrontmatterFormat` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:10-13]
- `WikiFrontmatter` (class) component `WikiFrontmatter [class]` (`862372eb-ec1d-56e0-9087-7b29b27353b9`) lines 16-30 [crates/gwiki/src/frontmatter.rs:16-30]
  - Signature: `pub struct WikiFrontmatter {`
  - Purpose: Indexed class `WikiFrontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:16-30]
- `WikiFrontmatter` (class) component `WikiFrontmatter [class]` (`23ca6438-a0eb-5b47-93a0-09260ef6a965`) lines 32-116 [crates/gwiki/src/frontmatter.rs:32-116]
  - Signature: `impl WikiFrontmatter {`
  - Purpose: Indexed class `WikiFrontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:32-116]
- `WikiFrontmatter.empty` (method) component `WikiFrontmatter.empty [method]` (`cfca94a5-346a-517d-97f5-45935c604b86`) lines 33-48 [crates/gwiki/src/frontmatter.rs:33-48]
  - Signature: `pub fn empty() -> Self {`
  - Purpose: Indexed method `WikiFrontmatter.empty` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:33-48]
- `WikiFrontmatter.as_json` (method) component `WikiFrontmatter.as_json [method]` (`d5dd93d0-eba1-5afa-b327-6239c38e9204`) lines 51-115 [crates/gwiki/src/frontmatter.rs:51-115]
  - Signature: `pub fn as_json(&self) -> Value {`
  - Purpose: Indexed method `WikiFrontmatter.as_json` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:51-115]
- `ParsedFrontmatter` (class) component `ParsedFrontmatter [class]` (`31fc2bd1-b6a8-55f9-ac9c-3a980c0fcdc0`) lines 119-125 [crates/gwiki/src/frontmatter.rs:119-125]
  - Signature: `pub struct ParsedFrontmatter<'a> {`
  - Purpose: Indexed class `ParsedFrontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:119-125]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`7c7306b0-e5db-5476-8a6b-d98d89f85249`) lines 128-130 [crates/gwiki/src/frontmatter.rs:128-130]
  - Signature: `pub struct FrontmatterError {`
  - Purpose: Indexed class `FrontmatterError` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:128-130]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`5741a959-f44d-5e63-acc7-560200272a23`) lines 132-136 [crates/gwiki/src/frontmatter.rs:132-136]
  - Signature: `impl fmt::Display for FrontmatterError {`
  - Purpose: Indexed class `FrontmatterError` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:132-136]
- `FrontmatterError.fmt` (method) component `FrontmatterError.fmt [method]` (`7beb2317-7d32-50a4-aab8-e4d1a6fa790a`) lines 133-135 [crates/gwiki/src/frontmatter.rs:133-135]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Indexed method `FrontmatterError.fmt` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:133-135]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`70a52b78-dee4-5ac2-8102-9551220365fa`) lines 138-138 [crates/gwiki/src/frontmatter.rs:138]
  - Signature: `impl std::error::Error for FrontmatterError {}`
  - Purpose: Indexed class `FrontmatterError` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:138]
- `parse_frontmatter` (function) component `parse_frontmatter [function]` (`04796375-e1a3-5fa7-af29-7b585d7764a4`) lines 140-170 [crates/gwiki/src/frontmatter.rs:140-170]
  - Signature: `pub fn parse_frontmatter(markdown: &str) -> Result<ParsedFrontmatter<'_>, FrontmatterError> {`
  - Purpose: Indexed function `parse_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:140-170]
- `mark_stale_markdown` (function) component `mark_stale_markdown [function]` (`ec57f434-ef82-58b6-a3ea-ebabb34d9cd5`) lines 173-191 [crates/gwiki/src/frontmatter.rs:173-191]
  - Signature: `pub fn mark_stale_markdown(markdown: &str, reason: &str) -> Result<String, FrontmatterError> {`
  - Purpose: Indexed function `mark_stale_markdown` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:173-191]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`512746ff-0f3b-5550-9097-eda6ccc053a1`) lines 193-199 [crates/gwiki/src/frontmatter.rs:193-199]
  - Signature: `impl FrontmatterError {`
  - Purpose: Indexed class `FrontmatterError` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:193-199]
- `FrontmatterError.new` (method) component `FrontmatterError.new [method]` (`0ccc9212-d972-5c3c-8cc6-92f1f5f97e71`) lines 194-198 [crates/gwiki/src/frontmatter.rs:194-198]
  - Signature: `fn new(detail: impl Into<String>) -> Self {`
  - Purpose: Indexed method `FrontmatterError.new` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:194-198]
- `OpeningDelimiter` (class) component `OpeningDelimiter [class]` (`2fd0a14f-74cd-5c63-b527-15903ca89148`) lines 201-205 [crates/gwiki/src/frontmatter.rs:201-205]
  - Signature: `struct OpeningDelimiter {`
  - Purpose: Indexed class `OpeningDelimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:201-205]
- `opening_delimiter` (function) component `opening_delimiter [function]` (`a3727ad6-7e39-56c1-af19-6a6dc96a508b`) lines 207-221 [crates/gwiki/src/frontmatter.rs:207-221]
  - Signature: `fn opening_delimiter(markdown: &str) -> Option<OpeningDelimiter> {`
  - Purpose: Indexed function `opening_delimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:207-221]
- `delimiter_content_start` (function) component `delimiter_content_start [function]` (`61c8145b-351e-5354-a213-1e4b5ff85f88`) lines 223-232 [crates/gwiki/src/frontmatter.rs:223-232]
  - Signature: `fn delimiter_content_start(markdown: &str, marker: &str) -> Option<usize> {`
  - Purpose: Indexed function `delimiter_content_start` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:223-232]
- `find_closing_delimiter` (function) component `find_closing_delimiter [function]` (`6dabf274-5145-5116-ab12-740528a0b01d`) lines 234-264 [crates/gwiki/src/frontmatter.rs:234-264]
  - Signature: `fn find_closing_delimiter(`
  - Purpose: Indexed function `find_closing_delimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:234-264]
- `parse_metadata` (function) component `parse_metadata [function]` (`585c7602-49d9-56e7-bcb5-2c9d6e14f120`) lines 266-286 [crates/gwiki/src/frontmatter.rs:266-286]
  - Signature: `fn parse_metadata(`
  - Purpose: Indexed function `parse_metadata` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:266-286]
- `serialize_yaml_frontmatter` (function) component `serialize_yaml_frontmatter [function]` (`b425aa16-095a-515b-8393-4c2c0607e72b`) lines 289-303 [crates/gwiki/src/frontmatter.rs:289-303]
  - Signature: `fn serialize_yaml_frontmatter(metadata: &WikiFrontmatter) -> Result<String, FrontmatterError> {`
  - Purpose: Indexed function `serialize_yaml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:289-303]
- `serialize_toml_frontmatter` (function) component `serialize_toml_frontmatter [function]` (`5b69b97a-0cc9-5358-a952-77de1c5d5e22`) lines 306-314 [crates/gwiki/src/frontmatter.rs:306-314]
  - Signature: `fn serialize_toml_frontmatter(metadata: &WikiFrontmatter) -> Result<String, FrontmatterError> {`
  - Purpose: Indexed function `serialize_toml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:306-314]
- `parse_yaml` (function) component `parse_yaml [function]` (`193d073e-0157-5714-9684-23723917e586`) lines 316-329 [crates/gwiki/src/frontmatter.rs:316-329]
  - Signature: `fn parse_yaml(raw: &str) -> Result<Value, FrontmatterError> {`
  - Purpose: Indexed function `parse_yaml` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:316-329]
- `parse_toml` (function) component `parse_toml [function]` (`9b1a56b2-2237-58a5-a34f-20423a118111`) lines 331-344 [crates/gwiki/src/frontmatter.rs:331-344]
  - Signature: `fn parse_toml(raw: &str) -> Result<Value, FrontmatterError> {`
  - Purpose: Indexed function `parse_toml` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:331-344]
- `frontmatter_from_object` (function) component `frontmatter_from_object [function]` (`5076c605-1a60-5d24-b173-29efc9d229da`) lines 346-394 [crates/gwiki/src/frontmatter.rs:346-394]
  - Signature: `fn frontmatter_from_object(mut object: Map<String, Value>) -> WikiFrontmatter {`
  - Purpose: Indexed function `frontmatter_from_object` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:346-394]
- `string_value` (function) component `string_value [function]` (`78f8d98e-d887-5892-a481-acbd552e62dc`) lines 396-398 [crates/gwiki/src/frontmatter.rs:396-398]
  - Signature: `fn string_value(value: &Value) -> Option<String> {`
  - Purpose: Indexed function `string_value` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:396-398]
- `string_list` (function) component `string_list [function]` (`72084818-7ab9-523d-aae4-8d6ce7c19b31`) lines 400-406 [crates/gwiki/src/frontmatter.rs:400-406]
  - Signature: `fn string_list(value: &Value) -> Vec<String> {`
  - Purpose: Indexed function `string_list` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:400-406]
- `string_value_str` (function) component `string_value_str [function]` (`74dbd104-6ca2-5e47-bb03-a79eb8eb7e1a`) lines 408-415 [crates/gwiki/src/frontmatter.rs:408-415]
  - Signature: `fn string_value_str(value: &str) -> Option<String> {`
  - Purpose: Indexed function `string_value_str` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:408-415]
- `tag_list` (function) component `tag_list [function]` (`6d347101-8bb8-514d-a820-82be99948bb0`) lines 419-434 [crates/gwiki/src/frontmatter.rs:419-434]
  - Signature: `fn tag_list(value: &Value) -> Vec<String> {`
  - Purpose: Indexed function `tag_list` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:419-434]
- `parse_source_kind` (function) component `parse_source_kind [function]` (`e5f13bbd-b026-53cb-b748-2d186f9a8f86`) lines 436-450 [crates/gwiki/src/frontmatter.rs:436-450]
  - Signature: `fn parse_source_kind(value: &str) -> Option<WikiSourceKind> {`
  - Purpose: Indexed function `parse_source_kind` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:436-450]
- `preserves_unknown_frontmatter` (function) component `preserves_unknown_frontmatter [function]` (`4fda93e7-4381-5019-acde-c27cd04691e1`) lines 457-524 [crates/gwiki/src/frontmatter.rs:457-524]
  - Signature: `fn preserves_unknown_frontmatter() {`
  - Purpose: Indexed function `preserves_unknown_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:457-524]
- `legacy_source_files_remain_unknown_metadata` (function) component `legacy_source_files_remain_unknown_metadata [function]` (`8fd81c16-3b26-5c3b-ac32-0690cdc59bdb`) lines 527-546 [crates/gwiki/src/frontmatter.rs:527-546]
  - Signature: `fn legacy_source_files_remain_unknown_metadata() {`
  - Purpose: Indexed function `legacy_source_files_remain_unknown_metadata` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:527-546]
- `frontmatter_migration_parses_shared_contract_keys` (function) component `frontmatter_migration_parses_shared_contract_keys [function]` (`01368509-6873-510a-9138-026736b2283e`) lines 549-578 [crates/gwiki/src/frontmatter.rs:549-578]
  - Signature: `fn frontmatter_migration_parses_shared_contract_keys() {`
  - Purpose: Indexed function `frontmatter_migration_parses_shared_contract_keys` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:549-578]
- `codewiki_contract_golden_page_parses_into_contract_fields` (function) component `codewiki_contract_golden_page_parses_into_contract_fields [function]` (`7dee62ac-f49d-56f3-b237-2fe832ecfc4f`) lines 581-626 [crates/gwiki/src/frontmatter.rs:581-626]
  - Signature: `fn codewiki_contract_golden_page_parses_into_contract_fields() {`
  - Purpose: Indexed function `codewiki_contract_golden_page_parses_into_contract_fields` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:581-626]
- `change_triggered_refresh_marks_page_stale_with_reason` (function) component `change_triggered_refresh_marks_page_stale_with_reason [function]` (`6cfa88b1-a508-52ac-b38f-c33f047fa807`) lines 629-659 [crates/gwiki/src/frontmatter.rs:629-659]
  - Signature: `fn change_triggered_refresh_marks_page_stale_with_reason() {`
  - Purpose: Indexed function `change_triggered_refresh_marks_page_stale_with_reason` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:629-659]
- `change_triggered_refresh_preserves_toml_frontmatter` (function) component `change_triggered_refresh_preserves_toml_frontmatter [function]` (`c63d4f83-2f52-5c66-a56f-8c812e238652`) lines 662-691 [crates/gwiki/src/frontmatter.rs:662-691]
  - Signature: `fn change_triggered_refresh_preserves_toml_frontmatter() {`
  - Purpose: Indexed function `change_triggered_refresh_preserves_toml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:662-691]

