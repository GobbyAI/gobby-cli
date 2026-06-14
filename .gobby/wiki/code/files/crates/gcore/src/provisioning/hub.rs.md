---
title: crates/gcore/src/provisioning/hub.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/hub.rs
  ranges:
  - 4-9
  - 11-20
  - 23-26
  - 28-35
  - 38-41
  - 44-48
  - 51-54
  - 56-66
  - 69-87
  - 89-167
  - 169-279
  - 281-283
  - 286-337
  - 340-344
  - 347-352
  - 355-358
  - 360-396
  - 398-408
  - 411-414
  - 416-428
  - 430-437
  - 440-442
  - 445-447
  - 450-455
  - 458-470
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/hub.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Purpose

Provides hub provisioning and database-URL resolution for gcore. It defines the option and result types used to identify a hub, collects candidate PostgreSQL DSNs from environment, config, and bootstrap sources, probes an existing database’s identity when possible, and falls back to Docker service provisioning when no verified hub is reachable.
[crates/gcore/src/provisioning/hub.rs:4-9]
[crates/gcore/src/provisioning/hub.rs:11-20]
[crates/gcore/src/provisioning/hub.rs:12-19]
[crates/gcore/src/provisioning/hub.rs:23-26]
[crates/gcore/src/provisioning/hub.rs:28-35]

## API Symbols

- `EnsureHubOptions` (class) component `EnsureHubOptions [class]` (`7751c0be-7f2d-58fc-94b9-35fc101e2af6`) lines 4-9 [crates/gcore/src/provisioning/hub.rs:4-9]
  - Signature: `pub struct EnsureHubOptions {`
  - Purpose: `EnsureHubOptions` encapsulates configuration parameters for hub initialization, comprising the Gobby home directory path, Docker service settings, a list of candidate database URLs, and a boolean flag controlling service provisioning. [crates/gcore/src/provisioning/hub.rs:4-9]
- `EnsureHubOptions` (class) component `EnsureHubOptions [class]` (`e5abcf74-d0f4-581b-a681-547b1b8fabcd`) lines 11-20 [crates/gcore/src/provisioning/hub.rs:11-20]
  - Signature: `impl EnsureHubOptions {`
  - Purpose: `EnsureHubOptions::new` is a constructor that initializes the struct with Docker service options, a gobby home directory path, an empty database URL candidate list, and service provisioning enabled. [crates/gcore/src/provisioning/hub.rs:11-20]
- `EnsureHubOptions.new` (method) component `EnsureHubOptions.new [method]` (`9e324f77-80a7-5ec4-833b-98e50caac48d`) lines 12-19 [crates/gcore/src/provisioning/hub.rs:12-19]
  - Signature: `pub fn new(gobby_home: PathBuf) -> Self {`
  - Purpose: Creates a new instance with `DockerServiceOptions` derived from the provided `gobby_home` path, an empty `candidate_database_urls` vector, and `provision_services` enabled. [crates/gcore/src/provisioning/hub.rs:12-19]
- `HubIdentity` (class) component `HubIdentity [class]` (`7ab65b74-081e-5228-9689-f084439be5d6`) lines 23-26 [crates/gcore/src/provisioning/hub.rs:23-26]
  - Signature: `pub struct HubIdentity {`
  - Purpose: `HubIdentity` is a struct that pairs a system identifier and database name to uniquely identify a hub instance. [crates/gcore/src/provisioning/hub.rs:23-26]
- `HubIdentity` (class) component `HubIdentity [class]` (`c9e62f4c-1fcb-51a0-b3dd-053375420b9d`) lines 28-35 [crates/gcore/src/provisioning/hub.rs:28-35]
  - Signature: `impl HubIdentity {`
  - Purpose: `HubIdentity` implements a `display_label` method that returns a formatted string representation of its `system_identifier` and `database_name` fields. [crates/gcore/src/provisioning/hub.rs:28-35]
