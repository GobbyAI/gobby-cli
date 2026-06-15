---
title: crates/gwiki/src/registry.rs
type: code_file
provenance:
- file: crates/gwiki/src/registry.rs
  ranges:
  - 15-20
  - 23-26
  - 29-33
  - 35-102
  - 104-136
  - 138-140
  - 142-144
  - 146-184
  - 186-203
  - 205-211
  - 213-225
  - 233-247
  - 250-322
  - 325-333
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/registry.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the serialized registry for wiki scopes and the persistence logic around it. `Registry` stores topic and project registrations in ordered `BTreeMap`s, while `TopicRegistration` and `ProjectRegistration` capture the identifying metadata and filesystem paths for each entry. `register_scope` updates the appropriate map entry for a topic or project, using a file lock from `lock_registry` to serialize access, `read_registry` to load the current JSON state, and `write_registry_atomically` to persist the new registry safely. The remaining helpers build lock and temporary file paths, implement exponential backoff for lock acquisition, and the tests verify backoff behavior, overwrite semantics, and temporary-path uniqueness.
[crates/gwiki/src/registry.rs:15-20]
[crates/gwiki/src/registry.rs:23-26]
[crates/gwiki/src/registry.rs:29-33]
[crates/gwiki/src/registry.rs:35-102]
[crates/gwiki/src/registry.rs:104-136]

## API Symbols

- `Registry` (class) component `Registry [class]` (`ffa5a7e0-cb3e-5a76-b8ca-d5067ec71649`) lines 15-20 [crates/gwiki/src/registry.rs:15-20]
  - Signature: `pub struct Registry {`
  - Purpose: Registry is a serde-serializable container that maintains two ordered maps associating string identifiers to TopicRegistration and ProjectRegistration entries using BTreeMap. [crates/gwiki/src/registry.rs:15-20]
- `TopicRegistration` (class) component `TopicRegistration [class]` (`8e40ba5e-972b-52b7-b0f4-a2155de5c5f6`) lines 23-26 [crates/gwiki/src/registry.rs:23-26]
  - Signature: `pub struct TopicRegistration {`
  - Purpose: `TopicRegistration` is a struct that encapsulates a topic identifier with its associated name and filesystem/resource path. [crates/gwiki/src/registry.rs:23-26]
- `ProjectRegistration` (class) component `ProjectRegistration [class]` (`8e821515-48e4-5609-8eca-ccf4abe9b0ae`) lines 29-33 [crates/gwiki/src/registry.rs:29-33]
  - Signature: `pub struct ProjectRegistration {`
  - Purpose: `ProjectRegistration` is a public struct that encapsulates a project's unique identifier and its associated root and file system paths. [crates/gwiki/src/registry.rs:29-33]
- `register_scope` (function) component `register_scope [function]` (`913bd7b1-eea6-57d4-ae82-08ab9143a4e3`) lines 35-102 [crates/gwiki/src/registry.rs:35-102]
  - Signature: `pub fn register_scope(path: &Path, scope: &ResolvedScope) -> Result<(), WikiError> {`
  - Purpose: Registers a Topic or Project scope to a file-locked registry by reading the current registry, inserting the scope entry, and atomically persisting the updated JSON to disk. [crates/gwiki/src/registry.rs:35-102]
- `lock_registry` (function) component `lock_registry [function]` (`bf4b4791-1644-5aa3-9692-08257e9bb7c6`) lines 104-136 [crates/gwiki/src/registry.rs:104-136]
  - Signature: `fn lock_registry(lock: &std::fs::File, lock_path: &Path) -> Result<(), WikiError> {`
  - Purpose: Acquires an exclusive file lock with exponential backoff retries up to a configured timeout, returning `WikiError` on timeout or lock failure. [crates/gwiki/src/registry.rs:104-136]
- `registry_lock_initial_delay` (function) component `registry_lock_initial_delay [function]` (`3fdca08b-a2a9-5c3f-b4d2-909e09a92169`) lines 138-140 [crates/gwiki/src/registry.rs:138-140]
  - Signature: `fn registry_lock_initial_delay() -> Duration {`
  - Purpose: Returns a Duration of 25 milliseconds to be used as the initial delay for registry lock operations. [crates/gwiki/src/registry.rs:138-140]
