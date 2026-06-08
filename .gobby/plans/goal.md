 Act as the Gobby build coordinator for the gwiki/gcode Parity+ epic, using `.gobby/plans/gwiki-parity-plus.md` as
  the build plan and root epic `#513`.

  This prompt is for Codex. Use Gobby skills through `gobby-skills` MCP only. Start with progressive discovery:

  1. `list_mcp_servers`
  2. `list_tools("gobby-skills")`
  3. `get_tool_schema("gobby-skills", "get_skill")`
  4. `call_tool("gobby-skills", "get_skill", {"name": "<skill>"})`

  Load these skills before coordinating:
  - `loading-skills`
  - `brevity`
  - `build-coordinator`
  - `task-creation`
  - `task-transitions`
  - `source-control`
  - `build`

  Use progressive tool discovery for every Gobby MCP server/tool you call.

  Create a separate coordination epic outside the `gwiki-parity-plus` task tree. Use that epic for coordinator work and
  for every Gobby daemon/build-system bug discovered during this run.

  Launch the build:

  ```bash
  gobby build .gobby/plans/gwiki-parity-plus.md \
    --isolation worktree \
    --stage planning:max_review_rounds=99 \
    --skip-stage pr \
    --coordinator current

  Constraints:

  - Worktree isolation for every build agent.
  - Up to 99 planning review rounds.
  - No PR stage.
  - Leave merge behavior at default auto-merge.
  - Keep planning-seed-state defaulted to drafted.
  - The plan is already drafted and gobby plans validate clean.
  - Planning, review, expansion, development, holistic QA, and merge should run through normal build automation.
  - After expansion and before development dispatch, inspect the target task tree once and normalize implementation leaves
    to the development stage unless the build state explicitly requires otherwise.

  Daemon/build-system fixes:

  - This run is authorized to edit ~/Projects/gobby.
  - Treat coordinator intervention as evidence of an unattended-build gap.
  - File every discovered Gobby build/daemon bug under the coordination epic.
  - Fix blocking daemon/build bugs immediately.
  - Fix non-blocking daemon/build bugs while agents are running or when otherwise idle.
  - Commit daemon fixes path-scoped in ~/Projects/gobby, linked to the bug task.
  - Every discovered build bug must be fixed, committed, linked, and closed before closing the target epic unless
    genuinely blocked on a user decision.

  Build journal:

  - Maintain an append-only task-<coordination-epic-ref>-build-journal.md in ~/Projects/gobby/.
  - For every Gobby daemon/build-system issue discovered, append a dated entry with:
      - symptom
      - where it surfaced in the build
      - affected ~/Projects/gobby file/symbol
      - root cause
      - action taken, including fix commit SHA and restart-gate result, or handoff prompt if deferred
      - linked coordination-epic child task ref

  - Commit the journal path-scoped in ~/Projects/gobby:
      - git commit -- task-<ref>-build-journal.md
      - never git add -A
      - verify staged diff contains only that file before committing

  Post-fix daemon restart gate:
  When a daemon/build-system fix affects dispatch, spawn, build controls, stage transitions, session handoff, worktree/
  clone isolation, or agent startup:

  - assume the running daemon still has old code
  - stop or keep blocked affected targets
  - stop agents spawned through stale behavior
  - record run IDs, task refs, workspace paths, and isolation metadata
  - notify active agents before restarting the daemon
  - restart daemon
  - verify daemon health
  - call gobby-sessions:compact_self
  - run a full status sweep
  - confirm the next spawned agent uses expected isolation/workspace metadata before resuming that path

  Coordinator loop:
  Each tick, check:

  - build status
  - stage state
  - active agents
  - build history
  - task tree health
  - workspace/worktree health
  - claimed tasks
  - session state

  Use:

  - gobby-tasks
  - gobby-agents
  - gobby-sessions
  - gobby-worktrees
  - relevant build/history tools discovered through MCP

  Work the highest-priority actionable coordination bug first. Resume or launch automation only after blocking bugs on the
  immediate dispatch path are fixed and restart-gated.

  Use gobby-agents:wait_for_agent(timeout_seconds=300) only as the final idle action when agents are running and no
  coordinator work remains.

  Resolve escalations directly unless a genuine user decision is required.

  Do not manually tick the dispatcher to keep a healthy build moving. Manual ticks/resumes are diagnostics or recovery
  actions only, and require evidence.

  Compaction:
  Call gobby-sessions:compact_self:

  - between completed coordination/bug tasks
  - at every handoff boundary
  - after daemon restart
  - when context is stale or large

  Before compacting, leave enough state in task notes or conversation to resume without rediscovery:

  - target epic ref
  - coordination epic ref
  - exact build command
  - build status
  - active runs
  - discovered bugs and fix commits
  - build journal path
  - escalations
  - validation run

  Completion criteria:
  Do not close the coordination epic while the target build is incomplete or discovered build bugs remain open.

  Completion requires:

  - target work merged/completed per its stages
  - no implementation leaf in the wrong stage
  - no stray running agents
  - no stray claimed tasks
  - all discovered daemon/build bugs fixed, committed, linked, and closed, or explicitly blocked on a user decision
  - build journal current and committed
  - required focused validation run complete
  - final status report covering build state, validation, bug fixes, escalations, and task states
