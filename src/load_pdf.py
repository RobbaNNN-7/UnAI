from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os 

def get_chunks(pdf_path):
    # Ensure the pdf_path is valid and not empty
    if not pdf_path:
        raise ValueError("ERROR: PDF path is empty or invalid!")

    loader = PyPDFLoader(pdf_path)  # Pass pdf_path to the loader
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(document)

    return chunks

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(current_dir,"books","UG-Student-Handbook.pdf")
print(get_chunks(file_path))