- `HubIdentity.display_label` (method) component `HubIdentity.display_label [method]` (`96f0de14-d7d2-5daa-a460-09ac19092930`) lines 29-34 [crates/gcore/src/provisioning/hub.rs:29-34]
  - Signature: `fn display_label(&self) -> String {`
  - Purpose: Returns a formatted `String` containing the `system_identifier` and `database_name` fields as comma-separated key-value pairs. [crates/gcore/src/provisioning/hub.rs:29-34]
- `HubIdentityProbeResult` (type) component `HubIdentityProbeResult [type]` (`0ad02dfc-1d6d-56f8-a76f-830cfdc2f7fc`) lines 38-41 [crates/gcore/src/provisioning/hub.rs:38-41]
  - Signature: `pub enum HubIdentityProbeResult {`
  - Purpose: Indexed type `HubIdentityProbeResult` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:38-41]
- `RecordedHubIdentityStatus` (type) component `RecordedHubIdentityStatus [type]` (`6827e75f-b20a-5f87-9354-8119b11785e1`) lines 44-48 [crates/gcore/src/provisioning/hub.rs:44-48]
  - Signature: `pub enum RecordedHubIdentityStatus {`
  - Purpose: Indexed type `RecordedHubIdentityStatus` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:44-48]
- `RecordedHubResolution` (class) component `RecordedHubResolution [class]` (`60d1616f-3bb4-5d1e-81eb-dcdaa4b69c39`) lines 51-54 [crates/gcore/src/provisioning/hub.rs:51-54]
  - Signature: `pub struct RecordedHubResolution {`
  - Purpose: `RecordedHubResolution` is a struct that encapsulates a database URL string and an associated identity status to represent the state of a resolved hub. [crates/gcore/src/provisioning/hub.rs:51-54]
- `ensure_hub` (function) component `ensure_hub [function]` (`0fa50ba7-0ca4-598a-966c-2b00eaee5f8a`) lines 56-66 [crates/gcore/src/provisioning/hub.rs:56-66]
  - Signature: `pub fn ensure_hub(`
  - Purpose: Ensures hub provisioning by delegating to `ensure_hub_with_identity` with callbacks for environment variable resolution, PostgreSQL connectivity verification, hub identity detection, and Docker service provisioning, returning a string identifier and optional provisioning report. [crates/gcore/src/provisioning/hub.rs:56-66]
- `ensure_hub_with` (function) component `ensure_hub_with [function]` (`bf134ad9-1612-5787-810c-cccc5ca7577c`) lines 69-87 [crates/gcore/src/provisioning/hub.rs:69-87]
  - Signature: `pub(crate) fn ensure_hub_with(`
  - Purpose: Ensures hub provisioning with supplied options and injectable callbacks (environment accessor, database reachability check, provisioning function), delegating to `ensure_hub_with_identity` with a hardcoded identity probe that always reports insufficient privilege. [crates/gcore/src/provisioning/hub.rs:69-87]
- `ensure_hub_with_identity` (function) component `ensure_hub_with_identity [function]` (`1a20a85b-4eb8-5056-8b13-57f778074bd0`) lines 89-167 [crates/gcore/src/provisioning/hub.rs:89-167]
  - Signature: `pub(crate) fn ensure_hub_with_identity(`
  - Purpose: Resolves a reachable hub database URL from multiple candidate sources (environment, Gcore config, bootstrap) using identity probing to validate the configuration, returning the selected database URL and optional Docker provisioning report. [crates/gcore/src/provisioning/hub.rs:89-167]
- `resolve_recorded_hub_database_url` (function) component `resolve_recorded_hub_database_url [function]` (`f27d3644-1a61-5b9e-8a46-ad64583cc1b5`) lines 169-279 [crates/gcore/src/provisioning/hub.rs:169-279]
  - Signature: `pub fn resolve_recorded_hub_database_url(`
  - Purpose: Returns a reachable hub database URL selected from optional existing and daemon candidates, with identity verification status indicating whether the endpoints are identical, single, or differing. [crates/gcore/src/provisioning/hub.rs:169-279]
