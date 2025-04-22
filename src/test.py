from model import model
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
# from langchain_core.memory import FirestoreChatMessageHistory
from chat_test import chat
import os 
import json
# from google.cloud import firestore

## Importing Json data from firebase_credentials file
# with open("firebase/firebase_credentials.json") as  f:
#     firebase_cred = json.load()

# PROJECT_ID = firebase_cred['project_id']
# SESSION_ID = "user_session_new"
# COLLECTION_ID = "chat_history"

## Loading ENV variables
# from dotenv import load_dotenv
# load_dotenv()

## Instantiating Models
# gemini_api_key = os.getenv("gemini_api_key")
# model = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash',temperature = 0,api_key = gemini_api_key)

# response_ = model.invoke("Who are you ?")
# if response_:
#     print(response_.content)
# else:
#     print("No Response")

# client = firestore.Client(projectID = PROJECT_ID)

# chat_history = FirestoreChatMessageHistory(
#     session_id = SESSION_ID,
#     collection = COLLECTION_ID,
#     client = client
# )


# from langchain.prompts import ChatPromptTemplate


# message = [
#     ("system","You are advisor of {designation} at nust "),
#     ("human","Tell me about your {query}")
# ]

# prompt_template = ChatPromptTemplate.from_messages(message)
# prompt = prompt_template.invoke({"designation":"scholarships","query":"JOB"})

# from query import query
# prompt_template = ChatPromptTemplate.from_messages(message)
# prompt =prompt_template.invoke({'desination':"scholarships","query":query})


from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

message = [
    ("system","You are an advisor at {name}"),
    ("human","Give me {number} of jokes")
]

prompt_template = ChatPromptTemplate.from_messages(message)

chain = prompt_template | model | StrOutputParser()

print(chain.invoke({"name":"NUST","number":"3"}))
