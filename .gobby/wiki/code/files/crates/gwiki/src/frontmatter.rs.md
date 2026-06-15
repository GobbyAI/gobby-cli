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

Defines the frontmatter model and parsing/serialization pipeline for wiki markdown, supporting YAML or TOML delimiters, extracting known metadata fields into `WikiFrontmatter`, and preserving all unknown keys so legacy or tool-specific data survives round trips. The helpers work together to locate the opening and closing delimiters, parse raw frontmatter into structured JSON-backed metadata, serialize it back in the original format, and update documents with stale markers while leaving the body unchanged; `FrontmatterError` provides the common error path.
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
  - Purpose: 'WikiFrontmatter' is a frontmatter metadata container for wiki pages that stores optional title, source/provenance/trust/freshness/indexing fields, alias and tag lists, arbitrary source/provenance payloads, and a 'BTreeMap' of unknown keys to preserve legacy or tool-specific frontmatter across parsing and serialization. [crates/gwiki/src/frontmatter.rs:16-30]
- `WikiFrontmatter` (class) component `WikiFrontmatter [class]` (`23ca6438-a0eb-5b47-93a0-09260ef6a965`) lines 32-116 [crates/gwiki/src/frontmatter.rs:32-116]
  - Signature: `impl WikiFrontmatter {`
  - Purpose: 'WikiFrontmatter' is a frontmatter model that stores optional wiki metadata fields plus an 'unknown' key/value map, and can serialize itself to JSON while preserving unknown keys and omitting unset or empty fields. [crates/gwiki/src/frontmatter.rs:32-116]
- `WikiFrontmatter.empty` (method) component `WikiFrontmatter.empty [method]` (`cfca94a5-346a-517d-97f5-45935c604b86`) lines 33-48 [crates/gwiki/src/frontmatter.rs:33-48]
  - Signature: `pub fn empty() -> Self {`
  - Purpose: Constructs and returns a new instance with all optional fields set to 'None' and all collection/map fields initialized empty ('Vec::new()'/'BTreeMap::new()'). [crates/gwiki/src/frontmatter.rs:33-48]
- `WikiFrontmatter.as_json` (method) component `WikiFrontmatter.as_json [method]` (`d5dd93d0-eba1-5afa-b327-6239c38e9204`) lines 51-115 [crates/gwiki/src/frontmatter.rs:51-115]
  - Signature: `pub fn as_json(&self) -> Value {`
  - Purpose: Builds a 'serde_json::Value::Object' by starting with 'self.unknown' and conditionally inserting the present optional fields plus non-empty 'aliases' and 'tags' as JSON strings/arrays. [crates/gwiki/src/frontmatter.rs:51-115]
- `ParsedFrontmatter` (class) component `ParsedFrontmatter [class]` (`31fc2bd1-b6a8-55f9-ac9c-3a980c0fcdc0`) lines 119-125 [crates/gwiki/src/frontmatter.rs:119-125]
  - Signature: `pub struct ParsedFrontmatter<'a> {`
  - Purpose: 'ParsedFrontmatter<'a>' represents the result of parsing a document’s frontmatter, capturing the detected format and byte range if present, the body start offset, a borrowed slice of the body text, and the parsed 'WikiFrontmatter' metadata. [crates/gwiki/src/frontmatter.rs:119-125]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`7c7306b0-e5db-5476-8a6b-d98d89f85249`) lines 128-130 [crates/gwiki/src/frontmatter.rs:128-130]
  - Signature: `pub struct FrontmatterError {`
  - Purpose: 'FrontmatterError' is a struct that stores a single 'detail: String' describing a frontmatter-related error. [crates/gwiki/src/frontmatter.rs:128-130]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`5741a959-f44d-5e63-acc7-560200272a23`) lines 132-136 [crates/gwiki/src/frontmatter.rs:132-136]
  - Signature: `impl fmt::Display for FrontmatterError {`
  - Purpose: 'FrontmatterError' implements 'fmt::Display' by formatting the error as its 'detail' string via 'write!(f, "{}", self.detail)'. [crates/gwiki/src/frontmatter.rs:132-136]
