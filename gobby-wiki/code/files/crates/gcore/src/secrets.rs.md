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

`crates/gcore/src/secrets.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `derive_fernet_key` | function | This function derives a Fernet-compatible cryptographic key by applying PBKDF2-HMAC-SHA256 key derivation (600,000 iterations) to the input machine ID with a provided salt, and returns the resulting 32-byte key as a URL-safe base64-encoded string. [crates/gcore/src/secrets.rs:18-22] |
| `decrypt_fernet` | function | Decrypts a Fernet-encrypted token using the provided key and returns the resulting plaintext as a UTF-8 string, with error handling for invalid keys, failed decryption, and non-UTF-8 output. [crates/gcore/src/secrets.rs:24-30] |
| `resolve_secret` | function | Retrieves an encrypted secret from a database by case-insensitive name lookup and returns the decrypted plaintext using a Fernet key derived from a stored machine ID and salt. [crates/gcore/src/secrets.rs:33-63] |
| `resolve_config_value` | function | Resolves a configuration value string by delegating to 'resolve_config_value_with' with a closure that resolves secrets from the provided database connection. [crates/gcore/src/secrets.rs:66-68] |
| `resolve_config_value_with` | function | Replaces '$secret:NAME' references in a configuration value string using a provided resolver function, then resolves environment variable patterns ('${...}'), and returns an error if any patterns remain unresolved. [crates/gcore/src/secrets.rs:70-103] |
| `validate_secret_name` | function | Validates a secret name string by ensuring it is non-empty, does not exceed 'SECRET_NAME_MAX_LEN' characters, and contains only bytes that satisfy the 'secret_name_byte' predicate, returning an 'anyhow::Result'. [crates/gcore/src/secrets.rs:105-116] |
| `validate_secret_reference_boundary` | function | This function validates that a secret reference within a string has a proper boundary by ensuring the character immediately following the secret reference name is either absent, a boundary character, or the start of another secret syntax marker. [crates/gcore/src/secrets.rs:118-133] |
| `secret_name_byte` | function | This function returns 'true' if the input byte is an ASCII alphanumeric character or one of the special characters: underscore, hyphen, or period. [crates/gcore/src/secrets.rs:135-137] |
| `secret_boundary_char` | function | Returns true if the input character is either ASCII whitespace or one of the reserved special characters commonly used as delimiters and separators. [crates/gcore/src/secrets.rs:139-168] |
| `test_secret_resolver` | function | This function resolves one of four hardcoded secret values based on the input name parameter, returning an 'anyhow::Result' containing the corresponding string or an error for unmatched inputs. [crates/gcore/src/secrets.rs:316-324] |

_Verified by 13 in-file unit tests._

