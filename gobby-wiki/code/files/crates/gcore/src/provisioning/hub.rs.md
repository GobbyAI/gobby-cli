---
title: crates/gcore/src/provisioning/hub.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/hub.rs
  ranges:
  - 4-9
  - 12-19
  - 23-26
  - 29-34
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/provisioning/hub.rs:4-9](crates/gcore/src/provisioning/hub.rs#L4-L9), [crates/gcore/src/provisioning/hub.rs:12-19](crates/gcore/src/provisioning/hub.rs#L12-L19), [crates/gcore/src/provisioning/hub.rs:23-26](crates/gcore/src/provisioning/hub.rs#L23-L26), [crates/gcore/src/provisioning/hub.rs:29-34](crates/gcore/src/provisioning/hub.rs#L29-L34), [crates/gcore/src/provisioning/hub.rs:38-41](crates/gcore/src/provisioning/hub.rs#L38-L41), [crates/gcore/src/provisioning/hub.rs:44-48](crates/gcore/src/provisioning/hub.rs#L44-L48), [crates/gcore/src/provisioning/hub.rs:51-54](crates/gcore/src/provisioning/hub.rs#L51-L54), [crates/gcore/src/provisioning/hub.rs:56-66](crates/gcore/src/provisioning/hub.rs#L56-L66), [crates/gcore/src/provisioning/hub.rs:69-87](crates/gcore/src/provisioning/hub.rs#L69-L87), [crates/gcore/src/provisioning/hub.rs:89-167](crates/gcore/src/provisioning/hub.rs#L89-L167), [crates/gcore/src/provisioning/hub.rs:169-279](crates/gcore/src/provisioning/hub.rs#L169-L279), [crates/gcore/src/provisioning/hub.rs:281-283](crates/gcore/src/provisioning/hub.rs#L281-L283), [crates/gcore/src/provisioning/hub.rs:286-337](crates/gcore/src/provisioning/hub.rs#L286-L337), [crates/gcore/src/provisioning/hub.rs:340-344](crates/gcore/src/provisioning/hub.rs#L340-L344), [crates/gcore/src/provisioning/hub.rs:347-352](crates/gcore/src/provisioning/hub.rs#L347-L352), [crates/gcore/src/provisioning/hub.rs:355-358](crates/gcore/src/provisioning/hub.rs#L355-L358), [crates/gcore/src/provisioning/hub.rs:360-396](crates/gcore/src/provisioning/hub.rs#L360-L396), [crates/gcore/src/provisioning/hub.rs:398-408](crates/gcore/src/provisioning/hub.rs#L398-L408), [crates/gcore/src/provisioning/hub.rs:411-414](crates/gcore/src/provisioning/hub.rs#L411-L414), [crates/gcore/src/provisioning/hub.rs:416-428](crates/gcore/src/provisioning/hub.rs#L416-L428), [crates/gcore/src/provisioning/hub.rs:430-437](crates/gcore/src/provisioning/hub.rs#L430-L437), [crates/gcore/src/provisioning/hub.rs:440-442](crates/gcore/src/provisioning/hub.rs#L440-L442), [crates/gcore/src/provisioning/hub.rs:445-447](crates/gcore/src/provisioning/hub.rs#L445-L447), [crates/gcore/src/provisioning/hub.rs:450-455](crates/gcore/src/provisioning/hub.rs#L450-L455), [crates/gcore/src/provisioning/hub.rs:458-470](crates/gcore/src/provisioning/hub.rs#L458-L470)

</details>

# crates/gcore/src/provisioning/hub.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file implements hub provisioning and database resolution logic for `gcore`. `EnsureHubOptions` carries the home directory, Docker service settings, candidate database URLs, and whether services should be provisioned; `ensure_hub` and its test-only `ensure_hub_with` delegate to `ensure_hub_with_identity`, which coordinates environment lookup, database reachability checks, hub identity probing, and service provisioning. The identity types classify whether a database is the same hub, reachable but unknown due to insufficient privilege, or otherwise verified, while the resolution helpers combine URLs from config, bootstrap files, and candidate inputs, normalize and redact DSNs, and verify which recorded or explicit Postgres databases can actually be reached.
[crates/gcore/src/provisioning/hub.rs:4-9]
[crates/gcore/src/provisioning/hub.rs:12-19]
[crates/gcore/src/provisioning/hub.rs:23-26]
[crates/gcore/src/provisioning/hub.rs:29-34]
[crates/gcore/src/provisioning/hub.rs:38-41]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `EnsureHubOptions` | class | `pub struct EnsureHubOptions {` | `EnsureHubOptions [class]` | `7751c0be-7f2d-58fc-94b9-35fc101e2af6` | 4-9 [crates/gcore/src/provisioning/hub.rs:4-9] | Indexed class `EnsureHubOptions` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:4-9] |
| `EnsureHubOptions::new` | method | `pub fn new(gobby_home: PathBuf) -> Self {` | `EnsureHubOptions::new [method]` | `9e324f77-80a7-5ec4-833b-98e50caac48d` | 12-19 [crates/gcore/src/provisioning/hub.rs:12-19] | Indexed method `EnsureHubOptions::new` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:12-19] |
| `HubIdentity` | class | `pub struct HubIdentity {` | `HubIdentity [class]` | `7ab65b74-081e-5228-9689-f084439be5d6` | 23-26 [crates/gcore/src/provisioning/hub.rs:23-26] | Indexed class `HubIdentity` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:23-26] |
| `HubIdentity::display_label` | method | `fn display_label(&self) -> String {` | `HubIdentity::display_label [method]` | `96f0de14-d7d2-5daa-a460-09ac19092930` | 29-34 [crates/gcore/src/provisioning/hub.rs:29-34] | Indexed method `HubIdentity::display_label` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:29-34] |
| `HubIdentityProbeResult` | type | `pub enum HubIdentityProbeResult {` | `HubIdentityProbeResult [type]` | `0ad02dfc-1d6d-56f8-a76f-830cfdc2f7fc` | 38-41 [crates/gcore/src/provisioning/hub.rs:38-41] | Indexed type `HubIdentityProbeResult` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:38-41] |
| `RecordedHubIdentityStatus` | type | `pub enum RecordedHubIdentityStatus {` | `RecordedHubIdentityStatus [type]` | `6827e75f-b20a-5f87-9354-8119b11785e1` | 44-48 [crates/gcore/src/provisioning/hub.rs:44-48] | Indexed type `RecordedHubIdentityStatus` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:44-48] |
| `RecordedHubResolution` | class | `pub struct RecordedHubResolution {` | `RecordedHubResolution [class]` | `60d1616f-3bb4-5d1e-81eb-dcdaa4b69c39` | 51-54 [crates/gcore/src/provisioning/hub.rs:51-54] | Indexed class `RecordedHubResolution` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:51-54] |
| `ensure_hub` | function | `pub fn ensure_hub(` | `ensure_hub [function]` | `0fa50ba7-0ca4-598a-966c-2b00eaee5f8a` | 56-66 [crates/gcore/src/provisioning/hub.rs:56-66] | Indexed function `ensure_hub` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:56-66] |
| `ensure_hub_with` | function | `pub(crate) fn ensure_hub_with(` | `ensure_hub_with [function]` | `bf134ad9-1612-5787-810c-cccc5ca7577c` | 69-87 [crates/gcore/src/provisioning/hub.rs:69-87] | Indexed function `ensure_hub_with` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:69-87] |
| `ensure_hub_with_identity` | function | `pub(crate) fn ensure_hub_with_identity(` | `ensure_hub_with_identity [function]` | `1a20a85b-4eb8-5056-8b13-57f778074bd0` | 89-167 [crates/gcore/src/provisioning/hub.rs:89-167] | Indexed function `ensure_hub_with_identity` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:89-167] |
| `resolve_recorded_hub_database_url` | function | `pub fn resolve_recorded_hub_database_url(` | `resolve_recorded_hub_database_url [function]` | `f27d3644-1a61-5b9e-8a46-ad64583cc1b5` | 169-279 [crates/gcore/src/provisioning/hub.rs:169-279] | Indexed function `resolve_recorded_hub_database_url` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:169-279] |
| `redacted_postgres_dsn_placeholder` | function | `fn redacted_postgres_dsn_placeholder(source: &str) -> String {` | `redacted_postgres_dsn_placeholder [function]` | `07c374c8-4a5e-559f-b908-12259969db93` | 281-283 [crates/gcore/src/provisioning/hub.rs:281-283] | Indexed function `redacted_postgres_dsn_placeholder` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:281-283] |
| `probe_postgres_hub_identity` | function | `pub fn probe_postgres_hub_identity(database_url: &str) -> anyhow::Result<HubIdentityProbeResult> {` | `probe_postgres_hub_identity [function]` | `1519ba59-ea5b-516e-812a-fb74f776f9c9` | 286-337 [crates/gcore/src/provisioning/hub.rs:286-337] | Indexed function `probe_postgres_hub_identity` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:286-337] |
| `insufficient_privilege` | function | `fn insufficient_privilege(error: &postgres::Error) -> bool {` | `insufficient_privilege [function]` | `38cb7d20-0e5a-5cea-87fd-749e2c07c27f` | 290-292 [crates/gcore/src/provisioning/hub.rs:290-292] | Indexed function `insufficient_privilege` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:290-292] |
| `probe_postgres_hub_identity` | function | `pub fn probe_postgres_hub_identity(_database_url: &str) -> anyhow::Result<HubIdentityProbeResult> {` | `probe_postgres_hub_identity [function]` | `43a85461-3db0-58b9-93f4-668f24423701` | 340-344 [crates/gcore/src/provisioning/hub.rs:340-344] | Indexed function `probe_postgres_hub_identity` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:340-344] |
| `HubDatabaseUrlSource` | type | `enum HubDatabaseUrlSource {` | `HubDatabaseUrlSource [type]` | `de73d338-72ba-5eff-8852-5d62328c2233` | 347-352 [crates/gcore/src/provisioning/hub.rs:347-352] | Indexed type `HubDatabaseUrlSource` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:347-352] |
| `HubDatabaseUrl` | class | `struct HubDatabaseUrl {` | `HubDatabaseUrl [class]` | `cf7cbf50-3223-53cb-9747-d42aaabb8091` | 355-358 [crates/gcore/src/provisioning/hub.rs:355-358] | Indexed class `HubDatabaseUrl` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:355-358] |
| `resolve_hub_database_urls` | function | `fn resolve_hub_database_urls(` | `resolve_hub_database_urls [function]` | `04f6fb3c-7427-5b7f-a517-ae402df5d8ba` | 360-396 [crates/gcore/src/provisioning/hub.rs:360-396] | Indexed function `resolve_hub_database_urls` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:360-396] |
| `resolve_database_url_from_gcore_config` | function | `fn resolve_database_url_from_gcore_config(home: &Path) -> anyhow::Result<Option<String>> {` | `resolve_database_url_from_gcore_config [function]` | `d406e49b-658d-58a4-a073-ac9929ff28e9` | 398-408 [crates/gcore/src/provisioning/hub.rs:398-408] | Indexed function `resolve_database_url_from_gcore_config` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:398-408] |
| `HubBootstrap` | class | `struct HubBootstrap {` | `HubBootstrap [class]` | `0fdb8183-1058-5fcc-b004-b405b8078378` | 411-414 [crates/gcore/src/provisioning/hub.rs:411-414] | Indexed class `HubBootstrap` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:411-414] |
| `resolve_database_url_from_bootstrap_file` | function | `fn resolve_database_url_from_bootstrap_file(path: &Path) -> anyhow::Result<Option<String>> {` | `resolve_database_url_from_bootstrap_file [function]` | `cc00b96c-d159-59ea-806d-dbe460fe29f5` | 416-428 [crates/gcore/src/provisioning/hub.rs:416-428] | Indexed function `resolve_database_url_from_bootstrap_file` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:416-428] |
| `non_empty_trimmed` | function | `fn non_empty_trimmed(value: Option<String>) -> Option<String> {` | `non_empty_trimmed [function]` | `46462147-3f5c-5912-99ef-8aaece7a0c4e` | 430-437 [crates/gcore/src/provisioning/hub.rs:430-437] | Indexed function `non_empty_trimmed` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:430-437] |
| `postgres_database_reachable` | function | `fn postgres_database_reachable(database_url: &str) -> bool {` | `postgres_database_reachable [function]` | `91f4d94b-f570-5148-b91c-daa3e21427fe` | 440-442 [crates/gcore/src/provisioning/hub.rs:440-442] | Indexed function `postgres_database_reachable` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:440-442] |
| `postgres_database_reachable` | function | `fn postgres_database_reachable(_database_url: &str) -> bool {` | `postgres_database_reachable [function]` | `048545f2-e259-5919-86eb-1cb59fe0e036` | 445-447 [crates/gcore/src/provisioning/hub.rs:445-447] | Indexed function `postgres_database_reachable` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:445-447] |
| `explicit_database_url_reachable` | function | `fn explicit_database_url_reachable(` | `explicit_database_url_reachable [function]` | `5ca78e2d-a136-5487-affc-5329c3623ad3` | 450-455 [crates/gcore/src/provisioning/hub.rs:450-455] | Indexed function `explicit_database_url_reachable` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:450-455] |
| `explicit_database_url_reachable` | function | `fn explicit_database_url_reachable(` | `explicit_database_url_reachable [function]` | `1f5ca7c9-ef07-5084-928b-3324f656a231` | 458-470 [crates/gcore/src/provisioning/hub.rs:458-470] | Indexed function `explicit_database_url_reachable` in `crates/gcore/src/provisioning/hub.rs`. [crates/gcore/src/provisioning/hub.rs:458-470] |
