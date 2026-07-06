from app.state.agent_state import ResearchAgentState

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "developer message",
]

def input_guardrail_node(state: ResearchAgentState) -> ResearchAgentState:

    messages = state["messages"]

    if not messages:
        return {
            "guardrail_errors": ["No user message found."]
        }
    
    user_text = messages[-1].content

    errors: list[str] = []

    if len(user_text.strip()) < 3:
        errors.append("Input is too short.")

    if len(user_text) > 5000:
        errors.append("Input is too long.")

    for pattern in BLOCKED_PATTERNS:
        if pattern in user_text:
            errors.append(
                f"Potential prompt injection detected: {pattern}"
            )

    return {
        "guardrail_errors": errors
    }