from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader
from langchain_community.llms.openai import AzureOpenAI
import os

# 環境変数の初期化
from dotenv import load_dotenv
load_dotenv()

llm = AzureOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
)


long_text = """
GPT-4は、OpenAIが開発したAI技術であるGPTシリーズの第4世代目のモデルです。

自然言語処理(NLP)という技術を使い、文章の生成や理解を行うことができます。

これにより、人間と同じような文章を作成することが可能です。

GPT-4は、トランスフォーマーアーキテクチャに基づいており、より強力な性能を発揮します。

GPT-4は、インターネット上の大量のテキストデータを学習し、豊富な知識を持っています。

しかし、2021年9月までの情報しか持っていません。

このモデルは、質問応答や文章生成、文章要約など、様々なタスクで使用できます。

ただし、GPT-4は完璧ではありません。

時々、誤った情報や不適切な内容を生成することがあります。

使用者は、その限界を理解し、

適切な方法で利用することが重要です。
"""
print(len(long_text))
with open("./long_text.txt", "w") as f:
    f.write(long_text)
    f.close()

loader = TextLoader('./long_text.txt')

text_splitter = CharacterTextSplitter(
    separator = "\n\n",
    chunk_size = 100,
    chunk_overlap = 0,
    length_function = len,
)

embeddings = AzureOpenAIEmbeddings(
    model=os.getenv("AOAI_EMB_DEPLOYMENT"),
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    openai_api_key=os.getenv("AOAI_API_KEY"),
    chunk_size=10  
)

index = VectorstoreIndexCreator(
    vectorstore_cls=Chroma,
    embedding=embeddings,
    text_splitter=text_splitter,
).from_loaders([loader])

query = "Q1. インターネット上の何のデータを使って、学習しているの？"
print(f"\n\n{query}")
answer = index.query(query,llm=llm)
print(answer)

answer_with_sources = index.query_with_sources(query,llm=llm)
print(answer_with_sources)

query = "Q2. GPT4は第何世代のモデル？"
print(f"\n\n{query}")
answer = index.query(query,llm=llm)
print(answer)

answer_with_sources = index.query_with_sources(query,llm=llm)
print(answer_with_sources)