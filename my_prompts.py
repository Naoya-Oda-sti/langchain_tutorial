from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
import os

template = PromptTemplate.from_template("{keyword}を解説するQiita記事のタイトル案は?")
prompt = template.format(keyword="kaggle")

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0
)
output = llm.predict(prompt)

print(output)
