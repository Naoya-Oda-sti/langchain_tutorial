from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings
import os

# 環境変数の初期化
from dotenv import load_dotenv
load_dotenv()

loader = PyPDFLoader("https://blog.freelance-jp.org/wp-content/uploads/2023/03/FreelanceSurvey2023.pdf")
pages = loader.load_and_split()
print(pages[0])

chroma_index = Chroma.from_documents(pages, AzureOpenAIEmbeddings(
    model=os.getenv("AOAI_EMB_DEPLOYMENT"),
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
))
docs = chroma_index.similarity_search("「フリーランスのリモートワークの実態」について教えて。", k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content)