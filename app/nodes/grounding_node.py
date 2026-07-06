from app.state.agent_state import ResearchAgentState
from app.evaluators.grounding import evaluate_grounding
from app.config.settings import settings

def grounding_node(state: ResearchAgentState) -> ResearchAgentState:

    result = evaluate_grounding(
        answer=state['draft_answer'],
        research_results=state['research_results'],
        min_score=settings.min_grounding_score
    )

    return {
        "grounding_result": result
    }