from store_FAISS import vector_store,embedding
from langchain.vectorstores import FAISS
import os
from dotenv import load_env
from pinecone import Pinecone

load_env()


pine_cone_api_key = os.getenv("pine_cone_api_key")
pc = Pinecone(api_key = pine_cone_api_key )
## REFERENCING FAISS AND COLLECTING THE RELEVENT QUERY

faiss_index_path = "faiss_index"

try:
    vector_store.load_local(faiss_index_path,embedding)
except Exception as e:
    print(f"Coudld not load : {faiss_index_path} , With Exception {e}")


query = "What Does NUST Stand For ?"

retriever = vector_store.as_retriever()

retriever_docs = retriever.get_relevant_documents(query)

if retriever_docs:
    print(retriever_docs[0].page_content)
else:
    print("Empty")



    