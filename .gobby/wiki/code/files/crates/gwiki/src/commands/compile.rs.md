---
title: crates/gwiki/src/commands/compile.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/compile.rs
  ranges:
  - 14-104
  - 109-119
  - 121-155
  - 160-190
  - 192-199
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/compile.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `gwiki compile` command by loading the resolved research session, determining the article topic from explicit input, topic scope, or session state, and then delegating to the wiki compiler with the requested outline, target kind, target page, and write intent. It also probes daemon synthesis availability, resolves the AI explainer transport, and conditionally supplies an `ExplainerGenerator` so compilation can use daemon or text-based synthesis when enabled. The helper transport methods and routing functions encapsulate whether AI synthesis is active, how the route is labeled, and how a given `AiRouting` configuration maps to either a resolved or disabled explainer backend.
[crates/gwiki/src/commands/compile.rs:14-104]
[crates/gwiki/src/commands/compile.rs:109-119]
[crates/gwiki/src/commands/compile.rs:121-155]
[crates/gwiki/src/commands/compile.rs:122-124]
[crates/gwiki/src/commands/compile.rs:126-131]

## API Symbols

- `execute` (function) component `execute [function]` (`c23787b4-704c-52bc-8292-76cbbff8c06c`) lines 14-104 [crates/gwiki/src/commands/compile.rs:14-104]
  - Signature: `pub(crate) fn execute(`
  - Purpose: # Summary Compiles a wiki article from a resolved research session with topic resolved through explicit/scope/session precedence and optional AI-powered synthesis routing. [crates/gwiki/src/commands/compile.rs:14-104]
- `ExplainerTransport` (type) component `ExplainerTransport [type]` (`64bc8757-3360-50ef-b69e-4ac1162ecaaa`) lines 109-119 [crates/gwiki/src/commands/compile.rs:109-119]
  - Signature: `enum ExplainerTransport {`
  - Purpose: Indexed type `ExplainerTransport` in `crates/gwiki/src/commands/compile.rs`. [crates/gwiki/src/commands/compile.rs:109-119]
- `ExplainerTransport` (class) component `ExplainerTransport [class]` (`edef227b-f665-5941-bb56-9a83febf7d66`) lines 121-155 [crates/gwiki/src/commands/compile.rs:121-155]
  - Signature: `impl ExplainerTransport {`
  - Purpose: ExplainerTransport conditionally routes AI prompt generation to daemon or text synthesis backends based on its operational state (Off, Unresolved, or Resolved). [crates/gwiki/src/commands/compile.rs:121-155]
- `ExplainerTransport.is_active` (method) component `ExplainerTransport.is_active [method]` (`94889f9c-cc62-52f2-a46a-1a5ad95f1794`) lines 122-124 [crates/gwiki/src/commands/compile.rs:122-124]
  - Signature: `fn is_active(&self) -> bool {`
  - Purpose: Returns 'true' if the instance is not the 'Off' enum variant, 'false' otherwise. [crates/gwiki/src/commands/compile.rs:122-124]
- `ExplainerTransport.route_label` (method) component `ExplainerTransport.route_label [method]` (`bb71d54b-71c0-5b52-aea2-6f9077291085`) lines 126-131 [crates/gwiki/src/commands/compile.rs:126-131]
  - Signature: `fn route_label(&self) -> &'static str {`
  - Purpose: This method returns a static string label: '"off"' for the 'Off' variant, or the result of delegating to 'routing_label()' with the dereferenced 'route' field for 'Unresolved' and 'Resolved' variants. [crates/gwiki/src/commands/compile.rs:126-131]
- `ExplainerTransport.generate` (method) component `ExplainerTransport.generate [method]` (`f337e6d0-a625-5d2b-a9cb-c1c72010d0f1`) lines 133-154 [crates/gwiki/src/commands/compile.rs:133-154]
  - Signature: `fn generate(&self, prompt: &ExplainerPrompt) -> Result<ExplainerResponse, String> {`
  - Purpose: This method generates an ExplainerResponse by routing the provided prompt through either a daemon or text-based AI service, or returns an error if synthesis is disabled or initialization failed. [crates/gwiki/src/commands/compile.rs:133-154]
- `resolve_explainer_transport` (function) component `resolve_explainer_transport [function]` (`bb503efa-4b4b-5c8c-ba05-49668cfcac7b`) lines 160-190 [crates/gwiki/src/commands/compile.rs:160-190]
  - Signature: `fn resolve_explainer_transport(requested: AiRouting) -> ExplainerTransport {`
  - Purpose: Returns 'ExplainerTransport::Off' for 'AiRouting::Off', otherwise resolves AI config and capability routing to 'Daemon' or 'Direct' and returns a resolved transport with the computed context, or falls back to 'Unresolved' for those routes on config-source errors and 'Off' for all other cases. [crates/gwiki/src/commands/compile.rs:160-190]
- `routing_label` (function) component `routing_label [function]` (`54e2eb1e-c21b-5b31-9063-59dff3147b2f`) lines 192-199 [crates/gwiki/src/commands/compile.rs:192-199]
  - Signature: `fn routing_label(route: AiRouting) -> &'static str {`
  - Purpose: Performs exhaustive pattern matching on an 'AiRouting' enum to return a static string representation of the input variant. [crates/gwiki/src/commands/compile.rs:192-199]

