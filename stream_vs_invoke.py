import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
load_dotenv()

import time

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0,reasoning_effort="low")
question="Write a 1000 word paragraph on parrots"

start=time.time()
first=None
for chunk in model.stream(question):
    if chunk.text and first is None:
        first=time.time()-start
print(f"stream: first text after {first:.2f}s, finished after {time.time()-start:.2f}s")

start=time.time()
reply=model.invoke(question)
print(f"invoke: {len(reply.text.split())} words, all there after {time.time()-start:.2f}s")

