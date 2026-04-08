# gsqz User Guide

gsqz wraps shell commands and compresses their output for LLM consumption. Instead of feeding 500 lines of `git status` or test output into a context window, gsqz reduces it to the essential information.

## Installation

Download from [GitHub Releases](https://github.com/GobbyAI/gobby-cli/releases/latest) or build from source:

```bash
cargo install gobby-squeeze
```

If you use [Gobby](https://github.com/GobbyAI/gobby), gsqz is already installed.

## Quick Start

```bash
# Compress command output
gsqz -- git status
gsqz -- cargo test
gsqz -- uv run pytest tests/

# Explicit output subcommand (identical behavior)
gsqz output -- cargo build

# Compress prose/text from stdin
echo "In order to fix this..." | gsqz input
echo "verbose docs" | gsqz input --level aggressive

# Compound commands work — last segment matched for pipeline selection
gsqz -- "cargo build && cargo test"

# See compression stats
gsqz --stats -- git diff

# Generate default config in current directory
gsqz --init

# Inspect the resolved config
gsqz --dump-config
```

When compression is applied, output is prefixed with a header:
```text
[Output compressed by gsqz — git-status, 72% reduction]
Modified (3):
  src/main.rs
  src/lib.rs
  src/config.rs
Untracked (1):
  new_file.txt
```

## How It Works

1. gsqz runs your command via `sh -c` and captures stdout + stderr
2. ANSI escape codes are stripped
3. The command string is matched against pipeline regexes (first match wins)
4. The matched pipeline's steps run sequentially, each transforming the line list
5. If no pipeline matches, the fallback steps apply (default: truncate head:20, tail:20)
6. If compression doesn't achieve at least 5% reduction, the original output is returned unchanged

Output under 1000 characters is never compressed (configurable via `min_output_length`).

gsqz always exits with code 0 — the LLM reads pass/fail from the content itself.

## Pipeline Steps

Each pipeline defines an ordered list of steps. Each step takes the current lines and produces new lines.

### `filter_lines`

Removes lines matching any of the given regex patterns. Use this to strip noise — progress bars, blank lines, boilerplate headers.

```yaml
- filter_lines:
    patterns:
      - '^\s*$'            # blank lines
      - '^On branch '      # git status header
      - '^\s*Compiling '   # cargo build progress
```

### `group_lines`

Aggregates lines into a structured summary. Available modes:

| Mode | Use Case | What It Does |
|------|----------|-------------|
| `git_status` | `git status` | Groups files by status (M/A/D/R/C/U/??) with counts. Shows up to 20 files per group. |
| `pytest_failures` | pytest output | Extracts FAILURES/ERRORS sections and the summary line. Drops passing tests entirely. |
| `test_failures` | Any test runner | Detects FAIL/FAILED/ERROR lines and includes everything from the first failure onward. If no failures, outputs "All tests passed." |
| `lint_by_rule` | Linter output | Groups diagnostics by rule code (e.g. E001, W123, `[rule-name]`). Shows up to 5 examples per rule. |
| `by_extension` | `ls`, `tree` | Groups files by extension, sorted by count descending. Shows up to 10 per group. |
| `by_directory` | `find` | Groups paths by parent directory, sorted by count descending. Shows up to 10 per group. |
| `by_file` | `grep`, `rg` | Groups `file:line:match` output by file path. Shows up to 5 matches per file. |
| `errors_warnings` | Build output | Separates errors (up to 20 shown) from warnings (up to 10 shown), plus the last 3 lines of other output. |

### `truncate`

Keeps the first N and last N lines, replacing the middle with `[... X lines omitted ...]`.

```yaml
- truncate:
    head: 20       # keep first 20 lines (default: 20)
    tail: 10       # keep last 10 lines (default: 10)
```

**Per-section mode** truncates each section independently, useful for diffs:

```yaml
- truncate:
    per_file_lines: 50       # max lines per section
    file_marker: '^@@\s'     # regex that marks section boundaries
```

Each section is split at the marker and truncated individually, with `[... X lines omitted in section ...]` markers.

### `dedup`

Collapses consecutive identical or near-identical lines. "Near-identical" means lines that differ only in numbers (e.g. `error at pos 42` and `error at pos 99` are considered duplicates).

```yaml
- dedup: {}
```

Output:
```text
error at pos 42
  [repeated 3 times]
```

### `replace`

Applies regex substitution to each line with backreference support (`$1`, `$2`). Rules chain — each rule's output feeds the next. Useful for normalizing paths, version strings, or timestamps before other steps.

```yaml
- replace:
    rules:
      - pattern: '/home/[^/]+/projects/[^/]+/'
        replacement: './'
      - pattern: 'v\d+\.\d+\.\d+'
        replacement: 'vX.X.X'
```

### `match_output`

Checks the full output blob (not per-line) against regex rules. If a pattern matches and the optional `unless` pattern does NOT match, returns a short message immediately, skipping all remaining steps. First matching rule wins. Place early in the step sequence for maximum savings.

```yaml
- match_output:
    rules:
      - pattern: 'test result: ok\.'
        unless: 'FAILED|panicked'
        message: 'All tests passed.'
```

### `compress_prose`

Applies prose compression to the output. Three levels available:

- **lite** — collapse blank lines, strip HTML comments, trim trailing whitespace
- **standard** — lite + remove filler phrases ("In order to" → "To", etc.) and filler words, while preserving code blocks, inline code, URLs, XML tags, file paths, and headings
- **aggressive** — standard + keep only first sentence per paragraph, truncate lists >5 items

```yaml
- compress_prose:
    level: standard
```

## Prose Compression (Input Mode)

`gsqz input` compresses prose/text from stdin — useful for reducing verbose documentation, LLM responses, or any text before it enters a context window.

```bash
# Standard compression (default)
cat verbose-docs.md | gsqz input

# Aggressive — first sentence per paragraph, truncated lists
cat api-response.txt | gsqz input --level aggressive

# Lite — just whitespace cleanup
cat notes.txt | gsqz input --level lite
```

Protected regions (code blocks, YAML frontmatter, inline code, URLs, file paths, XML tags, headings) are preserved at all levels.

## Compound Commands

gsqz splits compound commands at `&&`, `||`, and `;` operators (respecting quotes and parentheses) and tries segments in reverse order for pipeline matching. The last segment's output is typically most relevant.

```bash
# "cargo test" segment matches the cargo-test pipeline
gsqz -- "cargo build && cargo test"
```

Pipe chains (`|`) are NOT split — the output comes from the last command in the pipe.

## Degradation Markers

When output quality is degraded, gsqz prepends markers so the LLM knows:

- `[gsqz:passthrough]` — no pipeline matched, fallback truncation applied
- `[gsqz:low-savings]` — a pipeline matched but achieved less than 5% compression

## On-Empty Fallback

When pipeline steps produce empty output, gsqz returns a configurable message instead of nothing:

```yaml
settings:
  on_empty: 'No output after compression.'

pipelines:
  my-pipeline:
    match: '\bmy-cmd\b'
    on_empty: 'Command produced no meaningful output.'
    steps: [...]
```

Pipeline-level `on_empty` overrides the global setting.

## Configuration

gsqz uses a single config file with simple priority:

| Priority | Path | Purpose |
|----------|------|---------|
| 1 | `--config path/to/file.yaml` | Explicit CLI override |
| 2 | `.gobby/gsqz.yaml` | Project-level config |
| 3 | `~/.gobby/gsqz.yaml` | Global config (auto-created on first run) |
| 4 | Compiled into binary | Built-in default (fallback) |

First found wins entirely — no merging between layers. On first run, gsqz auto-exports the default config to `~/.gobby/gsqz.yaml`. Run `gsqz --init` to write a project-level config to `.gobby/gsqz.yaml` (backs up existing to `gsqz.yaml.bak`).

### Settings

```yaml
settings:
  min_output_length: 1000      # skip compression below this char count
  max_compressed_lines: 100    # hard cap on compressed output lines
  daemon_url: "http://..."     # optional gobby daemon URL
```

### Excluding Commands

Commands matching these regexes are never compressed:

```yaml
excluded_commands:
  - '\bcat\b'
  - '\becho\b'
```

### Full Pipeline Example

```yaml
pipelines:
  terraform-plan:
    match: '\bterraform\s+plan\b'
    steps:
      - filter_lines:
          patterns:
            - '^\s*$'
            - '^\s*#'
            - 'Refreshing state'
      - group_lines:
          mode: errors_warnings
      - truncate:
          head: 40
          tail: 10
```

## Debugging

```bash
# See which pipelines are loaded and their match patterns
gsqz --dump-config

# See which strategy matched and compression ratio
gsqz --stats -- your-command-here
```

The `--stats` flag prints to stderr:
```text
[gsqz] strategy=pytest original=12847 compressed=1923 savings=85.0%
```

Strategy names to look for:
- A pipeline name (e.g. `git-status`, `pytest`, `cargo-test`) — matched and compressed
- `{name}/low-savings` — pipeline matched but compression was marginal (<5%)
- `{name}/on_empty` — pipeline produced empty output, on_empty fallback used
- `fallback` — no pipeline matched, generic truncation applied (with `[gsqz:passthrough]` marker)
- `passthrough` — output was too short or compression didn't help
- `excluded` — command matched an exclusion pattern
- `prose/{level}` — prose compression via `gsqz input`
