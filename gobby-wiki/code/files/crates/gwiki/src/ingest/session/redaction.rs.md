---
title: crates/gwiki/src/ingest/session/redaction.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/redaction.rs
  ranges:
  - 5-7
  - 9-15
  - 17-23
  - 25-33
  - 35-41
  - 54-70
  - 73-126
  - 128-145
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/redaction.rs:5-7](crates/gwiki/src/ingest/session/redaction.rs#L5-L7), [crates/gwiki/src/ingest/session/redaction.rs:9-15](crates/gwiki/src/ingest/session/redaction.rs#L9-L15), [crates/gwiki/src/ingest/session/redaction.rs:17-23](crates/gwiki/src/ingest/session/redaction.rs#L17-L23), [crates/gwiki/src/ingest/session/redaction.rs:25-33](crates/gwiki/src/ingest/session/redaction.rs#L25-L33), [crates/gwiki/src/ingest/session/redaction.rs:35-41](crates/gwiki/src/ingest/session/redaction.rs#L35-L41), [crates/gwiki/src/ingest/session/redaction.rs:54-70](crates/gwiki/src/ingest/session/redaction.rs#L54-L70), [crates/gwiki/src/ingest/session/redaction.rs:73-126](crates/gwiki/src/ingest/session/redaction.rs#L73-L126), [crates/gwiki/src/ingest/session/redaction.rs:128-145](crates/gwiki/src/ingest/session/redaction.rs#L128-L145)

</details>

# crates/gwiki/src/ingest/session/redaction.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the session redaction layer used during ingest: `redact_session_markdown` delegates to `redact_session_text`, which applies a sequence of regex-based replacements to scrub home-directory paths, common API key/token formats, and email addresses with fixed `[REDACTED_*]` markers. The regex builders are cached with `OnceLock` so the patterns are compiled once and reused. The test module exercises the redaction rules and verifies that session ingest writes redacted markdown into the indexed store rather than leaking secrets.
[crates/gwiki/src/ingest/session/redaction.rs:5-7]
[crates/gwiki/src/ingest/session/redaction.rs:9-15]
[crates/gwiki/src/ingest/session/redaction.rs:17-23]
[crates/gwiki/src/ingest/session/redaction.rs:25-33]
[crates/gwiki/src/ingest/session/redaction.rs:35-41]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `redact_session_markdown` | function | `pub(crate) fn redact_session_markdown(markdown: &str) -> String {` | `redact_session_markdown [function]` | `394dfb04-8d1f-5615-871f-a670ef543c1e` | 5-7 [crates/gwiki/src/ingest/session/redaction.rs:5-7] | Indexed function `redact_session_markdown` in `crates/gwiki/src/ingest/session/redaction.rs`. [crates/gwiki/src/ingest/session/redaction.rs:5-7] |
| `redact_session_text` | function | `pub(crate) fn redact_session_text(text: &str) -> String {` | `redact_session_text [function]` | `d0a0b9ae-8113-5625-b364-791d2e421ce6` | 9-15 [crates/gwiki/src/ingest/session/redaction.rs:9-15] | Indexed function `redact_session_text` in `crates/gwiki/src/ingest/session/redaction.rs`. [crates/gwiki/src/ingest/session/redaction.rs:9-15] |
| `home_dir_regex` | function | `fn home_dir_regex() -> &'static Regex {` | `home_dir_regex [function]` | `7867d44e-677e-5f25-824e-e626f4b5f289` | 17-23 [crates/gwiki/src/ingest/session/redaction.rs:17-23] | Indexed function `home_dir_regex` in `crates/gwiki/src/ingest/session/redaction.rs`. [crates/gwiki/src/ingest/session/redaction.rs:17-23] |
| `api_key_regex` | function | `fn api_key_regex() -> &'static Regex {` | `api_key_regex [function]` | `1f34dc1a-b296-5a99-b234-ba6903f78385` | 25-33 [crates/gwiki/src/ingest/session/redaction.rs:25-33] | Indexed function `api_key_regex` in `crates/gwiki/src/ingest/session/redaction.rs`. [crates/gwiki/src/ingest/session/redaction.rs:25-33] |
| `email_regex` | function | `fn email_regex() -> &'static Regex {` | `email_regex [function]` | `c9e82f14-9f8c-5b87-8889-a2c191839280` | 35-41 [crates/gwiki/src/ingest/session/redaction.rs:35-41] | Indexed function `email_regex` in `crates/gwiki/src/ingest/session/redaction.rs`. [crates/gwiki/src/ingest/session/redaction.rs:35-41] |
| `redacts_session_secret_patterns` | function | `fn redacts_session_secret_patterns() {` | `redacts_session_secret_patterns [function]` | `2d95fecf-b063-57e7-9d33-dedf787219be` | 54-70 [crates/gwiki/src/ingest/session/redaction.rs:54-70] | Indexed function `redacts_session_secret_patterns` in `crates/gwiki/src/ingest/session/redaction.rs`. [crates/gwiki/src/ingest/session/redaction.rs:54-70] |
| `session_ingest_writes_redacted_markdown` | function | `fn session_ingest_writes_redacted_markdown() {` | `session_ingest_writes_redacted_markdown [function]` | `b0ba8499-9fc7-5d39-a509-680e4d2302fa` | 73-126 [crates/gwiki/src/ingest/session/redaction.rs:73-126] | Indexed function `session_ingest_writes_redacted_markdown` in `crates/gwiki/src/ingest/session/redaction.rs`. [crates/gwiki/src/ingest/session/redaction.rs:73-126] |
| `indexed_store_text` | function | `fn indexed_store_text(store: &MemoryWikiStore) -> String {` | `indexed_store_text [function]` | `2d3b8498-a78f-5011-9a3a-3ad10a8e50ac` | 128-145 [crates/gwiki/src/ingest/session/redaction.rs:128-145] | Indexed function `indexed_store_text` in `crates/gwiki/src/ingest/session/redaction.rs`. [crates/gwiki/src/ingest/session/redaction.rs:128-145] |
