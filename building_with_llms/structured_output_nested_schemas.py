import truststore
truststore.inject_into_ssl()

from pydantic import BaseModel,Field
from typing import Literal,Optional

from langchain.chat_models import init_chat_model

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

class Item(BaseModel):
    name: str
    quantity: int

class Order(BaseModel):
    customer: str
    items: list[Item]

order=model.with_structured_output(Order,method="json_schema").invoke("Maya wants 2 notebooks and 3 pens, plus one stapler.")

print(order)
print(sum(item.quantity for item in order.items),"items in total")