---
title: crates/gwiki/src/ingest/session
type: code_module
provenance:
- file: crates/gwiki/src/ingest/session/codex.rs
  ranges:
  - '12'
  - 15-20
  - 22-96
  - 100-105
  - 108-110
  - 113-117
  - 120-131
  - 133-156
  - 158-180
  - 182-204
  - 206-226
  - 228-242
  - 244-258
  - 260-274
  - 276-280
  - 282-303
  - 305-309
  - 311-316
  - 318-323
  - 325-330
  - 332-339
  - 352-471
  - 474-541
- file: crates/gwiki/src/ingest/session/derived.rs
  ranges:
  - 10-26
  - 28-52
  - 54-81
  - 83-105
- file: crates/gwiki/src/ingest/session/droid.rs
  ranges:
  - '12'
  - 15-17
  - 19-21
  - 23-77
  - 81-91
  - 94-97
  - 99-105
  - 107-114
  - 116-137
  - 139-148
  - 150-160
  - 162-166
  - 168-189
  - 191-202
  - 204-217
  - 219-223
  - 225-244
  - 246-277
  - 279-284
  - 286-297
  - 307-415
  - 418-432
  - 435-454
- file: crates/gwiki/src/ingest/session/gemini.rs
  ranges:
  - '12'
  - 15-20
  - 22-83
  - 87-102
  - 104-119
  - 121-147
  - 149-175
  - 177-192
  - 194-198
  - 200-221
  - 223-227
  - 229-234
  - 236-241
  - 251-333
  - 336-356
- file: crates/gwiki/src/ingest/session/grok.rs
  ranges:
  - '12'
  - 15-20
  - 22-32
  - 34-104
  - 108-118
  - 121-125
  - 127-139
  - 141-153
  - 155-188
  - 190-212
  - 214-232
  - 234-250
  - 252-256
  - 258-279
  - 281-285
  - 287-292
  - 294-299
  - 309-376
  - 379-408
  - 411-430
- file: crates/gwiki/src/ingest/session/metadata.rs
  ranges:
  - 10-15
  - 18-22
  - 24-28
  - 30-32
  - 34-36
  - 38-44
  - 47-87
  - 89-100
  - 102-106
  - 108-119
  - 121-132
  - 134-146
  - 148-152
- file: crates/gwiki/src/ingest/session/qwen.rs
  ranges:
  - '12'
  - 15-20
  - 22-24
  - 26-77
  - 81-89
  - 92-96
  - 98-104
  - 106-126
  - 128-145
  - 147-159
  - 161-169
  - 171-196
  - 198-211
  - 213-228
  - 230-236
  - 238-243
  - 245-247
  - 257-382
  - 385-407
  - 410-430
