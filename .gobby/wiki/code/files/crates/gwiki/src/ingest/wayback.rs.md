---
title: crates/gwiki/src/ingest/wayback.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/wayback.rs
  ranges:
  - 18-25
  - 28-47
  - 50-60
  - 63-75
  - 78-98
  - 101-108
  - 111-118
  - 121-129
  - 132-139
  - 142-145
  - 148-153
  - 156-163
  - 166-171
  - 174-180
  - 183-185
  - 188-215
  - 218-226
  - 229-238
  - 241-266
  - 269-292
  - 295-304
  - 307-313
  - 316-352
  - 361-400
  - 403-413
  - 416-430
  - 433-465
  - 468-475
  - 478-491
  - 494-511
  - 513-516
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/wayback.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

This file implements ingestion for Wayback-archived captures. `WaybackCaptureSnapshot` holds the archived URL metadata, timestamps, body bytes, and optional content type; `ingest_capture` turns that snapshot into a stored wiki record by validating and decoding the HTML, parsing it for a title and visible text, registering a `SourceDraft` in the source manifest, rendering a Wayback-specific Markdown document, and writing/indexing it. The helper functions support that pipeline by enforcing HTML-only content types, choosing an encoding from the response headers, BOM, or HTML `<meta charset>`, deriving fallback titles from the document or URL, extracting plain text from the HTML tree while skipping head/script/style content and preserving block structure, and formatting the final markdown metadata and body. The tests exercise the main behaviors: metadata recording, title fallback order, charset decoding, HTML validation, and text extraction rules.
[crates/gwiki/src/ingest/wayback.rs:18-25]
[crates/gwiki/src/ingest/wayback.rs:28-47]
[crates/gwiki/src/ingest/wayback.rs:50-60]
[crates/gwiki/src/ingest/wayback.rs:63-75]
[crates/gwiki/src/ingest/wayback.rs:78-98]

## API Symbols

- `WaybackCaptureSnapshot` (class) component `WaybackCaptureSnapshot [class]` (`ceb67b01-2212-5c09-80d9-6cc5686bb87b`) lines 18-25 [crates/gwiki/src/ingest/wayback.rs:18-25]
  - Signature: `pub struct WaybackCaptureSnapshot {`
  - Purpose: 'WaybackCaptureSnapshot' is a data container for an archived web capture, storing the original and capture URLs, capture and fetch timestamps, raw response body bytes, and an optional content type. [crates/gwiki/src/ingest/wayback.rs:18-25]
- `ingest_capture` (function) component `ingest_capture [function]` (`64b0c162-7265-5858-b461-95e60f8dd46d`) lines 28-47 [crates/gwiki/src/ingest/wayback.rs:28-47]
  - Signature: `pub fn ingest_capture(`
  - Purpose: 'ingest_capture' decodes a Wayback snapshot’s HTML, parses it to derive a title, registers a 'SourceDraft' for the capture URL and fetched body in the vault manifest, renders Wayback-specific Markdown using the record’s content hash, and writes/indexes the result via 'write_raw_then_index'. [crates/gwiki/src/ingest/wayback.rs:28-47]
- `decode_wayback_html` (function) component `decode_wayback_html [function]` (`74aa7287-4f63-5b76-b031-5476596e6de6`) lines 50-60 [crates/gwiki/src/ingest/wayback.rs:50-60]
  - Signature: `fn decode_wayback_html(snapshot: &WaybackCaptureSnapshot) -> Result<String, WikiError> {`
  - Purpose: Validates that the snapshot’s content type is HTML, decodes the body bytes into a string, verifies the result looks like an HTML document, and returns it or a 'WikiError::InvalidInput' if the capture is not valid HTML. [crates/gwiki/src/ingest/wayback.rs:50-60]
