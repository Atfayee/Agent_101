from pydantic import BaseModel, Field

class GroundingResult(BaseModel):
    score: float = Field(ge=0, le=1)
    supported: bool
    unsupported_claims: list[str] = Field(default_factory=list)
    missing_sources: list[str] = Field(default_factory=list)