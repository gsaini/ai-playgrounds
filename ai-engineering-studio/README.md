# AI Engineering Studio


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)
![DuckDuckGo](https://img.shields.io/badge/duckduckgo-de5833?style=for-the-badge&logo=duckduckgo&logoColor=white)

This directory contains projects focused on building AI agents and tools for advanced engineering use cases. Each project demonstrates the integration of AI models with custom tools and protocols.

## Projects

### 1. **MCP Agent**
- **Description**: Implements an MCP (Model Context Protocol) agent using the `agno` library to interact with language models and tools like `DuckDuckGoTools`.
- **Features**:
  - Real-time tool calls for fetching external data.
  - Stateless design with markdown-formatted responses.
  - Future enhancements include memory integration and improved user interaction.
- **How to Run**:
  - Install dependencies from `requirements.txt`.
  - Run the `agent.py` script.
  - Modify the query in the script to test different scenarios.
- **Assets**:
  - Example output in `mcp_agent_output.png`.

### 2. **Multi-Tool Agent**
- **Description**: Demonstrates the use of Google ADK (Agent Development Kit) to build AI agents capable of performing tasks using custom tools like `get_weather` and `get_current_time`.
- **Features**:
  - Integration with Google ADK and Gemini Model.
  - Custom tools for weather and time information.
  - Future enhancements include memory integration and advanced features like voice and video streaming.
- **How to Run**:
  - Set up a virtual environment and install dependencies from `requirements.txt`.
  - Update the API key in the `.env` file.
  - Run the agent using the ADK Dev UI.
- **Assets**:
  - Workflow diagrams and screenshots in `assets/`.
  - Tests for tools in `tests/`.

### 3. **Optical Character Recognition (OCR)**
- **Description**: Leverages the Gemma-3 model to extract structured text from images.
- **Features**:
  - Advanced text and visual reasoning capabilities.
  - Supports over 140 languages for global applications.
  - Outputs structured Markdown for clear and concise results.
- **How to Run**:
  - Install dependencies from `requirements.txt`.
  - Run the `app.py` script using Streamlit.
  - Upload an image and extract text interactively.
- **Assets**:
  - Static assets like `gemma3.png` in `assets/`.

### 4. **Web URL Scraper**
- **Description**: A tool designed to scrape and extract structured data from web pages using BeautifulSoup and Requests libraries.
- **Features**:
    - Extracts metadata, headings, and main content from web pages.
    - Handles dynamic content using Selenium for JavaScript-heavy websites.
    - Outputs data in JSON or Markdown format for easy integration.
- **How to Run**:
    - Install dependencies from `requirements.txt`.
    - Update the target URL in the `scraper.py` script.
    - Run the script to fetch and process the web page content.
- **Assets**:
    - Example output files in `outputs/`.
    - Screenshots and logs in `assets/`.


## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to improve the projects.