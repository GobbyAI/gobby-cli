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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/registry.rs:15-20](crates/gwiki/src/registry.rs#L15-L20), [crates/gwiki/src/registry.rs:23-26](crates/gwiki/src/registry.rs#L23-L26), [crates/gwiki/src/registry.rs:29-33](crates/gwiki/src/registry.rs#L29-L33), [crates/gwiki/src/registry.rs:35-102](crates/gwiki/src/registry.rs#L35-L102), [crates/gwiki/src/registry.rs:104-136](crates/gwiki/src/registry.rs#L104-L136), [crates/gwiki/src/registry.rs:138-140](crates/gwiki/src/registry.rs#L138-L140), [crates/gwiki/src/registry.rs:142-144](crates/gwiki/src/registry.rs#L142-L144), [crates/gwiki/src/registry.rs:146-184](crates/gwiki/src/registry.rs#L146-L184), [crates/gwiki/src/registry.rs:186-203](crates/gwiki/src/registry.rs#L186-L203), [crates/gwiki/src/registry.rs:205-211](crates/gwiki/src/registry.rs#L205-L211), [crates/gwiki/src/registry.rs:213-225](crates/gwiki/src/registry.rs#L213-L225), [crates/gwiki/src/registry.rs:233-247](crates/gwiki/src/registry.rs#L233-L247), [crates/gwiki/src/registry.rs:250-322](crates/gwiki/src/registry.rs#L250-L322), [crates/gwiki/src/registry.rs:325-333](crates/gwiki/src/registry.rs#L325-L333)

</details>

# crates/gwiki/src/registry.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the persistent wiki registry data model and the file-locking update path for it. `Registry` stores topic and project registrations in `BTreeMap`s keyed by name or project ID, while `TopicRegistration` and `ProjectRegistration` record the registered identifiers plus their source and resolved paths. `register_scope` loads the current registry, updates the appropriate entry for a `ResolvedScope`, and writes it back safely. The helper functions handle the supporting file mechanics: `lock_registry` waits on a lock file with retry backoff, `write_registry_atomically` stages writes through a temporary file before replacing the registry, `read_registry` deserializes the on-disk state, and the path helpers build the lock and temp-file locations. The tests cover overwrite behavior, unique temp paths, and exponential lock retry timing.
[crates/gwiki/src/registry.rs:15-20]
[crates/gwiki/src/registry.rs:23-26]
[crates/gwiki/src/registry.rs:29-33]
[crates/gwiki/src/registry.rs:35-102]
[crates/gwiki/src/registry.rs:104-136]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Registry` | class | `pub struct Registry {` | `Registry [class]` | `ffa5a7e0-cb3e-5a76-b8ca-d5067ec71649` | 15-20 [crates/gwiki/src/registry.rs:15-20] | Indexed class `Registry` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:15-20] |
| `TopicRegistration` | class | `pub struct TopicRegistration {` | `TopicRegistration [class]` | `8e40ba5e-972b-52b7-b0f4-a2155de5c5f6` | 23-26 [crates/gwiki/src/registry.rs:23-26] | Indexed class `TopicRegistration` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:23-26] |
| `ProjectRegistration` | class | `pub struct ProjectRegistration {` | `ProjectRegistration [class]` | `8e821515-48e4-5609-8eca-ccf4abe9b0ae` | 29-33 [crates/gwiki/src/registry.rs:29-33] | Indexed class `ProjectRegistration` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:29-33] |
| `register_scope` | function | `pub fn register_scope(path: &Path, scope: &ResolvedScope) -> Result<(), WikiError> {` | `register_scope [function]` | `913bd7b1-eea6-57d4-ae82-08ab9143a4e3` | 35-102 [crates/gwiki/src/registry.rs:35-102] | Indexed function `register_scope` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:35-102] |
| `lock_registry` | function | `fn lock_registry(lock: &std::fs::File, lock_path: &Path) -> Result<(), WikiError> {` | `lock_registry [function]` | `bf4b4791-1644-5aa3-9692-08257e9bb7c6` | 104-136 [crates/gwiki/src/registry.rs:104-136] | Indexed function `lock_registry` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:104-136] |
| `registry_lock_initial_delay` | function | `fn registry_lock_initial_delay() -> Duration {` | `registry_lock_initial_delay [function]` | `3fdca08b-a2a9-5c3f-b4d2-909e09a92169` | 138-140 [crates/gwiki/src/registry.rs:138-140] | Indexed function `registry_lock_initial_delay` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:138-140] |
| `next_registry_lock_delay` | function | `fn next_registry_lock_delay(current: Duration) -> Duration {` | `next_registry_lock_delay [function]` | `ca2be697-df86-5535-9c02-95c6c0ef4380` | 142-144 [crates/gwiki/src/registry.rs:142-144] | Indexed function `next_registry_lock_delay` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:142-144] |
| `write_registry_atomically` | function | `fn write_registry_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {` | `write_registry_atomically [function]` | `8a0e38b4-b13e-52ac-9d09-ed1e716d1b7c` | 146-184 [crates/gwiki/src/registry.rs:146-184] | Indexed function `write_registry_atomically` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:146-184] |
| `temp_registry_path` | function | `fn temp_registry_path(path: &Path) -> PathBuf {` | `temp_registry_path [function]` | `50fcb843-622f-577c-8269-bf49f33f465d` | 186-203 [crates/gwiki/src/registry.rs:186-203] | Indexed function `temp_registry_path` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:186-203] |
| `registry_lock_path` | function | `fn registry_lock_path(path: &Path) -> PathBuf {` | `registry_lock_path [function]` | `f3309c02-5669-59dd-b2cd-1e64f87db993` | 205-211 [crates/gwiki/src/registry.rs:205-211] | Indexed function `registry_lock_path` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:205-211] |
| `read_registry` | function | `fn read_registry(path: &Path) -> Result<Registry, WikiError> {` | `read_registry [function]` | `c9bbb6e1-870c-5cee-8f69-16b5dd27957d` | 213-225 [crates/gwiki/src/registry.rs:213-225] | Indexed function `read_registry` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:213-225] |
| `registry_lock_retry_delay_backs_off_exponentially` | function | `fn registry_lock_retry_delay_backs_off_exponentially() {` | `registry_lock_retry_delay_backs_off_exponentially [function]` | `9017e1eb-0601-517b-b32d-9edcebb55ef5` | 233-247 [crates/gwiki/src/registry.rs:233-247] | Indexed function `registry_lock_retry_delay_backs_off_exponentially` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:233-247] |
| `register_overwrites_existing_entries` | function | `fn register_overwrites_existing_entries() {` | `register_overwrites_existing_entries [function]` | `b311e76f-cde2-5832-a371-69bdc9f75e67` | 250-322 [crates/gwiki/src/registry.rs:250-322] | Indexed function `register_overwrites_existing_entries` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:250-322] |
| `temp_registry_paths_are_unique_in_registry_directory` | function | `fn temp_registry_paths_are_unique_in_registry_directory() {` | `temp_registry_paths_are_unique_in_registry_directory [function]` | `0a171faf-15fb-58b7-9d1b-224d78da7676` | 325-333 [crates/gwiki/src/registry.rs:325-333] | Indexed function `temp_registry_paths_are_unique_in_registry_directory` in `crates/gwiki/src/registry.rs`. [crates/gwiki/src/registry.rs:325-333] |
