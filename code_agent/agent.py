from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = Agent(
    name="code_agent",
    model="gemini-2.0-flash",
    code_executor=BuiltInCodeExecutor(),
    instruction="사용자의 요청을 처리하는 코드를 작성하고, 실행 결과를 알려줘.",
    include_contents='none'
)