- `ensure_html_content_type` (function) component `ensure_html_content_type [function]` (`63d89456-50e7-5784-954e-868577d872ba`) lines 63-75 [crates/gwiki/src/ingest/wayback.rs:63-75]
  - Signature: `fn ensure_html_content_type(content_type: Option<&str>) -> Result<(), WikiError> {`
  - Purpose: Validates that an optional 'content_type' resolves to either 'text/html' or 'application/xhtml+xml', returning 'Ok(())' for HTML/XHTML and otherwise raising 'WikiError::InvalidInput' for missing or non-HTML content types. [crates/gwiki/src/ingest/wayback.rs:63-75]
- `decode_html_bytes` (function) component `decode_html_bytes [function]` (`2fbf37d2-86ce-5b78-9ef9-123d039786df`) lines 78-98 [crates/gwiki/src/ingest/wayback.rs:78-98]
  - Signature: `fn decode_html_bytes(bytes: &[u8], content_type: Option<&str>) -> String {`
  - Purpose: Decodes the input HTML byte slice to a 'String' by selecting an encoding in priority order from the 'Content-Type' charset, then a byte-order mark, then an HTML '<meta charset>' declaration, and falling back to UTF-8. [crates/gwiki/src/ingest/wayback.rs:78-98]
- `content_type_media_type` (function) component `content_type_media_type [function]` (`bbe86f9f-d0dd-5b58-a712-225a48c1e80e`) lines 101-108 [crates/gwiki/src/ingest/wayback.rs:101-108]
  - Signature: `fn content_type_media_type(content_type: Option<&str>) -> Option<String> {`
  - Purpose: Returns the lowercase MIME media type prefix from an optional 'Content-Type' string by taking the substring before the first ';', trimming whitespace, discarding empty results, and propagating 'None' when input is absent. [crates/gwiki/src/ingest/wayback.rs:101-108]
- `charset_from_content_type` (function) component `charset_from_content_type [function]` (`429d497d-d280-5e0e-a700-be67336aeb74`) lines 111-118 [crates/gwiki/src/ingest/wayback.rs:111-118]
  - Signature: `fn charset_from_content_type(content_type: Option<&str>) -> Option<String> {`
  - Purpose: Parses an optional 'Content-Type' header string and returns the first non-empty 'charset' parameter value, case-insensitively matching the parameter name and trimming the label. [crates/gwiki/src/ingest/wayback.rs:111-118]
- `charset_from_html_meta` (function) component `charset_from_html_meta [function]` (`1cc71d43-27e3-51f4-88b0-1945b184c7c4`) lines 121-129 [crates/gwiki/src/ingest/wayback.rs:121-129]
  - Signature: `fn charset_from_html_meta(bytes: &[u8]) -> Option<String> {`
  - Purpose: Scans up to the first 4096 bytes of the input as lossy UTF-8 and returns the first case-insensitive 'charset=...' value matching '[a-z0-9._:-]+' from the HTML head, or 'None' if no match is found. [crates/gwiki/src/ingest/wayback.rs:121-129]
- `trim_charset_label` (function) component `trim_charset_label [function]` (`7a3a3a8d-7036-5b0b-9dec-628897fb0215`) lines 132-139 [crates/gwiki/src/ingest/wayback.rs:132-139]
  - Signature: `fn trim_charset_label(value: &str) -> String {`
  - Purpose: Returns a new 'String' with leading and trailing whitespace removed, then any surrounding double or single quotes stripped, and whitespace trimmed again. [crates/gwiki/src/ingest/wayback.rs:132-139]
- `html_looks_like_document` (function) component `html_looks_like_document [function]` (`b9157707-ea6a-5d17-aad3-840932a7783f`) lines 142-145 [crates/gwiki/src/ingest/wayback.rs:142-145]
  - Signature: `fn html_looks_like_document(html: &str) -> bool {`
  - Purpose: Returns 'true' when the trimmed, case-insensitive HTML string begins with '<!doctype html' or '<html', or contains a '<body' tag anywhere, indicating it likely represents a full document rather than a fragment. [crates/gwiki/src/ingest/wayback.rs:142-145]
