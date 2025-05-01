import streamlit as st
from utils.milvus_utils import search_milvus
from utils.chat_utils import generate_chat_response
from utils.embeddings_utils import emb_text
from pymilvus import MilvusClient

# Streamlit app configuration
st.set_page_config(page_title="Q&A Chat Application", layout="wide")

# Title and description
st.title("Q&A Chat Application")
st.markdown("This application uses Milvus for vector search and Ollama for generating responses.")

# Milvus setup
collection_name = "my_rag_collection"
milvus_client = MilvusClient(uri="./milvus_demo.db")

# Main chat interface
st.header("Ask a Question")
user_input = st.text_input("Enter your question:", placeholder="Type your question here...")

if st.button("Submit") and user_input:
    with st.spinner("Searching and generating response..."):
        try:
            # Search for relevant text lines in Milvus
            search_res = search_milvus(milvus_client, collection_name, emb_text(user_input))

            retrieved_lines_with_distances = [
                (res["entity"]["text"], res["distance"]) for res in search_res[0]
            ]

            # Generate a response using the retrieved context
            response = generate_chat_response(retrieved_lines_with_distances, user_input)

            # Display the response
            st.markdown("### Response")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")