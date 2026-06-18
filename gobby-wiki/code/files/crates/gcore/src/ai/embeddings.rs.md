---
title: crates/gcore/src/ai/embeddings.rs
type: code_file
provenance:
- file: crates/gcore/src/ai/embeddings.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai/embeddings.rs

Module: [[code/modules/crates/gcore/src/ai|crates/gcore/src/ai]]

## Overview

`crates/gcore/src/ai/embeddings.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gcore/src/ai/embeddings.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `embed_one` | function | Indexed function `embed_one` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:19-38] |
| `embed_batch` | function | Indexed function `embed_batch` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:42-92] |
| `send_request` | function | Indexed function `send_request` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:94-105] |
| `parse_embedding` | function | Indexed function `parse_embedding` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:107-133] |
| `config` | function | Indexed function `config` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:140-148] |
| `embed_one_sends_string_input_with_bearer_auth` | function | Indexed function `embed_one_sends_string_input_with_bearer_auth` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:151-166] |
| `embed_batch_sends_array_input_and_reorders_by_index` | function | Indexed function `embed_batch_sends_array_input_and_reorders_by_index` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:169-190] |
| `embed_batch_with_no_inputs_skips_the_request` | function | Indexed function `embed_batch_with_no_inputs_skips_the_request` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:193-197] |
| `embed_batch_rejects_vector_count_mismatch` | function | Indexed function `embed_batch_rejects_vector_count_mismatch` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:200-217] |
| `embed_batch_rejects_duplicate_index` | function | Indexed function `embed_batch_rejects_duplicate_index` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:220-242] |
| `non_success_status_surfaces_status_and_body` | function | Indexed function `non_success_status_surfaces_status_and_body` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:245-258] |
| `non_numeric_embedding_values_are_rejected` | function | Indexed function `non_numeric_embedding_values_are_rejected` in `crates/gcore/src/ai/embeddings.rs`. [crates/gcore/src/ai/embeddings.rs:261-273] |

