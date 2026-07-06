from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from app.agents.research_agent import ResearchAgent
from app.observability.tracing import print_tracing_status

def main():
    load_dotenv()
    print_tracing_status()

    agent = ResearchAgent()

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Research why reliability matters in enterprise LangGraph agents."
                )
            ],
            "tool_call_count": 0,
            "retry_count": 0,
            "reflection_count": 0,
            "research_results": [],
            "guardrail_errors": []
        }
    )

    print("\nFINAL ANSWER:")
    print(result.get("final_answer"))

    print("\nGROUNDING:")
    print(result.get("grounding_result"))

    print("\nREFLECTION:")
    print(result.get("reflection_result"))

if __name__ == "__main__":
    main()