import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv

load_dotenv()

from langchain.messages import SystemMessage,HumanMessage,AIMessage,ToolMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

# message=HumanMessage(content='Hello!',name='Alice',id='msg_123')
# print(message.type,message.name,message.id)
# print(message.content)

# messages=[
#     SystemMessage("You are a pirate. Reply with a poem of four lines."),
#     HumanMessage("Write a poem on artificial intelligence")
# ]

# print(model.invoke(messages).text)

## Giving the model a conversation history

# messages=[
#     HumanMessage("Hi, my name is Adnan"),
#     #AIMessage("Hello Adnan, I am an AI language model. How can I assist you today?"),
#     HumanMessage("What is my name and what does it mean?")
# ]

# print(model.invoke(messages).text)

## Passing a tool result back with ToolMessage

# messages=[
#     HumanMessage("What is the weather in San Francisco?"),
#     AIMessage(content="",tool_calls=[{"name":"get_weather","args":{"location":"San Francisco"},"id":"call_123"}]),
#     ToolMessage(content="Sunny 22 C",tool_call_id="call_123")
# ]

# print(model.invoke(messages).text)

## Building messages from a template

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a {role}. Answer in one sentence in {language}."),
    ("human","{question}")
])

values={"role":"pirate","question":"Why is the sky blue?","language":"English"}

for message in prompt.invoke(values).to_messages():
    print(message.type,"|",message.content)
print((prompt|model).invoke(values).text)