# Context_Memory_Aware_Agent_7
A context-aware Agentic AI system built using LangChain and OpenAI. This project demonstrates how agents can retain conversational memory across multiple prompts using ConversationBufferMemory. The system evolves from simple stateless prompts to multi-turn, memory-rich dialogue, enabling intelligent chaining of logic and code generation.


# 🧠 Context-Aware Agent with Memory (LangChain + OpenAI)

This project demonstrates a **memory-enabled AI assistant** using [LangChain](https://www.langchain.com/) and OpenAI's GPT models. The agent retains previous interactions using `ConversationBufferMemory`, allowing it to understand references like _"the previous function"_ or _"use what we did earlier"_ — bringing contextual intelligence to multi-turn interactions.

---

## 📚 ConversationBufferMemory

### 🎯 Goal:
Build an agent that remembers previous inputs and uses them to respond intelligently in future prompts.

---

## 🧠 Features

- Implements LangChain's `ConversationBufferMemory`
- Uses `ConversationChain` for prompt + memory orchestration
- Tracks multi-turn context automatically
- Includes token usage logging via OpenAI callback
- Example of using memory to build on prior code generation

---

## 💻 Sample Interaction

```text
User: Write a Python function to reverse a string
AI: def reverse_string(s): return s[::-1]

User: Now write a function to check if a string is a palindrome using the previous one
AI: def is_palindrome(s): return s == reverse_string(s)


## 🛠 Tech Stack**
Python 3.9+

LangChain

OpenAI GPT-3.5 Turbo

ConversationBufferMemory for in-session memory

Token usage callback for cost analysis


## 🚀 How to Run

1. Install dependencies

pip install langchain openai


2. Set your OpenAI API key

export OPENAI_API_KEY="your-key-here"


3. Run the script

python main.py


