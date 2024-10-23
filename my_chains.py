# 【Waring!】 chainは非推奨になり、代替機能も現状見つからないため後回し
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RunnableSequence 
import os

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0
)

template = PromptTemplate.from_template("{keyword}を解説するQiita記事のタイトル案は?")

# LLMChainの代わりにRunnableSequenceを使用
chain = RunnableSequence([template, llm])

result = chain.invoke({"keyword": "kaggle"})
print(result)
