"""
- Data is in Books directory. It's Corrosponding MetaData is Dumped into JSON folder 
- TODO:
        VECTORIZE ALL the PATHS IN JSON FOLDER , and Store them in ChromaDB
        WITH Metadata as prescribed in JSON folder

- NOTE:
        Single File Vectorization is Already Handled in vector_data_base.py
        This Script Vectorizes Entire Paths in JSON FOLDER
"""

import os 
import json
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma 
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

with open("metadata/university_metadata.json","r") as f:
    metadata = json.load(f)


# # TODO: GET PATHS FROM THE JSON , AND VECTORIZE

current_dir = os.path.dirname(os.path.abspath(__file__)) #scripts
parent_dir = os.path.dirname(current_dir) #UnAI
persistent_directory = os.path.join(parent_dir,"db","Chroma") #UnAI/db/Chroma
file_paths = []

for data in metadata:
    uni_data = metadata.get(data,[]) # [] includes the documents for a specific university
    for doc in uni_data:
        """ Now file_paths has all the Paths """
        file_paths.append(doc["path"])


""" Starting Vectorization Process """

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma(
    embedding_function=embedding_model,
    persist_directory=persistent_directory
)

print(" Creating/Loading Chroma Database ")

uni_name = ""
uni_doc_type = ""
uni_doc_path = ""

for path in file_paths:

    """ Before Splitting the Data , We Need to Update the MetaData """

    for data in metadata:
        uni_data = metadata.get(data,[])
        uni_name = data
        for docs in uni_data:
            
            # Initialzing Variables
            uni_doc_type = docs["type"]
            uni_doc_path = docs["path"]

            # Loading Document and Updating Metadata
            loader = PyPDFLoader(path)
            document = loader.load()

            for docs in document:
                docs.metadata.update(
                    {
                        "university_name" : uni_name,
                        "document_type"   : uni_doc_type,
                        "document_path"   : uni_doc_path 
                    }
                )

    # Splitting the Documents
    textSplitter = RecursiveCharacterTextSplitter(chunk_size = 1400,chunk_overlap = 400)
    chunks = textSplitter.split_documents(document)

    # Vectorizing
    db.add_documents(
        documents = chunks
    )
    # db.persist()


print("Finished vectorizing and adding documents.")





