# Task 310 TDD Evidence

Task: #310 Add audio ingestion and transcription

## Red Recovery

The original development handoff omitted literal red output. Red was recovered in
an isolated temporary worktree at the parent commit of the implementation:

- Base commit: `37b99cb89981093c4af2d17a2aabca02ce0abc98`
- Implementation commit: `64c29d9dabf01eabdc7a7bdc107ecda98c5ad7b0`
- Temporary worktree: `/private/tmp/gobby-task-310-red.rw5esQ`
- Recovery method: add only the #310 acceptance tests and module wiring for
  `crates/gwiki/src/ingest/audio.rs` and `crates/gwiki/src/transcribe.rs`, with
  no audio/transcription implementation.

Exact red command:

```bash
cd /private/tmp/gobby-task-310-red.rw5esQ && CARGO_TARGET_DIR=/private/tmp/gobby-task-310-red-target cargo check -p gobby-wiki --no-default-features --tests
```

Result: failed with exit code `101`.

Output excerpt:

```text
error[E0432]: unresolved imports `crate::transcribe::TranscriptSegment`, `crate::transcribe::TranscriptionClient`, `crate::transcribe::TranscriptionOutput`, `crate::transcribe::TranscriptionRequest`
  --> crates/gwiki/src/ingest/audio.rs:10:9
   |
10 |         TranscriptSegment, TranscriptionClient, TranscriptionOutput, TranscriptionRequest,
   |         ^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^ no `TranscriptionRequest` in `transcribe`

error[E0425]: cannot find type `AudioSnapshot` in this scope
  --> crates/gwiki/src/ingest/audio.rs:15:29

error[E0425]: cannot find function `ingest_audio` in this scope
  --> crates/gwiki/src/ingest/audio.rs:51:22

error[E0425]: cannot find function `ingest_audio_with_transcription` in this scope
  --> crates/gwiki/src/ingest/audio.rs:77:22

error[E0425]: cannot find function `write_audio_transcript_markdown` in this scope
  --> crates/gwiki/src/transcribe.rs:64:22

error: could not compile `gobby-wiki` (lib test) due to 19 previous errors; 2 warnings emitted
```

The temp worktree was checked for `compile_error!`, `test_cfg_probe`, and
`red_probe` before this command; none were present.

## Green And Final Evidence

The implementation in `64c29d9dabf01eabdc7a7bdc107ecda98c5ad7b0` provides the
audio ingest and transcription API referenced by the failing tests. Fresh final
validation was rerun after this evidence artifact was added, using focused
`gobby-wiki` commands only.
