from ollama import chat

def generate_chat_response(retrieved_lines, question):
    """
    Generate a chat response using retrieved context and a question.

    Args:
        retrieved_lines (list): List of retrieved text lines with distances.
        question (str): The question to answer.

    Returns:
        str: The generated chat response.
    """
    context = "\n".join(
        [line_with_distance[0] for line_with_distance in retrieved_lines]
    )

    SYSTEM_PROMPT = """
    Human: You are an AI assistant. You are able to find answers to the questions from the contextual passage snippets provided.
    """
    USER_PROMPT = f"""
    Use the following pieces of information enclosed in <context> tags to provide an answer to the question enclosed in <question> tags.
    <context>
    {context}
    </context>
    <question>
    {question}
    </question>
    """

    response = chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT},
            ],
        )

    return response["message"]["content"]