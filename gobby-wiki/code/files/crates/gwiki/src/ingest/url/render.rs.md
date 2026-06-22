---
title: crates/gwiki/src/ingest/url/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/url/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/url/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/url/render.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/url/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_url_markdown` | function | The 'render_url_markdown' function generates a Markdown-formatted string by combining serialized metadata from a 'UrlSnapshot' with a structured document title header and the converted markdown-like text content of an HTML document. [crates/gwiki/src/ingest/url/render.rs:12-37] |
| `render_non_html_url_markdown` | function | This function constructs and returns a Markdown string containing structured metadata fields, a formatted header title, and a preservation notice for a non-HTML URL response snapshot. [crates/gwiki/src/ingest/url/render.rs:39-66] |
| `snapshot_is_html` | function | This function determines if a URL snapshot represents HTML by matching its content-type media type against 'text/html' or 'application/xhtml+xml', falling back to heuristic body analysis if no content-type is present. [crates/gwiki/src/ingest/url/render.rs:68-74] |
| `source_kind_for_url_response` | function | This function maps an optional HTTP 'Content-Type' header value to a corresponding 'SourceKind' enum variant by extracting and matching the media type against known PDF, image, audio, video, and text patterns, defaulting to 'SourceKind::File'. [crates/gwiki/src/ingest/url/render.rs:76-88] |
| `content_type_media_type` | function | This function extracts the primary media type from an optional HTTP 'Content-Type' header string slice by retrieving the trimmed, lowercase portion preceding any semicolon-delimited parameter, returning it as an 'Option<String>' if it is not empty. [crates/gwiki/src/ingest/url/render.rs:90-97] |
| `body_looks_like_html` | function | The function determines if a byte slice represents HTML by converting up to its first 512 bytes into a lossy, lowercase UTF-8 string and checking if, after trimming leading whitespace, it starts with '<!doctype html' or '<html', or contains '<body'. [crates/gwiki/src/ingest/url/render.rs:99-105] |
| `file_name_for_url_response` | function | This function extracts the last path segment of the URL in a 'UrlSnapshot' to determine a filename, falling back to a default name mapped from the 'SourceKind' if the URL is invalid or lacks a valid final path segment. [crates/gwiki/src/ingest/url/render.rs:107-123] |
| `extract_title` | function | The 'extract_title' function selects the first '<title>' element from an HTML document, extracts and joins its text contents into a single-line string, and returns it as 'Some(String)' if the resulting string is non-empty, or 'None' otherwise. [crates/gwiki/src/ingest/url/render.rs:125-135] |
| `html_to_markdownish_text` | function | The 'html_to_markdownish_text' function extracts visible text from an HTML document's body element (or root element if absent), joins the collected text components with newlines, and returns a normalized markdown-like string. [crates/gwiki/src/ingest/url/render.rs:137-146] |
| `collect_visible_text` | function | This function recursively traverses an element's DOM tree, extracting and appending visible inline and block text segments to a mutable vector while ignoring hidden elements and preserving block-level structural boundaries. [crates/gwiki/src/ingest/url/render.rs:148-182] |
| `collect_inline_text` | function | The 'collect_inline_text' function recursively traverses the non-hidden child nodes of a given element and appends all encountered text node contents to a mutable string buffer. [crates/gwiki/src/ingest/url/render.rs:184-199] |
| `push_inline_part` | function | The 'push_inline_part' function moves the contents of the mutable 'inline' string into the 'parts' vector (replacing 'inline' with an empty string) if its single-line representation is non-empty, and clears 'inline' otherwise. [crates/gwiki/src/ingest/url/render.rs:201-207] |
| `is_hidden_element` | function | The 'is_hidden_element' function determines if a given string slice matches "head", "script", or "style" and returns 'true' if it does, and 'false' otherwise. [crates/gwiki/src/ingest/url/render.rs:209-211] |
| `is_text_block` | function | The 'is_text_block' function evaluates whether a given string slice matches a predefined list of HTML block-level or structural text element tags, returning 'true' if a match is found and 'false' otherwise. [crates/gwiki/src/ingest/url/render.rs:213-233] |
| `normalize_markdown_text` | function | The 'normalize_markdown_text' function normalizes each line of the input text, filters out empty and consecutive duplicate lines, and joins the remaining lines with double newlines. [crates/gwiki/src/ingest/url/render.rs:235-244] |

