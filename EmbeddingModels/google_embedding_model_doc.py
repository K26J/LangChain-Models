from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2", dimensions=32)

document= ["My Name Is Keshav Joshi",
           "I am a Data Scientist",
           "I am a Python Developer",
           "I am a Machine Learning Engineer",
           "I am a Deep Learning Engineer",
           "I am a Data Analyst"
           ]

result= embedding.embed_documents(document)

print(str(result))