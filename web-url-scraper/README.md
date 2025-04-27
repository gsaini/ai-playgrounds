# Web URL Scraper

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

## Overview
The Web URL Scraper is a Streamlit-based application designed to scrape and analyze web pages. It leverages LangChain components and Selenium to extract and process data from web pages, providing users with insights and analysis in an interactive UI.

## Features
- **Web Scraping**: Uses Selenium to extract data from web pages.
- **Data Analysis**: Embeds and stores vectors for document analysis.
- **Interactive UI**: Allows users to input URLs and view results interactively.

## Requirements
- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd web-url-scraper
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run web_url_scraper.py
   ```
2. Enter a URL in the input field to scrape and analyze the web page.

## Future Enhancements
- Add support for scraping multiple URLs simultaneously.
- Integrate additional analysis tools for richer insights.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.