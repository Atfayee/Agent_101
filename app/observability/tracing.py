import os

def print_tracing_status() -> None:
    enabled = os.getenv("LANGSMITH_TRACING", "false")
    project = os.getenv("LANGSMITH_PROJECT", "default")

    print(f"LangSmith tracing: {enabled}")
    print(f"LangSmith project: {project}")