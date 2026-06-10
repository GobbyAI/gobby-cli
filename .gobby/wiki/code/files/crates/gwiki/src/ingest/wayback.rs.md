---
title: crates/gwiki/src/ingest/wayback.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/wayback.rs
  ranges:
  - 17-24
  - 26-45
  - 47-57
  - 59-71
  - 73-93
  - 95-102
  - 104-111
  - 113-121
  - 123-130
  - 132-135
  - 137-142
  - 144-151
  - 153-158
  - 160-166
  - 168-170
  - 172-199
  - 201-209
  - 211-220
  - 222-247
  - 249-272
  - 274-283
  - 285-291
  - 293-329
  - 338-377
  - 380-390
  - 393-407
  - 410-442
  - 445-452
  - 455-468
  - 471-488
  - 490-493
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/wayback.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

`crates/gwiki/src/ingest/wayback.rs` exposes 31 indexed API symbols.
[crates/gwiki/src/ingest/wayback.rs:17-24]
[crates/gwiki/src/ingest/wayback.rs:26-45]
[crates/gwiki/src/ingest/wayback.rs:47-57]
[crates/gwiki/src/ingest/wayback.rs:59-71]
[crates/gwiki/src/ingest/wayback.rs:73-93]
[crates/gwiki/src/ingest/wayback.rs:95-102]
[crates/gwiki/src/ingest/wayback.rs:104-111]
[crates/gwiki/src/ingest/wayback.rs:113-121]
[crates/gwiki/src/ingest/wayback.rs:123-130]
[crates/gwiki/src/ingest/wayback.rs:132-135]
[crates/gwiki/src/ingest/wayback.rs:137-142]
[crates/gwiki/src/ingest/wayback.rs:144-151]
[crates/gwiki/src/ingest/wayback.rs:153-158]
[crates/gwiki/src/ingest/wayback.rs:160-166]
[crates/gwiki/src/ingest/wayback.rs:168-170]
[crates/gwiki/src/ingest/wayback.rs:172-199]
[crates/gwiki/src/ingest/wayback.rs:201-209]
[crates/gwiki/src/ingest/wayback.rs:211-220]
[crates/gwiki/src/ingest/wayback.rs:222-247]
[crates/gwiki/src/ingest/wayback.rs:249-272]
[crates/gwiki/src/ingest/wayback.rs:274-283]
[crates/gwiki/src/ingest/wayback.rs:285-291]
[crates/gwiki/src/ingest/wayback.rs:293-329]
[crates/gwiki/src/ingest/wayback.rs:338-377]
[crates/gwiki/src/ingest/wayback.rs:380-390]
[crates/gwiki/src/ingest/wayback.rs:393-407]
[crates/gwiki/src/ingest/wayback.rs:410-442]
[crates/gwiki/src/ingest/wayback.rs:445-452]
[crates/gwiki/src/ingest/wayback.rs:455-468]
[crates/gwiki/src/ingest/wayback.rs:471-488]
[crates/gwiki/src/ingest/wayback.rs:490-493]

## API Symbols

- `WaybackCaptureSnapshot` (class) component `WaybackCaptureSnapshot [class]` (`3782102d-0baa-5894-8b1b-3daa71b7f6b0`) lines 17-24 [crates/gwiki/src/ingest/wayback.rs:17-24]
  - Signature: `pub struct WaybackCaptureSnapshot {`
  - Purpose: `WaybackCaptureSnapshot` is a struct that encapsulates an archived webpage snapshot from the Wayback Machine, containing the original and capture URLs, capture and fetch timestamps, the raw response body as bytes, and an optional content type. [crates/gwiki/src/ingest/wayback.rs:17-24]
- `ingest_capture` (function) component `ingest_capture [function]` (`7bedf6d3-f4c2-54cb-b16a-40fe72a24db4`) lines 26-45 [crates/gwiki/src/ingest/wayback.rs:26-45]
  - Signature: `pub fn ingest_capture(`
  - Purpose: Ingests a Wayback Machine capture snapshot by extracting metadata from its HTML, generating a markdown source record, registering the source manifest, and indexing the content to the vault. [crates/gwiki/src/ingest/wayback.rs:26-45]