- `FrontmatterError.fmt` (method) component `FrontmatterError.fmt [method]` (`7beb2317-7d32-50a4-aab8-e4d1a6fa790a`) lines 133-135 [crates/gwiki/src/frontmatter.rs:133-135]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Implements 'Display' formatting by writing the value of 'self.detail' to the provided formatter. [crates/gwiki/src/frontmatter.rs:133-135]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`70a52b78-dee4-5ac2-8102-9551220365fa`) lines 138-138 [crates/gwiki/src/frontmatter.rs:138]
  - Signature: `impl std::error::Error for FrontmatterError {}`
  - Purpose: 'FrontmatterError' is a Rust error type that implements 'std::error::Error', allowing it to integrate with standard error handling and propagation. [crates/gwiki/src/frontmatter.rs:138]
- `parse_frontmatter` (function) component `parse_frontmatter [function]` (`04796375-e1a3-5fa7-af29-7b585d7764a4`) lines 140-170 [crates/gwiki/src/frontmatter.rs:140-170]
  - Signature: `pub fn parse_frontmatter(markdown: &str) -> Result<ParsedFrontmatter<'_>, FrontmatterError> {`
  - Purpose: Parses a markdown string for an opening frontmatter delimiter, returns empty frontmatter and the original body when none is present, errors on an unterminated block, and otherwise extracts the raw frontmatter, parses its metadata, and returns the frontmatter format, byte range, body start offset, body slice, and parsed metadata. [crates/gwiki/src/frontmatter.rs:140-170]
- `mark_stale_markdown` (function) component `mark_stale_markdown [function]` (`ec57f434-ef82-58b6-a3ea-ebabb34d9cd5`) lines 173-191 [crates/gwiki/src/frontmatter.rs:173-191]
  - Signature: `pub fn mark_stale_markdown(markdown: &str, reason: &str) -> Result<String, FrontmatterError> {`
  - Purpose: Parses the markdown frontmatter, sets 'stale = true' and 'stale_reason' to the trimmed input in the unknown metadata, reserializes the frontmatter in the original format or YAML by default, and returns the updated document with the unchanged body. [crates/gwiki/src/frontmatter.rs:173-191]
- `FrontmatterError` (class) component `FrontmatterError [class]` (`512746ff-0f3b-5550-9097-eda6ccc053a1`) lines 193-199 [crates/gwiki/src/frontmatter.rs:193-199]
  - Signature: `impl FrontmatterError {`
  - Purpose: 'FrontmatterError' is a simple error wrapper that constructs a new instance by storing a provided 'detail' string converted via 'Into<String>'. [crates/gwiki/src/frontmatter.rs:193-199]
- `FrontmatterError.new` (method) component `FrontmatterError.new [method]` (`0ccc9212-d972-5c3c-8cc6-92f1f5f97e71`) lines 194-198 [crates/gwiki/src/frontmatter.rs:194-198]
  - Signature: `fn new(detail: impl Into<String>) -> Self {`
  - Purpose: Creates a 'Self' instance by converting 'detail' into a 'String' and storing it in the 'detail' field. [crates/gwiki/src/frontmatter.rs:194-198]
- `OpeningDelimiter` (class) component `OpeningDelimiter [class]` (`2fd0a14f-74cd-5c63-b527-15903ca89148`) lines 201-205 [crates/gwiki/src/frontmatter.rs:201-205]
  - Signature: `struct OpeningDelimiter {`
  - Purpose: 'OpeningDelimiter' is a value object that records a frontmatter opening delimiter by its 'FrontmatterFormat', the delimiter 'marker' string, and the byte index 'content_start' where the frontmatter content begins. [crates/gwiki/src/frontmatter.rs:201-205]
