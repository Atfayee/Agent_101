from app.state.agent_state import ResearchAgentState
from app.evaluators.reflection import reflect_on_answer

def reflection_node(state: ResearchAgentState) -> ResearchAgentState:
    
    result = reflect_on_answer(
        state.get("draft_answer"),
        state.get("grounding_result")
    )

    return {
        "reflection_result": result,
        "reflection_count": state.get("reflection_count", 0) + 1
    }