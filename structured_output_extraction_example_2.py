import truststore
truststore.inject_into_ssl()

import os

from pydantic import BaseModel,Field
from typing import Literal,Optional

from langchain.chat_models import init_chat_model

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)

class Ticket(BaseModel):
    customer: str
    order_id: str
    product: str
    category: Literal["defective","late","wrong_item","other"]
    refund_requested: bool
    amount: float

class TicketOptional(BaseModel):
    customer: str
    order_id: Optional[str]=Field(None,description="The order number, or null if the message has none")
    product: str
    category: Literal["defective","late","wrong_item","other"]
    refund_requested: bool
    amount: Optional[float]=Field(None,description="Amount paid, or null if not stated")

email="""अवगत कराना है कि हमारा इनवर्टर एक हफ्ते से खराब है इंजीनियर को कॉल करने के बाद भी इंजीनियर नहीं आए और हमने शिकायत दर्ज कराई ऑनलाइन लेकिन कुछ नहीं हुआ। Exide Home inverter, 10 February 2026, wa.me/917044000000?text=Hi
Purchase City	Balrampur
Phone no. 7696339668
Grievance Number	10088670"""

try:
    print(model.with_structured_output(Ticket).invoke(email))
except Exception as error:
    print(type(error).__name__,str(error)[:80])

print(model.with_structured_output(TicketOptional).invoke(email))