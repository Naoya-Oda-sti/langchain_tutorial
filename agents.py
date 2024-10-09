# エラーが発生してるので修正をお願いします
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_community.llms.openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = AzureOpenAI(
    azure_endpoint=os.getenv("AOAI_ENDPOINT"),
    api_key=os.getenv("AOAI_API_KEY"),
    api_version=os.getenv("AOAI_API_VERSION"),
    openai_api_type="azure",
    azure_deployment=os.getenv("AOAI_35_DEPLOYMENT"),
)
tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

try:
    output = agent.run("今日の富山県の最高気温は摂氏何度ですか？またその値を2乗してください。")
    print(output)
except ValueError as e:
    print(f"エラーが発生しました: {e}")
