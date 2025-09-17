from typing_extensions import override
from typing import AsyncGenerator, Optional
from google.adk.agents import BaseAgent, InvocationContext
from google.adk.events import Event
from google.adk.events.event_actions import EventActions


def fibonacci(f: list[int]) -> list[int]:
    if f is None:
        f = [0, 1]
    else:
        f.append(f[-1] + f[-2])
    return f

class WhileAgent(BaseAgent):
    """
    Custom agent to orchestrate a workflow with a condition.
    This agent runs to make fibonacci numbers while a specified condition is met.
    """
    condition: str

    @override
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        # ctx.session.state: Dict[str, Any] = {"number": 0, "result": []}
        result = []
        max_len = ctx.session.state['number']
        while len(result) < max_len:
            result = fibonacci(result)
        actions = EventActions(state_delta={"result": result})
        yield Event(author=self.name, invocation_id=ctx.invocation_id, actions=actions)


# class WhileAgent(BaseAgent):
#     """
#     Custom agent to orchestrate a workflow with a condition.
#     This agent runs a sequence of sub-agents while a specified condition is met.
#     """
#     condition: str
#     max_iterations: Optional[int] = None

#     @override
#     async def _run_async_impl(
#         self, ctx: InvocationContext
#     ) -> AsyncGenerator[Event, None]:
#         while eval(self.condition, {}, ctx.session.state):
#             for agent in self.sub_agents:
#                 async for event in agent.run_async(ctx):
#                     yield event
#         yield Event(author=self.name, invocation_id=ctx.invocation_id)

