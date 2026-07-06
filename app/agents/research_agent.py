from graph import build_research_graph

class ResearchAgent:
    def __init__(self):
        self.graph = build_research_graph()

    def invoke(self, state: dict) -> dict:
        return self.graph.invoke(state)