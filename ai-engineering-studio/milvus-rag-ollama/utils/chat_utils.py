from ollama import chat
import streamlit as st

from utils.milvus_utils import search_milvus
from utils.embeddings_utils import emb_text

from pymilvus import MilvusClient


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
        Use the following pieces of information enclosed in <context> tags to provide an answer to the question enclosed information in <question> tags.
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
        stream=True,
        options={"temperature": 0.0},
    )

    return response


def handle_user_input(prompt):

    # Milvus setup
    collection_name = "my_rag_collection"
    milvus_client = MilvusClient(uri="./milvus_demo.db")

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Searching and generating response..."):
        # Fetch relevant context from Milvus DB
        search_results = search_milvus(milvus_client, collection_name, emb_text(prompt))
        retrieved_lines_with_distances = [
            (res["entity"]["text"], res["distance"]) for res in search_results[0]
        ]

        # Generate response using the retrieved context
        response_stream = generate_chat_response(retrieved_lines_with_distances, prompt)

        # Display assistant response in chat message container
        content_stream = (chunk["message"]["content"] for chunk in response_stream)
        streamed_response = st.chat_message("assistant").write_stream(content_stream)

        # Add assistant response to chat history
        st.session_state.messages.append(
            {"role": "assistant", "content": streamed_response}
        )
