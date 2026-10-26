# Agent Playbook

**Retired and unsupported as of 2026-10-02.** No maintenance, fixes, or security
updates are provided. Never published to PyPI by `yeongseon`; history, tags, and
GitHub releases are historical source snapshots only. A same-named PyPI project
is not an official release from this repository.

Limit work to preserving history and correcting retirement documentation unless
the maintainer explicitly decides to reactivate the project. Do not resume feature
work, renew publishing credentials, configure a Trusted Publisher, enable release
or Azure e2e workflows, or run release/recovery procedures. Retained procedures
are historical reference, not authorization to execute them.

## Source Of Truth
- `AGENTS.md` for repository-wide engineering and agent rules.
- `README.md` for installation, quick start, and CLI examples.
- `CONTRIBUTING.md` for branch, commit, and release workflow.
- `pyproject.toml` and `Makefile` for supported commands.

## Repository Map
- `src/azure_functions_knowledge/` package code.
- `tests/` RAG decorator and provider coverage.
- `examples/` example Azure Functions apps.
- `docs/` documentation site content.

## Change Workflow
1. Confirm whether the change affects knowledge API, provider behavior, decorator interface, or docs only.
2. Update examples when they are used as public contract material.
3. Keep tests and docs in lockstep for public behavior changes.
4. Do not broaden supported Python versions or dependency ranges casually.

## Validation
- `make test`
- `make lint`
- `make typecheck`
- `make security`
- `make build`
