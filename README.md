# AI Playgrounds

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![mlflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

Welcome to **AI Playgrounds**, a repository created to explore, experiment, and prototype Proof of Concepts (POCs) around AI tools and technologies using Python. This repository serves as a dynamic space for quick experimentation and learning in the ever-evolving field of Artificial Intelligence.

## Objectives
- **Experimentation**: Test and build quick POCs around AI tools, frameworks, and techniques.
- **Learning**: Provide a space for learning, experimenting, and iterating on AI concepts.
- **Expansion**: Continuously expand with new POCs, keeping the repository fresh and relevant.

## Repository Structure

### 1. **Multi-Tool Agent**
- **Description**: Demonstrates the use of Google ADK (Agent Development Kit) to build AI agents capable of performing tasks using custom tools like `get_weather` and `get_current_time`.
- **Features**:
  - Integration with Google ADK and Gemini Model.
  - Custom tools for weather and time information.
  - Future enhancements include memory integration and advanced features like voice and video streaming.
- **How to Run**:
  - Set up a virtual environment and install dependencies.
  - Update the API key in the `.env` file.
  - Run the agent using the ADK Dev UI.

### 2. **MCP Agent**
- **Description**: Implements an MCP (Model Context Protocol) agent using the `agno` library to interact with language models and tools like `DuckDuckGoTools`.
- **Features**:
  - Real-time tool calls for fetching external data.
  - Stateless design with markdown-formatted responses.
  - Future enhancements include memory integration and improved user interaction.
- **How to Run**:
  - Install dependencies and run the `agent.py` script.
  - Modify the query in the script to test different scenarios.

### 3. **Web URL Scraper**
- **Description**: A Streamlit-based application to scrape and analyze web pages using LangChain components.
- **Features**:
  - Uses Selenium for web scraping.
  - Embeddings and vector storage for document analysis.
  - Interactive UI for user input and results display.
- **How to Run**:
  - Install dependencies and run the `web_url_scraper.py` script.
  - Enter a URL in the Streamlit app to scrape and analyze.

### 4. **AI Case Studies**
- **Description**: A collection of AI-based case studies to explore and solve real-world problems using machine learning and data analysis.
- **Current Projects**:
  - **Hotel Booking Cancellation Prediction**:
    - Predicts hotel booking cancellations using machine learning.
    - Features data analysis, visualization, and predictive modeling.
    - Future enhancements include real-time dashboards and automated model retraining.
    - **How to Run**:
      - Install dependencies and run the `main.py` script using Streamlit.
      - Perform EDA and visualize results interactively.
  - **Optical Character Recognition (OCR)**
    - **Description**: Leverages the Gemma-3 model on local machine to extract structured text from images.
    - **Features**:
      - Advanced text and visual reasoning capabilities.
      - Supports over 140 languages for global applications.
      - Outputs structured Markdown for clear and concise results.
    - **Gemma-3 Overview**:
      - Gemma-3 is a cutting-edge AI model optimized for single GPU/TPU usage.
      - Offers a 128k-token context window for handling complex tasks.
      - Supports function calling and structured outputs for building intelligent workflows.
      - Integrates seamlessly with tools like Hugging Face, Ollama, and Google AI Studio.
    - **How to Run**:
      - Install dependencies and run the `app.py` script using Streamlit.
      - Upload an image and extract text interactively.
- **Future Additions**: More AI-based case studies will be added to this directory.

## Contributions
Contributions are warmly welcomed! Whether it's improving existing POCs, adding new experiments, or sharing ideas, your inputs are highly valued. Feel free to open issues or submit pull requests to collaborate.
