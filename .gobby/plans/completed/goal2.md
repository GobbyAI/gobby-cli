 > **COMPLETED 2026-06-11.** All five steps done; verdict certified in fable-repo-analysis.md.
 > The "#597–#603, #613–#668" backlog framing below is superseded: the queue now lives under
 > epics #692 (gsqz/gloc/ghook), #704 (gcode), #705 (gwiki), #706 (gcore), with #590 holding
 > only #678 + closed history. Forward plan: .gobby/plans/goal3-backlog-agent.md.

 Goal: Parity-plus closeout — re-heal the codewiki via the daemon and certify the verdict

  Mission

  Phases 0–2 of the original parity-plus goal are complete: per-crate reviews, competitor
  feature analysis, and the parity matrix all live in ./fable-repo-analysis.md, with the
  review backlog filed under epic #590 (#597–#603, #613–#668, #678 — Josh's queue, leave
  untouched). Phase 3 stalled when the heal run silently degraded 7 codewiki pages
  (committed as a "heal" in 52e837a). The blockers have since been fixed and committed:

  - #694 — daemon text-generation routing validated (gwiki ask routes auto → daemon → frontier).
  - #695 (824c2fb) — gcore::ai re-gated behind the `ai` feature; tiny binaries lost the HTTP stack.
  - #687 (35cf05b) — degradation recorded on every fallback path; degraded docs repaired by re-runs;
    bounded transport retry; failed runs never displace healthy prose.
  - #681 (867f5bf) — unchanged docs reused with zero LLM calls; per-doc write-as-you-go persistence;
    interrupted runs resume from disk.

  Finish the remaining work and certify parity-plus with evidence.

  Definition of done: the 7 casualty pages carry AI prose generated through the daemon with
  bounded citations; a fallback sweep over .gobby/wiki finds nothing silent; all five binaries
  in ~/.gobby/bin are rebuilt from current dev with matching sidecars; fable-repo-analysis.md
  documents the regression, the re-heal, and the final per-dimension parity-plus verdict.

  Step 1 — #696: mid-tier profile for heavyweight prose

  Claim and implement #696. gcore gains an `ai.text_generate.profile` binding (default
  `feature_low`) plus a per-call profile override on `generate_via_daemon_with_max_tokens`,
  sent only when provider/model are unset. gcode codewiki passes the heavier profile
  (default `feature_mid`) for module/repo/architecture aggregate docs; file/symbol docs and
  gwiki ask/research stay on the default. Daemon side is config only: define `feature_mid`
  candidates via PUT /api/config/values — verify the key shape against gobby
  src/gobby/config/ai.py first. Gates: cargo nextest -p gobby-core --features ai,
  -p gobby-code --no-default-features, clippy workspace -D warnings, fmt.

  Step 2 — Surgical re-heal through the daemon

  1. Delete the 7 casualties: .gobby/wiki/code/repo.md, code/_architecture.md,
     code/modules/crates.md, code/modules/crates/gcode.md, code/modules/crates/gwiki.md,
     code/modules/crates/gcode/src.md, code/modules/crates/gwiki/src.md.
  2. Rebuild gcode first so the run uses #681/#687/#696 (cargo build --workspace --release;
     deploy per Step 4 mechanics or run from target/release).
  3. Run: gcode codewiki --out .gobby/wiki --ai-depth sections --verbose — routing auto →
     daemon → frontier. Post-#681 only the deleted pages and their changed parents
     regenerate (minutes). The run must go through the daemon; LM Studio/qwen direct
     routing is retired for text generation and local:lm-studio must never be a
     default or profile candidate.
  4. Verify: fallback sweep over .gobby/wiki/code finds no structural-fallback overviews
     ("covers N files across" / "direct files" first lines, citation-marker walls); no
     degraded: true anywhere except the legitimate codeowners_unavailable in _ownership.md;
     _meta/codewiki.json records no degraded entries; repo.md Overview is real prose with
     bounded citations (#682).
  5. Resume spot-check: interrupt a scoped codewiki run against a temp --out dir, re-run,
     confirm it resumes from disk without regenerating completed pages (#681 evidence).
  6. gwiki index; then commit only changed .gobby/wiki/** paths as
     [gobby-cli-#590] fix: re-heal silently degraded codewiki pages via daemon route.

  Step 3 — Analysis doc correction + final verdict

  Update ./fable-repo-analysis.md: document the heal run's silent regression (what and why —
  silenced once-only warning, unrecorded fallbacks, hash-skip preserving degraded pages) and
  the re-heal result; supersede 52e837a's "heal" claim (no history rewrite). Refresh the
  per-dimension parity matrix where the verdict depended on AI prose quality, incremental
  updates, or resume behavior — #681/#687 changed the incremental-update story materially.
  End with an explicit, evidence-backed parity-plus verdict per dimension.

  Step 4 — Rebuild + redeploy all five binaries

  cargo build --workspace --release; for each of gcode, gwiki, gsqz, gloc, ghook: atomic cp
  to ~/.gobby/bin/<name>.new then mv over the existing binary; refresh each .{name}-version
  sidecar; run ghook --version to rewrite .ghook-runtime.json. Dependency proof stays green:
  cargo tree -p gobby-squeeze/-local/-hooks -e normal shows no reqwest/ureq.

  Step 5 — End-to-end certification

  Following docs/guides only: gwiki search, ask, and compile against the healed vault;
  gwiki ask --llm --require-ai reports route: daemon. Fix any doc inaccuracy hit along the
  way (doc fixes are worked directly). Confirm the definition of done, then stop.

  Execution boundary

  Fable works directly: Steps 1–5, blocking bugs they surface, docs/guides corrections,
  coordinated daemon-side contract/config updates. Fable creates tasks only: new
  code-quality findings, consolidation ideas, features beyond the parity-plus baseline.

  Hard constraints

  - Branch dev; Josh pushes — never git push. Never git add -A (shared tree): stage explicit
    paths, verify git diff --cached --stat, commit with -- <paths>.
  - Claim a Gobby task before editing; close gates: fresh validation after last edit →
    commit → memory review → set_variable(memory_review_completed=true) →
    close_task(task_id, commit_sha, changes_summary). Stop at each closure boundary —
    Josh runs /compact manually.
  - No compatibility shims or legacy fallbacks. No unilateral hub-schema/config_store
    mutation from the CLIs; coordinated daemon-side changes are allowed.
  - Wiki/codewiki output may be wiped and rebuilt at any point.

  Two notes on choices I made: I ordered #696 before the re-heal (the plan's reason holds — the 7 casualties are exactly the heavyweight aggregate
  pages that should regenerate on the mid model), and I added the resume spot-check to Step 2 since it was the original plan's only unverified #681
  claim against the real binary.