"""
app.py

Main entry point for the AI PDF Assistant application.
Handles user interaction, file upload, and connects all components
of the RAG pipeline to generate answers from PDF documents.

"""

import streamlit as st
from src.pdf_reader import extract_text_from_pdf
from src.chunker import chunk_text
from src.vector_store import create_collection, add_chunks_to_collection, search_collection
from src.rag_pipeline import generate_answer


# Configure Streamlit page
st.set_page_config(page_title="AI PDF Assistant", page_icon="📄")

# UI Title and description
st.title("AI PDF Assistant")
st.write("Upload a PDF and ask questions about its content.")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    # Process PDF only once per session
    if "processed" not in st.session_state:
        with st.spinner("Processing PDF..."):
            # Step 1: Extract text from PDF
            text = extract_text_from_pdf(uploaded_file)

            # Step 2: Split text into chunks
            chunks = chunk_text(text)

            # Step 3: Store chunks in vector database
            collection = create_collection()
            add_chunks_to_collection(collection, chunks)

            # Store data in session state to avoid reprocessing
            st.session_state.collection = collection
            st.session_state.processed = True
            st.session_state.chunks = chunks

        st.success("PDF processed successfully.")

    # User input for question
    query = st.text_input("Ask a question about the PDF:")

    if query:
        with st.spinner("Searching document and generating answer..."):
            # Step 4: Retrieve relevant chunks
            results = search_collection(st.session_state.collection, query)

            # Step 5: Generate answer using RAG pipeline
            answer = generate_answer(query, results)

        # Display answer
        st.subheader("Answer")
        st.write(answer)

        # Display retrieved context for transparency
        st.subheader("Retrieved Context")
        for i, chunk in enumerate(results["documents"][0], start=1):
            st.markdown(f"**Chunk {i}:**")
            st.write(chunk)
            st.write("---")