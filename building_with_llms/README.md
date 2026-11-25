# Building with LLMs — LangChain & LangGraph Foundations

A structured collection of hands-on Python scripts exploring core LLM engineering patterns using **LangChain (`v1.4`)**, **LangGraph (`v1.2`)**, **Google Gemini**, and **Groq**. 

This module covers foundational primitives—from basic chat model initialization and LCEL runnables to token streaming, parallel batch processing, schema-enforced structured outputs, and stateful conversational memory.

---

## 📂 Repository Contents

### 1. Model Initialization, Prompts & LCEL
Core building blocks for invoking LLMs, formatting multi-turn prompt templates, and chaining components with the LangChain Expression Language (LCEL) pipe operator (`|`).

| Script | Description |
| :--- | :--- |
| `genai.py` | Direct baseline integration with the Google GenAI SDK (`gemini-3.5-flash-lite`). |
| `first_llm_app_google.py` | Initializing and invoking Google Gemini chat models via `langchain-google-genai`. |
| `first_llm_app_groq.py` | Initializing and invoking Groq-hosted models (`openai/gpt-oss-120b`) via `langchain-groq`. |
| `langchain_essentials.py` | Core `init_chat_model` usage and standard message invocation patterns. |
| `langchain_essentials_runnables_pipe_operator.py` | Composing prompts, models, and output parsers using LCEL `Runnable` chains (`\|`). |
| `messages_and_prompts.py` | Working with `SystemMessage`, `HumanMessage`, `AIMessage`, and dynamic `ChatPromptTemplate` placeholders. |

### 2. Streaming & Batch Execution
Optimizing latency and throughput for real-time user interfaces and multi-input workloads.

| Script | Description |
| :--- | :--- |
| `streaming.py` | Token-by-token response streaming using `.stream()` with flushed console output. |
| `stream_vs_invoke.py` | Side-by-side latency and UX comparison between blocking `.invoke()` and incremental `.stream()`. |
| `stream_adding_chunks.py` | Aggregating `AIMessageChunk` objects during streaming to reconstruct full response metadata. |
| `batch.py` | Executing multiple independent prompts concurrently using `.batch()`. |
| `batch_time_demo.py` | Benchmarking sequential `.invoke()` loops against parallel `.batch()` execution using Unix timestamps. |

### 3. Structured Outputs & Schema Validation
Enforcing deterministic JSON/object responses using Pydantic models and `TypedDict` schemas via `.with_structured_output()`.

| Script | Description |
| :--- | :--- |
| `pydantic_test.py` | Fundamentals of Pydantic `BaseModel` validation, type coercion, and `Field` descriptions. |
| `typeddict_test.py` | Lightweight structured extraction using Python `TypedDict` and `Annotated` field metadata. |
| `structured_output.py` | Binding schemas to chat models with `.with_structured_output()` for reliable data extraction. |
| `structured_output_nested_schemas.py` | Extracting hierarchical, multi-level objects using nested Pydantic schemas. |
| `structured_output_extraction_example_1.py` | Applied information extraction from unstructured text into validated domain models. |
| `structured_output_extraction_example_2.py` | Handling optional/missing fields (`Optional[...]`) and prompt constraints to prevent field misassignment. |

### 4. Stateful Chatbots & Memory Management
Progression from naive in-memory message lists to production-grade LangGraph checkpointing and context-window optimization.

| Script | Description |
| :--- | :--- |
| `chatbot_with_memory_1.py` | Basic multi-turn conversational loop demonstrating stateless vs. stateful model calls. |
| `chatbot_with_memory_keeping_history_list.py` | Manually managing conversation state by appending `HumanMessage` and `AIMessage` history to a Python list. |
| `chatbot_with_memory_checkpointer.py` | Thread-scoped persistent conversation memory powered by LangGraph's `InMemorySaver` checkpointer. |
| `chatbot_with_memory_trimming_summarizing_history.py` | Managing context window limits by trimming older messages and summarizing prior conversation turns. |
| `chatbot_with_memory_trimming_inside_agent.py` | Implementing automatic message trimming middleware/hooks inside an agent workflow before model invocation. |

*(Note: `temp.py` is a scratchpad script used for quick local experiments.)*

---

## ⚙️ Setup & Local Execution

### 1. Prerequisites
* **Python 3.12+**
* API keys from [Google AI Studio](https://aistudio.google.com/) (`GOOGLE_API_KEY`) and [Groq Console](https://console.groq.com/) (`GROQ_API_KEY`).

### 2. Installation
Clone the repository and install dependencies into a virtual environment:

```bash
git clone [https://github.com/adnan-mustafa/generative-ai-learning.git](https://github.com/adnan-mustafa/generative-ai-learning.git)
cd generative-ai-learning
python -m venv .venv