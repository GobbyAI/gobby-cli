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
| `SearchArgs` | class | 'SearchArgs' is a CLI argument struct for a search command that accepts a required 'query' string, an optional '--limit' 'usize' defaulting to '10', and a '--no-semantic' flag to disable semantic vector search for that query. [crates/gwiki/src/main.rs:226-236] |
| `AskArgs` | class | 'AskArgs' is a CLI argument struct that captures the required 'question' string plus flags controlling wiki-hit answer synthesis ('--llm'), AI routing override ('--ai' with 'auto\|daemon\|direct\|off'), and hard-failure behavior when no AI route succeeds ('--require-ai'). [crates/gwiki/src/main.rs:239-254] |
| `SyncSessionsArgs` | class | 'SyncSessionsArgs' is a CLI argument struct that optionally specifies the path to a directory of archived '*.jsonl.gz' session transcripts and an optional positive upper bound on how many archives to process. [crates/gwiki/src/main.rs:257-265] |
| `BenchmarkArgs` | class | 'BenchmarkArgs' is a command-line argument struct that defines a single 'retrieval_candidates: usize' option, parsed as a positive integer and defaulting to 'BenchmarkOptions::DEFAULT_RETRIEVAL_CANDIDATES', for configuring seeded retrieval precision probes. [crates/gwiki/src/main.rs:268-276] |
| `parse_positive_usize` | function | Parses 'value' as a 'usize' and returns it only if it is strictly greater than zero, otherwise converting the parse error or a zero value into a 'String' error. [crates/gwiki/src/main.rs:278-289] |
| `RemoveSourceArgs` | class | 'RemoveSourceArgs' is a CLI argument struct for removing a source by 'id', with flags to enable a non-mutating 'dry_run', bypass confirmation via 'yes', and preserve the referenced raw asset via 'keep_asset'. [crates/gwiki/src/main.rs:292-307] |
| `RefreshArgs` | class | 'RefreshArgs' is a CLI argument struct that collects zero or more source IDs to refresh via repeated '--id SOURCE_ID' flags and an optional '--dry-run' flag to preview refresh candidates without performing fetch, write, delete, or index operations. [crates/gwiki/src/main.rs:310-318] |
| `ReadArgs` | class | 'ReadArgs' is a CLI argument struct containing two optional flags, 'path: Option<PathBuf>' for selecting a vault-relative wiki path to read and 'title: Option<String>' for resolving a first-heading title within that selected scope. [crates/gwiki/src/main.rs:326-334] |
| `BacklinksArgs` | class | 'BacklinksArgs' is a command-line argument struct containing a single required 'page' field of type 'String', accepted as a positional value named 'PAGE'. [crates/gwiki/src/main.rs:337-340] |
| `LinkSuggestArgs` | class | 'LinkSuggestArgs' is a CLI argument struct that defines a single '--limit' option of type 'usize', defaulting to '10', to cap the number of suggestions returned. [crates/gwiki/src/main.rs:343-346] |
| `CompileArgs` | class | 'CompileArgs' is a clap-parsed argument struct for a compile command that optionally accepts a topic positional, multiple outline and source values, a 'CompileKind' selector defaulting to 'topic', an optional target page path, a 'write-intent' flag, and an AI routing mode defaulting to 'auto'. [crates/gwiki/src/main.rs:349-374] |
| `ExportArgs` | class | 'ExportArgs' is a Rust CLI argument struct that contains a single 'command' field of type 'ExportSubcommand', declared as the program’s subcommand selector via '#[command(subcommand)]'. [crates/gwiki/src/main.rs:377-380] |
| `ReviewReportArgs` | class | 'ReviewReportArgs' is a CLI argument struct that collects repeated '--file' and '--symbol' identifiers, an optional '--diff' path, and an '--output' filename defaulting to 'review-report.md' for generating a review report. [crates/gwiki/src/main.rs:383-396] |
| `ExportSubcommand` | type | Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:399-413] |
| `CompileKind` | type | Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:416-420] |
| `StderrLogger` | class | 'StderrLogger' is a zero-sized struct type that serves as a stderr-backed logger implementation. [crates/gwiki/src/main.rs:427] |
| `StderrLogger::enabled` | method | Returns 'true' when the log record’s level is less than or equal to the current global maximum log level, and 'false' otherwise. [crates/gwiki/src/main.rs:432-434] |
| `StderrLogger::log` | method | Checks whether the record’s metadata is enabled and, if so, writes a formatted log line of the form 'gwiki: <level>: <message>' to standard error via 'eprintln!'. [crates/gwiki/src/main.rs:436-440] |
| `StderrLogger::flush` | method | 'flush' is a no-op method that takes an immutable reference to 'self' and performs no state changes or I/O. [crates/gwiki/src/main.rs:442] |

_15 more symbol(s) not shown — run `gcode outline crates/gwiki/src/main.rs` for the full list._

