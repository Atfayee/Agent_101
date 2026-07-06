from typing import Literal

from langchain_core.tools import tool

from app.config.settings import settings
from app.schemas.research import ResearchResult, ResearchToolOutput
from app.tools.errors import ToolInputError, ToolTemporaryError
from app.tools.retry import retry_with_backoff

@retry_with_backoff(
    max_attempts=settings.max_retries,
)
def _mock_search_provider(query: str, source: str) -> ResearchToolOutput:
    if "timeout" in query.lower():
        raise ToolTemporaryError("upstream search provider timed out.")
    
    return ResearchToolOutput(
        query=query,
        source=source,
        results=[
            ResearchResult(
                title=f"{source.upper()} reuslt for {query}",
                summary=f"This mocked sources says {query} is relevant to LangGraph",
                url="https://exmaple.com/research",
                confidence=0.82,
                image=[]
            )
        ]
    )


@tool
def search_research_source(
    query: str,
    source: Literal["web", "docs", "news"] = "web"
) -> dict:
    """
    Search a research source.

    Agrs: 
        query: Research query.
        source: One of web, docs, news
    """
    if not query or len(query) < 3:
        raise ToolInputError("Query must contain at least 3 characters.")
    
    if source not in {"web", "docs", "news"}:
        raise ToolInputError("Source must be from 'web', 'news' or 'docs'")
    
    return _mock_search_provider(query=query, source=source)

research_tools = [search_research_source]