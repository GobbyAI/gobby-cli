---
title: crates/gcore/src/secrets.rs
type: code_file
provenance:
- file: crates/gcore/src/secrets.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/secrets.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/secrets.rs` exposes 23 indexed API symbols.

## How it fits

`crates/gcore/src/secrets.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `derive_fernet_key` | function | Indexed function `derive_fernet_key` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:18-22] |
| `decrypt_fernet` | function | Indexed function `decrypt_fernet` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:24-30] |
| `resolve_secret` | function | Indexed function `resolve_secret` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:33-63] |
| `resolve_config_value` | function | Indexed function `resolve_config_value` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:66-68] |
| `resolve_config_value_with` | function | Indexed function `resolve_config_value_with` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:70-103] |
| `validate_secret_name` | function | Indexed function `validate_secret_name` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:105-116] |
| `validate_secret_reference_boundary` | function | Indexed function `validate_secret_reference_boundary` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:118-133] |
| `secret_name_byte` | function | Indexed function `secret_name_byte` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:135-137] |
| `secret_boundary_char` | function | Indexed function `secret_boundary_char` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:139-168] |
| `derive_fernet_key_is_deterministic` | function | Indexed function `derive_fernet_key_is_deterministic` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:175-181] |
| `derive_fernet_key_uses_salt` | function | Indexed function `derive_fernet_key_uses_salt` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:184-189] |
| `decrypt_fernet_round_trips` | function | Indexed function `decrypt_fernet_round_trips` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:192-200] |
| `resolve_config_value_expands_embedded_secret` | function | Indexed function `resolve_config_value_expands_embedded_secret` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:203-211] |
| `resolve_config_value_expands_leading_whole_value_secret` | function | Indexed function `resolve_config_value_expands_leading_whole_value_secret` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:214-221] |
| `resolve_config_value_expands_multiple_secrets` | function | Indexed function `resolve_config_value_expands_multiple_secrets` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:224-232] |
| `resolve_config_value_expands_secret_then_environment` | function | Indexed function `resolve_config_value_expands_secret_then_environment` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:236-249] |
| `resolve_config_value_rejects_unresolved_secret` | function | Indexed function `resolve_config_value_rejects_unresolved_secret` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:252-257] |
| `resolve_config_value_rejects_invalid_secret_names` | function | Indexed function `resolve_config_value_rejects_invalid_secret_names` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:260-274] |
| `validate_secret_name_rejects_empty_and_unsupported_names` | function | Indexed function `validate_secret_name_rejects_empty_and_unsupported_names` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:277-282] |
| `resolve_config_value_rejects_unresolved_environment` | function | Indexed function `resolve_config_value_rejects_unresolved_environment` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:285-290] |
| `unresolved_environment_omits_expanded_secret_output` | function | Indexed function `unresolved_environment_omits_expanded_secret_output` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:293-304] |
| `resolve_config_value_plain_value_uses_fast_path` | function | Indexed function `resolve_config_value_plain_value_uses_fast_path` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:307-314] |
| `test_secret_resolver` | function | Indexed function `test_secret_resolver` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:316-324] |

