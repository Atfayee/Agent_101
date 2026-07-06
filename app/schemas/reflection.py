from pydantic import BaseModel, Field

class ReflectionResult(BaseModel):
    approved: bool
    confidence: float = Field(ge=0, le=1)
    comments: list[str] = Field(default_factory=list)
    missing_information: list[str] = Field(default_factory=list)
    revision_reason: str | None = None