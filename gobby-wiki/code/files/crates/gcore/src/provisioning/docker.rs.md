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

`crates/gcore/src/provisioning/docker.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DockerServiceOptions` | class | Indexed class `DockerServiceOptions` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:9-18] |
| `DockerServiceOptions::new` | method | Indexed method `DockerServiceOptions::new` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:21-32] |
| `DockerServiceOptions::database_url` | method | Indexed method `DockerServiceOptions::database_url` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:34-36] |
| `DockerServiceOptions::qdrant_url` | method | Indexed method `DockerServiceOptions::qdrant_url` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:38-40] |
| `ServiceAssetReport` | class | Indexed class `ServiceAssetReport` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:44-49] |
| `DockerProvisioningReport` | class | Indexed class `DockerProvisioningReport` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:52-58] |
| `CommandSpec` | class | Indexed class `CommandSpec` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:61-66] |
| `CommandOutput` | class | Indexed class `CommandOutput` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:69-73] |
| `CommandRunner` | type | Indexed type `CommandRunner` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:75-77] |
| `RealCommandRunner` | class | Indexed class `RealCommandRunner` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:79] |
| `RealCommandRunner::run` | method | Indexed method `RealCommandRunner::run` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:82-97] |
| `DockerHealthChecker` | type | Indexed type `DockerHealthChecker` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:100-104] |
| `TcpDockerHealthChecker` | class | Indexed class `TcpDockerHealthChecker` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:106-109] |
| `TcpDockerHealthChecker::default` | method | Indexed method `TcpDockerHealthChecker::default` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:112-117] |
| `TcpDockerHealthChecker::wait_postgres` | method | Indexed method `TcpDockerHealthChecker::wait_postgres` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:121-124] |
| `TcpDockerHealthChecker::wait_qdrant` | method | Indexed method `TcpDockerHealthChecker::wait_qdrant` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:126-142] |
| `TcpDockerHealthChecker::wait_falkordb` | method | Indexed method `TcpDockerHealthChecker::wait_falkordb` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:144-147] |
| `provision_docker_services` | function | Indexed function `provision_docker_services` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:150-156] |
| `provision_docker_services_with` | function | Indexed function `provision_docker_services_with` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:158-190] |
| `prepare_service_assets` | function | Indexed function `prepare_service_assets` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:192-271] |
| `docker_compose_up_spec` | function | Indexed function `docker_compose_up_spec` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:273-306] |
| `PgSearchVersionFile` | class | Indexed class `PgSearchVersionFile` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:309-313] |
| `PgSearchManifest` | class | Indexed class `PgSearchManifest` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:315-318] |
| `pgsearch_manifest` | function | Indexed function `pgsearch_manifest` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:320-331] |
| `debian_arch` | function | Indexed function `debian_arch` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:333-339] |
| `update_env_file` | function | Indexed function `update_env_file` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:341-362] |
| `first_non_empty` | function | Indexed function `first_non_empty` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:364-370] |
| `wait_for_tcp` | function | Indexed function `wait_for_tcp` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:372-382] |
| `wait_for` | function | Indexed function `wait_for` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:384-403] |
| `make_executable` | function | Indexed function `make_executable` in `crates/gcore/src/provisioning/docker.rs`. [crates/gcore/src/provisioning/docker.rs:405-418] |

