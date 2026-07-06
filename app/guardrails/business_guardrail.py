from app.config.settings import settings
from app.state.agent_state import ResearchAgentState

def should_stop_for_guardrails(state: ResearchAgentState) -> bool:

    if state.get("tool_call_count", 0) > settings.max_tool_calls:
        return True
    
    if state.get("reflection_count", 0) > settings.max_reflection_loops:
        return True
    
    if state.get("retry_count", 0) > settings.max_retries:
        return True
    
    return False