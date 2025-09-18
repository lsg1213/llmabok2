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
    
    print('일상적인 대화를 하는 에이전트입니다.')
    print('대화를 시작하세요. 종료하려면 exit 또는 quit을 입력하세요.')
    print('새로운 대화를 시작하려면 "new"를 입력하세요.')
    while True:
        user_input = input('input?\n')
        if user_input.lower() in {"exit", "quit"}:
            break
        elif user_input.lower() == "new":
            session = await runner.session_service.get_session(app_name=root_agent.name, user_id="TESTER", session_id=session.id)
            await runner.memory_service.add_session_to_memory(session)

            for event in session.events:
                print('=' * 80)
                print(f'{event.author}: {event.content}')

            session = await runner.session_service.create_session(app_name=root_agent.name, 
                                                            user_id="TESTER", session_id=session.id)
            
            print('-' * 10 + "새로운 대화를 시작합니다." + '-' * 10)
            continue
        
        for event in runner.run(user_id=session.user_id, session_id=session.id, new_message=UserContent(user_input)):
            if event.is_final_response():
                print(f'Agent: {event.content.parts[0].text.strip()}')

    session = await runner.session_service.get_session(app_name=root_agent.name, user_id="TESTER", session_id=session.id)
    await runner.memory_service.add_session_to_memory(session)


asyncio.run(main())