- `redacted_postgres_dsn_placeholder` (function) component `redacted_postgres_dsn_placeholder [function]` (`07c374c8-4a5e-559f-b908-12259969db93`) lines 281-283 [crates/gcore/src/provisioning/hub.rs:281-283]
  - Signature: `fn redacted_postgres_dsn_placeholder(source: &str) -> String {`
  - Purpose: Returns a redacted placeholder string for a PostgreSQL DSN by formatting the input source parameter as `<redacted-{source}-postgres-dsn>`. [crates/gcore/src/provisioning/hub.rs:281-283]
- `probe_postgres_hub_identity` (function) component `probe_postgres_hub_identity [function]` (`1519ba59-ea5b-516e-812a-fb74f776f9c9`) lines 286-337 [crates/gcore/src/provisioning/hub.rs:286-337]
  - Signature: `pub fn probe_postgres_hub_identity(database_url: &str) -> anyhow::Result<HubIdentityProbeResult> {`
  - Purpose: Probes a PostgreSQL instance's hub identity by verifying the current role has privilege to execute `pg_control_system()` and retrieving the system identifier and database name. [crates/gcore/src/provisioning/hub.rs:286-337]
- `insufficient_privilege` (function) component `insufficient_privilege [function]` (`38cb7d20-0e5a-5cea-87fd-749e2c07c27f`) lines 290-292 [crates/gcore/src/provisioning/hub.rs:290-292]
  - Signature: `fn insufficient_privilege(error: &postgres::Error) -> bool {`
  - Purpose: Returns `true` if the given PostgreSQL error has the `INSUFFICIENT_PRIVILEGE` SQL state code, `false` otherwise. [crates/gcore/src/provisioning/hub.rs:290-292]
- `probe_postgres_hub_identity` (function) component `probe_postgres_hub_identity [function]` (`43a85461-3db0-58b9-93f4-668f24423701`) lines 340-344 [crates/gcore/src/provisioning/hub.rs:340-344]
  - Signature: `pub fn probe_postgres_hub_identity(_database_url: &str) -> anyhow::Result<HubIdentityProbeResult> {`
  - Purpose: Returns a hard-coded `UnknownInsufficientPrivilege` error indicating that PostgreSQL identity probing is unavailable because gobby-core was compiled without PostgreSQL support. [crates/gcore/src/provisioning/hub.rs:340-344]
- `HubDatabaseUrlSource` (type) component `HubDatabaseUrlSource [type]` (`de73d338-72ba-5eff-8852-5d62328c2233`) lines 347-352 [crates/gcore/src/provisioning/hub.rs:347-352]
  - Signature: `enum HubDatabaseUrlSource {`
  - Purpose: Indexed type `HubDatabaseUrlSource` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:347-352]
- `HubDatabaseUrl` (class) component `HubDatabaseUrl [class]` (`cf7cbf50-3223-53cb-9747-d42aaabb8091`) lines 355-358 [crates/gcore/src/provisioning/hub.rs:355-358]
  - Signature: `struct HubDatabaseUrl {`
  - Purpose: `HubDatabaseUrl` is a struct that pairs a database URL string with its source origin via the `HubDatabaseUrlSource` enum. [crates/gcore/src/provisioning/hub.rs:355-358]
- `resolve_hub_database_urls` (function) component `resolve_hub_database_urls [function]` (`04f6fb3c-7427-5b7f-a517-ae402df5d8ba`) lines 360-396 [crates/gcore/src/provisioning/hub.rs:360-396]
  - Signature: `fn resolve_hub_database_urls(`
  - Purpose: Aggregates PostgreSQL database URLs from multiple sources (command options, GOBBY_POSTGRES_DSN environment variable, gcore config, and bootstrap.yaml file), returning each with source attribution metadata. [crates/gcore/src/provisioning/hub.rs:360-396]
