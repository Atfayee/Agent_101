from pydantic import BaseModel, Field


class ResearchResult(BaseModel):
    title: str
    summary: str
    confidence: float = Field(ge=0, le=1)
    url: str
    image: list = Field(default_factory=list)


class ResearchToolOutput(BaseModel):
    query: str
    source: str
    results: list[ResearchResult] = Field(default_factory=list)