- `wayback_title` (function) component `wayback_title [function]` (`a46c9b3c-1cc8-512c-9bdd-439dc4eeed15`) lines 148-153 [crates/gwiki/src/ingest/wayback.rs:148-153]
  - Signature: `fn wayback_title(snapshot: &WaybackCaptureSnapshot, document: &Html) -> String {`
  - Purpose: Returns the best available title for a Wayback snapshot by preferring the document’s HTML title, then the original URL path, then the original URL host, and finally a markdown-formatted original URL fallback. [crates/gwiki/src/ingest/wayback.rs:148-153]
- `html_title` (function) component `html_title [function]` (`983cc05c-c50f-5d44-b58c-157e91ef49a8`) lines 156-163 [crates/gwiki/src/ingest/wayback.rs:156-163]
  - Signature: `fn html_title(document: &Html) -> Option<String> {`
  - Purpose: Returns the first '<title>' element’s text from the HTML document, normalizes it via 'single_line' and 'markdown_title', and yields 'None' if the resulting title is empty or absent. [crates/gwiki/src/ingest/wayback.rs:156-163]
- `title_from_url_path` (function) component `title_from_url_path [function]` (`74d345fa-9c9b-5add-a8a6-d07bfe193f5f`) lines 166-171 [crates/gwiki/src/ingest/wayback.rs:166-171]
  - Signature: `fn title_from_url_path(url: &str) -> Option<String> {`
  - Purpose: Parses 'url' as a 'Url', takes the last non-empty path segment, percent-decodes it, converts it with 'markdown_title', and returns 'Some(title)' only if the result is non-empty. [crates/gwiki/src/ingest/wayback.rs:166-171]
- `url_host` (function) component `url_host [function]` (`5cfab864-7609-5f52-b29e-0d2eb99aacd5`) lines 174-180 [crates/gwiki/src/ingest/wayback.rs:174-180]
  - Signature: `fn url_host(url: &str) -> Option<String> {`
  - Purpose: Parses the input string as a URL and returns the non-empty host component as an owned 'String', or 'None' if parsing fails or no host is present. [crates/gwiki/src/ingest/wayback.rs:174-180]
- `percent_decode_lossy` (function) component `percent_decode_lossy [function]` (`e6fc6764-8a2c-5687-92d1-6f6806110fca`) lines 183-185 [crates/gwiki/src/ingest/wayback.rs:183-185]
  - Signature: `fn percent_decode_lossy(value: &str) -> String {`
  - Purpose: 'percent_decode_lossy' percent-decodes the input string and returns a UTF-8 lossy-decoded owned 'String', replacing any invalid byte sequences with the Unicode replacement character. [crates/gwiki/src/ingest/wayback.rs:183-185]
- `render_wayback_markdown` (function) component `render_wayback_markdown [function]` (`3be24ac8-55f8-5e35-8d9c-e6e0494de09f`) lines 188-215 [crates/gwiki/src/ingest/wayback.rs:188-215]
  - Signature: `fn render_wayback_markdown(`
  - Purpose: Builds a Wayback markdown document by emitting metadata fields for the snapshot and source hash, then appending a शीर्ष-level title and the plain-text extraction of the HTML document, ensuring the result ends with a newline. [crates/gwiki/src/ingest/wayback.rs:188-215]
- `html_to_text` (function) component `html_to_text [function]` (`8e64392c-e5fd-5aa3-b61d-9a93c43fd092`) lines 218-226 [crates/gwiki/src/ingest/wayback.rs:218-226]
  - Signature: `fn html_to_text(document: &Html) -> String {`
  - Purpose: Converts an 'Html' document to plain text by extracting its text content, normalizing each line with 'single_line', discarding empty lines, and joining the remaining lines with blank-line separators ('"\n\n"'). [crates/gwiki/src/ingest/wayback.rs:218-226]
