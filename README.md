# gobby-code

Fast Rust CLI for [Gobby](https://github.com/GobbyAI/gobby)'s code index. AST-aware search, symbol navigation, and dependency graph analysis — all from the command line.

Binary name: `gcode`

## What it does

`gcode` gives AI coding agents (and humans) fast access to a project's code graph without needing the Gobby daemon running. It reads and writes the same databases as the daemon — SQLite for symbols/search, Neo4j for the call graph, Qdrant for semantic vectors.

## Installation

### From GitHub Releases (recommended)

Download the latest binary for your platform from [Releases](https://github.com/GobbyAI/gobby-code/releases).

### From source

```bash
cargo install --git https://github.com/GobbyAI/gobby-code
```

### Via Gobby

```bash
gobby install  # Installs gcode automatically
```

## Usage

```bash
# Indexing (standalone — tree-sitter in Rust)
gcode index [<path>]                      # Full/incremental index
gcode index --files <f1> <f2>             # Index specific files
gcode status                              # Project stats
gcode invalidate                          # Clear index, force re-index

# Search
gcode search <query> [--limit N]          # Hybrid RRF (FTS + semantic + graph)
gcode search-text <query> [--limit N]     # FTS5 symbol names
gcode search-content <query> [--limit N]  # FTS5 file content

# Symbol retrieval
gcode outline <file>                      # Hierarchical symbol tree
gcode symbol <id>                         # Source by ID (byte-offset read)
gcode symbols <id1> <id2> ...             # Batch retrieve
gcode tree                                # File tree with symbol counts

# Graph (Neo4j)
gcode callers <name> [--limit N]          # Who calls this?
gcode usages <name> [--limit N]           # All references
gcode imports <file>                      # Import graph
gcode blast-radius <target> [--depth N]   # Transitive impact analysis

# Summaries
gcode summary <symbol_id>                 # Cached AI summary
gcode repo-outline                        # Directory-grouped stats

# Global flags
--project <path>     # Override project root
--format text|json   # Output format (default: json)
--quiet              # Suppress warnings
```

## Data layer

gcode shares Gobby's data layer — it is not a standalone database:

| Store | Purpose | Location |
|-------|---------|----------|
| SQLite | Symbols, FTS5 search, file metadata, config | `~/.gobby/gobby-hub.db` |
| Neo4j | Call graph, import graph, blast radius | HTTP API (config from DB) |
| Qdrant | Semantic vector search | REST API (config from DB) |

Config is resolved from `~/.gobby/bootstrap.yaml` → SQLite `config_store` table. Secrets are decrypted using Gobby's Fernet key derivation (`~/.gobby/machine_id` + `~/.gobby/.secret_salt`).

## Graceful degradation

| Service unavailable | Behavior |
|---------------------|----------|
| Neo4j down | Graph commands return `[]`. Search loses graph boost. |
| Qdrant down | Search loses semantic boost. FTS5 + graph still work. |
| GGUF model missing | Semantic embeddings disabled. FTS5 + graph still work. |
| No index yet | `gcode search` returns nothing. `gcode index` creates it. |

## Features

The `embeddings` Cargo feature (default: on) enables local GGUF embedding generation via `llama-cpp-2`. Requires cmake to build.

```bash
# Build with embeddings (macOS Metal GPU)
cargo build --release

# Build without embeddings (no cmake needed)
cargo build --release --no-default-features
```

## License

Apache 2.0

Copyright 2026 Gobby AI
