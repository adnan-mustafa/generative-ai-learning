import truststore
truststore.inject_into_ssl()

from dotenv import load_dotenv
import os

from langchain.chat_models import init_chat_model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

for name in ["groq:openai/gpt-oss-120b", "groq:openai/gpt-oss-20b", "google_genai:gemini-3.5-flash-lite"]:
    model=init_chat_model(name)
    print(name,"->",model.invoke("Reply with the single word: pong").text)

embedder=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
print(len(embedder.embed_query("hello")),"numbers in one embedding")

import sys

print(sys.version.split()[0])
print("ok" if sys.version_info>=(3,10) else "too old")

from importlib.metadata import version

for name in ["langchain","langchain-core", "langchain-groq","langchain-google-genai", "langgraph","python-dotenv"]:
    print(name,version(name))
