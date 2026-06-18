---
title: crates/gcore/src/provisioning/tests.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/tests.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Overview

`crates/gcore/src/provisioning/tests.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gcore/src/provisioning/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `EnvGuard` | class | Indexed class `EnvGuard` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:5-7] |
| `EnvGuard::new` | method | Indexed method `EnvGuard::new` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:10-18] |
| `EnvGuard::clear` | method | Indexed method `EnvGuard::clear` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:20-34] |
| `EnvGuard::drop` | method | Indexed method `EnvGuard::drop` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:38-40] |
| `write_services_stack` | function | Indexed function `write_services_stack` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:43-46] |
| `gcore_yaml_reads_flat_and_nested_keys` | function | Indexed function `gcore_yaml_reads_flat_and_nested_keys` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:49-87] |
| `gcore_yaml_reads_dotted_mapping_prefixes` | function | Indexed function `gcore_yaml_reads_dotted_mapping_prefixes` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:90-102] |
| `gcore_yaml_text_generation_defaults_do_not_override_explicit_values` | function | Indexed function `gcore_yaml_text_generation_defaults_do_not_override_explicit_values` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:105-123] |
| `gcore_yaml_writes_nested_keys` | function | Indexed function `gcore_yaml_writes_nested_keys` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:126-153] |
| `gcore_yaml_write_rejects_scalar_to_nested_mapping_collision` | function | Indexed function `gcore_yaml_write_rejects_scalar_to_nested_mapping_collision` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:156-170] |
| `gcore_yaml_rejects_excessive_nesting` | function | Indexed function `gcore_yaml_rejects_excessive_nesting` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:173-185] |
| `gcore_yaml_rejects_sequence_scalar_values` | function | Indexed function `gcore_yaml_rejects_sequence_scalar_values` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:188-204] |
| `gcore_yaml_stringifies_tagged_scalar_values` | function | Indexed function `gcore_yaml_stringifies_tagged_scalar_values` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:207-226] |
| `gcore_yaml_stringifies_tagged_sequence_values` | function | Indexed function `gcore_yaml_stringifies_tagged_sequence_values` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:229-251] |
| `nested_yaml_str` | function | Indexed function `nested_yaml_str` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:253-261] |
| `standalone_config_resolves_service_keys_and_plain_api_key` | function | Indexed function `standalone_config_resolves_service_keys_and_plain_api_key` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:264-288] |
| `writes_ai_embeddings_standalone_api_key` | function | Indexed function `writes_ai_embeddings_standalone_api_key` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:291-328] |
| `compose_template_matches_daemon_checkout_when_present` | function | Indexed function `compose_template_matches_daemon_checkout_when_present` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:331-340] |
| `daemon_compose_template_path` | function | Indexed function `daemon_compose_template_path` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:342-357] |
| `docker_provisioning_prepares_assets_runs_compose_and_health_checks` | function | Indexed function `docker_provisioning_prepares_assets_runs_compose_and_health_checks` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:360-397] |
| `ensure_hub_reuses_then_provisions` | function | Indexed function `ensure_hub_reuses_then_provisions` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:400-454] |
| `gcore_yaml_database_url_requires_services_stack` | function | Indexed function `gcore_yaml_database_url_requires_services_stack` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:457-488] |
| `no_double_provision_when_reachable` | function | Indexed function `no_double_provision_when_reachable` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:491-521] |
| `divergent_hubs_surface_conflict` | function | Indexed function `divergent_hubs_surface_conflict` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:524-577] |
| `reachable_env_database_url_conflicts_with_recorded_hub` | function | Indexed function `reachable_env_database_url_conflicts_with_recorded_hub` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:580-620] |
| `insufficient_identity_privilege_preserves_hub` | function | Indexed function `insufficient_identity_privilege_preserves_hub` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:623-686] |
| `override_plus_recorded_hub_preserves_recorded_when_identity_unknown` | function | Indexed function `override_plus_recorded_hub_preserves_recorded_when_identity_unknown` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:689-721] |
| `RecordingRunner` | class | Indexed class `RecordingRunner` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:724-726] |
| `RecordingRunner::run` | method | Indexed method `RecordingRunner::run` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:729-736] |
| `RecordingHealth` | class | Indexed class `RecordingHealth` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:740-743] |
| `RecordingHealth::wait_postgres` | method | Indexed method `RecordingHealth::wait_postgres` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:746-750] |
| `RecordingHealth::wait_qdrant` | method | Indexed method `RecordingHealth::wait_qdrant` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:752-756] |
| `RecordingHealth::wait_falkordb` | method | Indexed method `RecordingHealth::wait_falkordb` in `crates/gcore/src/provisioning/tests.rs`. [crates/gcore/src/provisioning/tests.rs:758-762] |

