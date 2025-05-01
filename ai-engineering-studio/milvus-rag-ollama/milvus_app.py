from tqdm import tqdm
import json
import os
from ollama import chat
from ollama import ChatResponse
from pymilvus import MilvusClient
from utils.file_utils import load_text_lines
from utils.milvus_utils import create_milvus_collection, insert_data, search_milvus
from utils.chat_utils import generate_chat_response
from utils.embeddings_utils import emb_text

data = []

# Load text lines from markdown files
text_lines = load_text_lines("en/faq/*.md")

# Create embeddings for the text lines
for i, line in enumerate(tqdm(text_lines, desc="Creating embeddings")):
    data.append({"id": i, "vector": emb_text(line), "text": line})

# Initialize Milvus client
milvus_client = MilvusClient(uri="./milvus_demo.db")

# Create a collection in Milvus
collection_name = "my_rag_collection"
create_milvus_collection(milvus_client, collection_name, dimension=1024)

# Insert data into the collection
insert_data(milvus_client, collection_name, data)

# Define the question for retrieval
question = "How is data stored in milvus?"

# Search for relevant text lines in Milvus
query_vector = emb_text(question)
search_res = search_milvus(milvus_client, collection_name, query_vector)


retrieved_lines_with_distances = [
    (res["entity"]["text"], res["distance"]) for res in search_res[0]
]

print(json.dumps(retrieved_lines_with_distances, indent=4))

# Generate a response using the retrieved context
response = generate_chat_response(retrieved_lines_with_distances, question)
print(response)
