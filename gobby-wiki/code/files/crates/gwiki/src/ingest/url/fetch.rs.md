---
title: crates/gwiki/src/ingest/url/fetch.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/url/fetch.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/url/fetch.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/url/fetch.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/url/fetch.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `fetch_url_snapshot` | function | The 'fetch_url_snapshot' function synchronously retrieves a snapshot of a given URL at a specified timestamp using a default 'BlockingUrlFetcher' instance, returning a 'Result' containing either a 'UrlSnapshot' or a 'UrlIngestFailure'. [crates/gwiki/src/ingest/url/fetch.rs:15-20] |
| `BlockingUrlFetcher` | class | 'BlockingUrlFetcher' is a synchronous HTTP client wrapper that manages network requests using an underlying 'ureq::Agent'. [crates/gwiki/src/ingest/url/fetch.rs:23-25] |
| `BlockingUrlFetcher::default` | method | The 'default' method constructs an instance of 'Self' containing a 'ureq' HTTP client agent configured with zero redirects and a timeout set to 'URL_FETCH_TIMEOUT'. [crates/gwiki/src/ingest/url/fetch.rs:28-35] |
| `BlockingUrlFetcher::fetch` | method | The 'fetch' method validates and executes an HTTP GET request for a specified URL, sequentially resolving and validating redirect locations up to 'MAX_REDIRECTS' times, to return a 'Result' containing either a 'UrlSnapshot' or a 'UrlIngestFailure'. [crates/gwiki/src/ingest/url/fetch.rs:39-110] |
| `content_length_exceeds_limit` | function | This function parses an optional string slice representation of a content length as a 64-bit unsigned integer and returns true if the parsed value successfully exceeds the specified maximum byte limit, and false otherwise. [crates/gwiki/src/ingest/url/fetch.rs:113-117] |
| `read_limited_body` | function | The 'read_limited_body' function reads bytes from a reader into a vector, enforcing a size limit of 'max_bytes' and returning a 'UrlIngestFailure' if a read error occurs or if the consumed data exceeds the specified limit. [crates/gwiki/src/ingest/url/fetch.rs:119-133] |
| `response_too_large` | function | The 'response_too_large' function instantiates and returns a 'UrlIngestFailure' indicating that the response payload for a given URL exceeded the specified maximum byte limit. [crates/gwiki/src/ingest/url/fetch.rs:135-141] |
| `UrlIngestFailure::new` | method | This package-private constructor initializes and returns a new instance of the struct, converting the provided 'url', 'code', and 'message' arguments of any type implementing 'Into<String>' into owned 'String' fields. [crates/gwiki/src/ingest/url/fetch.rs:144-154] |
| `UrlIngestFailure::from_wiki_error` | method | The 'from_wiki_error' method constructs a new instance of the implementing type by invoking 'Self::new' with the provided URL, the error code, and the string representation of the 'WikiError'. [crates/gwiki/src/ingest/url/fetch.rs:156-158] |
| `UrlIngestFailure::http_status` | method | The 'http_status' method constructs an instance of 'Self' by reading up to a specified byte limit from an HTTP response body, converting it to a truncated single-line UTF-8 string, and formatting a detail message that combines the HTTP status code with the response body content or read error. [crates/gwiki/src/ingest/url/fetch.rs:160-173] |
| `resolve_redirect_url` | function | The 'resolve_redirect_url' function parses a base URL and joins it with a redirect location to resolve and return the absolute redirect URL, returning a 'UrlIngestFailure' if either the base URL or the joint redirect URL is invalid. [crates/gwiki/src/ingest/url/fetch.rs:176-185] |
| `validate_fetch_url` | function | The 'validate_fetch_url' function parses a raw URL string and validates that its scheme is either HTTP or HTTPS, returning 'Ok(())' on success or a 'UrlIngestFailure' error if the URL is invalid or the scheme is unsupported. [crates/gwiki/src/ingest/url/fetch.rs:187-199] |
| `validate_resolved_fetch_url` | function | The function parses a raw URL, resolves its host and port to IP addresses via DNS, and verifies that none of the resolved IPs are disallowed (with an exception for loopback addresses in tests), returning 'Ok(())' if valid or a 'UrlIngestFailure' error on failure. [crates/gwiki/src/ingest/url/fetch.rs:201-234] |
| `loopback_fetch_allowed_for_tests` | function | This function returns 'true' if debug assertions are enabled, the specified IP address is a loopback address, and the 'GWIKI_ALLOW_LOOPBACK_URL_FETCH_FOR_TESTS' environment variable is set. [crates/gwiki/src/ingest/url/fetch.rs:236-240] |
| `is_disallowed_fetch_ip` | function | This function determines whether a given IPv4 or IPv6 address is disallowed for fetching by checking if it belongs to private, loopback, link-local (including the 169.254.169.254 metadata address), multicast, unspecified, or unique local IP address ranges. [crates/gwiki/src/ingest/url/fetch.rs:242-263] |
| `is_ipv6_unique_local` | function | The 'is_ipv6_unique_local' function determines whether a given IPv6 address is a unique local address by checking if the 7 most significant bits of its first 16-bit segment match the 'fc00::/7' prefix. [crates/gwiki/src/ingest/url/fetch.rs:265-267] |
| `is_ipv6_unicast_link_local` | function | This function checks if a given IPv6 address is a unicast link-local address by verifying if its first 16-bit segment falls within the 'fe80::/10' prefix range. [crates/gwiki/src/ingest/url/fetch.rs:269-271] |
| `truncate_message` | function | The 'truncate_message' function truncates a string slice to its first 200 characters, returning it as a new 'String' with an appended ellipsis if the original input contains additional characters. [crates/gwiki/src/ingest/url/fetch.rs:273-282] |

