from langchain_openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = AzureOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    # gpt35_turbo以前のモデル（text completion）を選択
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0.9
)

output = llm.predict("日本の総理大臣は誰ですか？")

print(output)