import ollama

def emb_text(text):
    """
    Generates an embedding vector for the given text using the specified model.

    This function utilizes the `ollama.embeddings` method to compute a high-dimensional
    embedding representation of the input text. The embedding can be used for various 
    natural language processing tasks such as semantic similarity, clustering, or as 
    input to machine learning models.

    Args:
        text (str): The input text for which the embedding is to be generated.

    Returns:
        list[float]: A list of floating-point numbers representing the embedding vector 
        of the input text.

    Raises:
        KeyError: If the response from the `ollama.embeddings` method does not contain 
        the "embedding" key.
        Exception: If there is an issue with the `ollama.embeddings` call or the model 
        specified.

    Note:
        - The function uses the "mxbai-embed-large" model for generating embeddings.
        - Ensure that the `ollama` library is properly configured and the model is 
          available before calling this function.
    """
    response = ollama.embeddings(model="mxbai-embed-large", prompt=text)
    return response["embedding"]