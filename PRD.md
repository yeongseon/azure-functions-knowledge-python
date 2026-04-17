# PRD - azure-functions-knowledge-python

## Overview

`azure-functions-knowledge-python` provides knowledge retrieval (RAG) decorators for the
Azure Functions Python v2 programming model.

It is intended for decorator-based `func.FunctionApp()` applications that want provider-backed
knowledge search and document retrieval in handlers without leaving the Azure Functions model.

## Problem Statement

Azure Functions Python applications often need retrieval-augmented behavior, but teams lack a
consistent way to:

- wire provider search into handler parameters
- inject provider clients safely for imperative retrieval workflows
- keep provider choice and authentication details behind a small, reusable abstraction

This leads to duplicated integration code, ad-hoc credential handling, and inconsistent RAG
patterns across function apps.

## Goals

- Provide a small decorator-first API for knowledge retrieval integration.
- Inject provider search results as typed `Document` lists.
- Inject provider clients for direct `search()` and `get_document()` workflows.
- Support built-in Notion integration and custom provider registration through a protocol.
- Stay aligned with Azure Functions Python v2 and companion libraries in this ecosystem.

## Non-Goals

- Building a full agent framework or LLM orchestration runtime
- Replacing Azure Functions trigger/routing/runtime concepts
- Owning embedding generation, vector storage, or indexing pipelines
- Mandating a single provider backend
- Supporting the legacy `function.json`-based Python v1 model

## Primary Users

- Maintainers of Azure Functions Python APIs that need RAG-style retrieval
- Teams adopting decorator-based Azure Functions and wanting provider abstraction
- Users pairing this package with `azure-functions-openapi-python` and `azure-functions-validation-python`

## Core Use Cases

- Annotate a handler with `@kb.input` to inject `Document` search results
- Annotate a handler with `@kb.inject_client` for imperative provider operations
- Resolve `%VAR%` placeholders in connection strings at runtime
- Register custom providers via `register_provider()` for non-Notion backends

## Success Criteria

- Supported examples execute successfully in CI with retrieval decorators enabled
- Decorator composition rules (`input` vs `inject_client`, duplicate prevention) are enforced
- Connection placeholder resolution fails fast with clear configuration errors
- Documentation and examples stay aligned with provider protocol and `Document` shape

## Example-First Design

### Philosophy

Small-ecosystem libraries succeed when developers can copy a working example and see
results immediately. `azure-functions-knowledge-python` treats runnable examples as a first-class
deliverable - every decorator feature should have a corresponding example that returns real
retrieval results or provider-backed document content.

### Quick Start (Search Endpoint)

The shortest path from zero to a working knowledge search endpoint:

```python
import azure.functions as func
from azure_functions_knowledge import Document, KnowledgeBindings

app = func.FunctionApp()
kb = KnowledgeBindings()


@app.route(route="search", methods=["GET"])
@kb.input(
    "docs",
    provider="notion",
    query=lambda req: req.params.get("q", ""),
    top=5,
    connection="%NOTION_TOKEN%",
)
def search(req: func.HttpRequest, docs: list[Document]) -> func.HttpResponse:
    import json

    results = [{"title": d.title, "url": d.url} for d in docs]
    return func.HttpResponse(json.dumps(results), mimetype="application/json")
```

Run `func start`, then call `http://localhost:7071/api/search?q=your-query`.

### Why Examples Matter

1. **Lower entry barrier.** A working search example in the PRD and README lets developers
   evaluate provider integration quickly.
2. **AI agent discoverability.** Tools like GitHub Copilot, Cursor, and Claude Code recommend
   libraries based on README, PRD, and example content. Rich examples increase the chance
   that AI agents surface `azure-functions-knowledge-python` for RAG-in-Azure-Functions prompts.
3. **Cookbook role.** For niche ecosystems, `examples/` and `docs/` are often the primary
   learning material. New decorator patterns should ship with runnable examples.
4. **Operational clarity.** Examples capture practical details such as `%VAR%` connection
   resolution, provider wiring, and response-shaping patterns.

### Examples Inventory

| Role | Path | Pattern |
|---|---|---|
| Representative | `examples/function_app.py` | Search endpoint with `@kb.input` and page retrieval with `@kb.inject_client` |

Examples should remain smoke-testable and updated when decorator contracts evolve.
