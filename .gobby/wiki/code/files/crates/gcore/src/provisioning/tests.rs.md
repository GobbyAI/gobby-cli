---
title: crates/gcore/src/provisioning/tests.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/tests.rs
  ranges:
  - 5-7
  - 9-35
  - 37-41
  - 43-46
  - 49-74
  - 77-89
  - 92-119
  - 122-136
  - 139-151
  - 154-170
  - 173-192
  - 195-217
  - 219-227
  - 230-254
  - 257-294
  - 297-306
  - 308-323
  - 326-363
  - 366-420
  - 423-454
  - 457-487
  - 490-543
  - 546-586
  - 589-652
  - 655-687
  - 690-692
  - 694-703
  - 706-709
  - 711-729
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/tests.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Purpose

Test module for `gcore` provisioning that exercises `StandaloneConfig` YAML parsing/writing, service-stack file generation, hub/database URL resolution, and Docker provisioning behavior. It uses `EnvGuard` to serialize and clear test environment state, plus lightweight test doubles like `RecordingRunner` and `RecordingHealth` to verify command execution and health-check calls without running real services.
[crates/gcore/src/provisioning/tests.rs:5-7]
[crates/gcore/src/provisioning/tests.rs:9-35]
[crates/gcore/src/provisioning/tests.rs:10-18]
[crates/gcore/src/provisioning/tests.rs:20-34]
[crates/gcore/src/provisioning/tests.rs:37-41]

## API Symbols

- `EnvGuard` (class) component `EnvGuard [class]` (`b7e17b70-74b9-5491-b283-50ea559f94cb`) lines 5-7 [crates/gcore/src/provisioning/tests.rs:5-7]
  - Signature: `struct EnvGuard {`
  - Purpose: 'EnvGuard' is a zero-logic guard type that owns a 'MutexGuard<'static, ()>', using the held mutex lock to provide exclusive, process-wide synchronization while the guard is in scope. [crates/gcore/src/provisioning/tests.rs:5-7]
- `EnvGuard` (class) component `EnvGuard [class]` (`7ae5b255-1e13-58bb-901d-e7ef3140c18e`) lines 9-35 [crates/gcore/src/provisioning/tests.rs:9-35]
  - Signature: `impl EnvGuard {`
  - Purpose: 'EnvGuard' is a test-only RAII guard that serializes access with 'TEST_ENV_LOCK' and clears a fixed set of Gobby-related environment variables on construction to isolate test state. [crates/gcore/src/provisioning/tests.rs:9-35]
- `EnvGuard.new` (method) component `EnvGuard.new [method]` (`614c9763-f589-52a4-bd68-add3498fa73f`) lines 10-18 [crates/gcore/src/provisioning/tests.rs:10-18]
  - Signature: `fn new() -> Self {`
  - Purpose: Creates a 'Self' instance holding a recovered 'TEST_ENV_LOCK' mutex guard, clears the associated test environment state, and returns the initialized guard. [crates/gcore/src/provisioning/tests.rs:10-18]
- `EnvGuard.clear` (method) component `EnvGuard.clear [method]` (`5a80db9e-185c-5aa1-a48c-ceddef5c8931`) lines 20-34 [crates/gcore/src/provisioning/tests.rs:20-34]
  - Signature: `fn clear(&self) {`
  - Purpose: Acquires the internal environment lock and then unsafely removes a fixed set of Gobby-related environment variables ('GOBBY_FALKORDB_HOST', 'GOBBY_FALKORDB_PORT', 'GOBBY_FALKORDB_PASSWORD', 'GOBBY_POSTGRES_DSN', 'GOBBY_QDRANT_URL', 'GOBBY_QDRANT_API_KEY') from the process environment. [crates/gcore/src/provisioning/tests.rs:20-34]
