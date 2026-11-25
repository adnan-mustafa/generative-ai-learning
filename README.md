# Generative & Agentic AI Engineering

A hands-on engineering repository documenting my end-to-end journey into **Generative AI, LLM Application Development, RAG Pipelines, and Stateful Agentic Workflows** using Python, **LangChain (`v1.4`)**, and **LangGraph (`v1.2`)**.

Every module contains clean, runnable Python implementations tested across multiple model providers (**Google Gemini** and **Groq**), focusing on production patterns such as schema-enforced structured outputs, latency optimization, context-window management, and resilient SSL/environment configuration.

---

## 🗺️ Repository Structure & Learning Roadmap

| Module | Directory | Status | Key Concepts Covered |
| :--- | :--- | :---: | :--- |
| **01. Building with LLMs** | [`building_with_llms/`](./building_with_llms) | ✅ Completed | Model initialization (`init_chat_model`), LCEL runnables (`\|`), streaming vs. batching, Pydantic/`TypedDict` structured outputs, and LangGraph checkpointed memory (`InMemorySaver`). |
| **02. RAG & Vector Search** | `rag_pipelines/` | 🚧 Upcoming | Document loaders, semantic chunking, `gemini-embedding-001` embeddings, vector stores, hybrid retrieval, and citation grounding. |
| **03. Tool Calling & Agents** | `agentic_workflows/` | 🚧 Upcoming | Custom `@tool` definitions, ReAct loops, human-in-the-loop (HITL) interrupts, and multi-step state graphs in LangGraph. |
| **04. Multi-Agent & Production Ops** | `multi_agent_systems/` | 📋 Planned | Supervisor/worker orchestration, LangSmith tracing, automated LLM-as-a-judge evaluation, and Dockerized API deployment. |

---

## 🛠️ Tech Stack & Models

* **Core Frameworks:** `langchain==1.4.3`, `langgraph==1.2.14`
* **Model Providers & Integrations:**
  * **Google GenAI (`langchain-google-genai==4.4.0`):** `gemini-3.5-flash-lite`, `gemini-embedding-001`
  * **Groq (`langchain-groq==1.1.3`):** `openai/gpt-oss-120b`, `openai/gpt-oss-20b`
* **Data Validation & Typing:** `pydantic` (`BaseModel`, `Field`), `typing_extensions` (`TypedDict`, `Annotated`)
* **Environment & Networking:** Python 3.12, `uv` / `pip`, `python-dotenv==1.2.4`, `truststore` (native OS certificate store injection for corporate TLS/SSL inspection)

---

## 🚀 Quickstart

### 1. Clone the Repository
```bash
git clone [https://github.com/adnan-mustafa/generative-ai-learning.git](https://github.com/adnan-mustafa/generative-ai-learning.git)
cd generative-ai-learning