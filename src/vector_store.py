"""
vector_store.py

Handles storage and retrieval of text chunks using a vector database (Chroma).
Each text chunk is converted into an embedding and stored for semantic search.

"""

import chromadb


def create_collection():
    """
    Creates or retrieves a Chroma collection.

    Returns:
        collection: A Chroma collection used to store and query embeddings
    """
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="pdf_chunks")
    return collection


def add_chunks_to_collection(collection, chunks):
    """
    Adds text chunks to the vector database.

    Args:
        collection: Chroma collection
        chunks (list[str]): List of text chunks to store
    """

    # Generate unique IDs for each chunk
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Clear existing data to avoid duplicates when reprocessing PDFs
    try:
        existing = collection.get()
        if existing["ids"]:
            collection.delete(ids=existing["ids"])
    except Exception:
        pass

    # Add chunks to the collection (embeddings are created automatically)
    collection.add(
        documents=chunks,
        ids=ids
    )


def search_collection(collection, query, n_results=3):
    """
    Performs semantic search in the vector database.

    Args:
        collection: Chroma collection
        query (str): User query
        n_results (int): Number of relevant chunks to retrieve

    Returns:
        dict: Search results containing the most relevant documents
    """

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results