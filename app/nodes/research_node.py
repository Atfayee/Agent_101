from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from app.tools.research_tools import search_research_source
from app.prompts import ENTERPRISE_RESEARCH_SYSTEM_PROMPT
from app.state import ResearchAgentState

tools = [search_research_source]

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

llm_with_tools = llm.bind_tools(tools)

def research_node(state: ResearchAgentState) -> ResearchAgentState:
    
    messages = [
        SystemMessage(content=ENTERPRISE_RESEARCH_SYSTEM_PROMPT), 
        *state["messages"]
    ]
    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }