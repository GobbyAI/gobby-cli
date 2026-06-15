---
title: crates/gcore/src/provisioning/docker.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/docker.rs
  ranges:
  - 9-18
  - 20-41
  - 44-49
  - 52-58
  - 61-66
  - 69-73
  - 75-77
  - '79'
  - 81-98
  - 100-104
  - 106-109
  - 111-118
  - 120-148
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

# crates/gcore/src/provisioning/docker.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Purpose

This file provisions a Docker-backed service stack for Gobby by defining the service configuration, command execution abstraction, health-check logic, and the orchestration flow that writes required assets, runs `docker-compose`, and waits for PostgreSQL, Qdrant, and FalkorDB to become ready. `DockerServiceOptions` carries ports, hosts, and credentials plus helpers for service URLs; `ServiceAssetReport` and `DockerProvisioningReport` describe the generated files and startup results; `CommandSpec`/`CommandOutput` with `CommandRunner` and `RealCommandRunner` wrap external process execution; `TcpDockerHealthChecker` polls TCP or Qdrant HTTP health endpoints; and helper functions build manifests, normalize architecture names, update env files, retry readiness checks, and make scripts executable.
[crates/gcore/src/provisioning/docker.rs:9-18]
[crates/gcore/src/provisioning/docker.rs:20-41]
[crates/gcore/src/provisioning/docker.rs:21-32]
[crates/gcore/src/provisioning/docker.rs:34-36]
[crates/gcore/src/provisioning/docker.rs:38-40]

## API Symbols

- `DockerServiceOptions` (class) component `DockerServiceOptions [class]` (`058087a3-9962-5e44-a6be-506dda77aae3`) lines 9-18 [crates/gcore/src/provisioning/docker.rs:9-18]
  - Signature: `pub struct DockerServiceOptions {`
  - Purpose: `DockerServiceOptions` is a configuration struct that encapsulates network endpoints (ports and hosts) and credentials for three Docker-based services: PostgreSQL, Qdrant (with HTTP and gRPC ports), and FalkorDB. [crates/gcore/src/provisioning/docker.rs:9-18]
- `DockerServiceOptions` (class) component `DockerServiceOptions [class]` (`a573e0bd-f68f-55ab-86a9-e1d89bbd844d`) lines 20-41 [crates/gcore/src/provisioning/docker.rs:20-41]
  - Signature: `impl DockerServiceOptions {`
  - Purpose: `DockerServiceOptions` is a configuration struct that initializes containerized database services (PostgreSQL, Qdrant vector search, and FalkorDB graph database) with default ports and provides methods to construct their connection URLs. [crates/gcore/src/provisioning/docker.rs:20-41]
- `DockerServiceOptions.new` (method) component `DockerServiceOptions.new [method]` (`d300ea36-004e-5579-9b5d-79d454d396ed`) lines 21-32 [crates/gcore/src/provisioning/docker.rs:21-32]
  - Signature: `pub fn new(gobby_home: PathBuf) -> Self {`
  - Purpose: Constructs a new instance with the provided `gobby_home` PathBuf and initializes all service configuration fields (PostgreSQL, Qdrant HTTP/gRPC, and FalkorDB ports and credentials) to their default constant values. [crates/gcore/src/provisioning/docker.rs:21-32]
- `DockerServiceOptions.database_url` (method) component `DockerServiceOptions.database_url [method]` (`f939c597-f88a-56e6-8c06-2bfb4e5ff7c0`) lines 34-36 [crates/gcore/src/provisioning/docker.rs:34-36]
  - Signature: `pub fn database_url(&self) -> String {`
  - Purpose: Returns a database URL string by delegating to `default_database_url()` with the instance's PostgreSQL port. [crates/gcore/src/provisioning/docker.rs:34-36]
