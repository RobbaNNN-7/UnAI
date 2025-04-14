import os 
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Loading File Paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
file_path = os.path.join(parent_dir,"books","UG-Student-Handbook.pdf")
persistent_directory = os.path.join(parent_dir,"Chroma","db")


if not (os.path.exists(persistent_directory)):
    print("Initializing Splitting and Chunking the Document")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could Not Find {file_path}. Does Not Exist?")
    
    # Loading the Document
    loader = PyPDFLoader(file_path)
    document = loader.load()

    # Splitting the Documents into Chunks
    textSplitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 200)
    chunk = textSplitter.split_documents(document)

    # Storing into Vector dataBase
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    print("Creating Vector Database")
    db = Chroma.from_documents(
    documents=chunk,
    embedding=embedding_model,
    persist_directory=persistent_directory
)
    db.persist()


## ALready Vectorized
else:
    print("Document Already Vectorized ... Aborting ...")
