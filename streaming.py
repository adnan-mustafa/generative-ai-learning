import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0,reasoning_effort="low")

for chunk in model.stream("Write a 100 line paragraph on parrots"):
    if chunk.text:
        print(chunk.text,end='|',flush=True)