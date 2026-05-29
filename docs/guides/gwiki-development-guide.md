# gwiki Development Guide

`gobby-wiki` owns wiki files and derived wiki indexes. It treats Gobby daemon services as optional integrations. Runtime code must resolve the daemon base URL through `gobby_core::daemon_url::daemon_url()` or `daemon_url_at()` and must report unavailable optional services as structured degradation metadata.

## Daemon Capability Probe

`crates/gwiki/src/daemon.rs` defines the current probe contract. It returns a `DaemonCapabilityReport` with one availability record per capability plus a top-level `degraded` list. A 2xx response marks an endpoint available. `405 Method Not Allowed` and `422 Unprocessable Entity` also mark a route as present for mutating endpoints probed without a body. `404`, auth failures, unexpected statuses, and transport failures become `DaemonDegradation` entries with capability, endpoint, reason, status, message, and fallback.

## Verified Endpoint Contracts

The endpoint shapes below were verified from the daemon source under `src/gobby/servers/routes` and `src/gobby/servers/websocket`.

| Capability | Endpoint | Request Shape | Response Shape | Fallback |
|---|---|---|---|---|
| Embeddings maintenance | `POST /api/memories/embeddings/reindex` | Query `project_id?`; no JSON body. | Object from `memory_manager.reindex_embeddings`, including generated/total counts or error detail on failure. | Do not use this as arbitrary text embedding for gwiki. Disable daemon-backed embedding generation and keep lexical/wiki indexing paths available until a dedicated request-time embedding endpoint exists. |
| Synthesis provider discovery | `GET /api/providers/models` | No body. | `{ "providers": [ { "provider", "available", "models", "source", "startup_error", ... } ] }`. | Skip daemon-assisted synthesis and return source/manually-authored wiki content. |
| Synthesis stream | `WS /ws` message `chat_message` | JSON frame: `type: "chat_message"`, `conversation_id?`, `content?`, `content_blocks?`, `model?`, `provider?`, `project_id?`, `request_id?`, `reasoning_effort?`, `attachments?`, `tts_enabled?`. | Frames include `connection_established`, `session_info`, `chat_stream` chunks with `done`, `chat_thinking`, `tool_status`, and `chat_error`. Final `chat_stream` may include usage, context window, session ref, and SDK session id. | Degrade synthesis, keep source collection/indexing results, and do not assume a provider-native completion schema. |
| Vision attachment ingress | `POST /api/chat/attachments` | Multipart form: `file`, `draft_id?`, `project_id?`. | Attachment object with `id`, `project_id`, `filename`, `mime_type`, `size_bytes`, local storage metadata, and timestamps. | Store raw image assets and surface filename/metadata only. Visual extraction stays skipped. |
| Vision prompt path | `WS /ws` message `chat_message` | Use `content_blocks` and/or `attachments` with stored attachment IDs. | Same streaming frames as synthesis. The daemon does not expose a separate image-analysis REST endpoint. | Treat vision as unavailable when attachment upload or model support is absent. Never drop the raw asset. |
| Transcription status | `GET /api/voice/status?want_stt=true` | Query `want_stt?`, `want_tts?`. | Voice status object with `enabled`, `stt_enabled`, `stt_available`, `stt_reason`, warmup fields, `voice_ready`, and TTS fields. | Keep raw audio assets and require supplied transcripts. |
| Transcription request | `POST /api/voice/transcribe` | Multipart form: `file`. | `{ "text", "bytes", "content_type" }` on success or `{ "error", "text": "" }` when disabled/unavailable/failing. | Keep raw audio assets; mark transcript generation degraded. |
| Agent dispatch | `POST /api/agents/spawn` | JSON `AgentSpawnRequest`: `task_id`, `agent_name?`, `prompt?`, `web_chat?`, `isolation?`, `provider?`, `model?`, `reasoning_effort?`, `reasoning_required?`, `workflow?`, `branch_name?`, `base_branch?`, `timeout?`, `max_turns?`. | `AgentSpawnResponse`: `success`, optional `run_id`, `child_session_id`, `conversation_id`, `isolation`, `branch_name`, `pid`, `message`, `reasoning`, or `error`. | Return dispatch degradation metadata. `gwiki` must not spawn or manage internal subprocesses. |
| Build/lifecycle dispatch | `POST /api/build` | JSON `BuildRequest`: `input_ref`, `project_id?`, `cwd?`, `quick?`, `skip_stages?`, `isolation?`, `workspace_backend?`, `agent?`, `stage?`, `max_active_agents?`, `max_retries?`, and related build options. | Build result object containing lifecycle run state and dispatcher summary fields. | Use only as daemon integration for higher-level build automation; no local process fallback. |
| Session list and monitoring fallback | `GET /api/sessions` | Query filters such as `source?`, `project_id?`, `status?`, `limit?`, `offset?`. | Session listing object with session rows and count/pagination fields. | Disable live monitoring and rely on explicit command output. |
| Session messages | `GET /api/sessions/{session_id}/messages` | Query `limit?`, `offset?`, `role?`, `format=rendered|legacy`. | `{ "status": "success", "messages", "total_count", "response_time_ms", "format" }`. | Polling history is unavailable; surface no live session transcript. |
| Session/event stream | `WS /ws` | Client frames include `subscribe`, `unsubscribe`, `continue_in_chat`, `attach_to_session`, `detach_from_session`, and `send_to_cli_session`. | Broadcast frames include task/session/chat events plus request-correlated responses. Initial connection sends `connection_established`. | Fall back to REST polling where available; otherwise mark monitoring degraded. |

## Integration Rules

- Endpoint availability is a probe result, not an implementation permission. Mutating daemon routes must still be called only by the feature that owns the mutation.
- `POST /api/memories/embeddings/reindex` is memory maintenance. It is not a request-time embedding API for arbitrary wiki text.
- Image and audio ingestion must write raw assets before calling optional daemon services. Missing vision or transcription records degradation and preserves raw files.
- Agent dispatch belongs to the daemon: `gwiki` sends requests to `/api/agents/spawn` or `/api/build` and records daemon responses. It must not shell out to Codex, Claude, tmux, or subprocess runners directly.
