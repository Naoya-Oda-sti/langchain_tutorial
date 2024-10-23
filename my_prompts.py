from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
import os
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_DEPLOYMENT"),
    temperature=0
)

# systemメッセージプロンプトテンプレートの準備
template="あなたは {input_language} を {output_language} に翻訳するアシスタントです。"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# humanメッセージプロンプトテンプレートの準備
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# chatプロンプトテンプレートの準備
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# プロンプトテンプレートによるチャットモデルの呼び出し
response = llm.invoke(chat_prompt.format_prompt(
    input_language="日本語", 
    output_language="英語", 
    text="私はlangchainを使ったプログラミングが大好きです。"
).to_messages())
print(response.content)