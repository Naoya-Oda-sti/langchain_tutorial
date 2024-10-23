# gpt4oでは使えない
from langchain import ConversationChain
from langchain_community.llms.openai import AzureOpenAI
import os

llm = AzureOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0
)

conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.run("私の妻の名前は花子です")
# output = conversation.run("私の妻の名前は何でしょうか？")

print(output)