- `DockerServiceOptions.qdrant_url` (method) component `DockerServiceOptions.qdrant_url [method]` (`870f641e-2314-58c6-aef3-55e022cb19bf`) lines 38-40 [crates/gcore/src/provisioning/docker.rs:38-40]
  - Signature: `pub fn qdrant_url(&self) -> String {`
  - Purpose: This method constructs and returns an HTTP URL string for a Qdrant server instance running on localhost, using the port stored in `self.qdrant_http_port`. [crates/gcore/src/provisioning/docker.rs:38-40]
- `ServiceAssetReport` (class) component `ServiceAssetReport [class]` (`b391095b-1212-57a2-8309-707c0a07df16`) lines 44-49 [crates/gcore/src/provisioning/docker.rs:44-49]
  - Signature: `pub struct ServiceAssetReport {`
  - Purpose: `ServiceAssetReport` is a struct that aggregates file system paths to a services directory, Docker Compose configuration file, environment variables file, and PostgreSQL asset directory. [crates/gcore/src/provisioning/docker.rs:44-49]
- `DockerProvisioningReport` (class) component `DockerProvisioningReport [class]` (`a58a620b-bd7b-524a-aa2c-4b080a0d9296`) lines 52-58 [crates/gcore/src/provisioning/docker.rs:52-58]
  - Signature: `pub struct DockerProvisioningReport {`
  - Purpose: `DockerProvisioningReport` aggregates the configuration file paths (services directory, Docker Compose file, and environment file) alongside the provisioning outcomes—specifically the activated profiles and their associated health checks. [crates/gcore/src/provisioning/docker.rs:52-58]
- `CommandSpec` (class) component `CommandSpec [class]` (`bb1a4995-86d9-5bc9-b0b1-5145bb3d7cfd`) lines 61-66 [crates/gcore/src/provisioning/docker.rs:61-66]
  - Signature: `pub struct CommandSpec {`
  - Purpose: CommandSpec is a Rust struct that encapsulates all parameters required to execute a process: the program name, command-line arguments, environment variables as a BTreeMap, and an optional working directory path. [crates/gcore/src/provisioning/docker.rs:61-66]
- `CommandOutput` (class) component `CommandOutput [class]` (`a4ec36de-2f88-594f-81e3-049788542be7`) lines 69-73 [crates/gcore/src/provisioning/docker.rs:69-73]
  - Signature: `pub struct CommandOutput {`
  - Purpose: CommandOutput is a struct that encapsulates the result of a command execution, containing an i32 exit status code and the captured stdout and stderr output as strings. [crates/gcore/src/provisioning/docker.rs:69-73]
- `CommandRunner` (type) component `CommandRunner [type]` (`6bf7d150-1d16-5452-bc2c-2c6f74305480`) lines 75-77 [crates/gcore/src/provisioning/docker.rs:75-77]
  - Signature: `pub trait CommandRunner {`
  - Purpose: Indexed type `CommandRunner` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:75-77]
- `RealCommandRunner` (class) component `RealCommandRunner [class]` (`c078847c-c3b9-566a-9e45-9a7b785a3782`) lines 79-79 [crates/gcore/src/provisioning/docker.rs:79]
  - Signature: `pub struct RealCommandRunner;`
  - Purpose: `RealCommandRunner` is a public unit struct (zero-sized type) that serves as a concrete implementation for executing actual system commands. [crates/gcore/src/provisioning/docker.rs:79]
- `RealCommandRunner` (class) component `RealCommandRunner [class]` (`759cd91b-a62d-5242-b0c1-9ce9249443cd`) lines 81-98 [crates/gcore/src/provisioning/docker.rs:81-98]
  - Signature: `impl CommandRunner for RealCommandRunner {`
  - Purpose: RealCommandRunner is a concrete implementation of the CommandRunner trait that spawns and executes system processes with configurable arguments, working directory, and environment variables, capturing their exit code and output streams as a CommandOutput struct. [crates/gcore/src/provisioning/docker.rs:81-98]
