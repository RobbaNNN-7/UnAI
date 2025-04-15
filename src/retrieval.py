import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
persistent_directory = os.path.join(parent_dir,"db","Chroma")

def get_context(query):

    # Initializing the Embedding Model
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2" )

    # Initialize Chroma Instance
    db = Chroma(
        embedding_function = embedding_model,
        persist_directory  = persistent_directory
    )

    retrieval_docs = db.as_retriever(search_kwargs = {"k":4})
    context_docs = retrieval_docs.invoke(query)

    return context_docs


