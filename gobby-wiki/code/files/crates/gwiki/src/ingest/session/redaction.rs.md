---
title: crates/gwiki/src/ingest/session/redaction.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/session/redaction.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/session/redaction.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/session/redaction.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/session/redaction.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `redact_session_markdown` | function | The function 'redact_session_markdown' takes a markdown string slice as input and returns a redacted 'String' by delegating its processing to 'redact_session_text'. [crates/gwiki/src/ingest/session/redaction.rs:5-7] |
| `redact_session_text` | function | The 'redact_session_text' function sanitizes a given string slice by using regular expressions to replace occurrences of home directory paths, API keys, and email addresses with standardized redaction placeholders, returning the modified text as a new 'String'. [crates/gwiki/src/ingest/session/redaction.rs:9-15] |
| `home_dir_regex` | function | The 'home_dir_regex' function lazily initializes and returns a static reference to a regular expression ('&'static Regex') designed to match macOS user home directory paths under '/Users/' for redaction. [crates/gwiki/src/ingest/session/redaction.rs:17-23] |
| `api_key_regex` | function | This function lazily compiles and returns a static reference to a thread-safe regular expression designed to detect common API keys and credential tokens (such as those for Stripe, Slack, GitHub, and Google Cloud) using 'OnceLock'. [crates/gwiki/src/ingest/session/redaction.rs:25-33] |
| `email_regex` | function | The 'email_regex' function lazily compiles and returns a static reference to a case-insensitive regular expression for matching email addresses, caching the result in a thread-safe 'OnceLock'. [crates/gwiki/src/ingest/session/redaction.rs:35-41] |
| `indexed_store_text` | function | The 'indexed_store_text' function serializes a 'MemoryWikiStore' into a single string by sequentially appending the optional titles and bodies of all documents, followed by the optional headings and contents of all stored chunks. [crates/gwiki/src/ingest/session/redaction.rs:128-145] |

_Verified by 2 in-file unit tests._

