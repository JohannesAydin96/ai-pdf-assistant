"""
rag_pipeline.py

Combines retrieved document chunks with a language model to generate answers.
This file implements the core Retrieval Augmented Generation (RAG) logic.

"""

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (API key)
load_dotenv()

# Initialize OpenAI client
client = OpenAI()


def generate_answer(query, search_results):
    """
    Generates an answer using retrieved context and a language model.

    Args:
        query (str): User's question
        search_results (dict): Results from the vector database search

    Returns:
        str: Generated answer based on the retrieved context
    """

    # Extract relevant chunks from search results
    context_chunks = search_results["documents"][0]

    # Combine chunks into a single context string
    context = "\n\n".join(context_chunks)

    # Construct the RAG prompt
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using only the provided context.
If the answer cannot be found in the context, say:
"The information is not available in the document."

Be clear and concise.

Context:
{context}

Question:
{query}
"""

    # Send request to OpenAI model
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text