- `opening_delimiter` (function) component `opening_delimiter [function]` (`a3727ad6-7e39-56c1-af19-6a6dc96a508b`) lines 207-221 [crates/gwiki/src/frontmatter.rs:207-221]
  - Signature: `fn opening_delimiter(markdown: &str) -> Option<OpeningDelimiter> {`
  - Purpose: Returns the first frontmatter opening delimiter in 'markdown', preferring YAML '---' over TOML '+++', and constructs an 'OpeningDelimiter' with the corresponding format, marker, and content start offset. [crates/gwiki/src/frontmatter.rs:207-221]
- `delimiter_content_start` (function) component `delimiter_content_start [function]` (`61c8145b-351e-5354-a213-1e4b5ff85f88`) lines 223-232 [crates/gwiki/src/frontmatter.rs:223-232]
  - Signature: `fn delimiter_content_start(markdown: &str, marker: &str) -> Option<usize> {`
  - Purpose: Returns the byte offset immediately after a leading 'marker' and a following line ending ('\r\n' or '\n') in 'markdown', or 'None' if the string does not start with that exact delimiter pattern. [crates/gwiki/src/frontmatter.rs:223-232]
- `find_closing_delimiter` (function) component `find_closing_delimiter [function]` (`6dabf274-5145-5116-ab12-740528a0b01d`) lines 234-264 [crates/gwiki/src/frontmatter.rs:234-264]
  - Signature: `fn find_closing_delimiter(`
  - Purpose: Scans 'markdown' from 'offset' line by line, normalizing an optional trailing '\r', and returns the byte range start of the first line whose trimmed contents exactly match 'marker' plus the byte index where the following body begins, or 'None' if no such line exists. [crates/gwiki/src/frontmatter.rs:234-264]
- `parse_metadata` (function) component `parse_metadata [function]` (`585c7602-49d9-56e7-bcb5-2c9d6e14f120`) lines 266-286 [crates/gwiki/src/frontmatter.rs:266-286]
  - Signature: `fn parse_metadata(`
  - Purpose: 'parse_metadata' parses the raw frontmatter as YAML or TOML based on 'format', requires the result to be a map/object or null, and converts that object into a 'WikiFrontmatter', returning a 'FrontmatterError' for parse failures or non-object frontmatter. [crates/gwiki/src/frontmatter.rs:266-286]
- `serialize_yaml_frontmatter` (function) component `serialize_yaml_frontmatter [function]` (`b425aa16-095a-515b-8393-4c2c0607e72b`) lines 289-303 [crates/gwiki/src/frontmatter.rs:289-303]
  - Signature: `fn serialize_yaml_frontmatter(metadata: &WikiFrontmatter) -> Result<String, FrontmatterError> {`
  - Purpose: Serializes 'WikiFrontmatter' to a YAML string via 'serde_yaml', removes a leading '---\n' and trailing '...\n' if present, ensures a final newline, and returns a 'FrontmatterError' if serialization fails. [crates/gwiki/src/frontmatter.rs:289-303]
- `serialize_toml_frontmatter` (function) component `serialize_toml_frontmatter [function]` (`5b69b97a-0cc9-5358-a952-77de1c5d5e22`) lines 306-314 [crates/gwiki/src/frontmatter.rs:306-314]
  - Signature: `fn serialize_toml_frontmatter(metadata: &WikiFrontmatter) -> Result<String, FrontmatterError> {`
  - Purpose: Serializes 'WikiFrontmatter' to TOML by converting 'metadata.as_json()' with 'toml::to_string', mapping serialization failures into 'FrontmatterError', and guaranteeing the returned string ends with a trailing newline. [crates/gwiki/src/frontmatter.rs:306-314]
- `parse_yaml` (function) component `parse_yaml [function]` (`193d073e-0157-5714-9684-23723917e586`) lines 316-329 [crates/gwiki/src/frontmatter.rs:316-329]
  - Signature: `fn parse_yaml(raw: &str) -> Result<Value, FrontmatterError> {`
  - Purpose: Parses a YAML frontmatter string into a 'serde_json::Value', returning an empty object for blank input and mapping YAML parse or YAML-to-JSON conversion failures into 'FrontmatterError'. [crates/gwiki/src/frontmatter.rs:316-329]