- `EnvGuard` (class) component `EnvGuard [class]` (`3e4594fc-d49c-5097-98e5-d6b94b3563fc`) lines 37-41 [crates/gcore/src/provisioning/tests.rs:37-41]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: 'EnvGuard' is a Rust RAII guard whose 'Drop' implementation calls 'self.clear()' to automatically clear its managed environment state when the value goes out of scope. [crates/gcore/src/provisioning/tests.rs:37-41]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`0974fba8-549c-5e67-89e3-a96aa4b0a85b`) lines 38-40 [crates/gcore/src/provisioning/tests.rs:38-40]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Invokes 'self.clear()' to remove all elements from the collection when the value is dropped. [crates/gcore/src/provisioning/tests.rs:38-40]
- `write_services_stack` (function) component `write_services_stack [function]` (`3a1d922a-7aa6-5d16-8fac-0dd37efa0d4f`) lines 43-46 [crates/gcore/src/provisioning/tests.rs:43-46]
  - Signature: `fn write_services_stack(home: &Path) {`
  - Purpose: Creates the services directory under 'home' and writes a minimal Compose file containing 'services: {}' to the corresponding path. [crates/gcore/src/provisioning/tests.rs:43-46]
- `gcore_yaml_reads_flat_and_nested_keys` (function) component `gcore_yaml_reads_flat_and_nested_keys [function]` (`b9b78d7c-f07d-5dc0-a3be-b52f209d0ec0`) lines 49-74 [crates/gcore/src/provisioning/tests.rs:49-74]
  - Signature: `fn gcore_yaml_reads_flat_and_nested_keys() {`
  - Purpose: Verifies that 'StandaloneConfig::from_yaml_str' correctly parses both flat dotted YAML keys and nested YAML mappings into retrievable string values via 'config.get()', including a dynamically named API key field. [crates/gcore/src/provisioning/tests.rs:49-74]
- `gcore_yaml_reads_dotted_mapping_prefixes` (function) component `gcore_yaml_reads_dotted_mapping_prefixes [function]` (`5d45c5e8-3bff-5c62-830b-3ff091b09a6e`) lines 77-89 [crates/gcore/src/provisioning/tests.rs:77-89]
  - Signature: `fn gcore_yaml_reads_dotted_mapping_prefixes() {`
  - Purpose: Verifies that 'StandaloneConfig::from_yaml_str' correctly interprets dotted YAML mapping prefixes by allowing nested keys like 'ai.embeddings.provider' and 'ai.embeddings.model' to be retrieved from a flattened dotted path. [crates/gcore/src/provisioning/tests.rs:77-89]
- `gcore_yaml_writes_nested_keys` (function) component `gcore_yaml_writes_nested_keys [function]` (`1699fd95-ad46-5689-bff9-aa5cca8e0a8b`) lines 92-119 [crates/gcore/src/provisioning/tests.rs:92-119]
  - Signature: `fn gcore_yaml_writes_nested_keys() {`
  - Purpose: Verifies that 'StandaloneConfig::write_at' serializes dotted configuration keys into nested YAML mappings rather than flat keys, and that the written values can be read back correctly via both YAML traversal and 'StandaloneConfig::read_at'. [crates/gcore/src/provisioning/tests.rs:92-119]
- `gcore_yaml_write_rejects_scalar_to_nested_mapping_collision` (function) component `gcore_yaml_write_rejects_scalar_to_nested_mapping_collision [function]` (`7c652d9e-4a71-5a2a-b05d-214a91ab41d7`) lines 122-136 [crates/gcore/src/provisioning/tests.rs:122-136]
  - Signature: `fn gcore_yaml_write_rejects_scalar_to_nested_mapping_collision() {`
  - Purpose: Verifies that writing a 'StandaloneConfig' fails when a nested key like 'ai.embeddings.provider' collides with an existing scalar YAML value at 'ai', and that the error reports the scalar-to-nested-mapping conflict. [crates/gcore/src/provisioning/tests.rs:122-136]
