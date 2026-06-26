---
title: crates/gwiki/src/main.rs
type: code_file
provenance:
- file: crates/gwiki/src/main.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/main.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/main.rs` exposes 39 indexed API symbols.

## How it fits

`crates/gwiki/src/main.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Cli` | class | 'Cli' is the top-level command-line argument struct that flattens shared scope options, exposes global '--format' and '--quiet' flags, and dispatches to a required subcommand via 'command'. [crates/gwiki/src/main.rs:48-62] |
| `CliCommand` | type | Indexed type `CliCommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:65-153] |
| `ScopeArgs` | class | 'ScopeArgs' is a CLI argument struct that defines two mutually exclusive global scope selectors for Gobby wiki operations: '--project' optionally takes a project root path and defaults to the current directory when passed without a value, while '--topic' selects a named topic scope. [crates/gwiki/src/main.rs:156-171] |
| `NormalizeArgs` | class | 'NormalizeArgs' is a CLI argument struct containing a '--check' boolean flag that enables reporting which authored documents need normalization without modifying them. [crates/gwiki/src/main.rs:174-178] |
| `SetupArgs` | class | 'SetupArgs' is a CLI argument struct that configures Gobby/gwiki setup behavior, including standalone and service-provisioning flags, PostgreSQL and vector-store connection settings, and optional embedding provider/API/model parameters. [crates/gwiki/src/main.rs:181-223] |
| `SearchArgs` | class | SearchArgs is a Rust struct for parsing command-line search arguments, comprising a required query string, configurable result limit (default 10), boolean flag to disable semantic vector search, and optional token budget for result trimming. [crates/gwiki/src/main.rs:226-240] |
| `AskArgs` | class | 'AskArgs' is a command-line argument struct for wiki-based question retrieval with optional LLM answer synthesis, configurable AI routing strategies, mandatory synthesis enforcement, and token-budget-constrained result trimming. [crates/gwiki/src/main.rs:243-262] |
| `SyncSessionsArgs` | class | SyncSessionsArgs is a struct defining command-line arguments that specify an optional directory containing archived *.jsonl.gz session transcripts and an optional maximum number of archives to process. [crates/gwiki/src/main.rs:265-273] |
| `BenchmarkArgs` | class | BenchmarkArgs is a command-line argument struct containing a single field 'retrieval_candidates' (positive usize) specified via the '--retrieval-candidates' flag to configure the number of seeded retrieval precision probes to evaluate. [crates/gwiki/src/main.rs:276-284] |
| `parse_positive_usize` | function | Parses a string as a 'usize' and validates that the result is positive (greater than zero), returning 'Result<usize, String>' with a descriptive error message on parse failure or zero value. [crates/gwiki/src/main.rs:286-297] |
| `RemoveSourceArgs` | class | RemoveSourceArgs is a command-line argument struct for removing a vault source by ID, with optional flags for dry-run preview, destructive confirmation, and raw asset preservation. [crates/gwiki/src/main.rs:300-315] |
| `RefreshArgs` | class | RefreshArgs is a command-line argument struct that specifies one or more source IDs to refresh and optionally enables dry-run mode to preview the refresh operation without executing fetch, write, delete, or indexing operations. [crates/gwiki/src/main.rs:318-326] |
| `ReadArgs` | class | 'ReadArgs' is a command-line argument struct that accepts optional fields for a vault-relative wiki path and a first-heading title to resolve within the selected scope. [crates/gwiki/src/main.rs:334-342] |
| `BacklinksArgs` | class | BacklinksArgs is a command-line argument struct that defines a single required String parameter named 'page' for parsing CLI input via the clap framework. [crates/gwiki/src/main.rs:345-348] |
| `LinkSuggestArgs` | class | 'LinkSuggestArgs' is a command-line argument struct defining a single 'limit' parameter of type 'usize' with a default value of 10, parsed via the 'clap' crate. [crates/gwiki/src/main.rs:351-354] |
| `CompileArgs` | class | CompileArgs is a struct encapsulating command-line arguments for topic-based compilation with configurable sources, outline headings, compilation kind, output path, and optional AI routing for explainer synthesis. [crates/gwiki/src/main.rs:357-382] |
| `ExportArgs` | class | # Summary **ExportArgs** is a struct that encapsulates a single 'ExportSubcommand' field annotated with '#[command(subcommand)]' to designate it as a CLI subcommand parser. [crates/gwiki/src/main.rs:385-388] |
| `ReviewReportArgs` | class | ReviewReportArgs is a CLI argument struct that accepts multiple files and symbol identifiers, an optional diff path, and specifies an output file (defaulting to "review-report.md") for generating a code review report. [crates/gwiki/src/main.rs:391-404] |
| `ExportSubcommand` | type | Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:407-421] |
| `CompileKind` | type | Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:424-428] |
| `StderrLogger` | class | StderrLogger is a struct that provides logging functionality by writing output to the standard error stream (stderr). [crates/gwiki/src/main.rs:435] |
| `StderrLogger::enabled` | method | Returns 'true' if the log message's level does not exceed the configured maximum log level, otherwise 'false'. [crates/gwiki/src/main.rs:440-442] |
| `StderrLogger::log` | method | Conditionally writes log records to stderr in the format 'gwiki: {level}: {message}' if logging is enabled for the record's metadata. [crates/gwiki/src/main.rs:444-448] |
| `StderrLogger::flush` | method | This is an unimplemented instance method that accepts an immutable self reference and contains no executable code. [crates/gwiki/src/main.rs:450] |

_15 more symbol(s) not shown — run `gcode outline crates/gwiki/src/main.rs` for the full list._

