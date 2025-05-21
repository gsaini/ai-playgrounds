import asyncio
import uuid
import httpx
from a2a.client import A2AClient
from a2a.types import MessageSendParams

async def main():
    async with httpx.AsyncClient() as httpx_client:
        client = await A2AClient.get_client_from_agent_card_url(
            httpx_client, "http://localhost:8008/"
        )

        message_text = "Hello A2A Echo Agent!"
        send_message_payload = {
            "message": {
                "role": "user",
                "parts": [{"type": "text", "text": message_text}],
                "messageId": uuid.uuid4().hex,
            }
        }
        request = MessageSendParams(**send_message_payload)
        response = await client.send_message(request)
        print("Server response:", response.model_dump_json(exclude_none=True))

if __name__ == "__main__":
    asyncio.run(main())