- `next_registry_lock_delay` (function) component `next_registry_lock_delay [function]` (`ca2be697-df86-5535-9c02-95c6c0ef4380`) lines 142-144 [crates/gwiki/src/registry.rs:142-144]
  - Signature: `fn next_registry_lock_delay(current: Duration) -> Duration {`
  - Purpose: Doubles the input duration using saturating multiplication and caps the result at a maximum of 250 milliseconds, implementing an exponential backoff with an upper bound. [crates/gwiki/src/registry.rs:142-144]
- `write_registry_atomically` (function) component `write_registry_atomically [function]` (`8a0e38b4-b13e-52ac-9d09-ed1e716d1b7c`) lines 146-184 [crates/gwiki/src/registry.rs:146-184]
  - Signature: `fn write_registry_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Atomically writes byte contents to a file by creating a temporary file, syncing data durability, and atomically renaming it to the target path while also syncing the parent directory. [crates/gwiki/src/registry.rs:146-184]
- `temp_registry_path` (function) component `temp_registry_path [function]` (`50fcb843-622f-577c-8269-bf49f33f465d`) lines 186-203 [crates/gwiki/src/registry.rs:186-203]
  - Signature: `fn temp_registry_path(path: &Path) -> PathBuf {`
  - Purpose: Constructs a unique temporary file path by appending the process ID, an incrementing atomic counter, and current nanosecond timestamp to the original filename in the format `.{filename}.{pid}.{counter}.{nanos}.tmp`. [crates/gwiki/src/registry.rs:186-203]
- `registry_lock_path` (function) component `registry_lock_path [function]` (`f3309c02-5669-59dd-b2cd-1e64f87db993`) lines 205-211 [crates/gwiki/src/registry.rs:205-211]
  - Signature: `fn registry_lock_path(path: &Path) -> PathBuf {`
  - Purpose: Returns a lock file path by appending `.lock` to the input path's filename, defaulting to `wikis.json.lock` if the filename is absent or non-UTF-8. [crates/gwiki/src/registry.rs:205-211]
- `read_registry` (function) component `read_registry [function]` (`c9bbb6e1-870c-5cee-8f69-16b5dd27957d`) lines 213-225 [crates/gwiki/src/registry.rs:213-225]
  - Signature: `fn read_registry(path: &Path) -> Result<Registry, WikiError> {`
  - Purpose: Deserializes a JSON registry from a file path, returning a default Registry if the file is not found, or a WikiError on parse or I/O errors. [crates/gwiki/src/registry.rs:213-225]
- `registry_lock_retry_delay_backs_off_exponentially` (function) component `registry_lock_retry_delay_backs_off_exponentially [function]` (`9017e1eb-0601-517b-b32d-9edcebb55ef5`) lines 233-247 [crates/gwiki/src/registry.rs:233-247]
  - Signature: `fn registry_lock_retry_delay_backs_off_exponentially() {`
  - Purpose: Unit test verifying that registry lock retry delays double exponentially from an initial 25ms until capping at a maximum of 250ms. [crates/gwiki/src/registry.rs:233-247]
- `register_overwrites_existing_entries` (function) component `register_overwrites_existing_entries [function]` (`b311e76f-cde2-5832-a371-69bdc9f75e67`) lines 250-322 [crates/gwiki/src/registry.rs:250-322]
  - Signature: `fn register_overwrites_existing_entries() {`
  - Purpose: Tests that `register_scope` overwrites the path of existing registry entries with matching identifiers while preserving unmodified entries. [crates/gwiki/src/registry.rs:250-322]
- `temp_registry_paths_are_unique_in_registry_directory` (function) component `temp_registry_paths_are_unique_in_registry_directory [function]` (`0a171faf-15fb-58b7-9d1b-224d78da7676`) lines 325-333 [crates/gwiki/src/registry.rs:325-333]
  - Signature: `fn temp_registry_paths_are_unique_in_registry_directory() {`
  - Purpose: Asserts that successive calls to `temp_registry_path()` generate unique temporary paths while maintaining the same parent directory as the input path. [crates/gwiki/src/registry.rs:325-333]

