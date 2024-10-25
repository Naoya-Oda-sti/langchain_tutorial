from langchain_openai import AzureChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0
)

messages = [
    SystemMessage(content="あなたは日本語を英語に翻訳するアシスタントです。"),
    HumanMessage(content="「私はプログラミングが大好きです。」を日本語から英語に翻訳してください。")
]
response = llm.invoke(messages)
print(response.content)
