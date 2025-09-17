import dotenv
dotenv.load_dotenv()

from agent import root_agent

import asyncio
from google.adk.runners import InMemoryRunner
from google.genai.types import UserContent

async def main():
    runner = InMemoryRunner(agent=root_agent, app_name=root_agent.name)

    session = await runner.session_service.create_session(app_name=root_agent.name, 
                                                            user_id="TESTER")
    while True:
        print('국가에 대한 정보를 제공하는 agent입니다.')
        print('궁금한 국가 이름을 입력하세요. 종료하려면 exit 또는 quit을 입력하세요.')
        user_country = input('국가는?\n')
        if user_country.lower() in {"exit", "quit"}:
            break
        
        for event in runner.run(user_id=session.user_id, session_id=session.id, new_message=UserContent(user_country)):
            if event.is_final_response():
                print(event.content.parts[0].text.strip())

    session = await runner.session_service.get_session(app_name=root_agent.name, user_id="TESTER", session_id=session.id)
    print(session.events)
    capital: dict = session.state['output']
    capital = capital.get('capital')
    if capital:
        print(f"마지막으로 조회한 수도: {capital}")

asyncio.run(main())