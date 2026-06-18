---
title: crates/gwiki/src/setup.rs
type: code_file
provenance:
- file: crates/gwiki/src/setup.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/setup.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/setup.rs` exposes 25 indexed API symbols.

## How it fits

`crates/gwiki/src/setup.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GwikiTable` | type | Indexed type `GwikiTable` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:29-35] |
| `GwikiTable::name` | method | Indexed method `GwikiTable::name` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:38-46] |
| `GwikiPostgresObjectKind` | type | Indexed type `GwikiPostgresObjectKind` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:50-54] |
| `GwikiPostgresObject` | class | Indexed class `GwikiPostgresObject` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:57-61] |
| `GwikiStandaloneSetup` | class | Indexed class `GwikiStandaloneSetup` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:64-66] |
| `GwikiStandaloneSetup::new` | method | Indexed method `GwikiStandaloneSetup::new` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:69-73] |
| `GwikiStandaloneSetup::schema` | method | Indexed method `GwikiStandaloneSetup::schema` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:76-78] |
| `GwikiStandaloneSetup::postgres_objects` | method | Indexed method `GwikiStandaloneSetup::postgres_objects` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:80-101] |
| `GwikiStandaloneSetup::table_sql` | method | Indexed method `GwikiStandaloneSetup::table_sql` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:103-192] |
| `GwikiStandaloneSetup::index_sql` | method | Indexed method `GwikiStandaloneSetup::index_sql` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:194-228] |
| `GwikiStandaloneSetup::qualified_relation_name` | method | Indexed method `GwikiStandaloneSetup::qualified_relation_name` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:230-236] |
| `GwikiStandaloneSetup::namespace` | method | Indexed method `GwikiStandaloneSetup::namespace` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:240-242] |
| `GwikiStandaloneSetup::owned_objects` | method | Indexed method `GwikiStandaloneSetup::owned_objects` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:244-250] |
| `GwikiStandaloneSetup::create` | method | Indexed method `GwikiStandaloneSetup::create` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:252-266] |
| `default_setup` | function | Indexed function `default_setup` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:269-271] |
| `table` | function | Indexed function `table` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:273-279] |
| `index` | function | Indexed function `index` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:281-287] |
| `preflight` | function | Indexed function `preflight` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:289-295] |
| `owned_object` | function | Indexed function `owned_object` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:297-305] |
| `execute_postgres_ddl` | function | Indexed function `execute_postgres_ddl` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:307-329] |
| `quote_identifier` | function | Indexed function `quote_identifier` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:331-355] |
| `setup_creates_only_gwiki_owned_objects` | function | Indexed function `setup_creates_only_gwiki_owned_objects` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:363-454] |
| `published_lists_match_generated_objects` | function | Indexed function `published_lists_match_generated_objects` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:457-480] |
| `quote_identifier_rejects_names_over_postgres_byte_limit` | function | Indexed function `quote_identifier_rejects_names_over_postgres_byte_limit` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:483-488] |
| `quote_identifier_rejects_escaped_names_over_postgres_byte_limit` | function | Indexed function `quote_identifier_rejects_escaped_names_over_postgres_byte_limit` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:491-496] |

