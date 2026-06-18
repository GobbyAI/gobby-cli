---
title: crates/ghook/src/transport.rs
type: code_file
provenance:
- file: crates/ghook/src/transport.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/transport.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/transport.rs` exposes 23 indexed API symbols.

## How it fits

`crates/ghook/src/transport.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DeliveryOutcome` | type | Indexed type `DeliveryOutcome` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:31-36] |
| `DeliveryFailureKind` | type | Indexed type `DeliveryFailureKind` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:40-45] |
| `DeliveryReport` | class | Indexed class `DeliveryReport` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:49-55] |
| `inbox_dir` | function | Indexed function `inbox_dir` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:58-60] |
| `quarantine_dir` | function | Indexed function `quarantine_dir` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:63-65] |
| `ts13` | function | Indexed function `ts13` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:68-74] |
| `envelope_filename` | function | Indexed function `envelope_filename` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:77-81] |
| `atomic_write` | function | Indexed function `atomic_write` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:87-114] |
| `enqueue_to` | function | Indexed function `enqueue_to` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:119-125] |
| `envelope_id_from_path` | function | Indexed function `envelope_id_from_path` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:127-129] |
| `post_and_cleanup` | function | Indexed function `post_and_cleanup` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:137-204] |
| `classify_transport_error` | function | Indexed function `classify_transport_error` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:206-221] |
| `quarantine_malformed` | function | Indexed function `quarantine_malformed` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:225-232] |
| `quarantine_malformed_at` | function | Indexed function `quarantine_malformed_at` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:242-273] |
| `ts13_is_13_digits` | function | Indexed function `ts13_is_13_digits` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:286-290] |
| `filename_prefix_reflects_critical` | function | Indexed function `filename_prefix_reflects_critical` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:293-296] |
| `atomic_write_creates_parent_dirs` | function | Indexed function `atomic_write_creates_parent_dirs` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:299-305] |
| `atomic_write_leaves_no_tmp_on_success` | function | Indexed function `atomic_write_leaves_no_tmp_on_success` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:308-314] |
| `enqueue_writes_envelope_to_inbox` | function | Indexed function `enqueue_writes_envelope_to_inbox` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:317-332] |
| `quarantine_writes_pair` | function | Indexed function `quarantine_writes_pair` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:335-348] |
| `post_and_cleanup_captures_success_response_body` | function | Indexed function `post_and_cleanup_captures_success_response_body` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:351-404] |
| `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint` | function | Indexed function `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:407-458] |
| `post_and_cleanup_captures_http_error_body` | function | Indexed function `post_and_cleanup_captures_http_error_body` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:461-493] |

