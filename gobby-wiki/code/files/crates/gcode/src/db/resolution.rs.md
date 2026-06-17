---
title: crates/gcode/src/db/resolution.rs
type: code_file
provenance:
- file: crates/gcode/src/db/resolution.rs
  ranges:
  - 16-18
  - 21-24
  - 27-29
  - 31-33
  - 39-48
  - 51-64
  - 67-81
  - 83-138
  - 140-156
  - 158-166
  - 168-175
  - 177-186
  - 188-211
  - 213-226
  - 228-235
  - 237-244
  - 246-255
  - 257-280
  - 282-284
  - 286-300
  - 302-323
  - 325-353
  - 362-367
  - 370-378
  - 381-388
  - 391-399
  - 402-417
  - 420-432
  - 435-452
  - 455-472
  - 475-500
  - 503-511
  - 514-521
  - 524-529
  - 532-537
  - 540-552
  - 555-572
  - 575-583
  - 586-597
  - 600-604
  - 607-613
  - 616-622
  - 625-633
  - 636-648
  - 651-665
  - 668-682
  - 685-696
  - 699-711
  - 714-722
  - 725-733
  - 736-744
  - 746-754
  - 756-761
  - 763-765
  - 767-794
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/db/resolution.rs:16-18](crates/gcode/src/db/resolution.rs#L16-L18), [crates/gcode/src/db/resolution.rs:21-24](crates/gcode/src/db/resolution.rs#L21-L24), [crates/gcode/src/db/resolution.rs:27-29](crates/gcode/src/db/resolution.rs#L27-L29), [crates/gcode/src/db/resolution.rs:31-33](crates/gcode/src/db/resolution.rs#L31-L33), [crates/gcode/src/db/resolution.rs:39-48](crates/gcode/src/db/resolution.rs#L39-L48), [crates/gcode/src/db/resolution.rs:51-64](crates/gcode/src/db/resolution.rs#L51-L64), [crates/gcode/src/db/resolution.rs:67-81](crates/gcode/src/db/resolution.rs#L67-L81), [crates/gcode/src/db/resolution.rs:83-138](crates/gcode/src/db/resolution.rs#L83-L138), [crates/gcode/src/db/resolution.rs:140-156](crates/gcode/src/db/resolution.rs#L140-L156), [crates/gcode/src/db/resolution.rs:158-166](crates/gcode/src/db/resolution.rs#L158-L166), [crates/gcode/src/db/resolution.rs:168-175](crates/gcode/src/db/resolution.rs#L168-L175), [crates/gcode/src/db/resolution.rs:177-186](crates/gcode/src/db/resolution.rs#L177-L186), [crates/gcode/src/db/resolution.rs:188-211](crates/gcode/src/db/resolution.rs#L188-L211), [crates/gcode/src/db/resolution.rs:213-226](crates/gcode/src/db/resolution.rs#L213-L226), [crates/gcode/src/db/resolution.rs:228-235](crates/gcode/src/db/resolution.rs#L228-L235), [crates/gcode/src/db/resolution.rs:237-244](crates/gcode/src/db/resolution.rs#L237-L244), [crates/gcode/src/db/resolution.rs:246-255](crates/gcode/src/db/resolution.rs#L246-L255), [crates/gcode/src/db/resolution.rs:257-280](crates/gcode/src/db/resolution.rs#L257-L280), [crates/gcode/src/db/resolution.rs:282-284](crates/gcode/src/db/resolution.rs#L282-L284), [crates/gcode/src/db/resolution.rs:286-300](crates/gcode/src/db/resolution.rs#L286-L300), [crates/gcode/src/db/resolution.rs:302-323](crates/gcode/src/db/resolution.rs#L302-L323), [crates/gcode/src/db/resolution.rs:325-353](crates/gcode/src/db/resolution.rs#L325-L353), [crates/gcode/src/db/resolution.rs:362-367](crates/gcode/src/db/resolution.rs#L362-L367), [crates/gcode/src/db/resolution.rs:370-378](crates/gcode/src/db/resolution.rs#L370-L378), [crates/gcode/src/db/resolution.rs:381-388](crates/gcode/src/db/resolution.rs#L381-L388), [crates/gcode/src/db/resolution.rs:391-399](crates/gcode/src/db/resolution.rs#L391-L399), [crates/gcode/src/db/resolution.rs:402-417](crates/gcode/src/db/resolution.rs#L402-L417), [crates/gcode/src/db/resolution.rs:420-432](crates/gcode/src/db/resolution.rs#L420-L432), [crates/gcode/src/db/resolution.rs:435-452](crates/gcode/src/db/resolution.rs#L435-L452), [crates/gcode/src/db/resolution.rs:455-472](crates/gcode/src/db/resolution.rs#L455-L472), [crates/gcode/src/db/resolution.rs:475-500](crates/gcode/src/db/resolution.rs#L475-L500), [crates/gcode/src/db/resolution.rs:503-511](crates/gcode/src/db/resolution.rs#L503-L511), [crates/gcode/src/db/resolution.rs:514-521](crates/gcode/src/db/resolution.rs#L514-L521), [crates/gcode/src/db/resolution.rs:524-529](crates/gcode/src/db/resolution.rs#L524-L529), [crates/gcode/src/db/resolution.rs:532-537](crates/gcode/src/db/resolution.rs#L532-L537), [crates/gcode/src/db/resolution.rs:540-552](crates/gcode/src/db/resolution.rs#L540-L552), [crates/gcode/src/db/resolution.rs:555-572](crates/gcode/src/db/resolution.rs#L555-L572), [crates/gcode/src/db/resolution.rs:575-583](crates/gcode/src/db/resolution.rs#L575-L583), [crates/gcode/src/db/resolution.rs:586-597](crates/gcode/src/db/resolution.rs#L586-L597), [crates/gcode/src/db/resolution.rs:600-604](crates/gcode/src/db/resolution.rs#L600-L604), [crates/gcode/src/db/resolution.rs:607-613](crates/gcode/src/db/resolution.rs#L607-L613), [crates/gcode/src/db/resolution.rs:616-622](crates/gcode/src/db/resolution.rs#L616-L622), [crates/gcode/src/db/resolution.rs:625-633](crates/gcode/src/db/resolution.rs#L625-L633), [crates/gcode/src/db/resolution.rs:636-648](crates/gcode/src/db/resolution.rs#L636-L648), [crates/gcode/src/db/resolution.rs:651-665](crates/gcode/src/db/resolution.rs#L651-L665), [crates/gcode/src/db/resolution.rs:668-682](crates/gcode/src/db/resolution.rs#L668-L682), [crates/gcode/src/db/resolution.rs:685-696](crates/gcode/src/db/resolution.rs#L685-L696), [crates/gcode/src/db/resolution.rs:699-711](crates/gcode/src/db/resolution.rs#L699-L711), [crates/gcode/src/db/resolution.rs:714-722](crates/gcode/src/db/resolution.rs#L714-L722), [crates/gcode/src/db/resolution.rs:725-733](crates/gcode/src/db/resolution.rs#L725-L733), [crates/gcode/src/db/resolution.rs:736-744](crates/gcode/src/db/resolution.rs#L736-L744), [crates/gcode/src/db/resolution.rs:746-754](crates/gcode/src/db/resolution.rs#L746-L754), [crates/gcode/src/db/resolution.rs:756-761](crates/gcode/src/db/resolution.rs#L756-L761), [crates/gcode/src/db/resolution.rs:763-765](crates/gcode/src/db/resolution.rs#L763-L765), [crates/gcode/src/db/resolution.rs:767-794](crates/gcode/src/db/resolution.rs#L767-L794)

</details>

# crates/gcode/src/db/resolution.rs

Module: [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Purpose

Resolves the gcode PostgreSQL hub database URL from a layered set of sources, with validation and bootstrap support for daemoned and daemonless operation. It starts from `gobby_home`/`bootstrap_path`, then tries broker resolution, environment overrides, recorded bootstrap config, and gcore config in priority order, using helper functions to parse bootstrap data, filter empty values, and verify the resulting URL and database reachability. The broker path reads a local CLI token, sends it to a loopback daemon with a configurable timeout, and accepts only well-formed PostgreSQL URLs; the rest of the file is mostly test coverage for precedence, parsing, timeout handling, and failure cases.
[crates/gcode/src/db/resolution.rs:16-18]
[crates/gcode/src/db/resolution.rs:21-24]
[crates/gcode/src/db/resolution.rs:27-29]
[crates/gcode/src/db/resolution.rs:31-33]
[crates/gcode/src/db/resolution.rs:39-48]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `BrokerDatabaseUrlResponse` | class | `struct BrokerDatabaseUrlResponse {` | `BrokerDatabaseUrlResponse [class]` | `e1a47bd4-8488-57c2-b9f3-fe11f328e9ee` | 16-18 [crates/gcode/src/db/resolution.rs:16-18] | Indexed class `BrokerDatabaseUrlResponse` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:16-18] |
| `BootstrapDatabase` | class | `struct BootstrapDatabase {` | `BootstrapDatabase [class]` | `a4a8ec5f-8b7e-56f7-b7b0-98451701ff1b` | 21-24 [crates/gcode/src/db/resolution.rs:21-24] | Indexed class `BootstrapDatabase` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:21-24] |
| `gobby_home` | function | `pub fn gobby_home() -> anyhow::Result<PathBuf> {` | `gobby_home [function]` | `abf8feb8-2b7f-59c8-a22b-3b7b171bead7` | 27-29 [crates/gcode/src/db/resolution.rs:27-29] | Indexed function `gobby_home` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:27-29] |
| `bootstrap_path` | function | `pub fn bootstrap_path() -> anyhow::Result<PathBuf> {` | `bootstrap_path [function]` | `2d5e07d4-698a-547c-9493-86b1404eb7f7` | 31-33 [crates/gcode/src/db/resolution.rs:31-33] | Indexed function `bootstrap_path` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:31-33] |
| `resolve_database_url` | function | `pub fn resolve_database_url() -> anyhow::Result<String> {` | `resolve_database_url [function]` | `62e0931c-0f59-5d70-aee0-e3a67f5cd70b` | 39-48 [crates/gcode/src/db/resolution.rs:39-48] | Indexed function `resolve_database_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:39-48] |
| `resolve_database_url_from_sources` | function | `fn resolve_database_url_from_sources(` | `resolve_database_url_from_sources [function]` | `2eb15708-e3e4-5511-80ba-28078ec3c819` | 51-64 [crates/gcode/src/db/resolution.rs:51-64] | Indexed function `resolve_database_url_from_sources` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:51-64] |
| `resolve_database_url_from_sources_with_identity` | function | `fn resolve_database_url_from_sources_with_identity(` | `resolve_database_url_from_sources_with_identity [function]` | `14f5c3a0-921c-5ad1-87ac-2cfcec180161` | 67-81 [crates/gcode/src/db/resolution.rs:67-81] | Indexed function `resolve_database_url_from_sources_with_identity` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:67-81] |
| `resolve_database_url_from_sources_with_identity_and_reachability` | function | `fn resolve_database_url_from_sources_with_identity_and_reachability(` | `resolve_database_url_from_sources_with_identity_and_reachability [function]` | `195bd3ff-a7ef-5a63-91b1-ab7762b1edf9` | 83-138 [crates/gcode/src/db/resolution.rs:83-138] | Indexed function `resolve_database_url_from_sources_with_identity_and_reachability` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:83-138] |
| `resolve_recorded_hub_database_url` | function | `fn resolve_recorded_hub_database_url(` | `resolve_recorded_hub_database_url [function]` | `5bc0cad3-9212-5aba-a753-cbefe56a1abf` | 140-156 [crates/gcode/src/db/resolution.rs:140-156] | Indexed function `resolve_recorded_hub_database_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:140-156] |
| `resolve_database_url_from_bootstrap_file` | function | `fn resolve_database_url_from_bootstrap_file(path: &Path) -> anyhow::Result<Option<String>> {` | `resolve_database_url_from_bootstrap_file [function]` | `61681180-8d76-5562-94de-2dbce8c9144b` | 158-166 [crates/gcode/src/db/resolution.rs:158-166] | Indexed function `resolve_database_url_from_bootstrap_file` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:158-166] |
| `resolve_database_url_from_gcore_config` | function | `fn resolve_database_url_from_gcore_config(home: &Path) -> anyhow::Result<Option<String>> {` | `resolve_database_url_from_gcore_config [function]` | `20fd61b6-3117-5b9a-93b0-14ff0ea8b39a` | 168-175 [crates/gcode/src/db/resolution.rs:168-175] | Indexed function `resolve_database_url_from_gcore_config` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:168-175] |
| `resolve_database_url_from_env` | function | `fn resolve_database_url_from_env(` | `resolve_database_url_from_env [function]` | `4bd03715-17ec-5950-ae70-0671e91e616a` | 177-186 [crates/gcode/src/db/resolution.rs:177-186] | Indexed function `resolve_database_url_from_env` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:177-186] |
| `parse_bootstrap_database` | function | `fn parse_bootstrap_database(contents: &str) -> anyhow::Result<BootstrapDatabase> {` | `parse_bootstrap_database [function]` | `882e9b8a-ebab-5fab-97bf-5e32f701c6d8` | 188-211 [crates/gcode/src/db/resolution.rs:188-211] | Indexed function `parse_bootstrap_database` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:188-211] |
| `resolve_database_url_from_bootstrap` | function | `fn resolve_database_url_from_bootstrap(bootstrap: &BootstrapDatabase) -> anyhow::Result<String> {` | `resolve_database_url_from_bootstrap [function]` | `f05288c3-69df-520e-be0c-d278c7d01b7a` | 213-226 [crates/gcode/src/db/resolution.rs:213-226] | Indexed function `resolve_database_url_from_bootstrap` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:213-226] |
| `non_empty_trimmed` | function | `fn non_empty_trimmed(value: Option<String>) -> Option<String> {` | `non_empty_trimmed [function]` | `731e2901-3f38-57dc-bead-ea5470c45727` | 228-235 [crates/gcode/src/db/resolution.rs:228-235] | Indexed function `non_empty_trimmed` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:228-235] |
| `resolve_brokered_database_url_at` | function | `fn resolve_brokered_database_url_at(` | `resolve_brokered_database_url_at [function]` | `b73be4b7-f3af-53af-ada1-32d201a0f27a` | 237-244 [crates/gcode/src/db/resolution.rs:237-244] | Indexed function `resolve_brokered_database_url_at` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:237-244] |
| `read_local_cli_token_at` | function | `fn read_local_cli_token_at(gobby_home: &Path) -> anyhow::Result<String> {` | `read_local_cli_token_at [function]` | `248d9efb-c1f7-5501-aec9-a1ea837a2d7a` | 246-255 [crates/gcode/src/db/resolution.rs:246-255] | Indexed function `read_local_cli_token_at` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:246-255] |
| `request_broker_database_url` | function | `fn request_broker_database_url(daemon_url: &str, token: &str) -> anyhow::Result<String> {` | `request_broker_database_url [function]` | `60cd637f-925d-5638-95af-884e02f0d7a7` | 257-280 [crates/gcode/src/db/resolution.rs:257-280] | Indexed function `request_broker_database_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:257-280] |
| `broker_timeout` | function | `fn broker_timeout() -> Duration {` | `broker_timeout [function]` | `34b739a1-8fa3-54dd-addd-24326b488f9f` | 282-284 [crates/gcode/src/db/resolution.rs:282-284] | Indexed function `broker_timeout` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:282-284] |
| `broker_timeout_from_env` | function | `fn broker_timeout_from_env(env: impl Fn(&str) -> Option<String>) -> Duration {` | `broker_timeout_from_env [function]` | `6635c09c-dd4b-5ac5-8026-f8ba7f8043c2` | 286-300 [crates/gcode/src/db/resolution.rs:286-300] | Indexed function `broker_timeout_from_env` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:286-300] |
| `validate_loopback_daemon_url` | function | `fn validate_loopback_daemon_url(daemon_url: &str) -> anyhow::Result<()> {` | `validate_loopback_daemon_url [function]` | `d3d7be68-0422-5599-a960-b776ca36e123` | 302-323 [crates/gcode/src/db/resolution.rs:302-323] | Indexed function `validate_loopback_daemon_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:302-323] |
| `validate_broker_database_url` | function | `fn validate_broker_database_url(database_url: &str) -> anyhow::Result<String> {` | `validate_broker_database_url [function]` | `8170e4c7-35e6-5066-ba6d-4760164f2f5d` | 325-353 [crates/gcode/src/db/resolution.rs:325-353] | Indexed function `validate_broker_database_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:325-353] |
| `bootstrap` | function | `fn bootstrap(hub_backend: &str, database_url: Option<&str>) -> BootstrapDatabase {` | `bootstrap [function]` | `7928ce0e-d6f7-5d2f-aa5b-055adb4f1117` | 362-367 [crates/gcode/src/db/resolution.rs:362-367] | Indexed function `bootstrap` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:362-367] |
| `database_url_env_prefers_gcode_specific_var` | function | `fn database_url_env_prefers_gcode_specific_var() {` | `database_url_env_prefers_gcode_specific_var [function]` | `ceb3e7e0-7825-55aa-8212-9c9f66a8acbc` | 370-378 [crates/gcode/src/db/resolution.rs:370-378] | Indexed function `database_url_env_prefers_gcode_specific_var` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:370-378] |
| `database_url_env_falls_back_to_gobby_postgres_dsn` | function | `fn database_url_env_falls_back_to_gobby_postgres_dsn() {` | `database_url_env_falls_back_to_gobby_postgres_dsn [function]` | `1e9f51d8-920f-5189-a1eb-e676d4b4f0cc` | 381-388 [crates/gcode/src/db/resolution.rs:381-388] | Indexed function `database_url_env_falls_back_to_gobby_postgres_dsn` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:381-388] |
| `database_url_env_ignores_empty_values` | function | `fn database_url_env_ignores_empty_values() {` | `database_url_env_ignores_empty_values [function]` | `d1770dc2-5349-54c4-97d0-ae0cb69585a7` | 391-399 [crates/gcode/src/db/resolution.rs:391-399] | Indexed function `database_url_env_ignores_empty_values` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:391-399] |
| `database_url_sources_prefer_env_over_daemon_broker` | function | `fn database_url_sources_prefer_env_over_daemon_broker() {` | `database_url_sources_prefer_env_over_daemon_broker [function]` | `4c814114-0977-5503-82e1-8db30e783288` | 402-417 [crates/gcode/src/db/resolution.rs:402-417] | Indexed function `database_url_sources_prefer_env_over_daemon_broker` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:402-417] |
| `database_url_sources_use_daemon_broker_after_env` | function | `fn database_url_sources_use_daemon_broker_after_env() {` | `database_url_sources_use_daemon_broker_after_env [function]` | `8f222e02-ecf8-5cb3-98de-9d70a122e8e9` | 420-432 [crates/gcode/src/db/resolution.rs:420-432] | Indexed function `database_url_sources_use_daemon_broker_after_env` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:420-432] |
| `database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable` | function | `fn database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable() {` | `database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable [function]` | `693476f8-f3ce-5a0a-8ce0-f8dc4850f406` | 435-452 [crates/gcode/src/db/resolution.rs:435-452] | Indexed function `database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:435-452] |
| `database_url_sources_use_gcore_after_daemon_and_bootstrap` | function | `fn database_url_sources_use_gcore_after_daemon_and_bootstrap() {` | `database_url_sources_use_gcore_after_daemon_and_bootstrap [function]` | `05dc0ea7-ef9e-557a-bdbe-16f72a6914da` | 455-472 [crates/gcode/src/db/resolution.rs:455-472] | Indexed function `database_url_sources_use_gcore_after_daemon_and_bootstrap` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:455-472] |
| `adopted_hub_resolves_without_conflict` | function | `fn adopted_hub_resolves_without_conflict() {` | `adopted_hub_resolves_without_conflict [function]` | `bae371fd-bdce-5ca6-a0f3-ffddf4b8aa90` | 475-500 [crates/gcode/src/db/resolution.rs:475-500] | Indexed function `adopted_hub_resolves_without_conflict` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:475-500] |
| `postgres_bootstrap_accepts_inline_url` | function | `fn postgres_bootstrap_accepts_inline_url() {` | `postgres_bootstrap_accepts_inline_url [function]` | `e5fd214d-eb81-542e-bd5a-73eb0e17267b` | 503-511 [crates/gcode/src/db/resolution.rs:503-511] | Indexed function `postgres_bootstrap_accepts_inline_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:503-511] |
| `non_postgres_bootstrap_fails_clearly` | function | `fn non_postgres_bootstrap_fails_clearly() {` | `non_postgres_bootstrap_fails_clearly [function]` | `d372b49d-7b5b-5db2-94c7-a63dc6ba6eed` | 514-521 [crates/gcode/src/db/resolution.rs:514-521] | Indexed function `non_postgres_bootstrap_fails_clearly` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:514-521] |
| `missing_hub_backend_fails_clearly` | function | `fn missing_hub_backend_fails_clearly() {` | `missing_hub_backend_fails_clearly [function]` | `132008a8-f931-5acc-badf-e5d5d56063ff` | 524-529 [crates/gcode/src/db/resolution.rs:524-529] | Indexed function `missing_hub_backend_fails_clearly` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:524-529] |
| `missing_postgres_dsn_fails_clearly` | function | `fn missing_postgres_dsn_fails_clearly() {` | `missing_postgres_dsn_fails_clearly [function]` | `11114b11-3e11-59f1-b5b9-c42abd078123` | 532-537 [crates/gcode/src/db/resolution.rs:532-537] | Indexed function `missing_postgres_dsn_fails_clearly` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:532-537] |
| `parse_bootstrap_database_reads_postgres_fields` | function | `fn parse_bootstrap_database_reads_postgres_fields() {` | `parse_bootstrap_database_reads_postgres_fields [function]` | `a8b6e9ea-2e1e-5ef1-9849-edad058c1246` | 540-552 [crates/gcode/src/db/resolution.rs:540-552] | Indexed function `parse_bootstrap_database_reads_postgres_fields` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:540-552] |
| `broker_request_returns_database_url_and_sends_local_token` | function | `fn broker_request_returns_database_url_and_sends_local_token() {` | `broker_request_returns_database_url_and_sends_local_token [function]` | `edab86ee-085d-5f66-84f0-20d49facd6b4` | 555-572 [crates/gcode/src/db/resolution.rs:555-572] | Indexed function `broker_request_returns_database_url_and_sends_local_token` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:555-572] |
| `broker_request_rejects_non_loopback_daemon_url_before_sending_local_token` | function | `fn broker_request_rejects_non_loopback_daemon_url_before_sending_local_token() {` | `broker_request_rejects_non_loopback_daemon_url_before_sending_local_token [function]` | `26510a28-69d3-5381-a2f8-5af92b456d41` | 575-583 [crates/gcode/src/db/resolution.rs:575-583] | Indexed function `broker_request_rejects_non_loopback_daemon_url_before_sending_local_token` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:575-583] |
| `broker_request_allows_cold_daemon_latency` | function | `fn broker_request_allows_cold_daemon_latency() {` | `broker_request_allows_cold_daemon_latency [function]` | `0d8e4e28-deab-5aec-95e8-01a57ddaf503` | 586-597 [crates/gcode/src/db/resolution.rs:586-597] | Indexed function `broker_request_allows_cold_daemon_latency` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:586-597] |
| `broker_timeout_defaults_to_seven_seconds` | function | `fn broker_timeout_defaults_to_seven_seconds() {` | `broker_timeout_defaults_to_seven_seconds [function]` | `f98ef5c5-95d9-5e2e-b4f4-835edf4ddf71` | 600-604 [crates/gcode/src/db/resolution.rs:600-604] | Indexed function `broker_timeout_defaults_to_seven_seconds` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:600-604] |
| `broker_timeout_reads_positive_env_value` | function | `fn broker_timeout_reads_positive_env_value() {` | `broker_timeout_reads_positive_env_value [function]` | `6c1402bd-165b-55d2-ae65-aaad2d1e713d` | 607-613 [crates/gcode/src/db/resolution.rs:607-613] | Indexed function `broker_timeout_reads_positive_env_value` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:607-613] |
| `broker_timeout_ignores_invalid_env_value` | function | `fn broker_timeout_ignores_invalid_env_value() {` | `broker_timeout_ignores_invalid_env_value [function]` | `ec03e1fa-d8fa-5dbd-91a9-0d72195a5d3f` | 616-622 [crates/gcode/src/db/resolution.rs:616-622] | Indexed function `broker_timeout_ignores_invalid_env_value` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:616-622] |
| `broker_missing_token_fails` | function | `fn broker_missing_token_fails() {` | `broker_missing_token_fails [function]` | `b632aba3-0f0f-546e-9b2d-37b2c3b8f66d` | 625-633 [crates/gcode/src/db/resolution.rs:625-633] | Indexed function `broker_missing_token_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:625-633] |
| `broker_daemon_down_fails` | function | `fn broker_daemon_down_fails() {` | `broker_daemon_down_fails [function]` | `f45f6c51-249a-54d8-b797-bef949997bdc` | 636-648 [crates/gcode/src/db/resolution.rs:636-648] | Indexed function `broker_daemon_down_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:636-648] |
| `broker_auth_failure_fails` | function | `fn broker_auth_failure_fails() {` | `broker_auth_failure_fails [function]` | `e52f4392-fd13-57b8-a8f5-bbbc74615199` | 651-665 [crates/gcode/src/db/resolution.rs:651-665] | Indexed function `broker_auth_failure_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:651-665] |
| `broker_non_success_status_fails` | function | `fn broker_non_success_status_fails() {` | `broker_non_success_status_fails [function]` | `45b2ab8a-3d84-5151-99ce-3ce3bd420638` | 668-682 [crates/gcode/src/db/resolution.rs:668-682] | Indexed function `broker_non_success_status_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:668-682] |
| `broker_invalid_json_fails` | function | `fn broker_invalid_json_fails() {` | `broker_invalid_json_fails [function]` | `25cdbc95-780b-5f77-bf31-e6287089462c` | 685-696 [crates/gcode/src/db/resolution.rs:685-696] | Indexed function `broker_invalid_json_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:685-696] |
| `broker_empty_database_url_fails` | function | `fn broker_empty_database_url_fails() {` | `broker_empty_database_url_fails [function]` | `4fc29167-b0a8-53df-b8fc-44c629729d14` | 699-711 [crates/gcode/src/db/resolution.rs:699-711] | Indexed function `broker_empty_database_url_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:699-711] |
| `broker_invalid_database_url_scheme_fails` | function | `fn broker_invalid_database_url_scheme_fails() {` | `broker_invalid_database_url_scheme_fails [function]` | `bfa5b0f2-1d34-5f63-a9fe-c1c5ebb469e3` | 714-722 [crates/gcode/src/db/resolution.rs:714-722] | Indexed function `broker_invalid_database_url_scheme_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:714-722] |
| `broker_missing_database_url_host_fails` | function | `fn broker_missing_database_url_host_fails() {` | `broker_missing_database_url_host_fails [function]` | `66b42ab9-dfe6-5365-b098-6acb7cdbd1f4` | 725-733 [crates/gcode/src/db/resolution.rs:725-733] | Indexed function `broker_missing_database_url_host_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:725-733] |
| `broker_missing_database_url_path_fails` | function | `fn broker_missing_database_url_path_fails() {` | `broker_missing_database_url_path_fails [function]` | `f06db841-f4c0-57ef-9705-213dc8e0de68` | 736-744 [crates/gcode/src/db/resolution.rs:736-744] | Indexed function `broker_missing_database_url_path_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:736-744] |
| `write_bootstrap` | function | `fn write_bootstrap(home: &Path, daemon_port: u16) -> PathBuf {` | `write_bootstrap [function]` | `cb84ebd0-8819-571a-9d40-0c4a16c14575` | 746-754 [crates/gcode/src/db/resolution.rs:746-754] | Indexed function `write_bootstrap` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:746-754] |
| `http_response` | function | `fn http_response(status: &str, body: &str) -> String {` | `http_response [function]` | `003ca858-885e-50ea-9283-6e4808dc4473` | 756-761 [crates/gcode/src/db/resolution.rs:756-761] | Indexed function `http_response` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:756-761] |
| `spawn_http_response` | function | `fn spawn_http_response(response: String) -> (String, thread::JoinHandle<String>) {` | `spawn_http_response [function]` | `f1d75b29-ef41-5e51-89d2-c8d5e1aa70fd` | 763-765 [crates/gcode/src/db/resolution.rs:763-765] | Indexed function `spawn_http_response` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:763-765] |
| `spawn_http_response_after` | function | `fn spawn_http_response_after(` | `spawn_http_response_after [function]` | `8d052b0a-d623-5bc9-beda-f07d7d3f786a` | 767-794 [crates/gcode/src/db/resolution.rs:767-794] | Indexed function `spawn_http_response_after` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:767-794] |
