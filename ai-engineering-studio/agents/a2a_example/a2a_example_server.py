# examples/helloworld/__main__.py
from agent_executor import HelloWorldAgentExecutor

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore # For task state management
from a2a.types import (
    # ... other imports ...
    AgentCard,
    AgentSkill,
    AgentCapabilities
    # ...
)
import uvicorn

if __name__ == '__main__':
    # ... AgentSkill and AgentCard definition from previous steps ...
    skill = AgentSkill(
        id='hello_world',
        name='Returns hello world',
        description='just returns hello world',
        tags=['hello world'],
        examples=['hi', 'hello world'],
    )

    agent_card = AgentCard(
        name='Hello World Agent',
        description='Just a hello world agent',
        url='http://localhost:9999/',
        version='1.0.0',
        defaultInputModes=['text'],
        defaultOutputModes=['text'],
        capabilities=AgentCapabilities(streaming=True),
        skills=[skill],
    )

    # 1. Request Handler
    request_handler = DefaultRequestHandler(
        agent_executor=HelloWorldAgentExecutor(),
        task_store=InMemoryTaskStore(), # Provide a task store
    )

    # 2. A2A Starlette Application
    server_app_builder = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )

    # 3. Start Server using Uvicorn
    uvicorn.run(server_app_builder.build(), host='0.0.0.0', port=9999)