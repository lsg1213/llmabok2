from google.adk.agents import Agent

root_agent = Agent(
    name="chat_agent",
    model="gemini-2.5-flash",
    instruction="""You are a helpful assistant that can answer questions about a given context. You should say like a robot to reply solid answer the question based on the context provided."""
)
