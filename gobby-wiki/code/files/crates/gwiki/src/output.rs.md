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
| `SearchOutput` | class | 'SearchOutput' is a struct that encapsulates the complete results and metadata of a search operation, including the query parameters, result set, code citations, degradation diagnostives, and an optional token-budget hint. [crates/gwiki/src/output.rs:73-84] |
| `SearchOutput::new` | method | Constructs a search result struct by initializing search parameters (scope, query, limit, results, degradations) and extracting code citations from the results vector, with hint defaulting to None. [crates/gwiki/src/output.rs:87-105] |
| `code_citations_from_results` | function | Extracts unique code citations from search results by filtering code-type hits and deduplicating on (file path, symbol) pairs. [crates/gwiki/src/output.rs:111-129] |
| `AskOutput` | class | AskOutput is a struct that represents the complete result of an AI-powered search query operation, encapsulating search hits, citations, evidence, token budget accounting, and optional synthesized responses along with metadata for service degradation and result truncation. [crates/gwiki/src/output.rs:135-158] |
| `AskEvidenceOutput` | class | AskEvidenceOutput is a public struct that encapsulates evidence metadata, containing file paths to a wiki page and source document along with an excerpt character count. [crates/gwiki/src/output.rs:162-166] |
| `CodeCitationOutput` | class | CodeCitationOutput is a serde-enabled struct that represents a code location citation with a required file path and optional line number and symbol name, skipping serialization of absent optional fields. [crates/gwiki/src/output.rs:169-175] |
| `SearchResultType` | type | Indexed type `SearchResultType` in `crates/gwiki/src/output.rs`. [crates/gwiki/src/output.rs:180-183] |
| `SearchResultType::from_wiki_page` | method | This method constructs and returns a 'Self' enum variant ('Code' or 'Wiki') based on whether the normalized file path begins with "code/files/". [crates/gwiki/src/output.rs:188-198] |
| `SearchResultType::is_code` | method | This method consumes 'self' and returns 'true' if the enum value is the 'Code' variant, 'false' otherwise. [crates/gwiki/src/output.rs:200-202] |
| `SearchResultOutput` | class | 'SearchResultOutput' is a struct that encapsulates a search result, containing its content snippet, relevance score, source metadata (paths and references), result type classification, and supporting source explanation data. [crates/gwiki/src/output.rs:206-216] |
| `AskAiOutput` | class | 'AskAiOutput' is a struct that encapsulates metadata about an AI request, containing a boolean request flag, three static string references for mode/route/status, and optional String fields for model selection and error reporting. [crates/gwiki/src/output.rs:219-226] |
| `AskSynthesisOutput` | class | 'AskSynthesisOutput' is a struct that encapsulates a synthesized answer string, an optional model identifier, and citation verification results. [crates/gwiki/src/output.rs:229-233] |
| `AskCitationCheckOutput` | class | AskCitationCheckOutput is a Rust struct that represents the results of a citation verification operation, containing a static string status indicator, a count of evaluated claims, and a vector of unsupported claim strings. [crates/gwiki/src/output.rs:240-244] |
| `SearchSourceExplanationOutput` | class | 'SearchSourceExplanationOutput' is a public struct that encapsulates a search result with three fields: a 'String' source identifier, a 'usize' rank representing position, and an 'f64' score representing relevance or matching strength. [crates/gwiki/src/output.rs:247-251] |
| `QueryOutput` | class | QueryOutput is a Rust struct that encapsulates a query response, containing a static command identifier, scope context, the input query string, the generated answer string, and a vector of supporting citations. [crates/gwiki/src/output.rs:254-260] |

_5 more symbol(s) not shown — run `gcode outline crates/gwiki/src/output.rs` for the full list._

_Verified by 3 in-file unit tests._

