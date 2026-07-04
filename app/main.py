from langchain_core.messages import HumanMessage
from app.graph import build_graph

def main():
    graph = build_graph()

    result = graph.invoke(
        {
            "messages": HumanMessage(
                content="Search docs about LangGraph reliability"
            )
        }
    )

    for message in result["messages"]:
        print(message.type.upper())
        print(message.content)
        print("-" * 80)

if __name__ == "__main__":
    main()