from google.adk.agents import Agent
from google.adk.tools import AgentTool

summarizer = Agent(
    name="summarizer",
    model="gemini-2.0-flash",
    description="Agent to summarize text",
    instruction="주어진 내용을 간결하게 요약하십시오.",
)

root_agent = Agent(
    name="summary_agent",
    model="gemini-2.0-flash",
    tools=[AgentTool(agent=summarizer)],
    instruction="사용자가 제공한 긴 텍스트를 요약하는 에이전트입니다. 'summarizer' 도구를 사용하여 요약을 생성하십시오.",
)


root_agent = Agent(
    name="summary_agent",
    model="gemini-2.0-flash",
    tools=[summarizer],
    instruction="사용자가 제공한 긴 텍스트를 요약하는 에이전트입니다. 'summarizer' 도구를 사용하여 요약을 생성하십시오.",
)
