import truststore
truststore.inject_into_ssl()

from langchain.agents import create_agent
from langchain.agents.middleware import before_model
from langchain.chat_models import init_chat_model
from langchain.messages import RemoveMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import REMOVE_ALL_MESSAGES

# @before_model
# def keep_last_four(state,runtime):
#     messages= state["messages"]
#     if len(messages)<=4:
#         return None
#     return {"messages":[RemoveMessage(id=REMOVE_ALL_MESSAGES),*messages[-4:]]}

# model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)
# agent=create_agent(model,tools=[],middleware=[keep_last_four],checkpointer=InMemorySaver())
# config={"configurable":{"thread_id":"t1"}}

# for text in ["My name is Adnan.","I live in Kolkata","I like football","I have a cat called Kitty","What is my name?"]:
#     result=agent.invoke({"messages":[{"role":"user","content":text}]},config)
#     print(len(result["messages"]), "messages |", result["messages"][-1].text[:60].replace("\n",""))


##Practicing with keeping last 10 messages below:
@before_model
def keep_last_ten(state,runtime):
    messages= state["messages"]
    if len(messages)<=10:
        return None
    return {"messages":[RemoveMessage(id=REMOVE_ALL_MESSAGES),*messages[-10:]]}

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0.9)
agent=create_agent(model,tools=[],middleware=[keep_last_ten],checkpointer=InMemorySaver())
config={"configurable":{"thread_id":"t1"}}

for text in ["My name is Adnan.","I live in Kolkata","I like football","I have a cat called Kitty","What is my name?"]:
    result=agent.invoke({"messages":[{"role":"user","content":text}]},config)
    print(len(result["messages"]), "messages |", result["messages"][-1].text[:60].replace("\n",""))