- `decode_wayback_html` (function) component `decode_wayback_html [function]` (`1a0c6739-ffc5-5cb8-8e44-7b50bc049e41`) lines 47-57 [crates/gwiki/src/ingest/wayback.rs:47-57]
  - Signature: `fn decode_wayback_html(snapshot: &WaybackCaptureSnapshot) -> Result<String, WikiError> {`
  - Purpose: Decodes the body of a Wayback snapshot as HTML after validating the content type and verifying the decoded output is a well-formed HTML document. [crates/gwiki/src/ingest/wayback.rs:47-57]
- `ensure_html_content_type` (function) component `ensure_html_content_type [function]` (`7daa664d-e27a-5b9c-9e9c-8372e21a2040`) lines 59-71 [crates/gwiki/src/ingest/wayback.rs:59-71]
  - Signature: `fn ensure_html_content_type(content_type: Option<&str>) -> Result<(), WikiError> {`
  - Purpose: Validates that an optional content type is one of the HTML/XHTML media types (text/html or application/xhtml+xml), returning a WikiError if absent or incompatible. [crates/gwiki/src/ingest/wayback.rs:59-71]
- `decode_html_bytes` (function) component `decode_html_bytes [function]` (`403108d7-6074-5fa0-ad83-1df02e033e1b`) lines 73-93 [crates/gwiki/src/ingest/wayback.rs:73-93]
  - Signature: `fn decode_html_bytes(bytes: &[u8], content_type: Option<&str>) -> String {`
  - Purpose: Decodes bytes to a String by attempting charset detection via Content-Type header, byte-order mark, HTML meta charset declaration, and defaulting to UTF-8. [crates/gwiki/src/ingest/wayback.rs:73-93]
- `content_type_media_type` (function) component `content_type_media_type [function]` (`74f527a3-5555-5ef3-b917-cb7873c6a559`) lines 95-102 [crates/gwiki/src/ingest/wayback.rs:95-102]
  - Signature: `fn content_type_media_type(content_type: Option<&str>) -> Option<String> {`
  - Purpose: Extracts the media type component from a content-type header string by parsing the first semicolon-delimited segment, trimming whitespace, and converting to lowercase. [crates/gwiki/src/ingest/wayback.rs:95-102]
- `charset_from_content_type` (function) component `charset_from_content_type [function]` (`c9aed3dc-9f54-5373-9103-cd4ffe772b49`) lines 104-111 [crates/gwiki/src/ingest/wayback.rs:104-111]
  - Signature: `fn charset_from_content_type(content_type: Option<&str>) -> Option<String> {`
  - Purpose: Extracts the charset parameter value from a Content-Type header string by splitting on delimiters and performing case-insensitive matching, returning the trimmed result or None if absent or empty. [crates/gwiki/src/ingest/wayback.rs:104-111]
- `charset_from_html_meta` (function) component `charset_from_html_meta [function]` (`715a3f8f-d104-5ce3-bfa5-f5ac691c0965`) lines 113-121 [crates/gwiki/src/ingest/wayback.rs:113-121]
  - Signature: `fn charset_from_html_meta(bytes: &[u8]) -> Option<String> {`
  - Purpose: Extracts the charset value from an HTML meta declaration by scanning the first 4096 bytes with a case-insensitive regex pattern. [crates/gwiki/src/ingest/wayback.rs:113-121]
- `trim_charset_label` (function) component `trim_charset_label [function]` (`b5fd7f8d-ee49-542c-9c9e-682380ebf331`) lines 123-130 [crates/gwiki/src/ingest/wayback.rs:123-130]
  - Signature: `fn trim_charset_label(value: &str) -> String {`
  - Purpose: Strips leading and trailing whitespace and both single and double quotation marks from the input string, returning an owned `String`. [crates/gwiki/src/ingest/wayback.rs:123-130]
