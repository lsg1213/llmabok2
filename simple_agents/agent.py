from .lambda_agent import LambdaAgent
from .json_input_agent import JsonInputAgent
from .while_agent import WhileAgent

from google.adk.agents import SequentialAgent


root_agent = SequentialAgent(name="root_agent", 
                             sub_agents=[
                                 JsonInputAgent(name="json_agent"),
                                 WhileAgent(name="while_agent", 
                                            condition="number < 50",
                                            sub_agents=[
                                                LambdaAgent(name="increase_agent",
                                                                func=lambda x: x + 1,
                                                                input_keys=['number'],
                                                                output_key="number"),
                                                LambdaAgent(name="square_agent",
                                                                func=lambda x: x**2,
                                                                input_keys=["number"],
                                                                output_key="result")
                                            ])
                             ])

