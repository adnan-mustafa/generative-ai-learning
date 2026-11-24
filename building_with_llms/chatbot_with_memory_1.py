#Seeing that a model remembers nothing

import truststore
truststore.inject_into_ssl()

from langchain.chat_models import init_chat_model

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

print(model.invoke("My name is Adnan").text)
print(model.invoke("What's my name?").text)