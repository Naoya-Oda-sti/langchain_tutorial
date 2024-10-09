from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template("{keyword}を解説するQiita記事のタイトル案は?")
prompt = template.format(keyword="kaggle")

chat = AzureChatOpenAI(temperature=0)
output = chat.predict(prompt)

print(output)
