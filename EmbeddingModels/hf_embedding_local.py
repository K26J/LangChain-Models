from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

documents= ["My Name Is Keshav Joshi",
           "I am a Data Scientist"]

result= embedding.embed_documents(documents)

print(str(result))