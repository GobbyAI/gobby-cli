---
title: crates/gwiki/src/ingest/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/mod.rs` exposes 61 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IngestResult` | class | 'IngestResult' is a result container holding the ingested 'SourceRecord', the original 'raw_path', and an optional derived 'asset_path' for the processed asset. [crates/gwiki/src/ingest/mod.rs:29-33] |
| `lowercase_extension` | function | Returns the file extension of 'path' as a lowercase 'String', or 'None' if the path has no extension or its extension is not valid UTF-8. [crates/gwiki/src/ingest/mod.rs:35-40] |
| `write_raw_markdown` | function | Creates a 'raw/<record.id>.md' path, writes the provided markdown bytes immutably under 'vault_root' via 'write_immutable', and returns the relative 'PathBuf' on success. [crates/gwiki/src/ingest/mod.rs:42-50] |
| `write_asset` | function | Constructs an asset path from the source record and file name, writes the provided bytes immutably under 'vault_root' at that path, and returns the resulting 'PathBuf' on success. [crates/gwiki/src/ingest/mod.rs:52-61] |
| `write_asset_with_suffix` | function | Creates an immutable asset file under 'raw/assets' named '{record.id}.{sanitized_suffix}.{sanitized_extension}', writes the provided bytes to 'vault_root' at that path, and returns the relative 'PathBuf' or a 'WikiError' on failure. [crates/gwiki/src/ingest/mod.rs:63-77] |
| `write_asset_from_path` | function | Builds the asset path for the given record and file name, writes the source file there as an immutable file using the provided content hash, and returns the resulting 'PathBuf' on success. [crates/gwiki/src/ingest/mod.rs:79-89] |
| `sanitize_asset_suffix` | function | Converts 'value' into a lowercase-preserving asset suffix containing only ASCII alphanumerics and '_', collapsing runs of invalid characters into single '-', trimming trailing '-', and returning '"asset"' if the result is empty. [crates/gwiki/src/ingest/mod.rs:91-111] |
| `index_after_ingest` | function | Calls 'indexer::index_vault' on the given 'vault_root' and 'store', converting any indexing error into 'WikiError::InvalidInput' with field '"index"'. [crates/gwiki/src/ingest/mod.rs:113-121] |
| `write_raw_then_index` | function | Writes the raw markdown for a source record under 'vault_root', reindexes the wiki store afterward, and returns an 'IngestResult' containing the original record, the written raw path, and any optional asset path. [crates/gwiki/src/ingest/mod.rs:124-139] |
| `markdown_metadata` | function | Converts a slice of '(key, String)' pairs into 'MetadataValue::string' entries and delegates to 'markdown_metadata_values' to render the metadata as a 'String'. [crates/gwiki/src/ingest/mod.rs:141-147] |
| `MetadataValue` | type | Indexed type `MetadataValue` in `crates/gwiki/src/ingest/mod.rs`. [crates/gwiki/src/ingest/mod.rs:150-155] |
| `MetadataValue::string` | method | Constructs and returns a 'Self::String' variant by converting the provided 'value' into a 'String'. [crates/gwiki/src/ingest/mod.rs:158-160] |
| `MetadataValue::number` | method | Constructs and returns 'Self::Number' by converting the provided 'value' to a 'String' with 'ToString::to_string()'. [crates/gwiki/src/ingest/mod.rs:162-164] |
| `MetadataValue::bool` | method | Constructs and returns a 'Self::Bool' enum variant initialized with the provided 'bool' value. [crates/gwiki/src/ingest/mod.rs:166-168] |
| `MetadataValue::json` | method | Serializes the given 'Serialize' value to a JSON string with 'serde_json::to_string', falling back to '"null"' on serialization failure, and wraps the result in 'Self::Json'. [crates/gwiki/src/ingest/mod.rs:170-172] |
| `markdown_metadata_values` | function | Builds and returns a YAML front-matter string by writing '---', then each '(key, value)' pair as 'key: <yaml-escaped value>' on its own line, and finally closing with '---' followed by a blank line. [crates/gwiki/src/ingest/mod.rs:175-185] |
| `yaml_metadata_value` | function | Converts a 'MetadataValue' into a YAML-compatible 'String', dispatching to string, numeric, boolean, or JSON formatting based on the enum variant. [crates/gwiki/src/ingest/mod.rs:187-194] |
| `yaml_metadata_scalar` | function | Returns a YAML-safe scalar for metadata values, quoting a normalized single-line string when 'key == "content_type"' and otherwise emitting 'value' as a safe single-line YAML scalar. [crates/gwiki/src/ingest/mod.rs:196-202] |
| `yaml_safe_single_line_scalar` | function | Normalizes the input to a single line and returns it unchanged if it is safe as a YAML plain scalar, otherwise returns a YAML-quoted string. [crates/gwiki/src/ingest/mod.rs:204-211] |
| `yaml_numeric_scalar` | function | Returns the input normalized to a single line and emits it unchanged if it is a YAML-safe numeric scalar, otherwise YAML-escapes it by quoting the string. [crates/gwiki/src/ingest/mod.rs:213-220] |
| `yaml_json_value` | function | Returns a single-line representation of 'value', leaving it unchanged if it parses as valid JSON and otherwise wrapping it as a quoted YAML string. [crates/gwiki/src/ingest/mod.rs:222-229] |
| `yaml_plain_scalar_is_safe` | function | Returns 'true' only for non-empty strings that are not YAML-reserved scalars or scalar-like values (booleans, null/NaN/Inf, integers, floats, timestamps) and do not contain YAML-breaking characters or patterns such as ':', ' #', quotes, or reserved leading punctuation. [crates/gwiki/src/ingest/mod.rs:231-251] |
| `yaml_numeric_scalar_is_safe` | function | Returns 'true' if 'value' parses as a valid 'i64' or as a finite 'f64', and 'false' otherwise. [crates/gwiki/src/ingest/mod.rs:253-255] |
| `yaml_plain_scalar_is_timestamp` | function | Returns 'true' when the input has a YAML date prefix and its 11th byte is either absent, 'T', 't', or a space, indicating a plain scalar timestamp form. [crates/gwiki/src/ingest/mod.rs:257-260] |

_30 more symbol(s) not shown — run `gcode outline crates/gwiki/src/ingest/mod.rs` for the full list._

_Verified by 7 in-file unit tests._

