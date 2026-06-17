---
title: crates/gwiki/src/support
type: code_module
provenance:
- file: crates/gwiki/src/support/config.rs
  ranges:
  - 18-20
  - 23-29
  - 31-43
  - 46-61
  - 68-71
  - 74-79
  - 82-86
  - 88-93
  - 96-102
  - 104-111
  - 113-118
  - 120-127
  - 129-136
  - 138-142
  - 144-151
  - 153-168
  - 182-185
  - 188-200
  - 204-211
  - 214-220
  - 223-225
  - 228-231
  - 235-237
  - 239-241
  - 245-257
  - 260-279
  - 283-301
  - 304-316
  - 320-332
  - 336-363
- file: crates/gwiki/src/support/counts.rs
  ranges:
  - 4-10
  - 12-20
  - 22-33
  - 36-42
  - 45-53
  - 56-72
  - 79-85
- file: crates/gwiki/src/support/env.rs
  ranges:
  - 21-24
  - 27-30
  - 32-49
  - 51-55
  - 57-66
  - 68-75
  - 77-89
  - 91-98
  - 100-109
  - 111-142
  - 144-154
  - 156-180
  - 182-188
  - 190-200
  - 202-218
  - 220-224
  - 226-234
  - 236-238
  - 251-257
  - 261-285
  - 288-297
  - 299-322
- file: crates/gwiki/src/support/graph.rs
  ranges:
  - 8-55
  - 57-90
  - 92-103
  - 105-107
  - 109-122
  - 124-146
  - 148-154
  - 162-192
  - 195-208
  - 211-236
  - 239-272
- file: crates/gwiki/src/support/mod.rs
  ranges:
  - 1-12
- file: crates/gwiki/src/support/postgres.rs
  ranges:
  - 6-39
  - 41-51
- file: crates/gwiki/src/support/scope.rs
  ranges:
  - 12-36
  - 38-42
  - 44-55
  - 60-66
  - 68-76
  - 78-87
  - 89-95
  - 97-102
  - 105-109
  - 111-122
- file: crates/gwiki/src/support/search.rs
  ranges:
  - 11-13
  - 16-21
  - '24'
  - 27-38
  - 41-43
  - 46-51
  - 53-57
  - 60-161
- file: crates/gwiki/src/support/text.rs
  ranges:
  - 7-13
  - 15-22
  - 26-46
  - 48-59
  - 61-73
  - 75-83
  - 85-91
  - 93-95
  - 97-99
  - 101-126
  - 133-138
  - 141-153
  - 156-166
