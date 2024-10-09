# from langchain.chat_models import ChatOpenAI azure or openai
from langchain_openai import AzureChatOpenAI
# https://python.langchain.com/v0.2/docs/integrations/chat/azure_chat_openai/
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = AzureChatOpenAI(temperature=0)
output = chat.predict("日本の総理大臣は誰ですか？") 

print(output)
