---
title: Schema Provisioning
type: code_concept
provenance:
- file: crates/gcode/src/setup/contracts.rs
- file: crates/gcode/src/setup/ddl.rs
- file: crates/gcode/src/setup/identifiers.rs
- file: crates/gcode/src/setup/postgres.rs
- file: crates/gcode/src/setup/tests.rs
- file: crates/gcode/src/setup/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/setup/contracts.rs](crates/gcode/src/setup/contracts.rs)
- [crates/gcode/src/setup/ddl.rs](crates/gcode/src/setup/ddl.rs)
- [crates/gcode/src/setup/identifiers.rs](crates/gcode/src/setup/identifiers.rs)
- [crates/gcode/src/setup/postgres.rs](crates/gcode/src/setup/postgres.rs)
- [crates/gcode/src/setup/tests.rs](crates/gcode/src/setup/tests.rs)
- [crates/gcode/src/setup/types.rs](crates/gcode/src/setup/types.rs)

</details>

# Schema Provisioning

## Purpose

Schema Provisioning is the standalone setup path that prepares the code-index PostgreSQL schema before the rest of the system relies on it. It solves the problem of getting a database into a known-good, version-compatible state: rather than assuming the schema already exists or is correct, the provisioning step validates the current state, can reset it, and creates the schema as needed. It is built to do this safely — in particular, it treats secrets as redacted so that connection and credential material is not leaked during setup, and it performs compatibility checks so that an out-of-date or mismatched schema is caught instead of silently used. The contracts that govern this behavior live in the setup module at [crates/gcode/src/setup/contracts.rs:5-8].

## Covers / Does not cover

This page covers the standalone schema setup concept implemented under [crates/gcode/src/setup](crates/gcode/src/setup/contracts.rs#L5-L8): validating the code-index PostgreSQL schema, resetting it, creating it, applying redacted-secret safety, and running compatibility checks.

It does not cover the runtime query path that uses the provisioned schema, the indexing logic that populates it, or the broader application configuration outside of setup. Because the supplied input exposes no concrete symbols, CLI flags, environment variables, or source bodies, this page does not enumerate specific commands, function names, configuration keys, or schema definitions — only the responsibilities described by the setup module's contracts. Treat anything not anchored to [crates/gcode/src/setup/contracts.rs:5-8] as out of scope here.

## Architecture

Schema Provisioning is organized as a self-contained setup module rather than being interleaved with the application's normal data-access code. This separation is deliberate: provisioning is a privileged, occasional operation with different safety requirements than steady-state reads and writes, so isolating it limits where schema-altering and secret-handling logic can run. The behavioral surface of this module is expressed through contracts at [crates/gcode/src/setup/contracts.rs:5-8], which define what the provisioning step promises — validation, reset, and creation of the schema — and the safety constraints around it.

The "why" of the arrangement is twofold. First, redacted-secret safety means the module is structured so that credential material is handled in a controlled way and not exposed through logs or output, which is easier to guarantee when secret handling is concentrated in one setup boundary. Second, compatibility checks are positioned as a gate: the module is designed to verify the schema is compatible before the system depends on it, so a mismatch is surfaced at setup time rather than as a runtime failure deep in the application. Keeping validation, reset, and creation together behind these contracts lets the provisioning flow make decisions (proceed, recreate, or fail) in one place.

## Data flow

The following traces the intended provisioning flow as described by the setup module's contracts at [crates/gcode/src/setup/contracts.rs:5-8]. Where a dependency is unavailable, the available evidence does not specify the exact fallback, so those points are noted as decision boundaries rather than invented behavior.

1. Provisioning begins as a standalone setup operation, separate from normal application runtime.
2. Secrets needed to reach PostgreSQL are handled under redacted-secret safety, so credential material is not exposed during the run.
3. The current code-index schema is validated against expectations.
4. A compatibility check determines whether the existing schema is usable; an incompatible schema is meant to be caught here rather than passed through to runtime.
5. If a reset is required, the existing schema is reset.
6. The schema is created so the code-index database reaches a known-good state.
7. If the database connection or required schema state is unavailable at any step, the operation stops at that boundary instead of proceeding with an unverified schema. The supplied input does not detail the specific error or retry behavior, so the precise handling should be confirmed against the contracts in [crates/gcode/src/setup/contracts.rs:5-8].

## Key components

The only component exposed by the supplied input is the setup module and its contracts. There are no indexed symbols or source excerpts to enumerate beyond this, so the table is intentionally minimal.

| Symbol / File | Role |
| --- | --- |
| [crates/gcode/src/setup](crates/gcode/src/setup/contracts.rs#L5-L8) | Standalone setup module responsible for validating, resetting, and creating the code-index PostgreSQL schema |
| [crates/gcode/src/setup/contracts.rs:5-8] | Contracts defining the provisioning responsibilities and safety constraints (redacted secrets, compatibility checks) |

## Where to start

Start by reading the contracts at [crates/gcode/src/setup/contracts.rs:5-8]. They define the responsibilities and guarantees of the provisioning flow — validation, reset, creation, redacted-secret safety, and compatibility checks — and are the most concrete entry point available for understanding how Schema Provisioning is expected to behave before exploring the rest of the [crates/gcode/src/setup](crates/gcode/src/setup/contracts.rs#L5-L8) module.

## Explore

- [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

