from dotenv import load_dotenv
load_dotenv()

from langgraph.checkpoint.memory import InMemorySaver
in_memory_server = InMemorySaver()

from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
llm = ChatDeepSeek(model="deepseek-chat")
agent = create_agent(model=llm,checkpointer=in_memory_server)
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Hi,My name is Bob"
            }
        ]
    },
    {
        "configurable": {
            "thread_id": 1
        }
    }
)
from langchain.messages import AIMessage
for message in response.get("messages"):
    if isinstance(message, AIMessage):
        print(f"第一次对话结果:{message.content}")

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What am my name?"
            }
        ]
    },
    {
        
        "configurable": {
            "thread_id": 1
        }
    }
)
for message in response.get("messages"):
    if isinstance(message, AIMessage):
        print(f"第二次对话结果:{message.content}")