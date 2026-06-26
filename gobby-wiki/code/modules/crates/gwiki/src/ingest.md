---
title: crates/gwiki/src/ingest
type: code_module
provenance:
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/document/html.rs
- file: crates/gwiki/src/ingest/document/mod.rs
- file: crates/gwiki/src/ingest/document/office.rs
- file: crates/gwiki/src/ingest/document/render.rs
- file: crates/gwiki/src/ingest/document/tests.rs
- file: crates/gwiki/src/ingest/file/tests.rs
- file: crates/gwiki/src/ingest/git.rs
- file: crates/gwiki/src/ingest/image.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/ingest/pdf/ingest.rs
- file: crates/gwiki/src/ingest/pdf/markdown.rs
- file: crates/gwiki/src/ingest/pdf/render.rs
- file: crates/gwiki/src/ingest/pdf/tests.rs
- file: crates/gwiki/src/ingest/pdf/text.rs
- file: crates/gwiki/src/ingest/session.rs
- file: crates/gwiki/src/ingest/session/codex.rs
- file: crates/gwiki/src/ingest/session/droid.rs
- file: crates/gwiki/src/ingest/session/gemini.rs
- file: crates/gwiki/src/ingest/session/grok.rs
- file: crates/gwiki/src/ingest/session/metadata.rs
- file: crates/gwiki/src/ingest/session/qwen.rs
- file: crates/gwiki/src/ingest/session_archive.rs
- file: crates/gwiki/src/ingest/url.rs
- file: crates/gwiki/src/ingest/url/fetch.rs
- file: crates/gwiki/src/ingest/url/render.rs
- file: crates/gwiki/src/ingest/url/tests.rs
- file: crates/gwiki/src/ingest/video/processing.rs
- file: crates/gwiki/src/ingest/video/tests.rs
- file: crates/gwiki/src/ingest/wayback.rs
provenance_truncated: 15
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest` contains 10 direct files and 6 child modules.
[crates/gwiki/src/ingest/audio.rs:21-28]
[crates/gwiki/src/ingest/document/html.rs:8-39]
[crates/gwiki/src/ingest/document/mod.rs:21-27]
[crates/gwiki/src/ingest/document/office.rs:39-52]
[crates/gwiki/src/ingest/document/render.rs:11-33]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/src/ingest/document\|crates/gwiki/src/ingest/document]] | `crates/gwiki/src/ingest/document` contains 5 direct files and 0 child modules. [crates/gwiki/src/ingest/document/html.rs:8-39] [crates/gwiki/src/ingest/document/mod.rs:21-27] [crates/gwiki/src/ingest/document/office.rs:39-52] [crates/gwiki/src/ingest/document/render.rs:11-33] [crates/gwiki/src/ingest/document/tests.rs:9-18] |
| [[code/modules/crates/gwiki/src/ingest/file\|crates/gwiki/src/ingest/file]] | `crates/gwiki/src/ingest/file` contains 7 direct files and 0 child modules. [crates/gwiki/src/ingest/file/degradation.rs:4-11] [crates/gwiki/src/ingest/file/dispatch.rs:43-242] [crates/gwiki/src/ingest/file/generic.rs:11-57] [crates/gwiki/src/ingest/file/render.rs:6-51] [crates/gwiki/src/ingest/file/replay.rs:8-32] |
| [[code/modules/crates/gwiki/src/ingest/pdf\|crates/gwiki/src/ingest/pdf]] | `crates/gwiki/src/ingest/pdf` contains 7 direct files and 0 child modules. [crates/gwiki/src/ingest/pdf/ingest.rs:23-37] [crates/gwiki/src/ingest/pdf/markdown.rs:15-89] [crates/gwiki/src/ingest/pdf/mod.rs:22-25] [crates/gwiki/src/ingest/pdf/render.rs:23-39] [crates/gwiki/src/ingest/pdf/tests.rs:21] |
| [[code/modules/crates/gwiki/src/ingest/session\|crates/gwiki/src/ingest/session]] | `crates/gwiki/src/ingest/session` contains 8 direct files and 0 child modules. [crates/gwiki/src/ingest/session/codex.rs:12] [crates/gwiki/src/ingest/session/derived.rs:10-26] [crates/gwiki/src/ingest/session/droid.rs:12] [crates/gwiki/src/ingest/session/gemini.rs:12] [crates/gwiki/src/ingest/session/grok.rs:12] |
| [[code/modules/crates/gwiki/src/ingest/url\|crates/gwiki/src/ingest/url]] | `crates/gwiki/src/ingest/url` contains 3 direct files and 0 child modules. [crates/gwiki/src/ingest/url/fetch.rs:15-20] [crates/gwiki/src/ingest/url/render.rs:12-37] [crates/gwiki/src/ingest/url/tests.rs:21-60] [crates/gwiki/src/ingest/url/fetch.rs:23-25] [crates/gwiki/src/ingest/url/fetch.rs:28-35] |
| [[code/modules/crates/gwiki/src/ingest/video\|crates/gwiki/src/ingest/video]] | `crates/gwiki/src/ingest/video` contains 5 direct files and 0 child modules. [crates/gwiki/src/ingest/video/assets.rs:4-23] [crates/gwiki/src/ingest/video/metadata.rs:4-8] [crates/gwiki/src/ingest/video/mod.rs:32-45] [crates/gwiki/src/ingest/video/processing.rs:18-26] [crates/gwiki/src/ingest/video/tests.rs:25-62] |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/audio.rs\|crates/gwiki/src/ingest/audio.rs]] | `crates/gwiki/src/ingest/audio.rs` exposes 46 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/file.rs\|crates/gwiki/src/ingest/file.rs]] | `crates/gwiki/src/ingest/file.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/git.rs\|crates/gwiki/src/ingest/git.rs]] | `crates/gwiki/src/ingest/git.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/image.rs\|crates/gwiki/src/ingest/image.rs]] | `crates/gwiki/src/ingest/image.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/mediawiki.rs\|crates/gwiki/src/ingest/mediawiki.rs]] | `crates/gwiki/src/ingest/mediawiki.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/mod.rs\|crates/gwiki/src/ingest/mod.rs]] | `crates/gwiki/src/ingest/mod.rs` exposes 61 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session.rs\|crates/gwiki/src/ingest/session.rs]] | `crates/gwiki/src/ingest/session.rs` exposes 45 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session_archive.rs\|crates/gwiki/src/ingest/session_archive.rs]] | `crates/gwiki/src/ingest/session_archive.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/url.rs\|crates/gwiki/src/ingest/url.rs]] | `crates/gwiki/src/ingest/url.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/wayback.rs\|crates/gwiki/src/ingest/wayback.rs]] | `crates/gwiki/src/ingest/wayback.rs` exposes 31 indexed API symbols. |

