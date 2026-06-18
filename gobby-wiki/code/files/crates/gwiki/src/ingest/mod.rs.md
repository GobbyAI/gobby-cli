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

`crates/gwiki/src/ingest/mod.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

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
| `has_yaml_date_prefix` | function | Returns 'true' only when 'bytes' is at least 10 bytes long and begins with an ASCII date prefix of the form 'YYYY-MM-DD' using four digits, a hyphen, two digits, a hyphen, and two digits. [crates/gwiki/src/ingest/mod.rs:262-269] |
| `quote_yaml_string` | function | Serializes the input string as a JSON string literal to produce a YAML-safe quoted string, falling back to '""' if serialization fails. [crates/gwiki/src/ingest/mod.rs:271-273] |
| `single_line` | function | Returns a new 'String' containing the input text with all whitespace collapsed to single spaces by splitting on whitespace and joining the tokens with '" "'. [crates/gwiki/src/ingest/mod.rs:275-277] |
| `markdown_title` | function | Returns a normalized one-line markdown title by collapsing 'value' to a single line, trimming leading and trailing '#' characters, and then trimming surrounding whitespace. [crates/gwiki/src/ingest/mod.rs:279-281] |
| `text_from_utf8_lossy` | function | Converts a byte slice to a 'String' using lossily decoded UTF-8, then normalizes Windows CRLF line endings to LF by replacing '"\r\n"' with '"\n"'. [crates/gwiki/src/ingest/mod.rs:283-285] |
| `path_to_string` | function | Converts a 'Path' to a UTF-8 string using lossy decoding and normalizes path separators by replacing բոլոր backslashes with forward slashes. [crates/gwiki/src/ingest/mod.rs:287-289] |
| `write_immutable` | function | 'write_immutable' ensures the target file under 'vault_root' contains 'bytes' by creating parent directories, atomically persisting a temp file with 'persist_noclobber' if absent, or validating that any preexisting file already matches the requested bytes, while mapping I/O failures to 'WikiError::Io'. [crates/gwiki/src/ingest/mod.rs:291-330] |
| `write_immutable_file` | function | Validates the source file hash, ensures the destination directory exists, then atomically writes 'source_path' into 'vault_root.join(relative)' via a temp file with 'noclobber' semantics, or verifies an existing file against the expected hash/relative path if the destination already exists. [crates/gwiki/src/ingest/mod.rs:332-382] |
| `validate_existing_raw_bytes` | function | Computes the content hash of the existing file at 'path' and returns 'Ok(())' only if it matches the hash of 'bytes', otherwise mapping hash I/O failures to 'WikiError::Io' and returning 'immutable_exists_error(relative)'. [crates/gwiki/src/ingest/mod.rs:384-399] |
| `validate_existing_raw_file` | function | Computes the current content hash of 'path' and returns 'Ok(())' only if it matches 'source_hash', otherwise mapping any I/O failure to 'WikiError::Io' or returning an immutable-exists error for 'relative'. [crates/gwiki/src/ingest/mod.rs:401-416] |
| `validate_source_file_hash` | function | Computes the hash of the file at 'source_path', returns it if it exactly matches 'content_hash', and otherwise returns a 'WikiError::InvalidInput' or maps hashing I/O failures to 'WikiError::Io'. [crates/gwiki/src/ingest/mod.rs:418-435] |
| `immutable_exists_error` | function | Constructs a 'WikiError::InvalidInput' for the 'raw_path' field with a message indicating that an immutable raw source already exists at the given 'relative' path. [crates/gwiki/src/ingest/mod.rs:437-445] |
| `create_raw_temp_file` | function | Creates a 'NamedTempFile' in 'path'’s parent directory with a hidden '.{filename}.tmp' name pattern, or returns a 'WikiError::Io' if the path has no valid parent or temp file creation fails. [crates/gwiki/src/ingest/mod.rs:447-474] |
| `asset_path` | function | Constructs a 'PathBuf' under 'raw/assets' named '{record.id}.{sanitized_extension_for_file_name(file_name)}'. [crates/gwiki/src/ingest/mod.rs:478-483] |
| `sanitized_extension_for_file_name` | function | Returns the sanitized file extension from the basename of 'file_name', falling back to '"bin"' if no valid, non-empty extension exists. [crates/gwiki/src/ingest/mod.rs:485-499] |
| `sanitize_extension` | function | Returns a new string containing only the ASCII alphanumeric characters from 'extension', converted to lowercase. [crates/gwiki/src/ingest/mod.rs:501-507] |
| `no_ai_context` | function | Constructs an 'AiContext' resolved from 'EnvOnlySource', then marks it with 'IngestFileOptions { no_ai: true, ..default() }' via 'apply_to_ai_context' before returning it. [crates/gwiki/src/ingest/mod.rs:534-543] |
| `write_file` | function | Joins 'relative' to 'root', creates any missing parent directories for the resulting path, and writes 'contents' to that file, panicking if directory creation or file write fails. [crates/gwiki/src/ingest/mod.rs:545-551] |
| `test_source_record` | function | Constructs and returns a 'SourceRecord' for a manually ingested PDF source with fixed IDs, file paths, timestamp, content hash, pending compile status, and all optional metadata unset. [crates/gwiki/src/ingest/mod.rs:553-568] |
| `asset_path_uses_basename_before_extension_extraction` | function | Verifies that 'asset_path' ignores directory components, lowercases the extracted extension when present, and falls back to '.bin' when the input path has no extension. [crates/gwiki/src/ingest/mod.rs:571-582] |
| `markdown_metadata_quotes_yaml_sensitive_scalars` | function | Verifies that 'markdown_metadata' emits YAML metadata with plain scalars where safe and double-quotes values that would otherwise be parsed ambiguously by YAML, such as colons, comments, booleans, null-like values, numbers, dates, timestamps, and MIME-like strings. [crates/gwiki/src/ingest/mod.rs:585-611] |
| `markdown_metadata_allows_explicit_typed_values` | function | Verifies that 'markdown_metadata_values' renders explicitly typed metadata correctly by emitting numeric, stringified unsafe numeric, boolean, and JSON values in markdown metadata output. [crates/gwiki/src/ingest/mod.rs:614-629] |
| `immutable_file_requires_declared_source_hash_before_copy` | function | Verifies that 'write_asset_from_path' rejects an immutable asset copy when the declared source hash is stale, returns 'invalid_input', and does not create the destination file. [crates/gwiki/src/ingest/mod.rs:632-649] |
| `immutable_file_existing_match_requires_declared_hash` | function | Verifies that writing an immutable asset is idempotent only when the existing file content matches the declared content hash, and that any hash mismatch or different source content is rejected with 'invalid_input'. [crates/gwiki/src/ingest/mod.rs:652-701] |
| `ingest_indexes_raw_without_wiki_rewrite` | function | Verifies that ingesting a raw source file with 'no_ai' enabled writes a new raw 'INDEX.md' ingestion record without rewriting an existing wiki page whose content hash is unchanged. [crates/gwiki/src/ingest/mod.rs:704-750] |
| `RawFirstStore` | class | 'RawFirstStore' is a wrapper struct that tracks a vault root, the expected raw content path, an in-memory wiki store, and a flag indicating whether an index write has been observed. [crates/gwiki/src/ingest/mod.rs:753-758] |
| `RawFirstStore::new` | method | Constructs a new instance by cloning 'vault_root' into 'self.vault_root', converting 'expected_raw_path' into a 'PathBuf', initializing 'inner' with 'MemoryWikiStore::default()', and setting 'observed_index_write' to 'false'. [crates/gwiki/src/ingest/mod.rs:761-768] |
| `RawFirstStore::assert_raw_exists_before_index` | method | Marks that an index write has been observed and asserts that the expected raw source file already exists at 'vault_root/expected_raw_path', enforcing that the external connector writes raw data before derived index rows. [crates/gwiki/src/ingest/mod.rs:770-776] |
| `RawFirstStore::indexed_hashes` | method | Returns the 'BTreeMap<PathBuf, String>' of indexed hashes by delegating to 'self.inner.indexed_hashes()', propagating any 'StoreError' from the inner store. [crates/gwiki/src/ingest/mod.rs:780-784] |
| `RawFirstStore::upsert_document` | method | Checks that the raw store exists before indexing, then delegates the 'WikiDocument' upsert to 'self.inner.upsert_document(document)'. [crates/gwiki/src/ingest/mod.rs:786-789] |
| `RawFirstStore::replace_chunks` | method | 'replace_chunks' asserts that the raw source already exists in the index, then delegates to 'self.inner.replace_chunks(path, chunks)' to replace the wiki chunks for the given 'Path', returning 'Result<(), StoreError>'. [crates/gwiki/src/ingest/mod.rs:791-798] |
| `RawFirstStore::replace_links` | method | Ensures the raw store exists before indexing, then delegates to 'self.inner.replace_links(path, links)' to replace the wiki links for the given path. [crates/gwiki/src/ingest/mod.rs:800-803] |
| `RawFirstStore::upsert_source` | method | Ensures raw data exists before indexing by calling 'assert_raw_exists_before_index()', then delegates the 'WikiSource' upsert to 'self.inner.upsert_source(source)' and returns its 'Result<(), StoreError>'. [crates/gwiki/src/ingest/mod.rs:805-808] |
| `RawFirstStore::record_ingestion` | method | Validates that raw data exists before indexing, then delegates the 'WikiIngestion' record to the inner store implementation and returns its 'Result<(), StoreError>'. [crates/gwiki/src/ingest/mod.rs:810-813] |
| `RawFirstStore::record_file_hash` | method | Asserts that the raw store exists before indexing, then forwards the given 'path' and 'content_hash' to 'inner.record_file_hash' and returns its 'Result<(), StoreError>'. [crates/gwiki/src/ingest/mod.rs:815-822] |
| `RawFirstStore::delete_derived_rows` | method | Asserts that the raw data exists before indexing, then delegates to 'self.inner.delete_derived_rows(path)' to delete derived rows for the given 'path' and returns its 'Result<(), StoreError>'. [crates/gwiki/src/ingest/mod.rs:824-827] |
| `external_connectors_write_raw_first` | function | Verifies that ingesting a Wayback snapshot through 'wayback::ingest_capture' causes 'RawFirstStore' to perform an index write, confirming the raw-first external connector ingestion path. [crates/gwiki/src/ingest/mod.rs:831-864] |

