from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from app.state.agent_state import ResearchAgentState
from app.nodes.research_node import research_node
from app.nodes.reflection_node import reflection_node
from app.nodes.grounding_node import grounding_node
from app.nodes.final_node import final_node
from app.guardrails.input_guardrail import input_guardrail_node
from app.guardrails.business_guardrail import should_stop_for_guardrails
from app.config.settings import settings
from app.tools.research_tools import research_tools
from app.tools.errors import format_tool_error


def route_after_input_guardrail(state: ResearchAgentState) -> str:
    if should_stop_for_guardrails(state=state):
        return "final"
    return "research"

def route_after_research(state: ResearchAgentState) -> str:
    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"
    
    return "grounding"

def route_after_reflection(state: ResearchAgentState) -> str:
    reflection = state.get("reflection_result")

    if not reflection:
        return "final"
    
    if not reflection.approved:
        return "final"
    
    if state.get("reflection_count", 0) >= settings.max_reflection_loops:
        return "final"
    
    return "research"

def build_research_graph():

    builder = StateGraph(ResearchAgentState)

    builder.add_node(
        "input_guardrail",
        input_guardrail_node
    )

    builder.add_node(
        "research",
        research_node
    )

    builder.add_node(
        "tools",
        ToolNode(
            tools=research_tools,
            handle_tool_errors=format_tool_error
        )
    )

    builder.add_node(
        "reflection",
        reflection_node
    )

    builder.add_node(
        "grounding",
        grounding_node
    )

    builder.add_node(
        "final",
        final_node
    )

    builder.set_entry_point(
        "input_guardrail"
    )

    builder.add_conditional_edges(
        "input_guardrail",
        route_after_input_guardrail,
        {
            "final": "final",
            "research": "research"
        }
    )

    builder.add_conditional_edges(
        "research",
        route_after_research,
        {
            "tools": "tools",
            "grounding": "grounding"
        }
    )

    builder.add_edge("tools", "research")

    builder.add_edge("grounding", "reflection")

    builder.add_conditional_edges(
        "reflection",
        route_after_reflection,
        {
            "final": "final",
            "research": "research"
        }
    )

    builder.add_edge(
        "final",
        END
    )

    return builder.compile()