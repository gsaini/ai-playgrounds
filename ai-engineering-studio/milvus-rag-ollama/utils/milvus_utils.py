from pymilvus import Collection

def create_milvus_collection(client, collection_name, dimension):
    """
    Create a Milvus collection with the specified name and dimension.

    Args:
        client (MilvusClient): The Milvus client instance.
        collection_name (str): Name of the collection to create.
        dimension (int): Dimension of the vectors to store.
    """

    if client.has_collection(collection_name):
        client.drop_collection(collection_name)

    client.create_collection(
        collection_name,
        dimension=1024,
        metric_type="IP",  # Inner product distance
        consistency_level="Strong",  # Supported values are (`"Strong"`, `"Session"`, `"Bounded"`, `"Eventually"`). See https://milvus.io/docs/consistency.md#Consistency-Level for more details.
    )

def insert_data(client, collection_name, data):
    """
    Insert data into a Milvus collection.

    Args:
        client (MilvusClient): The Milvus client instance.
        collection_name (str): Name of the collection to insert data into.
        data (list): List of data dictionaries to insert.
    """
    client.insert(collection_name, data)

def search_milvus(client, collection_name, query_vector):
    """
    Search for similar vectors in a Milvus collection.

    Args:
        client (MilvusClient): The Milvus client instance.
        collection_name (str): Name of the collection to search.
        query_vector (str): embed query vector

    Returns:
        list: Retrieved results with distances.
    """
    results = client.search(
        collection_name=collection_name,
        data=[query_vector],
        limit=3,
        search_params={"metric_type": "IP", "params": {}},  # Inner product distance
        output_fields=["text"],  # Return the text field
    )
    return results