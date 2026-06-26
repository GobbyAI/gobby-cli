---
title: crates/gcore/src
type: code_module
provenance:
- file: crates/gcore/src/ai/daemon/tests.rs
- file: crates/gcore/src/ai/embeddings.rs
- file: crates/gcore/src/ai/mod.rs
- file: crates/gcore/src/ai/probe.rs
- file: crates/gcore/src/ai/transcription.rs
- file: crates/gcore/src/ai/vision.rs
- file: crates/gcore/src/ai_context.rs
- file: crates/gcore/src/ai_types.rs
- file: crates/gcore/src/bootstrap.rs
- file: crates/gcore/src/cli_contract.rs
- file: crates/gcore/src/config/resolve.rs
- file: crates/gcore/src/config/tests.rs
- file: crates/gcore/src/config/types.rs
- file: crates/gcore/src/daemon_url.rs
- file: crates/gcore/src/degradation.rs
- file: crates/gcore/src/falkor.rs
- file: crates/gcore/src/graph_analytics.rs
- file: crates/gcore/src/graph_analytics/leiden.rs
- file: crates/gcore/src/indexing.rs
- file: crates/gcore/src/postgres.rs
- file: crates/gcore/src/provisioning/bootstrap.rs
- file: crates/gcore/src/provisioning/docker.rs
- file: crates/gcore/src/provisioning/hub.rs
- file: crates/gcore/src/provisioning/mod.rs
- file: crates/gcore/src/provisioning/tests.rs
- file: crates/gcore/src/qdrant.rs
- file: crates/gcore/src/qdrant/tests.rs
- file: crates/gcore/src/search.rs
- file: crates/gcore/src/secrets.rs
- file: crates/gcore/src/setup.rs
provenance_truncated: 13
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src

Parent: [[code/modules/crates/gcore|crates/gcore]]

## Overview

