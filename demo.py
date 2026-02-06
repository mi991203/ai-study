import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam, ChatCompletionAssistantMessageParam

load_dotenv()

llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)
response = llm.chat.completions.create(
    model="deepseek-chat",
    messages=[
        ChatCompletionSystemMessageParam(role="system", content="You are a useful coder"),
        ChatCompletionUserMessageParam(role="user", content="Please write quick sort code"),
        ChatCompletionAssistantMessageParam(role="assistant", content="Please generate by python")
    ],
    max_tokens=1024,
    temperature=0.7,
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