- `gcore_yaml_rejects_excessive_nesting` (function) component `gcore_yaml_rejects_excessive_nesting [function]` (`08edb6a0-ef56-5e70-9b3a-c5a2072fb88b`) lines 139-151 [crates/gcore/src/provisioning/tests.rs:139-151]
  - Signature: `fn gcore_yaml_rejects_excessive_nesting() {`
  - Purpose: Constructs a YAML document nested beyond 64 levels, verifies 'StandaloneConfig::from_yaml_str' rejects it with an error, and asserts the message reports that the maximum depth of 64 was exceeded. [crates/gcore/src/provisioning/tests.rs:139-151]
- `gcore_yaml_rejects_sequence_scalar_values` (function) component `gcore_yaml_rejects_sequence_scalar_values [function]` (`85ce0cde-8638-52c4-9ff2-4324a52c8dbf`) lines 154-170 [crates/gcore/src/provisioning/tests.rs:154-170]
  - Signature: `fn gcore_yaml_rejects_sequence_scalar_values() {`
  - Purpose: Verifies that 'StandaloneConfig::from_yaml_str' rejects YAML sequences at the scalar path 'ai.embeddings.provider' and returns an error containing 'gcore.yaml path 'ai.embeddings.provider' cannot be a sequence'. [crates/gcore/src/provisioning/tests.rs:154-170]
- `gcore_yaml_stringifies_tagged_scalar_values` (function) component `gcore_yaml_stringifies_tagged_scalar_values [function]` (`02d36e64-3cc4-57e0-8b53-7e27a2553e3a`) lines 173-192 [crates/gcore/src/provisioning/tests.rs:173-192]
  - Signature: `fn gcore_yaml_stringifies_tagged_scalar_values() {`
  - Purpose: Verifies that 'StandaloneConfig::from_yaml_str' stringifies a tagged YAML scalar ('!provider ollama') and stores it at 'ai.embeddings.provider' as the exact serialized YAML string produced by 'serde_yaml::to_string(...).trim()'. [crates/gcore/src/provisioning/tests.rs:173-192]
- `gcore_yaml_stringifies_tagged_sequence_values` (function) component `gcore_yaml_stringifies_tagged_sequence_values [function]` (`1b7c546a-12f8-5ecb-a470-5ce04e7a23f4`) lines 195-217 [crates/gcore/src/provisioning/tests.rs:195-217]
  - Signature: `fn gcore_yaml_stringifies_tagged_sequence_values() {`
  - Purpose: Verifies that a YAML tagged sequence under 'ai.embeddings.provider' is parsed and reserialized as a string, and that 'StandaloneConfig::get("ai.embeddings.provider")' returns that stringified tagged YAML. [crates/gcore/src/provisioning/tests.rs:195-217]
- `nested_yaml_str` (function) component `nested_yaml_str [function]` (`b232f77c-a4a1-5ab1-97c1-e3a2fb8460c1`) lines 219-227 [crates/gcore/src/provisioning/tests.rs:219-227]
  - Signature: `fn nested_yaml_str<'a>(value: &'a serde_yaml::Value, path: &[&str]) -> Option<&'a str> {`
  - Purpose: Traverses a 'serde_yaml::Value' along a sequence of mapping keys and returns the final node as 'Some(&str)' if every lookup succeeds and the terminal value is a string, otherwise 'None'. [crates/gcore/src/provisioning/tests.rs:219-227]
- `standalone_config_resolves_service_keys_and_plain_api_key` (function) component `standalone_config_resolves_service_keys_and_plain_api_key [function]` (`3a7415ac-6858-5a36-b732-c949a24dfdcd`) lines 230-254 [crates/gcore/src/provisioning/tests.rs:230-254]
  - Signature: `fn standalone_config_resolves_service_keys_and_plain_api_key() {`
  - Purpose: Parses a standalone YAML config containing FalkorDB, Qdrant, and embedding service keys, then verifies the resolver functions correctly extract the FalkorDB password, Qdrant URL, and embedding API key from the config. [crates/gcore/src/provisioning/tests.rs:230-254]
