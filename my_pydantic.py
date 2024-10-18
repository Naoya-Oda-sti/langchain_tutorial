# 4o系じゃないと実行不可？
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel
import json
import os

# 環境変数の初期化
from dotenv import load_dotenv
load_dotenv()

class Output(BaseModel):
    """Output Structure"""
    city: str
    reason: str
    

model = AzureChatOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_4o_DEPLOYMENT"),
    temperature=0.7
).bind(seed=0)
model = model.with_structured_output(Output)

output = model.invoke('世界で住みやすい都市を理由をつけて教えて下さい。')
print(output)