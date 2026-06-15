---
title: crates/gwiki/src/ingest/url/fetch.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/url/fetch.rs
  ranges:
  - 15-20
  - 23-25
  - 27-36
  - 38-111
  - 113-117
  - 119-133
  - 135-141
  - 143-174
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

# crates/gwiki/src/ingest/url/fetch.rs

Module: [[code/modules/crates/gwiki/src/ingest/url|crates/gwiki/src/ingest/url]]

## Purpose

Implements blocking URL snapshot fetching for ingest: `fetch_url_snapshot` constructs a default `BlockingUrlFetcher`, which issues HTTP GETs with a fixed timeout and user agent, follows redirects up to a cap, and returns a `UrlSnapshot` or a structured `UrlIngestFailure`. The supporting helpers validate the original and resolved URLs, reject disallowed fetch targets such as local/private IPs, limit and truncate response bodies, resolve redirect targets, and map fetch or HTTP failures into error types with appropriate status information.
[crates/gwiki/src/ingest/url/fetch.rs:15-20]
[crates/gwiki/src/ingest/url/fetch.rs:23-25]
[crates/gwiki/src/ingest/url/fetch.rs:27-36]
[crates/gwiki/src/ingest/url/fetch.rs:28-35]
[crates/gwiki/src/ingest/url/fetch.rs:38-111]

## API Symbols

- `fetch_url_snapshot` (function) component `fetch_url_snapshot [function]` (`11a06225-0ad9-5778-8edf-c45ccbf1b0fd`) lines 15-20 [crates/gwiki/src/ingest/url/fetch.rs:15-20]
  - Signature: `pub(super) fn fetch_url_snapshot(`
  - Purpose: Indexed function `fetch_url_snapshot` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:15-20]
- `BlockingUrlFetcher` (class) component `BlockingUrlFetcher [class]` (`577536dc-7a49-50f2-b7fe-37aebc2cc1d1`) lines 23-25 [crates/gwiki/src/ingest/url/fetch.rs:23-25]
  - Signature: `struct BlockingUrlFetcher {`
  - Purpose: Indexed class `BlockingUrlFetcher` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:23-25]
- `BlockingUrlFetcher` (class) component `BlockingUrlFetcher [class]` (`a0347384-4666-54de-b135-ac6b40f9b3bc`) lines 27-36 [crates/gwiki/src/ingest/url/fetch.rs:27-36]
  - Signature: `impl Default for BlockingUrlFetcher {`
  - Purpose: Indexed class `BlockingUrlFetcher` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:27-36]
- `BlockingUrlFetcher.default` (method) component `BlockingUrlFetcher.default [method]` (`4da23ab2-00d9-5c2d-90e7-bdbbfaae08ab`) lines 28-35 [crates/gwiki/src/ingest/url/fetch.rs:28-35]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `BlockingUrlFetcher.default` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:28-35]
- `BlockingUrlFetcher` (class) component `BlockingUrlFetcher [class]` (`c52f6596-547b-58ec-84d3-2ed0330a062e`) lines 38-111 [crates/gwiki/src/ingest/url/fetch.rs:38-111]
  - Signature: `impl BlockingUrlFetcher {`
  - Purpose: Indexed class `BlockingUrlFetcher` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:38-111]
- `BlockingUrlFetcher.fetch` (method) component `BlockingUrlFetcher.fetch [method]` (`74ea55d8-bf1a-5c27-a16b-9a4c2261649e`) lines 39-110 [crates/gwiki/src/ingest/url/fetch.rs:39-110]
  - Signature: `fn fetch(&self, url: &str, fetched_at: &str) -> Result<UrlSnapshot, UrlIngestFailure> {`
  - Purpose: Indexed method `BlockingUrlFetcher.fetch` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:39-110]
- `content_length_exceeds_limit` (function) component `content_length_exceeds_limit [function]` (`faef89b1-5378-539c-984f-0ef8ae403188`) lines 113-117 [crates/gwiki/src/ingest/url/fetch.rs:113-117]
  - Signature: `pub(super) fn content_length_exceeds_limit(content_length: Option<&str>, max_bytes: u64) -> bool {`
  - Purpose: Indexed function `content_length_exceeds_limit` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:113-117]
- `read_limited_body` (function) component `read_limited_body [function]` (`993bd27b-c1c9-5585-91e9-70d32bdbf9b9`) lines 119-133 [crates/gwiki/src/ingest/url/fetch.rs:119-133]
  - Signature: `pub(super) fn read_limited_body(`
  - Purpose: Indexed function `read_limited_body` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:119-133]
- `response_too_large` (function) component `response_too_large [function]` (`1a1eb760-a5c3-5069-a868-c666ee0860a0`) lines 135-141 [crates/gwiki/src/ingest/url/fetch.rs:135-141]
  - Signature: `fn response_too_large(url: &str, max_bytes: u64) -> UrlIngestFailure {`
  - Purpose: Indexed function `response_too_large` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:135-141]
