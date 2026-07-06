from langchain_community.tools import TavilySearchResults
from langchain_core.tools import tool

_search = TavilySearchResults(
    max_results=5
)

@tool
def search(query: str) -> str:
    """
    Search the web for recent factual information

    Use this tool whenever the answer depends on current events or information after the LLM's training cutoff.
    Args:
        query: Search query.
    Return:
        Search results.
    """
    return _search.invoke(query)