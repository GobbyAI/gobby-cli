---
title: crates/gwiki/src/ingest/wayback.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/wayback.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/wayback.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/wayback.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/wayback.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WaybackCaptureSnapshot` | class | The 'WaybackCaptureSnapshot' struct represents a retrieved Wayback Machine capture, storing metadata such as the original and capture URLs, timestamps, content type, and the raw binary payload of the captured page. [crates/gwiki/src/ingest/wayback.rs:18-25] |
| `ingest_capture` | function | The 'ingest_capture' function decodes and parses HTML from a 'WaybackCaptureSnapshot', registers a corresponding 'SourceManifest' within a vault root using a constructed 'SourceDraft', and then renders, writes, and indexes the Markdown representation into a 'WikiIndexStore'. [crates/gwiki/src/ingest/wayback.rs:28-47] |
| `decode_wayback_html` | function | The 'decode_wayback_html' function validates the content type of a 'WaybackCaptureSnapshot', decodes its raw body bytes into an HTML string, and verifies that the decoded string resembles a valid HTML document, returning a 'WikiError' if any validation or decoding step fails. [crates/gwiki/src/ingest/wayback.rs:50-60] |
| `ensure_html_content_type` | function | This function validates that the extracted media type from an optional content-type string is either 'text/html' or 'application/xhtml+xml', returning 'Ok(())' on success or a 'WikiError::InvalidInput' if the media type is unsupported or absent. [crates/gwiki/src/ingest/wayback.rs:63-75] |
| `decode_html_bytes` | function | This function decodes a byte slice of HTML into a UTF-8 String by sequentially attempting to detect the character encoding from an optional Content-Type header, a byte order mark (BOM), or HTML meta tags, defaulting to UTF-8 if no encoding is successfully matched. [crates/gwiki/src/ingest/wayback.rs:78-98] |
| `content_type_media_type` | function | The 'content_type_media_type' function extracts the primary media type from an optional 'Content-Type' header string by isolating the substring prior to the first semicolon, trimming leading and trailing whitespace, converting it to ASCII lowercase, and returning it as an optional owned string. [crates/gwiki/src/ingest/wayback.rs:101-108] |
| `charset_from_content_type` | function | This function extracts and returns the trimmed, non-empty value of the first case-insensitive 'charset' parameter from an optional 'Content-Type' header string by parsing its semicolon-separated key-value pairs. [crates/gwiki/src/ingest/wayback.rs:111-118] |
| `charset_from_html_meta` | function | The 'charset_from_html_meta' function decodes up to the first 4096 bytes of a byte slice into a lossy UTF-8 string and extracts the character encoding name from a 'charset' attribute using a case-insensitive regular expression, returning it as an 'Option<String>'. [crates/gwiki/src/ingest/wayback.rs:121-129] |
| `trim_charset_label` | function | The 'trim_charset_label' function strips leading and trailing whitespace and surrounding single or double quotes from a string slice, returning the cleaned value as an owned 'String'. [crates/gwiki/src/ingest/wayback.rs:132-139] |
| `html_looks_like_document` | function | This function determines whether a string slice contains a complete HTML document by trimming leading whitespace, converting it to ASCII lowercase, and checking if it starts with '<!doctype html' or '<html', or contains '<body'. [crates/gwiki/src/ingest/wayback.rs:142-145] |
| `wayback_title` | function | This function determines a fallback-ordered title for a snapshot by attempting to extract the HTML document title, parsing a title from the original URL's path, formatting the URL's host as a Markdown title, or ultimately formatting the full original URL as a Markdown title. [crates/gwiki/src/ingest/wayback.rs:148-153] |
| `html_title` | function | The 'html_title' function extracts the text of the first '<title>' element in an HTML document, normalizes and formats it as a single-line markdown title, and returns it as an 'Option<String>' if the resulting string is non-empty. [crates/gwiki/src/ingest/wayback.rs:156-163] |
| `title_from_url_path` | function | The function parses a URL, extracts and percent-decodes its last non-empty path segment, and returns a formatted markdown title wrapped in 'Some(String)' if it is not empty, or 'None' otherwise. [crates/gwiki/src/ingest/wayback.rs:166-171] |
| `url_host` | function | The 'url_host' function parses a URL string slice and returns its host name as an owned 'String' wrapped in 'Some' if the URL is valid and has a non-empty host, otherwise returning 'None'. [crates/gwiki/src/ingest/wayback.rs:174-180] |
| `percent_decode_lossy` | function | Decodes a percent-encoded string slice into its raw bytes and then performs a lossy UTF-8 decoding to return an owned 'String' where invalid sequences are replaced with the Unicode replacement character. [crates/gwiki/src/ingest/wayback.rs:183-185] |
| `render_wayback_markdown` | function | This function generates a Markdown string containing metadata frontmatter extracted from a 'WaybackCaptureSnapshot' and a source hash, followed by a specified title header and the plain text representation of a parsed 'Html' document. [crates/gwiki/src/ingest/wayback.rs:188-215] |
| `html_to_text` | function | The 'html_to_text' function extracts text from an HTML document reference, transforms each line using a 'single_line' utility, removes empty lines, and concatenates the remaining non-empty lines using a double-newline separator. [crates/gwiki/src/ingest/wayback.rs:218-226] |
| `extract_html_text` | function | The 'extract_html_text' function extracts visible text from an 'Html' document by traversing the first 'body' element if found, or falling back to the root element, and joins the gathered text segments with newlines. [crates/gwiki/src/ingest/wayback.rs:229-238] |
| `collect_visible_text` | function | This function recursively traverses an HTML element tree to extract and aggregate visible text into a vector of strings, ignoring metadata and scripting elements while segmenting the output at block-level boundaries and '<br>' line breaks. [crates/gwiki/src/ingest/wayback.rs:241-266] |
| `collect_inline_text` | function | This function recursively traverses the child nodes of a given HTML element to accumulate visible text, appending text nodes to an inline buffer and flushing completed segments to a parts vector upon encountering '<br>' or block-boundary elements, while completely ignoring '<head>', '<script>', and '<style>' tags. [crates/gwiki/src/ingest/wayback.rs:269-292] |
| `append_inline_text` | function | Converts the input string slice to a single-line representation and, if non-empty, appends it to a mutable string buffer, prepending a space if the buffer is not already empty. [crates/gwiki/src/ingest/wayback.rs:295-304] |
| `push_text_part` | function | The 'push_text_part' function converts the mutable 'inline' string buffer into a single-line string, clears the buffer, and appends the resulting string to the 'parts' vector if it is not empty. [crates/gwiki/src/ingest/wayback.rs:307-313] |
| `is_block_boundary` | function | The 'is_block_boundary' function returns a boolean indicating whether the provided string slice matches any of a predefined set of block-level HTML element tag names. [crates/gwiki/src/ingest/wayback.rs:316-352] |
| `document_for` | function | The 'document_for' function decodes a byte slice into an HTML string under the assumption of a 'text/html' MIME type and parses the resulting string into an 'Html' document. [crates/gwiki/src/ingest/wayback.rs:513-516] |

_Verified by 7 in-file unit tests._

