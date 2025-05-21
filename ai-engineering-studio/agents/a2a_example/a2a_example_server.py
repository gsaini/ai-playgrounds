import asyncio
import uvicorn
from a2a.server.agent_execution import AgentExecutor, EventQueue, RequestContext
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCard,
    AgentCapabilities,
    AgentSkill,
    Message,
)
from a2a.utils import new_agent_text_message

# 2. Agent Skill
echo_skill = AgentSkill(
    id="echo_skill",
    name="Echoes the input",
    description="A simple skill that takes a text message and returns it.",
    tags=["echo", "example"],
    examples=["echo hello", "say something"],
    input_modes=["text/plain"],
    output_modes=["text/plain"],
)

# 3. Agent Card
echo_agent_card = AgentCard(
    name="EchoAgent",
    description="A simple A2A agent that echoes text messages.",
    url="http://localhost:8008/",
    version="0.1.0",
    default_input_modes=["text/plain"],
    default_output_modes=["text/plain"],
    capabilities=AgentCapabilities(streaming=False),
    skills=[echo_skill],
)

# 4. Agent Logic
class EchoAgentLogic:
    async def echo(self, text: str) -> str:
        return text

# 5. Agent Executor
class EchoAgentExecutor(AgentExecutor):
    def __init__(self):
        self.logic = EchoAgentLogic()

self.logic = EchoAgentLogic()

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        try:
            text_to_echo = context.request.params.message.parts[0].text
            echoed_text = await self.logic.echo(text_to_echo)
            response_message = new_agent_text_message(echoed_text)
            event_queue.put_nowait(response_message)
        except IndexError:
            error_message = new_agent_text_message("Error: No message parts found.")
            event_queue.put_nowait(error_message)
        except Exception as e:
            error_message = new_agent_text_message(f"An error occurred: {str(e)}")
            event_queue.put_nowait(error_message)
        finally:
            event_queue.put_nowait(None)  # Signal end of events

    async def cancel(self):
        raise NotImplementedError("Cancel not supported")
        text_to_echo = context.request.params.message.parts[0].text
        echoed_text = await self.logic.echo(text_to_echo)
        response_message = new_agent_text_message(echoed_text)
        event_queue.put_nowait(response_message)
        event_queue.put_nowait(None)  # Signal end of events

event_queue.put_nowait(None)  # Signal end of events

    async def cancel(self):
        # TODO: Implement basic cancellation mechanism
        print("Cancellation requested, but not implemented yet.")

# 6. Server Setup
if __name__ == "__main__":
        raise NotImplementedError("Cancel not supported")

# 6. Server Setup
if __name__ == "__main__":
    executor = EchoAgentExecutor()
    request_handler = DefaultRequestHandler(
        executor=executor, task_store=InMemoryTaskStore()
    )
    app = A2AStarletteApplication(
        agent_card=echo_agent_card, request_handler=request_handler
    )
    uvicorn.run(app.build(), host="0.0.0.0", port=8008)