- `extract_html_text` (function) component `extract_html_text [function]` (`ffdc2350-229a-58aa-b35b-a4baae81c8ec`) lines 229-238 [crates/gwiki/src/ingest/wayback.rs:229-238]
  - Signature: `fn extract_html_text(document: &Html) -> String {`
  - Purpose: Extracts visible text from the HTML '<body>' element if present, otherwise from the document root, by recursively collecting text into a buffer and joining the segments with newline separators. [crates/gwiki/src/ingest/wayback.rs:229-238]
- `collect_visible_text` (function) component `collect_visible_text [function]` (`84e1fe88-0ea4-5e19-a54d-55c7935ed31d`) lines 241-266 [crates/gwiki/src/ingest/wayback.rs:241-266]
  - Signature: `fn collect_visible_text(element: ElementRef<'_>, parts: &mut Vec<String>) {`
  - Purpose: Recursively extracts visible text from an HTML element into 'parts', skipping 'head'/'script'/'style', preserving inline text accumulation, and flushing on '<br>' or block-boundary elements. [crates/gwiki/src/ingest/wayback.rs:241-266]
- `collect_inline_text` (function) component `collect_inline_text [function]` (`3dda53fa-58b8-53e7-b90b-c5ce8ff79b57`) lines 269-292 [crates/gwiki/src/ingest/wayback.rs:269-292]
  - Signature: `fn collect_inline_text(element: ElementRef<'_>, parts: &mut Vec<String>, inline: &mut String) {`
  - Purpose: Recursively accumulates visible inline text from an HTML element into 'inline', flushing it into 'parts' at '<br>' and block-boundary descendants while skipping 'head', 'script', and 'style' subtrees. [crates/gwiki/src/ingest/wayback.rs:269-292]
- `append_inline_text` (function) component `append_inline_text [function]` (`87d78bce-d102-50f3-b1e9-e47b376f80c0`) lines 295-304 [crates/gwiki/src/ingest/wayback.rs:295-304]
  - Signature: `fn append_inline_text(inline: &mut String, text: &str) {`
  - Purpose: Appends 'text' to 'inline' as a single-line string, skipping empty input and inserting one separating space if 'inline' already contains content. [crates/gwiki/src/ingest/wayback.rs:295-304]
- `push_text_part` (function) component `push_text_part [function]` (`79d78a00-1ad0-5c4a-91c7-668c833e1d58`) lines 307-313 [crates/gwiki/src/ingest/wayback.rs:307-313]
  - Signature: `fn push_text_part(parts: &mut Vec<String>, inline: &mut String) {`
  - Purpose: Normalizes the accumulated 'inline' text to a single line, clears the buffer, and appends the resulting string to 'parts' only if it is non-empty. [crates/gwiki/src/ingest/wayback.rs:307-313]
- `is_block_boundary` (function) component `is_block_boundary [function]` (`fdf6e74d-b4f3-5bbb-9924-e0cb0facb3ed`) lines 316-352 [crates/gwiki/src/ingest/wayback.rs:316-352]
  - Signature: `fn is_block_boundary(name: &str) -> bool {`
  - Purpose: Returns 'true' iff 'name' is one of a fixed set of HTML block-level/sectioning container tag names, and 'false' otherwise. [crates/gwiki/src/ingest/wayback.rs:316-352]
- `wayback_records_capture_metadata` (function) component `wayback_records_capture_metadata [function]` (`1b535367-6c76-569d-a85f-f7e9362ecae4`) lines 361-400 [crates/gwiki/src/ingest/wayback.rs:361-400]
  - Signature: `fn wayback_records_capture_metadata() {`
  - Purpose: Tests that ingesting a Wayback capture writes a Markdown record with the expected source metadata and decoded body content, strips scripts/styles, and records a single 'Wayback' entry in the source manifest. [crates/gwiki/src/ingest/wayback.rs:361-400]