- `html_looks_like_document` (function) component `html_looks_like_document [function]` (`36676641-fc5d-5776-8999-e849e83bdad5`) lines 132-135 [crates/gwiki/src/ingest/wayback.rs:132-135]
  - Signature: `fn html_looks_like_document(html: &str) -> bool {`
  - Purpose: Returns true if the trimmed and lowercased HTML string begins with a DOCTYPE or html tag, or contains a body tag—indicating it's likely a complete document rather than a fragment. [crates/gwiki/src/ingest/wayback.rs:132-135]
- `wayback_title` (function) component `wayback_title [function]` (`1a6b76cc-4bec-5e59-aeb7-00eeef1e7ccb`) lines 137-142 [crates/gwiki/src/ingest/wayback.rs:137-142]
  - Signature: `fn wayback_title(snapshot: &WaybackCaptureSnapshot, document: &Html) -> String {`
  - Purpose: Extracts a title for a Wayback Machine snapshot using cascading fallbacks: HTML document title, URL path-derived title, domain hostname, or the full original URL as a last resort. [crates/gwiki/src/ingest/wayback.rs:137-142]
- `html_title` (function) component `html_title [function]` (`203ac21e-97cf-5111-a227-608d8f6130a7`) lines 144-151 [crates/gwiki/src/ingest/wayback.rs:144-151]
  - Signature: `fn html_title(document: &Html) -> Option<String> {`
  - Purpose: Extracts the first HTML title element, collapses its text content to a single line, applies markdown title formatting, and returns the non-empty result as an `Option<String>`. [crates/gwiki/src/ingest/wayback.rs:144-151]
- `title_from_url_path` (function) component `title_from_url_path [function]` (`93a16b8e-a800-52c1-b397-28d5339886d2`) lines 153-158 [crates/gwiki/src/ingest/wayback.rs:153-158]
  - Signature: `fn title_from_url_path(url: &str) -> Option<String> {`
  - Purpose: This function extracts the rightmost non-empty path segment from a URL, percent-decodes it, formats it as a markdown title, and returns `Some(title)` if non-empty or `None` otherwise. [crates/gwiki/src/ingest/wayback.rs:153-158]
- `url_host` (function) component `url_host [function]` (`810c7483-b377-594d-804d-d60e82bd5706`) lines 160-166 [crates/gwiki/src/ingest/wayback.rs:160-166]
  - Signature: `fn url_host(url: &str) -> Option<String> {`
  - Purpose: Parses a URL string and returns its non-empty hostname as an owned String, or None if parsing fails or the host is empty. [crates/gwiki/src/ingest/wayback.rs:160-166]
- `percent_decode_lossy` (function) component `percent_decode_lossy [function]` (`d4c1b3aa-03c0-5760-ae2d-f23107630a24`) lines 168-170 [crates/gwiki/src/ingest/wayback.rs:168-170]
  - Signature: `fn percent_decode_lossy(value: &str) -> String {`
  - Purpose: Decodes a percent-encoded string into an owned String, replacing any invalid UTF-8 byte sequences with the Unicode replacement character (U+FFFD). [crates/gwiki/src/ingest/wayback.rs:168-170]
- `render_wayback_markdown` (function) component `render_wayback_markdown [function]` (`b1a3cc02-f1d6-51bf-b640-faa0d4a583e0`) lines 172-199 [crates/gwiki/src/ingest/wayback.rs:172-199]
  - Signature: `fn render_wayback_markdown(`
  - Purpose: Renders a Wayback Machine snapshot into markdown format by prepending metadata fields (original URL, capture URL, timestamp, fetched time, source hash, and optional content type) as a header block, followed by a title heading and extracted text content from the HTML document. [crates/gwiki/src/ingest/wayback.rs:172-199]
