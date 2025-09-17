from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
    instruction='사용자가 제공한 쿼리를 기반으로 Google 검색을 수행하는 도구를 사용할 수 있는 유용한 검색 도우미입니다. 주어진 질문에 따라 적절한 도구를 사용하여 답변하십시오.',
    tools=[google_search],
)