- `parse_toml` (function) component `parse_toml [function]` (`9b1a56b2-2237-58a5-a34f-20423a118111`) lines 331-344 [crates/gwiki/src/frontmatter.rs:331-344]
  - Signature: `fn parse_toml(raw: &str) -> Result<Value, FrontmatterError> {`
  - Purpose: Returns an empty JSON object for blank input, otherwise parses the TOML string into a 'toml::Table' and converts it to a 'serde_json::Value', wrapping parse or conversion failures in 'FrontmatterError'. [crates/gwiki/src/frontmatter.rs:331-344]
- `frontmatter_from_object` (function) component `frontmatter_from_object [function]` (`5076c605-1a60-5d24-b173-29efc9d229da`) lines 346-394 [crates/gwiki/src/frontmatter.rs:346-394]
  - Signature: `fn frontmatter_from_object(mut object: Map<String, Value>) -> WikiFrontmatter {`
  - Purpose: Constructs a 'WikiFrontmatter' by extracting and type-coercing known fields from a JSON object map, supporting legacy aliases for 'source_kind', preserving the raw 'source' and 'provenance' values, and storing all unrecognized key-value pairs in 'unknown'. [crates/gwiki/src/frontmatter.rs:346-394]
- `string_value` (function) component `string_value [function]` (`78f8d98e-d887-5892-a481-acbd552e62dc`) lines 396-398 [crates/gwiki/src/frontmatter.rs:396-398]
  - Signature: `fn string_value(value: &Value) -> Option<String> {`
  - Purpose: Returns 'Some(String)' by passing the inner '&str' from 'value.as_str()' to 'string_value_str', and returns 'None' for non-string values or when the helper yields no result. [crates/gwiki/src/frontmatter.rs:396-398]
- `string_list` (function) component `string_list [function]` (`72084818-7ab9-523d-aae4-8d6ce7c19b31`) lines 400-406 [crates/gwiki/src/frontmatter.rs:400-406]
  - Signature: `fn string_list(value: &Value) -> Vec<String> {`
  - Purpose: Returns a 'Vec<String>' by converting a JSON 'Value::String' into zero or one normalized string, extracting and filtering all string-like elements from a 'Value::Array', and returning an empty vector for all other 'Value' variants. [crates/gwiki/src/frontmatter.rs:400-406]
- `string_value_str` (function) component `string_value_str [function]` (`74dbd104-6ca2-5e47-bb03-a79eb8eb7e1a`) lines 408-415 [crates/gwiki/src/frontmatter.rs:408-415]
  - Signature: `fn string_value_str(value: &str) -> Option<String> {`
  - Purpose: Trims surrounding whitespace from 'value' and returns 'None' if the result is empty, otherwise returns 'Some' containing the trimmed string as an owned 'String'. [crates/gwiki/src/frontmatter.rs:408-415]
- `tag_list` (function) component `tag_list [function]` (`6d347101-8bb8-514d-a820-82be99948bb0`) lines 419-434 [crates/gwiki/src/frontmatter.rs:419-434]
  - Signature: `fn tag_list(value: &Value) -> Vec<String> {`
  - Purpose: 'tag_list' converts a JSON 'Value' into a 'Vec<String>' by extracting tags from either a string split on commas or whitespace, or from an array of string values, trimming whitespace and leading '#' characters and discarding non-string or empty entries. [crates/gwiki/src/frontmatter.rs:419-434]
- `parse_source_kind` (function) component `parse_source_kind [function]` (`e5f13bbd-b026-53cb-b748-2d186f9a8f86`) lines 436-450 [crates/gwiki/src/frontmatter.rs:436-450]
  - Signature: `fn parse_source_kind(value: &str) -> Option<WikiSourceKind> {`
  - Purpose: Parses a string into a 'WikiSourceKind' by trimming, lowercasing, and normalizing hyphens/spaces to underscores, returning 'Some' for 'raw', 'source_note', 'concept', 'topic', or 'inbox', and 'None' otherwise. [crates/gwiki/src/frontmatter.rs:436-450]
