import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
load_dotenv()

#Using init_chat_model function to initialize the model
from langchain.chat_models import init_chat_model
model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

reply=model.invoke("Why do parrots talk? Answer in two sentences.")

print(reply.text)
print(type(reply).__name__)
print(reply.usage_metadata)
print(reply.response_metadata["model_name"],reply.response_metadata["finish_reason"])

##Using provider's class directly

from langchain_groq import ChatGroq

model=ChatGroq(model_name="openai/gpt-oss-120b",temperature=0)

reply=model.invoke("Why do parrots talk? Answer in two sentences.")

print(reply.text)
print(type(reply).__name__)
print(reply.usage_metadata)
print(reply.response_metadata["model_name"],reply.response_metadata["finish_reason"])