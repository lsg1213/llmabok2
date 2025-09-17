from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="country_agent",
    model="gemini-2.0-flash",
    instruction="사용자의 {country}에 관한 질문에 답하세요.",
    tools=[google_search],
)
