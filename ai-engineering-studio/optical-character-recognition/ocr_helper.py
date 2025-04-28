import ollama

def process_ocr(image_bytes):
    """
    Processes an image to extract readable text content using the Gemma-3 model.

    This function sends the provided image bytes to the Gemma-3 model via the Ollama API.
    The model analyzes the image and extracts all readable text content, returning it
    in a structured Markdown format. The output is designed to be clear, concise, and
    well-organized, with proper formatting such as headings, lists, or code blocks
    where necessary.

    Args:
        image_bytes (bytes): The binary content of the image to be processed.

    Returns:
        str: The extracted text content in Markdown format.
    """
    user_message = {
        'role': 'user',
        'content': (
            "Analyze the text in the provided image. Extract all readable content "
            "and present it in a structured Markdown format that is clear, concise, "
            "and well-organized. Ensure proper formatting (e.g., headings, lists, or "
            "code blocks) as necessary to represent the content effectively."
        ),
        'images': [image_bytes]
    }
    response = ollama.chat(
        model='gemma3:12b',  # Specify the model to use
        messages=[user_message]
    )
    return response.message.content