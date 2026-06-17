---
title: crates/gwiki/src/ingest/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/mod.rs
  ranges:
  - 29-33
  - 35-40
  - 42-50
  - 52-61
  - 63-77
  - 79-89
  - 91-111
  - 113-121
  - 124-139
  - 141-147
  - 150-155
  - 158-160
  - 162-164
  - 166-168
  - 170-172
  - 175-185
  - 187-194
  - 196-202
  - 204-211
  - 213-220
  - 222-229
  - 231-251
  - 253-255
  - 257-260
  - 262-269
  - 271-273
  - 275-277
  - 279-281
  - 283-285
  - 287-289
  - 291-330
  - 332-382
  - 384-399
  - 401-416
  - 418-435
  - 437-445
  - 447-474
  - 478-483
  - 485-499
  - 501-507
  - 534-543
  - 545-551
  - 553-568
  - 571-582
  - 585-611
  - 614-629
  - 632-649
  - 652-701
  - 704-750
  - 753-758
  - 761-768
  - 770-776
  - 780-784
  - 786-789
  - 791-798
  - 800-803
  - 805-808
  - 810-813
  - 815-822
  - 824-827
  - 831-864
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/mod.rs:29-33](crates/gwiki/src/ingest/mod.rs#L29-L33), [crates/gwiki/src/ingest/mod.rs:35-40](crates/gwiki/src/ingest/mod.rs#L35-L40), [crates/gwiki/src/ingest/mod.rs:42-50](crates/gwiki/src/ingest/mod.rs#L42-L50), [crates/gwiki/src/ingest/mod.rs:52-61](crates/gwiki/src/ingest/mod.rs#L52-L61), [crates/gwiki/src/ingest/mod.rs:63-77](crates/gwiki/src/ingest/mod.rs#L63-L77), [crates/gwiki/src/ingest/mod.rs:79-89](crates/gwiki/src/ingest/mod.rs#L79-L89), [crates/gwiki/src/ingest/mod.rs:91-111](crates/gwiki/src/ingest/mod.rs#L91-L111), [crates/gwiki/src/ingest/mod.rs:113-121](crates/gwiki/src/ingest/mod.rs#L113-L121), [crates/gwiki/src/ingest/mod.rs:124-139](crates/gwiki/src/ingest/mod.rs#L124-L139), [crates/gwiki/src/ingest/mod.rs:141-147](crates/gwiki/src/ingest/mod.rs#L141-L147), [crates/gwiki/src/ingest/mod.rs:150-155](crates/gwiki/src/ingest/mod.rs#L150-L155), [crates/gwiki/src/ingest/mod.rs:158-160](crates/gwiki/src/ingest/mod.rs#L158-L160), [crates/gwiki/src/ingest/mod.rs:162-164](crates/gwiki/src/ingest/mod.rs#L162-L164), [crates/gwiki/src/ingest/mod.rs:166-168](crates/gwiki/src/ingest/mod.rs#L166-L168), [crates/gwiki/src/ingest/mod.rs:170-172](crates/gwiki/src/ingest/mod.rs#L170-L172), [crates/gwiki/src/ingest/mod.rs:175-185](crates/gwiki/src/ingest/mod.rs#L175-L185), [crates/gwiki/src/ingest/mod.rs:187-194](crates/gwiki/src/ingest/mod.rs#L187-L194), [crates/gwiki/src/ingest/mod.rs:196-202](crates/gwiki/src/ingest/mod.rs#L196-L202), [crates/gwiki/src/ingest/mod.rs:204-211](crates/gwiki/src/ingest/mod.rs#L204-L211), [crates/gwiki/src/ingest/mod.rs:213-220](crates/gwiki/src/ingest/mod.rs#L213-L220), [crates/gwiki/src/ingest/mod.rs:222-229](crates/gwiki/src/ingest/mod.rs#L222-L229), [crates/gwiki/src/ingest/mod.rs:231-251](crates/gwiki/src/ingest/mod.rs#L231-L251), [crates/gwiki/src/ingest/mod.rs:253-255](crates/gwiki/src/ingest/mod.rs#L253-L255), [crates/gwiki/src/ingest/mod.rs:257-260](crates/gwiki/src/ingest/mod.rs#L257-L260), [crates/gwiki/src/ingest/mod.rs:262-269](crates/gwiki/src/ingest/mod.rs#L262-L269), [crates/gwiki/src/ingest/mod.rs:271-273](crates/gwiki/src/ingest/mod.rs#L271-L273), [crates/gwiki/src/ingest/mod.rs:275-277](crates/gwiki/src/ingest/mod.rs#L275-L277), [crates/gwiki/src/ingest/mod.rs:279-281](crates/gwiki/src/ingest/mod.rs#L279-L281), [crates/gwiki/src/ingest/mod.rs:283-285](crates/gwiki/src/ingest/mod.rs#L283-L285), [crates/gwiki/src/ingest/mod.rs:287-289](crates/gwiki/src/ingest/mod.rs#L287-L289), [crates/gwiki/src/ingest/mod.rs:291-330](crates/gwiki/src/ingest/mod.rs#L291-L330), [crates/gwiki/src/ingest/mod.rs:332-382](crates/gwiki/src/ingest/mod.rs#L332-L382), [crates/gwiki/src/ingest/mod.rs:384-399](crates/gwiki/src/ingest/mod.rs#L384-L399), [crates/gwiki/src/ingest/mod.rs:401-416](crates/gwiki/src/ingest/mod.rs#L401-L416), [crates/gwiki/src/ingest/mod.rs:418-435](crates/gwiki/src/ingest/mod.rs#L418-L435), [crates/gwiki/src/ingest/mod.rs:437-445](crates/gwiki/src/ingest/mod.rs#L437-L445), [crates/gwiki/src/ingest/mod.rs:447-474](crates/gwiki/src/ingest/mod.rs#L447-L474), [crates/gwiki/src/ingest/mod.rs:478-483](crates/gwiki/src/ingest/mod.rs#L478-L483), [crates/gwiki/src/ingest/mod.rs:485-499](crates/gwiki/src/ingest/mod.rs#L485-L499), [crates/gwiki/src/ingest/mod.rs:501-507](crates/gwiki/src/ingest/mod.rs#L501-L507), [crates/gwiki/src/ingest/mod.rs:534-543](crates/gwiki/src/ingest/mod.rs#L534-L543), [crates/gwiki/src/ingest/mod.rs:545-551](crates/gwiki/src/ingest/mod.rs#L545-L551), [crates/gwiki/src/ingest/mod.rs:553-568](crates/gwiki/src/ingest/mod.rs#L553-L568), [crates/gwiki/src/ingest/mod.rs:571-582](crates/gwiki/src/ingest/mod.rs#L571-L582), [crates/gwiki/src/ingest/mod.rs:585-611](crates/gwiki/src/ingest/mod.rs#L585-L611), [crates/gwiki/src/ingest/mod.rs:614-629](crates/gwiki/src/ingest/mod.rs#L614-L629), [crates/gwiki/src/ingest/mod.rs:632-649](crates/gwiki/src/ingest/mod.rs#L632-L649), [crates/gwiki/src/ingest/mod.rs:652-701](crates/gwiki/src/ingest/mod.rs#L652-L701), [crates/gwiki/src/ingest/mod.rs:704-750](crates/gwiki/src/ingest/mod.rs#L704-L750), [crates/gwiki/src/ingest/mod.rs:753-758](crates/gwiki/src/ingest/mod.rs#L753-L758), [crates/gwiki/src/ingest/mod.rs:761-768](crates/gwiki/src/ingest/mod.rs#L761-L768), [crates/gwiki/src/ingest/mod.rs:770-776](crates/gwiki/src/ingest/mod.rs#L770-L776), [crates/gwiki/src/ingest/mod.rs:780-784](crates/gwiki/src/ingest/mod.rs#L780-L784), [crates/gwiki/src/ingest/mod.rs:786-789](crates/gwiki/src/ingest/mod.rs#L786-L789), [crates/gwiki/src/ingest/mod.rs:791-798](crates/gwiki/src/ingest/mod.rs#L791-L798), [crates/gwiki/src/ingest/mod.rs:800-803](crates/gwiki/src/ingest/mod.rs#L800-L803), [crates/gwiki/src/ingest/mod.rs:805-808](crates/gwiki/src/ingest/mod.rs#L805-L808), [crates/gwiki/src/ingest/mod.rs:810-813](crates/gwiki/src/ingest/mod.rs#L810-L813), [crates/gwiki/src/ingest/mod.rs:815-822](crates/gwiki/src/ingest/mod.rs#L815-L822), [crates/gwiki/src/ingest/mod.rs:824-827](crates/gwiki/src/ingest/mod.rs#L824-L827), [crates/gwiki/src/ingest/mod.rs:831-864](crates/gwiki/src/ingest/mod.rs#L831-L864)

</details>

# crates/gwiki/src/ingest/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Helpers for ingesting immutable raw wiki sources. The module ties together source-specific ingest submodules and provides the shared plumbing for writing raw markdown and assets into the vault, normalizing file extensions and asset names, and building markdown/YAML metadata safely. It also enforces the raw-first ingest workflow by validating existing files and source hashes, creating temporary raw files when needed, and coordinating indexing through `index_after_ingest` and the `RawFirstStore` adapter so external connectors can persist raw content before derived wiki data is updated.
[crates/gwiki/src/ingest/mod.rs:29-33]
[crates/gwiki/src/ingest/mod.rs:35-40]
[crates/gwiki/src/ingest/mod.rs:42-50]
[crates/gwiki/src/ingest/mod.rs:52-61]
[crates/gwiki/src/ingest/mod.rs:63-77]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IngestResult` | class | `pub struct IngestResult {` | `IngestResult [class]` | `039b6212-1767-5f3b-831d-00b5f7e2c81d` | 29-33 [crates/gwiki/src/ingest/mod.rs:29-33] | Indexed class `IngestResult` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:29-33] |
| `lowercase_extension` | function | `pub(crate) fn lowercase_extension(path: impl AsRef<Path>) -> Option<String> {` | `lowercase_extension [function]` | `37e82625-a996-5433-9895-23a2264a08db` | 35-40 [crates/gwiki/src/ingest/mod.rs:35-40] | Indexed function `lowercase_extension` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:35-40] |
| `write_raw_markdown` | function | `pub(crate) fn write_raw_markdown(` | `write_raw_markdown [function]` | `97f5d1f5-a236-5a9d-9a71-6284e82d559e` | 42-50 [crates/gwiki/src/ingest/mod.rs:42-50] | Indexed function `write_raw_markdown` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:42-50] |
| `write_asset` | function | `pub(crate) fn write_asset(` | `write_asset [function]` | `f4cce6dd-7da3-55ac-9b6f-9e5ab327c3f5` | 52-61 [crates/gwiki/src/ingest/mod.rs:52-61] | Indexed function `write_asset` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:52-61] |
| `write_asset_with_suffix` | function | `pub(crate) fn write_asset_with_suffix(` | `write_asset_with_suffix [function]` | `1bc36c9a-fe4b-5942-85df-80622a1f81c8` | 63-77 [crates/gwiki/src/ingest/mod.rs:63-77] | Indexed function `write_asset_with_suffix` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:63-77] |
| `write_asset_from_path` | function | `pub(crate) fn write_asset_from_path(` | `write_asset_from_path [function]` | `b2f846bf-0245-52d9-8142-4fef3b099994` | 79-89 [crates/gwiki/src/ingest/mod.rs:79-89] | Indexed function `write_asset_from_path` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:79-89] |
| `sanitize_asset_suffix` | function | `fn sanitize_asset_suffix(value: &str) -> String {` | `sanitize_asset_suffix [function]` | `4ee28def-f3bf-5241-acfd-7198d7c21466` | 91-111 [crates/gwiki/src/ingest/mod.rs:91-111] | Indexed function `sanitize_asset_suffix` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:91-111] |
| `index_after_ingest` | function | `pub(crate) fn index_after_ingest(` | `index_after_ingest [function]` | `bd494856-c957-5339-9143-c30a026a49b3` | 113-121 [crates/gwiki/src/ingest/mod.rs:113-121] | Indexed function `index_after_ingest` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:113-121] |
| `write_raw_then_index` | function | `pub(crate) fn write_raw_then_index(` | `write_raw_then_index [function]` | `bdb498d8-73ed-5c0e-8206-641a8230309d` | 124-139 [crates/gwiki/src/ingest/mod.rs:124-139] | Indexed function `write_raw_then_index` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:124-139] |
| `markdown_metadata` | function | `pub(crate) fn markdown_metadata(fields: &[(&str, String)]) -> String {` | `markdown_metadata [function]` | `a25bcd12-6963-5c0f-a33e-09210c63a8f6` | 141-147 [crates/gwiki/src/ingest/mod.rs:141-147] | Indexed function `markdown_metadata` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:141-147] |
| `MetadataValue` | type | `pub(crate) enum MetadataValue {` | `MetadataValue [type]` | `d68b1ba5-492d-5af0-be81-d7214f66b05d` | 150-155 [crates/gwiki/src/ingest/mod.rs:150-155] | Indexed type `MetadataValue` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:150-155] |
| `MetadataValue::string` | method | `pub(crate) fn string(value: impl Into<String>) -> Self {` | `MetadataValue::string [method]` | `3a4b2516-a33b-5931-a250-f60a65d673bb` | 158-160 [crates/gwiki/src/ingest/mod.rs:158-160] | Indexed method `MetadataValue::string` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:158-160] |
| `MetadataValue::number` | method | `pub(crate) fn number(value: impl ToString) -> Self {` | `MetadataValue::number [method]` | `9a619182-b988-5d83-bb73-9928c9f1ecb4` | 162-164 [crates/gwiki/src/ingest/mod.rs:162-164] | Indexed method `MetadataValue::number` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:162-164] |
| `MetadataValue::bool` | method | `pub(crate) fn bool(value: bool) -> Self {` | `MetadataValue::bool [method]` | `db7e3aa9-0f20-5c91-a6aa-aa2d8285ad2a` | 166-168 [crates/gwiki/src/ingest/mod.rs:166-168] | Indexed method `MetadataValue::bool` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:166-168] |
| `MetadataValue::json` | method | `pub(crate) fn json(value: impl Serialize) -> Self {` | `MetadataValue::json [method]` | `139a1d2f-1932-55e3-a1be-fb17149ce453` | 170-172 [crates/gwiki/src/ingest/mod.rs:170-172] | Indexed method `MetadataValue::json` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:170-172] |
| `markdown_metadata_values` | function | `pub(crate) fn markdown_metadata_values(fields: &[(&str, MetadataValue)]) -> String {` | `markdown_metadata_values [function]` | `5274fa0c-636b-5c25-80ac-9b4779e43966` | 175-185 [crates/gwiki/src/ingest/mod.rs:175-185] | Indexed function `markdown_metadata_values` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:175-185] |
| `yaml_metadata_value` | function | `fn yaml_metadata_value(key: &str, value: &MetadataValue) -> String {` | `yaml_metadata_value [function]` | `8c2fd750-142a-5c80-b524-b91f58ab6dfc` | 187-194 [crates/gwiki/src/ingest/mod.rs:187-194] | Indexed function `yaml_metadata_value` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:187-194] |
| `yaml_metadata_scalar` | function | `fn yaml_metadata_scalar(key: &str, value: &str) -> String {` | `yaml_metadata_scalar [function]` | `fbdbb95c-e01d-56d6-ba2f-44ceb09e64d6` | 196-202 [crates/gwiki/src/ingest/mod.rs:196-202] | Indexed function `yaml_metadata_scalar` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:196-202] |
| `yaml_safe_single_line_scalar` | function | `fn yaml_safe_single_line_scalar(value: &str) -> String {` | `yaml_safe_single_line_scalar [function]` | `d6f23b96-a226-5322-a128-0315642dec56` | 204-211 [crates/gwiki/src/ingest/mod.rs:204-211] | Indexed function `yaml_safe_single_line_scalar` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:204-211] |
| `yaml_numeric_scalar` | function | `fn yaml_numeric_scalar(value: &str) -> String {` | `yaml_numeric_scalar [function]` | `6c222def-e237-5eae-8d20-e784a2f15438` | 213-220 [crates/gwiki/src/ingest/mod.rs:213-220] | Indexed function `yaml_numeric_scalar` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:213-220] |
| `yaml_json_value` | function | `fn yaml_json_value(value: &str) -> String {` | `yaml_json_value [function]` | `6392045e-bcbe-50c1-8d52-bc3f79576afe` | 222-229 [crates/gwiki/src/ingest/mod.rs:222-229] | Indexed function `yaml_json_value` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:222-229] |
| `yaml_plain_scalar_is_safe` | function | `fn yaml_plain_scalar_is_safe(value: &str) -> bool {` | `yaml_plain_scalar_is_safe [function]` | `95b9fa59-bd17-5dbd-b103-b516fb644e27` | 231-251 [crates/gwiki/src/ingest/mod.rs:231-251] | Indexed function `yaml_plain_scalar_is_safe` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:231-251] |
| `yaml_numeric_scalar_is_safe` | function | `fn yaml_numeric_scalar_is_safe(value: &str) -> bool {` | `yaml_numeric_scalar_is_safe [function]` | `2ab4786b-d3e2-560d-8e33-98b8300bc10c` | 253-255 [crates/gwiki/src/ingest/mod.rs:253-255] | Indexed function `yaml_numeric_scalar_is_safe` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:253-255] |
| `yaml_plain_scalar_is_timestamp` | function | `fn yaml_plain_scalar_is_timestamp(value: &str) -> bool {` | `yaml_plain_scalar_is_timestamp [function]` | `1b6cc9d9-61c9-52e0-9024-c7c73628fc67` | 257-260 [crates/gwiki/src/ingest/mod.rs:257-260] | Indexed function `yaml_plain_scalar_is_timestamp` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:257-260] |
| `has_yaml_date_prefix` | function | `fn has_yaml_date_prefix(bytes: &[u8]) -> bool {` | `has_yaml_date_prefix [function]` | `6894c5b9-2c52-5f6a-ba6f-1c4709d39cbd` | 262-269 [crates/gwiki/src/ingest/mod.rs:262-269] | Indexed function `has_yaml_date_prefix` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:262-269] |
| `quote_yaml_string` | function | `fn quote_yaml_string(value: &str) -> String {` | `quote_yaml_string [function]` | `2e118c4f-3a60-5fe7-b6f9-53e082412478` | 271-273 [crates/gwiki/src/ingest/mod.rs:271-273] | Indexed function `quote_yaml_string` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:271-273] |
| `single_line` | function | `pub(crate) fn single_line(value: &str) -> String {` | `single_line [function]` | `fac74773-a20c-5e48-9d44-26a246d8427b` | 275-277 [crates/gwiki/src/ingest/mod.rs:275-277] | Indexed function `single_line` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:275-277] |
| `markdown_title` | function | `pub(crate) fn markdown_title(value: &str) -> String {` | `markdown_title [function]` | `cd78a6b4-e6e8-5897-bde0-e08a52bc9407` | 279-281 [crates/gwiki/src/ingest/mod.rs:279-281] | Indexed function `markdown_title` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:279-281] |
| `text_from_utf8_lossy` | function | `pub(crate) fn text_from_utf8_lossy(bytes: &[u8]) -> String {` | `text_from_utf8_lossy [function]` | `e7c267d0-b26f-5ee3-bb78-ceb04a2f8ad3` | 283-285 [crates/gwiki/src/ingest/mod.rs:283-285] | Indexed function `text_from_utf8_lossy` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:283-285] |
| `path_to_string` | function | `pub(crate) fn path_to_string(path: &Path) -> String {` | `path_to_string [function]` | `6236326a-b681-57e0-a759-442081c805d5` | 287-289 [crates/gwiki/src/ingest/mod.rs:287-289] | Indexed function `path_to_string` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:287-289] |
| `write_immutable` | function | `fn write_immutable(vault_root: &Path, relative: &Path, bytes: &[u8]) -> Result<(), WikiError> {` | `write_immutable [function]` | `206f714d-125f-5473-876d-c490bd2868e4` | 291-330 [crates/gwiki/src/ingest/mod.rs:291-330] | Indexed function `write_immutable` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:291-330] |
| `write_immutable_file` | function | `fn write_immutable_file(` | `write_immutable_file [function]` | `63311152-bb72-5010-8891-de154791407e` | 332-382 [crates/gwiki/src/ingest/mod.rs:332-382] | Indexed function `write_immutable_file` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:332-382] |
| `validate_existing_raw_bytes` | function | `fn validate_existing_raw_bytes(` | `validate_existing_raw_bytes [function]` | `b21228b3-1f6e-5219-bbf4-fc8dda5779f7` | 384-399 [crates/gwiki/src/ingest/mod.rs:384-399] | Indexed function `validate_existing_raw_bytes` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:384-399] |
| `validate_existing_raw_file` | function | `fn validate_existing_raw_file(` | `validate_existing_raw_file [function]` | `4cd1feb3-b726-5631-af2a-d04ba55b9178` | 401-416 [crates/gwiki/src/ingest/mod.rs:401-416] | Indexed function `validate_existing_raw_file` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:401-416] |
| `validate_source_file_hash` | function | `fn validate_source_file_hash(source_path: &Path, content_hash: &str) -> Result<String, WikiError> {` | `validate_source_file_hash [function]` | `64621cb1-2f49-538f-8d4e-84660e99fa4c` | 418-435 [crates/gwiki/src/ingest/mod.rs:418-435] | Indexed function `validate_source_file_hash` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:418-435] |
| `immutable_exists_error` | function | `fn immutable_exists_error(relative: &Path) -> WikiError {` | `immutable_exists_error [function]` | `1ca9551f-7d9c-59cc-af0e-64a3dbcea06c` | 437-445 [crates/gwiki/src/ingest/mod.rs:437-445] | Indexed function `immutable_exists_error` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:437-445] |
| `create_raw_temp_file` | function | `fn create_raw_temp_file(path: &Path) -> Result<tempfile::NamedTempFile, WikiError> {` | `create_raw_temp_file [function]` | `bbd224c3-a6fd-5d88-9a87-aa7b2876b8bb` | 447-474 [crates/gwiki/src/ingest/mod.rs:447-474] | Indexed function `create_raw_temp_file` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:447-474] |
| `asset_path` | function | `pub(crate) fn asset_path(record: &SourceRecord, file_name: &str) -> PathBuf {` | `asset_path [function]` | `6da093b4-05ad-57f1-b31d-3bde60bbc5f5` | 478-483 [crates/gwiki/src/ingest/mod.rs:478-483] | Indexed function `asset_path` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:478-483] |
| `sanitized_extension_for_file_name` | function | `fn sanitized_extension_for_file_name(file_name: &str) -> String {` | `sanitized_extension_for_file_name [function]` | `968c6b65-1c43-5545-b72e-9654ae5da29e` | 485-499 [crates/gwiki/src/ingest/mod.rs:485-499] | Indexed function `sanitized_extension_for_file_name` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:485-499] |
| `sanitize_extension` | function | `fn sanitize_extension(extension: &str) -> String {` | `sanitize_extension [function]` | `94a0a060-1ca3-56e3-9a54-69eaba871b83` | 501-507 [crates/gwiki/src/ingest/mod.rs:501-507] | Indexed function `sanitize_extension` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:501-507] |
| `no_ai_context` | function | `fn no_ai_context() -> AiContext {` | `no_ai_context [function]` | `d0082fc8-3c69-5ee0-b1c6-530f7fd3e438` | 534-543 [crates/gwiki/src/ingest/mod.rs:534-543] | Indexed function `no_ai_context` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:534-543] |
| `write_file` | function | `fn write_file(root: &std::path::Path, relative: &str, contents: &str) {` | `write_file [function]` | `87db0649-b8b6-5934-96e3-3a16944e53d2` | 545-551 [crates/gwiki/src/ingest/mod.rs:545-551] | Indexed function `write_file` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:545-551] |
| `test_source_record` | function | `fn test_source_record() -> SourceRecord {` | `test_source_record [function]` | `87745c9c-4bfa-5c91-8063-b200f8f5b647` | 553-568 [crates/gwiki/src/ingest/mod.rs:553-568] | Indexed function `test_source_record` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:553-568] |
| `asset_path_uses_basename_before_extension_extraction` | function | `fn asset_path_uses_basename_before_extension_extraction() {` | `asset_path_uses_basename_before_extension_extraction [function]` | `8ee98c72-d874-5f91-95db-ad3afec4c5af` | 571-582 [crates/gwiki/src/ingest/mod.rs:571-582] | Indexed function `asset_path_uses_basename_before_extension_extraction` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:571-582] |
| `markdown_metadata_quotes_yaml_sensitive_scalars` | function | `fn markdown_metadata_quotes_yaml_sensitive_scalars() {` | `markdown_metadata_quotes_yaml_sensitive_scalars [function]` | `bbcb8e0b-b32b-5b70-9d6f-62fad2888312` | 585-611 [crates/gwiki/src/ingest/mod.rs:585-611] | Indexed function `markdown_metadata_quotes_yaml_sensitive_scalars` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:585-611] |
| `markdown_metadata_allows_explicit_typed_values` | function | `fn markdown_metadata_allows_explicit_typed_values() {` | `markdown_metadata_allows_explicit_typed_values [function]` | `2b2cd1dc-d31d-5893-9b0f-79b01b728489` | 614-629 [crates/gwiki/src/ingest/mod.rs:614-629] | Indexed function `markdown_metadata_allows_explicit_typed_values` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:614-629] |
| `immutable_file_requires_declared_source_hash_before_copy` | function | `fn immutable_file_requires_declared_source_hash_before_copy() {` | `immutable_file_requires_declared_source_hash_before_copy [function]` | `f9e81cff-9d73-525f-ba41-c318f608c2da` | 632-649 [crates/gwiki/src/ingest/mod.rs:632-649] | Indexed function `immutable_file_requires_declared_source_hash_before_copy` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:632-649] |
| `immutable_file_existing_match_requires_declared_hash` | function | `fn immutable_file_existing_match_requires_declared_hash() {` | `immutable_file_existing_match_requires_declared_hash [function]` | `fd6a7cab-acba-5a80-863e-24db7e20126c` | 652-701 [crates/gwiki/src/ingest/mod.rs:652-701] | Indexed function `immutable_file_existing_match_requires_declared_hash` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:652-701] |
| `ingest_indexes_raw_without_wiki_rewrite` | function | `fn ingest_indexes_raw_without_wiki_rewrite() {` | `ingest_indexes_raw_without_wiki_rewrite [function]` | `05abd631-6048-5eec-be8d-696b65ef6337` | 704-750 [crates/gwiki/src/ingest/mod.rs:704-750] | Indexed function `ingest_indexes_raw_without_wiki_rewrite` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:704-750] |
| `RawFirstStore` | class | `struct RawFirstStore {` | `RawFirstStore [class]` | `15cef8c4-3c02-5ec3-8c9e-ed97e3610f08` | 753-758 [crates/gwiki/src/ingest/mod.rs:753-758] | Indexed class `RawFirstStore` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:753-758] |
| `RawFirstStore::new` | method | `fn new(vault_root: &Path, expected_raw_path: impl Into<PathBuf>) -> Self {` | `RawFirstStore::new [method]` | `aff3e655-56c2-5b3a-85db-1b57e1b76fa9` | 761-768 [crates/gwiki/src/ingest/mod.rs:761-768] | Indexed method `RawFirstStore::new` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:761-768] |
| `RawFirstStore::assert_raw_exists_before_index` | method | `fn assert_raw_exists_before_index(&mut self) {` | `RawFirstStore::assert_raw_exists_before_index [method]` | `5bf701ac-bbc8-502d-b665-5455e68745de` | 770-776 [crates/gwiki/src/ingest/mod.rs:770-776] | Indexed method `RawFirstStore::assert_raw_exists_before_index` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:770-776] |
| `RawFirstStore::indexed_hashes` | method | `fn indexed_hashes(` | `RawFirstStore::indexed_hashes [method]` | `93cad582-09c8-5278-9d32-b1a37e3d0657` | 780-784 [crates/gwiki/src/ingest/mod.rs:780-784] | Indexed method `RawFirstStore::indexed_hashes` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:780-784] |
| `RawFirstStore::upsert_document` | method | `fn upsert_document(&mut self, document: WikiDocument) -> Result<(), StoreError> {` | `RawFirstStore::upsert_document [method]` | `f478d8fe-c22a-5217-b605-a118a14bb1ed` | 786-789 [crates/gwiki/src/ingest/mod.rs:786-789] | Indexed method `RawFirstStore::upsert_document` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:786-789] |
| `RawFirstStore::replace_chunks` | method | `fn replace_chunks(` | `RawFirstStore::replace_chunks [method]` | `cc3d588d-7ffa-594d-98e8-fdfbb3170166` | 791-798 [crates/gwiki/src/ingest/mod.rs:791-798] | Indexed method `RawFirstStore::replace_chunks` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:791-798] |
| `RawFirstStore::replace_links` | method | `fn replace_links(&mut self, path: &Path, links: Vec<WikiLink>) -> Result<(), StoreError> {` | `RawFirstStore::replace_links [method]` | `0b05c0e9-7fd6-5c7c-9a5f-b850d0d2bc38` | 800-803 [crates/gwiki/src/ingest/mod.rs:800-803] | Indexed method `RawFirstStore::replace_links` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:800-803] |
| `RawFirstStore::upsert_source` | method | `fn upsert_source(&mut self, source: WikiSource) -> Result<(), StoreError> {` | `RawFirstStore::upsert_source [method]` | `be196e3c-75ef-5c74-acc7-9976a1812af0` | 805-808 [crates/gwiki/src/ingest/mod.rs:805-808] | Indexed method `RawFirstStore::upsert_source` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:805-808] |
| `RawFirstStore::record_ingestion` | method | `fn record_ingestion(&mut self, ingestion: WikiIngestion) -> Result<(), StoreError> {` | `RawFirstStore::record_ingestion [method]` | `b96ab963-ecb0-56cb-bd65-d7dc44c5e6d7` | 810-813 [crates/gwiki/src/ingest/mod.rs:810-813] | Indexed method `RawFirstStore::record_ingestion` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:810-813] |
| `RawFirstStore::record_file_hash` | method | `fn record_file_hash(` | `RawFirstStore::record_file_hash [method]` | `7dc7572c-92c3-547e-86f5-59f2ab70661c` | 815-822 [crates/gwiki/src/ingest/mod.rs:815-822] | Indexed method `RawFirstStore::record_file_hash` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:815-822] |
| `RawFirstStore::delete_derived_rows` | method | `fn delete_derived_rows(&mut self, path: &Path) -> Result<(), StoreError> {` | `RawFirstStore::delete_derived_rows [method]` | `c605b7bd-7619-5de7-8a53-cf28994a65cf` | 824-827 [crates/gwiki/src/ingest/mod.rs:824-827] | Indexed method `RawFirstStore::delete_derived_rows` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:824-827] |
| `external_connectors_write_raw_first` | function | `fn external_connectors_write_raw_first() {` | `external_connectors_write_raw_first [function]` | `0bf88760-9345-57cb-9545-a1f5494c23a1` | 831-864 [crates/gwiki/src/ingest/mod.rs:831-864] | Indexed function `external_connectors_write_raw_first` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:831-864] |