- file: crates/gwiki/src/ingest/session/redaction.rs
  ranges:
  - 5-7
  - 9-15
  - 17-23
  - 25-33
  - 35-41
  - 54-70
  - 73-126
  - 128-145
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/session/codex.rs:12](crates/gwiki/src/ingest/session/codex.rs#L12), [crates/gwiki/src/ingest/session/codex.rs:15-20](crates/gwiki/src/ingest/session/codex.rs#L15-L20), [crates/gwiki/src/ingest/session/codex.rs:22-96](crates/gwiki/src/ingest/session/codex.rs#L22-L96), [crates/gwiki/src/ingest/session/codex.rs:100-105](crates/gwiki/src/ingest/session/codex.rs#L100-L105), [crates/gwiki/src/ingest/session/codex.rs:108-110](crates/gwiki/src/ingest/session/codex.rs#L108-L110), [crates/gwiki/src/ingest/session/codex.rs:113-117](crates/gwiki/src/ingest/session/codex.rs#L113-L117), [crates/gwiki/src/ingest/session/codex.rs:120-131](crates/gwiki/src/ingest/session/codex.rs#L120-L131), [crates/gwiki/src/ingest/session/codex.rs:133-156](crates/gwiki/src/ingest/session/codex.rs#L133-L156), [crates/gwiki/src/ingest/session/codex.rs:158-180](crates/gwiki/src/ingest/session/codex.rs#L158-L180), [crates/gwiki/src/ingest/session/codex.rs:182-204](crates/gwiki/src/ingest/session/codex.rs#L182-L204), [crates/gwiki/src/ingest/session/codex.rs:206-226](crates/gwiki/src/ingest/session/codex.rs#L206-L226), [crates/gwiki/src/ingest/session/codex.rs:228-242](crates/gwiki/src/ingest/session/codex.rs#L228-L242), [crates/gwiki/src/ingest/session/codex.rs:244-258](crates/gwiki/src/ingest/session/codex.rs#L244-L258), [crates/gwiki/src/ingest/session/codex.rs:260-274](crates/gwiki/src/ingest/session/codex.rs#L260-L274), [crates/gwiki/src/ingest/session/codex.rs:276-280](crates/gwiki/src/ingest/session/codex.rs#L276-L280), [crates/gwiki/src/ingest/session/codex.rs:282-303](crates/gwiki/src/ingest/session/codex.rs#L282-L303), [crates/gwiki/src/ingest/session/codex.rs:305-309](crates/gwiki/src/ingest/session/codex.rs#L305-L309), [crates/gwiki/src/ingest/session/codex.rs:311-316](crates/gwiki/src/ingest/session/codex.rs#L311-L316), [crates/gwiki/src/ingest/session/codex.rs:318-323](crates/gwiki/src/ingest/session/codex.rs#L318-L323), [crates/gwiki/src/ingest/session/codex.rs:325-330](crates/gwiki/src/ingest/session/codex.rs#L325-L330), [crates/gwiki/src/ingest/session/codex.rs:332-339](crates/gwiki/src/ingest/session/codex.rs#L332-L339), [crates/gwiki/src/ingest/session/codex.rs:352-471](crates/gwiki/src/ingest/session/codex.rs#L352-L471), [crates/gwiki/src/ingest/session/codex.rs:474-541](crates/gwiki/src/ingest/session/codex.rs#L474-L541)
- [crates/gwiki/src/ingest/session/derived.rs:10-26](crates/gwiki/src/ingest/session/derived.rs#L10-L26), [crates/gwiki/src/ingest/session/derived.rs:28-52](crates/gwiki/src/ingest/session/derived.rs#L28-L52), [crates/gwiki/src/ingest/session/derived.rs:54-81](crates/gwiki/src/ingest/session/derived.rs#L54-L81), [crates/gwiki/src/ingest/session/derived.rs:83-105](crates/gwiki/src/ingest/session/derived.rs#L83-L105)
- [crates/gwiki/src/ingest/session/droid.rs:12](crates/gwiki/src/ingest/session/droid.rs#L12), [crates/gwiki/src/ingest/session/droid.rs:15-17](crates/gwiki/src/ingest/session/droid.rs#L15-L17), [crates/gwiki/src/ingest/session/droid.rs:19-21](crates/gwiki/src/ingest/session/droid.rs#L19-L21), [crates/gwiki/src/ingest/session/droid.rs:23-77](crates/gwiki/src/ingest/session/droid.rs#L23-L77), [crates/gwiki/src/ingest/session/droid.rs:81-91](crates/gwiki/src/ingest/session/droid.rs#L81-L91), [crates/gwiki/src/ingest/session/droid.rs:94-97](crates/gwiki/src/ingest/session/droid.rs#L94-L97), [crates/gwiki/src/ingest/session/droid.rs:99-105](crates/gwiki/src/ingest/session/droid.rs#L99-L105), [crates/gwiki/src/ingest/session/droid.rs:107-114](crates/gwiki/src/ingest/session/droid.rs#L107-L114), [crates/gwiki/src/ingest/session/droid.rs:116-137](crates/gwiki/src/ingest/session/droid.rs#L116-L137), [crates/gwiki/src/ingest/session/droid.rs:139-148](crates/gwiki/src/ingest/session/droid.rs#L139-L148), [crates/gwiki/src/ingest/session/droid.rs:150-160](crates/gwiki/src/ingest/session/droid.rs#L150-L160), [crates/gwiki/src/ingest/session/droid.rs:162-166](crates/gwiki/src/ingest/session/droid.rs#L162-L166), [crates/gwiki/src/ingest/session/droid.rs:168-189](crates/gwiki/src/ingest/session/droid.rs#L168-L189), [crates/gwiki/src/ingest/session/droid.rs:191-202](crates/gwiki/src/ingest/session/droid.rs#L191-L202), [crates/gwiki/src/ingest/session/droid.rs:204-217](crates/gwiki/src/ingest/session/droid.rs#L204-L217), [crates/gwiki/src/ingest/session/droid.rs:219-223](crates/gwiki/src/ingest/session/droid.rs#L219-L223), [crates/gwiki/src/ingest/session/droid.rs:225-244](crates/gwiki/src/ingest/session/droid.rs#L225-L244), [crates/gwiki/src/ingest/session/droid.rs:246-277](crates/gwiki/src/ingest/session/droid.rs#L246-L277), [crates/gwiki/src/ingest/session/droid.rs:279-284](crates/gwiki/src/ingest/session/droid.rs#L279-L284), [crates/gwiki/src/ingest/session/droid.rs:286-297](crates/gwiki/src/ingest/session/droid.rs#L286-L297), [crates/gwiki/src/ingest/session/droid.rs:307-415](crates/gwiki/src/ingest/session/droid.rs#L307-L415), [crates/gwiki/src/ingest/session/droid.rs:418-432](crates/gwiki/src/ingest/session/droid.rs#L418-L432), [crates/gwiki/src/ingest/session/droid.rs:435-454](crates/gwiki/src/ingest/session/droid.rs#L435-L454)
- [crates/gwiki/src/ingest/session/gemini.rs:12](crates/gwiki/src/ingest/session/gemini.rs#L12), [crates/gwiki/src/ingest/session/gemini.rs:15-20](crates/gwiki/src/ingest/session/gemini.rs#L15-L20), [crates/gwiki/src/ingest/session/gemini.rs:22-83](crates/gwiki/src/ingest/session/gemini.rs#L22-L83), [crates/gwiki/src/ingest/session/gemini.rs:87-102](crates/gwiki/src/ingest/session/gemini.rs#L87-L102), [crates/gwiki/src/ingest/session/gemini.rs:104-119](crates/gwiki/src/ingest/session/gemini.rs#L104-L119), [crates/gwiki/src/ingest/session/gemini.rs:121-147](crates/gwiki/src/ingest/session/gemini.rs#L121-L147), [crates/gwiki/src/ingest/session/gemini.rs:149-175](crates/gwiki/src/ingest/session/gemini.rs#L149-L175), [crates/gwiki/src/ingest/session/gemini.rs:177-192](crates/gwiki/src/ingest/session/gemini.rs#L177-L192), [crates/gwiki/src/ingest/session/gemini.rs:194-198](crates/gwiki/src/ingest/session/gemini.rs#L194-L198), [crates/gwiki/src/ingest/session/gemini.rs:200-221](crates/gwiki/src/ingest/session/gemini.rs#L200-L221), [crates/gwiki/src/ingest/session/gemini.rs:223-227](crates/gwiki/src/ingest/session/gemini.rs#L223-L227), [crates/gwiki/src/ingest/session/gemini.rs:229-234](crates/gwiki/src/ingest/session/gemini.rs#L229-L234), [crates/gwiki/src/ingest/session/gemini.rs:236-241](crates/gwiki/src/ingest/session/gemini.rs#L236-L241), [crates/gwiki/src/ingest/session/gemini.rs:251-333](crates/gwiki/src/ingest/session/gemini.rs#L251-L333), [crates/gwiki/src/ingest/session/gemini.rs:336-356](crates/gwiki/src/ingest/session/gemini.rs#L336-L356)
- [crates/gwiki/src/ingest/session/grok.rs:12](crates/gwiki/src/ingest/session/grok.rs#L12), [crates/gwiki/src/ingest/session/grok.rs:15-20](crates/gwiki/src/ingest/session/grok.rs#L15-L20), [crates/gwiki/src/ingest/session/grok.rs:22-32](crates/gwiki/src/ingest/session/grok.rs#L22-L32), [crates/gwiki/src/ingest/session/grok.rs:34-104](crates/gwiki/src/ingest/session/grok.rs#L34-L104), [crates/gwiki/src/ingest/session/grok.rs:108-118](crates/gwiki/src/ingest/session/grok.rs#L108-L118), [crates/gwiki/src/ingest/session/grok.rs:121-125](crates/gwiki/src/ingest/session/grok.rs#L121-L125), [crates/gwiki/src/ingest/session/grok.rs:127-139](crates/gwiki/src/ingest/session/grok.rs#L127-L139), [crates/gwiki/src/ingest/session/grok.rs:141-153](crates/gwiki/src/ingest/session/grok.rs#L141-L153), [crates/gwiki/src/ingest/session/grok.rs:155-188](crates/gwiki/src/ingest/session/grok.rs#L155-L188), [crates/gwiki/src/ingest/session/grok.rs:190-212](crates/gwiki/src/ingest/session/grok.rs#L190-L212), [crates/gwiki/src/ingest/session/grok.rs:214-232](crates/gwiki/src/ingest/session/grok.rs#L214-L232), [crates/gwiki/src/ingest/session/grok.rs:234-250](crates/gwiki/src/ingest/session/grok.rs#L234-L250), [crates/gwiki/src/ingest/session/grok.rs:252-256](crates/gwiki/src/ingest/session/grok.rs#L252-L256), [crates/gwiki/src/ingest/session/grok.rs:258-279](crates/gwiki/src/ingest/session/grok.rs#L258-L279), [crates/gwiki/src/ingest/session/grok.rs:281-285](crates/gwiki/src/ingest/session/grok.rs#L281-L285), [crates/gwiki/src/ingest/session/grok.rs:287-292](crates/gwiki/src/ingest/session/grok.rs#L287-L292), [crates/gwiki/src/ingest/session/grok.rs:294-299](crates/gwiki/src/ingest/session/grok.rs#L294-L299), [crates/gwiki/src/ingest/session/grok.rs:309-376](crates/gwiki/src/ingest/session/grok.rs#L309-L376), [crates/gwiki/src/ingest/session/grok.rs:379-408](crates/gwiki/src/ingest/session/grok.rs#L379-L408), [crates/gwiki/src/ingest/session/grok.rs:411-430](crates/gwiki/src/ingest/session/grok.rs#L411-L430)
- [crates/gwiki/src/ingest/session/metadata.rs:10-15](crates/gwiki/src/ingest/session/metadata.rs#L10-L15), [crates/gwiki/src/ingest/session/metadata.rs:18-22](crates/gwiki/src/ingest/session/metadata.rs#L18-L22), [crates/gwiki/src/ingest/session/metadata.rs:24-28](crates/gwiki/src/ingest/session/metadata.rs#L24-L28), [crates/gwiki/src/ingest/session/metadata.rs:30-32](crates/gwiki/src/ingest/session/metadata.rs#L30-L32), [crates/gwiki/src/ingest/session/metadata.rs:34-36](crates/gwiki/src/ingest/session/metadata.rs#L34-L36), [crates/gwiki/src/ingest/session/metadata.rs:38-44](crates/gwiki/src/ingest/session/metadata.rs#L38-L44), [crates/gwiki/src/ingest/session/metadata.rs:47-87](crates/gwiki/src/ingest/session/metadata.rs#L47-L87), [crates/gwiki/src/ingest/session/metadata.rs:89-100](crates/gwiki/src/ingest/session/metadata.rs#L89-L100), [crates/gwiki/src/ingest/session/metadata.rs:102-106](crates/gwiki/src/ingest/session/metadata.rs#L102-L106), [crates/gwiki/src/ingest/session/metadata.rs:108-119](crates/gwiki/src/ingest/session/metadata.rs#L108-L119), [crates/gwiki/src/ingest/session/metadata.rs:121-132](crates/gwiki/src/ingest/session/metadata.rs#L121-L132), [crates/gwiki/src/ingest/session/metadata.rs:134-146](crates/gwiki/src/ingest/session/metadata.rs#L134-L146), [crates/gwiki/src/ingest/session/metadata.rs:148-152](crates/gwiki/src/ingest/session/metadata.rs#L148-L152)
- [crates/gwiki/src/ingest/session/qwen.rs:12](crates/gwiki/src/ingest/session/qwen.rs#L12), [crates/gwiki/src/ingest/session/qwen.rs:15-20](crates/gwiki/src/ingest/session/qwen.rs#L15-L20), [crates/gwiki/src/ingest/session/qwen.rs:22-24](crates/gwiki/src/ingest/session/qwen.rs#L22-L24), [crates/gwiki/src/ingest/session/qwen.rs:26-77](crates/gwiki/src/ingest/session/qwen.rs#L26-L77), [crates/gwiki/src/ingest/session/qwen.rs:81-89](crates/gwiki/src/ingest/session/qwen.rs#L81-L89), [crates/gwiki/src/ingest/session/qwen.rs:92-96](crates/gwiki/src/ingest/session/qwen.rs#L92-L96), [crates/gwiki/src/ingest/session/qwen.rs:98-104](crates/gwiki/src/ingest/session/qwen.rs#L98-L104), [crates/gwiki/src/ingest/session/qwen.rs:106-126](crates/gwiki/src/ingest/session/qwen.rs#L106-L126), [crates/gwiki/src/ingest/session/qwen.rs:128-145](crates/gwiki/src/ingest/session/qwen.rs#L128-L145), [crates/gwiki/src/ingest/session/qwen.rs:147-159](crates/gwiki/src/ingest/session/qwen.rs#L147-L159), [crates/gwiki/src/ingest/session/qwen.rs:161-169](crates/gwiki/src/ingest/session/qwen.rs#L161-L169), [crates/gwiki/src/ingest/session/qwen.rs:171-196](crates/gwiki/src/ingest/session/qwen.rs#L171-L196), [crates/gwiki/src/ingest/session/qwen.rs:198-211](crates/gwiki/src/ingest/session/qwen.rs#L198-L211), [crates/gwiki/src/ingest/session/qwen.rs:213-228](crates/gwiki/src/ingest/session/qwen.rs#L213-L228), [crates/gwiki/src/ingest/session/qwen.rs:230-236](crates/gwiki/src/ingest/session/qwen.rs#L230-L236), [crates/gwiki/src/ingest/session/qwen.rs:238-243](crates/gwiki/src/ingest/session/qwen.rs#L238-L243), [crates/gwiki/src/ingest/session/qwen.rs:245-247](crates/gwiki/src/ingest/session/qwen.rs#L245-L247), [crates/gwiki/src/ingest/session/qwen.rs:257-382](crates/gwiki/src/ingest/session/qwen.rs#L257-L382), [crates/gwiki/src/ingest/session/qwen.rs:385-407](crates/gwiki/src/ingest/session/qwen.rs#L385-L407), [crates/gwiki/src/ingest/session/qwen.rs:410-430](crates/gwiki/src/ingest/session/qwen.rs#L410-L430)
- [crates/gwiki/src/ingest/session/redaction.rs:5-7](crates/gwiki/src/ingest/session/redaction.rs#L5-L7), [crates/gwiki/src/ingest/session/redaction.rs:9-15](crates/gwiki/src/ingest/session/redaction.rs#L9-L15), [crates/gwiki/src/ingest/session/redaction.rs:17-23](crates/gwiki/src/ingest/session/redaction.rs#L17-L23), [crates/gwiki/src/ingest/session/redaction.rs:25-33](crates/gwiki/src/ingest/session/redaction.rs#L25-L33), [crates/gwiki/src/ingest/session/redaction.rs:35-41](crates/gwiki/src/ingest/session/redaction.rs#L35-L41), [crates/gwiki/src/ingest/session/redaction.rs:54-70](crates/gwiki/src/ingest/session/redaction.rs#L54-L70), [crates/gwiki/src/ingest/session/redaction.rs:73-126](crates/gwiki/src/ingest/session/redaction.rs#L73-L126), [crates/gwiki/src/ingest/session/redaction.rs:128-145](crates/gwiki/src/ingest/session/redaction.rs#L128-L145)

</details>

# crates/gwiki/src/ingest/session

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

The crates/gwiki/src/ingest/session module manages the ingestion, parsing, and structured normalization of raw session archives from multiple platforms into a unified session format. By providing a common trait-driven framework, the module delegates the interpretation of platform-specific archives to specialized implementations such as CodexSessionAdapter [crates/gwiki/src/ingest/session/codex.rs:12], DroidSessionAdapter , GrokSessionAdapter [crates/gwiki/src/ingest/session/grok.rs:12], QwenSessionAdapter [crates/gwiki/src/ingest/session/qwen.rs:12], and a Gemini transcript adapter [crates/gwiki/src/ingest/session/gemini.rs:12]. These adapters match and filter valid envelopes, assemble message timelines, reconstruct tool invocations, and normalize roles [crates/gwiki/src/ingest/session/codex.rs:15-20, crates/gwiki/src/ingest/session/grok.rs:15-20, crates/gwiki/src/ingest/session/qwen.rs:15-20].

During the ingestion pipeline, session-level metadata—including model names, git branch records, and token counters—is accumulated within the ParsedSessionMetadata struct [crates/gwiki/src/ingest/session/metadata.rs:10-15]. To prevent security leaks, the module routes parsed text through redact_session_markdown, which uses high-performance regex replacement rules compiled via OnceLock to scrub home directories, API keys, and email addresses [crates/gwiki/src/ingest/session/redaction.rs:9-15, crates/gwiki/src/ingest/session/redaction.rs:17-23]. Finally, write_session_derived_markdown performs an atomic, crash-resilient write to persist the sanitized output safely into the wiki vault directories [crates/gwiki/src/ingest/session/derived.rs:10-26, crates/gwiki/src/ingest/session/derived.rs:54-81].

| Symbol / Adapter Type | Target / Purpose | Supporting Spans |
| --- | --- | --- |
| CodexSessionAdapter | Parser for Codex session events (event_msg, response_item, session_meta, turn_context). | crates/gwiki/src/ingest/session/codex.rs:12 |
| DroidSessionAdapter | Parser for Droid records, recognizing Droid-specific message and session_start envelopes. | crates/gwiki/src/ingest/session/droid.rs:11 |
| GrokSessionAdapter | Parser for Grok archives, deserializing GrokRecords and handling streaming text and tools. | crates/gwiki/src/ingest/session/grok.rs:12 |
| QwenSessionAdapter | Parser for Qwen archives, extracting visible chat payloads while filtering thought content. | crates/gwiki/src/ingest/session/qwen.rs:12 |
| ParsedSessionMetadata | Small accumulator tracking model metadata, git branch, tool counts, and token totals. | crates/gwiki/src/ingest/session/metadata.rs:10-15 |
| redact_session_markdown | Entrypoint for applying cached, regex-based security scrubbing rules to session markdown. | crates/gwiki/src/ingest/session/redaction.rs:9-15 |
| write_session_derived_markdown | Computes target paths and writes normalized session records atomically to the vault. | crates/gwiki/src/ingest/session/derived.rs:10-26 |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/session/codex.rs\|crates/gwiki/src/ingest/session/codex.rs]] | This file defines `CodexSessionAdapter`, an implementation of `SessionTranscriptAdapter` that recognizes Codex archive envelope types and converts them into a normalized `ParsedSession`. Its `parse` logic walks supported envelopes, extracts session metadata such as start time, model, branch, and session type, and dispatches Codex-specific payloads through helper parsers for event messages, response items, function calls/outputs, and tool-search calls/outputs. The rendering helpers format content and JSON-ish values into text blocks, and the tests cover parsing both synthetic message/tool-item cases and a real archive fixture when enabled. [crates/gwiki/src/ingest/session/codex.rs:12] [crates/gwiki/src/ingest/session/codex.rs:15-20] [crates/gwiki/src/ingest/session/codex.rs:22-96] [crates/gwiki/src/ingest/session/codex.rs:100-105] [crates/gwiki/src/ingest/session/codex.rs:108-110] |
| [[code/files/crates/gwiki/src/ingest/session/derived.rs\|crates/gwiki/src/ingest/session/derived.rs]] | Writes derived session markdown files into a vault safely and atomically. `write_session_derived_markdown` computes the record’s derived markdown path, creates any missing parent directories under the vault root, and delegates to the atomic writer, returning the relative path on success. The lower-level helpers build a temporary file in the target directory, write and `sync` the contents, persist it over the destination, and then sync the parent directory so the on-disk update is durable. [crates/gwiki/src/ingest/session/derived.rs:10-26] [crates/gwiki/src/ingest/session/derived.rs:28-52] [crates/gwiki/src/ingest/session/derived.rs:54-81] [crates/gwiki/src/ingest/session/derived.rs:83-105] |
| [[code/files/crates/gwiki/src/ingest/session/droid.rs\|crates/gwiki/src/ingest/session/droid.rs]] | This file implements the Droid session transcript adapter for ingesting archived session data into a normalized `ParsedSession`. `DroidSessionAdapter` declares support for `message` and `session_start` envelopes, detects Droid archives by looking for a session start record, then parses envelopes into session metadata and ordered messages while rejecting archives that do not contain usable message content. The helper functions break that work into small steps: identifying Droid record types, recognizing session-start and hidden-context records, extracting message roles, rendering content and tool use/result payloads, collecting tool names, and deciding when JSON-like content should be emitted as pretty JSON versus plain text. The tests cover persisted records, envelope-wrapped payloads, and real fixture archives to confirm the adapter handles both session metadata and tool interactions correctly. [crates/gwiki/src/ingest/session/droid.rs:12] [crates/gwiki/src/ingest/session/droid.rs:15-17] [crates/gwiki/src/ingest/session/droid.rs:19-21] [crates/gwiki/src/ingest/session/droid.rs:23-77] [crates/gwiki/src/ingest/session/droid.rs:81-91] |
| [[code/files/crates/gwiki/src/ingest/session/gemini.rs\|crates/gwiki/src/ingest/session/gemini.rs]] | Defines a `SessionTranscriptAdapter` for Gemini session archives that recognizes Gemini envelope types, parses each `SessionArchiveEnvelope` into `GeminiRecord`s, and builds a `ParsedSession` by tracking start time, model metadata, and message sequence. The helper functions split the parsing/rendering work across message, tool call, and tool result cases, handle content assembly and call IDs, and support delta appends for streamed content. The file also includes tests for parsing streamed JSON messages/tools and for a real-stream fixture path. [crates/gwiki/src/ingest/session/gemini.rs:12] [crates/gwiki/src/ingest/session/gemini.rs:15-20] [crates/gwiki/src/ingest/session/gemini.rs:22-83] [crates/gwiki/src/ingest/session/gemini.rs:87-102] [crates/gwiki/src/ingest/session/gemini.rs:104-119] |
| [[code/files/crates/gwiki/src/ingest/session/grok.rs\|crates/gwiki/src/ingest/session/grok.rs]] | Implements a `SessionTranscriptAdapter` for Grok archives, turning Grok session envelopes into a `ParsedSession` with metadata, timestamps, and normalized messages. `GrokSessionAdapter` first decides whether an envelope type or archive looks like Grok, then `parse` deserializes each supported record into `GrokRecord`/`GrokToolCall` and dispatches to helpers that build chat messages, streaming text chunks, tool calls and results, errors, and content rendering, merging adjacent message parts when needed. The file also includes tests covering local chat history, streaming JSON text chunks, and a real archive fixture path. [crates/gwiki/src/ingest/session/grok.rs:12] [crates/gwiki/src/ingest/session/grok.rs:15-20] [crates/gwiki/src/ingest/session/grok.rs:22-32] [crates/gwiki/src/ingest/session/grok.rs:34-104] [crates/gwiki/src/ingest/session/grok.rs:108-118] |
| [[code/files/crates/gwiki/src/ingest/session/metadata.rs\|crates/gwiki/src/ingest/session/metadata.rs]] | Defines `ParsedSessionMetadata`, a small accumulator for ingesting session-level metadata like model, git branch, token totals, and subagent status, with setters that only fill fields once and helpers that merge token usage data. It also builds the exported metadata field list for a `ParsedSession` by conditionally emitting model, tool counts, token totals, duration, hour buckets, subagent flag, and git branch, using shared utilities to coerce JSON number fields, compute counts and time-based summaries, and parse timestamps. [crates/gwiki/src/ingest/session/metadata.rs:10-15] [crates/gwiki/src/ingest/session/metadata.rs:18-22] [crates/gwiki/src/ingest/session/metadata.rs:24-28] [crates/gwiki/src/ingest/session/metadata.rs:30-32] [crates/gwiki/src/ingest/session/metadata.rs:34-36] |
| [[code/files/crates/gwiki/src/ingest/session/qwen.rs\|crates/gwiki/src/ingest/session/qwen.rs]] | Implements the Qwen session transcript adapter for ingesting archived chat payloads into the wiki’s parsed session format. `QwenSessionAdapter` पहचान/filters supported envelopes and archives, parses each Qwen record into session metadata and visible messages, and uses helper functions and data models to normalize record types, roles, tool calls/responses, and rendered parts while skipping non-visible thought content; the tests verify wrapped payloads, tool/message handling, and real archive parsing. [crates/gwiki/src/ingest/session/qwen.rs:12] [crates/gwiki/src/ingest/session/qwen.rs:15-20] [crates/gwiki/src/ingest/session/qwen.rs:22-24] [crates/gwiki/src/ingest/session/qwen.rs:26-77] [crates/gwiki/src/ingest/session/qwen.rs:81-89] |
| [[code/files/crates/gwiki/src/ingest/session/redaction.rs\|crates/gwiki/src/ingest/session/redaction.rs]] | This file defines the session redaction layer used during ingest: `redact_session_markdown` delegates to `redact_session_text`, which applies a sequence of regex-based replacements to scrub home-directory paths, common API key/token formats, and email addresses with fixed `[REDACTED_*]` markers. The regex builders are cached with `OnceLock` so the patterns are compiled once and reused. The test module exercises the redaction rules and verifies that session ingest writes redacted markdown into the indexed store rather than leaking secrets. [crates/gwiki/src/ingest/session/redaction.rs:5-7] [crates/gwiki/src/ingest/session/redaction.rs:9-15] [crates/gwiki/src/ingest/session/redaction.rs:17-23] [crates/gwiki/src/ingest/session/redaction.rs:25-33] [crates/gwiki/src/ingest/session/redaction.rs:35-41] |

## Components

| Component ID |
| --- |
| `15267d70-ca9b-5ff1-99b3-78619085b140` |
| `893b9cf9-0451-5249-a4fc-2707cdf6d4b5` |
| `a273032b-c75f-527c-81f2-0c4bc7035c34` |
| `d81b7fc0-a29e-5ef0-97bd-739906ac9aa9` |
| `63bcf4e5-71fe-5bfc-8da7-bddab2fa3a11` |
| `04dd0d53-f2d6-5b8a-b34b-e0d3b5e5b3b5` |
| `3a3d1367-2011-596b-9f21-1f8518181150` |
| `ee11657a-dbc9-5ac9-bbc9-968f6aad4d07` |
| `17b87d33-9141-5cf7-8fa9-2c18da3c0ea2` |
| `11de5e8a-050f-5853-a051-c886610a1e1c` |
| `e3427821-de25-57e6-b9d5-89c7e84d97d1` |
| `940fb53d-f326-57a9-8110-f88971092b8d` |
| `adf9c99c-c2dc-5382-80ca-0d88110be284` |
| `877faf57-d9a3-579a-938c-bcd9f4aaf72f` |
| `8519de77-8278-5306-be4a-f998dbbc1985` |
| `46402732-b1de-5b33-bd48-5c3972b36b35` |
| `e288533e-f1e7-53c1-b569-16fcd384cab6` |
| `3ba443d6-6091-5952-96b3-723bd726b56d` |
| `2960b4c5-d8cb-579d-a0d5-3c1e3a8e8777` |
| `00ca871e-5da9-5290-b8ea-0ab82ad3616d` |
| `699a26e8-d40d-58c5-9447-0fcc88a1d706` |
| `427bc068-717b-5226-9eed-da1dc20e147f` |
| `3d667516-0cbc-5f9c-9846-71689c5f099d` |
| `82b642e1-4d58-5219-8a89-17488dd8dec4` |
| `3338d0be-7796-5e7a-9fa4-00839f887ac7` |
| `032602f1-ad47-5140-8bd2-cd0feb01b5ed` |
| `5898354c-8cb0-54fe-be64-8431c3445df4` |
| `d1d653d4-549d-5d60-95e5-436601680da4` |
| `00f7d870-7dd9-55b0-b637-e1ccdc6baed5` |
| `260f3293-c8b7-5f7d-995a-e6a99718c2aa` |
| `601197eb-5801-588e-a6ba-1253bb1a8ec4` |
| `2433a147-4015-5a42-acc2-8659bbe07199` |
| `e932bd63-afc2-5937-81f4-5f17135e0eb7` |
| `01892012-c4ed-585c-adc5-180f9b12f90b` |
| `f435dd21-d587-5e3d-b3da-3b91f58d4211` |
| `7bd45590-a4ad-518e-a889-e1bb50a10709` |
| `bfb3f3d4-4fba-5fc8-ae22-ab1d81f1ad9e` |
| `d0a65821-1d91-53d2-bdf9-d95972c5e395` |
| `7a73119c-3fbd-5dbc-86a4-303b545c25f4` |
| `552f7a15-2cfa-55bd-87ab-1d6b1968f7f6` |
| `e31d540a-e753-55af-a17e-5221a9bf721d` |
| `1dc704b4-a8d7-5c93-8314-3edc3903d7da` |
| `7fb499f6-4444-596d-b51a-42a60d23e803` |
| `ad2f1d01-1567-5400-84c6-ad7885143905` |
| `da96d7a6-f0dc-5bb8-8f2f-3f3ab591d6e2` |
| `a6db41df-1270-5d2b-8bc1-3d92fc6a2fd5` |
| `bac00586-3208-549a-bf4d-8b6a68886acc` |
| `41a61251-5b52-50b5-889d-854c192526e9` |
| `36f9a2b1-d3d7-57a5-8f99-32123854451c` |
| `c99abb33-c55a-5f49-9c0a-fa3d1aba2b8a` |
| `60e3e444-06e9-5846-9fab-87c8cd3be1f4` |
| `cfc52f54-c2b2-5f2d-9fea-a65d70d5a017` |
| `d0474e50-1632-5ea5-be4e-ff6f2139415c` |
| `9fb32d49-8ab2-57a8-b047-80e238f0f643` |
| `95493f75-b853-5753-bc28-c4230a65c4c6` |
| `0bb9488c-ff2b-5972-bf65-4756955170c4` |
| `18530d67-6c0b-5c34-b897-01c9dd8dd55a` |
| `8d42e440-bc1b-5d40-a57d-e2b8467fe5ef` |
| `a9a5237d-80c0-531d-9d27-64190bb73b1c` |
| `b3664055-76a2-50cf-b260-78ed85f2db02` |
| `8da72047-c2d5-5068-bf73-1fa0e93fc5dc` |
| `1ca79743-b53f-5269-9508-76688f12ab20` |
| `dc84d688-a6d4-5b7e-a7b3-7e85f13dac71` |
| `7d505ed5-1dd5-5ba6-ab35-75aa828fd841` |
| `642a7df7-4916-5df9-a4bc-078ff1ca8f26` |
| `724b03e2-ae94-5977-9f2a-e9b3d50529fc` |
| `58ff2c03-d108-580f-896d-48445a1037fb` |
| `431f1442-e4fd-5de7-b025-dcba678c4d8b` |
| `86cd130b-5c1b-5c01-bc71-5fe8f8b24cec` |
| `4abc683e-a4ed-5a41-8d97-630feef26e0c` |
| `f958a1e5-2344-52b0-b553-8f546fbb1032` |
| `04ad594c-49ca-517a-a50f-5da744ed3985` |
| `c952fe21-a159-5da1-85da-bb6f89a70867` |
| `06a2334d-2b93-5559-9845-2762ec64f38b` |
| `ff99685e-51c0-535c-a145-76968a52c1d9` |
| `cc11ff77-8a51-5972-8154-20080cc11104` |
| `118444db-6f7a-562a-89a4-2dd7cb585a42` |
| `48cf894e-351a-5151-a9fe-2b7832227d51` |
| `4c7c414b-756c-5185-ba61-077a1eee9cc5` |
| `462d0105-beb6-53e0-b0ec-c401258959a9` |
| `6f81fd48-8446-5c8c-b035-8893d9f877e7` |
| `1ca4fb54-43ef-5c18-a6bd-9216cf05f539` |
| `8ebc6c0e-f6cd-5ece-81a4-3f109dda7274` |
| `bc408ed0-bbfa-5aea-bd97-c146a952cb55` |
| `82053cf0-1566-53e0-86f9-2c2bdb24b368` |
| `3650e669-80be-5f64-b69b-a26c4e1c70f9` |
| `55d1f20a-9adf-5f1d-b109-110b0e8bc038` |
| `09880663-c897-5aef-a7e8-ff19422c3ebb` |
| `b90eed6b-5e22-5157-97db-0c8f43a2df1c` |
| `5b01053e-60c1-5588-9245-683ecb6aa95d` |
| `6659d1c9-e9eb-5964-a0c8-a199789b6f39` |
| `338d6874-d9fb-55d2-a939-41df90807614` |
| `9d0484bb-c033-572f-bd67-8df2c434d56f` |
| `6d6d7c3c-c1b2-518a-b534-15a6d5aede66` |
| `126d18c4-fe24-5546-b3da-829617f7a295` |
| `121b9252-1e46-5624-96c6-d2c1c45d9a64` |
| `e2e25698-28cc-5e61-be8c-cfa440f60bb3` |
| `d6a11f1a-6893-5bcc-8c13-a94dcf6a24c0` |
| `eee4b49d-4b4d-5ca1-9e41-366740fd40f5` |
| `b2c51b10-415a-5e11-bde5-2e4c614df85b` |
| `63a00279-9589-56a3-b895-8839949cb38b` |
| `ad509413-7c8a-5cda-a519-a960e1f6a80b` |
| `32f15781-c79e-5991-ae9a-3fafc5d8b993` |
| `a01392ab-8445-5f80-b751-8a71e89c3f7f` |
| `0fc01ea2-2c00-5d28-aa42-de340b4ab468` |
| `f9afaeef-d0fd-578c-9900-a429bc1266f1` |
| `853a2bf5-c5be-5094-be42-d6f0e8bca17f` |
| `afe56666-cbc5-5f26-8e0b-b203571e287b` |
| `0c628b48-4adf-5d09-99a3-f34bbd62874e` |
| `efd17c82-2b54-55af-a421-a2904d162756` |
| `4d95167e-1794-5555-a256-ba821d59a5b0` |
| `212112ec-025c-56bf-a5ba-041347a6564b` |
| `584feb0e-2147-5167-8ed3-3268597d288f` |
| `b6548d52-a57d-583d-aeac-f7dbdd1953d7` |
| `79b9b42f-3f66-52c2-a78d-db135e5026fa` |
| `07c99793-ff85-5c3b-9382-2cec4a8db490` |
| `b5ab2227-52c0-5694-bdc2-706459e63840` |
| `6c625a5c-b044-5a7a-af33-9cf940bc5cad` |
| `394dfb04-8d1f-5615-871f-a670ef543c1e` |
| `d0a0b9ae-8113-5625-b364-791d2e421ce6` |
| `7867d44e-677e-5f25-824e-e626f4b5f289` |
| `1f34dc1a-b296-5a99-b234-ba6903f78385` |
| `c9e82f14-9f8c-5b87-8889-a2c191839280` |
| `2d95fecf-b063-57e7-9d33-dedf787219be` |
| `b0ba8499-9fc7-5d39-a509-680e4d2302fa` |
| `2d3b8498-a78f-5011-9a3a-3ad10a8e50ac` |
