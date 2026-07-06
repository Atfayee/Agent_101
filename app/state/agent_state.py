from typing import TypedDict, Annotated

from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages

from app.state.reducers import append_list
from app.schemas.research import ResearchResult
from app.schemas.grounding import GroundingResult
from app.schemas.reflection import ReflectionResult



class ResearchAgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

    research_results: Annotated[list[ResearchResult], append_list]

    draft_answer: str
    final_answer: str

    tool_call_count: int
    retry_count: int
    reflection_count: int

    grounding_result: GroundingResult
    reflection_result: ReflectionResult

    guardrail_errors: Annotated[list[str], append_list]
