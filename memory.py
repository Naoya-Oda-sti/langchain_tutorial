from langchain import ConversationChain
from langchain_community.llms.openai import AzureOpenAI

llm = AzureOpenAI(
    azure_endpoint="https://chatbot-poc-oai-oda.openai.azure.com/",
    api_key="7758f8c0f4c746578cf57825aca7c34e",
    api_version="2024-07-01-preview",
    openai_api_type="azure",
    azure_deployment="gpt-35" )

conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.run("私は日本人です。何を聞いても日本語で答えてください。")
output = conversation.run("Who is the prime minister of Japan?")

print(output)