- `html_to_text` (function) component `html_to_text [function]` (`01debb8a-4923-5556-9d02-32b657855bd8`) lines 201-209 [crates/gwiki/src/ingest/wayback.rs:201-209]
  - Signature: `fn html_to_text(document: &Html) -> String {`
  - Purpose: Extracts text from an HTML document, applies per-line transformation via `single_line`, removes empty lines, and joins the result with paragraph-break separators. [crates/gwiki/src/ingest/wayback.rs:201-209]
- `extract_html_text` (function) component `extract_html_text [function]` (`7f903796-7a22-54ad-b1ca-03c667c4bb0f`) lines 211-220 [crates/gwiki/src/ingest/wayback.rs:211-220]
  - Signature: `fn extract_html_text(document: &Html) -> String {`
  - Purpose: Extracts all visible text from an HTML document's body element (or root element if unavailable) and returns it as a newline-delimited string. [crates/gwiki/src/ingest/wayback.rs:211-220]
- `collect_visible_text` (function) component `collect_visible_text [function]` (`17dc2a6a-e2e7-5f84-be8c-7ebe33cb94f1`) lines 222-247 [crates/gwiki/src/ingest/wayback.rs:222-247]
  - Signature: `fn collect_visible_text(element: ElementRef<'_>, parts: &mut Vec<String>) {`
  - Purpose: Recursively collects visible text from an HTML element's subtree into a partitioned string vector, excluding non-rendered elements (head, script, style) and respecting block-level boundaries. [crates/gwiki/src/ingest/wayback.rs:222-247]
- `collect_inline_text` (function) component `collect_inline_text [function]` (`f673f2e4-b02f-56d0-ab34-72c7652e3390`) lines 249-272 [crates/gwiki/src/ingest/wayback.rs:249-272]
  - Signature: `fn collect_inline_text(element: ElementRef<'_>, parts: &mut Vec<String>, inline: &mut String) {`
  - Purpose: Recursively extracts inline text content from an HTML element tree, segmenting the accumulated text into parts whenever block-level element boundaries or `<br>` tags are encountered, while excluding head, script, and style elements. [crates/gwiki/src/ingest/wayback.rs:249-272]
- `append_inline_text` (function) component `append_inline_text [function]` (`4c5c5862-9326-5340-9b05-4116e332d6e4`) lines 274-283 [crates/gwiki/src/ingest/wayback.rs:274-283]
  - Signature: `fn append_inline_text(inline: &mut String, text: &str) {`
  - Purpose: Appends single-line-normalized text to a mutable string with a space separator if the string is non-empty. [crates/gwiki/src/ingest/wayback.rs:274-283]
- `push_text_part` (function) component `push_text_part [function]` (`4b0dd54b-5581-5094-beb1-5fa1b1abf2b2`) lines 285-291 [crates/gwiki/src/ingest/wayback.rs:285-291]
  - Signature: `fn push_text_part(parts: &mut Vec<String>, inline: &mut String) {`
  - Purpose: Converts the inline string to a single line via `single_line()`, clears it, and conditionally pushes the non-empty result to the parts vector. [crates/gwiki/src/ingest/wayback.rs:285-291]
- `is_block_boundary` (function) component `is_block_boundary [function]` (`346392cd-8fef-567f-9632-6f5eba8f8aa9`) lines 293-329 [crates/gwiki/src/ingest/wayback.rs:293-329]
  - Signature: `fn is_block_boundary(name: &str) -> bool {`
  - Purpose: Returns whether the provided element name corresponds to an HTML block-level element via pattern matching against a predefined set of block element tags. [crates/gwiki/src/ingest/wayback.rs:293-329]
- `wayback_records_capture_metadata` (function) component `wayback_records_capture_metadata [function]` (`e440d3ac-25fd-5dc7-9f27-81406f82a27d`) lines 338-377 [crates/gwiki/src/ingest/wayback.rs:338-377]
  - Signature: `fn wayback_records_capture_metadata() {`
  - Purpose: Tests that `ingest_capture` correctly ingests a Wayback Machine capture snapshot into a wiki store, extracting sanitized content and metadata while generating a corresponding source manifest entry. [crates/gwiki/src/ingest/wayback.rs:338-377]
