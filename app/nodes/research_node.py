from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

from app.config.settings import settings
from app.tools.research_tools import research_tools
from app.state.agent_state import ResearchAgentState
from app.prompts.research import RESEARCH_SYSTEM_PROMPT


llm = ChatOpenAI(
    model=settings.openai_model,
    temperature=settings.temperature
)

llm_with_tools = llm.bind_tools(research_tools)

def research_node(state: ResearchAgentState) -> ResearchAgentState:

    messages = [
        SystemMessage(content=RESEARCH_SYSTEM_PROMPT),
        *state["messages"]
    ]

    response = llm_with_tools.invoke(messages)

    update: ResearchAgentState = {
        "messages": [response]
    }

    if getattr(response, "tool_calls", None):

        update["tool_call_count"] = state.get("tool_call_count", 0) + len(response.tool_calls)

    else:
        update["draft_answer"] = response.content

    return update