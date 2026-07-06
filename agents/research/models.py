from pydantic import BaseModel, Field

class ResearchResult(BaseModel):
    """
    Final structured output produced by the Research Agent.
    """
    summary: str = Field(
        description="A concise summary of the research findings."
    )

    sources: list[str] = Field(
        default_factory=list,
        description="URLs or names of information sources used."
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1."
    )

    keywords: list[str] = Field(
        default_factory=list,
        description="Important keywords extracted from the research."
    )