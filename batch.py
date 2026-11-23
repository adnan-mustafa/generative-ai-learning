import truststore
truststore.inject_into_ssl()

from langchain.chat_models import init_chat_model

model=init_chat_model("groq:openai/gpt-oss-120b",temperature=0,reasoning_effort="low")

questions = [
    "Why do parrots have colourful feathers? One sentence.",
    "How do airplanes fly? One sentence.",
    "What is quantum computing? One sentence.",
    "ps6 approximate date of release?",
    "What is langchain? One sentence."
]

replies=model.batch(questions, config={"max_concurrency":2})

for question,reply in zip(questions,replies):
    print(question)
    print("->",reply.text)