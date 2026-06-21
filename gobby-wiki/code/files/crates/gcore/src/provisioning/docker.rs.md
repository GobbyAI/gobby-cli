---
title: crates/gcore/src/provisioning/docker.rs
type: code_file
provenance:
- file: crates/gcore/src/provisioning/docker.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/provisioning/docker.rs

Module: [[code/modules/crates/gcore/src/provisioning|crates/gcore/src/provisioning]]

## Overview

`crates/gcore/src/provisioning/docker.rs` exposes 30 indexed API symbols.

## How it fits

`crates/gcore/src/provisioning/docker.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DockerServiceOptions` | class | 'DockerServiceOptions' is a Rust struct that encapsulates configuration parameters for multiple containerized services, including port bindings for PostgreSQL, Qdrant (vector database), and FalkorDB (graph database), along with FalkorDB credentials and a home directory path. [crates/gcore/src/provisioning/docker.rs:9-18] |
| `DockerServiceOptions::new` | method | Constructs a new instance with the specified 'gobby_home' PathBuf while initializing PostgreSQL, Qdrant, and FalkorDB service configuration fields (ports, host, and credentials) to their default constant values. [crates/gcore/src/provisioning/docker.rs:21-32] |
| `DockerServiceOptions::database_url` | method | This public instance method constructs and returns a database URL string by delegating to the 'default_database_url()' function with the instance's 'postgres_port' parameter. [crates/gcore/src/provisioning/docker.rs:34-36] |
| `DockerServiceOptions::qdrant_url` | method | This method constructs and returns an HTTP localhost URL string by formatting it with the instance's 'qdrant_http_port' value. [crates/gcore/src/provisioning/docker.rs:38-40] |
| `ServiceAssetReport` | class | 'ServiceAssetReport' is a public struct that encapsulates four 'PathBuf' fields representing filesystem paths to service configuration assets: a services directory, Docker Compose file, environment file, and PostgreSQL asset directory. [crates/gcore/src/provisioning/docker.rs:44-49] |
| `DockerProvisioningReport` | class | 'DockerProvisioningReport' is a struct that aggregates Docker provisioning metadata, including filesystem paths for service and configuration files, along with lists of provisioned service profiles and their associated health checks. [crates/gcore/src/provisioning/docker.rs:52-58] |
| `CommandSpec` | class | # CommandSpec 'CommandSpec' is a configuration struct for executing external processes, containing the program name, command-line arguments, environment variables, and an optional working directory. [crates/gcore/src/provisioning/docker.rs:61-66] |
| `CommandOutput` | class | 'CommandOutput' is a public struct that encapsulates the result of command execution, containing an exit status code ('i32'), standard output ('String'), and standard error output ('String'). [crates/gcore/src/provisioning/docker.rs:69-73] |
| `CommandRunner` | type | Indexed type `CommandRunner` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:75-77] |
| `RealCommandRunner` | class | RealCommandRunner is a public unit struct serving as a zero-sized marker type for concrete command execution implementation. [crates/gcore/src/provisioning/docker.rs:79] |
| `RealCommandRunner::run` | method | Executes a system command specified by a CommandSpec with configured arguments, environment variables, and working directory, capturing and returning the exit status code and UTF-8-decoded stdout/stderr output. [crates/gcore/src/provisioning/docker.rs:82-97] |
| `DockerHealthChecker` | type | Indexed type `DockerHealthChecker` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:100-104] |
| `TcpDockerHealthChecker` | class | TcpDockerHealthChecker is a configuration struct that specifies TCP health check parameters with a retry count and probe interval duration. [crates/gcore/src/provisioning/docker.rs:106-109] |
| `TcpDockerHealthChecker::default` | method | This method implements the 'Default' trait, returning a new instance of the struct with 'retries' set to 30 and 'interval' set to a 2-second 'Duration'. [crates/gcore/src/provisioning/docker.rs:112-117] |
| `TcpDockerHealthChecker::wait_postgres` | method | Polls TCP connectivity to the specified PostgreSQL host and port using stored retry configuration, mapping connection failures to an anyhow error. [crates/gcore/src/provisioning/docker.rs:121-124] |
| `TcpDockerHealthChecker::wait_qdrant` | method | Polls a Qdrant service's HTTP '/healthz' endpoint at the specified host and port with configurable retries and intervals until it returns a 200 status code. [crates/gcore/src/provisioning/docker.rs:126-142] |
| `TcpDockerHealthChecker::wait_falkordb` | method | Polls for TCP connectivity to FalkorDB at the specified host and port using instance-configured retries and interval, returning an 'anyhow::Result<()>' that wraps connection errors as a descriptive anyhow error. [crates/gcore/src/provisioning/docker.rs:144-147] |
| `provision_docker_services` | function | Provisions Docker services according to the provided options by instantiating a real command runner and TCP health checker, delegating to an internal provisioning function, and returning a 'DockerProvisioningReport' or error. [crates/gcore/src/provisioning/docker.rs:150-156] |
| `provision_docker_services_with` | function | Provisions standalone Docker services by executing a docker-compose specification and performing sequential health checks on PostgreSQL, Qdrant, and FalkorDB instances before returning a provisioning report. [crates/gcore/src/provisioning/docker.rs:158-190] |
| `prepare_service_assets` | function | # Summary 'prepare_service_assets' provisions Docker service infrastructure by creating directory structures, writing configuration files (Docker Compose, Dockerfiles, SQL initialization scripts, and shell utilities), and populating environment variables for PostgreSQL and Qdrant services. [crates/gcore/src/provisioning/docker.rs:192-271] |
| `docker_compose_up_spec` | function | Constructs a CommandSpec that specifies a detached docker-compose up command with environment variables derived from DockerServiceOptions and execution in a specified services directory. [crates/gcore/src/provisioning/docker.rs:273-306] |
| `PgSearchVersionFile` | class | PgSearchVersionFile is a struct that stores a pg_search version string, a base SHA256 checksum, and an optional BTreeMap of architecture-specific SHA256 checksums. [crates/gcore/src/provisioning/docker.rs:309-313] |
| `PgSearchManifest` | class | PgSearchManifest is a struct that encapsulates pg_search version metadata and a SHA256 hash for integrity verification and version tracking. [crates/gcore/src/provisioning/docker.rs:315-318] |
| `pgsearch_manifest` | function | This function deserializes a JSON manifest file to construct and return a 'PgSearchManifest' containing the version and the SHA256 hash appropriate for the current system architecture, with a fallback to a default hash if an architecture-specific entry is not found. [crates/gcore/src/provisioning/docker.rs:320-331] |

_6 more symbol(s) not shown — run `gcode outline crates/gcore/src/provisioning/docker.rs` for the full list._

