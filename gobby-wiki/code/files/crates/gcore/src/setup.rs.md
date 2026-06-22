---
title: crates/gcore/src/setup.rs
type: code_file
provenance:
- file: crates/gcore/src/setup.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/setup.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/setup.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gcore/src/setup.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `StoreKind` | type | Indexed type `StoreKind` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:11-18] |
| `ValidationContext` | class | 'ValidationContext' is a lifetime-parameterized struct that holds optional references to PostgreSQL database connections and FalkorDB and Qdrant service configurations for validation operations. [crates/gcore/src/setup.rs:26-34] |
| `ValidationReport` | class | ValidationReport is a struct that holds two vectors: one containing names of objects that passed validation, and another containing tuples of failed object names paired with their associated SetupIssue details. [crates/gcore/src/setup.rs:38-43] |
| `ValidationReport::is_healthy` | method | The 'is_healthy' method returns a boolean indicating whether the instance's 'missing' field is empty. [crates/gcore/src/setup.rs:47-49] |
| `RequiredValidator` | type | Indexed type `RequiredValidator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:53-54] |
| `RequiredObject` | class | RequiredObject encapsulates a named object owned by a specified store kind with an associated boxed consumer-supplied validator function for validation logic. [crates/gcore/src/setup.rs:57-64] |
| `AttachedValidator` | type | Indexed type `AttachedValidator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:69-84] |
| `AttachedValidator.validate` | method | This method invokes validator functions on each required object against the provided validation context and returns a ValidationReport that partitions results into present (successful) and missing (failed with error details) entries. [crates/gcore/src/setup.rs:74-83] |
| `SetupContext` | class | SetupContext<'a> is a lifetime-parameterized configuration context struct that optionally holds mutable and immutable references to a PostgreSQL executor and FalkorDB/Qdrant configurations, respectively, along with a non-interactive mode flag for automated setup operations. [crates/gcore/src/setup.rs:90-100] |
| `SetupPostgresExecutor` | type | Indexed type `SetupPostgresExecutor` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:104-107] |
| `batch_execute` | function | Executes multiple SQL statements in a batch operation against a PostgreSQL database connection, returning a Result that is Ok(()) on success or Err(postgres::Error) on failure. [crates/gcore/src/setup.rs:111-113] |
| `batch_execute` | function | This function executes multiple SQL statements as a batch within a PostgreSQL transaction, returning 'Result<(), postgres::Error>' to indicate success or propagate any database errors. [crates/gcore/src/setup.rs:118-120] |
| `SetupReport` | class | SetupReport is a struct that tracks the outcomes of a setup operation across three categories: successfully created objects, pre-existing skipped objects, and failed creations paired with error messages. [crates/gcore/src/setup.rs:125-132] |
| `SetupError` | type | Indexed type `SetupError` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:136-156] |
| `OwnedCreator` | type | Indexed type `OwnedCreator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:159] |
| `OwnedObject` | class | 'OwnedObject' is a struct that encapsulates a named, store-owned object with a boxed consumer-supplied creation function. [crates/gcore/src/setup.rs:162-169] |
| `StandaloneSetup` | type | Indexed type `StandaloneSetup` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:172-181] |
| `RuntimeValidator` | class | RuntimeValidator is a struct designed to perform validation operations at runtime. [crates/gcore/src/setup.rs:191] |
| `RuntimeValidator::required_objects` | method | Returns a vector of two required PostgreSQL-backed objects—a symbols table with a passing validator and a BM25 index with a validator that always fails, returning a SetupIssue with guidance to run the standalone setup command. [crates/gcore/src/setup.rs:194-217] |

_Verified by 3 in-file unit tests._

