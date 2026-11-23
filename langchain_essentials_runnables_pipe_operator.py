import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model=init_chat_model("groq:openai/gpt-oss-20b",temperature=0)
print(type(model).__module__,type(model).__name__)

prompt=ChatPromptTemplate.from_messages([("system","Answer in {language}."), ("human","{question}")])

chain=prompt|model|StrOutputParser()

print(chain.invoke({"language":"Spanish","question":"What is your name?"}))

