from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 

load_dotenv()

gemini_api_key = os.getenv("gemini_api_key")

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",temperature = 0, api_key = gemini_api_key)


from google import generativeai as genai


client = genai.Client(api_key="gemini_api_key")

result = client.models.embed_content(
    model="gemini-embedding-exp-03-07",
    contents="How does AlphaFold work?",
)

print(result.embeddings)