- `RealCommandRunner.run` (method) component `RealCommandRunner.run [method]` (`7f5b61ef-3bca-581b-8de1-bebc361641c0`) lines 82-97 [crates/gcore/src/provisioning/docker.rs:82-97]
  - Signature: `fn run(&mut self, spec: &CommandSpec) -> std::io::Result<CommandOutput> {`
  - Purpose: This method executes an external process with the program, arguments, working directory, and environment variables specified in a `CommandSpec`, returning its exit code and captured UTF-8-decoded stdout/stderr output. [crates/gcore/src/provisioning/docker.rs:82-97]
- `DockerHealthChecker` (type) component `DockerHealthChecker [type]` (`356a8faf-cf84-57fd-b125-1b8843f52650`) lines 100-104 [crates/gcore/src/provisioning/docker.rs:100-104]
  - Signature: `pub trait DockerHealthChecker {`
  - Purpose: Indexed type `DockerHealthChecker` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:100-104]
- `TcpDockerHealthChecker` (class) component `TcpDockerHealthChecker [class]` (`56773d94-cdfa-5e0f-9072-7f5b640367fb`) lines 106-109 [crates/gcore/src/provisioning/docker.rs:106-109]
  - Signature: `pub struct TcpDockerHealthChecker {`
  - Purpose: `TcpDockerHealthChecker` is a configuration struct that specifies the retry count and polling interval for TCP-based Docker container health checks. [crates/gcore/src/provisioning/docker.rs:106-109]
- `TcpDockerHealthChecker` (class) component `TcpDockerHealthChecker [class]` (`43b398d5-932b-5a88-a36b-1477de95a809`) lines 111-118 [crates/gcore/src/provisioning/docker.rs:111-118]
  - Signature: `impl Default for TcpDockerHealthChecker {`
  - Purpose: `TcpDockerHealthChecker`'s Default trait implementation initializes a TCP-based Docker health checker with 30 retry attempts at 2-second intervals. [crates/gcore/src/provisioning/docker.rs:111-118]
- `TcpDockerHealthChecker.default` (method) component `TcpDockerHealthChecker.default [method]` (`b4cf94b7-7f25-5111-94f2-60496b945a63`) lines 112-117 [crates/gcore/src/provisioning/docker.rs:112-117]
  - Signature: `fn default() -> Self {`
  - Purpose: This method implements the `Default` trait, returning an instance of `Self` configured with 30 retries and a 2-second interval duration. [crates/gcore/src/provisioning/docker.rs:112-117]
- `TcpDockerHealthChecker` (class) component `TcpDockerHealthChecker [class]` (`b90275cc-1e4a-5733-ac7b-19a8b8a8ea52`) lines 120-148 [crates/gcore/src/provisioning/docker.rs:120-148]
  - Signature: `impl DockerHealthChecker for TcpDockerHealthChecker {`
  - Purpose: `TcpDockerHealthChecker` implements `DockerHealthChecker` to verify PostgreSQL and FalkorDB service readiness via TCP connectivity polling and Qdrant readiness via HTTP GET requests to the `/healthz` endpoint, with configurable retry logic. [crates/gcore/src/provisioning/docker.rs:120-148]
- `TcpDockerHealthChecker.wait_postgres` (method) component `TcpDockerHealthChecker.wait_postgres [method]` (`0e53fcb4-e8a7-591d-b886-954df10640cd`) lines 121-124 [crates/gcore/src/provisioning/docker.rs:121-124]
  - Signature: `fn wait_postgres(&mut self, host: &str, port: u16) -> anyhow::Result<()> {`
  - Purpose: Waits for TCP connectivity to a PostgreSQL server at the specified host and port, returning an error if reachability is not achieved after configured retries and intervals. [crates/gcore/src/provisioning/docker.rs:121-124]
