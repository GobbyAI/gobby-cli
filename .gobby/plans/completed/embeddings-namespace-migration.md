# Embeddings Namespace Migration (gobby-cli) — `embeddings.* → ai.embeddings.*`

<!-- markdownlint-disable MD013 MD036 -->

**Plan ID:** embeddings-namespace-migration

## O1: Overview

`kind: framing`

The gobby-cli (gcode + standalone `gcore.yaml`) half of a **cross-repo P0**: rename embedding configuration from the
legacy `embeddings.*` namespace to `ai.embeddings.*`, with **no aliases at the end state** and **no env-var layer**, using
**expand → migrate → contract** with dual-read so it ships independently of the daemon and ends shim-free. The companion
daemon epic (same Plan ID, in `~/Projects/gobby`) owns the `config_store` rewrite. The downstream `gwiki-multimodal-ai`
epic's §8.2 (gcode embed-routing) is a **consumer that depends on this epic's Contract (P3)** — it does not re-own the cut.

**Why now:** the rename is shared config; a no-alias atomic flip would force a same-window co-release and risk silently
disabling code-index reindex / semantic search. It also fixes a pre-existing split — gcode reads `embeddings.vector_dim`
while the daemon writes/reads `embeddings.dim` — unified here on **`ai.embeddings.dim`**. Verified live: this daemon-managed
install holds `embeddings.{api_base=http://localhost:1234/v1, model=text-embedding-nomic-embed-text-v1.5@f16, dim=768,
api_key}`; `ai.embeddings.*` does not exist yet.

`## M1` (task manifest) is intentionally omitted — emitted by adversarial expansion on approval, then validated
`--mode expansion`.

## C1: Contract & constraints

`kind: framing`

- **Config sources — NO ENV VARS (product decision)**: gcode/standalone embedding config resolves **only** from
  `config_store` (when a hub DSN is reachable) → `~/.gobby/gcore.yaml` → defaults, plus CLI flags. The `GOBBY_EMBEDDING_*`
  env layer is removed; **no `GOBBY_AI_*` env keys are introduced**. DB-DSN discovery (locating the hub) is infra and
  unaffected.
