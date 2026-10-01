# Changelog

## [0.1.2](https://github.com/yeongseon/azure-functions-knowledge-python/compare/v0.1.1...v0.1.2) (2026-10-01)


### Bug Fixes

* **ci:** align canonical azure/login pin with the bumped v3.1.0 SHA ([#121](https://github.com/yeongseon/azure-functions-knowledge-python/issues/121)) ([8551a85](https://github.com/yeongseon/azure-functions-knowledge-python/commit/8551a8565a22806ceaed4a97d5ec9f6d6c34a0c1))
* **ci:** bump canonical azure/login pin to v3.0.2 ([#107](https://github.com/yeongseon/azure-functions-knowledge-python/issues/107)) ([0047fc7](https://github.com/yeongseon/azure-functions-knowledge-python/commit/0047fc722b4aff7ac2a19722012c84db106692cb)), closes [#103](https://github.com/yeongseon/azure-functions-knowledge-python/issues/103)
* **ci:** correct release wording, stale.yml inputs, and add issue templates ([#127](https://github.com/yeongseon/azure-functions-knowledge-python/issues/127)) ([0802608](https://github.com/yeongseon/azure-functions-knowledge-python/commit/0802608ee1532f346bd728ecd29393e282897b93))
* **ci:** stop the changed-file format gate failing open ([#124](https://github.com/yeongseon/azure-functions-knowledge-python/issues/124)) ([de64a27](https://github.com/yeongseon/azure-functions-knowledge-python/commit/de64a272441e5db88845de39a3d64578c9119cfa))
* **compat:** deprecate Python 3.10 ahead of its removal ([#148](https://github.com/yeongseon/azure-functions-knowledge-python/issues/148)) ([f0ea38d](https://github.com/yeongseon/azure-functions-knowledge-python/commit/f0ea38d5e4b8b09b60b215c61f35e09dac42e7d4))
* **decorator:** keep handler errors when cleanup fails ([6bc8c4e](https://github.com/yeongseon/azure-functions-knowledge-python/commit/6bc8c4ed6f7e8c4b1447a4e492a4d49d3cdeb76d))
* **decorator:** keep the handler error when provider cleanup also fails ([#150](https://github.com/yeongseon/azure-functions-knowledge-python/issues/150)) ([6bc8c4e](https://github.com/yeongseon/azure-functions-knowledge-python/commit/6bc8c4ed6f7e8c4b1447a4e492a4d49d3cdeb76d))
* **decorator:** resolve dynamic query against positional handler args ([#106](https://github.com/yeongseon/azure-functions-knowledge-python/issues/106)) ([27449d2](https://github.com/yeongseon/azure-functions-knowledge-python/commit/27449d21baf52e82d437e3cd8a86ed27f0d9cf13)), closes [#105](https://github.com/yeongseon/azure-functions-knowledge-python/issues/105)
* **deps:** drop unsupported semver cooldown keys for github-actions ecosystem ([#111](https://github.com/yeongseon/azure-functions-knowledge-python/issues/111)) ([e319707](https://github.com/yeongseon/azure-functions-knowledge-python/commit/e319707af0f4486963e815b8b75f706c9c24b7c6))
* gate publish on non-empty importable wheel and drop redundant hatch sources ([#88](https://github.com/yeongseon/azure-functions-knowledge-python/issues/88)) ([fefee87](https://github.com/yeongseon/azure-functions-knowledge-python/commit/fefee8739464f879892f5feaa51d7c681a4fc8df))

## Changelog

All notable changes to this project will be documented in this file.

### Documentation

- *(release)* Require cookbook dogfood verification after publish 

### Other

- Bump version to 0.1.1 

### Bug Fixes

- *(decorator)* Stop exposing __wrapped__ on knowledge handler wrappers (#46) 
- *(release)* Align PyPI distribution name to azure-functions-knowledge (#43) 
- *(providers)* Correct notion install hint to canonical package name (#20) 
- *(providers/notion)* Harden registration, populate search content, paginate & recurse blocks (#10) 

### Documentation

- Update changelog 
- *(release)* Document PyPI trusted publisher configuration (#41) 
- Require translation sync in the same PR as English changes (Closes #39) (#40) 
- Align README with toolkit standard structure (#37) (#38) 
- Author standard docs (api, architecture, configuration, usage, providers) and expand examples (#29) 
- Enable mermaid rendering and add canonical architecture diagram (#30) 
- Add discoverability metadata (pepy badge + llms.txt) (#35) 
- Add 'For AI Coding Assistants' section pointing to llms.txt (#24) 
- *(contributing)* Document GitHub Actions SHA pinning policy (#14) 
- *(agents)* Standardize AGENTS.md with coverage floor, PR workflow, and issue conventions (#12) 
- Fix ecosystem table names, badges, and Part of intro line 

### Miscellaneous Tasks

- *(deps)* Cap azure-functions below 2.0.0 (#48) 
- Track issue priority via priority:* labels instead of body line (#42) 
- Align AGENTS.md test_public_api guidance and enforce 95% coverage floor (#22) 

### Other

- Bump version to 0.1.0 

### Refactor

- *(metadata)* Formalize knowledge metadata contract (TypedDict + version) (#49) 
- *(decorator)* Type provider kwargs and resolve Document.score (#36) 
- *(decorator)* Dedupe wrappers, add provider lifecycle, integrate toolkit metadata (#33) 
- *(tests)* Assert __version__ against importlib.metadata (#17) 

### Testing

- Tighten CI coverage enforcement and add provider/decorator edge cases (#31) 

### Bug Fixes

- Declare wheel packages explicitly for hatchling (#6) 

### Documentation

- Mark cookbook as dogfood, fix ecosystem table description 
- Fix ecosystem table — add knowledge row, fix labels and links 
- Fix README H1 title to proper capitalized name 

### Features

- Initial implementation of azure-functions-knowledge 

### Miscellaneous Tasks

- Update repo references for azure-functions-{feature}-python naming convention 
- Add DX Toolkit standard files, Ecosystem section, and CI workflows (#4) 
- Unify Python 3.10 minimum and add missing governance files (#1) 
<!-- generated by git-cliff -->
