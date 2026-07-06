# Enterprise Research Agent

This project is a production-style LangGraph Research Agent built from:

- Chapter 1: Enterprise ReAct Agent
- Chapter 2: Agent Reliability

## Features

- Structured state
- Tool calling
- Tool error handling
- Retry and backoff
- Input guardrails
- Business guardrails
- Grounding evaluation
- Reflection review
- LangSmith observability support
- Chapter 3 multi-agent ready architecture

## Run

```bash
pip install -r requirements.txt
cp .env.example .env
python -m app.main