- **Key set** (gcore.yaml + config_store, no env): `ai.embeddings.{api_base, model, api_key, query_prefix, provider, dim}`.
  Dimension unifies on **`ai.embeddings.dim`**. **Old dim keys are repo-specific**: gcode's old dim key is
  `embeddings.vector_dim` (the daemon's is `embeddings.dim`), and gcode's P1 dual-read maps **this repo's** old key
  (`embeddings.vector_dim`) into canonical `ai.embeddings.dim`. No pre-0.5.0 key (`embeddings.*`, `GOBBY_EMBEDDING_*`,
  `embeddings.api_key_env`) survives at P3.
- **api_key storage differs by mode**: attached mode may store `ai.embeddings.api_key = $secret:NAME` in `config_store`
  and resolve it through the daemon-backed secret path. Daemonless standalone mode has no secret store, so
  `~/.gobby/gcore.yaml` may store the optional `ai.embeddings.api_key` as a plaintext local user token. `gcode` output
  must still redact it (`api_key_present` + fingerprint only), and `gcore.yaml` must remain user-local / uncommitted. The
  legacy `embeddings.api_key_env` env-indirection is **retired**, not renamed.
- **Migration ownership**: only the daemon rewrites `config_store`; gcode/standalone changes are **`gcore.yaml`-only**.
- **Dim advisory**: gcode auto-detects the embedding dimension from the endpoint (mirroring the daemon's
  `_probe_embedding_dim`); `ai.embeddings.dim` is an override only.
- **Canonical-read sequencing** (P1 reads old-canonical, P2 flips): P1 dual-reads preferring `embeddings.*` →
  `ai.embeddings.*` (behavior unchanged); P2 flips to prefer `ai.embeddings.*` after the daemon's migration has populated
  rows; P3 drops the old fallback.
- **CI guard (allowlisted)**: all embedding key names live in **one constants module**; a CI test rejects any literal
  `embeddings.`/`ai.embeddings.` string outside that module + migration code + their tests; tightened at P3.
- **Verified key inventory** (do not miss any): resolver `crates/gcore/src/config.rs:166-173`
  (`embeddings.api_base/model/api_key/query_prefix`); gcode dim `crates/gcode/src/config/context.rs:39-40`
  (`embeddings.vector_dim`); standalone env-indirection `crates/gcore/src/provisioning.rs:123`
  (`embeddings.api_key_env`, retired); writers `crates/gcore/src/provisioning.rs:513-517` +
  `crates/gcode/src/commands/setup.rs:264`; client `crates/gcode/src/vector/code_symbols/embedding.rs`.

## R1: Phase order

`kind: framing`

`P1 (Expand)` → `P2 (Migrate)` → `P3 (Contract)`. The **namespace** dual-read is non-breaking and ships anytime
(resolution still lands on the old `embeddings.*`), but **P1 drops the `GOBBY_EMBEDDING_*` env layer immediately** — a
deliberate, accepted breaking change (the no-env product decision, C1): current code still resolves
`GOBBY_EMBEDDING_URL/_MODEL/_API_KEY` (`crates/gcore/src/config.rs:168`) and `GOBBY_EMBEDDING_VECTOR_DIM`
(`crates/gcode/src/config/services.rs:203`), and at P1 the resolver stops consulting them, so env-configured installs must
move those values into `config_store`/`gcore.yaml`. P3 (the no-alias cut) is gated on the daemon epic's Migrate landing
first, so every reachable install already carries `ai.embeddings.*` rows.

## P1: Expand

`kind: framing`

**Goal**: introduce `ai.embeddings.*` as a dual-read (old canonical) — **namespace-non-breaking** (resolution still lands
on `embeddings.*`) but with one **intentional breaking change: the `GOBBY_EMBEDDING_*` env layer is dropped here**
(accepted, per the no-env decision — C1) — centralize key names, make dimension advisory, and ship the doctor.

### 1.1 Centralize embedding key names + allowlisted CI guard [category: code]

`kind: deliverable`

Target: `crates/gcore/src/config.rs`, `crates/gcode/src/config/context.rs`

Move every embedding key string into one constants module and add an allowlisted CI test rejecting literal `embeddings.`/
`ai.embeddings.` strings outside that module + the migration code + their tests. This is the anchor for the no-alias cut at
P3.

**Acceptance:**

- 1.1.1 - All embedding key names resolve from a single constants module; no other module contains a literal embedding key
  string. test: `crates/gcore/src/config.rs::tests::embedding_keys_centralized`.
- 1.1.2 - The CI guard fails on a stray `embeddings.`/`ai.embeddings.` literal added outside the allowlist. test:
  `crates/gcore/src/config.rs::tests::ci_guard_rejects_stray_literal`.

### 1.2 Advisory dimension via endpoint probe [category: code]

`kind: deliverable`

Target: `crates/gcode/src/vector/code_symbols/embedding.rs`, `crates/gcode/src/config/context.rs`, `crates/gcode/src/config/services.rs`

gcode auto-detects the embedding dimension from the endpoint (a 1-token probe mirroring the daemon's `_probe_embedding_dim`);
`ai.embeddings.dim` becomes an override only, and the legacy `GOBBY_EMBEDDING_VECTOR_DIM` env read
(`crates/gcode/src/config/services.rs:203`) is dropped (no-env decision — an intentional P1 breaking change). This resolves
the `vector_dim`/`dim` split independently of the prefix.

**Acceptance:**

- 1.2.1 - With no configured dim, gcode probes the endpoint for the dimension; a configured `ai.embeddings.dim` overrides
  the probe. test: `crates/gcode/src/vector/code_symbols/embedding.rs::tests::dim_probe_with_override`.

### 1.3 Dual-read with old canonical, no env layer [category: code]

`kind: deliverable`

Target: `crates/gcore/src/config.rs`

Resolve every embedding field (`api_base`, `model`, `api_key`, `query_prefix`, `provider`, `dim`) preferring `embeddings.*`
→ falling back to `ai.embeddings.*`, across `config_store` (read-only) + `gcore.yaml` only — **no env layer** in the
resolver. For the `dim` field specifically, gcode's old key is `embeddings.vector_dim` (not `embeddings.dim`), so the
dual-read maps `embeddings.vector_dim` → canonical `ai.embeddings.dim`; dim is otherwise probe-advisory per §1.2, with the
config value an override. For `config_store`/`gcore.yaml`-configured installs behavior is unchanged (nothing writes the
new namespace yet, so resolution still lands on `embeddings.*`); the **one** intentional change is that `GOBBY_EMBEDDING_*`
env vars are no longer honored — the deliberate P1 breaking change (no-env decision), so env-configured installs must
relocate those values to `config_store`/`gcore.yaml`.

**Acceptance:**

- 1.3.1 - Each field reads `embeddings.*` when present and falls back to `ai.embeddings.*` otherwise; a `GOBBY_*` env var
  for an embedding key has no effect. test: `crates/gcore/src/config.rs::tests::dual_read_old_canonical_no_env`.

### 1.4 `gcode embeddings doctor` [category: code]

`kind: deliverable`

Target: `crates/gcode/src/commands/embeddings_doctor.rs`, `crates/gcode/src/cli.rs`

A read-only consistency check emitting the shared-contract JSON (`endpoint, model, dim, api_key_present,
api_key_fingerprint, namespace_resolved, source, agrees, drift`) — `api_key_fingerprint` is the api_key's `sha256[:16]`
redaction (`string | null`). **Exit-code contract** (shared verbatim with the daemon doctor): `0` = healthy (embedding
config resolved and self-consistent; `agrees=true`, or `agrees=null` when no daemon peer is reachable — daemon-absent is
exit 0, not an error); `10` = config not resolved (`namespace_resolved=null` — no embedding config in either namespace);
`11` = drift (`agrees=false` — gcode and the daemon both resolve config but disagree on ≥1 of endpoint/model/dim); `20` =
probe/transport failure (couldn't reach the embedding endpoint or the daemon doctor route to verify). **`drift` shape**:
`null` when `agrees ∈ {true, null}`; otherwise an array of `{ field, self, peer }` objects, one per differing field
(`field ∈ {"endpoint","model","dim"}`; `self` = this tool's resolved value, `peer` = the daemon's; values
`string|number|null`).

**Acceptance:**

- 1.4.1 - `gcode embeddings doctor` emits the contract JSON with the api_key redacted and never errors when the daemon is
  down (agrees=null, exit 0 if self-consistent). test: `crates/gcode/src/commands/embeddings_doctor.rs::tests::doctor_json_and_exit_codes`.

## P2: Migrate

`kind: framing`

**Goal**: once the daemon epic's migration has populated `ai.embeddings.*` rows, flip gcode's canonical read to prefer the
new namespace.

### 2.1 Flip canonical read to prefer `ai.embeddings.*` [category: code]

`kind: deliverable`

Target: `crates/gcore/src/config.rs`

Flip the resolver to prefer `ai.embeddings.*` → fall back to `embeddings.*`; verify standalone and daemon-attached installs
resolve from the new namespace and the doctor reports agreement.

**Acceptance:**

- 2.1.1 - The resolver prefers `ai.embeddings.*`, still falling back to `embeddings.*`; the doctor reports
  `namespace_resolved = "ai.embeddings"`. test: `crates/gcore/src/config.rs::tests::flip_prefers_new_namespace`.

## P3: Contract

`kind: framing`

**Goal**: the gcode/standalone no-alias cut — the gwiki-multimodal-ai §8.2 routing refactor depends on this.

### 3.1 Drop old-key fallback; `ai.embeddings.*` only [category: code]

`kind: deliverable`

Target: `crates/gcore/src/config.rs`, `crates/gcode/src/config/context.rs`

Remove the `embeddings.*` fallback in the resolver and the gcode dim path; `ai.embeddings.*` is the only supported shape.

**Acceptance:**

- 3.1.1 - Pre-0.5.0 keys (`embeddings.*`, `embeddings.api_key_env`, the old `GOBBY_EMBEDDING_*` env reads) are not honored;
  only `ai.embeddings.*` resolves. test: `crates/gcore/src/config.rs::tests::legacy_keys_not_honored`.

### 3.2 Move gcore.yaml writers; retire env-indirection [category: code]

`kind: deliverable`

Target: `crates/gcore/src/provisioning.rs`, `crates/gcode/src/commands/setup.rs`

The standalone writers emit `ai.embeddings.*`; the `StandaloneConfig` `embeddings.api_key_env` env-indirection is retired
so the standalone api-key is read straight from the local standalone config's optional plaintext `ai.embeddings.api_key`.
Attached daemon/config_store mode may still use `$secret:` references through the daemon-backed resolver. Update the
standalone-config round-trip tests.

**Acceptance:**

- 3.2.1 - Standalone provisioning/setup write `ai.embeddings.*` (incl. provider/query_prefix); optional standalone
  `ai.embeddings.api_key` is read directly from local `gcore.yaml` with no `api_key_env` indirection, and command output
  redacts it. test: `crates/gcore/src/provisioning.rs::tests::writes_ai_embeddings_standalone_api_key`.

### 3.3 Tighten the CI allowlist [category: code]

`kind: deliverable`

Target: `crates/gcore/src/config.rs`

Delete the legacy constants from the allowlist so any remaining `embeddings.` literal fails CI.

**Acceptance:**

- 3.3.1 - After P3 the CI guard rejects any `embeddings.` (old-namespace) literal anywhere. test:
  `crates/gcore/src/config.rs::tests::ci_guard_rejects_legacy_namespace`.

## VS1: Verification

`kind: verification`

The gobby-cli half succeeds when: `ai.embeddings.*` resolves with no env layer and no plaintext api_key (C1); dimension is
advisory and unified on `ai.embeddings.dim`; P1 is non-breaking (old canonical) and P2 flips to the new namespace; `gcode
embeddings doctor` agrees with the daemon (or reports `agrees=null` standalone) and redacts the key; and at P3 no pre-0.5.0
embedding key (`embeddings.*`, `embeddings.api_key_env`, `GOBBY_EMBEDDING_*`) is honored, with the CI guard enforcing it.
The gwiki-multimodal-ai §8.2 embed-routing refactor consumes this epic's P3 output.
