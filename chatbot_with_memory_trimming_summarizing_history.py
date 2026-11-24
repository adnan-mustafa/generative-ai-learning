#Trimming and summarising an eight-message history

import truststore
truststore.inject_into_ssl()

from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage,HumanMessage,AIMessage,ToolMessage,trim_messages

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

history=[
    SystemMessage("You are a concise assistant"),
    HumanMessage("My name is Adnan and I live in Kolkata."),
    AIMessage("Nice to meet you, Adnan."),
    HumanMessage("I like football."),
    AIMessage("Football is a great game."),
    HumanMessage("I have a cat called Kitty."),
    AIMessage("Kitty is a lovely name"),
    HumanMessage("What is my name?")
]

kept=trim_messages(history,max_tokens=4,strategy="last",token_counter="approximate",include_system=True,start_on="human")
print([m.type for m in kept])

older=history[1:5]

summary=model.invoke([SystemMessage("Summarize the conversation in one sentence."),*older]).text

compact=[history[0],HumanMessage(f"Here is a summary of the conversation to date: {summary}"),*history[5:]]

print("summary: ",summary)
print("full: ",model.invoke(history).text)
print("trimmed: ",model.invoke(kept).text)
print("summarized: ",model.invoke(compact).text)