- `preserves_unknown_frontmatter` (function) component `preserves_unknown_frontmatter [function]` (`4fda93e7-4381-5019-acde-c27cd04691e1`) lines 457-524 [crates/gwiki/src/frontmatter.rs:457-524]
  - Signature: `fn preserves_unknown_frontmatter() {`
  - Purpose: Verifies that 'parse_frontmatter' correctly parses YAML and TOML frontmatter while preserving unrecognized keys and nested values in 'metadata.unknown' without disturbing the extracted body or known fields. [crates/gwiki/src/frontmatter.rs:457-524]
- `legacy_source_files_remain_unknown_metadata` (function) component `legacy_source_files_remain_unknown_metadata [function]` (`8fd81c16-3b26-5c3b-ac32-0690cdc59bdb`) lines 527-546 [crates/gwiki/src/frontmatter.rs:527-546]
  - Signature: `fn legacy_source_files_remain_unknown_metadata() {`
  - Purpose: Verifies that legacy 'source_files' frontmatter is preserved as unknown metadata while 'source' and 'provenance' remain 'None', and that the parsed body starts after the frontmatter. [crates/gwiki/src/frontmatter.rs:527-546]
- `frontmatter_migration_parses_shared_contract_keys` (function) component `frontmatter_migration_parses_shared_contract_keys [function]` (`01368509-6873-510a-9138-026736b2283e`) lines 549-578 [crates/gwiki/src/frontmatter.rs:549-578]
  - Signature: `fn frontmatter_migration_parses_shared_contract_keys() {`
  - Purpose: Verifies that 'parse_frontmatter' correctly reads shared contract keys ('generated_by', 'trust', 'freshness', 'source', and 'provenance') into structured metadata and does not leave 'source' or 'provenance' in the unknown-field map. [crates/gwiki/src/frontmatter.rs:549-578]
- `codewiki_contract_golden_page_parses_into_contract_fields` (function) component `codewiki_contract_golden_page_parses_into_contract_fields [function]` (`7dee62ac-f49d-56f3-b237-2fe832ecfc4f`) lines 581-626 [crates/gwiki/src/frontmatter.rs:581-626]
  - Signature: `fn codewiki_contract_golden_page_parses_into_contract_fields() {`
  - Purpose: Verifies that 'codewiki_contract::GOLDEN_PAGE' frontmatter parses into the expected contract metadata fields ('title', 'generated_by', 'trust', 'freshness', and provenance file/ranges) and that its body contains a wikilink resolving to 'code/files/src/lib.rs'. [crates/gwiki/src/frontmatter.rs:581-626]
- `change_triggered_refresh_marks_page_stale_with_reason` (function) component `change_triggered_refresh_marks_page_stale_with_reason [function]` (`6cfa88b1-a508-52ac-b38f-c33f047fa807`) lines 629-659 [crates/gwiki/src/frontmatter.rs:629-659]
  - Signature: `fn change_triggered_refresh_marks_page_stale_with_reason() {`
  - Purpose: Verifies that 'mark_stale_markdown' adds 'stale=true' and a 'stale_reason' of '"src/lib.rs changed"' to frontmatter while preserving the original title and body content. [crates/gwiki/src/frontmatter.rs:629-659]
- `change_triggered_refresh_preserves_toml_frontmatter` (function) component `change_triggered_refresh_preserves_toml_frontmatter [function]` (`c63d4f83-2f52-5c66-a56f-8c812e238652`) lines 662-691 [crates/gwiki/src/frontmatter.rs:662-691]
  - Signature: `fn change_triggered_refresh_preserves_toml_frontmatter() {`
  - Purpose: Verifies that 'mark_stale_markdown' preserves TOML frontmatter formatting and existing fields while adding 'stale = true' and 'stale_reason = "src/lib.rs changed"', and that the resulting document still parses with the original body and title intact. [crates/gwiki/src/frontmatter.rs:662-691]

