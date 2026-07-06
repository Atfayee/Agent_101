from langchain_core.tools import tool
from typing import Literal
from error_handling import ToolFataError, ToolInputError, ToolTemporaryError

@tool
def research_search_tool(
    query: str,
    source: Literal["web", "docs", "news"] = "web"
) -> dict:
    """
    Search a research source and return structured results.

    Args:
        query: The research query.
        source: One of "web", "news", "docs".
    """

    if not query or len(query.strip()) < 3:
        raise ToolInputError("query must have at least 3 characters.")
    
    if source not in {"web", "docs", "news"}:
        raise ToolInputError("source must from 'dosc', 'web' or 'news'.")
    
    if "timeout" in query.lower():
        raise ToolTemporaryError("upstream search provider timeout.")
    
    return {
        "query": query,
        "source": source,
        "results": {
            "title": f"Search {query}",
            "summary": "Fake research results",
            "confidence": 0.92,
            "url": "https://image.test",
            "images": []
        }
    }