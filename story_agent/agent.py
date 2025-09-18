from google.adk.agents import SequentialAgent, LoopAgent
from .sub_agents import initial_writer_agent, critic_agent, refiner_agent


refiner_critic_loop_agent = LoopAgent(
    name="loop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=5,
)

root_agent = SequentialAgent(
    name="sequential",
    sub_agents=[initial_writer_agent, refiner_critic_loop_agent])

# root_agent = initial_writer_agent
from .story_agent import StoryAgent
root_agent = StoryAgent(name='story_agent',
                        generator=initial_writer_agent,
                        reviser=refiner_agent,
                       critic=critic_agent,
                       max_iterations=5,
                       is_stop_critic='false')