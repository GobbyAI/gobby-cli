# Gobby Build Restart Issues

This note records the restart and recovery problems seen while running the
`gcore-rust-foundation.md` build in `gobby-cli`.

## Context

- Observed: 2026-05-27 (or appropriate date)
- Repository: `/Users/josh/Projects/gobby-cli`
- Target branch: `dev`
- Plan file: `.gobby/plans/gcore-rust-foundation.md`
- Original task: `#208 Build gcore-rust-foundation.md`
- Replacement task: `#210 Build gcore-rust-foundation.md`
- Intended lifecycle: `planning -> expansion -> development -> holistic_qa -> merge`
- Skipped lifecycle stage: `pr`
- Isolation policy: planning and plan review run without worktree isolation; development-forward stages may use worktree isolation.
- Planning override: only planning needs `max_work_attempts=99,max_review_rounds=99`; later stages use defaults.

## What Failed

Task `#208` was seeded correctly at first, but a stale integration worktree was
deleted while the task was still active. After that, the build dispatcher
reported:

```text
Error: integration worktree metadata is missing; clean/restart
```

`gobby build clean '#208' --force --yes` did not repair the dispatcher state.
`gobby build stop '#208' --force --yes` stopped automation, but later restart
attempts reconstructed the lifecycle incorrectly.

The observed broken restart state was:

```text
planning -> merge
```

The expected lifecycle was:

```text
planning -> expansion -> development -> holistic_qa -> merge
```

`gobby tasks repair-lifecycle --task '#208'` found no repair candidates, so the
stunted manifest could not be fixed in place with the available task repair
command.

## Worktree Deletion Symptom

Deleting the integration worktree with:

```bash
gobby worktrees delete wt-46ea5b --yes --force
```

removed the worktree directory but exited with:

```text
Failed to delete worktree: None
```

Git then still had a prunable worktree registration until `git worktree prune`
was run. After pruning, `gobby worktrees list` showed no worktrees, but the
build task still expected missing integration metadata.

## Restart / Stage Selection Symptom

Restart attempts with a planning-only cap override left `#208` with only
`planning` and `merge`.

Example restart command:

```bash
gobby build restart '#208' --force --yes --no-resume \
  --skip-stage pr \
  --isolation worktree \
  --target-branch dev \
  --stage planning:max_work_attempts=99,max_review_rounds=99 \
  --coordinator '#181'
```

Expected result:

```text
planning -> expansion -> development -> holistic_qa -> merge
```

Actual result:

```text
planning -> merge
```

Fresh plan-file build later produced a healthy replacement task `#210`, so the
remaining issue on `#208` appears to be recovery of an already-damaged lifecycle
manifest rather than the normal fresh-build path.

## Current Recovery

The usable recovery path was to seed a fresh task from the current plan on
`dev`.

The replacement task `#210` has the correct lifecycle:

```text
planning -> expansion -> development -> holistic_qa -> merge
```

It was seeded from the R8 plan content with planning already at review round 8.
The plan adversary for the next planning review ran without worktree isolation,
as intended.

## Follow-Up Expectations

Gobby should be able to recover this class of damaged build state without
requiring a new task. The useful behavior would be:

- `gobby build restart` reconstructs the full intended lifecycle from the task's
  build provenance or plan-file seed.
- `repair-lifecycle` detects stunted manifests like `planning -> merge` when the
  plan/build provenance implies expansion, development, and QA stages.
- Worktree deletion either completes registry and Git cleanup atomically or
  fails before removing filesystem state.
- A planning-only cap override should preserve all non-planning stages.
- Planning remains non-isolated under a worktree-isolated build.
