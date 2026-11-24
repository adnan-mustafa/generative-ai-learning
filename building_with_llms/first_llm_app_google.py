import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model=init_chat_model("google_genai:gemini-4-hydrogen",temperature=0)
#model=init_chat_model("groq:openai/gpt-oss-20b",temperature=1)


reply=model.invoke("Why do parrots talk? Answer in two sentences.")

print(reply.text)
print(type(reply).__name__)
print(reply.usage_metadata)
print(reply.response_metadata["model_name"],reply.response_metadata["finish_reason"])

# while True:
#     question=input("You:")
#     if question in ("quit","exit"):
#         break
#     print("Bot:",model.invoke(question).text)

for question in ["What is the capital of France?","And what is its population?","What is its flag colour?"]:
    print("You:",question)
    print("Bot:",model.invoke(question).text)