- `UrlIngestFailure` (class) component `UrlIngestFailure [class]` (`ba89700a-570c-532e-ae04-8bbbf85c728a`) lines 143-174 [crates/gwiki/src/ingest/url/fetch.rs:143-174]
  - Signature: `impl UrlIngestFailure {`
  - Purpose: Indexed class `UrlIngestFailure` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:143-174]
- `UrlIngestFailure.new` (method) component `UrlIngestFailure.new [method]` (`fd4742a0-ffae-518c-be08-1249389f7f5b`) lines 144-154 [crates/gwiki/src/ingest/url/fetch.rs:144-154]
  - Signature: `pub(super) fn new(`
  - Purpose: Indexed method `UrlIngestFailure.new` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:144-154]
- `UrlIngestFailure.from_wiki_error` (method) component `UrlIngestFailure.from_wiki_error [method]` (`6d9002a2-65da-5412-adbe-037bb1d65852`) lines 156-158 [crates/gwiki/src/ingest/url/fetch.rs:156-158]
  - Signature: `pub(super) fn from_wiki_error(url: &str, error: WikiError) -> Self {`
  - Purpose: Indexed method `UrlIngestFailure.from_wiki_error` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:156-158]
- `UrlIngestFailure.http_status` (method) component `UrlIngestFailure.http_status [method]` (`b860735c-6559-593e-8e4b-d97aed891752`) lines 160-173 [crates/gwiki/src/ingest/url/fetch.rs:160-173]
  - Signature: `fn http_status(url: &str, status: u16, response: ureq::Response) -> Self {`
  - Purpose: Indexed method `UrlIngestFailure.http_status` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:160-173]
- `resolve_redirect_url` (function) component `resolve_redirect_url [function]` (`164fc21b-f3a1-53c6-abb2-59431397aec9`) lines 176-185 [crates/gwiki/src/ingest/url/fetch.rs:176-185]
  - Signature: `pub(super) fn resolve_redirect_url(`
  - Purpose: Indexed function `resolve_redirect_url` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:176-185]
- `validate_fetch_url` (function) component `validate_fetch_url [function]` (`532bc610-052c-5468-8247-217911c7af4c`) lines 187-199 [crates/gwiki/src/ingest/url/fetch.rs:187-199]
  - Signature: `fn validate_fetch_url(raw_url: &str) -> Result<(), UrlIngestFailure> {`
  - Purpose: Indexed function `validate_fetch_url` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:187-199]
- `validate_resolved_fetch_url` (function) component `validate_resolved_fetch_url [function]` (`170bc9f5-8062-50c2-a52e-ecd192e32eb5`) lines 201-234 [crates/gwiki/src/ingest/url/fetch.rs:201-234]
  - Signature: `fn validate_resolved_fetch_url(raw_url: &str) -> Result<(), UrlIngestFailure> {`
  - Purpose: Indexed function `validate_resolved_fetch_url` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:201-234]
- `loopback_fetch_allowed_for_tests` (function) component `loopback_fetch_allowed_for_tests [function]` (`5c6426f7-8b96-5698-b993-665b683922b3`) lines 236-240 [crates/gwiki/src/ingest/url/fetch.rs:236-240]
  - Signature: `fn loopback_fetch_allowed_for_tests(ip: IpAddr) -> bool {`
  - Purpose: Indexed function `loopback_fetch_allowed_for_tests` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:236-240]
- `is_disallowed_fetch_ip` (function) component `is_disallowed_fetch_ip [function]` (`0ad1e13f-d8f0-5171-9cb6-a5e746907d48`) lines 242-263 [crates/gwiki/src/ingest/url/fetch.rs:242-263]
  - Signature: `pub(super) fn is_disallowed_fetch_ip(ip: IpAddr) -> bool {`
  - Purpose: Indexed function `is_disallowed_fetch_ip` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:242-263]
- `is_ipv6_unique_local` (function) component `is_ipv6_unique_local [function]` (`f13ed816-63d9-5fea-92de-d6611de7c6e4`) lines 265-267 [crates/gwiki/src/ingest/url/fetch.rs:265-267]
  - Signature: `fn is_ipv6_unique_local(ip: Ipv6Addr) -> bool {`
  - Purpose: Indexed function `is_ipv6_unique_local` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:265-267]
- `is_ipv6_unicast_link_local` (function) component `is_ipv6_unicast_link_local [function]` (`7699f494-2916-5e24-914a-6af2fb9a4546`) lines 269-271 [crates/gwiki/src/ingest/url/fetch.rs:269-271]
  - Signature: `fn is_ipv6_unicast_link_local(ip: Ipv6Addr) -> bool {`
  - Purpose: Indexed function `is_ipv6_unicast_link_local` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:269-271]
- `truncate_message` (function) component `truncate_message [function]` (`19d9739a-21b0-5f11-bf97-3db1b9d6fac3`) lines 273-282 [crates/gwiki/src/ingest/url/fetch.rs:273-282]
  - Signature: `fn truncate_message(message: &str) -> String {`
  - Purpose: Indexed function `truncate_message` in `crates/gwiki/src/ingest/url/fetch.rs`. [crates/gwiki/src/ingest/url/fetch.rs:273-282]

