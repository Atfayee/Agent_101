from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_model: str = "gpt-4o-mini"
    temperature: float = 0

    max_tool_calls: int = 5
    max_retries: int = 3
    min_grounding_score: float = 0.65
    max_reflection_loops: int = 2

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()