import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
persistent_directory = os.path.join(parent_dir,"Chroma","db")

# Initializing the Embedding Model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2" )

# Initialize Chroma Instance

db = Chroma(
    embedding_function = embedding_model,
    persist_directory  = persistent_directory
)

retriever = db.as_retriever(
    search_type = "similarity_score_threshold",
    search_kwargs =  {"k":3,"score_threshold" :0.4}
)

query = input("Enter Query for similarity Search : ")
answer = retriever.invoke(query)

print(answer[0].page_content)


