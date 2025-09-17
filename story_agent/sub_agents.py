from google.adk.agents import Agent
from google.adk.tools import exit_loop

GEMINI_MODEL = "gemini-2.0-flash"

def is_no_criticism(criticism: str) -> bool:
    return criticism.strip().lower() == "false"

initial_writer_agent = Agent(
    name="InitialWriterAgent",
    model=GEMINI_MODEL,
    output_key="story",
    # instruction="당신은 창의적인 삼행시를 만드는 작가입니다. 사용자 입력을 기반으로 아주 웃긴 삼행시를 작성해 주세요.",
    instruction="당신은 창의적인 이야기를 만드는 작가입니다. 사용자 입력을 기반으로 흥미로운 이야기를 작성해 주세요.",
)

critic_agent = Agent(
    name="CriticAgent",
    model=GEMINI_MODEL,
    output_key="criticism",
    # instruction="""당신은 삼행시의 비평가입니다. 비판적으로 삼행시를 읽고, 개선할 점을 하나하나 개조식으로 지적해 주시고 markdown 형식으로 반환해주세요. 이 때에 삼행시 형식이 지켜졌는지도 꼭 확인해주세요.
    #                한국어가 아닌 다른 언어로 작성되었다면 해당 부분도 지적해주세요.
    #                만약 삼행시가 충분히 좋다면, **false**를 반환하세요.
    #                이야기: {story}""",
    instruction="""당신은 이야기의 비평가입니다. 비판적으로 이야기를 읽고, 개선할 점을 하나하나 개조식으로 지적해 주시고 markdown 형식으로 반환해주세요.
                   만약 이야기가 충분히 좋다면, **false**를 반환하세요.
                   이야기: {story}""",
    tools=[is_no_criticism],
)

refiner_agent = Agent(
    name="RefinerAgent",
    model=GEMINI_MODEL,
    output_key="story",
    tools=[exit_loop],
    # instruction="""당신은 삼행시를 다듬는 전문가입니다. **criticism 변수가 false가 아니라면, 비평가의 의견을 반영하여 삼행시를 개선해 주세요**. 
    #                비평가의 의견: {criticism}
    #                만약 {criticism}이 false라면, 'exit_loop' 도구를 사용하여 루프를 종료하세요.""",
    instruction="""당신은 이야기를 다듬는 전문가입니다. **criticism 변수가 false가 아니라면, 비평가의 의견을 반영하여 이야기를 개선해 주세요**. 
                   비평가의 의견: {criticism}
                   만약 {criticism}이 false라면, 'exit_loop' 도구를 사용하여 루프를 종료하세요.""",
)
