---
title: crates/gwiki/src/ingest/document/html.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/document/html.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/document/html.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/document/html.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/document/html.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `extract_html_document` | function | This function parses raw bytes into a lossy UTF-8 HTML document, extracts its title and visible body text to generate normalized Markdown, and returns a 'DocumentExtraction' struct indicating either a successful extraction or a no-content degradation state. [crates/gwiki/src/ingest/document/html.rs:8-39] |
| `extract_html_title` | function | This function extracts the text of the first '<title>' element from the provided HTML document, decodes XML entities, formats the content, and returns the non-empty result as 'Some(String)' or 'None'. [crates/gwiki/src/ingest/document/html.rs:41-51] |
| `collect_visible_text` | function | This function recursively traverses an HTML element tree to extract visible text into a vector of strings, segmenting the text at block-level element boundaries while coalescing adjacent inline text nodes and inline child elements. [crates/gwiki/src/ingest/document/html.rs:53-76] |
| `collect_inline_text` | function | This function recursively extracts and concatenates all text content from the given HTML element and its descendant nodes, skipping content inside 'head', 'script', and 'style' elements. [crates/gwiki/src/ingest/document/html.rs:78-96] |
| `append_inline_text` | function | The 'append_inline_text' function appends a trimmed, non-empty string slice to a mutable string buffer, conditionally prepending a space separator if the buffer is not empty, does not end with whitespace, and the trimmed input does not begin with closing punctuation. [crates/gwiki/src/ingest/document/html.rs:98-110] |
| `starts_with_closing_punctuation` | function | The function returns 'true' if the input string slice starts with a character matching a predefined set of closing punctuation, brackets, quotes, and sentence-ending marks, and 'false' if the string is empty or starts with any other character. [crates/gwiki/src/ingest/document/html.rs:112-140] |
| `push_visible_part` | function | The function 'push_visible_part' extracts a single-line representation from a mutable string buffer, appends it to a vector of strings if it is not empty, and subsequently clears the original buffer. [crates/gwiki/src/ingest/document/html.rs:142-148] |
| `is_block_element` | function | The 'is_block_element' function checks if a given string slice matches a predefined list of HTML block-level, layout, list, or table element tag names, returning 'true' if a match is found and 'false' otherwise. [crates/gwiki/src/ingest/document/html.rs:150-199] |
| `normalize_markdown_text` | function | This function decodes XML entities and normalizes Unicode whitespace in the input string, then splits it into lines, processes each line, filters out empty lines, deduplicates consecutive identical lines, and finally joins them with double newlines. [crates/gwiki/src/ingest/document/html.rs:201-213] |
| `normalize_unicode_whitespace` | function | The 'normalize_unicode_whitespace' function iterates over the characters of a string slice to return a new 'String' where line breaks, carriage returns, line separators, and paragraph separators are normalized to standard line feeds ('\n'), all other Unicode whitespace characters are normalized to standard spaces (' '), and non-whitespace characters remain unchanged. [crates/gwiki/src/ingest/document/html.rs:215-223] |

_Verified by 2 in-file unit tests._

