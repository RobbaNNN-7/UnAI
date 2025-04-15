from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Setup paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
persistent_directory = os.path.join(parent_dir, "db", "Chroma")

# Initialize the embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize Gemini
gemini_api_key = os.getenv("gemini_api_key")
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, api_key=gemini_api_key)

# Initialize Chroma
db = Chroma(
    embedding_function=embedding_model,
    persist_directory=persistent_directory
)

# Define retriever
retriever = db.as_retriever(search_kwargs={"k": 5})

# Define prompt template
template = """
You are a helpful assistant that provides information about universities.
Answer the question based ONLY on the following context:

{context}

Question: {question}

If the information is not present in the context, say "I don't have enough information about that in the provided documents."
"""
prompt = ChatPromptTemplate.from_template(template)

# Create RAG chain
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# Run the chain
answer = rag_chain.invoke("What programs does NUST offer for engineering?")
print(answer)