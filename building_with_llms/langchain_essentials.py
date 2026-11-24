import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

from langchain.chat_models import init_chat_model

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)
reply=model.invoke("a string, or a list of messages")
print(reply.text)