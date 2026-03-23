"""
pdf_reader.py

Responsible for extracting raw text from PDF files using PyPDF.
This is the first step in the pipeline, converting a PDF document
into plain text that can be processed further.

"""

from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_file: A file path or file-like object (e.g., from Streamlit upload)

    Returns:
        str: The combined text extracted from all pages of the PDF
    """

    reader = PdfReader(pdf_file)

    text = ""

    # Iterate through each page and extract text
    for page in reader.pages:
        page_text = page.extract_text()

        # Ensure page contains extractable text
        if page_text:
            text += page_text

    return text