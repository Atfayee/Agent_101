from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class ResearchAgentState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

    tool_call_count: int
    retry_count: int

    guardrail_errors: list[str]

    total_tokens: int

    hallucination_score: float | None

    reflection: str | None

    final_answer: str | None