- `writes_ai_embeddings_standalone_api_key` (function) component `writes_ai_embeddings_standalone_api_key [function]` (`4853a3ec-ba61-5749-900e-e2ad10fd4e7f`) lines 257-294 [crates/gcore/src/provisioning/tests.rs:257-294]
  - Signature: `fn writes_ai_embeddings_standalone_api_key() {`
  - Purpose: Creates a temporary standalone bootstrap config with embedding settings and asserts that 'write_standalone_bootstrap' writes the provider, API base, model, vector dimension, query prefix, and API key into the expected AI embedding config keys. [crates/gcore/src/provisioning/tests.rs:257-294]
- `compose_template_matches_daemon_checkout_when_present` (function) component `compose_template_matches_daemon_checkout_when_present [function]` (`f6dd3942-d35e-5d68-9b78-55b4f99fe8d7`) lines 297-306 [crates/gcore/src/provisioning/tests.rs:297-306]
  - Signature: `fn compose_template_matches_daemon_checkout_when_present() {`
  - Purpose: Returns early unless the daemon compose template file exists, and otherwise reads it as a string and asserts it exactly matches 'COMPOSE_TEMPLATE'. [crates/gcore/src/provisioning/tests.rs:297-306]
- `daemon_compose_template_path` (function) component `daemon_compose_template_path [function]` (`915f3380-7591-5c82-bde6-5930ae99baf8`) lines 308-323 [crates/gcore/src/provisioning/tests.rs:308-323]
  - Signature: `fn daemon_compose_template_path() -> Option<PathBuf> {`
  - Purpose: Returns a compose-template 'PathBuf' from the trimmed 'GOBBY_DAEMON_COMPOSE_PATH' environment variable when set and non-empty, otherwise falls back to '../../../gobby/src/gobby/data/docker-compose.services.yml' relative to the crate manifest, or 'None' if that path resolution fails. [crates/gcore/src/provisioning/tests.rs:308-323]
- `docker_provisioning_prepares_assets_runs_compose_and_health_checks` (function) component `docker_provisioning_prepares_assets_runs_compose_and_health_checks [function]` (`17377349-05ed-545a-9b06-b98f1b77be7c`) lines 326-363 [crates/gcore/src/provisioning/tests.rs:326-363]
  - Signature: `fn docker_provisioning_prepares_assets_runs_compose_and_health_checks() {`
  - Purpose: Creates a temporary provisioning environment, invokes Docker Compose once with the 'all' profile, performs health checks for 'postgres', 'qdrant', and 'falkordb', and verifies the generated compose, service assets, and env file contents. [crates/gcore/src/provisioning/tests.rs:326-363]
- `ensure_hub_reuses_then_provisions` (function) component `ensure_hub_reuses_then_provisions [function]` (`5dbf8bcd-4b1c-5bc9-a3ad-307efd38562f`) lines 366-420 [crates/gcore/src/provisioning/tests.rs:366-420]
  - Signature: `fn ensure_hub_reuses_then_provisions() {`
  - Purpose: Tests that 'ensure_hub_with' prefers and reuses a reachable configured Postgres DSN without provisioning services, then falls back to provisioning a new hub and returning the provisioned/default database URL when no candidate URL is reachable. [crates/gcore/src/provisioning/tests.rs:366-420]
- `gcore_yaml_database_url_requires_services_stack` (function) component `gcore_yaml_database_url_requires_services_stack [function]` (`b78921e7-974d-5d13-ad98-3943cfcf01ca`) lines 423-454 [crates/gcore/src/provisioning/tests.rs:423-454]
  - Signature: `fn gcore_yaml_database_url_requires_services_stack() {`
  - Purpose: Verifies that when the Gobby YAML config contains a PostgreSQL DSN, 'ensure_hub_with' provisions the services stack fallback and returns the default database URL for the configured port rather than the recorded DSN. [crates/gcore/src/provisioning/tests.rs:423-454]