- `TcpDockerHealthChecker.wait_qdrant` (method) component `TcpDockerHealthChecker.wait_qdrant [method]` (`47b37107-0c4b-5b85-bfb4-ae85292c8050`) lines 126-142 [crates/gcore/src/provisioning/docker.rs:126-142]
  - Signature: `fn wait_qdrant(&mut self, host: &str, port: u16) -> anyhow::Result<()> {`
  - Purpose: Polls a Qdrant instance's `/healthz` endpoint via TCP with configured retry limits until the server responds with an HTTP 200 status code. [crates/gcore/src/provisioning/docker.rs:126-142]
- `TcpDockerHealthChecker.wait_falkordb` (method) component `TcpDockerHealthChecker.wait_falkordb [method]` (`90e58149-3764-5732-922f-a70c1a0eb734`) lines 144-147 [crates/gcore/src/provisioning/docker.rs:144-147]
  - Signature: `fn wait_falkordb(&mut self, host: &str, port: u16) -> anyhow::Result<()> {`
  - Purpose: Waits for TCP connectivity to a FalkorDB instance at the specified host and port using configured retry parameters, returning an error if the connection is not established. [crates/gcore/src/provisioning/docker.rs:144-147]
- `provision_docker_services` (function) component `provision_docker_services [function]` (`defc89f1-d9e0-53e3-a5dd-f183f30807e9`) lines 150-156 [crates/gcore/src/provisioning/docker.rs:150-156]
  - Signature: `pub fn provision_docker_services(`
  - Purpose: Provisions Docker services by instantiating concrete implementations of `RealCommandRunner` and `TcpDockerHealthChecker` and delegating to `provision_docker_services_with`. [crates/gcore/src/provisioning/docker.rs:150-156]
- `provision_docker_services_with` (function) component `provision_docker_services_with [function]` (`58066265-375c-54d2-ab57-80956ffdefa4`) lines 158-190 [crates/gcore/src/provisioning/docker.rs:158-190]
  - Signature: `pub fn provision_docker_services_with(`
  - Purpose: Provisions a Docker service stack by executing docker-compose with specified options, blocking until PostgreSQL, Qdrant, and FalkorDB health checks pass, then returns a DockerProvisioningReport. [crates/gcore/src/provisioning/docker.rs:158-190]
- `prepare_service_assets` (function) component `prepare_service_assets [function]` (`3adcedf6-7f24-51bb-81a4-636a6584ac36`) lines 192-271 [crates/gcore/src/provisioning/docker.rs:192-271]
  - Signature: `pub fn prepare_service_assets(`
  - Purpose: Initializes Docker service assets by creating the directory structure, writing PostgreSQL configuration and initialization files (including pgSearch and pgAudit scripts), and updating the environment configuration file with service parameters. [crates/gcore/src/provisioning/docker.rs:192-271]
- `docker_compose_up_spec` (function) component `docker_compose_up_spec [function]` (`aa6292cb-da15-5f26-ab6b-b728ee107fdd`) lines 273-306 [crates/gcore/src/provisioning/docker.rs:273-306]
  - Signature: `pub fn docker_compose_up_spec(`
  - Purpose: Constructs a CommandSpec that builds a `docker-compose up` command in detached mode with all profiles enabled, orphaned container removal, and FalkorDB/PostgreSQL/Qdrant credentials configured via environment variables. [crates/gcore/src/provisioning/docker.rs:273-306]
- `PgSearchVersionFile` (class) component `PgSearchVersionFile [class]` (`0202b323-b704-58d2-b097-604a0a40daed`) lines 309-313 [crates/gcore/src/provisioning/docker.rs:309-313]
  - Signature: `struct PgSearchVersionFile {`
  - Purpose: `PgSearchVersionFile` is a struct that encapsulates pg_search package version metadata, consisting of a version identifier, a unified SHA256 checksum, and optional per-architecture SHA256 checksums for integrity verification. [crates/gcore/src/provisioning/docker.rs:309-313]
