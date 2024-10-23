from langchain.embeddings import AzureOpenAIEmbeddings
import os

# 環境変数の初期化
from dotenv import load_dotenv
load_dotenv()

embeddings = AzureOpenAIEmbeddings(
    model=os.getenv("AOAI_EMB_DEPLOYMENT"),
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    openai_api_key=os.getenv("AOAI_API_KEY"),
    chunk_size=10  
)
query_result = embeddings.embed_query("ITエンジニアについて30文字で教えて。")

print("ベクトル：",query_result)
print("ベクトルの次元数：",len(query_result))