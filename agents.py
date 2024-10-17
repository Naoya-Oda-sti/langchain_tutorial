# gpt3.5でやること
from langchain.agents import AgentType, initialize_agent, load_tools
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

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

output = agent.run("今日の新宿区の最高気温の摂氏温度の平方根はいくつ？")

print(output)