`crates/gcore/src` contains 26 direct files and 5 child modules.
[crates/gcore/src/ai/daemon.rs:1-16]
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/request.rs:11-19]
[crates/gcore/src/ai/daemon/response.rs:7-9]
[crates/gcore/src/ai/daemon/tests.rs:15-24]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/src/ai\|crates/gcore/src/ai]] | `crates/gcore/src/ai` contains 7 direct files and 1 child module. [crates/gcore/src/ai/daemon.rs:1-16] [crates/gcore/src/ai/daemon/operations.rs:20-72] [crates/gcore/src/ai/daemon/request.rs:11-19] [crates/gcore/src/ai/daemon/response.rs:7-9] [crates/gcore/src/ai/daemon/tests.rs:15-24] |
| [[code/modules/crates/gcore/src/config\|crates/gcore/src/config]] | `crates/gcore/src/config` contains 4 direct files and 0 child modules. [crates/gcore/src/config/mod.rs:1-31] [crates/gcore/src/config/resolve.rs:11-21] [crates/gcore/src/config/tests.rs:5-7] [crates/gcore/src/config/types.rs:7-11] [crates/gcore/src/config/resolve.rs:24-75] |
| [[code/modules/crates/gcore/src/graph_analytics\|crates/gcore/src/graph_analytics]] | `crates/gcore/src/graph_analytics` contains 1 direct file and 0 child modules. [crates/gcore/src/graph_analytics/leiden.rs:32-40] [crates/gcore/src/graph_analytics/leiden.rs:45-72] [crates/gcore/src/graph_analytics/leiden.rs:76-79] [crates/gcore/src/graph_analytics/leiden.rs:82-87] [crates/gcore/src/graph_analytics/leiden.rs:94-184] |
| [[code/modules/crates/gcore/src/provisioning\|crates/gcore/src/provisioning]] | `crates/gcore/src/provisioning` contains 5 direct files and 0 child modules. [crates/gcore/src/provisioning/bootstrap.rs:8-15] [crates/gcore/src/provisioning/docker.rs:9-18] [crates/gcore/src/provisioning/hub.rs:4-9] [crates/gcore/src/provisioning/mod.rs:55-57] [crates/gcore/src/provisioning/tests.rs:5-7] |
| [[code/modules/crates/gcore/src/qdrant\|crates/gcore/src/qdrant]] | `crates/gcore/src/qdrant` contains 2 direct files and 0 child modules. [crates/gcore/src/qdrant/naming.rs:3-10] [crates/gcore/src/qdrant/tests.rs:12-30] [crates/gcore/src/qdrant/naming.rs:13-22] [crates/gcore/src/qdrant/naming.rs:25-43] [crates/gcore/src/qdrant/naming.rs:45-70] |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/ai/embeddings.rs\|crates/gcore/src/ai/embeddings.rs]] | `crates/gcore/src/ai/embeddings.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/mod.rs\|crates/gcore/src/ai/mod.rs]] | `crates/gcore/src/ai/mod.rs` exposes 37 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/probe.rs\|crates/gcore/src/ai/probe.rs]] | `crates/gcore/src/ai/probe.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/text.rs\|crates/gcore/src/ai/text.rs]] | `crates/gcore/src/ai/text.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/transcription.rs\|crates/gcore/src/ai/transcription.rs]] | `crates/gcore/src/ai/transcription.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/vision.rs\|crates/gcore/src/ai/vision.rs]] | `crates/gcore/src/ai/vision.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcore/src/ai_context.rs\|crates/gcore/src/ai_context.rs]] | `crates/gcore/src/ai_context.rs` exposes 56 indexed API symbols. |
| [[code/files/crates/gcore/src/ai_types.rs\|crates/gcore/src/ai_types.rs]] | `crates/gcore/src/ai_types.rs` exposes 34 indexed API symbols. |
| [[code/files/crates/gcore/src/bootstrap.rs\|crates/gcore/src/bootstrap.rs]] | `crates/gcore/src/bootstrap.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcore/src/cli_contract.rs\|crates/gcore/src/cli_contract.rs]] | `crates/gcore/src/cli_contract.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gcore/src/codewiki_contract.rs\|crates/gcore/src/codewiki_contract.rs]] | `crates/gcore/src/codewiki_contract.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcore/src/daemon_url.rs\|crates/gcore/src/daemon_url.rs]] | `crates/gcore/src/daemon_url.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcore/src/degradation.rs\|crates/gcore/src/degradation.rs]] | `crates/gcore/src/degradation.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcore/src/falkor.rs\|crates/gcore/src/falkor.rs]] | `crates/gcore/src/falkor.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gcore/src/graph_analytics.rs\|crates/gcore/src/graph_analytics.rs]] | `crates/gcore/src/graph_analytics.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gcore/src/graph_analytics/leiden.rs\|crates/gcore/src/graph_analytics/leiden.rs]] | `crates/gcore/src/graph_analytics/leiden.rs` exposes 36 indexed API symbols. |
| [[code/files/crates/gcore/src/indexing.rs\|crates/gcore/src/indexing.rs]] | `crates/gcore/src/indexing.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcore/src/lib.rs\|crates/gcore/src/lib.rs]] | `crates/gcore/src/lib.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcore/src/libpq.rs\|crates/gcore/src/libpq.rs]] | `crates/gcore/src/libpq.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcore/src/postgres.rs\|crates/gcore/src/postgres.rs]] | `crates/gcore/src/postgres.rs` exposes 32 indexed API symbols. |
| [[code/files/crates/gcore/src/project.rs\|crates/gcore/src/project.rs]] | `crates/gcore/src/project.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcore/src/provisioning/hub.rs\|crates/gcore/src/provisioning/hub.rs]] | `crates/gcore/src/provisioning/hub.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gcore/src/qdrant.rs\|crates/gcore/src/qdrant.rs]] | `crates/gcore/src/qdrant.rs` exposes 30 indexed API symbols. |
| [[code/files/crates/gcore/src/search.rs\|crates/gcore/src/search.rs]] | `crates/gcore/src/search.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcore/src/secrets.rs\|crates/gcore/src/secrets.rs]] | `crates/gcore/src/secrets.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gcore/src/setup.rs\|crates/gcore/src/setup.rs]] | `crates/gcore/src/setup.rs` exposes 22 indexed API symbols. |

