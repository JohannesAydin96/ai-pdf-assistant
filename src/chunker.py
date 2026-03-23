"""
chunker.py

Responsible for splitting large text into smaller overlapping chunks.
This is necessary because language models have input size limitations
and perform better with smaller, context-preserving text segments.

"""


def chunk_text(text, chunk_size=500, overlap=50):
    """
    Splits text into smaller overlapping chunks.

    Args:
        text (str): The full text to be split
        chunk_size (int): Maximum size of each chunk (in characters)
        overlap (int): Number of overlapping characters between chunks

    Returns:
        list[str]: A list of text chunks
    """

    chunks = []

    start = 0
    text_length = len(text)

    # Loop through the text and create chunks
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        # Move start forward while keeping overlap
        start += chunk_size - overlap

    return chunks