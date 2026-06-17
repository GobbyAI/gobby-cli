---
title: crates/gcore/src/provisioning/docker.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/docker.rs
  ranges:
  - 9-18
  - 21-32
  - 34-36
  - 38-40
  - 44-49
  - 52-58
  - 61-66
  - 69-73
  - 75-77
  - '79'
  - 82-97
  - 100-104
  - 106-109
  - 112-117
  - 121-124
  - 126-142
  - 144-147
  - 150-156
  - 158-190
  - 192-271
  - 273-306
  - 309-313
  - 315-318
  - 320-331
  - 333-339
  - 341-362
  - 364-370
  - 372-382
  - 384-403
  - 405-418
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/provisioning/docker.rs:9-18](crates/gcore/src/provisioning/docker.rs#L9-L18), [crates/gcore/src/provisioning/docker.rs:21-32](crates/gcore/src/provisioning/docker.rs#L21-L32), [crates/gcore/src/provisioning/docker.rs:34-36](crates/gcore/src/provisioning/docker.rs#L34-L36), [crates/gcore/src/provisioning/docker.rs:38-40](crates/gcore/src/provisioning/docker.rs#L38-L40), [crates/gcore/src/provisioning/docker.rs:44-49](crates/gcore/src/provisioning/docker.rs#L44-L49), [crates/gcore/src/provisioning/docker.rs:52-58](crates/gcore/src/provisioning/docker.rs#L52-L58), [crates/gcore/src/provisioning/docker.rs:61-66](crates/gcore/src/provisioning/docker.rs#L61-L66), [crates/gcore/src/provisioning/docker.rs:69-73](crates/gcore/src/provisioning/docker.rs#L69-L73), [crates/gcore/src/provisioning/docker.rs:75-77](crates/gcore/src/provisioning/docker.rs#L75-L77), [crates/gcore/src/provisioning/docker.rs:79](crates/gcore/src/provisioning/docker.rs#L79), [crates/gcore/src/provisioning/docker.rs:82-97](crates/gcore/src/provisioning/docker.rs#L82-L97), [crates/gcore/src/provisioning/docker.rs:100-104](crates/gcore/src/provisioning/docker.rs#L100-L104), [crates/gcore/src/provisioning/docker.rs:106-109](crates/gcore/src/provisioning/docker.rs#L106-L109), [crates/gcore/src/provisioning/docker.rs:112-117](crates/gcore/src/provisioning/docker.rs#L112-L117), [crates/gcore/src/provisioning/docker.rs:121-124](crates/gcore/src/provisioning/docker.rs#L121-L124), [crates/gcore/src/provisioning/docker.rs:126-142](crates/gcore/src/provisioning/docker.rs#L126-L142), [crates/gcore/src/provisioning/docker.rs:144-147](crates/gcore/src/provisioning/docker.rs#L144-L147), [crates/gcore/src/provisioning/docker.rs:150-156](crates/gcore/src/provisioning/docker.rs#L150-L156), [crates/gcore/src/provisioning/docker.rs:158-190](crates/gcore/src/provisioning/docker.rs#L158-L190), [crates/gcore/src/provisioning/docker.rs:192-271](crates/gcore/src/provisioning/docker.rs#L192-L271), [crates/gcore/src/provisioning/docker.rs:273-306](crates/gcore/src/provisioning/docker.rs#L273-L306), [crates/gcore/src/provisioning/docker.rs:309-313](crates/gcore/src/provisioning/docker.rs#L309-L313), [crates/gcore/src/provisioning/docker.rs:315-318](crates/gcore/src/provisioning/docker.rs#L315-L318), [crates/gcore/src/provisioning/docker.rs:320-331](crates/gcore/src/provisioning/docker.rs#L320-L331), [crates/gcore/src/provisioning/docker.rs:333-339](crates/gcore/src/provisioning/docker.rs#L333-L339), [crates/gcore/src/provisioning/docker.rs:341-362](crates/gcore/src/provisioning/docker.rs#L341-L362), [crates/gcore/src/provisioning/docker.rs:364-370](crates/gcore/src/provisioning/docker.rs#L364-L370), [crates/gcore/src/provisioning/docker.rs:372-382](crates/gcore/src/provisioning/docker.rs#L372-L382), [crates/gcore/src/provisioning/docker.rs:384-403](crates/gcore/src/provisioning/docker.rs#L384-L403), [crates/gcore/src/provisioning/docker.rs:405-418](crates/gcore/src/provisioning/docker.rs#L405-L418)

</details>

# crates/gcore/src/provisioning/docker.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Purpose

Provides Docker-based service provisioning for the gobby/gcore stack. `DockerServiceOptions` holds the home directory and container port/password defaults, with helpers for the database and Qdrant URLs; the report structs capture prepared assets and provisioning results. The command runner abstraction (`CommandSpec`, `CommandOutput`, `CommandRunner`, `RealCommandRunner`) executes external commands for compose operations, while `TcpDockerHealthChecker` waits for Postgres, Qdrant, and FalkorDB to become reachable. The top-level provisioning functions assemble service assets, write env and compose files, choose the Docker Compose `up` spec, and apply supporting utilities for manifest generation, architecture detection, env-file updates, readiness polling, and executable-file setup.
[crates/gcore/src/provisioning/docker.rs:9-18]
[crates/gcore/src/provisioning/docker.rs:21-32]
[crates/gcore/src/provisioning/docker.rs:34-36]
[crates/gcore/src/provisioning/docker.rs:38-40]
[crates/gcore/src/provisioning/docker.rs:44-49]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DockerServiceOptions` | class | `pub struct DockerServiceOptions {` | `DockerServiceOptions [class]` | `058087a3-9962-5e44-a6be-506dda77aae3` | 9-18 [crates/gcore/src/provisioning/docker.rs:9-18] | Indexed class `DockerServiceOptions` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:9-18] |
| `DockerServiceOptions::new` | method | `pub fn new(gobby_home: PathBuf) -> Self {` | `DockerServiceOptions::new [method]` | `d300ea36-004e-5579-9b5d-79d454d396ed` | 21-32 [crates/gcore/src/provisioning/docker.rs:21-32] | Indexed method `DockerServiceOptions::new` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:21-32] |
| `DockerServiceOptions::database_url` | method | `pub fn database_url(&self) -> String {` | `DockerServiceOptions::database_url [method]` | `f939c597-f88a-56e6-8c06-2bfb4e5ff7c0` | 34-36 [crates/gcore/src/provisioning/docker.rs:34-36] | Indexed method `DockerServiceOptions::database_url` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:34-36] |
| `DockerServiceOptions::qdrant_url` | method | `pub fn qdrant_url(&self) -> String {` | `DockerServiceOptions::qdrant_url [method]` | `870f641e-2314-58c6-aef3-55e022cb19bf` | 38-40 [crates/gcore/src/provisioning/docker.rs:38-40] | Indexed method `DockerServiceOptions::qdrant_url` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:38-40] |
| `ServiceAssetReport` | class | `pub struct ServiceAssetReport {` | `ServiceAssetReport [class]` | `b391095b-1212-57a2-8309-707c0a07df16` | 44-49 [crates/gcore/src/provisioning/docker.rs:44-49] | Indexed class `ServiceAssetReport` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:44-49] |
| `DockerProvisioningReport` | class | `pub struct DockerProvisioningReport {` | `DockerProvisioningReport [class]` | `a58a620b-bd7b-524a-aa2c-4b080a0d9296` | 52-58 [crates/gcore/src/provisioning/docker.rs:52-58] | Indexed class `DockerProvisioningReport` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:52-58] |
| `CommandSpec` | class | `pub struct CommandSpec {` | `CommandSpec [class]` | `bb1a4995-86d9-5bc9-b0b1-5145bb3d7cfd` | 61-66 [crates/gcore/src/provisioning/docker.rs:61-66] | Indexed class `CommandSpec` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:61-66] |
| `CommandOutput` | class | `pub struct CommandOutput {` | `CommandOutput [class]` | `a4ec36de-2f88-594f-81e3-049788542be7` | 69-73 [crates/gcore/src/provisioning/docker.rs:69-73] | Indexed class `CommandOutput` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:69-73] |
| `CommandRunner` | type | `pub trait CommandRunner {` | `CommandRunner [type]` | `6bf7d150-1d16-5452-bc2c-2c6f74305480` | 75-77 [crates/gcore/src/provisioning/docker.rs:75-77] | Indexed type `CommandRunner` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:75-77] |
| `RealCommandRunner` | class | `pub struct RealCommandRunner;` | `RealCommandRunner [class]` | `c078847c-c3b9-566a-9e45-9a7b785a3782` | 79-79 [crates/gcore/src/provisioning/docker.rs:79] | Indexed class `RealCommandRunner` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:79] |
| `RealCommandRunner::run` | method | `fn run(&mut self, spec: &CommandSpec) -> std::io::Result<CommandOutput> {` | `RealCommandRunner::run [method]` | `7f5b61ef-3bca-581b-8de1-bebc361641c0` | 82-97 [crates/gcore/src/provisioning/docker.rs:82-97] | Indexed method `RealCommandRunner::run` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:82-97] |
| `DockerHealthChecker` | type | `pub trait DockerHealthChecker {` | `DockerHealthChecker [type]` | `356a8faf-cf84-57fd-b125-1b8843f52650` | 100-104 [crates/gcore/src/provisioning/docker.rs:100-104] | Indexed type `DockerHealthChecker` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:100-104] |
| `TcpDockerHealthChecker` | class | `pub struct TcpDockerHealthChecker {` | `TcpDockerHealthChecker [class]` | `56773d94-cdfa-5e0f-9072-7f5b640367fb` | 106-109 [crates/gcore/src/provisioning/docker.rs:106-109] | Indexed class `TcpDockerHealthChecker` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:106-109] |
| `TcpDockerHealthChecker::default` | method | `fn default() -> Self {` | `TcpDockerHealthChecker::default [method]` | `b4cf94b7-7f25-5111-94f2-60496b945a63` | 112-117 [crates/gcore/src/provisioning/docker.rs:112-117] | Indexed method `TcpDockerHealthChecker::default` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:112-117] |
| `TcpDockerHealthChecker::wait_postgres` | method | `fn wait_postgres(&mut self, host: &str, port: u16) -> anyhow::Result<()> {` | `TcpDockerHealthChecker::wait_postgres [method]` | `0e53fcb4-e8a7-591d-b886-954df10640cd` | 121-124 [crates/gcore/src/provisioning/docker.rs:121-124] | Indexed method `TcpDockerHealthChecker::wait_postgres` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:121-124] |
| `TcpDockerHealthChecker::wait_qdrant` | method | `fn wait_qdrant(&mut self, host: &str, port: u16) -> anyhow::Result<()> {` | `TcpDockerHealthChecker::wait_qdrant [method]` | `47b37107-0c4b-5b85-bfb4-ae85292c8050` | 126-142 [crates/gcore/src/provisioning/docker.rs:126-142] | Indexed method `TcpDockerHealthChecker::wait_qdrant` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:126-142] |
| `TcpDockerHealthChecker::wait_falkordb` | method | `fn wait_falkordb(&mut self, host: &str, port: u16) -> anyhow::Result<()> {` | `TcpDockerHealthChecker::wait_falkordb [method]` | `90e58149-3764-5732-922f-a70c1a0eb734` | 144-147 [crates/gcore/src/provisioning/docker.rs:144-147] | Indexed method `TcpDockerHealthChecker::wait_falkordb` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:144-147] |
| `provision_docker_services` | function | `pub fn provision_docker_services(` | `provision_docker_services [function]` | `defc89f1-d9e0-53e3-a5dd-f183f30807e9` | 150-156 [crates/gcore/src/provisioning/docker.rs:150-156] | Indexed function `provision_docker_services` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:150-156] |
| `provision_docker_services_with` | function | `pub fn provision_docker_services_with(` | `provision_docker_services_with [function]` | `58066265-375c-54d2-ab57-80956ffdefa4` | 158-190 [crates/gcore/src/provisioning/docker.rs:158-190] | Indexed function `provision_docker_services_with` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:158-190] |
| `prepare_service_assets` | function | `pub fn prepare_service_assets(` | `prepare_service_assets [function]` | `3adcedf6-7f24-51bb-81a4-636a6584ac36` | 192-271 [crates/gcore/src/provisioning/docker.rs:192-271] | Indexed function `prepare_service_assets` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:192-271] |
| `docker_compose_up_spec` | function | `pub fn docker_compose_up_spec(` | `docker_compose_up_spec [function]` | `aa6292cb-da15-5f26-ab6b-b728ee107fdd` | 273-306 [crates/gcore/src/provisioning/docker.rs:273-306] | Indexed function `docker_compose_up_spec` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:273-306] |
| `PgSearchVersionFile` | class | `struct PgSearchVersionFile {` | `PgSearchVersionFile [class]` | `0202b323-b704-58d2-b097-604a0a40daed` | 309-313 [crates/gcore/src/provisioning/docker.rs:309-313] | Indexed class `PgSearchVersionFile` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:309-313] |
| `PgSearchManifest` | class | `struct PgSearchManifest {` | `PgSearchManifest [class]` | `f8ee2cd2-bea4-5ce1-ade9-3cdf513573e8` | 315-318 [crates/gcore/src/provisioning/docker.rs:315-318] | Indexed class `PgSearchManifest` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:315-318] |
| `pgsearch_manifest` | function | `fn pgsearch_manifest() -> anyhow::Result<PgSearchManifest> {` | `pgsearch_manifest [function]` | `17e612db-e581-53f1-9eac-d24f61c63ba1` | 320-331 [crates/gcore/src/provisioning/docker.rs:320-331] | Indexed function `pgsearch_manifest` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:320-331] |
| `debian_arch` | function | `fn debian_arch(arch: &str) -> String {` | `debian_arch [function]` | `8ae72d07-80e4-57e0-aedb-ff948457a460` | 333-339 [crates/gcore/src/provisioning/docker.rs:333-339] | Indexed function `debian_arch` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:333-339] |
| `update_env_file` | function | `fn update_env_file(path: &Path, updates: BTreeMap<String, String>) -> anyhow::Result<()> {` | `update_env_file [function]` | `44358839-5fea-545c-8dc1-0d43b24c979d` | 341-362 [crates/gcore/src/provisioning/docker.rs:341-362] | Indexed function `update_env_file` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:341-362] |
| `first_non_empty` | function | `fn first_non_empty<'a>(first: &'a str, second: &'a str) -> &'a str {` | `first_non_empty [function]` | `3c8ce0f4-e3cc-5bb0-be35-d05bb58dcf0a` | 364-370 [crates/gcore/src/provisioning/docker.rs:364-370] | Indexed function `first_non_empty` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:364-370] |
| `wait_for_tcp` | function | `fn wait_for_tcp(host: &str, port: u16, retries: usize, interval: Duration) -> anyhow::Result<()> {` | `wait_for_tcp [function]` | `ab081c43-b0e1-5f80-ae69-899d13885151` | 372-382 [crates/gcore/src/provisioning/docker.rs:372-382] | Indexed function `wait_for_tcp` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:372-382] |
| `wait_for` | function | `fn wait_for(` | `wait_for [function]` | `9271fb32-7e22-563f-8933-994fb05aeea5` | 384-403 [crates/gcore/src/provisioning/docker.rs:384-403] | Indexed function `wait_for` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:384-403] |
| `make_executable` | function | `fn make_executable(path: &Path) -> anyhow::Result<()> {` | `make_executable [function]` | `36beb4a9-afde-5e15-a2a0-80d26c2d66a8` | 405-418 [crates/gcore/src/provisioning/docker.rs:405-418] | Indexed function `make_executable` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:405-418] |
