---
title: crates/gwiki/src/output.rs
type: code_file
provenance:
- file: crates/gwiki/src/output.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/output.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/output.rs` exposes 32 indexed API symbols.

## How it fits

`crates/gwiki/src/output.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Format` | type | Indexed type `Format` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:10-13] |
| `OutputError` | type | Indexed type `OutputError` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:16-19] |
| `OutputError::fmt` | method | Formats the error enum by writing '"output write failed: {error}"' for 'Io' and '"JSON rendering failed: {error}"' for 'Json' into the provided formatter. [crates/gwiki/src/output.rs:22-27] |
| `OutputError::from` | method | Converts a 'std::io::Error' into 'Self' by wrapping it in the 'Self::Io' variant. [crates/gwiki/src/output.rs:33-35] |
| `OutputError::from` | method | Converts a 'serde_json::Error' into 'Self' by wrapping it in the 'Self::Json' variant. [crates/gwiki/src/output.rs:39-41] |
| `print_result` | function | 'print_result' dispatches to 'print_json' or 'print_text' based on the requested 'Format', writing either 'result.payload' or 'result.text' to the provided 'Write' and returning the corresponding 'Result<(), OutputError>'. [crates/gwiki/src/output.rs:44-53] |
| `print_json` | function | Serializes 'value' to pretty-printed JSON with 'serde_json::to_string_pretty', writes it followed by a newline to 'writer', and returns 'Ok(())' or propagates serialization/write errors as 'OutputError'. [crates/gwiki/src/output.rs:55-61] |
| `print_text` | function | Writes 'text' followed by a newline to the provided 'writer' using 'writeln!', then returns 'Ok(())' or propagates any write failure as 'OutputError'. [crates/gwiki/src/output.rs:63-66] |
| `print_status` | function | Prints the given message to standard error prefixed with 'gwiki: '. [crates/gwiki/src/output.rs:68-70] |
| `SearchOutput` | class | 'SearchOutput' is a Rust struct that captures the outcome of a search operation, including the executed command, target scope, query string, result limit, returned search results, code citations, and any degradation messages. [crates/gwiki/src/output.rs:73-81] |
| `SearchOutput::new` | method | Constructs a 'Search' instance by converting the query into a 'String', deriving 'code_citations' from the provided 'results', and storing the supplied 'scope', 'limit', 'results', and 'degradations' with 'command' fixed to '"search"'. [crates/gwiki/src/output.rs:84-101] |
| `code_citations_from_results` | function | Filters 'SearchResultOutput' entries to code results only, deduplicates them by '(source file path, title)' using a 'BTreeSet', and returns a 'Vec<CodeCitationOutput>' with each unique file and symbol and no line number. [crates/gwiki/src/output.rs:107-125] |
| `AskOutput` | class | 'AskOutput' is a serialized result container for an ask/query operation that records the command, scope, query, execution status, degradation and truncation metadata, search hits and source/citation/evidence lists, prompt token budgeting, warnings, and optional AI/synthesis outputs. [crates/gwiki/src/output.rs:131-151] |
| `AskEvidenceOutput` | class | 'AskEvidenceOutput' is a Rust data struct that records the output of an evidence lookup with the wiki page path, the source file path, and the number of excerpt characters returned. [crates/gwiki/src/output.rs:155-159] |
| `CodeCitationOutput` | class | 'CodeCitationOutput' is a serializable Rust struct that identifies a code citation by file path and optionally includes a line number and symbol name. [crates/gwiki/src/output.rs:162-168] |
| `SearchResultType` | type | Indexed type `SearchResultType` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:173-176] |
| `SearchResultType::from_wiki_page` | method | Returns 'Self::Code' if the normalized path string begins with 'code/files/' after converting backslashes to forward slashes, otherwise returns 'Self::Wiki'. [crates/gwiki/src/output.rs:181-191] |
| `SearchResultType::is_code` | method | Returns 'true' if 'self' is the 'Code' variant, and 'false' otherwise. [crates/gwiki/src/output.rs:193-195] |
| `SearchResultOutput` | class | 'SearchResultOutput' is a search result record containing an optional title, a fusion key, wiki and source file paths, a result type, snippet text, a numeric score, a list of source identifiers, and per-source explanation entries. [crates/gwiki/src/output.rs:199-209] |
| `AskAiOutput` | class | 'AskAiOutput' is a response struct that records whether an AI request was made, the requested mode, route, and status as static strings, plus optional 'model' and 'error' details as owned strings. [crates/gwiki/src/output.rs:212-219] |
| `AskSynthesisOutput` | class | 'AskSynthesisOutput' is a struct that packages a synthesized 'answer' string, an optional 'model' identifier, and a required 'AskCitationCheckOutput' used for citation verification. [crates/gwiki/src/output.rs:222-226] |
| `AskCitationCheckOutput` | class | 'AskCitationCheckOutput' is a result struct containing a status string, the number of claims checked, and a list of unsupported claim strings. [crates/gwiki/src/output.rs:233-237] |
| `SearchSourceExplanationOutput` | class | 'SearchSourceExplanationOutput' is a Rust struct that records a search source identifier ('source'), its ordinal position ('rank'), and its relevance metric ('score'). [crates/gwiki/src/output.rs:240-244] |
| `QueryOutput` | class | 'QueryOutput' is a Rust struct that represents the result of a query, containing the originating command, a 'ScopeIdentity' scope, the query text, the generated answer, and a vector of 'QueryCitation' references. [crates/gwiki/src/output.rs:247-253] |

_5 more symbol(s) not shown — run `gcode outline crates/gwiki/src/output.rs` for the full list._

_Verified by 3 in-file unit tests._

