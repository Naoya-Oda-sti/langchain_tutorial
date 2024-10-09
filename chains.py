from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

chat = AzureChatOpenAI(temperature=0)
template = PromptTemplate.from_template("{keyword}を解説するQiita記事のタイトル案は?")

chain = LLMChain(llm=chat, prompt=template)
output = chain.run("LangChain")

print(output)
