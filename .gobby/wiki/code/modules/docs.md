---
title: docs
type: code_module
provenance: []
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# docs

Parent: [[code/repo|Repository Overview]]

## Overview

The docs module serves as the centralized documentation hub for the project, containing no direct source code or indexed APIs. It is organized into four submodules: contracts for interface specifications and shared schemas, guides for comprehensive setup instructions, workflow standards, and subsystem documentation, plans for technical design specifications and release strategies, and spikes for cross-language interoperability research. Together, these components provide the complete informational reference framework for the platform's architecture, development lifecycle, and future planning.

## Child Modules

- [[code/modules/docs/contracts|docs/contracts]] - This module contains documentation for interface contracts and schemas, covering CLI specifications for gcode and gwiki, gwiki research, and a shared graph schema.
- [[code/modules/docs/guides|docs/guides]] - This module provides comprehensive documentation and guides for the platform's core components and development workflows. It covers AI configuration, daemon contracts, and CodeWiki integration, alongside detailed user and developer instructions for subsystems including GCode, GCore, GHook, GLoc, GSQZ, and GWiki. The collection also includes setup instructions for hub installation and standardized procedures for managing software releases.
- [[code/modules/docs/plans|docs/plans]] - This module contains technical planning documents and design specifications for project features. It includes a release plan and delegates completed plans to the `docs/plans/completed` subdirectory. No indexed code APIs are present.
- [[code/modules/docs/spikes|docs/spikes]] - The `docs/spikes` module contains documentation for technical spikes investigating external callees across various programming languages. Individual files detail interop and call patterns for Bash, C/C++, Dart/Elixir, Kotlin, Lua, Ruby, and Scala. The module comprises purely informational documentation with no indexed API symbols, child modules, or stable components.

