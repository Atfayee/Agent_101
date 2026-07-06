
from app.schemas.grounding import GroundingResult
from app.schemas.research import ResearchResult

def evaluate_grounding(
    answer: str,
    research_results: list[ResearchResult],
    min_score: float
) -> GroundingResult:
    
    if not answer:
        return GroundingResult(
            score=0,
            supported=False,
            unsupported_claims=["Empty answer."]
        )
    
    if not research_results:
        return GroundingResult(
            score=0.2,
            supported=False,
            unsupported_claims=["No research evidence available."]
        )
    
    avg_confidence = sum(r.confidence for r in research_results) / len(research_results)

    unsupported: list[str] = []

    source_term = " ".join(
        [r.title + " " + r.summary for r in research_results]
    )

    for sentence in answer:
        sentence = sentence.strip()
        
        if not sentence:
            continue

        keywords = [w.lower() for w in sentence.split() if len(w) > 5]
        if keywords and not any(k in source_term for k in keywords):
            unsupported.append(sentence)

    penalty = min(len(unsupported) * 0.1, 0.4)
    score = max(0, avg_confidence - penalty)

    return GroundingResult(
        score=score,
        supported=score>min_score,
        unsupported_claims=unsupported,
        missing_sources=[]
    )