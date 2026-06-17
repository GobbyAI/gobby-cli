---
title: crates/gcore/src/provisioning/tests.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/tests.rs
  ranges:
  - 5-7
  - 10-18
  - 20-34
  - 38-40
  - 43-46
  - 49-87
  - 90-102
  - 105-123
  - 126-153
  - 156-170
  - 173-185
  - 188-204
  - 207-226
  - 229-251
  - 253-261
  - 264-288
  - 291-328
  - 331-340
  - 342-357
  - 360-397
  - 400-454
  - 457-488
  - 491-521
  - 524-577
  - 580-620
  - 623-686
  - 689-721
  - 724-726
  - 729-736
  - 740-743
  - 746-750
  - 752-756
  - 758-762
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/provisioning/tests.rs:5-7](crates/gcore/src/provisioning/tests.rs#L5-L7), [crates/gcore/src/provisioning/tests.rs:10-18](crates/gcore/src/provisioning/tests.rs#L10-L18), [crates/gcore/src/provisioning/tests.rs:20-34](crates/gcore/src/provisioning/tests.rs#L20-L34), [crates/gcore/src/provisioning/tests.rs:38-40](crates/gcore/src/provisioning/tests.rs#L38-L40), [crates/gcore/src/provisioning/tests.rs:43-46](crates/gcore/src/provisioning/tests.rs#L43-L46), [crates/gcore/src/provisioning/tests.rs:49-87](crates/gcore/src/provisioning/tests.rs#L49-L87), [crates/gcore/src/provisioning/tests.rs:90-102](crates/gcore/src/provisioning/tests.rs#L90-L102), [crates/gcore/src/provisioning/tests.rs:105-123](crates/gcore/src/provisioning/tests.rs#L105-L123), [crates/gcore/src/provisioning/tests.rs:126-153](crates/gcore/src/provisioning/tests.rs#L126-L153), [crates/gcore/src/provisioning/tests.rs:156-170](crates/gcore/src/provisioning/tests.rs#L156-L170), [crates/gcore/src/provisioning/tests.rs:173-185](crates/gcore/src/provisioning/tests.rs#L173-L185), [crates/gcore/src/provisioning/tests.rs:188-204](crates/gcore/src/provisioning/tests.rs#L188-L204), [crates/gcore/src/provisioning/tests.rs:207-226](crates/gcore/src/provisioning/tests.rs#L207-L226), [crates/gcore/src/provisioning/tests.rs:229-251](crates/gcore/src/provisioning/tests.rs#L229-L251), [crates/gcore/src/provisioning/tests.rs:253-261](crates/gcore/src/provisioning/tests.rs#L253-L261), [crates/gcore/src/provisioning/tests.rs:264-288](crates/gcore/src/provisioning/tests.rs#L264-L288), [crates/gcore/src/provisioning/tests.rs:291-328](crates/gcore/src/provisioning/tests.rs#L291-L328), [crates/gcore/src/provisioning/tests.rs:331-340](crates/gcore/src/provisioning/tests.rs#L331-L340), [crates/gcore/src/provisioning/tests.rs:342-357](crates/gcore/src/provisioning/tests.rs#L342-L357), [crates/gcore/src/provisioning/tests.rs:360-397](crates/gcore/src/provisioning/tests.rs#L360-L397), [crates/gcore/src/provisioning/tests.rs:400-454](crates/gcore/src/provisioning/tests.rs#L400-L454), [crates/gcore/src/provisioning/tests.rs:457-488](crates/gcore/src/provisioning/tests.rs#L457-L488), [crates/gcore/src/provisioning/tests.rs:491-521](crates/gcore/src/provisioning/tests.rs#L491-L521), [crates/gcore/src/provisioning/tests.rs:524-577](crates/gcore/src/provisioning/tests.rs#L524-L577), [crates/gcore/src/provisioning/tests.rs:580-620](crates/gcore/src/provisioning/tests.rs#L580-L620), [crates/gcore/src/provisioning/tests.rs:623-686](crates/gcore/src/provisioning/tests.rs#L623-L686), [crates/gcore/src/provisioning/tests.rs:689-721](crates/gcore/src/provisioning/tests.rs#L689-L721), [crates/gcore/src/provisioning/tests.rs:724-726](crates/gcore/src/provisioning/tests.rs#L724-L726), [crates/gcore/src/provisioning/tests.rs:729-736](crates/gcore/src/provisioning/tests.rs#L729-L736), [crates/gcore/src/provisioning/tests.rs:740-743](crates/gcore/src/provisioning/tests.rs#L740-L743), [crates/gcore/src/provisioning/tests.rs:746-750](crates/gcore/src/provisioning/tests.rs#L746-L750), [crates/gcore/src/provisioning/tests.rs:752-756](crates/gcore/src/provisioning/tests.rs#L752-L756), [crates/gcore/src/provisioning/tests.rs:758-762](crates/gcore/src/provisioning/tests.rs#L758-L762)

</details>

# crates/gcore/src/provisioning/tests.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Purpose

This file is the test suite for `gcore` provisioning logic, covering YAML config parsing/writing, service-stack setup, compose template handling, Docker provisioning, hub reuse and conflict detection, and environment/database URL rules. It also defines small test helpers: `EnvGuard` serializes and clears provisioning-related environment variables around tests, `write_services_stack` creates a minimal services directory and compose file fixture, and the `RecordingRunner`/`RecordingHealth` types capture runner and health-check calls for assertions.
[crates/gcore/src/provisioning/tests.rs:5-7]
[crates/gcore/src/provisioning/tests.rs:10-18]
[crates/gcore/src/provisioning/tests.rs:20-34]
[crates/gcore/src/provisioning/tests.rs:38-40]
[crates/gcore/src/provisioning/tests.rs:43-46]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `EnvGuard` | class | `struct EnvGuard {` | `EnvGuard [class]` | `b7e17b70-74b9-5491-b283-50ea559f94cb` | 5-7 [crates/gcore/src/provisioning/tests.rs:5-7] | Indexed class `EnvGuard` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:5-7] |
| `EnvGuard::new` | method | `fn new() -> Self {` | `EnvGuard::new [method]` | `614c9763-f589-52a4-bd68-add3498fa73f` | 10-18 [crates/gcore/src/provisioning/tests.rs:10-18] | Indexed method `EnvGuard::new` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:10-18] |
| `EnvGuard::clear` | method | `fn clear(&self) {` | `EnvGuard::clear [method]` | `5a80db9e-185c-5aa1-a48c-ceddef5c8931` | 20-34 [crates/gcore/src/provisioning/tests.rs:20-34] | Indexed method `EnvGuard::clear` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:20-34] |
| `EnvGuard::drop` | method | `fn drop(&mut self) {` | `EnvGuard::drop [method]` | `0974fba8-549c-5e67-89e3-a96aa4b0a85b` | 38-40 [crates/gcore/src/provisioning/tests.rs:38-40] | Indexed method `EnvGuard::drop` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:38-40] |
| `write_services_stack` | function | `fn write_services_stack(home: &Path) {` | `write_services_stack [function]` | `3a1d922a-7aa6-5d16-8fac-0dd37efa0d4f` | 43-46 [crates/gcore/src/provisioning/tests.rs:43-46] | Indexed function `write_services_stack` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:43-46] |
| `gcore_yaml_reads_flat_and_nested_keys` | function | `fn gcore_yaml_reads_flat_and_nested_keys() {` | `gcore_yaml_reads_flat_and_nested_keys [function]` | `b9b78d7c-f07d-5dc0-a3be-b52f209d0ec0` | 49-87 [crates/gcore/src/provisioning/tests.rs:49-87] | Indexed function `gcore_yaml_reads_flat_and_nested_keys` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:49-87] |
| `gcore_yaml_reads_dotted_mapping_prefixes` | function | `fn gcore_yaml_reads_dotted_mapping_prefixes() {` | `gcore_yaml_reads_dotted_mapping_prefixes [function]` | `91097697-4e43-5851-8c88-a21fcbd13c7d` | 90-102 [crates/gcore/src/provisioning/tests.rs:90-102] | Indexed function `gcore_yaml_reads_dotted_mapping_prefixes` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:90-102] |
| `gcore_yaml_text_generation_defaults_do_not_override_explicit_values` | function | `fn gcore_yaml_text_generation_defaults_do_not_override_explicit_values() {` | `gcore_yaml_text_generation_defaults_do_not_override_explicit_values [function]` | `7d0143a7-b3b3-5898-83b8-8e7ef5fa0e56` | 105-123 [crates/gcore/src/provisioning/tests.rs:105-123] | Indexed function `gcore_yaml_text_generation_defaults_do_not_override_explicit_values` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:105-123] |
| `gcore_yaml_writes_nested_keys` | function | `fn gcore_yaml_writes_nested_keys() {` | `gcore_yaml_writes_nested_keys [function]` | `e32f1bef-994f-5099-8207-295a805d62d3` | 126-153 [crates/gcore/src/provisioning/tests.rs:126-153] | Indexed function `gcore_yaml_writes_nested_keys` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:126-153] |
| `gcore_yaml_write_rejects_scalar_to_nested_mapping_collision` | function | `fn gcore_yaml_write_rejects_scalar_to_nested_mapping_collision() {` | `gcore_yaml_write_rejects_scalar_to_nested_mapping_collision [function]` | `e818c456-ec19-5b3b-9eeb-8fd0611d44c3` | 156-170 [crates/gcore/src/provisioning/tests.rs:156-170] | Indexed function `gcore_yaml_write_rejects_scalar_to_nested_mapping_collision` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:156-170] |
| `gcore_yaml_rejects_excessive_nesting` | function | `fn gcore_yaml_rejects_excessive_nesting() {` | `gcore_yaml_rejects_excessive_nesting [function]` | `e4102b85-5fb4-549e-b722-f319dd1bb2ba` | 173-185 [crates/gcore/src/provisioning/tests.rs:173-185] | Indexed function `gcore_yaml_rejects_excessive_nesting` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:173-185] |
| `gcore_yaml_rejects_sequence_scalar_values` | function | `fn gcore_yaml_rejects_sequence_scalar_values() {` | `gcore_yaml_rejects_sequence_scalar_values [function]` | `b9c534c8-ef8c-532c-8c68-4c522052371f` | 188-204 [crates/gcore/src/provisioning/tests.rs:188-204] | Indexed function `gcore_yaml_rejects_sequence_scalar_values` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:188-204] |
| `gcore_yaml_stringifies_tagged_scalar_values` | function | `fn gcore_yaml_stringifies_tagged_scalar_values() {` | `gcore_yaml_stringifies_tagged_scalar_values [function]` | `1655eb43-66f1-5b63-ada3-332703c8af55` | 207-226 [crates/gcore/src/provisioning/tests.rs:207-226] | Indexed function `gcore_yaml_stringifies_tagged_scalar_values` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:207-226] |
| `gcore_yaml_stringifies_tagged_sequence_values` | function | `fn gcore_yaml_stringifies_tagged_sequence_values() {` | `gcore_yaml_stringifies_tagged_sequence_values [function]` | `a8b6fac1-714b-53bb-b9c0-14986b855aac` | 229-251 [crates/gcore/src/provisioning/tests.rs:229-251] | Indexed function `gcore_yaml_stringifies_tagged_sequence_values` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:229-251] |
| `nested_yaml_str` | function | `fn nested_yaml_str<'a>(value: &'a serde_yaml::Value, path: &[&str]) -> Option<&'a str> {` | `nested_yaml_str [function]` | `e01638fa-ded9-560c-b711-1028e648a8fe` | 253-261 [crates/gcore/src/provisioning/tests.rs:253-261] | Indexed function `nested_yaml_str` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:253-261] |
| `standalone_config_resolves_service_keys_and_plain_api_key` | function | `fn standalone_config_resolves_service_keys_and_plain_api_key() {` | `standalone_config_resolves_service_keys_and_plain_api_key [function]` | `43396126-529f-52bd-b828-67434dc6b5c4` | 264-288 [crates/gcore/src/provisioning/tests.rs:264-288] | Indexed function `standalone_config_resolves_service_keys_and_plain_api_key` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:264-288] |
| `writes_ai_embeddings_standalone_api_key` | function | `fn writes_ai_embeddings_standalone_api_key() {` | `writes_ai_embeddings_standalone_api_key [function]` | `776e685b-0747-5e25-8991-4b9443fe6e67` | 291-328 [crates/gcore/src/provisioning/tests.rs:291-328] | Indexed function `writes_ai_embeddings_standalone_api_key` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:291-328] |
| `compose_template_matches_daemon_checkout_when_present` | function | `fn compose_template_matches_daemon_checkout_when_present() {` | `compose_template_matches_daemon_checkout_when_present [function]` | `71a595b0-1cdb-5718-b64a-53b62bcd83f4` | 331-340 [crates/gcore/src/provisioning/tests.rs:331-340] | Indexed function `compose_template_matches_daemon_checkout_when_present` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:331-340] |
| `daemon_compose_template_path` | function | `fn daemon_compose_template_path() -> Option<PathBuf> {` | `daemon_compose_template_path [function]` | `d57bc87f-c47d-58fb-88dd-847fcc8ca589` | 342-357 [crates/gcore/src/provisioning/tests.rs:342-357] | Indexed function `daemon_compose_template_path` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:342-357] |
| `docker_provisioning_prepares_assets_runs_compose_and_health_checks` | function | `fn docker_provisioning_prepares_assets_runs_compose_and_health_checks() {` | `docker_provisioning_prepares_assets_runs_compose_and_health_checks [function]` | `8bb076a0-6a74-51d7-9e16-5ecab78699c4` | 360-397 [crates/gcore/src/provisioning/tests.rs:360-397] | Indexed function `docker_provisioning_prepares_assets_runs_compose_and_health_checks` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:360-397] |
| `ensure_hub_reuses_then_provisions` | function | `fn ensure_hub_reuses_then_provisions() {` | `ensure_hub_reuses_then_provisions [function]` | `7e890fb0-00bd-53a9-bfd5-b482c217fd8d` | 400-454 [crates/gcore/src/provisioning/tests.rs:400-454] | Indexed function `ensure_hub_reuses_then_provisions` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:400-454] |
| `gcore_yaml_database_url_requires_services_stack` | function | `fn gcore_yaml_database_url_requires_services_stack() {` | `gcore_yaml_database_url_requires_services_stack [function]` | `77ec29fc-8bad-5ee6-ae6b-f70d7513a544` | 457-488 [crates/gcore/src/provisioning/tests.rs:457-488] | Indexed function `gcore_yaml_database_url_requires_services_stack` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:457-488] |
| `no_double_provision_when_reachable` | function | `fn no_double_provision_when_reachable() {` | `no_double_provision_when_reachable [function]` | `9687425f-ffe8-5efc-a9e1-8d7b1f4d089b` | 491-521 [crates/gcore/src/provisioning/tests.rs:491-521] | Indexed function `no_double_provision_when_reachable` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:491-521] |
| `divergent_hubs_surface_conflict` | function | `fn divergent_hubs_surface_conflict() {` | `divergent_hubs_surface_conflict [function]` | `4477bbf7-268e-56cd-abea-b9f4df8357d7` | 524-577 [crates/gcore/src/provisioning/tests.rs:524-577] | Indexed function `divergent_hubs_surface_conflict` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:524-577] |
| `reachable_env_database_url_conflicts_with_recorded_hub` | function | `fn reachable_env_database_url_conflicts_with_recorded_hub() {` | `reachable_env_database_url_conflicts_with_recorded_hub [function]` | `07833f10-068e-5e4c-9cbb-501cc21852c4` | 580-620 [crates/gcore/src/provisioning/tests.rs:580-620] | Indexed function `reachable_env_database_url_conflicts_with_recorded_hub` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:580-620] |
| `insufficient_identity_privilege_preserves_hub` | function | `fn insufficient_identity_privilege_preserves_hub() {` | `insufficient_identity_privilege_preserves_hub [function]` | `76c7e6d7-2fc0-546b-a1be-a10c3e662a6b` | 623-686 [crates/gcore/src/provisioning/tests.rs:623-686] | Indexed function `insufficient_identity_privilege_preserves_hub` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:623-686] |
| `override_plus_recorded_hub_preserves_recorded_when_identity_unknown` | function | `fn override_plus_recorded_hub_preserves_recorded_when_identity_unknown() {` | `override_plus_recorded_hub_preserves_recorded_when_identity_unknown [function]` | `425fc682-5c68-50f6-aa20-3d99065ad1dc` | 689-721 [crates/gcore/src/provisioning/tests.rs:689-721] | Indexed function `override_plus_recorded_hub_preserves_recorded_when_identity_unknown` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:689-721] |
| `RecordingRunner` | class | `struct RecordingRunner {` | `RecordingRunner [class]` | `0095ebba-9ba1-5840-be22-ca5b056e6dae` | 724-726 [crates/gcore/src/provisioning/tests.rs:724-726] | Indexed class `RecordingRunner` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:724-726] |
| `RecordingRunner::run` | method | `fn run(&mut self, spec: &CommandSpec) -> std::io::Result<CommandOutput> {` | `RecordingRunner::run [method]` | `0cecda10-bf18-566d-962c-179e39957c5c` | 729-736 [crates/gcore/src/provisioning/tests.rs:729-736] | Indexed method `RecordingRunner::run` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:729-736] |
| `RecordingHealth` | class | `struct RecordingHealth {` | `RecordingHealth [class]` | `5792bfa5-e3db-535d-b089-cb148fe5592e` | 740-743 [crates/gcore/src/provisioning/tests.rs:740-743] | Indexed class `RecordingHealth` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:740-743] |
| `RecordingHealth::wait_postgres` | method | `fn wait_postgres(&mut self, host: &str, port: u16) -> anyhow::Result<()> {` | `RecordingHealth::wait_postgres [method]` | `15b11fd9-8d89-58ea-937c-cfbba601943f` | 746-750 [crates/gcore/src/provisioning/tests.rs:746-750] | Indexed method `RecordingHealth::wait_postgres` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:746-750] |
| `RecordingHealth::wait_qdrant` | method | `fn wait_qdrant(&mut self, host: &str, port: u16) -> anyhow::Result<()> {` | `RecordingHealth::wait_qdrant [method]` | `051c53c0-4e42-51d9-9622-826beaa9b227` | 752-756 [crates/gcore/src/provisioning/tests.rs:752-756] | Indexed method `RecordingHealth::wait_qdrant` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:752-756] |
| `RecordingHealth::wait_falkordb` | method | `fn wait_falkordb(&mut self, host: &str, port: u16) -> anyhow::Result<()> {` | `RecordingHealth::wait_falkordb [method]` | `26ff4a76-a97a-5958-aebf-e9fe7fba8b5f` | 758-762 [crates/gcore/src/provisioning/tests.rs:758-762] | Indexed method `RecordingHealth::wait_falkordb` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:758-762] |
