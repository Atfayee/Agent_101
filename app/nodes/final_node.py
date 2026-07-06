from app.state.agent_state import ResearchAgentState

def final_node(state: ResearchAgentState) -> ResearchAgentState:

    if state["guardrail_errors"]:
        return {
            "final_answer": f"Cannot complete this request because it failed guardrail checks: {state["guardrail_errors"]}"
        }
    
    reflection = state.get("reflection_result")

    if reflection and not reflection.approved:
        return {
            "final_answer": (
                "Cannot produce a sufficiently reliable final answer."
                f"Reason: {reflection.revision_reason}"
                f"Review comments: {"; ".join(reflection.comments)}"
            )
        }
    
    return {
        "final_answer": state.get("draft_answer", "No final answer generated.")
    }