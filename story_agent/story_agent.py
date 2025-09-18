from typing_extensions import override
from typing import AsyncGenerator, Optional
from google.adk.agents import BaseAgent, InvocationContext
from google.adk.events import Event

class StoryAgent(BaseAgent):
    """
    Custom agent to orchestrate a story generation workflow.
    This agent runs a sequence of sub-agents to generate, critique, and refine a story.
    The process stops if the critic agent returns "No major issues found."
    """
    generator: BaseAgent
    critic: BaseAgent
    reviser: BaseAgent

    max_iterations: Optional[int] = None
    is_stop_critic: Optional[str] = 'false'

    @override
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        async for event in self.generator.run_async(ctx):
            yield event

        for _ in range(self.max_iterations):
            async for event in self.critic.run_async(ctx):
                yield event

            criticism = ctx.session.state['criticism']
            if self.is_stop_critic == criticism.lower().replace('*', '').strip():
                return

            async for event in self.reviser.run_async(ctx):
                yield event