- `no_double_provision_when_reachable` (function) component `no_double_provision_when_reachable [function]` (`652ae96a-9b4f-55ea-a182-452ddd5c21c1`) lines 457-487 [crates/gcore/src/provisioning/tests.rs:457-487]
  - Signature: `fn no_double_provision_when_reachable() {`
  - Purpose: Verifies that when the recorded PostgreSQL DSN is reachable and its hub identity is already known, 'ensure_hub_with_identity' reuses that DSN without provisioning services and returns 'None' for the report. [crates/gcore/src/provisioning/tests.rs:457-487]
- `divergent_hubs_surface_conflict` (function) component `divergent_hubs_surface_conflict [function]` (`1338db81-b929-5bef-b2af-e5882ca9b540`) lines 490-543 [crates/gcore/src/provisioning/tests.rs:490-543]
  - Signature: `fn divergent_hubs_surface_conflict() {`
  - Purpose: Sets up a standalone config and bootstrap pointing to two reachable Postgres hubs with different 'system_identifier' values, then verifies 'ensure_hub_with_identity' fails by surfacing both conflicting hub identities in the error message while redacting DSNs, secrets, and 'sslmode', and without provisioning services. [crates/gcore/src/provisioning/tests.rs:490-543]
- `reachable_env_database_url_conflicts_with_recorded_hub` (function) component `reachable_env_database_url_conflicts_with_recorded_hub [function]` (`122d1e68-9f53-55bf-bb58-95f7ae245556`) lines 546-586 [crates/gcore/src/provisioning/tests.rs:546-586]
  - Signature: `fn reachable_env_database_url_conflicts_with_recorded_hub() {`
  - Purpose: Verifies that 'ensure_hub_with_identity' rejects an environment-provided PostgreSQL DSN when it conflicts with a recorded hub identity for the same database, and that the resulting error reports both reachable hubs by system identifier and database name without leaking raw DSN URLs. [crates/gcore/src/provisioning/tests.rs:546-586]
- `insufficient_identity_privilege_preserves_hub` (function) component `insufficient_identity_privilege_preserves_hub [function]` (`cc17301f-6090-555d-add2-05fbb4f4eba7`) lines 589-652 [crates/gcore/src/provisioning/tests.rs:589-652]
  - Signature: `fn insufficient_identity_privilege_preserves_hub() {`
  - Purpose: Verifies that when hub identity probing returns 'UnknownInsufficientPrivilege', 'ensure_hub_with_identity' and 'resolve_recorded_hub_database_url' preserve the previously recorded hub database URL instead of provisioning or switching hubs. [crates/gcore/src/provisioning/tests.rs:589-652]
- `override_plus_recorded_hub_preserves_recorded_when_identity_unknown` (function) component `override_plus_recorded_hub_preserves_recorded_when_identity_unknown [function]` (`ec073f27-5326-59df-a1b3-a66f8b320666`) lines 655-687 [crates/gcore/src/provisioning/tests.rs:655-687]
  - Signature: `fn override_plus_recorded_hub_preserves_recorded_when_identity_unknown() {`
  - Purpose: Verifies that 'ensure_hub_with_identity' ignores an override DSN and preserves the recorded PostgreSQL URL when hub identity cannot be verified due to 'UnknownInsufficientPrivilege', returning no report and avoiding service provisioning. [crates/gcore/src/provisioning/tests.rs:655-687]
- `RecordingRunner` (class) component `RecordingRunner [class]` (`8cad3bf0-c0a0-5a79-ada6-fac6b75f26fb`) lines 690-692 [crates/gcore/src/provisioning/tests.rs:690-692]
  - Signature: `struct RecordingRunner {`
  - Purpose: 'RecordingRunner' is a struct that records an ordered collection of 'CommandSpec' values in its 'commands' field for later inspection or replay. [crates/gcore/src/provisioning/tests.rs:690-692]
