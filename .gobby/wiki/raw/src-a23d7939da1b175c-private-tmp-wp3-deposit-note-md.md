---
source_kind: markdown
source_location: /private/tmp/wp3-deposit-note.md
fetched_at: "unix-ms:1781421066871"
source_hash: a23d7939da1b175cda166e225c577f5e85f5b14a3be00f99f61b47ec0828b235
---

# wp3-deposit-note.md

# Why gsqz always exits 0

gsqz deliberately exits with status code 0 regardless of the wrapped
command's exit status. The compressed output carries the real pass/fail
signal in its content, and forcing exit 0 prevents the host LLM (Claude
Code) from framing the compressed text as a tool error.

Source: crates/gsqz/src/main.rs; CLAUDE.md "Exit code 0 (gsqz)".
