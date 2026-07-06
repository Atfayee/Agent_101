from app.schemas.grounding import GroundingResult
from app.schemas.reflection import ReflectionResult

def reflect_on_answer(
    draft_answer: str,
    grounding_result: GroundingResult | None
) -> ReflectionResult:
    comments: list[str] = []
    missing_information: list[str] = []

    if not draft_answer:
        return ReflectionResult(
            approved=False,
            confidence=0,
            comments=["Draft answer is empty."],
            revision_reason=["No draft answer was generated."]
        )
    
    if grounding_result and not grounding_result.supported:
        comments.append("Draft answer is not sufficient grounded.")
        comments.extend(grounding_result.unsupported_claims)
        return ReflectionResult(
            approved=False,
            confidence=grounding_result.score,
            comments=comments,
            missing_information=missing_information,
            revision_reason="Grounding score below threshold."
        )
    
    if len(draft_answer.split()) < 500:
        comments.append("Answer may be too short for enterprise research response.")
        missing_information.append("More explanation or supporting detail may be needed.")

    approved = not missing_information

    return ReflectionResult(
        approved=approved,
        confidence=grounding_result.score,
        comments=comments,
        missing_information=missing_information,
        revision_reason=None if approved else "Completeness issue."
    )