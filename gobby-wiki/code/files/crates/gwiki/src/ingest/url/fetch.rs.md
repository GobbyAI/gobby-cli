---
title: crates/gwiki/src/ingest/url/fetch.rs
type: code_file
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/url/fetch.rs:15-20](crates/gwiki/src/ingest/url/fetch.rs#L15-L20), [crates/gwiki/src/ingest/url/fetch.rs:23-25](crates/gwiki/src/ingest/url/fetch.rs#L23-L25), [crates/gwiki/src/ingest/url/fetch.rs:28-35](crates/gwiki/src/ingest/url/fetch.rs#L28-L35), [crates/gwiki/src/ingest/url/fetch.rs:39-110](crates/gwiki/src/ingest/url/fetch.rs#L39-L110), [crates/gwiki/src/ingest/url/fetch.rs:113-117](crates/gwiki/src/ingest/url/fetch.rs#L113-L117), [crates/gwiki/src/ingest/url/fetch.rs:119-133](crates/gwiki/src/ingest/url/fetch.rs#L119-L133), [crates/gwiki/src/ingest/url/fetch.rs:135-141](crates/gwiki/src/ingest/url/fetch.rs#L135-L141), [crates/gwiki/src/ingest/url/fetch.rs:144-154](crates/gwiki/src/ingest/url/fetch.rs#L144-L154), [crates/gwiki/src/ingest/url/fetch.rs:156-158](crates/gwiki/src/ingest/url/fetch.rs#L156-L158), [crates/gwiki/src/ingest/url/fetch.rs:160-173](crates/gwiki/src/ingest/url/fetch.rs#L160-L173), [crates/gwiki/src/ingest/url/fetch.rs:176-185](crates/gwiki/src/ingest/url/fetch.rs#L176-L185), [crates/gwiki/src/ingest/url/fetch.rs:187-199](crates/gwiki/src/ingest/url/fetch.rs#L187-L199), [crates/gwiki/src/ingest/url/fetch.rs:201-234](crates/gwiki/src/ingest/url/fetch.rs#L201-L234), [crates/gwiki/src/ingest/url/fetch.rs:236-240](crates/gwiki/src/ingest/url/fetch.rs#L236-L240), [crates/gwiki/src/ingest/url/fetch.rs:242-263](crates/gwiki/src/ingest/url/fetch.rs#L242-L263), [crates/gwiki/src/ingest/url/fetch.rs:265-267](crates/gwiki/src/ingest/url/fetch.rs#L265-L267), [crates/gwiki/src/ingest/url/fetch.rs:269-271](crates/gwiki/src/ingest/url/fetch.rs#L269-L271), [crates/gwiki/src/ingest/url/fetch.rs:273-282](crates/gwiki/src/ingest/url/fetch.rs#L273-L282)

</details>

# crates/gwiki/src/ingest/url/fetch.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the blocking URL-ingest path for `gwiki`: `fetch_url_snapshot` creates a default `BlockingUrlFetcher`, and `BlockingUrlFetcher::fetch` performs the HTTP GET with a fixed user agent, timeout, redirect handling, and snapshot return. The helper functions support that flow by validating the original and resolved URLs, rejecting disallowed IP targets, allowing loopback only for tests, resolving redirect targets, enforcing a body-size limit, truncating diagnostic text, and turning HTTP/status/transport failures into `UrlIngestFailure` values.
[crates/gwiki/src/ingest/url/fetch.rs:15-20]
[crates/gwiki/src/ingest/url/fetch.rs:23-25]
[crates/gwiki/src/ingest/url/fetch.rs:28-35]
[crates/gwiki/src/ingest/url/fetch.rs:39-110]
[crates/gwiki/src/ingest/url/fetch.rs:113-117]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `fetch_url_snapshot` | function | `pub(super) fn fetch_url_snapshot(` | `fetch_url_snapshot [function]` | `11a06225-0ad9-5778-8edf-c45ccbf1b0fd` | 15-20 [crates/gwiki/src/ingest/url/fetch.rs:15-20] | Indexed function `fetch_url_snapshot` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:15-20] |
| `BlockingUrlFetcher` | class | `struct BlockingUrlFetcher {` | `BlockingUrlFetcher [class]` | `577536dc-7a49-50f2-b7fe-37aebc2cc1d1` | 23-25 [crates/gwiki/src/ingest/url/fetch.rs:23-25] | Indexed class `BlockingUrlFetcher` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:23-25] |
| `BlockingUrlFetcher::default` | method | `fn default() -> Self {` | `BlockingUrlFetcher::default [method]` | `4da23ab2-00d9-5c2d-90e7-bdbbfaae08ab` | 28-35 [crates/gwiki/src/ingest/url/fetch.rs:28-35] | Indexed method `BlockingUrlFetcher::default` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:28-35] |
| `BlockingUrlFetcher::fetch` | method | `fn fetch(&self, url: &str, fetched_at: &str) -> Result<UrlSnapshot, UrlIngestFailure> {` | `BlockingUrlFetcher::fetch [method]` | `74ea55d8-bf1a-5c27-a16b-9a4c2261649e` | 39-110 [crates/gwiki/src/ingest/url/fetch.rs:39-110] | Indexed method `BlockingUrlFetcher::fetch` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:39-110] |
| `content_length_exceeds_limit` | function | `pub(super) fn content_length_exceeds_limit(content_length: Option<&str>, max_bytes: u64) -> bool {` | `content_length_exceeds_limit [function]` | `faef89b1-5378-539c-984f-0ef8ae403188` | 113-117 [crates/gwiki/src/ingest/url/fetch.rs:113-117] | Indexed function `content_length_exceeds_limit` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:113-117] |
| `read_limited_body` | function | `pub(super) fn read_limited_body(` | `read_limited_body [function]` | `993bd27b-c1c9-5585-91e9-70d32bdbf9b9` | 119-133 [crates/gwiki/src/ingest/url/fetch.rs:119-133] | Indexed function `read_limited_body` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:119-133] |
| `response_too_large` | function | `fn response_too_large(url: &str, max_bytes: u64) -> UrlIngestFailure {` | `response_too_large [function]` | `1a1eb760-a5c3-5069-a868-c666ee0860a0` | 135-141 [crates/gwiki/src/ingest/url/fetch.rs:135-141] | Indexed function `response_too_large` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:135-141] |
| `UrlIngestFailure::new` | method | `pub(super) fn new(` | `UrlIngestFailure::new [method]` | `fd4742a0-ffae-518c-be08-1249389f7f5b` | 144-154 [crates/gwiki/src/ingest/url/fetch.rs:144-154] | Indexed method `UrlIngestFailure::new` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:144-154] |
| `UrlIngestFailure::from_wiki_error` | method | `pub(super) fn from_wiki_error(url: &str, error: WikiError) -> Self {` | `UrlIngestFailure::from_wiki_error [method]` | `6d9002a2-65da-5412-adbe-037bb1d65852` | 156-158 [crates/gwiki/src/ingest/url/fetch.rs:156-158] | Indexed method `UrlIngestFailure::from_wiki_error` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:156-158] |
| `UrlIngestFailure::http_status` | method | `fn http_status(url: &str, status: u16, response: ureq::Response) -> Self {` | `UrlIngestFailure::http_status [method]` | `b860735c-6559-593e-8e4b-d97aed891752` | 160-173 [crates/gwiki/src/ingest/url/fetch.rs:160-173] | Indexed method `UrlIngestFailure::http_status` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:160-173] |
| `resolve_redirect_url` | function | `pub(super) fn resolve_redirect_url(` | `resolve_redirect_url [function]` | `164fc21b-f3a1-53c6-abb2-59431397aec9` | 176-185 [crates/gwiki/src/ingest/url/fetch.rs:176-185] | Indexed function `resolve_redirect_url` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:176-185] |
| `validate_fetch_url` | function | `fn validate_fetch_url(raw_url: &str) -> Result<(), UrlIngestFailure> {` | `validate_fetch_url [function]` | `532bc610-052c-5468-8247-217911c7af4c` | 187-199 [crates/gwiki/src/ingest/url/fetch.rs:187-199] | Indexed function `validate_fetch_url` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:187-199] |
| `validate_resolved_fetch_url` | function | `fn validate_resolved_fetch_url(raw_url: &str) -> Result<(), UrlIngestFailure> {` | `validate_resolved_fetch_url [function]` | `170bc9f5-8062-50c2-a52e-ecd192e32eb5` | 201-234 [crates/gwiki/src/ingest/url/fetch.rs:201-234] | Indexed function `validate_resolved_fetch_url` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:201-234] |
| `loopback_fetch_allowed_for_tests` | function | `fn loopback_fetch_allowed_for_tests(ip: IpAddr) -> bool {` | `loopback_fetch_allowed_for_tests [function]` | `5c6426f7-8b96-5698-b993-665b683922b3` | 236-240 [crates/gwiki/src/ingest/url/fetch.rs:236-240] | Indexed function `loopback_fetch_allowed_for_tests` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:236-240] |
| `is_disallowed_fetch_ip` | function | `pub(super) fn is_disallowed_fetch_ip(ip: IpAddr) -> bool {` | `is_disallowed_fetch_ip [function]` | `0ad1e13f-d8f0-5171-9cb6-a5e746907d48` | 242-263 [crates/gwiki/src/ingest/url/fetch.rs:242-263] | Indexed function `is_disallowed_fetch_ip` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:242-263] |
| `is_ipv6_unique_local` | function | `fn is_ipv6_unique_local(ip: Ipv6Addr) -> bool {` | `is_ipv6_unique_local [function]` | `f13ed816-63d9-5fea-92de-d6611de7c6e4` | 265-267 [crates/gwiki/src/ingest/url/fetch.rs:265-267] | Indexed function `is_ipv6_unique_local` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:265-267] |
| `is_ipv6_unicast_link_local` | function | `fn is_ipv6_unicast_link_local(ip: Ipv6Addr) -> bool {` | `is_ipv6_unicast_link_local [function]` | `7699f494-2916-5e24-914a-6af2fb9a4546` | 269-271 [crates/gwiki/src/ingest/url/fetch.rs:269-271] | Indexed function `is_ipv6_unicast_link_local` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:269-271] |
| `truncate_message` | function | `fn truncate_message(message: &str) -> String {` | `truncate_message [function]` | `19d9739a-21b0-5f11-bf97-3db1b9d6fac3` | 273-282 [crates/gwiki/src/ingest/url/fetch.rs:273-282] | Indexed function `truncate_message` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:273-282] |
