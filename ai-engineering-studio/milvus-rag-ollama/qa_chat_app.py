import streamlit as st
from utils.chat_utils import handle_user_input

# Streamlit app configuration
st.set_page_config(page_title="Q&A Chat Application", layout="wide")

# Title and description
st.title("Q&A Chat Application")
st.markdown("This application uses Milvus for vector search and Ollama for generating responses.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add a sample suggestion from Milvus DB content
sample_suggestions = [
    "How does Milvus handle vector similarity?", 
    "How is data stored in milvus?", 
    "What is the maximum dataset size Milvus can handle?"
]


# Display chat responses in a separate container
response_container = st.container(height=700, border=False)
with response_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# Organize questions and input chat into two rows of a container, with chat responses in a separate container
if sample_suggestions:
    with st.container():
        st.markdown("**Sample Questions:**")
        question_buttons = st.container()
        with question_buttons:
            for suggestion in sample_suggestions:
                if st.button(suggestion, key=suggestion):
                    with response_container:
                        handle_user_input(suggestion)

    with st.container():
        if prompt := st.chat_input("Type your question here..."):
            with response_container:
                handle_user_input(prompt)