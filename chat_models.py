# AzureOpenAIではなくAzureChatOpenAIを使う
# https://stackoverflow.com/questions/78656632/the-completion-operation-does-not-work-with-the-specified-model-gpt-4
from langchain_openai import AzureChatOpenAI
import os

chat = AzureChatOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0
)
output = chat.predict("あなたの名前を教えてください") 

print(output)
