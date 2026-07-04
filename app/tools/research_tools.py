from app.tools.retry import retry_with_backoff
from app.tools.error_handling import ToolTemporaryError, ToolInputError
from typing import Literal

@retry_with_backoff(
    max_attempts=3,
    base_delay=0.5,
    max_delay=2.0,
    jitter=True
)
def _search_provider(query: str, source: str) -> dict:

    if "timeout" in query:

        raise ToolTemporaryError("upstream search provider timed out.")
    
    return {
        "query": query,
        "source": source,
        "results": [
            {
                "title": f"Search result for {query}",
                "summary": "Mocked research result",
                "confidence": 0.82,
                "url": "https://example.com/research-image",
                "image": []
            },
        ]
    }


def research_search_tool(query: str, source: Literal["web", "news", "docs"] = "web") -> dict:

    if not query or len(query) < 3:
        raise ToolInputError("Query must contain at least 3 characters.")
    
    if source not in {"web", "news", "docs"}:

        raise ToolInputError("Source must be in 'web', 'news', 'docs'.")
    
    return _search_provider(
        query=query,
        source=source
    )