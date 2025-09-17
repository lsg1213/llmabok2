from .lambda_agent import LambdaAgent
from .json_input_agent import JsonInputAgent
from .while_agent import WhileAgent

from google.adk.agents import SequentialAgent


def fibonacci(f: list[int]) -> list[int]:
    if f is None:
        f = [0, 1]
    else:
        f.append(f[-1] + f[-2])
    return f

root_agent = SequentialAgent(name="root_agent", 
                             sub_agents=[
                                 JsonInputAgent(name="json_agent"),
                                 WhileAgent(name="while_agent", 
                                            sub_agents=[
                                                LambdaAgent(name="increase_agent",
                                                                func=fibonacci,
                                                                input_keys=['number'],
                                                                output_key="number"),
                                            ])
                             ])

