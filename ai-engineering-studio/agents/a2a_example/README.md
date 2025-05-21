# Simple A2A Echo Example

This example demonstrates a basic Agent2Agent (A2A) protocol interaction using the Python SDK. It consists of a simple "Echo Agent" (server) and a client that communicates with it.

**Important: Python Version Requirement**
This example requires **Python 3.13 or newer** due to the `a2a-sdk` dependency. The environment where this example was generated uses an older Python version, so these scripts could not be run there. Please ensure you have Python 3.13+ if you intend to execute this example.

## Components

1.  **`a2a_example_server.py`**:
    *   Implements the "Echo Agent".
    *   This agent has one skill: to echo back any text message it receives.
    *   It defines an Agent Card to advertise its capabilities.
    *   It runs an HTTP server on `http://localhost:8008`.

2.  **`a2a_example_client.py`**:
    *   Implements a client that connects to the Echo Agent.
    *   It fetches the agent's card, then sends a text message.
    *   It prints the response received from the agent.

## How to Run (in a Python 3.13+ environment)

1.  **Install Dependencies:**
    Open your terminal and ensure your environment has Python 3.13+. Then install the necessary packages:
    ```bash
    pip install "a2a-sdk>=0.0.10" uvicorn httpx
    ```

2.  **Start the Server:**
    In one terminal, navigate to the `ai-engineering-studio/agents/a2a_example` directory and run:
    ```bash
    python a2a_example_server.py
    ```
    The server should start and listen on port 8008.

3.  **Run the Client:**
    In another terminal, navigate to the `ai-engineering-studio/agents/a2a_example` directory and run:
    ```bash
    python a2a_example_client.py
    ```
    The client will send a message to the server and print the echoed response.

## Expected Output (Client)

The client should print a JSON response similar to this (IDs will vary):

```json
{
  "jsonrpc": "2.0",
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "result": {
    "type": "message",
    "role": "agent",
    "parts": [
      {
        "type": "text",
        "text": "Hello A2A Echo Agent!"
      }
    ],
    "messageId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
    "annotations": null
  }
}
```
This demonstrates the server echoing the client's message.
