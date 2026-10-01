from __future__ import annotations

import sys
import warnings

__version__ = "0.1.1"

import azure_functions_knowledge.providers.notion as _notion_module  # noqa: F401

from .decorator import KnowledgeBindings
from .errors import AuthError, ConfigurationError, KnowledgeError, ProviderError
from .providers.base import (
    KnowledgeProvider,
    create_provider,
    get_registered_providers,
    register_provider,
)
from .types import Document

__all__ = [
    "__version__",
    "AuthError",
    "ConfigurationError",
    "Document",
    "KnowledgeBindings",
    "KnowledgeError",
    "KnowledgeProvider",
    "ProviderError",
    "create_provider",
    "get_registered_providers",
    "register_provider",
]


if sys.version_info < (3, 11):
    warnings.warn(
        "azure-functions-knowledge will drop support for Python 3.10 in its next minor release. "
        "Python 3.10 reaches end of life in October 2026; upgrade to Python 3.11 "
        "or newer to keep receiving updates.",
        FutureWarning,
        stacklevel=2,
    )
