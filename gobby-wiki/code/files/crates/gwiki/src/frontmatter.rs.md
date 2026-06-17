---
title: crates/gwiki/src/frontmatter.rs
type: code_file
provenance:
- file: crates/gwiki/src/frontmatter.rs
  ranges:
  - 10-13
  - 16-30
  - 33-48
  - 51-115
  - 119-125
  - 128-130
  - 133-135
  - 140-170
  - 173-191
  - 194-198
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/frontmatter.rs:10-13](crates/gwiki/src/frontmatter.rs#L10-L13), [crates/gwiki/src/frontmatter.rs:16-30](crates/gwiki/src/frontmatter.rs#L16-L30), [crates/gwiki/src/frontmatter.rs:33-48](crates/gwiki/src/frontmatter.rs#L33-L48), [crates/gwiki/src/frontmatter.rs:51-115](crates/gwiki/src/frontmatter.rs#L51-L115), [crates/gwiki/src/frontmatter.rs:119-125](crates/gwiki/src/frontmatter.rs#L119-L125), [crates/gwiki/src/frontmatter.rs:128-130](crates/gwiki/src/frontmatter.rs#L128-L130), [crates/gwiki/src/frontmatter.rs:133-135](crates/gwiki/src/frontmatter.rs#L133-L135), [crates/gwiki/src/frontmatter.rs:140-170](crates/gwiki/src/frontmatter.rs#L140-L170), [crates/gwiki/src/frontmatter.rs:173-191](crates/gwiki/src/frontmatter.rs#L173-L191), [crates/gwiki/src/frontmatter.rs:194-198](crates/gwiki/src/frontmatter.rs#L194-L198), [crates/gwiki/src/frontmatter.rs:201-205](crates/gwiki/src/frontmatter.rs#L201-L205), [crates/gwiki/src/frontmatter.rs:207-221](crates/gwiki/src/frontmatter.rs#L207-L221), [crates/gwiki/src/frontmatter.rs:223-232](crates/gwiki/src/frontmatter.rs#L223-L232), [crates/gwiki/src/frontmatter.rs:234-264](crates/gwiki/src/frontmatter.rs#L234-L264), [crates/gwiki/src/frontmatter.rs:266-286](crates/gwiki/src/frontmatter.rs#L266-L286), [crates/gwiki/src/frontmatter.rs:289-303](crates/gwiki/src/frontmatter.rs#L289-L303), [crates/gwiki/src/frontmatter.rs:306-314](crates/gwiki/src/frontmatter.rs#L306-L314), [crates/gwiki/src/frontmatter.rs:316-329](crates/gwiki/src/frontmatter.rs#L316-L329), [crates/gwiki/src/frontmatter.rs:331-344](crates/gwiki/src/frontmatter.rs#L331-L344), [crates/gwiki/src/frontmatter.rs:346-394](crates/gwiki/src/frontmatter.rs#L346-L394), [crates/gwiki/src/frontmatter.rs:396-398](crates/gwiki/src/frontmatter.rs#L396-L398), [crates/gwiki/src/frontmatter.rs:400-406](crates/gwiki/src/frontmatter.rs#L400-L406), [crates/gwiki/src/frontmatter.rs:408-415](crates/gwiki/src/frontmatter.rs#L408-L415), [crates/gwiki/src/frontmatter.rs:419-434](crates/gwiki/src/frontmatter.rs#L419-L434), [crates/gwiki/src/frontmatter.rs:436-450](crates/gwiki/src/frontmatter.rs#L436-L450), [crates/gwiki/src/frontmatter.rs:457-524](crates/gwiki/src/frontmatter.rs#L457-L524), [crates/gwiki/src/frontmatter.rs:527-546](crates/gwiki/src/frontmatter.rs#L527-L546), [crates/gwiki/src/frontmatter.rs:549-578](crates/gwiki/src/frontmatter.rs#L549-L578), [crates/gwiki/src/frontmatter.rs:581-626](crates/gwiki/src/frontmatter.rs#L581-L626), [crates/gwiki/src/frontmatter.rs:629-659](crates/gwiki/src/frontmatter.rs#L629-L659), [crates/gwiki/src/frontmatter.rs:662-691](crates/gwiki/src/frontmatter.rs#L662-L691)

</details>

# crates/gwiki/src/frontmatter.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines wiki frontmatter handling for YAML and TOML: `FrontmatterFormat` selects the wire format, while `WikiFrontmatter` stores normalized fields like title, aliases, tags, source metadata, and an `unknown` map that preserves legacy or tool-specific keys. The implementation provides `empty` and `as_json` to build and serialize a frontmatter object without losing preserved fields, then parses raw metadata by finding delimiters, extracting the content, and dispatching to YAML/TOML parsers. Helper functions convert generic objects into typed fields (`string_value`, `string_list`, `tag_list`, `parse_source_kind`) and serialize back out in each format, with tests covering preservation of unknown keys, legacy source files, contract-key parsing, and stale-markdown refresh behavior.
[crates/gwiki/src/frontmatter.rs:10-13]
[crates/gwiki/src/frontmatter.rs:16-30]
[crates/gwiki/src/frontmatter.rs:33-48]
[crates/gwiki/src/frontmatter.rs:51-115]
[crates/gwiki/src/frontmatter.rs:119-125]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `FrontmatterFormat` | type | `pub enum FrontmatterFormat {` | `FrontmatterFormat [type]` | `7d7d2878-4616-50b7-b364-5d25d085c2ff` | 10-13 [crates/gwiki/src/frontmatter.rs:10-13] | Indexed type `FrontmatterFormat` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:10-13] |
| `WikiFrontmatter` | class | `pub struct WikiFrontmatter {` | `WikiFrontmatter [class]` | `862372eb-ec1d-56e0-9087-7b29b27353b9` | 16-30 [crates/gwiki/src/frontmatter.rs:16-30] | Indexed class `WikiFrontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:16-30] |
| `WikiFrontmatter::empty` | method | `pub fn empty() -> Self {` | `WikiFrontmatter::empty [method]` | `cfca94a5-346a-517d-97f5-45935c604b86` | 33-48 [crates/gwiki/src/frontmatter.rs:33-48] | Indexed method `WikiFrontmatter::empty` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:33-48] |
| `WikiFrontmatter::as_json` | method | `pub fn as_json(&self) -> Value {` | `WikiFrontmatter::as_json [method]` | `d5dd93d0-eba1-5afa-b327-6239c38e9204` | 51-115 [crates/gwiki/src/frontmatter.rs:51-115] | Indexed method `WikiFrontmatter::as_json` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:51-115] |
| `ParsedFrontmatter` | class | `pub struct ParsedFrontmatter<'a> {` | `ParsedFrontmatter [class]` | `31fc2bd1-b6a8-55f9-ac9c-3a980c0fcdc0` | 119-125 [crates/gwiki/src/frontmatter.rs:119-125] | Indexed class `ParsedFrontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:119-125] |
| `FrontmatterError` | class | `pub struct FrontmatterError {` | `FrontmatterError [class]` | `7c7306b0-e5db-5476-8a6b-d98d89f85249` | 128-130 [crates/gwiki/src/frontmatter.rs:128-130] | Indexed class `FrontmatterError` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:128-130] |
| `FrontmatterError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `FrontmatterError::fmt [method]` | `7beb2317-7d32-50a4-aab8-e4d1a6fa790a` | 133-135 [crates/gwiki/src/frontmatter.rs:133-135] | Indexed method `FrontmatterError::fmt` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:133-135] |
| `parse_frontmatter` | function | `pub fn parse_frontmatter(markdown: &str) -> Result<ParsedFrontmatter<'_>, FrontmatterError> {` | `parse_frontmatter [function]` | `04796375-e1a3-5fa7-af29-7b585d7764a4` | 140-170 [crates/gwiki/src/frontmatter.rs:140-170] | Indexed function `parse_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:140-170] |
| `mark_stale_markdown` | function | `pub fn mark_stale_markdown(markdown: &str, reason: &str) -> Result<String, FrontmatterError> {` | `mark_stale_markdown [function]` | `ec57f434-ef82-58b6-a3ea-ebabb34d9cd5` | 173-191 [crates/gwiki/src/frontmatter.rs:173-191] | Indexed function `mark_stale_markdown` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:173-191] |
| `FrontmatterError::new` | method | `fn new(detail: impl Into<String>) -> Self {` | `FrontmatterError::new [method]` | `0ccc9212-d972-5c3c-8cc6-92f1f5f97e71` | 194-198 [crates/gwiki/src/frontmatter.rs:194-198] | Indexed method `FrontmatterError::new` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:194-198] |
| `OpeningDelimiter` | class | `struct OpeningDelimiter {` | `OpeningDelimiter [class]` | `2fd0a14f-74cd-5c63-b527-15903ca89148` | 201-205 [crates/gwiki/src/frontmatter.rs:201-205] | Indexed class `OpeningDelimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:201-205] |
| `opening_delimiter` | function | `fn opening_delimiter(markdown: &str) -> Option<OpeningDelimiter> {` | `opening_delimiter [function]` | `a3727ad6-7e39-56c1-af19-6a6dc96a508b` | 207-221 [crates/gwiki/src/frontmatter.rs:207-221] | Indexed function `opening_delimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:207-221] |
| `delimiter_content_start` | function | `fn delimiter_content_start(markdown: &str, marker: &str) -> Option<usize> {` | `delimiter_content_start [function]` | `61c8145b-351e-5354-a213-1e4b5ff85f88` | 223-232 [crates/gwiki/src/frontmatter.rs:223-232] | Indexed function `delimiter_content_start` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:223-232] |
| `find_closing_delimiter` | function | `fn find_closing_delimiter(` | `find_closing_delimiter [function]` | `6dabf274-5145-5116-ab12-740528a0b01d` | 234-264 [crates/gwiki/src/frontmatter.rs:234-264] | Indexed function `find_closing_delimiter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:234-264] |
| `parse_metadata` | function | `fn parse_metadata(` | `parse_metadata [function]` | `585c7602-49d9-56e7-bcb5-2c9d6e14f120` | 266-286 [crates/gwiki/src/frontmatter.rs:266-286] | Indexed function `parse_metadata` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:266-286] |
| `serialize_yaml_frontmatter` | function | `fn serialize_yaml_frontmatter(metadata: &WikiFrontmatter) -> Result<String, FrontmatterError> {` | `serialize_yaml_frontmatter [function]` | `b425aa16-095a-515b-8393-4c2c0607e72b` | 289-303 [crates/gwiki/src/frontmatter.rs:289-303] | Indexed function `serialize_yaml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:289-303] |
| `serialize_toml_frontmatter` | function | `fn serialize_toml_frontmatter(metadata: &WikiFrontmatter) -> Result<String, FrontmatterError> {` | `serialize_toml_frontmatter [function]` | `5b69b97a-0cc9-5358-a952-77de1c5d5e22` | 306-314 [crates/gwiki/src/frontmatter.rs:306-314] | Indexed function `serialize_toml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:306-314] |
| `parse_yaml` | function | `fn parse_yaml(raw: &str) -> Result<Value, FrontmatterError> {` | `parse_yaml [function]` | `193d073e-0157-5714-9684-23723917e586` | 316-329 [crates/gwiki/src/frontmatter.rs:316-329] | Indexed function `parse_yaml` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:316-329] |
| `parse_toml` | function | `fn parse_toml(raw: &str) -> Result<Value, FrontmatterError> {` | `parse_toml [function]` | `9b1a56b2-2237-58a5-a34f-20423a118111` | 331-344 [crates/gwiki/src/frontmatter.rs:331-344] | Indexed function `parse_toml` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:331-344] |
| `frontmatter_from_object` | function | `fn frontmatter_from_object(mut object: Map<String, Value>) -> WikiFrontmatter {` | `frontmatter_from_object [function]` | `5076c605-1a60-5d24-b173-29efc9d229da` | 346-394 [crates/gwiki/src/frontmatter.rs:346-394] | Indexed function `frontmatter_from_object` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:346-394] |
| `string_value` | function | `fn string_value(value: &Value) -> Option<String> {` | `string_value [function]` | `78f8d98e-d887-5892-a481-acbd552e62dc` | 396-398 [crates/gwiki/src/frontmatter.rs:396-398] | Indexed function `string_value` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:396-398] |
| `string_list` | function | `fn string_list(value: &Value) -> Vec<String> {` | `string_list [function]` | `72084818-7ab9-523d-aae4-8d6ce7c19b31` | 400-406 [crates/gwiki/src/frontmatter.rs:400-406] | Indexed function `string_list` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:400-406] |
| `string_value_str` | function | `fn string_value_str(value: &str) -> Option<String> {` | `string_value_str [function]` | `74dbd104-6ca2-5e47-bb03-a79eb8eb7e1a` | 408-415 [crates/gwiki/src/frontmatter.rs:408-415] | Indexed function `string_value_str` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:408-415] |
| `tag_list` | function | `fn tag_list(value: &Value) -> Vec<String> {` | `tag_list [function]` | `6d347101-8bb8-514d-a820-82be99948bb0` | 419-434 [crates/gwiki/src/frontmatter.rs:419-434] | Indexed function `tag_list` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:419-434] |
| `parse_source_kind` | function | `fn parse_source_kind(value: &str) -> Option<WikiSourceKind> {` | `parse_source_kind [function]` | `e5f13bbd-b026-53cb-b748-2d186f9a8f86` | 436-450 [crates/gwiki/src/frontmatter.rs:436-450] | Indexed function `parse_source_kind` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:436-450] |
| `preserves_unknown_frontmatter` | function | `fn preserves_unknown_frontmatter() {` | `preserves_unknown_frontmatter [function]` | `4fda93e7-4381-5019-acde-c27cd04691e1` | 457-524 [crates/gwiki/src/frontmatter.rs:457-524] | Indexed function `preserves_unknown_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:457-524] |
| `legacy_source_files_remain_unknown_metadata` | function | `fn legacy_source_files_remain_unknown_metadata() {` | `legacy_source_files_remain_unknown_metadata [function]` | `8fd81c16-3b26-5c3b-ac32-0690cdc59bdb` | 527-546 [crates/gwiki/src/frontmatter.rs:527-546] | Indexed function `legacy_source_files_remain_unknown_metadata` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:527-546] |
| `frontmatter_migration_parses_shared_contract_keys` | function | `fn frontmatter_migration_parses_shared_contract_keys() {` | `frontmatter_migration_parses_shared_contract_keys [function]` | `01368509-6873-510a-9138-026736b2283e` | 549-578 [crates/gwiki/src/frontmatter.rs:549-578] | Indexed function `frontmatter_migration_parses_shared_contract_keys` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:549-578] |
| `codewiki_contract_golden_page_parses_into_contract_fields` | function | `fn codewiki_contract_golden_page_parses_into_contract_fields() {` | `codewiki_contract_golden_page_parses_into_contract_fields [function]` | `7dee62ac-f49d-56f3-b237-2fe832ecfc4f` | 581-626 [crates/gwiki/src/frontmatter.rs:581-626] | Indexed function `codewiki_contract_golden_page_parses_into_contract_fields` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:581-626] |
| `change_triggered_refresh_marks_page_stale_with_reason` | function | `fn change_triggered_refresh_marks_page_stale_with_reason() {` | `change_triggered_refresh_marks_page_stale_with_reason [function]` | `6cfa88b1-a508-52ac-b38f-c33f047fa807` | 629-659 [crates/gwiki/src/frontmatter.rs:629-659] | Indexed function `change_triggered_refresh_marks_page_stale_with_reason` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:629-659] |
| `change_triggered_refresh_preserves_toml_frontmatter` | function | `fn change_triggered_refresh_preserves_toml_frontmatter() {` | `change_triggered_refresh_preserves_toml_frontmatter [function]` | `c63d4f83-2f52-5c66-a56f-8c812e238652` | 662-691 [crates/gwiki/src/frontmatter.rs:662-691] | Indexed function `change_triggered_refresh_preserves_toml_frontmatter` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:662-691] |
