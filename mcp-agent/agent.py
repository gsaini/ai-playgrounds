import os
import asyncio

from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.ollama import Ollama

async def run_agent(message: str) -> None:
    # Initialize the agent
    agent = Agent(
        tools=[DuckDuckGoTools(fixed_max_results=5)],
        model=Ollama(id="llama3.2"),
        show_tool_calls=True,
        markdown=True,
        memory=None,
    )

    # Run the agent with the provided message
    agent.print_response(message, stream=True)
    
if __name__ == "__main__":
    # Run the agent with asyncio
    # asyncio.run(run_agent('Find the current weather in New York City & on the basis of response please suggest what to wear?'))

    asyncio.run(run_agent('Find the weather in New York City for next 10 days & on the basis of response please suggest what is the best time to visit New York City?'))