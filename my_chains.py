from langchain_community.llms.openai import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

import os

llm = AzureOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0.1
)

# 最初のプロンプトテンプレートの作成
prompt_1 = PromptTemplate(
    input_variables=["product"],
    template="{product}を作る会社の社名として、何かいいものはないですか？日本語の社名でお願いします。",
)

# 最初に実行する LLM チェーンを定義
# 会社名を考えてもらう
chain_1 = LLMChain(llm=llm, prompt=prompt_1)

# 次のプロンプトテンプレートの作成
prompt_2 = PromptTemplate(
    input_variables=["company_name"],
    template="{company_name}という会社名の企業のキャッチコピーを考えてください。",
)

# 次に実行する LLM チェーンを定義
# キャッチコピーを考えてもらう
chain_2 = LLMChain(llm=llm, prompt=prompt_2)

# 二つの LLM チェーンを連結
overall_chain = SimpleSequentialChain(chains=[chain_1, chain_2], verbose=True)

# 連結してできたチェーンを実行
chatchphrase = prediction = overall_chain.run("カラフルな靴下")
print(chatchphrase)