- `resolve_database_url_from_gcore_config` (function) component `resolve_database_url_from_gcore_config [function]` (`d406e49b-658d-58a4-a073-ac9929ff28e9`) lines 398-408 [crates/gcore/src/provisioning/hub.rs:398-408]
  - Signature: `fn resolve_database_url_from_gcore_config(home: &Path) -> anyhow::Result<Option<String>> {`
  - Purpose: Resolves a PostgreSQL database DSN from a gcore StandaloneConfig file if prerequisite service files exist in the home directory, otherwise returns None. [crates/gcore/src/provisioning/hub.rs:398-408]
- `HubBootstrap` (class) component `HubBootstrap [class]` (`0fdb8183-1058-5fcc-b004-b405b8078378`) lines 411-414 [crates/gcore/src/provisioning/hub.rs:411-414]
  - Signature: `struct HubBootstrap {`
  - Purpose: HubBootstrap is a configuration struct with two optional String fields for specifying a hub backend service and database connection URL. [crates/gcore/src/provisioning/hub.rs:411-414]
- `resolve_database_url_from_bootstrap_file` (function) component `resolve_database_url_from_bootstrap_file [function]` (`cc00b96c-d159-59ea-806d-dbe460fe29f5`) lines 416-428 [crates/gcore/src/provisioning/hub.rs:416-428]
  - Signature: `fn resolve_database_url_from_bootstrap_file(path: &Path) -> anyhow::Result<Option<String>> {`
  - Purpose: Reads a YAML bootstrap file and returns the non-empty trimmed database URL if the hub backend is PostgreSQL or unspecified, otherwise None. [crates/gcore/src/provisioning/hub.rs:416-428]
- `non_empty_trimmed` (function) component `non_empty_trimmed [function]` (`46462147-3f5c-5912-99ef-8aaece7a0c4e`) lines 430-437 [crates/gcore/src/provisioning/hub.rs:430-437]
  - Signature: `fn non_empty_trimmed(value: Option<String>) -> Option<String> {`
  - Purpose: Transforms an optional string to None if absent or empty after trimming whitespace; otherwise returns Some with the trimmed string. [crates/gcore/src/provisioning/hub.rs:430-437]
- `postgres_database_reachable` (function) component `postgres_database_reachable [function]` (`91f4d94b-f570-5148-b91c-daa3e21427fe`) lines 440-442 [crates/gcore/src/provisioning/hub.rs:440-442]
  - Signature: `fn postgres_database_reachable(database_url: &str) -> bool {`
  - Purpose: Returns a boolean indicating whether a read-only connection to the PostgreSQL database at the provided URL can be successfully established. [crates/gcore/src/provisioning/hub.rs:440-442]
- `postgres_database_reachable` (function) component `postgres_database_reachable [function]` (`048545f2-e259-5919-86eb-1cb59fe0e036`) lines 445-447 [crates/gcore/src/provisioning/hub.rs:445-447]
  - Signature: `fn postgres_database_reachable(_database_url: &str) -> bool {`
  - Purpose: A stub function that accepts a PostgreSQL database URL string reference and unconditionally returns `false`, regardless of actual database reachability. [crates/gcore/src/provisioning/hub.rs:445-447]
- `explicit_database_url_reachable` (function) component `explicit_database_url_reachable [function]` (`5ca78e2d-a136-5487-affc-5329c3623ad3`) lines 450-455 [crates/gcore/src/provisioning/hub.rs:450-455]
  - Signature: `fn explicit_database_url_reachable(`
  - Purpose: This function invokes a mutable callback closure with the given database URL string and returns its boolean result to determine whether the database is reachable. [crates/gcore/src/provisioning/hub.rs:450-455]
- `explicit_database_url_reachable` (function) component `explicit_database_url_reachable [function]` (`1f5ca7c9-ef07-5084-928b-3324f656a231`) lines 458-470 [crates/gcore/src/provisioning/hub.rs:458-470]
  - Signature: `fn explicit_database_url_reachable(`
  - Purpose: This function unconditionally returns `true` without probing database reachability for an explicit PostgreSQL DSN when the postgres feature is disabled, deferring connection validation to runtime. [crates/gcore/src/provisioning/hub.rs:458-470]

