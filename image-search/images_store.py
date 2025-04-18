import os
import ollama

from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document

class ImagesStore:
    embeddings = OllamaEmbeddings(model="llama3.2")
    vector_store = InMemoryVectorStore(embeddings)

    images_directory = "images/"
    document_ids_to_images = {}
    document_ids_to_documents = {}

    # Ensure the image directory exists before uploading images
    os.makedirs(images_directory, exist_ok=True)

    @classmethod
    def upload_images(cls, image):
        """
        Uploads images to the specified image directory and indexes them in the vector store.

        This method takes a list of images, saves them to the local file system in the
        `image_directory`, and then processes them to add their embeddings to the
        in-memory vector store for efficient search and retrieval.

        Args:
            images (list): A list of image objects to be uploaded. Each image object
                          should have a `name` attribute for the file name and a
                          `getbuffer()` method to retrieve the binary content.

        Raises:
            FileNotFoundError: If the `image_directory` does not exist and cannot be created.
        """
        image_path = cls.images_directory + image.name
        with open(image_path, "wb") as f:
            f.write(image.getbuffer())
        
        description = cls._describe_image(image_path)
        document = Document(page_content=description)
        document_id = cls.vector_store.add_documents([document])[0]
        cls.document_ids_to_images[document_id] = image.name
        cls.document_ids_to_documents[document_id] = document

        return document_id


    @classmethod
    def _describe_image(cls, image_path):
        res = ollama.chat(
            model="bakllava", # important: Specify the model to use (should be available in the local machine)
            messages=[
                {
                    'role': 'user',
                    'content': 'Tell me what do you see in this picture in only one sentence. Be concise.',
                    'images': [image_path]
                }
            ],
            options={'temperature': 0}
        )

        return res['message']['content']
    
    @classmethod
    def retrieve_docs_by_query(cls, query):
        """
        Retrieves documents from the vector store based on a similarity search query.

        This method performs a similarity search in the in-memory vector store using the
        provided query and returns the most relevant documents.

        Args:
            query (str): The search query string to find similar documents.

        Returns:
            list: A list of documents that are most similar to the query.
        """
        return cls.vector_store.similarity_search(query, k=1)

    @classmethod
    def get_by_id(cls, doc_id):
        """
        Retrieves a document from the in-memory store using its unique document ID.

        This method fetches the document object associated with the given document ID
        from the `document_ids_to_documents` mapping.

        Args:
            doc_id (str): The unique identifier of the document to retrieve.

        Returns:
            Document: The document object associated with the given ID.
        """
        return cls.document_ids_to_documents[doc_id]

    @classmethod
    def get_image_path_by_id(cls, doc_id):
        """
        Retrieves the file path of an image using its associated document ID.

        This method fetches the file path of the image associated with the given document ID
        from the `document_ids_to_images` mapping.

        Args:
            doc_id (str): The unique identifier of the document associated with the image.

        Returns:
            str: The file path of the image associated with the given document ID.
        """
        return cls.images_directory + cls.document_ids_to_images[doc_id]
