import truststore
truststore.inject_into_ssl()

from pydantic import BaseModel,Field
from langchain.chat_models import init_chat_model

class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    director: str = Field(description="The director of the movie")
    rating: float = Field(description="The movie's rating out of 10")

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0)
structured=model.with_structured_output(Movie, include_raw=True)
result=structured.invoke("Provide details about the movie Inception")


print(repr(result["parsed"]))
print(type(result["parsed"]).__name__,result["parsing_error"])
print(result["raw"].tool_calls[0]["name"],result["raw"].tool_calls[0]["args"])
