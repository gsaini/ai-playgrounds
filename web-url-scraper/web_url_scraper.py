import streamlit as st

# Importing necessary modules from LangChain for vector storage, embeddings, and LLMs
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

# Initialize the language model and embeddings using the Ollama LLM
model = OllamaLLM(model="llama3.2")
embeddings = OllamaEmbeddings(model="llama3.2")

# Create an in-memory vector store to store document embeddings
vector_store = InMemoryVectorStore(embeddings)

# Streamlit UI setup
st.title("Web URL Scraper")  # Display the title of the application
url = st.text_input("Enter a URL to scrape:")  # Input field for the user to enter a URL


def load_page(url):
    """
    Loads the content of a given URL using Selenium.

    Args:
        url (str): The URL to load.

    Returns:
        list: A list of documents containing the content of the loaded URL.
    """
    loader = SeleniumURLLoader(urls=[url])  # Initialize the Selenium URL loader with the given URL
    documents = loader.load()  # Load the content of the URL
    return documents

def split_text(documents):
    """
    Splits the input text into smaller chunks based on the specified chunk size and overlap.

    This function uses the RecursiveCharacterTextSplitter to divide the input text into
    manageable chunks. Each chunk has a maximum size defined by `chunk_size` and overlaps
    with the next chunk by a specified number of characters (`chunk_overlap`). The start
    index of each chunk can also be included in the output.

    Args:
        documents (str): The input text to be split into chunks.

    Returns:
        list: A list of text chunks with optional start indices.
    """
    text_spiltter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Maximum size of each text chunk
        chunk_overlap=200,  # Overlap between consecutive chunks
        add_start_index=True  # Include the start index of each chunk
    )
    data = text_spiltter.split_documents(documents)  # Split the documents into chunks
    return data

def index_docs(documents):
    """
    Indexes the documents into the vector store.

    This function takes chunked documents as input and adds them to the vector store.

    Args:
        documents (list): The chunked documents to be indexed.
    """
    vector_store.add_documents(documents)

template = """
        You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
        Question: {question} 
        Context: {context} 
        Answer:
    """

def answer_question (question, context):
    def answer_question(question, context):
        """
        Generates an answer to a given question based on the provided context using a language model.

        This function utilizes a chat prompt template and a language model to process the input
        question and context, and returns a generated response.

        Args:
            question (str): The question to be answered.
            context (str): The context or background information relevant to the question.

        Returns:
            str: The generated answer to the question based on the context.
        """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    return chain.invoke({"question": question, "context": context})  # Generate an answer using the language model

if url:
    # If a URL is provided, load the page and process it
    # Main workflow
    # Load the web page content from the provided URL
    documents = load_page(url)

    # Split the loaded documents into smaller chunks
    chunked_documents = split_text(documents)

    # Index the chunked documents into the vector store
    index_docs(chunked_documents)
 
    # Notify the user that the documents have been successfully loaded and indexed
    st.write("Documents loaded and indexed successfully!")

question = st.text_input("Ask a question about the content:")  # Input field for the user to ask a question

if question:
    st.chat_message("user").write(question)  # Display the user's question in the chat
    retrieve_documents = vector_store.similarity_search(question)  # Retrieve relevant documents from the vector store
    
    context = "\n\n".join([doc.page_content for doc in retrieve_documents])
    answer = answer_question(question, context)  # Generate an answer using the language model
    st.chat_message("assistant").write(answer)  # Display the generated answer in the chat