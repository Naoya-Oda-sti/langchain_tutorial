# from langchain.llms import OpenAI azure or openai
from langchain_community.llms.openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = AzureOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
)

output = llm.predict("日本の総理大臣は誰ですか？")

print(output)

# 元のコード
# from langchain.llms import OpenAI

# llm = OpenAI(temperature=0.9)
# output = llm.predict("日本の総理大臣は誰ですか？")

# print(output)