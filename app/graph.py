from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from app.state import ResearchAgentState
from app.tools.research_tools import search_research_source
from app.tools.error_handling import format_tool_error
from app.nodes import research_node

tools = [search_research_source]

def route_after_research(state: ResearchAgentState):
    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"
    
    return END

def build_graph():

    builder = StateGraph(ResearchAgentState)

    builder.add_node(
        "research",
        research_node
    )

    builder.add_node(
        "tools",
        ToolNode(
            tools=tools,
            handle_tool_errors=format_tool_error
        )
    )

    builder.set_entry_point(
        "research"
    )

    builder.add_conditional_edges(
        "research",
        route_after_research,
        {
            "tools":"tools",
            END:END
        }
    )

    builder.add_edge(
        "tools",
        "research"
    )

    return builder.compile()