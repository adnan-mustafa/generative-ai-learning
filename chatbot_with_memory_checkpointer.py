#Saving a conversation per user with a checkpointer

import truststore
truststore.inject_into_ssl()

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)
agent=create_agent(model, tools=[], system_prompt="You are a concise assistant.", checkpointer=InMemorySaver())

def say(text,thread):
    config={"configurable":{"thread_id": thread}}
    result=agent.invoke({"messages":[{"role":"user","content":text}]},config)
    return len(result["messages"]),result["messages"][-1].text

print("adnan:",say("My name is Adnan and I live in Kolkata.","adnan"))
print("adnan:",say("What is my name?","adnan"))
print("sam:",say("What is my name?","sam"))
print("adnan:",say("Where do I live?","adnan"))