- `PgSearchManifest` (class) component `PgSearchManifest [class]` (`f8ee2cd2-bea4-5ce1-ade9-3cdf513573e8`) lines 315-318 [crates/gcore/src/provisioning/docker.rs:315-318]
  - Signature: `struct PgSearchManifest {`
  - Purpose: PgSearchManifest is a struct that encapsulates pg_search version metadata and a SHA256 digest for integrity verification. [crates/gcore/src/provisioning/docker.rs:315-318]
- `pgsearch_manifest` (function) component `pgsearch_manifest [function]` (`17e612db-e581-53f1-9eac-d24f61c63ba1`) lines 320-331 [crates/gcore/src/provisioning/docker.rs:320-331]
  - Signature: `fn pgsearch_manifest() -> anyhow::Result<PgSearchManifest> {`
  - Purpose: Constructs a `PgSearchManifest` by parsing embedded version metadata and selecting the architecture-specific SHA256 hash with fallback to a default value. [crates/gcore/src/provisioning/docker.rs:320-331]
- `debian_arch` (function) component `debian_arch [function]` (`8ae72d07-80e4-57e0-aedb-ff948457a460`) lines 333-339 [crates/gcore/src/provisioning/docker.rs:333-339]
  - Signature: `fn debian_arch(arch: &str) -> String {`
  - Purpose: Normalizes architecture identifiers to Debian naming conventions by mapping x86_64 and aarch64 to their Debian equivalents (amd64 and arm64 respectively), while returning unrecognized architectures unchanged. [crates/gcore/src/provisioning/docker.rs:333-339]
- `update_env_file` (function) component `update_env_file [function]` (`44358839-5fea-545c-8dc1-0d43b24c979d`) lines 341-362 [crates/gcore/src/provisioning/docker.rs:341-362]
  - Signature: `fn update_env_file(path: &Path, updates: BTreeMap<String, String>) -> anyhow::Result<()> {`
  - Purpose: Merges a set of key-value pairs into an environment file by removing any existing entries with matching keys and appending the updates, while creating parent directories as needed. [crates/gcore/src/provisioning/docker.rs:341-362]
- `first_non_empty` (function) component `first_non_empty [function]` (`3c8ce0f4-e3cc-5bb0-be35-d05bb58dcf0a`) lines 364-370 [crates/gcore/src/provisioning/docker.rs:364-370]
  - Signature: `fn first_non_empty<'a>(first: &'a str, second: &'a str) -> &'a str {`
  - Purpose: Returns the trimmed first argument if non-empty, otherwise returns the trimmed second argument. [crates/gcore/src/provisioning/docker.rs:364-370]
- `wait_for_tcp` (function) component `wait_for_tcp [function]` (`ab081c43-b0e1-5f80-ae69-899d13885151`) lines 372-382 [crates/gcore/src/provisioning/docker.rs:372-382]
  - Signature: `fn wait_for_tcp(host: &str, port: u16, retries: usize, interval: Duration) -> anyhow::Result<()> {`
  - Purpose: Retries TCP connection establishment to a specified host and port at fixed intervals until successful or the retry limit is exhausted. [crates/gcore/src/provisioning/docker.rs:372-382]
- `wait_for` (function) component `wait_for [function]` (`9271fb32-7e22-563f-8933-994fb05aeea5`) lines 384-403 [crates/gcore/src/provisioning/docker.rs:384-403]
  - Signature: `fn wait_for(`
  - Purpose: Retries a check closure at fixed intervals up to a specified number of attempts, returning on first success or propagating the accumulated error on complete failure. [crates/gcore/src/provisioning/docker.rs:384-403]
- `make_executable` (function) component `make_executable [function]` (`36beb4a9-afde-5e15-a2a0-80d26c2d66a8`) lines 405-418 [crates/gcore/src/provisioning/docker.rs:405-418]
  - Signature: `fn make_executable(path: &Path) -> anyhow::Result<()> {`
  - Purpose: Sets Unix file permissions to 0o755 (rwxr-xr-x) on Unix systems to make a file executable, while being a platform-agnostic no-op on non-Unix platforms. [crates/gcore/src/provisioning/docker.rs:405-418]

