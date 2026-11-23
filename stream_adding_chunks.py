import truststore
truststore.inject_into_ssl()

from langchain.chat_models import init_chat_model

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

full=None

for chunk in model.stream("Say hi in three words"):
    full=chunk if full is None else full+chunk

print(type(full).__name__)
print(full.text)
print(full.usage_metadata)