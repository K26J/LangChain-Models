from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm= HuggingFacePipeline(
    model_id= "LiquidAI/LFM3-1.7B",
    task= "text-generation",
    pipeline_kwargs= {"max_new_tokens": 100, " temperature": 0.7}
)

model= ChatHuggingFace(llm=llm)
result= model.invoke("What is the capital of India?")
print(result.content)