- `wayback_extracts_body_text_without_head_metadata` (function) component `wayback_extracts_body_text_without_head_metadata [function]` (`47c27ca2-d5c7-52d9-b5d8-74cdb7a5e919`) lines 380-390 [crates/gwiki/src/ingest/wayback.rs:380-390]
  - Signature: `fn wayback_extracts_body_text_without_head_metadata() {`
  - Purpose: This test verifies that `html_to_text()` extracts only visible body text while excluding head metadata, title elements, and script tags from parsed HTML documents. [crates/gwiki/src/ingest/wayback.rs:380-390]
- `wayback_groups_inline_text_per_block` (function) component `wayback_groups_inline_text_per_block [function]` (`f5343749-32e8-5149-98ee-7ce1179545ea`) lines 393-407 [crates/gwiki/src/ingest/wayback.rs:393-407]
  - Signature: `fn wayback_groups_inline_text_per_block() {`
  - Purpose: This unit test verifies that `html_to_text()` groups inline sibling elements together as continuous text while separating block-level elements with double newlines and converting `<br>` tags to single newlines. [crates/gwiki/src/ingest/wayback.rs:393-407]
- `wayback_prefers_html_title_then_decoded_url_path_then_host` (function) component `wayback_prefers_html_title_then_decoded_url_path_then_host [function]` (`bd1bb26b-5312-5aa0-b89e-3209cf515265`) lines 410-442 [crates/gwiki/src/ingest/wayback.rs:410-442]
  - Signature: `fn wayback_prefers_html_title_then_decoded_url_path_then_host() {`
  - Purpose: A unit test verifying that `wayback_title()` extracts titles from Wayback snapshots using a cascading fallback strategy: HTML `<title>` element, then decoded URL path, then hostname. [crates/gwiki/src/ingest/wayback.rs:410-442]
- `wayback_does_not_decode_entities_twice` (function) component `wayback_does_not_decode_entities_twice [function]` (`49a7c712-906e-5df0-b76f-3b63b7505964`) lines 445-452 [crates/gwiki/src/ingest/wayback.rs:445-452]
  - Signature: `fn wayback_does_not_decode_entities_twice() {`
  - Purpose: This test verifies that `html_to_text()` decodes HTML entities exactly once, ensuring that `&amp;amp;` is decoded to `&amp;` rather than being double-decoded to `&`. [crates/gwiki/src/ingest/wayback.rs:445-452]
- `wayback_decodes_declared_charset` (function) component `wayback_decodes_declared_charset [function]` (`58de7c73-107a-58a8-9660-54d30470644a`) lines 455-468 [crates/gwiki/src/ingest/wayback.rs:455-468]
  - Signature: `fn wayback_decodes_declared_charset() {`
  - Purpose: This test verifies that `decode_wayback_html()` correctly respects the declared `windows-1252` charset to decode a Wayback Machine snapshot's body bytes into proper Unicode characters. [crates/gwiki/src/ingest/wayback.rs:455-468]
- `wayback_rejects_non_html_content_type` (function) component `wayback_rejects_non_html_content_type [function]` (`0237211d-54bc-5a90-8709-ba738ede58a6`) lines 471-488 [crates/gwiki/src/ingest/wayback.rs:471-488]
  - Signature: `fn wayback_rejects_non_html_content_type() {`
  - Purpose: This unit test verifies that `decode_wayback_html()` rejects Wayback Machine snapshots with non-HTML content types (e.g., `application/pdf`) by returning an `InvalidInput` error on the `content_type` field. [crates/gwiki/src/ingest/wayback.rs:471-488]
- `document_for` (function) component `document_for [function]` (`c5136a2c-7a83-57b9-8815-64f47f36d46c`) lines 490-493 [crates/gwiki/src/ingest/wayback.rs:490-493]
  - Signature: `fn document_for(bytes: &[u8]) -> Html {`
  - Purpose: This function decodes a byte slice as HTML text and returns a parsed HTML document object. [crates/gwiki/src/ingest/wayback.rs:490-493]

