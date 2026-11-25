from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings= GoogleGenerativeAIEmbeddings(model="gemini-embedding-2",dimesions= 32)

result= embeddings.embed_query("My Name Is Keshav Joshi")

print(str(result))
