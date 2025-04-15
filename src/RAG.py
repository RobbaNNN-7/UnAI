import os 
from retrieval import get_context

from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from chat_test import chat
from chat_test import get_template
from model import model




#TODO:
####  GET THE context From Retrieval.py and pass it to Gemini LLM 
####  GET a Structured OUTPUT

# I have context , just need to pass the context to chat model to give me answer


# GET THE CONTEXT FROM THE QUERY 
# INSERT THE CONTEXT INTO CHAT
# GET THE STRUCTURED OUTPUT

while True:
    query = input("Your Query :   ")
    if query.lower() == "exit":
        break
    human_message = query
    context_docs = get_context(query)
    chat(human_message,context_docs,model)