- file: crates/gwiki/src/support/time.rs
  ranges:
  - 3-6
  - 8-17
  - 24-39
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/config.rs:18-20](crates/gwiki/src/support/config.rs#L18-L20), [crates/gwiki/src/support/config.rs:23-29](crates/gwiki/src/support/config.rs#L23-L29), [crates/gwiki/src/support/config.rs:31-43](crates/gwiki/src/support/config.rs#L31-L43), [crates/gwiki/src/support/config.rs:46-61](crates/gwiki/src/support/config.rs#L46-L61), [crates/gwiki/src/support/config.rs:68-71](crates/gwiki/src/support/config.rs#L68-L71), [crates/gwiki/src/support/config.rs:74-79](crates/gwiki/src/support/config.rs#L74-L79), [crates/gwiki/src/support/config.rs:82-86](crates/gwiki/src/support/config.rs#L82-L86), [crates/gwiki/src/support/config.rs:88-93](crates/gwiki/src/support/config.rs#L88-L93), [crates/gwiki/src/support/config.rs:96-102](crates/gwiki/src/support/config.rs#L96-L102), [crates/gwiki/src/support/config.rs:104-111](crates/gwiki/src/support/config.rs#L104-L111), [crates/gwiki/src/support/config.rs:113-118](crates/gwiki/src/support/config.rs#L113-L118), [crates/gwiki/src/support/config.rs:120-127](crates/gwiki/src/support/config.rs#L120-L127), [crates/gwiki/src/support/config.rs:129-136](crates/gwiki/src/support/config.rs#L129-L136), [crates/gwiki/src/support/config.rs:138-142](crates/gwiki/src/support/config.rs#L138-L142), [crates/gwiki/src/support/config.rs:144-151](crates/gwiki/src/support/config.rs#L144-L151), [crates/gwiki/src/support/config.rs:153-168](crates/gwiki/src/support/config.rs#L153-L168), [crates/gwiki/src/support/config.rs:182-185](crates/gwiki/src/support/config.rs#L182-L185), [crates/gwiki/src/support/config.rs:188-200](crates/gwiki/src/support/config.rs#L188-L200), [crates/gwiki/src/support/config.rs:204-211](crates/gwiki/src/support/config.rs#L204-L211), [crates/gwiki/src/support/config.rs:214-220](crates/gwiki/src/support/config.rs#L214-L220), [crates/gwiki/src/support/config.rs:223-225](crates/gwiki/src/support/config.rs#L223-L225), [crates/gwiki/src/support/config.rs:228-231](crates/gwiki/src/support/config.rs#L228-L231), [crates/gwiki/src/support/config.rs:235-237](crates/gwiki/src/support/config.rs#L235-L237), [crates/gwiki/src/support/config.rs:239-241](crates/gwiki/src/support/config.rs#L239-L241), [crates/gwiki/src/support/config.rs:245-257](crates/gwiki/src/support/config.rs#L245-L257), [crates/gwiki/src/support/config.rs:260-279](crates/gwiki/src/support/config.rs#L260-L279), [crates/gwiki/src/support/config.rs:283-301](crates/gwiki/src/support/config.rs#L283-L301), [crates/gwiki/src/support/config.rs:304-316](crates/gwiki/src/support/config.rs#L304-L316), [crates/gwiki/src/support/config.rs:320-332](crates/gwiki/src/support/config.rs#L320-L332), [crates/gwiki/src/support/config.rs:336-363](crates/gwiki/src/support/config.rs#L336-L363)
- [crates/gwiki/src/support/counts.rs:4-10](crates/gwiki/src/support/counts.rs#L4-L10), [crates/gwiki/src/support/counts.rs:12-20](crates/gwiki/src/support/counts.rs#L12-L20), [crates/gwiki/src/support/counts.rs:22-33](crates/gwiki/src/support/counts.rs#L22-L33), [crates/gwiki/src/support/counts.rs:36-42](crates/gwiki/src/support/counts.rs#L36-L42), [crates/gwiki/src/support/counts.rs:45-53](crates/gwiki/src/support/counts.rs#L45-L53), [crates/gwiki/src/support/counts.rs:56-72](crates/gwiki/src/support/counts.rs#L56-L72), [crates/gwiki/src/support/counts.rs:79-85](crates/gwiki/src/support/counts.rs#L79-L85)
- [crates/gwiki/src/support/env.rs:21-24](crates/gwiki/src/support/env.rs#L21-L24), [crates/gwiki/src/support/env.rs:27-30](crates/gwiki/src/support/env.rs#L27-L30), [crates/gwiki/src/support/env.rs:32-49](crates/gwiki/src/support/env.rs#L32-L49), [crates/gwiki/src/support/env.rs:51-55](crates/gwiki/src/support/env.rs#L51-L55), [crates/gwiki/src/support/env.rs:57-66](crates/gwiki/src/support/env.rs#L57-L66), [crates/gwiki/src/support/env.rs:68-75](crates/gwiki/src/support/env.rs#L68-L75), [crates/gwiki/src/support/env.rs:77-89](crates/gwiki/src/support/env.rs#L77-L89), [crates/gwiki/src/support/env.rs:91-98](crates/gwiki/src/support/env.rs#L91-L98), [crates/gwiki/src/support/env.rs:100-109](crates/gwiki/src/support/env.rs#L100-L109), [crates/gwiki/src/support/env.rs:111-142](crates/gwiki/src/support/env.rs#L111-L142), [crates/gwiki/src/support/env.rs:144-154](crates/gwiki/src/support/env.rs#L144-L154), [crates/gwiki/src/support/env.rs:156-180](crates/gwiki/src/support/env.rs#L156-L180), [crates/gwiki/src/support/env.rs:182-188](crates/gwiki/src/support/env.rs#L182-L188), [crates/gwiki/src/support/env.rs:190-200](crates/gwiki/src/support/env.rs#L190-L200), [crates/gwiki/src/support/env.rs:202-218](crates/gwiki/src/support/env.rs#L202-L218), [crates/gwiki/src/support/env.rs:220-224](crates/gwiki/src/support/env.rs#L220-L224), [crates/gwiki/src/support/env.rs:226-234](crates/gwiki/src/support/env.rs#L226-L234), [crates/gwiki/src/support/env.rs:236-238](crates/gwiki/src/support/env.rs#L236-L238), [crates/gwiki/src/support/env.rs:251-257](crates/gwiki/src/support/env.rs#L251-L257), [crates/gwiki/src/support/env.rs:261-285](crates/gwiki/src/support/env.rs#L261-L285), [crates/gwiki/src/support/env.rs:288-297](crates/gwiki/src/support/env.rs#L288-L297), [crates/gwiki/src/support/env.rs:299-322](crates/gwiki/src/support/env.rs#L299-L322)
- [crates/gwiki/src/support/graph.rs:8-55](crates/gwiki/src/support/graph.rs#L8-L55), [crates/gwiki/src/support/graph.rs:57-90](crates/gwiki/src/support/graph.rs#L57-L90), [crates/gwiki/src/support/graph.rs:92-103](crates/gwiki/src/support/graph.rs#L92-L103), [crates/gwiki/src/support/graph.rs:105-107](crates/gwiki/src/support/graph.rs#L105-L107), [crates/gwiki/src/support/graph.rs:109-122](crates/gwiki/src/support/graph.rs#L109-L122), [crates/gwiki/src/support/graph.rs:124-146](crates/gwiki/src/support/graph.rs#L124-L146), [crates/gwiki/src/support/graph.rs:148-154](crates/gwiki/src/support/graph.rs#L148-L154), [crates/gwiki/src/support/graph.rs:162-192](crates/gwiki/src/support/graph.rs#L162-L192), [crates/gwiki/src/support/graph.rs:195-208](crates/gwiki/src/support/graph.rs#L195-L208), [crates/gwiki/src/support/graph.rs:211-236](crates/gwiki/src/support/graph.rs#L211-L236), [crates/gwiki/src/support/graph.rs:239-272](crates/gwiki/src/support/graph.rs#L239-L272)
- [crates/gwiki/src/support/mod.rs:1-12](crates/gwiki/src/support/mod.rs#L1-L12)
- [crates/gwiki/src/support/postgres.rs:6-39](crates/gwiki/src/support/postgres.rs#L6-L39), [crates/gwiki/src/support/postgres.rs:41-51](crates/gwiki/src/support/postgres.rs#L41-L51)
- [crates/gwiki/src/support/scope.rs:12-36](crates/gwiki/src/support/scope.rs#L12-L36), [crates/gwiki/src/support/scope.rs:38-42](crates/gwiki/src/support/scope.rs#L38-L42), [crates/gwiki/src/support/scope.rs:44-55](crates/gwiki/src/support/scope.rs#L44-L55), [crates/gwiki/src/support/scope.rs:60-66](crates/gwiki/src/support/scope.rs#L60-L66), [crates/gwiki/src/support/scope.rs:68-76](crates/gwiki/src/support/scope.rs#L68-L76), [crates/gwiki/src/support/scope.rs:78-87](crates/gwiki/src/support/scope.rs#L78-L87), [crates/gwiki/src/support/scope.rs:89-95](crates/gwiki/src/support/scope.rs#L89-L95), [crates/gwiki/src/support/scope.rs:97-102](crates/gwiki/src/support/scope.rs#L97-L102), [crates/gwiki/src/support/scope.rs:105-109](crates/gwiki/src/support/scope.rs#L105-L109), [crates/gwiki/src/support/scope.rs:111-122](crates/gwiki/src/support/scope.rs#L111-L122)
- [crates/gwiki/src/support/search.rs:11-13](crates/gwiki/src/support/search.rs#L11-L13), [crates/gwiki/src/support/search.rs:16-21](crates/gwiki/src/support/search.rs#L16-L21), [crates/gwiki/src/support/search.rs:24](crates/gwiki/src/support/search.rs#L24), [crates/gwiki/src/support/search.rs:27-38](crates/gwiki/src/support/search.rs#L27-L38), [crates/gwiki/src/support/search.rs:41-43](crates/gwiki/src/support/search.rs#L41-L43), [crates/gwiki/src/support/search.rs:46-51](crates/gwiki/src/support/search.rs#L46-L51), [crates/gwiki/src/support/search.rs:53-57](crates/gwiki/src/support/search.rs#L53-L57), [crates/gwiki/src/support/search.rs:60-161](crates/gwiki/src/support/search.rs#L60-L161)
- [crates/gwiki/src/support/text.rs:7-13](crates/gwiki/src/support/text.rs#L7-L13), [crates/gwiki/src/support/text.rs:15-22](crates/gwiki/src/support/text.rs#L15-L22), [crates/gwiki/src/support/text.rs:26-46](crates/gwiki/src/support/text.rs#L26-L46), [crates/gwiki/src/support/text.rs:48-59](crates/gwiki/src/support/text.rs#L48-L59), [crates/gwiki/src/support/text.rs:61-73](crates/gwiki/src/support/text.rs#L61-L73), [crates/gwiki/src/support/text.rs:75-83](crates/gwiki/src/support/text.rs#L75-L83), [crates/gwiki/src/support/text.rs:85-91](crates/gwiki/src/support/text.rs#L85-L91), [crates/gwiki/src/support/text.rs:93-95](crates/gwiki/src/support/text.rs#L93-L95), [crates/gwiki/src/support/text.rs:97-99](crates/gwiki/src/support/text.rs#L97-L99), [crates/gwiki/src/support/text.rs:101-126](crates/gwiki/src/support/text.rs#L101-L126), [crates/gwiki/src/support/text.rs:133-138](crates/gwiki/src/support/text.rs#L133-L138), [crates/gwiki/src/support/text.rs:141-153](crates/gwiki/src/support/text.rs#L141-L153), [crates/gwiki/src/support/text.rs:156-166](crates/gwiki/src/support/text.rs#L156-L166)
- [crates/gwiki/src/support/time.rs:3-6](crates/gwiki/src/support/time.rs#L3-L6), [crates/gwiki/src/support/time.rs:8-17](crates/gwiki/src/support/time.rs#L8-L17), [crates/gwiki/src/support/time.rs:24-39](crates/gwiki/src/support/time.rs#L24-L39)

</details>

# crates/gwiki/src/support

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

The `crates/gwiki/src/support` module serves as the primary utility and infrastructure layer for the GWiki system, centralizing environment resolution, configuration, database validation, search pipeline scoring, and structural graph construction [crates/gwiki/src/support/mod.rs:1-12]. It manages the runtime environment by dynamically detecting the PostgreSQL database URL using env variables, local brokered daemons, bootstrap files, or global Gcore configurations [crates/gwiki/src/support/env.rs:21-24, crates/gwiki/src/support/env.rs:32-49]. Once the runtime environment is detected, the module provides configuration resolution and connection validation utilities—including `HubPrimary` and `require_attached_index`—to establish schema validation, execute index-dependent database connections, and securely resolve secret-backed values through PostgreSQL [crates/gwiki/src/support/config.rs:18-20, crates/gwiki/src/support/postgres.rs:6-39].

The module also handles document processing, text analysis, and structural metadata. It builds an in-memory wiki graph from stored documents, links, and sources, sanitizing raw link targets, normalizing paths, and utilizing precomputed document slug maps for path-target matching [crates/gwiki/src/support/graph.rs:8-55, crates/gwiki/src/support/graph.rs:57-90]. For search and query operations, the module handles query tokenization, keyword relevance scoring, code-path sanitization, short text snippet extraction, and status label formatting [crates/gwiki/src/support/text.rs:7-13, crates/gwiki/src/support/text.rs:15-22, crates/gwiki/src/support/text.rs:26-46, crates/gwiki/src/support/text.rs:48-59]. It coordinates with `gobby_core` for core path and config resolution [crates/gwiki/src/support/config.rs:46-61] and calculates row count metrics for document index tables [crates/gwiki/src/support/counts.rs:4-10].

### Environment Variables

| Environment Variable | Description | Source Span |
| --- | --- | --- |
| GWIKI_DATABASE_URL | The primary environment variable used to resolve the PostgreSQL database URL. |  |
| GOBBY_POSTGRES_DSN | Secondary environment variable used as a fallback for the PostgreSQL database connection DSN. |  |
| GWIKI_BROKER_TIMEOUT_MS | Configures custom timeout duration in milliseconds for communicating with local CLI brokers. |  |

### Public API Symbols

| Symbol Name | Purpose / Responsibility | Source Span |
| --- | --- | --- |
| HubPrimary | ConfigSource layer mapping encrypted keys through an active PostgreSQL hub connection. | [crates/gwiki/src/support/config.rs:18-20] |
| hub_ai_config_source | Factory function establishing AI context config sources from Gobby home and database options. | [crates/gwiki/src/support/config.rs:46-61] |
| IndexCounts | Models grouped row totals for document, chunk, link, source, and ingestion tables. | [crates/gwiki/src/support/counts.rs:4-10] |
| index_counts | Computes IndexCounts metrics from an in-memory store. | [crates/gwiki/src/support/counts.rs:12-20] |
| postgres_index_counts | Queries IndexCounts metrics out of a PostgreSQL database connection. | [crates/gwiki/src/support/counts.rs:22-33] |
| database_url / database_url_for | Resolves database connection URLs using environment variables, brokers, or local fallback configurations. | [crates/gwiki/src/support/env.rs:21-24, crates/gwiki/src/support/env.rs:27-30] |
| memory_graph_from_store | Constructs a memory-backed WikiGraphFacts using stored documents, links, and sources. | [crates/gwiki/src/support/graph.rs:8-55] |
| require_attached_index | Connects to PostgreSQL and runs schema validation, raising errors if components are missing. | [crates/gwiki/src/support/postgres.rs:6-39] |
| require_postgres_index | Establishes a simple, read-only PostgreSQL client connection. | [crates/gwiki/src/support/postgres.rs:41-51] |
| query_tokens | Splits a search query into normalized lowercase alphanumeric tokens. | [crates/gwiki/src/support/text.rs:7-13] |
| keyword_score | Calculates frequency of search tokens in target text. | [crates/gwiki/src/support/text.rs:15-22] |
| sanitize_code_path | Validates and converts a path string into a safe, repository-relative file path. | [crates/gwiki/src/support/text.rs:26-46] |
| snippet_from_text | Safely extracts the first non-empty line of text, truncating and adding an ellipsis if over 240 chars. | [crates/gwiki/src/support/text.rs:48-59] |
| unix_timestamp_ms / collect_timestamp | Retrieves the current system epoch timestamp in milliseconds or formats it as an identifier prefix. | [crates/gwiki/src/support/time.rs:3-6, crates/gwiki/src/support/time.rs:8-17] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/support/config.rs\|crates/gwiki/src/support/config.rs]] | This file centralizes GWiki configuration resolution. It defines `HubPrimary`, a `ConfigSource` that reads config and resolves secret-backed values through a PostgreSQL hub when available, and `hub_ai_config_source`, which builds an AI config source from Gobby home plus an optional database connection. It also provides defaults and resolution helpers for shared code graph and indexing settings, including logic to read local `gcore.yaml`, prefer config over standalone defaults, and validate or clamp limit values. The remaining pieces are test/support utilities: `EnvGuard` and `write_file` manage temporary Gobby home state, while `TestSource` supplies a controllable `ConfigSource` for tests that verify defaults, precedence, YAML loading, and rejection of invalid limits. [crates/gwiki/src/support/config.rs:18-20] [crates/gwiki/src/support/config.rs:23-29] [crates/gwiki/src/support/config.rs:31-43] [crates/gwiki/src/support/config.rs:46-61] [crates/gwiki/src/support/config.rs:68-71] |
| [[code/files/crates/gwiki/src/support/counts.rs\|crates/gwiki/src/support/counts.rs]] | This file defines a small count-reporting helper for gwiki indexes. `IndexCounts` groups row totals for documents, chunks, links, sources, and ingestions, and `index_counts` computes those totals directly from the in-memory store. `postgres_index_counts` computes the same structure from PostgreSQL for a given search scope by calling `postgres_count` on each logical table. `GwikiTable` provides the fixed table-name mapping used by the SQL helper, and the test locks those identifiers down so the count queries stay pointed at the expected tables. [crates/gwiki/src/support/counts.rs:4-10] [crates/gwiki/src/support/counts.rs:12-20] [crates/gwiki/src/support/counts.rs:22-33] [crates/gwiki/src/support/counts.rs:36-42] [crates/gwiki/src/support/counts.rs:45-53] |
| [[code/files/crates/gwiki/src/support/env.rs\|crates/gwiki/src/support/env.rs]] | Resolves and validates gwiki runtime environment settings, centered on how to find the PostgreSQL database URL and related broker/daemon metadata. `database_url` tries direct env vars first, then falls back through a brokered lookup, a bootstrap file, and finally gcore config; `database_url_for` wraps failures in `WikiError` for command-specific reporting. The rest of the helpers support that flow by reading local tokens, building broker requests with timeouts, validating loopback daemon URLs and database URLs, parsing trimmed/positive env values, and spawning the broker when needed. [crates/gwiki/src/support/env.rs:21-24] [crates/gwiki/src/support/env.rs:27-30] [crates/gwiki/src/support/env.rs:32-49] [crates/gwiki/src/support/env.rs:51-55] [crates/gwiki/src/support/env.rs:57-66] |
| [[code/files/crates/gwiki/src/support/graph.rs\|crates/gwiki/src/support/graph.rs]] | This file builds an in-memory wiki graph from a `MemoryWikiStore` and provides the target-resolution logic that turns stored links into graph edges. `memory_graph_from_store` gathers documents, links, and sources into `WikiGraphFacts`, while `resolve_graph_target` normalizes each link target, rejects external/URL-like targets, resolves relative paths from the source document directory, and falls back to a precomputed slug-to-path map so links can be matched to the correct document. The smaller helpers support that flow by classifying path-like targets, normalizing paths, and deriving slug mappings used during resolution. [crates/gwiki/src/support/graph.rs:8-55] [crates/gwiki/src/support/graph.rs:57-90] [crates/gwiki/src/support/graph.rs:92-103] [crates/gwiki/src/support/graph.rs:105-107] [crates/gwiki/src/support/graph.rs:109-122] |
| [[code/files/crates/gwiki/src/support/mod.rs\|crates/gwiki/src/support/mod.rs]] | Defines the `support` module tree for `gwiki`, exposing internal submodules for config, counts, environment handling, graph logic, PostgreSQL access, scope, search, text, and time utilities, plus a test-only environment module. [crates/gwiki/src/support/mod.rs:1-12] |
| [[code/files/crates/gwiki/src/support/postgres.rs\|crates/gwiki/src/support/postgres.rs]] | Provides PostgreSQL-backed configuration checks for commands that depend on a wiki index. `require_attached_index` resolves the command’s database URL, opens a read-only PostgreSQL connection, runs runtime schema validation through `ValidationContext`, and returns a config error if any required index pieces are missing. `require_postgres_index` is the simpler helper that only resolves the database URL and returns a read-only `postgres::Client`, failing with a config error if no DSN is configured or the connection cannot be established. [crates/gwiki/src/support/postgres.rs:6-39] [crates/gwiki/src/support/postgres.rs:41-51] |
| [[code/files/crates/gwiki/src/support/scope.rs\|crates/gwiki/src/support/scope.rs]] | Resolves a user’s `ScopeSelection` into the concrete vault scope, output identity, and search scope used by the wiki, then uses that resolution to build an in-memory indexed store when the selected root is a directory. The helpers in the file translate between resolved vault scopes, search/store scope representations, and command precedence rules, with topic scopes taking priority over project scopes and a default project fallback of `"current"`. [crates/gwiki/src/support/scope.rs:12-36] [crates/gwiki/src/support/scope.rs:38-42] [crates/gwiki/src/support/scope.rs:44-55] [crates/gwiki/src/support/scope.rs:60-66] [crates/gwiki/src/support/scope.rs:68-76] |
| [[code/files/crates/gwiki/src/support/search.rs\|crates/gwiki/src/support/search.rs]] | This file provides support implementations for the wiki search pipeline. It includes a BM25 backend that simply returns precomputed store hits up to the requested limit, a semantic backend placeholder that always returns no results with a `qdrant` not-configured degradation, and a `PostgresConfigSource` adapter that reads and resolves config values from a PostgreSQL client. The `store_search_hits` helper ties the store side together by tokenizing the query, rejecting empty queries, scanning in-memory documents, filtering and scoring them with the shared text helpers, and assembling ranked `WikiSearchResult` values. [crates/gwiki/src/support/search.rs:11-13] [crates/gwiki/src/support/search.rs:16-21] [crates/gwiki/src/support/search.rs:24] [crates/gwiki/src/support/search.rs:27-38] [crates/gwiki/src/support/search.rs:41-43] |
| [[code/files/crates/gwiki/src/support/text.rs\|crates/gwiki/src/support/text.rs]] | Utilities for query handling, text normalization, and display labels used by `gwiki` support code. The file splits search queries into lowercase tokens, scores text against those tokens, sanitizes code paths into safe repo-relative strings, and extracts short snippets from larger text. It also maps degradation and document/object kinds into stable label strings, and provides slugification and path-display helpers, with tests covering path sanitization, snippet ellipsis handling, and slugify fallback/max-length behavior. [crates/gwiki/src/support/text.rs:7-13] [crates/gwiki/src/support/text.rs:15-22] [crates/gwiki/src/support/text.rs:26-46] [crates/gwiki/src/support/text.rs:48-59] [crates/gwiki/src/support/text.rs:61-73] |
| [[code/files/crates/gwiki/src/support/time.rs\|crates/gwiki/src/support/time.rs]] | This file provides small time utilities for the wiki support code. `unix_timestamp_ms` reads the current `SystemTime`, converts it to Unix epoch milliseconds, and returns `WikiError::Config` if the clock is before the epoch or the value does not fit in `u64`; `collect_timestamp` builds on that by formatting the result as `unix-ms:{millis}`. The test checks that `unix_timestamp_ms` returns a plausible epoch-millisecond timestamp within a recent range. [crates/gwiki/src/support/time.rs:3-6] [crates/gwiki/src/support/time.rs:8-17] [crates/gwiki/src/support/time.rs:24-39] |

## Components

| Component ID |
| --- |
| `bf09877f-8772-5b79-a0ea-177a058fea73` |
| `46a3fb54-b9ad-5717-be8e-31b1ea45da5f` |
| `7e81b3d9-3fd8-5dce-b466-5aa424f98ba2` |
| `03673ec0-e042-5ecb-8465-83e2e29b50c4` |
| `faa4c6ea-6b38-5a26-b2f0-43a0a74136be` |
| `fe650e09-8172-5b62-82ad-66fb771a5059` |
| `410c7d5e-0ab7-5e59-965c-ebac3fe2d0a2` |
| `f55cd370-a57f-5a75-a653-96990fbd8c19` |
| `60853d35-bf82-58e6-ad93-cc1f079f8d0d` |
| `d61deee2-96f4-5fde-ace0-2f4e6cd04042` |
| `d63925a8-cd8e-5d7e-82ab-f08e1213999a` |
| `fbc1bd41-cbfc-577a-aabe-3bcc8801eb76` |
| `c35262bf-e907-56e5-a22b-192bcc35ddcf` |
| `8f6696ea-2c91-51c7-8c27-d72238555df6` |
| `d0057609-80cc-5913-9b05-63a231f0a13e` |
| `fef1c01e-4e64-5064-9a84-fedd43d43c67` |
| `9b254d32-ba5e-511e-933d-54eb161a4d0d` |
| `7d7aa43d-75b2-5e0a-8631-f66e995e198d` |
| `562394c7-f0b4-5683-a08e-78c1833110e3` |
| `162348de-8b35-5292-872d-aae9d34f1e6a` |
| `6ce590b9-9982-5fc5-bba7-38ce4f07de55` |
| `bbe05f32-4c07-5393-aa0e-c64985500da8` |
| `a3921349-05db-58ca-aaf4-ca8caa1c947f` |
| `18816624-9bb0-5bf6-92ae-cca2b4841b3e` |
| `f1646dc9-8c4c-58f1-9150-c0f8cce540f5` |
| `cc49d970-fc85-595f-aae5-63d7e1050965` |
| `78da5e83-3767-5309-8c31-229eca2daee8` |
| `7bd819cf-723b-5c97-a07b-5e6035272491` |
| `97fc85e9-83df-5235-9cd4-56db6ab3aba5` |
| `eaf58024-bf53-5d32-bbf3-478b8b17238d` |
| `656f145d-38f1-5e5f-8d2f-3e5b9e20e1e1` |
| `fc6bcd38-24d5-5898-abd8-f7cccb038630` |
| `b479c64e-4fae-51b0-92fe-d60f7c9f9d94` |
| `95bb5c54-adbf-5876-a1e5-d79aac9a09ba` |
| `dbfc88fd-48d8-53db-864a-51902f6844ea` |
| `92643004-1821-5f95-a129-821545208e0d` |
| `c79499c8-39f6-5d27-85e5-9ec608e58c4a` |
| `6eef951c-c8de-5b3b-9eeb-431794396c90` |
| `8786c9c3-4b38-5f85-8f9a-a2fa7b4b178a` |
| `7acfa5f4-1a8d-55c2-8c66-45705c0b2ae9` |
| `58500376-9458-5dd0-aacc-f3d53c8080f0` |
| `1fad4bf4-a690-52bc-8d03-af8b394ae02c` |
| `18b25317-47eb-57e2-a149-7bee167bfb4a` |
| `30377db8-c862-5fb7-a883-ddd62e0e4acb` |
| `96399e18-c124-5761-8a66-ebd00f10e793` |
| `61248448-64b6-5ffa-b408-02fe22e9008a` |
| `ce1e7c82-54fe-51d6-8571-84cfc5fe744e` |
| `3e2c75af-1071-5ca2-a35a-c7576e8bb014` |
| `920f35da-5b07-5065-b5fa-c5ab57f1ad2c` |
| `65d37a63-038e-5844-85cd-a977b9824c6e` |
| `51ab5688-3f0e-5b2e-8541-8fe116e619a9` |
| `d20510a2-2f42-591d-b7be-4edd7db4fba3` |
| `bb07c06f-6a16-5a03-b359-d42af8261ce6` |
| `227d07d9-395c-5de5-b248-f26b36b2c4fb` |
| `aafef5e8-bf8a-5a7f-a7d7-e7a44e2a4855` |
| `4dadd1a6-e5a9-5733-8ff9-727835cf4023` |
| `d5b21cc5-c6c1-530d-8aac-f21ed1660bd6` |
| `6091d7ec-1fde-5e22-b8d8-76e452eb8ad4` |
| `df1722b7-7ee6-534e-ae75-bd9bd50080e3` |
| `c58bfe53-d5ea-5e3b-8307-5db7d7679aeb` |
| `fbf0a734-28e0-54f1-a47d-63120beb0197` |
| `cd20f1ee-83ea-57bb-96a3-d927c3608429` |
| `c5197c2f-64c9-5a8b-abd7-ffce06d1e758` |
| `5b38ce11-b074-5501-ad0f-a67c932f35f7` |
| `a6f8ad7e-af2f-59a1-bae5-47c7094b7d91` |
| `f10918ae-5486-56ec-bb51-c573bd941deb` |
| `289e2b52-0509-5e66-b63a-ba50562a6513` |
| `d111c3fe-cfab-50a5-8389-52b9fb7880ec` |
| `7437ceb8-e970-50fa-bca9-257417e413de` |
| `0e66cf59-0d78-55be-9627-7fe994e92989` |
| `e5e4bf14-b0e4-5ecf-a2e7-b9ca1e8a01db` |
| `5f965f9d-b719-59de-84bd-72e703a7bc08` |
| `8f54063e-8084-55f1-b7d1-bf23dfd5fb0c` |
| `821fcfba-0b58-5df4-bb53-99251b725b62` |
| `c6b77ff9-7bf5-59cd-a76d-7e4e64dd367e` |
| `48263c4e-f642-5b7b-9ebd-554b1bf614e9` |
| `f7e64c9b-bd8c-56a3-85e1-a58a9e27c5ec` |
| `1a05aa2b-117b-54d7-849b-2696e6197f32` |
| `b5b3766e-efe7-5e0f-a92e-2813c361acfd` |
| `cfa277c0-f6f7-5eed-8532-63622bc7b822` |
| `0b81337a-18a6-53c5-b6fa-fd3e0d49c61c` |
| `3bcc6db3-11eb-5919-8bfe-ee76e46c64b8` |
| `57275bba-d082-54ff-b944-52fdd9f97c05` |
| `1f0c3d0f-f271-5426-a656-c12b82843f34` |
| `0ab4dcb5-bbbc-51a8-b5ef-972b072e1658` |
| `15803901-4cc1-572d-a4ba-7110dfe6fe1a` |
| `7c1fea1d-963a-5541-9f57-2744e8bb5f8d` |
| `2325a736-cca6-5936-9f50-8c4900f9f802` |
| `70142db5-bd7d-559f-b313-2ac7ee7cb55b` |
| `23d15dc3-e88a-5fc5-8acf-a92884afbccf` |
| `9d7a2ce6-8feb-5fb6-aa36-19986c3ef7b7` |
| `91790d1a-0fe3-5fc3-ab61-2655714dc637` |
| `e6ee4298-a16f-59b0-8280-90cadaa5fcc3` |
| `a19532b2-de2b-59bd-8b3b-75376c885954` |
| `67129cf2-e917-5cd9-b30a-aed2a05b5be1` |
| `d42b4658-ebe0-52ae-a9e1-373a5a81d760` |
| `972dc6e5-2409-58d6-b9ed-89de9de3b427` |
| `a33408bc-a2eb-574c-b231-09c256188203` |
| `f9678e6e-5cab-5644-9005-69225719f089` |
| `85deb1dd-437d-5e93-bed7-18ce0f2b4493` |
| `9e229e53-0e5c-5140-b948-55f4b02e870a` |
| `8cf79b6a-4e06-5249-bb09-a271f3e99c7a` |
| `68bfe972-fb6b-5463-b9b8-292389fe08ce` |
| `3e2f928b-097a-5b21-9bce-c31e8a06b096` |
| `846416e3-5b33-5a34-aaa2-933004d7b604` |
| `53594747-a121-50f2-a698-e8d276c76a69` |
