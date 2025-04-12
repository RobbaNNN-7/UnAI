from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from model import model

def chat(model = model):
    chat_history = []


    system_message = SystemMessage(content = "You are A Software Engineer Working in Apple")
    chat_history.append(system_message)

    while True:
        human_message = input("Your Query : ")
        if human_message.lower() == 'exit':
            break
        chat_history.append(HumanMessage(content = human_message))
        response= model.invoke(chat_history)

        AI_message = response.content

        chat_history.append(AIMessage(content = AI_message))
        print(AI_message)
        

    return chat_history



## firebase
# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)




