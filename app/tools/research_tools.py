from typing import Literal
from app.tools.error_handling import ToolFataError, ToolInputError, ToolTemporaryError
from langchain_core.tools import tool


@tool
def search_research_source(
    query: str,
    source: Literal["web", "news", "docs"] = "web"
) -> dict:
    """
    
    """
    if not query or len(query.strip()) < 3:
        raise ToolInputError("Query must contain at least 3 characters")
    
    if source not in {"web", "news", "docs"}:
        raise ToolInputError(f"Invalid source: '{source}'")
    
    if "timeout" in query:
        raise ToolTemporaryError("The upstream search provider timed out.")
    
    return {
        "query": query,
        "source": source,
        "results": [
            {
                "title": f"Research result for {query}",
                "summary": "Mocked summary findings",
                "confidence": 0.92,
                "url": "https://images",
                "image": []
            }
        ]
    }