- `RecordingRunner` (class) component `RecordingRunner [class]` (`868167a9-a37c-50cf-b117-de8f01284e96`) lines 694-703 [crates/gcore/src/provisioning/tests.rs:694-703]
  - Signature: `impl CommandRunner for RecordingRunner {`
  - Purpose: 'RecordingRunner' is a 'CommandRunner' implementation that records each received 'CommandSpec' by cloning it into an internal 'commands' list and returns a successful empty 'CommandOutput' with exit status '0' and no stdout or stderr. [crates/gcore/src/provisioning/tests.rs:694-703]
- `RecordingRunner.run` (method) component `RecordingRunner.run [method]` (`8b94b08a-fa6a-524e-81c5-fa86f58416e0`) lines 695-702 [crates/gcore/src/provisioning/tests.rs:695-702]
  - Signature: `fn run(&mut self, spec: &CommandSpec) -> std::io::Result<CommandOutput> {`
  - Purpose: Appends a clone of the provided 'CommandSpec' to 'self.commands' and returns an 'Ok(CommandOutput)' with exit status '0' and empty 'stdout' and 'stderr'. [crates/gcore/src/provisioning/tests.rs:695-702]
- `RecordingHealth` (class) component `RecordingHealth [class]` (`f2b79fc9-ee48-5da8-a800-a5f6d82c53b5`) lines 706-709 [crates/gcore/src/provisioning/tests.rs:706-709]
  - Signature: `struct RecordingHealth {`
  - Purpose: 'RecordingHealth' is a struct that stores a list of health-check labels and a list of endpoint tuples, each containing a static name, a 'String' address, and a 'u16' port. [crates/gcore/src/provisioning/tests.rs:706-709]
- `RecordingHealth` (class) component `RecordingHealth [class]` (`49da4686-4620-5469-85be-189fa47401aa`) lines 711-729 [crates/gcore/src/provisioning/tests.rs:711-729]
  - Signature: `impl DockerHealthChecker for RecordingHealth {`
  - Purpose: 'RecordingHealth' is a 'DockerHealthChecker' test double that records each requested service check and its '(service, host, port)' endpoint for 'postgres', 'qdrant', and 'falkordb' while always returning 'Ok(())'. [crates/gcore/src/provisioning/tests.rs:711-729]
- `RecordingHealth.wait_postgres` (method) component `RecordingHealth.wait_postgres [method]` (`7d639a82-9fa8-5b15-9384-8cb01d8cbd11`) lines 712-716 [crates/gcore/src/provisioning/tests.rs:712-716]
  - Signature: `fn wait_postgres(&mut self, host: &str, port: u16) -> anyhow::Result<()> {`
  - Purpose: 'wait_postgres' records a Postgres readiness check by appending '"postgres"' to 'self.checks' and '("postgres", host.to_string(), port)' to 'self.endpoints', then returns 'Ok(())'. [crates/gcore/src/provisioning/tests.rs:712-716]
- `RecordingHealth.wait_qdrant` (method) component `RecordingHealth.wait_qdrant [method]` (`c31d5f15-20cc-5a90-b7d3-7f85ee167dc7`) lines 718-722 [crates/gcore/src/provisioning/tests.rs:718-722]
  - Signature: `fn wait_qdrant(&mut self, host: &str, port: u16) -> anyhow::Result<()> {`
  - Purpose: Records a 'qdrant' check by appending '"qdrant"' to 'self.checks' and storing the '(name, host, port)' endpoint tuple in 'self.endpoints', then returns 'Ok(())'. [crates/gcore/src/provisioning/tests.rs:718-722]
- `RecordingHealth.wait_falkordb` (method) component `RecordingHealth.wait_falkordb [method]` (`b42a70bf-34bd-52f9-945f-f79636e6624a`) lines 724-728 [crates/gcore/src/provisioning/tests.rs:724-728]
  - Signature: `fn wait_falkordb(&mut self, host: &str, port: u16) -> anyhow::Result<()> {`
  - Purpose: Appends '"falkordb"' to 'self.checks', records the '( "falkordb", host.to_string(), port )' endpoint in 'self.endpoints', and returns 'Ok(())'. [crates/gcore/src/provisioning/tests.rs:724-728]

