import truststore
truststore.inject_into_ssl()

from typing_extensions import Annotated, TypedDict

from langchain.chat_models import init_chat_model

class MovieDict(TypedDict):
    title: Annotated[str, ..., "The title of the movie"]
    year: Annotated[int, ..., "The year the movie was released"]

model = init_chat_model("groq:openai/gpt-oss-120b", temperature=0)
result = model.with_structured_output(MovieDict).invoke("Provide details about the movie Inception")
print(type(result).__name__, result)

