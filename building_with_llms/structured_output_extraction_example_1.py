import truststore
truststore.inject_into_ssl()

import os
from pydantic import BaseModel,Field
from langchain.chat_models import init_chat_model

from typing import Literal

class Ticket(BaseModel):
    customer: str = Field(description="Full name of the customer")
    order_id: str = Field(description="The order number")
    product: str
    category: Literal["defective","late","wrong_item","other"]
    refund_requested: bool
    amount: float = Field(description="Amount paid")
    sentiment: Literal["positive","negative","neutral"]

email= """Hi, this is Priya Nair. I ordered a standing desk (order #48213) two weeks ago
and the left leg arrived bent. I paid 389.99 and I would like a refund, not a replacement."""

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)
ticket=model.with_structured_output(Ticket).invoke(email)
print(repr(ticket))
print(ticket.amount*2)
