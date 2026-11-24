#Keeping a history list

import truststore
truststore.inject_into_ssl()

from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage,HumanMessage,AIMessage,ToolMessage

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

history=[SystemMessage("You are a concise assistant")]

def chat(text):
    history.append(HumanMessage(text))
    reply=model.invoke(history)
    history.append(reply)
    return reply

for text in ["My name is Adnan","I like football","What is my name?"]:
    reply=chat(text)
    print(f"{len(history):>2}) messages | {reply.usage_metadata['input_tokens']:>3} input tokens | {reply.text}")
