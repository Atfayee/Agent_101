from pydantic import BaseModel


class AgentMetrics(BaseModel):
    tool_call_count: int = 0
    retry_count: int = 0
    reflection_count: int = 0
    total_tokens: int = 0