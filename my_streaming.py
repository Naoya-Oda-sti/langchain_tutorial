# from langchain.callbacks.base import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_openai import AzureChatOpenAI
import os
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0


)

# チャットモデルの呼び出し
chunks = []
for chunk in llm.stream("今後の日本の将来について４００文字程度で述べてください。"):
    chunks.append(chunk)
    print(chunk.content, end="", flush=True)

#streamingを用いない場合、４００文字がそろってから出力される
# response = llm.invoke("今後の日本の将来について４００文字程度で述べてください。")
# print(response.content)