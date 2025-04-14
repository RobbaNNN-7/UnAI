import os
import json
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter


file_path = os.path.abspath("books/UG-Student-Handbook.pdf")
books_dir = os.path.dirname(file_path)  

files = os.listdir(books_dir)

university_metadata = {}


for file in files:
    if file.endswith(".pdf"):

        """ Stripping University Name and Data

        E.g. Stored as -- NUST-PROSPECTUS.pdf
        Final Result --   NUST,PROSPECTUS ("-" acts as a delimiter)
        
        """

        fileData = file.split("-")
        universityName = fileData[0] if len(fileData) > 0  else "unknown"
        universityDocType = fileData[1] if len(fileData) > 1 else "unknown"
        
        metadata = {
            "filename" : file,
            "type"     : universityDocType,
            "path"     : os.path.abspath(file)
        }
        
        if universityName not in university_metadata:
            university_metadata[universityName] = []
        
        university_metadata[universityName].append(metadata)
    


with open("university_metadata.json","w") as file:
    json.dump(university_metadata,file,indent = 4)










