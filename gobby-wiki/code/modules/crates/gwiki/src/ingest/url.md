---
title: crates/gwiki/src/ingest/url
type: code_module
provenance:
- file: crates/gwiki/src/ingest/url/fetch.rs
  ranges:
  - 15-20
  - 23-25
  - 28-35
  - 39-110
  - 113-117
  - 119-133
  - 135-141
  - 144-154
  - 156-158
  - 160-173
  - 176-185
  - 187-199
  - 201-234
  - 236-240
  - 242-263
  - 265-267
  - 269-271
  - 273-282
- file: crates/gwiki/src/ingest/url/render.rs
  ranges:
  - 12-37
  - 39-66
  - 68-74
  - 76-88
  - 90-97
  - 99-105
  - 107-123
  - 125-135
  - 137-146
  - 148-182
  - 184-199
  - 201-207
  - 209-211
  - 213-233
  - 235-244
- file: crates/gwiki/src/ingest/url/tests.rs
  ranges:
  - 21-60
  - 63-93
  - 96-107
  - 110-152
  - 155-175
  - 178-193
  - 196-216
  - 219-224
  - 226-242
  - 245-248
  - 251-254
  - 256-258
  - 260-262
  - 264-266
  - 268-270
  - 272-274
  - 276-278
  - 280-282
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/url/fetch.rs:15-20](crates/gwiki/src/ingest/url/fetch.rs#L15-L20), [crates/gwiki/src/ingest/url/fetch.rs:23-25](crates/gwiki/src/ingest/url/fetch.rs#L23-L25), [crates/gwiki/src/ingest/url/fetch.rs:28-35](crates/gwiki/src/ingest/url/fetch.rs#L28-L35), [crates/gwiki/src/ingest/url/fetch.rs:39-110](crates/gwiki/src/ingest/url/fetch.rs#L39-L110), [crates/gwiki/src/ingest/url/fetch.rs:113-117](crates/gwiki/src/ingest/url/fetch.rs#L113-L117), [crates/gwiki/src/ingest/url/fetch.rs:119-133](crates/gwiki/src/ingest/url/fetch.rs#L119-L133), [crates/gwiki/src/ingest/url/fetch.rs:135-141](crates/gwiki/src/ingest/url/fetch.rs#L135-L141), [crates/gwiki/src/ingest/url/fetch.rs:144-154](crates/gwiki/src/ingest/url/fetch.rs#L144-L154), [crates/gwiki/src/ingest/url/fetch.rs:156-158](crates/gwiki/src/ingest/url/fetch.rs#L156-L158), [crates/gwiki/src/ingest/url/fetch.rs:160-173](crates/gwiki/src/ingest/url/fetch.rs#L160-L173), [crates/gwiki/src/ingest/url/fetch.rs:176-185](crates/gwiki/src/ingest/url/fetch.rs#L176-L185), [crates/gwiki/src/ingest/url/fetch.rs:187-199](crates/gwiki/src/ingest/url/fetch.rs#L187-L199), [crates/gwiki/src/ingest/url/fetch.rs:201-234](crates/gwiki/src/ingest/url/fetch.rs#L201-L234), [crates/gwiki/src/ingest/url/fetch.rs:236-240](crates/gwiki/src/ingest/url/fetch.rs#L236-L240), [crates/gwiki/src/ingest/url/fetch.rs:242-263](crates/gwiki/src/ingest/url/fetch.rs#L242-L263), [crates/gwiki/src/ingest/url/fetch.rs:265-267](crates/gwiki/src/ingest/url/fetch.rs#L265-L267), [crates/gwiki/src/ingest/url/fetch.rs:269-271](crates/gwiki/src/ingest/url/fetch.rs#L269-L271), [crates/gwiki/src/ingest/url/fetch.rs:273-282](crates/gwiki/src/ingest/url/fetch.rs#L273-L282)
- [crates/gwiki/src/ingest/url/render.rs:12-37](crates/gwiki/src/ingest/url/render.rs#L12-L37), [crates/gwiki/src/ingest/url/render.rs:39-66](crates/gwiki/src/ingest/url/render.rs#L39-L66), [crates/gwiki/src/ingest/url/render.rs:68-74](crates/gwiki/src/ingest/url/render.rs#L68-L74), [crates/gwiki/src/ingest/url/render.rs:76-88](crates/gwiki/src/ingest/url/render.rs#L76-L88), [crates/gwiki/src/ingest/url/render.rs:90-97](crates/gwiki/src/ingest/url/render.rs#L90-L97), [crates/gwiki/src/ingest/url/render.rs:99-105](crates/gwiki/src/ingest/url/render.rs#L99-L105), [crates/gwiki/src/ingest/url/render.rs:107-123](crates/gwiki/src/ingest/url/render.rs#L107-L123), [crates/gwiki/src/ingest/url/render.rs:125-135](crates/gwiki/src/ingest/url/render.rs#L125-L135), [crates/gwiki/src/ingest/url/render.rs:137-146](crates/gwiki/src/ingest/url/render.rs#L137-L146), [crates/gwiki/src/ingest/url/render.rs:148-182](crates/gwiki/src/ingest/url/render.rs#L148-L182), [crates/gwiki/src/ingest/url/render.rs:184-199](crates/gwiki/src/ingest/url/render.rs#L184-L199), [crates/gwiki/src/ingest/url/render.rs:201-207](crates/gwiki/src/ingest/url/render.rs#L201-L207), [crates/gwiki/src/ingest/url/render.rs:209-211](crates/gwiki/src/ingest/url/render.rs#L209-L211), [crates/gwiki/src/ingest/url/render.rs:213-233](crates/gwiki/src/ingest/url/render.rs#L213-L233), [crates/gwiki/src/ingest/url/render.rs:235-244](crates/gwiki/src/ingest/url/render.rs#L235-L244)
- [crates/gwiki/src/ingest/url/tests.rs:21-60](crates/gwiki/src/ingest/url/tests.rs#L21-L60), [crates/gwiki/src/ingest/url/tests.rs:63-93](crates/gwiki/src/ingest/url/tests.rs#L63-L93), [crates/gwiki/src/ingest/url/tests.rs:96-107](crates/gwiki/src/ingest/url/tests.rs#L96-L107), [crates/gwiki/src/ingest/url/tests.rs:110-152](crates/gwiki/src/ingest/url/tests.rs#L110-L152), [crates/gwiki/src/ingest/url/tests.rs:155-175](crates/gwiki/src/ingest/url/tests.rs#L155-L175), [crates/gwiki/src/ingest/url/tests.rs:178-193](crates/gwiki/src/ingest/url/tests.rs#L178-L193), [crates/gwiki/src/ingest/url/tests.rs:196-216](crates/gwiki/src/ingest/url/tests.rs#L196-L216), [crates/gwiki/src/ingest/url/tests.rs:219-224](crates/gwiki/src/ingest/url/tests.rs#L219-L224), [crates/gwiki/src/ingest/url/tests.rs:226-242](crates/gwiki/src/ingest/url/tests.rs#L226-L242), [crates/gwiki/src/ingest/url/tests.rs:245-248](crates/gwiki/src/ingest/url/tests.rs#L245-L248), [crates/gwiki/src/ingest/url/tests.rs:251-254](crates/gwiki/src/ingest/url/tests.rs#L251-L254), [crates/gwiki/src/ingest/url/tests.rs:256-258](crates/gwiki/src/ingest/url/tests.rs#L256-L258), [crates/gwiki/src/ingest/url/tests.rs:260-262](crates/gwiki/src/ingest/url/tests.rs#L260-L262), [crates/gwiki/src/ingest/url/tests.rs:264-266](crates/gwiki/src/ingest/url/tests.rs#L264-L266), [crates/gwiki/src/ingest/url/tests.rs:268-270](crates/gwiki/src/ingest/url/tests.rs#L268-L270), [crates/gwiki/src/ingest/url/tests.rs:272-274](crates/gwiki/src/ingest/url/tests.rs#L272-L274), [crates/gwiki/src/ingest/url/tests.rs:276-278](crates/gwiki/src/ingest/url/tests.rs#L276-L278), [crates/gwiki/src/ingest/url/tests.rs:280-282](crates/gwiki/src/ingest/url/tests.rs#L280-L282)

</details>

# crates/gwiki/src/ingest/url

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

The `crates/gwiki/src/ingest/url` module is responsible for the synchronous ingestion of external web content into the `gwiki` knowledge base. It handles HTTP fetching of source URLs, HTML content rendering into clean Markdown-like text, and the safe storage of non-HTML response streams as raw external assets crates/gwiki/src/ingest/url/fetch.rs:15-20 crates/gwiki/src/ingest/url/render.rs:13-25. The module employs rigorous safety checks during fetch flows, such as blocking target IPs from private, local, or loopback subnets, enforcing response body limits, and capping HTTP redirect sequences to prevent loops crates/gwiki/src/ingest/url/fetch.rs:39-110 crates/gwiki/src/ingest/url/tests.rs:110-152.

In terms of key flows and collaboration, the fetch sequence uses an underlying blocking client to generate a `UrlSnapshot` crates/gwiki/src/ingest/url/fetch.rs:15-25. If the snapshot is identified as HTML, the rendering pipeline extracts body content and document titles via `scraper` parsing crates/gwiki/src/ingest/url/render.rs:13-39. Ingested snapshots and related assets are written to a target directory alongside a generated `SourceManifest` metadata index crates/gwiki/src/ingest/url/tests.rs:21-60. The module integrates closely with external libraries like `ureq` and `scraper` as well as local indexing mechanisms, validating that ingestion succeeds and registers changes inside a `WikiStore` implementation crates/gwiki/src/ingest/url/tests.rs:11-18.

### Module Constants

| Constant | Type | Value / Description | File:Line |
| --- | --- | --- | --- |
| `URL_FETCH_TIMEOUT` | Duration | `30` seconds | crates/gwiki/src/ingest/url/fetch.rs:9 |
| `HTTP_STATUS_BODY_LIMIT_BYTES` | u64 | `8192` bytes (8 KB) | crates/gwiki/src/ingest/url/fetch.rs:10 |
| `MAX_REDIRECTS` | usize | `10` | crates/gwiki/src/ingest/url/fetch.rs:11 |
| `USER_AGENT` | &str | `"gwiki/0.1"` | crates/gwiki/src/ingest/url/fetch.rs:12 |

### Core Symbols

| Symbol Name | Kind | Description | File:Line |
| --- | --- | --- | --- |
| `fetch_url_snapshot` | fn | Executes the blocking HTTP fetch flow and returns a `UrlSnapshot` | crates/gwiki/src/ingest/url/fetch.rs:15-20 |
| `BlockingUrlFetcher` | struct | Internal fetch client enclosing the blocking `ureq::Agent` | crates/gwiki/src/ingest/url/fetch.rs:23-25 |
| `render_url_markdown` | fn | Transforms a fetched HTML document into a Markdown-like string | crates/gwiki/src/ingest/url/render.rs:13-39 |
| `render_non_html_url_markdown` | fn | Emits Markdown metadata and treats the fetched document as an asset | crates/gwiki/src/ingest/url/render.rs:41-71 |
| `snapshot_is_html` | fn | Evaluates content type headers to detect HTML payloads | crates/gwiki/src/ingest/url/render.rs:73 |
| `ingest_snapshot` | fn | Performs directory persistence, manifest updates, and database indexing | crates/gwiki/src/ingest/url/tests.rs:40 |
[crates/gwiki/src/ingest/url/fetch.rs:15-20]
[crates/gwiki/src/ingest/url/render.rs:12-37]
[crates/gwiki/src/ingest/url/tests.rs:21-60]
[crates/gwiki/src/ingest/url/fetch.rs:23-25]
[crates/gwiki/src/ingest/url/fetch.rs:28-35]

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/url/fetch.rs\|crates/gwiki/src/ingest/url/fetch.rs]] | Implements the blocking URL-ingest path for `gwiki`: `fetch_url_snapshot` creates a default `BlockingUrlFetcher`, and `BlockingUrlFetcher::fetch` performs the HTTP GET with a fixed user agent, timeout, redirect handling, and snapshot return. The helper functions support that flow by validating the original and resolved URLs, rejecting disallowed IP targets, allowing loopback only for tests, resolving redirect targets, enforcing a body-size limit, truncating diagnostic text, and turning HTTP/status/transport failures into `UrlIngestFailure` values. [crates/gwiki/src/ingest/url/fetch.rs:15-20] [crates/gwiki/src/ingest/url/fetch.rs:23-25] [crates/gwiki/src/ingest/url/fetch.rs:28-35] [crates/gwiki/src/ingest/url/fetch.rs:39-110] [crates/gwiki/src/ingest/url/fetch.rs:113-117] |
| [[code/files/crates/gwiki/src/ingest/url/render.rs\|crates/gwiki/src/ingest/url/render.rs]] | This file turns a fetched URL snapshot into markdown, with separate paths for HTML and non-HTML responses. `render_url_markdown` builds metadata, writes a title heading, and converts the HTML document into plain markdown-like text, while `render_non_html_url_markdown` records the response as a preserved asset and emits a short note instead of body content. The helper functions support that split by classifying snapshots from content type and body heuristics, deriving a filename and title, and extracting visible text from HTML. `html_to_markdownish_text`, `collect_visible_text`, `collect_inline_text`, `push_inline_part`, `is_hidden_element`, `is_text_block`, and `normalize_markdown_text` work together to walk the DOM, skip hidden elements, preserve block structure, and clean up the extracted text. [crates/gwiki/src/ingest/url/render.rs:12-37] [crates/gwiki/src/ingest/url/render.rs:39-66] [crates/gwiki/src/ingest/url/render.rs:68-74] [crates/gwiki/src/ingest/url/render.rs:76-88] [crates/gwiki/src/ingest/url/render.rs:90-97] |
| [[code/files/crates/gwiki/src/ingest/url/tests.rs\|crates/gwiki/src/ingest/url/tests.rs]] | This test file exercises the URL ingestion pipeline end to end. It verifies that ingesting a snapshot writes the rendered raw document plus source manifest metadata, preserves non-HTML content as a typed asset, and that the HTML parser extracts body text and decodes entities correctly. It also covers batch ingestion behavior, including accepting partial successes while recording failures and indexing only once for an accepted batch, plus fetch safeguards such as content-length limits, blocking private/local addresses, and resolving relative redirect locations. A small `CountingStore` test double is included to track index/store method calls used by the ingestion flow. [crates/gwiki/src/ingest/url/tests.rs:21-60] [crates/gwiki/src/ingest/url/tests.rs:63-93] [crates/gwiki/src/ingest/url/tests.rs:96-107] [crates/gwiki/src/ingest/url/tests.rs:110-152] [crates/gwiki/src/ingest/url/tests.rs:155-175] |

## Components

| Component ID |
| --- |
| `11a06225-0ad9-5778-8edf-c45ccbf1b0fd` |
| `577536dc-7a49-50f2-b7fe-37aebc2cc1d1` |
| `4da23ab2-00d9-5c2d-90e7-bdbbfaae08ab` |
| `74ea55d8-bf1a-5c27-a16b-9a4c2261649e` |
| `faef89b1-5378-539c-984f-0ef8ae403188` |
| `993bd27b-c1c9-5585-91e9-70d32bdbf9b9` |
| `1a1eb760-a5c3-5069-a868-c666ee0860a0` |
| `fd4742a0-ffae-518c-be08-1249389f7f5b` |
| `6d9002a2-65da-5412-adbe-037bb1d65852` |
| `b860735c-6559-593e-8e4b-d97aed891752` |
| `164fc21b-f3a1-53c6-abb2-59431397aec9` |
| `532bc610-052c-5468-8247-217911c7af4c` |
| `170bc9f5-8062-50c2-a52e-ecd192e32eb5` |
| `5c6426f7-8b96-5698-b993-665b683922b3` |
| `0ad1e13f-d8f0-5171-9cb6-a5e746907d48` |
| `f13ed816-63d9-5fea-92de-d6611de7c6e4` |
| `7699f494-2916-5e24-914a-6af2fb9a4546` |
| `19d9739a-21b0-5f11-bf97-3db1b9d6fac3` |
| `21aefa28-d570-59c8-9cd7-9a6aea6ddc06` |
| `1a8b4668-73f8-5f9a-8ddb-2989ddfdd97e` |
| `80694710-9018-5f4c-a213-8e4b695502a0` |
| `d5a13fd7-9757-5672-967e-1a175cdc83c9` |
| `b0ff2069-d800-598c-aaf0-e675340fa595` |
| `7cca9fea-6099-5172-920a-305501b65dbf` |
| `1fabf794-8ac6-5eb7-a26d-b420746682ea` |
| `b852b1ce-8398-5ee7-af3e-9baf14841659` |
| `8c7a1d45-5b61-5a3c-b0ca-9a0e2c55f319` |
| `ea4a3a39-f2ad-515b-b02d-72e369879180` |
| `cb2147a6-c18f-5e8e-871e-73ecd2ea802b` |
| `af995ab1-a4e4-5fb5-a6ef-0876089a588a` |
| `b9a03989-bd23-5f82-b710-d4dd34ff75a3` |
| `1c21bd86-ef5d-5c09-bf50-b7936810284a` |
| `e2022f11-057b-5922-9402-f00b897dd499` |
| `dc1bc4da-6d0f-5fff-9eb7-f5a9d4488b61` |
| `270f239e-942c-5b9c-93fb-e603a581ff4c` |
| `9910df43-b2d5-5366-801a-2a532122b7f2` |
| `a18ae2a6-e388-5b49-bfa5-cdce243b04f6` |
| `ea11c97a-4a6f-5c17-bf3f-5bfe3a3c8fe8` |
| `ebc06a55-a3e1-508e-a71c-79ae95b34bcb` |
| `5122fa23-568d-5c76-9002-ac467cd4b7d1` |
| `c277ee98-3ba2-5a69-b3d3-7a367778c8ac` |
| `242d9bc6-25df-5dc5-b7b7-242079068a47` |
| `bae02c35-ce0a-5c31-af41-2ffb4e358285` |
| `4a4e0d07-296e-56f8-a944-2760bd5eba96` |
| `52f34138-c19e-56c5-ad66-3be5fc0dd4b7` |
| `5fb4eb2d-23fa-5f0f-9202-b0fe589584ca` |
| `ba0352de-22b0-54a0-b1ef-000a467d8acb` |
| `badcee9b-37de-5e74-946b-1fa178053e29` |
| `01a66b80-f006-5fb4-8c35-1312f7b68adb` |
| `0962ec4b-6488-58a8-b32b-030e362216ae` |
| `2573c39b-46fe-5265-897d-74aa7e1a8635` |
