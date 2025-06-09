# Basic Chatbot Getting Started

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![LangChain](https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

This is a simple Python chatbot application built using LangGraph, LangChain, and Gemini (Google GenAI) models. It demonstrates how to create a conversational agent with tool integration and streaming responses.

## Features

- **Conversational AI**: Uses Gemini-2.0-flash (Google GenAI) for natural language understanding and response generation.
- **Tool Integration**: Integrates external tools (e.g., TavilySearch) to enhance the chatbot's capabilities.
- **Streaming Responses**: Streams conversation updates for a more interactive experience.
- **Extensible Graph Architecture**: Built with LangGraph's StateGraph for flexible conversation flow.
- **Environment Variable Support**: Uses `python-dotenv` to load environment variables from a `.env` file.

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies.

## Installation

1. **Clone the repository**

   ```zsh
   git clone <your-repo-url>
   cd basic-chatbot-getting-started
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```zsh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```zsh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root and add any required API keys or configuration variables (see the documentation for TavilySearch and Gemini for details).

## Usage

Run the chatbot from your terminal:

```zsh
python main.py
```

You will see a prompt:

```
User: 
```

Type your message and press Enter. The assistant will respond. To exit, type `quit`, `exit`, or `q`.

## Code Structure

- `main.py`: Main application file containing the chatbot logic, graph setup, and streaming loop.
- `requirements.txt`: Python dependencies.

### Key Components

- **StateGraph**: Manages the conversation state and flow.
- **init_chat_model**: Initializes the Gemini chat model.
- **TavilySearch**: Example tool for web search integration.
- **stream_graph_updates**: Handles streaming of conversation updates and prints assistant responses.

## Customization

- Add or modify tools by editing the `tools` list in `main.py`.
- Change the model by updating the `init_chat_model` call.
- Extend the conversation logic by adding new nodes or edges to the `StateGraph`.

## Troubleshooting

- If you see errors about missing environment variables, ensure your `.env` file is set up correctly.
- For dependency issues, double-check your Python version and that all packages in `requirements.txt` are installed.

## License

This project is provided for educational purposes. See the repository for license details.

## Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Google GenAI (Gemini)](https://ai.google.dev/)
- [TavilySearch](https://python.langchain.com/docs/integrations/tools/tavily_search)

---

Feel free to fork and extend this project for your own chatbot experiments!
