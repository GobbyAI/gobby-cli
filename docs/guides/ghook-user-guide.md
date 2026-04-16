# ghook User Guide

ghook is the sandbox-tolerant hook dispatcher Gobby uses to receive lifecycle and tool-use events from host AI CLIs (Claude Code, Codex, Gemini CLI, Qwen CLI). It enqueues an envelope to `~/.gobby/hooks/inbox/` *before* attempting to POST to the local Gobby daemon — so the daemon's drain worker can replay any envelope whose POST was lost to a sandbox FS-read denial, a network blip, or a daemon restart.

You don't usually invoke ghook directly. The Gobby installer wires it into each host CLI's hook configuration. This guide explains what it does, how to verify it's working, and how to wire it manually if you need to.

## Installation

If you use [Gobby](https://github.com/GobbyAI/gobby), ghook is already installed and wired into your supported AI CLIs.

Otherwise, install from a release binary or crates.io:

```bash
cargo install gobby-hooks
```

The binary is named `ghook` (the package is `gobby-hooks` to disambiguate from singular use; the binary stays short).

## How It Works

```text
host AI CLI fires hook
  └─ runs ghook --gobby-owned --cli=<c> --type=<t>
      ├─ resolves project root (walk up from cwd to .gobby/project.json)
      ├─ reads stdin (the host CLI's hook payload)
      ├─ enriches input_data with terminal_context (when applicable)
      ├─ writes envelope atomically to ~/.gobby/hooks/inbox/
      └─ POSTs envelope to the Gobby daemon
          ├─ 2xx → delete inbox file, exit 0
          └─ failure → leave inbox file, exit 0 or 2 depending on --critical
                       └─ daemon's drain worker replays on next tick
```

Spool-first ordering is the whole point. If anything between ghook and the daemon goes wrong (sandbox FS denial, network blip, daemon restart), the envelope is already on disk and the daemon will pick it up on its next drain pass. From the host CLI's perspective the hook either succeeded or failed-loud (exit 2) — replay is invisible.

## CLI Surface

ghook has three modes. Exactly one must be selected.

```text
ghook --gobby-owned --cli=<c> --type=<t> [--critical] [--detach]
ghook --diagnose    --cli=<c> --type=<t>
ghook --version
```

| Flag | Mode | Purpose |
|------|------|---------|
| `--gobby-owned` | dispatch | Normal hook invocation. Reads stdin, enqueues, attempts POST. |
| `--diagnose` | introspection | Prints a JSON snapshot of what *would* happen. No network, no envelope write. |
| `--version` | metadata | Prints version and writes `~/.gobby/bin/.ghook-compatibility` for the daemon. |
| `--cli` | required for dispatch/diagnose | Host CLI name: `claude`, `codex`, `gemini`, `qwen`. Case-insensitive. |
| `--type` | required for dispatch/diagnose | Hook type. CLI-specific (e.g. `session-start` for Claude, `SessionStart` for Codex/Gemini/Qwen, `PreToolUse`, `PostToolUse`, `Stop`, `pre-compact`, `session-end`). |
| `--critical` | dispatch | Treat enqueue/POST failure as fatal — exit 2 to signal the host CLI. Default is exit 0 even on failure (envelope is still spooled). |
| `--detach` | dispatch | After enqueue and project-root walk-up, call `setsid(2)` to escape the host CLI's process group before the POST. Useful for hooks where the host CLI tears down its session immediately. |

### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Delivered (2xx) **OR** non-critical failure (envelope enqueued for replay). |
| `2` | Critical failure (envelope enqueued; signals the host CLI to abort). Used when `--critical` is set and POST fails. |

The `2` exit signals the host CLI that the hook didn't deliver synchronously. The envelope is *still* enqueued — the daemon will replay it. `--critical` is only about whether ghook tells the host CLI "this hook didn't go through right now," not about whether the event is lost.

## Wiring ghook into Claude Code

Most users get this configured automatically by the Gobby installer. To wire it manually, add hook entries to your Claude Code `settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "ghook --gobby-owned --cli=claude --type=session-start --critical"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "ghook --gobby-owned --cli=claude --type=session-end --critical"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "ghook --gobby-owned --cli=claude --type=PreToolUse"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "ghook --gobby-owned --cli=claude --type=PostToolUse"
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "ghook --gobby-owned --cli=claude --type=pre-compact --critical"
          }
        ]
      }
    ]
  }
}
```

Claude Code uses lowercase-hyphenated names internally for some hooks (`session-start`, `pre-compact`, `session-end`) and PascalCase for others (`PreToolUse`, `PostToolUse`). ghook treats `--type` as an opaque string, so pass the exact identifier the daemon expects for that CLI.

The `--critical` flag is on lifecycle hooks (`session-start`, `session-end`, `pre-compact`) because these set up state the daemon needs immediately. Tool-use hooks are non-critical — the envelope still spools, but a transient daemon outage won't block your tool call.

### Codex, Gemini, Qwen

Same pattern with different `--cli` and `--type` values. ghook's per-CLI registry (see `crates/ghook/src/cli_config.rs`) defines which hooks are critical and which receive enriched terminal context for each host CLI:

| CLI | Critical hooks | Terminal-context hooks |
|-----|----------------|------------------------|
| `claude` | `session-start`, `session-end`, `pre-compact` | `session-start` |
| `codex` | `SessionStart`, `Stop` | `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop` |
| `gemini` | `SessionStart` | `SessionStart` |
| `qwen` | `SessionStart` | `SessionStart` |

Unknown `--cli` values are tolerated — ghook uses the literal name as the source identifier and skips terminal-context enrichment. Hooks written for future CLIs won't break.

## Diagnose Mode

`ghook --diagnose` is the fastest way to confirm a hook is wired correctly. It runs the same configuration resolution as `--gobby-owned` but skips the network and the envelope write — pure introspection.

```bash
$ ghook --diagnose --cli=claude --type=session-start
{
  "schema_version": 1,
  "ghook_version": "0.1.0",
  "cli": "claude",
  "hook_type": "session-start",
  "source": "claude",
  "critical": true,
  "terminal_context_enabled": true,
  "daemon_url": "http://127.0.0.1:60887",
  "daemon_host": "127.0.0.1",
  "daemon_port": 60887,
  "project_root": "/Users/josh/Projects/gobby-cli",
  "project_id": "3bf57fe7-2a0c-4074-8912-a83d9cd4df01",
  "terminal_context_preview": {
    "parent_pid": 72441,
    "tty": "/dev/ttys005",
    "tmux_pane": "%179",
    "term_program": "tmux",
    "...": "..."
  },
  "cli_recognized": true
}
```

Look for:

- **`cli_recognized: true`** — confirms ghook knows about this CLI. `false` means it'll still spool, but without terminal-context enrichment and without honoring the per-CLI critical-hooks list.
- **`critical: true/false`** — does ghook *itself* consider this hook type critical for that CLI? Note this is independent of the `--critical` flag, which the host CLI sets based on its own settings.
- **`terminal_context_enabled: true`** — will ghook inject `terminal_context` into `input_data` for this hook? Required for hooks that the daemon uses to reconcile spawned-terminal agents.
- **`daemon_url`** — where will the POST go? If this is wrong, fix `~/.gobby/bootstrap.yaml`.
- **`project_root` / `project_id`** — did ghook correctly walk up from cwd to the project? `null` means no `.gobby/project.json` was found — daemon will receive the envelope without an `X-Gobby-Project-Id` header.

The diagnose JSON is validated against `crates/ghook/schemas/diagnose-output.v1.schema.json` in tests, so the schema is stable.

## Inbox & Replay

Envelopes spool to `~/.gobby/hooks/inbox/<prefix>-<ts13>-<uuid>.json`:

| Filename part | Meaning |
|---------------|---------|
| `prefix` | `c` (critical) or `n` (non-critical) — lets the drain worker prioritize critical hooks first |
| `ts13` | 13-digit zero-padded ms since epoch — gives lex-sortable filenames so drain order matches enqueue order |
| `uuid` | Random v4 — disambiguates within the same millisecond |
| `.tmp` suffix | Intermediate write; never a valid replay target. `atomic_write` does write→fsync→rename so the drain only ever sees fully-written envelopes. |

**Don't touch this directory by hand.** The daemon's drain worker owns it. If you need to clear stuck envelopes, stop the daemon first, delete the files, then start it again.

### Quarantine

Malformed stdin (the host CLI sent something that isn't valid JSON) lands in `~/.gobby/hooks/inbox/quarantine/` as a pair of files:

- `<stem>.json` — body containing the raw stdin bytes, base64-encoded.
- `<stem>.meta.json` — sidecar with `reason: "malformed_stdin"`, the JSON parse error, and the same base64 payload.

The drain never replays quarantined envelopes — they surface via `gobby status` and daemon logs so you can investigate.

## Troubleshooting

### `ghook: no mode specified`

You ran ghook without `--gobby-owned`, `--diagnose`, or `--version`. Pick one. The host CLI's hook command should always include `--gobby-owned`.

### `--gobby-owned requires --cli and --type`

Both flags are mandatory in dispatch mode. Check the hook entry in your host CLI's `settings.json`.

### Hook fires but daemon never receives it

1. `ghook --diagnose --cli=<c> --type=<t>` — confirm `daemon_url` is right and the CLI is recognized.
2. `ls ~/.gobby/hooks/inbox/` — if envelopes are piling up here, ghook is enqueuing fine but the daemon isn't draining. Check that the daemon is running.
3. If the inbox is empty too, the host CLI may not be invoking ghook at all. Check the host CLI's hook log/output.

### Hook returns exit 2 unexpectedly

The hook is marked `--critical` and the POST failed. The envelope is still spooled — check `~/.gobby/hooks/inbox/` for a `c-...json` file. The daemon will replay it. If you don't want exit 2 to signal the host CLI, drop `--critical` from the hook command (but only if you're OK with delayed delivery for that hook type).

### Sandbox FS-read denials (macOS)

The whole point of ghook's design is that this case is survivable. The envelope is written before the POST is attempted, and project-root walk-up happens before any potential `--detach`. If you see the daemon receive the envelope on the *next* hook fire instead of immediately, that's the drain worker doing its job — not a bug.

### Schema version mismatch

Envelopes carry `schema_version: 1`. If the daemon rejects envelopes for being a newer version than it understands, the daemon needs updating. ghook's `--version` command writes `~/.gobby/bin/.ghook-compatibility` so the daemon can detect this.