- `wayback_extracts_body_text_without_head_metadata` (function) component `wayback_extracts_body_text_without_head_metadata [function]` (`e4fd5946-35c5-52a2-94f0-a26791ab96e4`) lines 403-413 [crates/gwiki/src/ingest/wayback.rs:403-413]
  - Signature: `fn wayback_extracts_body_text_without_head_metadata() {`
  - Purpose: Verifies that HTML-to-text extraction from a Wayback-archived page returns only the decoded visible body text and excludes '<head>' metadata and script content. [crates/gwiki/src/ingest/wayback.rs:403-413]
- `wayback_groups_inline_text_per_block` (function) component `wayback_groups_inline_text_per_block [function]` (`43692c99-259f-5ccc-9320-3230f7e19ebd`) lines 416-430 [crates/gwiki/src/ingest/wayback.rs:416-430]
  - Signature: `fn wayback_groups_inline_text_per_block() {`
  - Purpose: Verifies that 'html_to_text' preserves inline siblings within a block as a single text run while converting block boundaries and '<br>' elements into the expected newline-separated output. [crates/gwiki/src/ingest/wayback.rs:416-430]
- `wayback_prefers_html_title_then_decoded_url_path_then_host` (function) component `wayback_prefers_html_title_then_decoded_url_path_then_host [function]` (`e68e6ece-a42f-5663-8080-9ded3c72cdf5`) lines 433-465 [crates/gwiki/src/ingest/wayback.rs:433-465]
  - Signature: `fn wayback_prefers_html_title_then_decoded_url_path_then_host() {`
  - Purpose: Verifies that 'wayback_title' chooses the HTML '<title>' when present, otherwise falls back to a decoded URL path segment, and finally to the host name when no path title is available. [crates/gwiki/src/ingest/wayback.rs:433-465]
- `wayback_does_not_decode_entities_twice` (function) component `wayback_does_not_decode_entities_twice [function]` (`83ecc2ee-e393-5ad0-a1a7-46e649d9da37`) lines 468-475 [crates/gwiki/src/ingest/wayback.rs:468-475]
  - Signature: `fn wayback_does_not_decode_entities_twice() {`
  - Purpose: Verifies that 'html_to_text' decodes HTML entities exactly once by converting '&amp;amp;' in the input into the literal text '&amp;' rather than '&'. [crates/gwiki/src/ingest/wayback.rs:468-475]
- `wayback_decodes_declared_charset` (function) component `wayback_decodes_declared_charset [function]` (`b0348520-a7e0-5b7b-b803-252980536758`) lines 478-491 [crates/gwiki/src/ingest/wayback.rs:478-491]
  - Signature: `fn wayback_decodes_declared_charset() {`
  - Purpose: Verifies that 'decode_wayback_html' decodes a Wayback snapshot’s HTML body using the declared 'windows-1252' charset, producing Unicode text containing 'café'. [crates/gwiki/src/ingest/wayback.rs:478-491]
- `wayback_rejects_non_html_content_type` (function) component `wayback_rejects_non_html_content_type [function]` (`8f244255-fb17-54c0-99b8-dcd36feecb42`) lines 494-511 [crates/gwiki/src/ingest/wayback.rs:494-511]
  - Signature: `fn wayback_rejects_non_html_content_type() {`
  - Purpose: Verifies that 'decode_wayback_html' rejects a Wayback snapshot whose 'content_type' is 'application/pdf' by returning 'WikiError::InvalidInput' for the 'content_type' field. [crates/gwiki/src/ingest/wayback.rs:494-511]
- `document_for` (function) component `document_for [function]` (`24eac95d-9a8b-5a3f-842c-a3eba4a478af`) lines 513-516 [crates/gwiki/src/ingest/wayback.rs:513-516]
  - Signature: `fn document_for(bytes: &[u8]) -> Html {`
  - Purpose: Decodes the input byte slice as HTML using 'decode_html_bytes' with a 'text/html' MIME hint, then parses the resulting string into an 'Html' document with 'Html::parse_document'. [crates/gwiki/src/ingest/wayback.rs:513-516]

